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
# The title H1 (group 1) immediately followed by an existing citation blockquote
# (group 2 — the contiguous run of `>`-prefixed lines). Used to re-render the
# block in place so parser improvements reach already-built notes.
_H1_THEN_BLOCK = re.compile(
    r"(^# .+$\n\n)(>[^\n]*(?:\n>[^\n]*)*)", re.MULTILINE
)


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
    inserted = rerendered = unchanged = unmatched = skipped = 0

    for note in sorted(papers_dir.glob("*.md")):
        text = note.read_text(encoding="utf-8")
        paper = by_key.get(_key_of(text, note.stem))
        if paper is None:
            print(f"  WARN: no feed match for {note.stem}")
            unmatched += 1
            continue
        block = note_builder.render_citation_block(paper)
        existing = _H1_THEN_BLOCK.search(text)
        if existing:
            # Replace the current citation blockquote in place (idempotent).
            new_text = text[: existing.start(2)] + block + text[existing.end(2):]
            if new_text == text:
                unchanged += 1
                continue
            rerendered += 1
        else:
            match = _BODY_H1.search(text)
            if not match:
                print(f"  WARN: no H1 in {note.stem}")
                skipped += 1
                continue
            new_text = f"{text[:match.end()]}\n\n{block}{text[match.end():]}"
            inserted += 1
        note.write_text(new_text, encoding="utf-8")

    print(
        f"done: {inserted} inserted, {rerendered} re-rendered, "
        f"{unchanged} unchanged, {unmatched} unmatched, {skipped} skipped"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
