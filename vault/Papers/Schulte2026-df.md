---
title: "Multi-platform analysis of electoral discourse on social media as a research infrastructure problem"
aliases: ["Multi-platform analysis of electoral discourse on social media as a research infrastructure problem"]
authors: ["Ludwig Schulte", "Dino Pasic", "Catalina Goanta", "Adriana Iamnitchi"]
year: 2026
doi: 10.1145/3795513.3807440
bibtex_key: Schulte2026-df
topics: [platform-data-access-and-research-infrastructure, political-communication-and-elections]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1145/3795513.3807440
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Schulte2026-df.mp3
pdf_available: true
discovery_date: 2026-05-26T17:18:00.349369Z
---

# Multi-platform analysis of electoral discourse on social media as a research infrastructure problem

> Schulte, L., Pasic, D., Goanta, C., & Iamnitchi, A. (2026). Multi-platform analysis of electoral discourse on social media as a research infrastructure problem. *Companion Publication of the 2026 18th ACM Web Science Conference*, 66–69. https://doi.org/10.1145/3795513.3807440
>
> [View paper](https://doi.org/10.1145/3795513.3807440)

## Summary

Using the 2025 German federal election as a case study, this paper reframes multi-platform analysis of electoral discourse not as a matter of accumulating more empirical studies but as a *research infrastructure* problem. The authors collected 81,866 posts from X and 43,597 videos from TikTok during the campaign period, applying topic modeling and a multimodal (facial, vocal, textual) analysis pipeline. Rather than foregrounding campaign findings, they use the exercise to expose the bottlenecks — algorithmic filtering, API limits, sampling noise, and inconsistent data structures — that constrain what electoral harms can be studied under post-API access conditions. They argue that platform observability should be treated as a reusable foundation of tools, workflows, and documentation, and offer four recommendations for making such infrastructure durable and reproducible.

## Key Contributions

- Reframes multi-platform electoral discourse analysis as a research infrastructure challenge rather than a set of one-off empirical studies.
- Documents a parallel X + TikTok data collection effort for the 2025 German federal election, including dataset statistics and platform-specific adaptations.
- Demonstrates a concrete multimodal pipeline for TikTok political videos, integrating facial, vocal, and textual signals at the diarized-segment level.
- Catalogues specific biases (algorithmic, temporal, sampling, noise) that emerge under post-API collection.
- Provides four actionable recommendations: standardized data structures, higher data-quality standards (e.g., transparent electoral account labeling), content-type-tailored analysis, and interdisciplinary collaboration.

## Methods

The study covers 6 November 2024 (German government collapse) to 23 February 2025 (election day). Data were collected in parallel from X (via a scraper on the X API v2) and TikTok (via a scraper aggregating partial results across repeated calls), seeded with official party accounts and expanded through mentions (X) and hashtags (TikTok). The authors distinguish *authored* posts (official party accounts) from *promoted* posts (retweets, mentions, hashtag-linked content). BERTopic clustered posts thematically and tracked temporal evolution. A multimodal pipeline ran on diarized TikTok segments (pyannote.audio) combining facial emotion (OpenCV + DeepFace), vocal tone (HuBERT), and textual sentiment (XLM-R), with Cramér's V quantifying cross-modal associations.

## Findings

- The dataset spans 81,866 X posts (541 accounts) and 43,597 TikTok videos (4,682 accounts) across seven German parties.
- Parties differ sharply in platform preference: BSW is most active on X and least on TikTok; AfD is highly active on TikTok, less so on X; FDP and CDU are active on both.
- Cross-modal associations on TikTok are uniformly weak (Cramér's V ≤ 0.104), indicating textual, vocal, and facial channels operate independently and carry distinct information.
- TikTok political content tends toward *politainment*: negative or critical text and visuals delivered in calm, neutral vocal tones.
- Russia/Ukraine and immigration are the top two topics on both platforms but in reversed order; migration is more prominent on TikTok, Israel/Gaza and EU topics on X.
- Roughly two-thirds of hashtag-scraped TikTok content was non-political, showing substantial noise bias.
- X's API limits (~1,000 posts/day per account) prevent full historical recovery, while TikTok returns algorithmically filtered partial results — introducing temporal and engagement biases.

## Connections

This paper sits squarely in the "post-API age" debate about data access for computational social science and connects to work on platform observability, transparency regimes, and the EU DSA vetted-researcher framework — see [[Freelon2024-sc]], [[Bruns2026-yv]], and [[Rieder2025-ju]]. Its multi-platform election-monitoring focus links it to comparative electoral discourse studies such as [[Gonzalez-Bailon2024-rq]] and to the TikTok politainment and visual-analysis literature in [[Achmann-Denkler2026-lx]] and [[Jurg2025-ur]]. On the governance and data-access side it resonates with [[Katzenbach2026-sl2e]] and [[Bechmann2026-dr]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Schulte2026-df.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-why-one-platform-isnt-enough-to/id1866587707?i=1000771443693)
