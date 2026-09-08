---
title: "Language Disparities in Moderation Workforce Allocation by Social Media Platforms"
aliases: ["Language Disparities in Moderation Workforce Allocation by Social Media Platforms"]
authors: ["Manuel Tonneau", "Diyi Liu", "Ryan McGrady", "Kevin Zheng", "Ralph Schroeder", "Ethan Zuckerman", "Scott Hale"]
year: 2026
doi: 10.1145/3805689.3806484
bibtex_key: Tonneau2025-bv
topics: [platform-governance-data-access]
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

This paper delivers the first comparative empirical analysis of how six major social media platforms — YouTube, Meta, TikTok, Twitter/X, Snapchat, and LinkedIn — distribute their human content moderators across languages, exploiting transparency data mandated by the EU's Digital Services Act (DSA). The authors document large cross-lingual disparities in both language coverage and moderator-to-content ratios, showing that millions of EU users on smaller platforms post in languages with no human oversight at all. Even where moderators exist, languages predominantly spoken in the Global South — Spanish, Portuguese, Arabic — receive proportionally fewer moderators than English, ranging from 55% of English's allocation on YouTube to as little as 7.5% on Twitter/X. The paper argues that DSA transparency, while pivotal, remains too incomplete to permit robust independent assessment, and calls for more meaningful and globally inclusive reporting requirements.

## Key Contributions

- First comparative empirical study of cross-lingual moderator workforce allocation across six DSA-regulated platforms.
- A novel methodology pairing DSA transparency disclosures with independently constructed, calibrated content-volume estimates to normalize moderator counts by language.
- Quantification of the number of EU users left without national-language moderation on specific platforms.
- Empirical extension of prior anecdotal/whistleblower reports (e.g., Haugen disclosures, Global Witness) on non-English moderation underinvestment.
- Concrete policy recommendations: mandate reporting of content volume per language, moderator workload capacity, harmful-content prevalence, and extend transparency obligations beyond the EU.

## Methods

The authors collected per-language moderator counts from DSA transparency reports (Summer 2023–Fall 2024), averaging across reporting periods and treating non-reported EU languages as having zero moderators. To make counts comparable, they normalized by content volume per language using independent datasets — the TwitterDay corpus (375M tweets from one day in September 2022) for Twitter/X and a random sample of ~26,000 YouTube videos for YouTube. Language identification relied on fastText applied to tweet text and video titles/descriptions, with inference scores calibrated against native-speaker annotations via isotonic regression. Bootstrap resampling (1,000 samples) generated expected post/video counts with confidence intervals. Twitter/X user locations were mapped to countries via the Google Geocoding API, and DSA-reported EU user counts were used to estimate how many users lack national-language moderation.

## Findings

- YouTube, Meta, and TikTok cover nearly all EU official languages; Twitter/X, LinkedIn, and Snapchat have multiple blind spots, especially in Southern, Eastern, and Northern Europe.
- Roughly 16M EU Twitter/X users (14%), 8M LinkedIn users (16%), and 7M Snapchat users (7%) have no moderators for their national language.
- On Twitter/X, blind-spot languages represent on average 31% of tweets in countries where they are official.
- On Twitter/X, only Bulgarian and German exceed English in moderators-per-content; Italian content is 78× more prevalent than Bulgarian yet has similar moderator counts.
- On Twitter/X, Portuguese, Arabic, and Spanish receive just 9%, 7%, and 7% of English's per-content allocation respectively.
- On YouTube most EU languages receive proportionally more moderators than English; only Spanish and Portuguese receive less, suggesting underinvestment in Latin American users.
- Global South languages average 55% of English's allocation on YouTube down to 7.5% on Twitter/X.
- There is a mismatch between interface-supported languages (e.g., Greek, Czech, Romanian) and moderation-staffed ones, and vice versa (e.g., Tagalog).

## Connections

This paper sits within the platform-governance strand focused on the DSA as an accountability and data-access instrument, complementing methodological critiques of the limits of platform transparency reporting such as [[Rieder2025-ju]] and broader treatments of moderation and platform governance like [[Katzenbach2026-sl2e]] and [[Gillespie2010-sla2]]. Its emphasis on linguistic and Global South inequities in moderation resource allocation extends questions of uneven platform accountability that also motivate work on platform data access and enforcement.
