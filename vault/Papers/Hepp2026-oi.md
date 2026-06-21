---
title: "The imaginative landscape of AI: Locating Silicon Valley’s “quiet futuring”"
aliases: ["The imaginative landscape of AI: Locating Silicon Valley’s “quiet futuring”"]
authors: ["Andreas Hepp"]
year: 2026
doi: 10.1177/01634437261454515
bibtex_key: Hepp2026-oi
topics: [platform-governance-data-access, elections-political-communication]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1177/01634437261454515
podcast_url: 
pdf_available: true
discovery_date: 2026-05-26T19:31:02.136444Z
---

# The imaginative landscape of AI: Locating Silicon Valley’s “quiet futuring”

> Hepp, A. (2026). The imaginative landscape of AI: Locating Silicon Valley’s “quiet futuring”. *Media, Culture & Society*. https://doi.org/10.1177/01634437261454515
>
> [View paper](https://doi.org/10.1177/01634437261454515)

## Summary

Using the 2025 German federal election as an empirical anchor, this paper diagnoses the practical and infrastructural obstacles to studying electoral discourse across multiple social media platforms in a post-API era. The authors collected 81,866 X posts and 43,597 TikTok videos from seven major German parties and ran a multimodal analytical pipeline to compare platform-specific affordances, party strategies, and topical agendas. Their central argument is that platform observability should be reconceived as a shared, reusable research infrastructure — standardized tools, workflows, and documentation that enable reliable cross-platform and cross-temporal comparison — rather than as a sequence of ad hoc study-specific data collections constrained by restrictive platform governance.

## Key Contributions

- Documents concrete bottlenecks in multi-platform election observability under restricted API regimes (X API v2 limits, TikTok's partial and algorithmically-influenced returns).
- Provides an empirical multi-platform, multimodal dataset and analytical pipeline for the 2025 German federal election.
- Reframes platform observability as a shared research-infrastructure problem rather than as isolated empirical work.
- Offers four actionable recommendations: standardize data structures per platform affordance; raise data-access quality standards (including transparent platform labeling of political accounts); tailor methods to content type (multimodal for video platforms); and institutionalize interdisciplinary collaboration.
- Generates evidence directly relevant to DSA Article 40 implementation and vetted researcher access debates.

## Methods

A case study covering 6 November 2024 to 23 February 2025, with parallel scraping of X (via a twitter-api-client implementation of X API v2) and TikTok, seeded with official party accounts and expanded via mentions (X) and hashtags (TikTok). The authors distinguish "authored" posts from party accounts and "promoted" posts (retweets, mentions, shared hashtags). For TikTok, a multimodal pipeline combined speaker diarization (pyannote.audio), facial emotion recognition (OpenCV + DeepFace), vocal tone (HuBERT), and textual sentiment (XLM-R), with Cramér's V used to assess cross-modal association. BERTopic supported topic identification and cross-platform comparison.

## Findings

- Parties differ markedly in platform preference: BSW dominates on X but is nearly absent from TikTok, AfD is highly active on TikTok, while FDP and CDU operate on both.
- Cross-modal associations on TikTok are uniformly weak (Cramér's V ≤ 0.104), indicating that textual, vocal, and facial channels convey largely independent emotional signals.
- Political TikToks frequently pair negative text and charged facial expressions with calm vocal tone — a "politainment" style that text-only analyses would miss.
- Topical agendas overlap (Russia/Ukraine and migration dominate both platforms) but diverge meaningfully: migration is more prominent on TikTok; Israel/Gaza and EU topics on X; news-driven events (Magdeburg attack, fall of the Syrian regime) appear in X's top topics but not TikTok's.
- About two-thirds of hashtag-seeded TikTok content was non-political noise requiring heavy filtering.
- X API v2 caps (~1000 posts/day per account) prevent full historical recovery, and TikTok's partial returns demand repeated calls — both undermining reproducibility.
- The DSA's transparency mandates remain practically unenforced, and X actively obstructs data collection.

## Connections

This paper sits squarely in post-API computational social science debates and connects directly to work on the "APIcalypse" and shrinking research access, especially [[Bruns2026-yv]], [[Rieder2025-ju]], and [[Rieder2026-pp]], as well as to the broader DSA Article 40 / vetted-researcher-access agenda discussed in [[de-Vreese2026-zx]]. Its multi-platform election design resonates with platform-comparative election studies such as [[Lukito2026-nb]] and [[Brown2026-br]], and its infrastructural framing of cross-platform observability complements platform-governance work like [[Helmond2026-ll]] and longitudinal monitoring efforts associated with [[Giglietto2026-632ef967]].
