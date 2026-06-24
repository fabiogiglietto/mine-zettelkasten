# The Luhmann method, operationalised

Niklas Luhmann said he could write papers because his *Zettelkasten* was a
"communication partner": he pulled a sequence of linked slips and the paper's
argument was, in large part, already there. The romantic reading ("the box wrote
my papers") is misleading. The useful reading is mechanical:

1. **The box removes the blank page.** Structure comes from an existing thread of
   notes, not from a template imposed on an empty document.
2. **Serendipity is engineered, not hoped for.** Because slips were cross-linked
   across unrelated subject headings, pulling a thread surfaced juxtapositions the
   author had not consciously planned. Novelty lived in the *links*, not the notes.
3. **The box talks back.** Following links produced surprise — a note pointing
   somewhere unexpected — and that surprise was the seed of a new argument.

This kasten reproduces all three mechanically, and the indexer exposes each one.

## The three moves

### Move 1 — Follow a Structure (*Folgezettel*)

A Structure note is already an argued sequence: a topic split into sub-threads,
each citing specific papers in a deliberate order. This is the closest thing to
Luhmann pulling a numbered slip-sequence. To write from it, you are not
*creating* structure — you are *expanding* one that exists.

- **Artifact:** `structures.csv` (which threads exist) → read the markdown at the
  listed `path` in full.
- **Fidelity:** highest. The argument, the order, and the citations are the
  user's own prior synthesis. Invention risk is low because you are elaborating,
  not connecting.
- **Good for:** literature reviews, "state of the field" sections, framing pieces,
  a thread the user has already half-thought-through.

### Move 2 — Cross the registers (engineered serendipity)

The generative heart. A paper that belongs to two topic registers, or links to a
paper in a register it doesn't itself belong to, is a *bridge* — a place where two
conversations touch. An argument that lives on that bridge is, almost by
definition, one the corpus has not yet stated as a single thread. That is where a
genuinely new paper comes from.

- **Artifacts:**
  - `bridges.csv` — every paper ranked by `bridge_score = (own topics − 1) +
    (distinct foreign topics its links reach)`. High scorers sit on seams.
  - `crossings.csv` — the actual linked *pairs that share no topic*. Each row is a
    candidate juxtaposition: "X (registers A,B) is linked to Y (register C) — what
    argument needs both?"
- **Method:** read both files, pick 2–3 crossings whose juxtaposition implies a
  thesis, state each as a one-line claim, let the user choose, then gather the
  papers on *both* sides of the bridge as the spine.
- **Balance (the user's chosen setting):** prefer crossings where the two sides
  share linked neighbours or a method, so the bridge is real rather than coincidental.
  Surface the non-obvious; do not manufacture a connection the notes won't carry.
  Every bridge claim is flagged as the user's to verify (see integrity rules).

### Move 3 — Seed from a question

The user supplies the thesis or RQ; the box supplies the thread. Retrieve relevant
notes via `index.json` (titles, `key_claims`, topics) and `topics.csv`, assemble
the supporting spine, and — crucially — report what the corpus *cannot* support.
A question the kasten can't answer is a finding about the reading list, not a
prompt to fill the gap from general knowledge.

## Choosing a move

| The user… | Move |
|-----------|------|
| names a topic/Structure, wants a review or framing | 1 |
| wants something new, or asks "what could I write?" | 2 |
| brings their own thesis/RQ | 3 |

Modes combine: seed from a question (3), discover the spine runs through a bridge
(2), and lean on an existing Structure (1) for one section. The point is always
the same — let the linked notes determine the shape, then write.

## What "done well" looks like

- The outline's sections each name the `bibtex_key`s they rest on *before* prose
  is written.
- Disagreements in the corpus are written as disagreements, not averaged away.
- Nothing is cited that isn't a note; nothing load-bearing rests on a Summary
  without a pointer back to the DOI.
- The user could take the draft, open every cited note, and trace each claim home.
