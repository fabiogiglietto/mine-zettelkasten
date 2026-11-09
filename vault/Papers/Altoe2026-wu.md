---
title: "Predicting narrative virality on social media streams for pre-peak misinformation triage"
aliases: ["Predicting narrative virality on social media streams for pre-peak misinformation triage"]
authors: ["Filipe Altoe", "Sérgio Miguel Gonçalves Pinto", "H. Sofia Pinto"]
year: 2026
doi: 10.1145/3799682.3840688
bibtex_key: Altoe2026-wu
topics: [information-disorder-and-health-misinformation, llm-assisted-computational-content-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1145/3799682.3840688
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Altoe2026-wu.mp3
pdf_available: true
discovery_date: 2026-11-08T09:21:58.131103Z
---

# Predicting narrative virality on social media streams for pre-peak misinformation triage

> Altoe, F., Pinto, S. M. G., & Pinto, H. S. (2026). Predicting narrative virality on social media streams for pre-peak misinformation triage. *Proceedings of the 35th ACM International Conference on Information and Knowledge Management*, 127–138. https://doi.org/10.1145/3799682.3840688
>
> [View paper](https://doi.org/10.1145/3799682.3840688)

## Summary

This paper reframes misinformation triage as a *narrative-level streaming virality prediction* problem, motivated by a timing gap: false narratives tend to peak in about 1.5 days while fact-checks arrive a median of 4.5 days later. The authors argue that the natural unit of analysis for triage is the narrative — a cluster of semantically equivalent claims — rather than individual posts or coarse events. They build an end-to-end streaming pipeline (online clustering → kernel-density anomaly detection → LLM claim normalization → cluster-level spread prediction → interpretable check-worthiness classification) and introduce the **Post-Detection Spread Ratio (PSR)**, a metric that quantifies the remaining intervention window at detection time. The work releases the first dataset and baselines for the task from a 1.52M-post US 2020-election Twitter/X stream and reports state-of-the-art results on two established Automatic Claim Detection benchmarks.

## Key Contributions

- A new task formulation: narrative-level streaming virality prediction with the claim cluster as the unit of analysis.
- The first dataset and baselines: virality labels plus 42-feature inputs for 529 anomalous cluster instances (535 distinct claims) drawn from 1.52M posts, with released code and prompts.
- The **PSR** metric, quantifying the remaining intervention window at detection time to enable pre-peak, actionable triage.
- New SOTA baselines on CT2025 claim normalization and CheckThat! 2024 check-worthiness.
- An interpretable **4-Parallel-Heads DeBERTa** architecture decomposing check-worthiness into checkability, verifiability, and harm potential, aligned with journalistic pre-judgment criteria.
- A frontier-LLM zero-shot ablation and a formative study with six professional fact-checkers supporting the modular, distilled design.

## Methods

The dataset was constructed from the US Election 2020 Tweets corpus (Oct 15–Nov 08), chosen because it needs no hydration and retains collection-time engagement counts (enabling no-lookahead temporal statistics). The pipeline uses incremental cosine-similarity streaming clustering over multilingual-mpnet embeddings (τ=0.65) behind a claim gate; online anomaly detection via EXPoSE (random Fourier feature kernel density, selected from the NAB leaderboard); two-stage retrieval plus contrastive, topic-aware few-shot prompting (Mistral-7B, Mixtral-8x7B, DeepSeek-3.1v) for claim normalization evaluated with METEOR; and PSR regression over a 6-hour post-detection window benchmarked across linear, tree, kernel, sequence/point-process, and text models. Check-worthiness used full fine-tuning of DeBERTa-v3-large with class-weighted cross-entropy and LLM-derived soft labels, compared against a Claude Opus 4.7 zero-shot baseline with McNemar testing and cost/latency analysis.

## Findings

- Contrastive few-shot Mistral-7B reaches METEOR 0.5569 on CT2025, beating the strongest published baseline by 10 points and even the larger Mixtral.
- The 4-Parallel-Heads DeBERTa achieves F1=0.833 on CheckThat! 2024 and generalizes zero-shot (ClaimBuster F1=0.973, CT2023 F1=0.933); a late-fusion variant scored marginally higher in-domain but generalized worse.
- EXPoSE dominates classical detectors (97.9% detected before peak, median +23h lead) because claim clusters violate stationarity assumptions.
- Cluster-level virality is approximately linear: regularized linear and kernel models match or beat sequence models and Hawkes point processes (which perform near-random); user/network authority features dominate content features.
- 86% of check-worthiness errors are shared across approaches, implicating representation learning — not feature engineering — as the bottleneck.
- The distilled classifier beats Claude Opus 4.7 zero-shot by 0.11 F1 at <10ms latency and near-zero cost versus ~$18/1k claims and ~9.9s.
- The pipeline surfaces ~500 candidates from ~1.5M posts; fact-checkers agreed/partially agreed in 83.3% of cases and all six endorsed the report structure.
- Fine-tuning underperformed prompting for normalization, and normalized claims can contain factual errors that METEOR fails to penalize.

## Connections

This work extends the Automatic Claim Detection and check-worthiness literature from static classification toward streaming, pre-virality triage, and connects to broader studies of how misinformation spreads faster than correction, notably the finding that false news diffuses more quickly than true news (Vosoughi2018-at) and research on the limited reach of fact-checks (Guess2020-rr). Its use of LLMs for claim-level content analysis under journalistic criteria resonates with work on scalable LLM-based classification and fact-check assistance such as [[DeVerna2025-dl]] and [[Le-Mens2025-qz]]. The anomaly-detection and narrative-emergence framing also relates to collective-action and coordinated-spread detection studies like [[Graham2025-gp]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Altoe2026-wu.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
