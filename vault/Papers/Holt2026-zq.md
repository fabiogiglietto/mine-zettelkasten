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
podcast_url: 
pdf_available: true
discovery_date: 2026-08-20T11:56:14.739426Z
---

# What Facebook users flag as false news: A mixed-methods investigation of user-reported links

> Holt, A. E. (2026). What Facebook users flag as false news: A mixed-methods investigation of user-reported links. *Digital Journalism*, 1–19. https://doi.org/10.1080/21670811.2026.2703607
>
> [View paper](https://doi.org/10.1080/21670811.2026.2703607)

## Summary

This paper offers one of the first large-scale empirical looks at what Facebook users actually flag as "False News," a question made urgent by Meta's January 2025 decision to abandon professional third-party fact-checking in the US in favour of Community Notes and user reporting. Drawing on the Meta/Social Science One URL Shares dataset (URLs shared publicly 100+ times, January 2017–November 2022), Holt applies a mixed-methods design to two critical cases — top-shared links during the 2018 Brazilian election and links from the BBC.com domain. The central argument is that user reporting functions less as a detector of falsehood and more as a "narrow statement of objection": reported URLs cluster around polarized political topics and typically contextualize controversial events rather than assert outright false claims, implying users flag content they disagree with rather than content they believe to be false.

## Key Contributions

- One of the first large-scale empirical investigations of what users actually report as false on Facebook, complementing an otherwise theoretical, experimental, or qualitative literature.
- Introduces user-reported content as a platform-intrinsic signal of "problematic" content and demonstrates a method for exploiting the underused User Reports Table in the URL Shares dataset.
- Analyses links/URLs rather than posts, offering a distinctive angle on user-driven moderation.
- Provides empirical evidence bearing on whether Wisdom-of-Crowds arguments transfer to real-world reporting systems, plus a non-US-centric (Brazil) case.
- Documents demographic and engagement signatures of reported content (age effects, angry reactions, sharing-without-clicking).

## Methods

Holt filters differential-privacy noise from the URL Shares dataset (retaining cells with genuine interactions at alpha < 0.001) and constructs three samples: a Reported Sample (110,224 URLs reported as False News 20+ times, with a conservative 44+ threshold to account for noise), a Misinformation Sample (28,271 fact-checked-false URLs), and a country-matched Control Sample (200,000 URLs). Two critical cases are selected — the October 2018 Brazilian election (via time-series maxima and highest reported-to-fact-checked ratio) and the BBC (a most-reported domain with zero fact-checked-false URLs). An NLP pipeline triangulates language detection, translates via NLLB-200-3B, and cleans text; content analysis combines frequency analysis, close reading/thematic grouping, and a Rank Difference Score. Interaction patterns (views, clicks, shares, shares-without-clicks, comments, likes, emoji reactions) are normalized by views across age groups and visualized as heatmaps.

## Findings

- In the 2018 Brazil case, user-reported URLs outnumbered fact-checked-false URLs 71:1 (1,568 vs. 22 for October 2018), showing scale potential — yet most reported links concerned candidates, corruption allegations, scandals, and social media use rather than false claims.
- Some Brazil reported URLs both affirmed and denied the same contested claim (e.g., the "gay kit" story), consistent with reporting as a political tool on divisive topics.
- BBC reported links had a narrower, more political and negative/sensational focus (Trump, Covid-19, vaccines), while control links were more diverse, neutral, or "evergreen."
- Older users engage more with reported URLs (likes, comments, shares, shares-without-clicks, angry reactions); younger users click less on reported than control URLs.
- Reported content drew more angry reactions per view than the Misinformation Sample, suggesting more contested topics.
- Overlap between Reported and Misinformation samples was small (3,446 URLs; 12.2% of Misinformation, 3.1% of Reported), confirming largely distinct phenomena.

## Connections

This paper sits squarely in the descriptive-empirical tradition of studies mining the Meta/Social Science One URL Shares dataset and interrogating its differential-privacy noise, connecting it to work on that dataset's reliability and reach such as [[Gonzalez-Bailon2024-rq]] and [[Allen2025-ot]]. Its skepticism about whether laboratory Wisdom-of-Crowds effects transfer to real reporting speaks to debates over lay misinformation identification and platform moderation signals, adjacent to [[Stagnaro2025-pz]] and [[Bak-Coleman2025-pm]]. On the governance side, its framing of Meta's 2025 pivot away from professional fact-checking toward user-driven moderation connects it to broader content-moderation scholarship represented here by [[Gillespie2010-sla2]] and [[Katzenbach2026-sl2e]].
