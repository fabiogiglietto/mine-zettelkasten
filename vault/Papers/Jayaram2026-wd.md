---
title: "Towards automating scientific review with Google&#x27;s Paper Assistant Tool"
aliases: ["Towards automating scientific review with Google&#x27;s Paper Assistant Tool"]
authors: ["Rajesh Jayaram", "Drew Tyler", "David Woodruff", "Corinna Cortes", "Yossi Matias", "Vahab Mirrokni", "Vincent Cohen-Addad"]
year: 2026
doi: 
bibtex_key: Jayaram2026-wd
topics: [computational-methods-for-content-analysis, meta-science-of-misinformation-research]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2606.28277v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Jayaram2026-wd.mp3
pdf_available: true
discovery_date: 2026-07-02T11:09:15.304164Z
---

# Towards automating scientific review with Google&#x27;s Paper Assistant Tool

> Jayaram, R., Tyler, D., Woodruff, D., Cortes, C., Matias, Y., Mirrokni, V., & Cohen-Addad, V. (2026). Towards automating scientific review with Google&#x27;s Paper Assistant Tool. *arXiv [cs.LG]*.
>
> [View paper](http://arxiv.org/abs/2606.28277v1)

## Summary

This paper introduces the Paper Assistant Tool (PAT), an agentic AI system built at Google Research for deep verification of mathematics and computer science manuscripts. PAT decomposes a paper into thematic segments, allocates variable inference-time compute per segment, runs parallel Deep Review agents (on a Gemini Deep Think backbone) with full-paper context, and synthesizes their outputs into a deduplicated report grounded via web search. The authors report a 34-point recall improvement over zero-shot on the math/CS subset of the SPOT benchmark and describe large-scale pre-submission pilots at STOC 2026 and ICML 2026 covering >4,700 papers. They also propose a four-level taxonomy of AI roles in peer review, arguing that current systems are ready for author-side use but not yet full reviewer replacement.

## Key Contributions

- A segmenter → budgeter → deep-reviewer → synthesizer pipeline specialized for detecting proof, logic, and experimental errors in technical manuscripts.
- Empirical evidence that orchestrated inference scaling meaningfully beats single-call and Pass@k LLM baselines on retraction-derived errors.
- First large-scale deployment of AI pre-submission review at premier CS venues (STOC, ICML), with author surveys and testimonials.
- A four-level taxonomy of AI in peer review (Tool for Authors, Tool for Reviewers, Supporting Reviewer, Total Automation), analogous to SAE autonomy levels.
- Speculative proposals for adjacent artifacts such as an "AIrXiv" repository of AI-reviewed preprints.

## Methods

- **Pipeline:** (1) a segmenter agent splits the paper into thematic units; (2) an adaptive budgeter assigns Light/Medium/High thinking budgets to each segment; (3) parallel Deep Review agents verify each segment with access to the full paper; (4) a synthesis agent deduplicates findings and grounds them using Google Search.
- **Benchmark:** filtered SPOT subset of 26 math/CS papers containing 29 known equation/proof errors from retractions and errata.
- **Grading:** a logic-aware LLM autograder, audited by the authors, judging semantic capture of ground-truth errors rather than surface keyword overlap.
- **Baselines:** zero-shot Gemini 3.1 Pro and the original SPOT SOTA.
- **Field deployment:** one PAT review per submission delivered to authors pre-deadline at STOC 2026 and ICML 2026, followed by voluntary author surveys (n=124 and n=733).

## Findings

- PAT detects 89.7% of ground-truth errors on the SPOT math/CS subset, versus 55.2% for zero-shot Gemini 3.1 Pro and 21.1% for prior SOTA.
- In one case, PAT synthesized an explicit counterexample refuting a main theorem that the zero-shot baseline had accepted.
- Author uptake was high: 97% (STOC) and 92.1% (ICML) said they would use PAT again; ~90% rated feedback very or mostly helpful.
- Grounding was less consistent — only 55.8% (STOC) and 64.8% (ICML) rated feedback as mostly or fully grounded.
- Substantive theory issues requiring >1 hour to address were flagged in 11.6% of STOC and 35.4% of ICML responses; 31% of ICML respondents ran new experiments in response.
- Reported failure modes include hallucinated dates, PDF parsing errors, and false accusations of invalidity against correct proofs.

## Connections

No other papers have been provided under shared topics, so there are no in-corpus wikilinks to make here. Intellectually, the work sits at the intersection of LLM-based proof and error checking (e.g., the SPOT benchmark it evaluates on), studies of peer-review inconsistency such as the NeurIPS 2014/2021 experiments, and broader discussions of autonomy taxonomies for AI-assisted research.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Jayaram2026-wd.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
