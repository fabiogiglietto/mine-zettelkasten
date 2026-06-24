# Paper skeletons

Outline templates for Step 3. Each section says **where its notes come from**, so
the spine is built from the box rather than a generic shape. Always instantiate
the outline with concrete `bibtex_key`s before drafting prose — an outline whose
sections don't name their notes is not ready.

A note on length and honesty: these are *drafting scaffolds*, not section quotas.
Drop sections the corpus can't support, and never pad a thin section with
general-knowledge claims. A short, fully-grounded piece beats a complete-looking
one with invented mortar.

---

## A. Literature review / "state of the field"  (best from Move 1)

Source spine: a **Structure** thread; one sub-section per its sub-threads.

1. **Framing** — what unifies the corpus and why it matters now. From the
   Structure's overview paragraph + the relevant Topic description.
2. **Thread 1…N** — one per Structure sub-thread. Each: state the thread's claim,
   then walk its papers in order, pulling Findings/Contributions from each note.
3. **Tensions** — where threads disagree. Often the Structure already stages this;
   make it explicit. *This is the section reviewers remember.*
4. **Open questions / agenda** — gaps the corpus itself reveals (papers that call
   for X; questions no note answers). Mark agenda items the notes don't support as
   the author's.

---

## B. Conceptual / theoretical paper  (Move 2 or 3)

Source spine: a **bridge** — papers from two registers that the corpus links but
hasn't unified. The contribution is the unification.

1. **The problem** — the conceptual tension, stated from the two papers on either
   side of the bridge (`crossings.csv` / `bridges.csv`).
2. **Position A** — the register-1 papers' framing, on its own terms.
3. **Position B** — the register-2 papers' framing, on its own terms.
4. **The synthesis** — your proposed concept/typology/distinction that the bridge
   implies. **Flag this as the author's new claim**, not corpus-established.
5. **Worked illustration** — empirical papers from either register used as
   exemplars (their Methods/Findings).
6. **Implications & limits** — including what the synthesis can't yet account for.

---

## C. Empirical paper — framing & related-work only  (Move 3)

The kasten supplies framing and positioning, **not** data. Be explicit that
Methods/Results are the author's to supply.

1. **Introduction & motivation** — from the Topic description + 2–3 anchor papers'
   key_claims.
2. **Related work** — a short Move-1 review of the most relevant thread.
3. **Gap / contribution** — what the corpus shows is missing (from Connections that
   point outward, and from agenda statements in the notes).
4. **[Data / Methods / Results]** — *placeholder.* The skill does not invent these.
   Offer to scaffold method language from cited papers' Methods sections only.
5. **Discussion** — situate hypothetical findings against the reviewed tensions.

---

## D. Research agenda / position piece  (Move 2)

Source spine: the highest `bridge_score` papers + recent additions (high `year`),
read as a map of where the field is moving.

1. **Where the field is** — 2–3 sentence synthesis across the top registers
   (`topics.csv` by size).
2. **Emerging seams** — the top bridges, each framed as a research direction with
   its two-register grounding.
3. **What's thin** — small topics (low `n_papers`) and dangling outward links as
   signals of under-covered areas.
4. **A call** — the author's argument for priorities. Clearly the author's voice.

---

## Citation manifest (always)

A table accompanying every draft:

| key | authors | year | doi | sections used |
|-----|---------|------|-----|----------------|

Flag any cited note with no `doi`. Build every row from frontmatter.

## Provenance map (always)

| claim (short) | source key(s) | status |
|---------------|---------------|--------|

`status` ∈ {grounded · synthetic (author to verify) · gap (no note supports)}.
Every "synthetic" and "gap" row is a place the author must look before submission.
