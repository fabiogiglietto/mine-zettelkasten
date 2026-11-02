---
title: "A practical guide and case study on how to instruct LLMs for automated coding during content analysis"
aliases: ["A practical guide and case study on how to instruct LLMs for automated coding during content analysis"]
authors: ["Mike Farjam", "Hendrik Meyer", "Meike Lohkamp"]
year: 2026
doi: 10.1177/08944393251349541
bibtex_key: Farjam2026-zg
topics: [generative-ai-for-content-analysis, computational-political-media-influence]
citation_count: 15
open_access: false
source_url: https://doi.org/10.1177/08944393251349541
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Farjam2026-zg.mp3
pdf_available: true
discovery_date: 2026-11-02T00:35:13.685862Z
---

# A practical guide and case study on how to instruct LLMs for automated coding during content analysis

> Farjam, M., Meyer, H., & Lohkamp, M. (2026). A practical guide and case study on how to instruct LLMs for automated coding during content analysis. *Social Science Computer Review*, *44*, 488–502. https://doi.org/10.1177/08944393251349541
>
> [View paper](https://doi.org/10.1177/08944393251349541)

## Summary

This paper is a methodological "how-to" for integrating Large Language Models into content analysis, aimed at communication and media researchers operating under typical university constraints of cost, scalability, and data privacy. The authors argue that LLMs can augment or replace human coders at acceptable reliability while running locally on consumer-grade hardware. They demonstrate this through a replication and extension of Feldman et al.'s (2015) study of U.S. newspaper climate change coverage, using a locally hosted Llama 3.1-70b model. Beyond validation, they scale the original analysis tenfold, apply finer-grained coding, and extend the same instructions to a German-language corpus without translation — all organized within a replicable agentic workflow.

## Key Contributions

- A general, replicable agentic workflow — **Instructor** (meta-prompting), **Classifier** (per-document coding with memory reset and chain-of-thought), optional **Judge** (adjudicates conflicting runs), and **Human Intermediary** (prompt refinement and validation).
- Practical, hands-on guidelines for prompting, output validation, and multilingual coding within realistic computational and legal limits.
- A demonstration of local, privacy-preserving LLM deployment on consumer-grade hardware, keeping proprietary data off corporate servers.
- A worked case study showing LLMs overcoming small-sample limits (scaling 642 → 3,274 articles) and enabling finer, impact/action-level coding.
- Emphasis on chain-of-thought reasoning and a transparent Judge mechanism as tools for replicability and accountability.

## Methods

The authors deployed a 6-bit quantized Llama 3.1-70b model locally (two M3 Max processors), selected after pre-testing several 2024 models. Data were drawn from Factiva using identical inclusion criteria to the original study: 3,274 U.S. articles (NYT, Washington Post, USA Today, WSJ) and 4,863 German articles (taz, Süddeutsche Zeitung, FAZ, Die Welt). Prompting techniques included meta-prompting, task decomposition, chain-of-thought reasoning requiring direct text quotes, and pooling two classifier runs per article. Validation used Krippendorff's alpha (target ≥0.7) with an 80/20 train-validation split to guard against prompt overfitting; the German corpus was validated against two expert coders on 200 articles.

## Findings

- LLM–human reliability reached acceptable levels (α ≥ 0.7) for most concepts; adding the Judge agent generally raised alpha (e.g., Frame rose from 0.61 to 0.74 in English, 0.68 to 0.80 in German).
- The abstract "efficacy" construct remained below threshold (~0.62–0.64) despite three refinement cycles, attributed to its theoretical vagueness.
- Reliability on combined training+validation data was slightly higher than on the validation subset alone, suggesting prompts were robust rather than overfitted.
- Performance was comparable across English and German, supporting multilingual coding without translation.
- The LLM was more sensitive than human coders, detecting variables more often, though this did not qualitatively alter the original study's conclusions.
- The most effective reliability gains came from reminding the model not to hallucinate, decomposing complex instructions, and requiring direct quotations.
- The full pipeline required ~two weeks of continuous operation, highlighting the computational overhead of decomposition and repeated runs.

## Connections

This paper sits squarely within the methodological literature on using LLMs for automated content and text annotation; it most directly complements validation- and reliability-focused work such as [[Gilardi2026-hw]] and benchmark/validity studies like [[Balluff2026-if]] and [[Balluff2026-bv]]. Its emphasis on cross-lingual coding and reproducible classification pipelines connects to broader efforts to assess LLM annotation quality found in [[Le-Mens2025-qz]] and [[Dierickx2026-tw]]. Its local-deployment, privacy-preserving stance offers a practical counterpoint to studies relying on proprietary API models.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Farjam2026-zg.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
