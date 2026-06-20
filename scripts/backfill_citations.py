"""One-time backfill: splice an APA citation block into existing paper notes.

Notes built before the citation feature have no `## Citation`-style block. The
journal/volume/pages needed for a citation live only in the source feeds (not in
note frontmatter or state), so this fetches both feeds, joins each existing
`vault/Papers/*.md` to its `Paper` by bibtex key, and inserts the same
`note_builder.render_citation_block` used by forward generation right after the
title H1. Idempotent: a note that already carries the block is skipped.

Run from the repo root:  python -m scripts.backfill_citations
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from src import feed_client, note_builder

_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_BODY_H1 = re.compile(r"^# .+?[ \t]*$", re.MULTILINE)
# A note already carrying a citation: a blockquote within ~2 lines of the H1.
_HAS_BLOCK = re.compile(r"^# .+\n\n> ", re.MULTILINE)


def _key_of(text: str, fallback: str) -> str:
    fm = _FRONTMATTER.match(text)
    if fm:
        data = yaml.safe_load(fm.group(1)) or {}
        if data.get("bibtex_key"):
            return str(data["bibtex_key"])
    return fallback


def main() -> int:
    cfg = yaml.safe_load(Path("config.yml").read_text(encoding="utf-8"))
    inputs = cfg["inputs"]

    papers = feed_client.fetch_feed(inputs["feed_url"])
    papers += feed_client.fetch_own_publications(inputs["own_publications_url"])
    by_key = {p.bibtex_key: p for p in papers}
    print(f"loaded {len(by_key)} papers from feeds")

    papers_dir = Path(cfg["vault"]["path"]) / cfg["vault"]["papers_dir"]
    spliced = skipped = unmatched = already = 0

    for note in sorted(papers_dir.glob("*.md")):
        text = note.read_text(encoding="utf-8")
        if _HAS_BLOCK.search(text):
            already += 1
            continue
        paper = by_key.get(_key_of(text, note.stem))
        if paper is None:
            print(f"  WARN: no feed match for {note.stem}")
            unmatched += 1
            continue
        match = _BODY_H1.search(text)
        if not match:
            print(f"  WARN: no H1 in {note.stem}")
            skipped += 1
            continue
        block = note_builder.render_citation_block(paper)
        insert_at = match.end()
        new_text = f"{text[:insert_at]}\n\n{block}{text[insert_at:]}"
        note.write_text(new_text, encoding="utf-8")
        spliced += 1

    print(
        f"done: {spliced} spliced, {already} already had a block, "
        f"{unmatched} unmatched, {skipped} skipped"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
