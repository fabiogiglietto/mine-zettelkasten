# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

`mine-zettelkasten` is the **MINE team fork** of
[`fabiogiglietto/fg-zettelkasten`](https://github.com/fabiogiglietto/fg-zettelkasten)
— the same feed → Claude-written Obsidian Zettelkasten → Quartz site pipeline,
fed by `mine-toread` instead of `toread` and grown by the whole team.

For commands, architecture, and conventions, read the **upstream CLAUDE.md**:
https://github.com/fabiogiglietto/fg-zettelkasten/blob/main/CLAUDE.md
Everything there applies here. Published site:
https://fabiogiglietto.github.io/mine-zettelkasten/

## What differs from upstream (deliberate)

- **Feed source:** `mine-toread`'s `feed.json` (team Slack submissions carry
  `submitted_by`; their notes are tagged `kind: team` and render a
  "suggested by" line — `note_builder.py`).
- **Dedup against the seeded corpus:** `state.py` keeps a DOI/title index so a
  team submission that already has a note is skipped (and mine-toread replies
  "already in the archive" in Slack).
- **Slack-inbox Drive folder:** team-attached PDFs are found via
  `SLACK_INBOX_DRIVE_FOLDER_ID` (`drive_client.py`).
- **No research-radio dispatch:** the team chain ends here; the workflow is
  triggered by mine-toread's `pipeline-finalize` plus its own daily cron.
- Teammate-facing instructions live in `CONTRIBUTING.md`.

## Code vs content — merge discipline

- **Code:** `src/`, `scripts/`, `quartz/`, `.github/` — comes from upstream.
- **Content and state:** `vault/`, `data/` — belongs to this repo (and to the
  bots); upstream merges must **never** touch these paths.

## Fork policy — read before changing code

This is a **config-diff fork**. Feature code and bug fixes land in upstream
`fg-zettelkasten` (behind config flags defaulting to fg behavior) and arrive
here via `git merge upstream/main`. Permanent local differences are limited to
`config.yml` values, repo Actions variables/secrets, `CONTRIBUTING.md`, these
doc stubs, and the content/state paths above. **Do not land feature code
directly in this repo** — implement upstream, flag it, then merge.

Pipeline DAG for both chains:
https://github.com/fabiogiglietto/toread/blob/main/PIPELINE.md

> **Status:** unification with upstream is in progress; until it completes,
> some `src/` files still diverge from `fg-zettelkasten`.
