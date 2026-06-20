"""One-time backfill: refresh the `## Podcast` section of existing paper notes.

Notes built before the multi-platform podcast feature carry at most a single
"Listen" MP3 link. This fetches research-radio's episode records, joins each
existing `vault/Papers/*.md` to its record by bibtex key, and rewrites the
`## Podcast` section with the same `note_builder.render_podcast_block` used by
forward generation — so the MP3 plus any Spotify/Apple links stay consistent
across new and existing notes. Idempotent: a note already carrying the rendered
block is skipped.

Own-publication notes (`kind: own`) keep MP3-only — their episodes are excluded
from research-radio's public feed and so never reach Spotify/Apple.

Run from the repo root:  python -m scripts.backfill_podcasts
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from src import episodes_client, note_builder

_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
# An existing "## Podcast" section: the heading through the end of the note or
# the next level-2 heading (whichever comes first). Podcast is rendered last by
# build_paper_note, so in practice it runs to EOF.
_PODCAST_SECTION = re.compile(
    r"\n## Podcast\n.*?(?=\n## |\Z)", re.DOTALL
)


def _meta_of(text: str, fallback: str) -> tuple[str, str | None]:
    """Return (bibtex_key, kind) from a note's frontmatter."""
    fm = _FRONTMATTER.match(text)
    if fm:
        data = yaml.safe_load(fm.group(1)) or {}
        key = str(data["bibtex_key"]) if data.get("bibtex_key") else fallback
        kind = data.get("kind")
        return key, (str(kind) if kind else None)
    return fallback, None


def main() -> int:
    cfg = yaml.safe_load(Path("config.yml").read_text(encoding="utf-8"))
    episodes = episodes_client.fetch_episodes(cfg["inputs"]["episodes_url"])
    print(f"loaded {len(episodes)} episodes from research-radio")

    papers_dir = Path(cfg["vault"]["path"]) / cfg["vault"]["papers_dir"]
    updated = appended = unchanged = skipped = 0

    for note in sorted(papers_dir.glob("*.md")):
        text = note.read_text(encoding="utf-8")
        key, kind = _meta_of(text, note.stem)
        episode = episodes.get(f"bibtex:{key}") or episodes.get(key)
        block = note_builder.render_podcast_block(episode, kind)

        existing = _PODCAST_SECTION.search(text)
        if existing:
            replacement = f"\n{block.rstrip()}\n" if block else ""
            new_text = text[: existing.start()] + replacement + text[existing.end():]
            if new_text == text:
                unchanged += 1
                continue
            updated += 1
        elif block:
            new_text = f"{text.rstrip()}\n\n{block}"
            appended += 1
        else:
            skipped += 1
            continue
        note.write_text(new_text, encoding="utf-8")

    print(
        f"done: {appended} appended, {updated} updated, "
        f"{unchanged} unchanged, {skipped} no-episode"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
