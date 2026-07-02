---
title: "Towards automating scientific review with Google&#x27;s Paper Assistant Tool"
aliases: ["Towards automating scientific review with Google&#x27;s Paper Assistant Tool"]
authors: ["Rajesh Jayaram", "Drew Tyler", "David Woodruff", "Corinna Cortes", "Yossi Matias", "Vahab Mirrokni", "Vincent Cohen-Addad"]
year: 2026
doi: 
bibtex_key: Jayaram2026-wd
topics: []
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2606.28277v1
podcast_url: 
pdf_available: true
discovery_date: 2026-07-02T11:09:15.304164Z
---

# Towards automating scientific review with Google&#x27;s Paper Assistant Tool

> Jayaram, R., Tyler, D., Woodruff, D., Cortes, C., Matias, Y., Mirrokni, V., & Cohen-Addad, V. (2026). Towards automating scientific review with Google&#x27;s Paper Assistant Tool. *arXiv [cs.LG]*.
>
> [View paper](http://arxiv.org/abs/2606.28277v1)

## Summary

This paper introduces the **Paper Assistant Tool (PAT)**, an agentic AI system from Google Research for deep technical review of mathematics and computer science manuscripts. PAT chains four stages — thematic segmentation, adaptive per-segment compute budgeting, parallel Deep Review agents built on Gemini Deep Think, and a search-grounded synthesis pass — to surface logical, mathematical, and experimental flaws in full papers. The authors report large gains over single-call LLM baselines on a proof-error subset of the SPOT benchmark, describe pre-submission pilot deployments at STOC 2026 and ICML 2026 covering over 4,700 papers with generally positive author reception, and propose a four-level taxonomy of AI roles in peer review as a framework for community policy discussion.

## Key Contributions

- The PAT pipeline itself: a segmenter → budgeter → parallel Deep Reviewers → synthesizer architecture specialized for math/CS verification.
- Benchmark evidence that orchestrated inference-scaling substantially outperforms zero-shot and Pass@k baselines on retraction-derived errors.
- First large-scale pilots of AI pre-submission review at premier CS venues (STOC 2026, ICML 2026), with survey data from ~857 authors.
- A four-level taxonomy of AI roles in peer review (Tool for Authors → Tool for Reviewers → Supporting Reviewer → Total Automation), analogized to SAE autonomy levels.
- Speculative proposals such as an "AIrXiv" automated-review repository and "AI for Students" as adjacent applications.

## Methods

The core system is a multi-stage agentic pipeline. A segmenter agent partitions the manuscript into thematic units; a budgeting stage assigns Light/Medium/High "thinking" compute per segment; Deep Review agents (Gemini Deep Think backbone) verify each segment against full-paper context in parallel; a final synthesis agent uses Google Search to ground, deduplicate, and consolidate findings. Evaluation combines (i) a filtered SPOT subset of 26 math/CS papers with 29 known equation/proof errors, scored with a logic-aware LLM autograder audited by humans, and (ii) live pilot deployments providing one PAT review per submission before conference deadlines, followed by author surveys (n=124 STOC, n=733 ICML).

## Findings

- On the SPOT math/CS proof-error subset, PAT achieves **89.7%** detection accuracy vs **55.2%** for zero-shot Gemini 3.1 Pro and **21.1%** for the prior SPOT SOTA.
- In one case study, PAT constructed a concrete counterexample invalidating a main theorem that zero-shot baselines accepted.
- Pilot scale: >4,700 submissions reviewed across STOC 2026 and ICML 2026.
- Author reception: 97% (STOC) / 92.1% (ICML) would use PAT again; ~90% rated feedback very or mostly helpful; 55.8%/64.8% found it mostly or fully grounded.
- Substantive theory gaps requiring >1 hour to fix were flagged in 11.6% of STOC and 35.4% of ICML respondent papers; 31% of ICML respondents ran new experiments in response.
- Reported failure modes include date hallucinations, PDF parsing errors, and false rejections of correct proofs.

## Connections

No other papers have been registered under the relevant topics, so there are no sibling notes to link. Intellectually, this work sits at the intersection of LLM-as-verifier research, benchmark studies of automated proof-checking (e.g., SPOT), and empirical work on peer-review reliability, but none of those are present in the local graph to link here.
