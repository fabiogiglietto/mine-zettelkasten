---
title: "TubeStats and TokStats: Research tools for random samples of YouTube and TikTok"
aliases: ["TubeStats and TokStats: Research tools for random samples of YouTube and TikTok"]
authors: ["Kevin Zheng", "Reagan Keeney", "Ryan McGrady", "Vikramaditya Jaisingh", "Ethan Zuckerman"]
year: 2026
doi: 10.17645/mac.12085
bibtex_key: Zheng2026-bi
topics: [platform-data-access-and-methods, platforms-audiences-and-online-communities]
citation_count: 0
open_access: false
source_url: https://doi.org/10.17645/mac.12085
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Zheng2026-bi.mp3
pdf_available: true
discovery_date: 2026-07-14T06:35:37.173094Z
---

# TubeStats and TokStats: Research tools for random samples of YouTube and TikTok

> Zheng, K., Keeney, R., McGrady, R., Jaisingh, V., & Zuckerman, E. (2026). TubeStats and TokStats: Research tools for random samples of YouTube and TikTok. *Media and Communication*, *14*. https://doi.org/10.17645/mac.12085
>
> [View paper](https://doi.org/10.17645/mac.12085)

## Summary

This paper introduces **TubeStats** and **TokStats**, two publicly accessible dashboard tools that report platform-wide statistics for YouTube and TikTok derived from genuinely random samples of hosted content. The authors argue that, in the "post-API age," neither platform offers adequate sanctioned means to build representative samples, pushing researchers toward opportunistic, popularity-biased data that misrepresents typical platform use. By exploiting the structure of each platform's video ID/URL schemes, the authors demonstrate that true random sampling is feasible without restrictive research APIs, yielding defensible denominators and engagement-distribution baselines. The work is positioned within platform and infrastructure studies and the open-science movement as a public-interest transparency practice, engaging debates about representative sampling, data-disclosure regulation (e.g., the EU DSA), and the ethics of unpermissioned platform-centered research.

## Key Contributions

- Two open, regularly updated research tools (TubeStats live; TokStats planned mid/late 2026) with open-source sampling and front-end code.
- Validated, reproducible random sampling methods for two major video platforms that do not depend on sanctioned APIs.
- Defensible denominators and engagement-distribution baselines that let researchers contextualize non-representative samples and support cross-platform comparison.
- A privacy-preserving data-sharing model pairing aggregate dashboards with public (de-identified) and gated full datasets.
- Documented downstream use by scholars, journalists (BBC, Washington Post), and DSA-linked moderation-workforce research.
- A candid account of the technical, financial, and ethical challenges of sustaining open research infrastructure.

## Methods

- **YouTube:** "Dialing for videos" queries purely random 11-character IDs to build a true random sample, validated against the more efficient "random prefix sampling" method that exploits prefix-searchable hyphenated IDs; searching via the Innertube package and downloading metadata/audio with yt-dlp. Language is identified via OpenAI's Whisper on audio, which is then immediately discarded (no audio/video archived).
- **TikTok:** Exploits the 64-bit structure of 19-digit IDs, where the first 32 bits encode a Unix creation timestamp; a random second is selected, tens of thousands of candidate IDs are generated for the remaining bits, and extant videos are detected via Selenium.
- **System:** SvelteKit front-end, static JSON summaries in an S3 bucket, Chart.js for logarithmic distribution charts and percentile calculators, pandas for binning and summary statistics.
- **Governance:** Aggregate-only public dashboards plus a planned dual release (public de-identified CSV and restricted full sample on application), with collaboration with qualitative and culturally-situated researchers to follow up on quantitative patterns.

## Findings

- Random prefix sampling yields results sufficiently similar to slower true-random dialing, justifying its use for efficiency.
- Hindi YouTube differs markedly from English, Spanish, and Russian YouTube — newer, shorter videos, more education/entertainment, with a distinct like-to-view pattern.
- Most TikTok videos are not uploaded from the US; popularity has shifted from India (late 2010s) toward other Asian countries, not the US or Europe.
- Engagement is extremely skewed: a video with 150 views sits at the 68th percentile of all YouTube videos, and 1,000–10,000 views place a video in the top 10%.
- TikTok sample generation takes months versus hours for YouTube, limiting update frequency.
- Cited auditing shows TikTok's "random" Research API is temporally biased (over 55% of returned videos posted on Saturdays), motivating an alternative sampling approach.
- Platforms are increasingly hostile to automated queries (e.g., YouTube's shift from DASH to the session-oriented SABR protocol), partly attributed to for-profit AI scraping.

## Connections

This work directly addresses the "APIcalypse" and post-API data-access constraints that also motivate broader debates over platform transparency and data disclosure, connecting to platform-governance and content-moderation scholarship such as [[Rieder2026-pp]], [[Rieder2025-ju]], and [[Katzenbach2026-sl2e]]. Its concern with representative sampling, denominator problems, and DSA-linked audits places it alongside methodological and platform-audit work on data access and moderation research, including [[Bechmann2026-dr]] and [[Larsson2026-ro]]. The TikTok-specific sampling and its critique of the Research API relate to TikTok-focused empirical studies such as [[Bouchaud2026-lr]] and [[Bouchaud2026-np]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Zheng2026-bi.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
