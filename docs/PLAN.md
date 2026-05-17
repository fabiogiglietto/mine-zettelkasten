# Plan: `fg-zettelkasten` — a topic-anchored Obsidian knowledge base

## Context

`toread` (Paperpile → enriched JSON Feed) and `research-radio` (feed → AI podcast)
form a pipeline with no place to *read, describe, and connect* the papers.
`fg-zettelkasten` is a new standalone project that builds an Obsidian vault: one
richly-described note per paper, organised under a **topic register derived from the
user's actual research agenda**, densely cross-linked, modelled on the Niklas Luhmann
Archive. It also emits a **shared structured summary** artifact that `research-radio`
will later consume so the expensive paper-comprehension pass happens once.

Verified pipeline facts:
- `toread/output/feed.json` — JSON Feed 1.1, **167 items today**; every item id is
  `bibtex:AuthorYear-xx` (even with a DOI). Item fields: `id`, `title`,
  `content_text` (abstract), `date_published`, `_discovery_date`, `_date_estimated`,
  `url`, `external_url`, `authors`, `tags`, `content_html`, `_academic`.
- `research-radio/docs/episodes.json` — keyed by the **same `bibtex:` id**; carries
  `audio_url`. → join key across all projects is `bibtex:AuthorYear-xx`, no normalisation.
- `research-radio/src/drive_client.py` already finds & extracts PDF text from the
  Paperpile Google Drive folder (`find_pdf`, `download_pdf`,
  `get_pdf_text(paper, max_chars=80000)`); it expects a `Paper` with single-string
  first-author / year / title.
- `fabiogiglietto.github.io` (Jekyll) publishes structured research-agenda data:
  `_data/projects.yml` (active funded projects: MINE, PROMPT, vera.ai),
  `_data/publications.yml`, `_data/teaching.yml`, `_data/news.yml`,
  `scripts/config.js` (`researchInterests`, `expertise`), `scripts/data/bio-seed.md`.

## Decisions (from interview)

- Language **Python**; own git repo at `/home/fg/projects/fg-zettelkasten`, **not published**.
- Inputs are consumed **live from published URLs** (raw GitHub), never local working copies:
  - toread feed: `raw.githubusercontent.com/fabiogiglietto/toread/main/output/feed.json`
  - research-radio episodes: research-radio's published `docs/episodes.json`
  - topic signals: the published `fabiogiglietto.github.io` repo (data files below).
- **LLM strategy = capability split.** Claude does all read/understand/write work;
  Gemini is kept only for research-radio's TTS (no Claude equivalent exists).
- Per-paper notes: **Claude (Opus) summary from full PDF text**; PDFs via the ported
  Drive client; abstract-only fallback when no PDF (flagged in frontmatter).
- Themes: **topic-anchored**, not free clustering — anchored to the user's research
  agenda extracted from github.io, with **emergent sub-themes** allowed for papers that
  fit no anchor (flagged as candidate new topics).
- Luhmann Archive model: **topic register entry points**, **dense cross-reference web**,
  **structure/hub notes**. (No Luhmann-style branching note IDs.)
- Vault layout: flat `Papers/` + `Topics/` register MOCs + `Structures/` hub notes.
- Automation: GitHub Actions cron; stable register, incremental assignment, periodic
  full re-cluster.
- research-radio refactor to consume the shared summary is a **follow-up** after the
  vault ships (designed for now, implemented later).

## LLM provider strategy (whole pipeline)

A single provider is impossible: research-radio's multi-speaker TTS is Gemini-native
and Claude has no TTS. So the split is by **capability**, not by project:

- **Claude** — comprehend the paper and write about it. Done **once** in fg-zettelkasten.
- **Gemini** — speech synthesis only.

The shared artifact (`data/summaries/<key>.json`) carries the **structured summary
only** — key claims, methods, findings, contributions, framing. The extracted full PDF
text is **transient**: used in-memory during summarization, optionally cached in a
gitignored `data/.cache/`, never committed. Reason: the fg-zettelkasten repo is **private**
(see below) and Paperpile publisher PDFs are not redistributable, so committing full
text is a copyright problem; a transformative structured summary is safe.

When research-radio is later refactored, its Claude script step fetches the PDF itself
(it already has a working `drive_client`) for fidelity — numbers, methods, caveats,
quotes — and uses fg-zettelkasten's structured summary as the narrative scaffold (themes,
key points, framing). Nothing is lost; Gemini only vocalizes. Because the repo is
private, research-radio's CI needs a **GitHub read token** to fetch `summaries/`.

```
Paperpile → toread (metadata, no LLM) → feed.json
fabiogiglietto.github.io (research agenda data, published)
         ↓
fg-zettelkasten (Claude/Opus: topic register + full-PDF structured summary + notes)
   ├─ vault/           (Obsidian vault)
   └─ data/summaries/  (shared: structured summary per paper — no raw full text)
         ↓ (follow-up — RR fetches its own PDFs; reads summaries via read token)
research-radio (reads feed + summaries; Claude: dialogue script; Gemini: TTS)
```

## Project layout

```
fg-zettelkasten/
  src/
    main.py           # CLI: bootstrap | update | refresh-topics | recluster
    feed_client.py    # fetch toread feed.json; + adapter to drive_client's Paper shape
    episodes_client.py# fetch research-radio episodes.json -> {bibtex_id: audio_url}
    topics_client.py  # fetch github.io signals (live) -> synthesize topic register
    drive_client.py   # ported from research-radio: find_pdf / get_pdf_text
    claude_client.py  # Anthropic SDK wrapper; prompt caching for shared prefixes
    summarizer.py     # Opus: full PDF text -> structured summary (shared artifact)
    themes.py         # topic-anchored assignment + emergent sub-themes
    note_builder.py   # render Papers/, Topics/, Structures/ markdown
    state.py          # load/save data/state.json
  vault/
    .obsidian/        # minimal committed config so the vault opens cleanly
    Papers/           # one note per paper, filename = bibtex key
    Topics/           # register MOC note per anchor/emergent topic (entry points)
    Structures/       # hub notes narrating an argument across papers in a topic
  data/
    topics.json       # the topic register (taxonomy synthesized from github.io)
    state.json        # per-paper state (schema below)
    summaries/        # <bibtex-key>.json: structured summary only (no raw full text)
    .cache/           # gitignored: transient extracted PDF text
  config.yml  requirements.txt  .env.example
  .github/workflows/update-vault.yml
  README.md  CLAUDE.md
```

`requirements.txt`: `anthropic`, `requests`, `pyyaml`, `pypdf`,
`google-api-python-client`, `google-auth`.

## Topic register (the Luhmann *Schlagwortregister*)

`topics_client.py` fetches, **live from the published github.io repo** (not the local
folder), all research-agenda signals: `_data/projects.yml`, `_data/publications.yml`,
`_data/teaching.yml`, `_data/news.yml`, `scripts/config.js`, `scripts/data/bio-seed.md`.
Claude synthesizes them into a curated taxonomy of **6–12 working topics**, written to
`data/topics.json` (each: `slug`, `name`, `description`, `source_signals`, `is_emergent`).
The synthesis prompt **weights toward the current agenda** — `status: Active` projects,
recent `news.yml`, recent publications — so the register reflects what the user works on
*now*, not the full historical publication record in `publications.yml`.

Each topic becomes a **register entry note** in `Topics/` — a *thin entry point* that
indexes into the paper web (description + links + a Dataview list), not a containment
folder. Papers live flat in `Papers/`; a paper may belong to several topics.

The register is refreshed by `refresh-topics` (weekly cron); the user's agenda changes
slowly so topic slugs stay stable.

## Two entry points

### `bootstrap` — process the whole archive first (run once)
1. `refresh-topics`: build `data/topics.json` + `Topics/*.md`.
2. For each of the 167 papers: fetch PDF via `drive_client`, extract text, run
   `summarizer` (Opus, full text) → structured summary written to
   `data/summaries/<key>.json`. No PDF → abstract-only summary,
   `pdf_source: "abstract_only"`.
3. `themes`: assign every paper to one or more register topics. Papers fitting no
   anchor are tagged `unassigned`; an **emergent sub-theme** is created only when
   **≥3 unassigned papers are mutually cohesive** (LLM check) — it is then added to
   `topics.json` with `is_emergent: true`. Below the threshold a paper stays
   `unassigned` and waits. This stops the register fragmenting into one-paper topics.
4. `note_builder`: render every `Papers/<key>.md` with cross-links, regenerate all
   `Topics/*.md`, and generate `Structures/` hub notes (one or more per topic).

### `update` — daily cron, new/changed papers only
1. Fetch feed + episodes; diff against `state.json` by id and by `content_hash` →
   new papers, and papers whose state changed (e.g. a podcast episode now exists).
2. For each: fetch PDF, summarize, **assign to existing register topics** by sending
   the paper + current `topics.json` names/descriptions to Claude (ask which 1–2 fit;
   no embeddings). Papers fitting none stay `unassigned`; they only form a new emergent
   topic at the next `recluster` once the ≥3-cohesive-papers threshold is met.
3. Render/refresh the paper note and **regenerate** affected `Topics/*.md` (deterministic
   templating from state — no LLM, cheap). `Structures/*.md` hub notes are LLM-written
   and regenerate **only on `bootstrap`/`recluster`**, not on every `update`.
4. Full **`recluster`** runs when `--recluster` is passed (weekly cron) or when
   `papers_since_cluster` exceeds a `config.yml` threshold (default 25).

## Note generation

`note_builder` + Claude produce, per paper, a `Papers/<bibtex-key>.md`:
- **Frontmatter**: `title`, `aliases: [<readable title>]`, `authors`, `year`, `doi`,
  `bibtex_key`, `topics`, `citation_count`, `open_access`, `source_url`, `podcast_url`
  (if the id is in `episodes.json`), `pdf_available` (quality flag), `discovery_date`.
- **Body**: summary, key contributions, methods, findings; a **"Connections"** section
  where Claude emits inline `[[bibtex-key]]` wikilinks to related papers (it is given
  the titles+ids of other papers in the same topic(s)); topic links `[[<Topic>]]`; and
  a **"Podcast"** section with `audio_url` when an episode exists.
- **Filename = bibtex key** → stable `[[bibtex-key]]` links; readable title in `aliases`.

**Topic register notes** (`Topics/*.md`) are fully **regenerated** every run from
`state.json` + `topics.json` — deterministic templating, no LLM, cheap; never appended
to (appending in CI drifts ordering and duplicates rows). **Structure/hub notes**
(`Structures/*.md`) are Claude-written narratives synthesizing a line of argument across
the papers in a topic — regenerated only on `bootstrap`/`recluster`.

### `data/state.json` schema
```json
{
  "papers": {
    "bibtex:Boyd2026-pm": {
      "note_path": "Papers/Boyd2026-pm.md",
      "topics": ["information-disorder", "platform-governance"],
      "pdf_source": "drive" | "abstract_only",
      "content_hash": "<sha256 of pdf-text-or-abstract + podcast flag>",
      "podcast_linked": true,
      "last_processed": "2026-05-17T..."
    }
  },
  "last_full_cluster": "2026-05-17T...",
  "papers_since_cluster": 0
}
```
`content_hash` lets `update` detect when a note must be regenerated (e.g. a podcast
appeared), not only handle brand-new ids.

### Full re-cluster policy (`recluster`)
- `topics.json`, all `Topics/*.md` and `Structures/*.md` are fully regenerated.
- Each `Papers/*.md` frontmatter `topics:` is updated in place from new membership.
- Paper note **bodies are not re-summarised** (cost). Tradeoff: inline "Connections"
  links may drift until a note is regenerated for another reason; a `--regenerate-notes`
  flag forces it.

## Reuse / adapters

Copy `research-radio/src/drive_client.py` unchanged; add a one-line adapter in
`feed_client.py` that builds its `Paper` shape from feed items (first-author surname,
year parsed from `date_published`, title). Follow research-radio's `config.yml` + `.env`
conventions for pipeline consistency.

## CI — `.github/workflows/update-vault.yml`
- Daily: `python -m src.main update`. Weekly: adds `--recluster` and `refresh-topics`.
- Commits changed `vault/` and `data/` files back to the repo.
- Secrets: `ANTHROPIC_API_KEY`, `GOOGLE_APPLICATION_CREDENTIALS` (service-account JSON,
  same as research-radio), `GOOGLE_DRIVE_FOLDER_ID`. Workflow needs `contents: write`.

## Cost (Opus; estimates, verify prices at build)

- Per-paper full-PDF summary (~24k in / ~3.5k out): **~$0.60**.
- Archive bootstrap (167 papers + register + ~15 hub notes): **~$65–105** one-time
  (~$60–70 if ~40% lack PDFs).
- Weekly `recluster` (register synthesis + clustering + ~10–20 hub-note regenerations):
  **~$7/run**.
- Steady state (~1 new paper/day + weekly recluster): **~$30/mo**.
- Lever: Sonnet for the per-paper pass cuts that ~5× (archive ~$15–20) — switchable in
  `config.yml` if Opus cost is unwelcome.

## Verification
1. `git init`; venv; `pip install -r requirements.txt`; set `.env`.
2. `python -m src.main refresh-topics` — inspect `data/topics.json` and `Topics/*.md`;
   confirm topics reflect MINE / PROMPT / vera.ai and the config.js interests.
3. `python -m src.main bootstrap --limit 5` — confirm 5 `Papers/*.md` with frontmatter,
   `[[wikilinks]]`, topic assignment; `data/summaries/*.json` carry the structured
   summary (no raw full text); `Structures/` hub notes generated.
4. Confirm a paper whose id is in `research-radio/docs/episodes.json` shows a "Podcast"
   section; confirm a paper with no Drive PDF gets `pdf_available: false`.
5. Open `vault/` in Obsidian: graph view shows paper↔paper and paper↔topic links
   resolving with no broken links; `aliases` render readable titles.
6. `python -m src.main update` with no new papers → no-op.
7. Run full `bootstrap` over all 167 papers once the above passes.
