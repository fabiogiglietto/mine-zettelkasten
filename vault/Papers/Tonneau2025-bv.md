---
title: "Language Disparities in Moderation Workforce Allocation by Social Media Platforms"
aliases: ["Language Disparities in Moderation Workforce Allocation by Social Media Platforms"]
authors: ["Manuel Tonneau", "Diyi Liu", "Ryan McGrady", "Kevin Zheng", "Ralph Schroeder", "Ethan Zuckerman", "Scott Hale"]
year: 2026
doi: 10.1145/3805689.3806484
bibtex_key: Tonneau2025-bv
topics: [platform-data-access-and-governance, information-disorder-and-health-misinformation]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1145/3805689.3806484
podcast_url: 
pdf_available: true
discovery_date: 2025-08-15T00:00:00Z
---

# Language Disparities in Moderation Workforce Allocation by Social Media Platforms

> Tonneau, M., Liu, D., McGrady, R., Zheng, K., Schroeder, R., Zuckerman, E., & Hale, S. (2026). Language Disparities in Moderation Workforce Allocation by Social Media Platforms. *Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency*. https://doi.org/10.1145/3805689.3806484
>
> [View paper](https://doi.org/10.1145/3805689.3806484)

## Summary

This paper offers the first comparative empirical analysis of how six major social media platforms — YouTube, Meta, TikTok, Twitter/X, Snapchat, and LinkedIn — distribute human content moderators across languages, exploiting transparency data mandated by the EU's Digital Services Act (DSA). The authors document stark cross-lingual disparities in both language coverage and moderator-to-content ratios. They find that smaller platforms leave millions of EU users without any human moderation in their national language, and that even where moderators exist, languages predominantly spoken in the Global South (Spanish, Portuguese, Arabic) receive proportionally far fewer moderators than English — from 55% of English's allocation on YouTube down to a mere 7.5% on Twitter/X. The study argues that current DSA reporting, while a pivotal advance, is insufficient for independent scrutiny and calls for globally inclusive transparency requirements.

## Key Contributions

- First comparative empirical analysis of cross-lingual moderator workforce allocation across six major DSA-regulated platforms.
- A novel methodology combining DSA transparency disclosures with independently constructed, calibrated content-volume estimates to normalize moderator counts per language.
- Quantification of the number of EU users left without national-language moderation on specific platforms.
- Empirical extension and nuancing of prior reports (Haugen disclosures, Global Witness) on underinvestment in non-English moderation.
- Concrete policy recommendations for more meaningful transparency, including mandatory reporting of content volume per language, moderator workload capacity, and harmful-content prevalence.

## Methods

The authors collected per-language moderator counts from DSA-mandated transparency reports (Summer 2023–Fall 2024), averaging across reporting periods and treating non-reported EU languages as zero. To normalize these counts by content volume, they used independent datasets — the TwitterDay corpus (375M tweets from one day in 2022) and a random sample of ~26,000 YouTube videos — applying fastText language identification calibrated against native-speaker annotations via isotonic regression. Bootstrap resampling (1,000 samples) produced per-language count estimates with confidence intervals. Twitter/X user locations were geocoded via the Google Geocoding API, and DSA-reported country-level user counts were used (with the UN geoscheme) to estimate how many users lack moderators for their national language.

## Findings

- YouTube, Meta, and TikTok cover nearly all EU official languages, while Twitter/X, LinkedIn, and Snapchat exhibit multiple blind spots, especially in Southern, Eastern, and Northern Europe.
- Roughly 16M EU Twitter/X users (14%), 8M LinkedIn users (16%), and 7M Snapchat users (7%) have no moderators for their national language.
- Languages subject to Twitter/X blind spots represent on average 31% of tweets in countries where they are official.
- On Twitter/X, only Bulgarian and German have more moderators than English relative to content volume; Italian and Bulgarian have similar moderator counts despite Italian content being 78 times more prevalent.
- On Twitter/X, Portuguese, Arabic, and Spanish receive roughly 9%, 7%, and 7% of English's moderator-per-content allocation respectively.
- On YouTube, most covered EU languages receive proportionally more moderators than English; only Spanish and Portuguese receive less, signaling reduced investment in Latin American user bases.
- Global South languages average 55% of English's allocation on YouTube, falling to 7.5% on Twitter/X.
- Some languages are supported in platform interfaces but lack dedicated moderation staff (Greek, Czech, Romanian), while some with moderators lack interface support (Tagalog).

## Connections

This work sits within the platform governance and accountability literature, extending studies of how platforms structure and disclose their operations [[Katzenbach2026-sl2e]] and foundational accounts of moderation infrastructure [[Gillespie2010-sla2]], [[Gillespie2022-jx]], [[van-Dijck2018-up]]. Its interrogation of DSA-mandated transparency reporting as a powerful but incomplete accountability mechanism relates to broader critiques of platform data access and audit regimes [[Rieder2020-sl35]], [[Rieder2025-ju]]. By centering linguistic inequities in user safety, it also speaks to concerns about uneven protection against information disorder across global communities.
