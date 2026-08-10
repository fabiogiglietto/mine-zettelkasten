---
title: "Multi-platform analysis of electoral discourse on social media as a research infrastructure problem"
aliases: ["Multi-platform analysis of electoral discourse on social media as a research infrastructure problem"]
authors: ["Ludwig Schulte", "Dino Pasic", "Cătălina Goanță", "Adriana Iamnitchi"]
year: 2026
doi: 10.1145/3795513.3807440
bibtex_key: Schulte2026-df
topics: [platform-data-access-governance, cross-national-disinformation-monitoring]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1145/3795513.3807440
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Schulte2026-df.mp3
pdf_available: true
discovery_date: 2026-05-26T17:18:00.349369Z
---

# Multi-platform analysis of electoral discourse on social media as a research infrastructure problem

> Schulte, L., Pasic, D., Goanță, C., & Iamnitchi, A. (2026). Multi-platform analysis of electoral discourse on social media as a research infrastructure problem. 66–69. https://doi.org/10.1145/3795513.3807440
>
> [View paper](https://doi.org/10.1145/3795513.3807440)

## Summary

This paper uses the 2025 German federal election as a case study to argue that the central problem in multi-platform electoral discourse research is not a shortage of studies but the absence of consolidated, reusable **research infrastructure** for platform observability under constrained access. Collecting 81,866 X posts and 43,597 TikTok videos across seven German parties, the authors apply topic modeling and multimodal (facial, vocal, textual) analysis — but foreground the bottlenecks in data access, collection, and analysis rather than campaign findings per se. Their core move is to reconceptualize observability as a reusable foundation of tools, workflows, and documentation that can support reliable cross-platform, cross-temporal, and cross-context comparison in the "post-API age."

## Key Contributions

- Reframes multi-platform electoral discourse analysis as a **research infrastructure problem** rather than a series of one-off empirical studies.
- Provides a documented case study of parallel X and TikTok data collection during the 2025 German federal election, with dataset statistics and platform-specific methodological adaptations.
- Demonstrates a concrete multimodal analysis pipeline for TikTok political videos integrating facial, vocal, and textual signals at the diarized-segment level.
- Identifies and catalogues specific biases (algorithmic, temporal, sampling, noise) that arise under post-API collection conditions.
- Offers four actionable recommendations: standardize data structures, raise data-quality standards (e.g., transparent electoral account labeling), tailor analysis to content type, and integrate interdisciplinary expertise.

## Methods

- Case study of the 2025 German federal election, spanning 6 Nov 2024 (government collapse) to 23 Feb 2025 (election day).
- Parallel scraping of X (X API v2 based) and TikTok (aggregating partial results across repeated calls), seeded with official party accounts and expanded via mentions (X) and hashtags (TikTok).
- Distinction between **authored** posts (official party accounts) and **promoted** posts (retweets, mentions, hashtag-linked content).
- Topic modeling with BERTopic to cluster posts and track temporal evolution.
- Multimodal pipeline on diarized TikTok segments (pyannote.audio): facial emotion via OpenCV + DeepFace, vocal tone via HuBERT, textual sentiment via XLM-R, with Cramér's V to measure inter-modal association.

## Findings

- Dataset: 81,866 X posts from 541 accounts and 43,597 TikTok videos from 4,682 accounts across seven parties.
- Parties differ markedly in platform preference: BSW most active on X, least on TikTok; AfD highly active on TikTok, less on X; FDP and CDU active on both.
- Textual, vocal, and facial signals on TikTok are only weakly associated (Cramér's V ≤ 0.104) — they operate as largely independent channels.
- TikTok political content pairs negative/critical text and visuals with calm, neutral vocal delivery — a **politainment** style.
- Russia/Ukraine and immigration are the top two topics on both platforms but in reversed order; migration is more prominent on TikTok, while Israel/Gaza and EU topics feature more on X.
- Roughly two-thirds of hashtag-scraped TikTok content was non-political, revealing substantial noise bias.
- X API limits (~1,000 posts/day per account) prevent full historical recovery, while TikTok returns algorithmically filtered partial results, introducing temporal and engagement-driven biases.

## Connections

This paper sits squarely in the "post-API age" methodological debate and the platform-transparency policy conversation around DSA Article 40 and vetted-researcher access, connecting to work on scraping, access, and observability such as [[Bruns2026-yv]], [[Rieder2025-ju]], Davies2026-cy and the DSA-focused strands in [[Rieder2026-pp]] and [[Bruns2026-pn]]. Its multi-platform electoral monitoring design resonates with the longitudinal election-observatory and coordinated-behavior tradition represented by [[Giglietto2026-632ef967]], [[Giglietto2025-1765bb4f]], and [[Pierri2025-hm]], while its TikTok multimodal and politainment focus links to short-video political communication work like [[Achmann-Denkler2026-lx]] and [[Jurg2025-ur]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Schulte2026-df.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-why-one-platform-isnt-enough-to/id1866587707?i=1000771443693)
