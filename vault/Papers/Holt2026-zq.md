---
title: "What Facebook users flag as false news: A mixed-methods investigation of user-reported links"
aliases: ["What Facebook users flag as false news: A mixed-methods investigation of user-reported links"]
authors: ["Anton Elias Holt"]
year: 2026
doi: 10.1080/21670811.2026.2703607
bibtex_key: Holt2026-zq
topics: [platform-governance-content-moderation, platform-data-access-methods]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/21670811.2026.2703607
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Holt2026-zq.mp3
pdf_available: true
discovery_date: 2026-08-20T11:56:14.739426Z
---

# What Facebook users flag as false news: A mixed-methods investigation of user-reported links

> Holt, A. E. (2026). What Facebook users flag as false news: A mixed-methods investigation of user-reported links. *Digital Journalism*, 1–19. https://doi.org/10.1080/21670811.2026.2703607
>
> [View paper](https://doi.org/10.1080/21670811.2026.2703607)

## Summary

This paper asks an empirical question with immediate policy relevance: when Facebook users flag content as "False News," what are they actually flagging? Motivated by Meta's January 2025 decision to end professional third-party fact-checking in the US in favor of Community Notes and user reports, Holt uses the Meta/Social Science One URL Shares dataset (all URLs shared publicly 100+ times, January 2017–November 2022) to examine two critical cases: top-shared links during the 2018 Brazilian election and links from BBC.com. Through a mixed-methods design combining NLP, statistics, and qualitative content analysis, the study finds that user-reported URLs tend to concern polarized political topics and often merely contextualize controversial events rather than present outright false claims. The core argument is that flagging functions as a "narrow statement of objection" — users report content they disagree with rather than content they believe to be false — casting doubt on the wisdom-of-crowds rationale underpinning Meta's shift.

## Key Contributions

- One of the first large-scale empirical investigations of what users actually report on Facebook, complementing a largely theoretical, experimental, or qualitative literature.
- Introduces user-reported content as a platform-intrinsic signal of "problematic" content and a method for exploiting the underused User Reports Table in the URL Shares dataset.
- Focuses on links/URLs rather than posts, giving a distinctive angle on user-driven moderation debates.
- Offers empirical evidence on whether wisdom-of-crowds arguments transfer to real-world platform reporting, including a non-US-centric case (Brazil).
- Documents demographic and engagement patterns (age effects, angry reactions, sharing-without-clicking) tied to reported content.

## Methods

The author analyzes the URL Shares dataset's Attributes, Breakdown, and User Reports tables, filtering differential-privacy noise to retain only cells with genuine interactions (alpha < 0.001). Three samples are constructed: a Reported Sample (110,224 URLs reported as False News with a conservative 44+ reports/month threshold), a Misinformation Sample (28,271 fact-checked-false URLs), and a country-matched Control Sample (200,000 URLs). Two critical cases are selected — the 2018 Brazilian election (via time-series maxima and highest reported-to-fact-checked ratio) and BBC (a top-reported domain with zero fact-checked-false URLs). An NLP pipeline handles language detection (triangulated), translation via NLLB-200-3B, and cleaning. Content analysis combines frequency analysis, close reading and thematic grouping, and a Rank Difference Score to identify words characteristic of reported vs. control samples. Interaction patterns (views, clicks, shares, comments, likes, emoji reactions) are normalized by views and visualized via heatmaps by age group.

## Findings

- In the 2018 Brazil case, user-reported URLs outnumbered fact-checked false URLs 71:1 (1,568 vs. 22 for October 2018), showing scale potential — but most concerned candidates, corruption allegations, misinformation scandals, and social media use rather than false claims themselves.
- Some Brazil reported URLs both affirmed and denied the same contested claim (e.g., the "gay kit" story), consistent with reporting used as a political tool.
- BBC reported links (239 bbc.com/news URLs) had a narrower, more political and negative/sensational focus (Trump, Covid-19, vaccines), while control links (301) were more diverse, neutral, or "evergreen."
- Older users engage more with reported URLs (more likes, comments, shares, shares-without-clicks, angry reactions); younger users click less on reported than control URLs.
- Reported content drew more angry reactions per view than the Misinformation Sample, suggesting more contested topics.
- Overlap between Reported and Misinformation samples was small (3,446 URLs; 12.2% of Misinformation, 3.1% of Reported), confirming the samples are largely distinct.

## Connections

This paper belongs to the descriptive-empirical tradition of research built on the Meta/Social Science One URL Shares dataset and its methodological quirks, connecting to work on interpreting and using that data such as [[Gonzalez-Bailon2024-rq]] and [[Ulloa2024-jm]]. Its engagement with the wisdom-of-crowds debate over whether laypeople can identify misinformation at scale relates to crowd-based and expert-comparison studies like [[Allen2025-ot]], while its focus on platform-driven flagging and Community Notes connects to work on Notes and user-driven moderation such as [[Renault2025-uh]] and [[Pierri2025-hm]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Holt2026-zq.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
