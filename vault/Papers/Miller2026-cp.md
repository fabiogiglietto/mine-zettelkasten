---
title: "Community-driven API and AI writer design for openly scaling Community Notes"
aliases: ["Community-driven API and AI writer design for openly scaling Community Notes"]
authors: ["Brad Miller", "Jay Baxter", "Jiansong Chao", "Keith Coleman", "Sophie Hilgard", "Daniel Ortiz"]
year: 2026
doi: 
bibtex_key: Miller2026-cp
topics: [llm-assisted-research-methods, platform-governance-and-data-access]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2609.40067v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Miller2026-cp.mp3
pdf_available: true
discovery_date: 2026-10-16T13:48:42.353889Z
---

# Community-driven API and AI writer design for openly scaling Community Notes

> Miller, B., Baxter, J., Chao, J., Coleman, K., Hilgard, S., & Ortiz, D. (2026). Community-driven API and AI writer design for openly scaling Community Notes. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2609.40067v1)

## Summary

This paper, written by X's own Community Notes team (all six authors list the affiliation "Community Notes, SpaceXAI"), presents the design, operation and measured impact of the AI Note Writer API, open to the public since September 2025, and of the Community Writer (CW), the largest API client, released as open source under Apache 2.0. AI writers consume feeds of candidate posts derived from user note requests and engagement and propose notes; contributor ratings and the open-source scoring algorithm still decide which notes show broadly. Evaluating June 2–29, 2026, the authors report that the CW produces 41% of proposed notes but 52% of Currently Rated Helpful (CRH) notes and 55% of CRH note views while consuming 22% of contributor ratings, and that AI writers have helped raise daily CRH note volume by 86.0% since launch. They argue AI writing is additive to human writing, not a substitute for it, and treat rater attention as "a critical resource" that the system must economize. Because the authors evaluate their own system, this is industry-produced evidence.

## Key Contributions

- **Openness:** documents the public AI API — its earn-in admissions process, hit-rate-based quota and feed hierarchy.
- **Scale:** describes mechanisms to prioritize, draft, evaluate and delete notes that economize contributor time (52% of CRH notes from 22% of ratings).
- **Speed:** shows an API client writing the first non-deleted note on 60% of posts that also have a note from another writer, yielding 55% of CRH note views.
- Releases the Community Writer's code, prompts and model-training code as open source.

## Methods

- System description plus a 28-day evaluation (June 2–29, 2026; note status as of June 30), with CW code, configuration, models and feeds frozen. Collaborative notes (a pilot feature) are excluded.
- **Earn-in:** a new client must pass three checks on its 50 most recent notes (≥95% resolving URLs, ≥98% not classified as harassment/abuse, ClaimOpinion-model score thresholds) before its notes collect ratings.
- **Quota:** a daily writing limit tied to hit rate, (CRH − CRNH) / (CRH + CRNH + NMR), and non-linear — a 10% hit rate allows 50 notes/day, a 20% hit rate the maximum of 500.
- **Feeds:** four candidate-post feeds (Small, Large, XL, XXL) built from explicit note requests and implicit signals (e.g. "@grok is this true?"); access to larger feeds is earned through note outcomes.
- **CW pipeline:** a Notable Post Model (an MLP predicting whether a post will receive a CRH note) prioritizes work queues; two writers (Grok 4.20 and the post-trained CN Grok) draft notes; four rejectors (Helpfulness, Recent Context, Screenshot, Revision) filter them.
- **Deletion Model:** logistic regression on real-time rating aggregates, applied once 3 ratings are available — an elevated threshold at 3–4 ratings and a standard one at 5 or more — deletes notes unlikely to reach CRH.
- The CW is compared with other AI clients, top human writers and other human writers on CRH rate, ratings consumed, views, latency and topic.

## Findings

- The CW accounts for 41% of proposed notes, 52% of CRH notes and 55% of CRH note views while consuming 22% of contributor ratings.
- AI writers supported 86.0% growth in daily CRH notes between September 2025 and September 2026 (all writers combined, 28-day trailing averages).
- Where both the CW and another writer proposed a note, the CW published the first non-deleted note on 60% of posts and the first AI note on 95%.
- Among posts with a CRH note, 42% have only AI notes (no human-proposed note) and 30% have no AI-proposed note.
- A rating spent on a CW note led to a CRH note 29% of the time, against 17% for top human writers.
- 54% of Needs More Ratings (NMR) notes have fewer than 10 ratings, the effective minimum for CRH status.
- Of 65 client accounts that began earn-in, 32 earned writing ability and 19 remain active.
- Stated limitations: no control for operational cost or feed size, and the CW is compared with all other AI writers in aggregate.

## Connections

This is the platform operator's own evaluation of AI-written Community Notes, and a case of the industry-produced evidence whose risks [[Bak-Coleman2025-pm]] examines. Independent analyses of the same program reach more critical conclusions: [[Bouchaud2026-np]] finds that 85.22% of notes never reach a status for lack of diverse ratings and that polarizing, election-related content is undermoderated by design, which echoes this paper's treatment of rater attention as "a critical resource"; [[Renault2025-uh]] uses helpful-rated notes to measure partisan asymmetry in who gets flagged. Thematically, [[Holt2026-zq]] studies user-driven flagging on Facebook as Meta moved to Community Notes, and [[Hackenburg2025-dj]] shows that the levers that make conversational AI more persuasive, chiefly packing in fact-checkable claims, also degrade its factual accuracy, a relevant backdrop for AI-written fact-checks.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Miller2026-cp.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
