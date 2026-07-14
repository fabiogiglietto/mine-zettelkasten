---
title: "TubeStats and TokStats: Research tools for random samples of YouTube and TikTok"
aliases: ["TubeStats and TokStats: Research tools for random samples of YouTube and TikTok"]
authors: ["Kevin Zheng", "Reagan Keeney", "Ryan McGrady", "Vikramaditya Jaisingh", "Ethan Zuckerman"]
year: 2026
doi: 10.17645/mac.12085
bibtex_key: Zheng2026-bi
topics: [computational-methods-llms-social-media, platform-governance-content-moderation]
citation_count: 0
open_access: false
source_url: https://doi.org/10.17645/mac.12085
podcast_url: 
pdf_available: true
discovery_date: 2026-07-14T06:35:37.173094Z
---

# TubeStats and TokStats: Research tools for random samples of YouTube and TikTok

> Zheng, K., Keeney, R., McGrady, R., Jaisingh, V., & Zuckerman, E. (2026). TubeStats and TokStats: Research tools for random samples of YouTube and TikTok. *Media and Communication*, *14*. https://doi.org/10.17645/mac.12085
>
> [View paper](https://doi.org/10.17645/mac.12085)

## Summary

This article introduces **TubeStats** and **TokStats**, two publicly accessible dashboard tools that deliver platform-wide statistics for YouTube and TikTok derived from genuinely random samples of hosted content. The authors argue that because neither platform offers sanctioned mechanisms for representative sampling — a problem sharpened in the "post-API age" — researchers routinely fall back on opportunistic, popularity-biased samples that systematically misrepresent typical platform use. The paper demonstrates that true random sampling is nonetheless feasible by exploiting each platform's video ID indexing schemes, and it positions such sampling as a public-interest transparency and accountability practice. Alongside the technical pipelines and system architecture, the authors offer a candid account of the financial and ethical challenges of sustaining open research infrastructure against increasingly hostile platforms.

## Key Contributions

- Two open, regularly updated research tools (TubeStats live; TokStats planned for mid/late 2026), with sampling and front-end code released on GitHub.
- Validated, reproducible random sampling methods for two major video platforms that do not depend on sanctioned research APIs.
- Defensible "denominators" and engagement-distribution baselines that let researchers contextualize non-representative samples and enable cross-platform comparison.
- A privacy-preserving data-sharing model pairing aggregate dashboards with public (de-identified) and gated full datasets.
- Documented downstream use by scholars, journalists (BBC, Washington Post), and DSA-linked moderation-workforce research.

## Methods

For YouTube, the authors use "dialing for videos" (querying random 11-character IDs for a true random sample) validated against the faster "random prefix sampling" method that exploits prefix-searchable hyphenated IDs; metadata and audio are retrieved via Innertube and yt-dlp, with Whisper used for language identification before audio is immediately discarded. For TikTok, they exploit the 64-bit structure of 19-digit IDs — where the first 32 bits encode a Unix creation timestamp — selecting a random second, generating tens of thousands of candidate IDs, and querying via Selenium to detect extant videos. The dashboards are built with SvelteKit, static JSON in S3, and Chart.js, with pandas handling binning and summary statistics. Governance combines aggregate-only public dashboards with a planned dual dataset release (public de-identified CSV plus a restricted full sample under application and privacy agreement).

## Findings

- Random prefix sampling yields results sufficiently similar to slower true-random sampling to justify its efficiency.
- Hindi YouTube differs markedly from English, Spanish, and Russian YouTube — newer, shorter videos, more education/entertainment, and a distinct like-to-view pattern.
- Most TikTok videos are not uploaded from the US; popularity shifted from India in the late 2010s to other Asian countries, not the US or Europe.
- Engagement is extremely skewed: a video with 150 views sits at the 68th percentile of all YouTube videos, and 1,000–10,000 views places a video in the top 10%.
- TikTok sample generation takes months versus hours for YouTube, limiting update frequency.
- Cited independent auditing shows TikTok's "random" Research API is temporally biased (over 55% of returned videos posted on Saturdays), motivating alternative sampling.
- Platforms are growing hostile to automated queries (e.g., YouTube's shift from DASH to session-oriented SABR streaming), partly attributed to for-profit AI scraping.

## Connections

This paper's concern with the "APIcalypse" and building alternative, unpermissioned data-collection infrastructure connects it to broader debates over platform data access and research-API reliability; its critique of biased sampling and defense of representative baselines resonates with work on platform accountability and moderation such as [[Gillespie2026-aa]] and [[Rieder2025-ju]]. Its emphasis on the EU DSA as a transparency and data-disclosure regime relates it to platform-governance scholarship in this register, and its focus on the moderation workforce links to that literature as well.
