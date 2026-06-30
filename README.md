# mine-zettelkasten

The **[MINE](https://mine.uniurb.it)** team's shared Zettelkasten (MINE = *Mapping Italian News*). It turns
the papers the team reads into a densely interconnected knowledge base, modelled
on the [Niklas Luhmann Archive](https://niklas-luhmann-archiv.de/), and publishes
it as a website.

**Browse it:** https://fabiogiglietto.github.io/mine-zettelkasten/

Each paper becomes a richly-described note, organised under a **topic register**,
cross-linked into a navigable web. It is a fork of
[fg-zettelkasten](https://github.com/fabiogiglietto/fg-zettelkasten), seeded with
that archive and then grown by the team.

## Adding papers (teammates start here)

You add papers straight from Slack — no Git. In the MINE **`#zettelkasten`**
channel, just **post a link to the paper** (no hashtag, no command):

```
https://doi.org/10.1080/1369118X.2024.2349123
```

A bot finds the open-access PDF (or asks you to attach one), summarizes the
paper, and publishes a note crediting you as the submitter. **Open-access papers
only.** Full instructions — the PDF fallback, duplicate handling, attribution —
are in **[CONTRIBUTING.md](CONTRIBUTING.md)**.

## Sources

Three streams feed the vault, all joined on the `bibtex:AuthorYear-xx` id:

1. **Team Slack submissions** — links posted in `#zettelkasten`, ingested by
   [mine-toread](https://github.com/fabiogiglietto/mine-toread). Notes are tagged
   `kind: team` and carry `submitted_by`.
2. **Paperpile reading list** — Fabio's curated to-read queue, also via
   mine-toread.
3. **Own publications** — from `fabiogiglietto.github.io`'s
   `own-publications.json`, tagged `kind: own` (recent or well-cited, built from
   the green open-access PDF). Toggle with the `own_publications` config block.

## Pipeline

```
#zettelkasten Slack channel ─┐
Paperpile "To Read"          ├─► mine-toread (Unpaywall/arXiv/Crossref + Drive)
                             ┘        │  -> output/feed.json (+ submitted_by)
                                      v
mine-zettelkasten (Claude: topic register + full-PDF summaries + notes)
   |- vault/           Obsidian vault (Papers / Topics / Structures)
   '- data/            state, topics, summaries (committed)
                                      │
                                      v
                          Quartz site on GitHub Pages
```

Duplicate submissions are caught twice: mine-toread replies *"already in the
archive"* in Slack, and mine-zettelkasten skips any new id whose DOI/title
already has a note.

## Setup (maintainer)

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then fill in the keys
```

`.env` / GitHub Actions secrets:

- `ANTHROPIC_API_KEY`
- `GOOGLE_APPLICATION_CREDENTIALS` (path to a Google service-account JSON with
  read access to **both** the Paperpile Drive folder and mine-toread's Slack-inbox
  folder) and `GOOGLE_DRIVE_FOLDER_ID` (Paperpile folder)
- `SLACK_INBOX_DRIVE_FOLDER_ID` — mine-toread's Slack-inbox upload folder (so
  team-submitted PDFs are found)
- `SLACK_WEBHOOK_URL` — incoming webhook bound to the team `#toread` channel,
  where each new note's digest is announced (papers are *submitted* in
  `#zettelkasten`; the digest goes to `#toread`)

The matching ingestion secrets (`SLACK_BOT_TOKEN`, `PAPERPILE_EXPORT_URL`, …)
live on **mine-toread**, where the repo variable `SLACK_REQUIRE_HASHTAG=false`
puts ingestion in dedicated-channel mode (any link is a submission).

## Usage

```bash
python -m src.main refresh-topics       # build the topic register from github.io
python -m src.main bootstrap            # process the whole archive (run once)
python -m src.main update               # incremental run (new/changed papers)
python -m src.main update --recluster   # incremental + full re-cluster
python -m src.main export-site          # export the vault to quartz/content/
```

In normal operation nothing is run by hand: mine-toread dispatches
`pipeline-finalize` on a feed change, and a daily cron runs `update` as a
fallback.

## Vault layout

- `vault/Papers/`     — one note per paper, filename = bibtex key
- `vault/Topics/`     — register entry notes (the *Schlagwortregister*)
- `vault/Structures/` — hub notes narrating an argument across papers in a topic

Open `vault/` as an Obsidian vault. `data/` and `vault/` are committed; extracted
PDF text is transient and never committed.

## Writing from the kasten (Claude Code skill)

The repo ships a Claude Code skill, **`zettel-paper`**, that drafts papers,
literature reviews, and syntheses *from* the vault the Luhmann way — pulling a
thread of linked notes that already forms an argument into prose, citing only
real notes with traceable DOIs. It lives in `.claude/skills/zettel-paper/` and is
auto-discovered when you open this repo in
[Claude Code](https://claude.com/claude-code).

Ask in plain language, e.g.:

- "Draft a literature review on coordinated inauthentic behavior from the kasten."
- "What non-obvious paper could the team write from these notes?"

It works from the **public** notes and summaries, so any teammate can run it on a
fresh clone.

## Website

Published with [Quartz](https://quartz.jzhao.xyz/) — interactive graph, backlinks,
search, topic/structure landing pages — at
**https://fabiogiglietto.github.io/mine-zettelkasten/**. The `update-vault` GitHub
Action rebuilds and deploys it on every run.

```bash
python -m src.main export-site                  # vault/ -> quartz/content/
cd quartz && npm ci && npx quartz build --serve # preview at localhost:8080
```

`export-site` is deterministic (no LLM) and never modifies the vault. Quartz
needs Node 22+; `quartz/content/` and `quartz/public/` are not committed.
