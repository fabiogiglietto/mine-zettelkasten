---
title: "Language Disparities in Moderation Workforce Allocation by Social Media Platforms"
aliases: ["Language Disparities in Moderation Workforce Allocation by Social Media Platforms"]
authors: ["Manuel Tonneau", "Diyi Liu", "Ryan McGrady", "Kevin Zheng", "Ralph Schroeder", "Ethan Zuckerman", "Scott Hale"]
year: 2025
doi: 10.31235/osf.io/amfws_v2
bibtex_key: Tonneau2025-bv
topics: [platform-governance-data-access, platform-engagement-affordances]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31235/osf.io/amfws_v2
podcast_url: 
pdf_available: true
discovery_date: 2025-08-15T00:00:00Z
---

# Language Disparities in Moderation Workforce Allocation by Social Media Platforms

> Tonneau, M., Liu, D., McGrady, R., Zheng, K., Schroeder, R., Zuckerman, E., & Hale, S. (2025). Language Disparities in Moderation Workforce Allocation by Social Media Platforms. https://doi.org/10.31235/osf.io/amfws_v2
>
> [View paper](https://doi.org/10.31235/osf.io/amfws_v2)

## Summary

This paper offers the first comparative empirical analysis of how six major social media platforms — YouTube, Meta, TikTok, Twitter/X, Snapchat, and LinkedIn — distribute their human content moderators across languages. Leveraging transparency disclosures mandated by the EU's Digital Services Act (DSA), the authors document substantial cross-lingual disparities in both language coverage and moderator-to-content ratios. They find that millions of EU users on smaller platforms post in languages with no human oversight, and that even where moderators exist, languages predominantly spoken in the Global South (Spanish, Portuguese, Arabic) receive proportionally far fewer moderators than English. The paper frames DSA transparency as a pivotal but incomplete advance and calls for more meaningful, globally inclusive reporting requirements.

## Key Contributions

- First comparative empirical study of cross-lingual moderator workforce allocation across six DSA-regulated platforms.
- A novel methodology that normalizes raw moderator counts by independently estimated, calibrated content volume per language.
- Quantification of how many EU users are left without national-language moderation on specific platforms.
- Empirical evidence extending prior disclosures (e.g., Haugen leaks, Global Witness) on underinvestment in non-English moderation.
- Concrete policy recommendations: require platforms to report content volume per language, moderator workload capacity, harmful-content prevalence, and to extend obligations beyond the EU.

## Methods

The authors collected moderator counts per language from DSA transparency reports (Summer 2023–Fall 2024), averaging across reporting periods and treating non-reported EU languages as having zero moderators. To normalize by content volume, they drew on independent datasets — the TwitterDay corpus (375M tweets) for Twitter/X and a random sample of ~26,000 YouTube videos — applying fastText language identification calibrated via isotonic regression against native-speaker annotations. Bootstrap resampling (1,000 samples) produced per-language post/video estimates with confidence intervals. Twitter/X user locations were geocoded to countries via the Google Geocoding API, and DSA-reported country-level user counts were used to estimate populations lacking national-language moderation, categorized using the UN geoscheme.

## Findings

- YouTube, Meta, and TikTok cover nearly all EU official languages; Twitter/X, LinkedIn, and Snapchat have multiple blind spots, especially in Southern, Eastern, and Northern Europe.
- ~16M EU Twitter/X users (14%), ~8M LinkedIn users (16%), and ~7M Snapchat users (7%) have no moderators for their national language.
- Blind-spot languages represent on average 31% of tweets in countries where they are official.
- On Twitter/X, only Bulgarian and German exceed English in moderators-per-content; Italian and Bulgarian have similar counts despite Italian content being 78× more prevalent.
- On Twitter/X, Portuguese, Arabic, and Spanish receive only 9%, 7%, and 7% of English's per-content allocation.
- On YouTube, most EU languages get proportionally more moderators than English, with Spanish and Portuguese the exceptions — signalling reduced investment in Latin American user bases.
- Global South languages average 55% of English's allocation on YouTube, falling to just 7.5% on Twitter/X.
- Interface language support and moderation staffing frequently mismatch (e.g., Greek, Czech, Romanian supported in UI but unmoderated; Tagalog moderated but unsupported in UI).

## Connections

This study sits within the platform-governance and data-access strand that treats DSA transparency disclosures as a research resource and a contested object of accountability; it resonates with work interrogating the adequacy and interpretation of platform transparency and data-access regimes such as [[Rieder2025-ju]] and [[Rieder2026-pp]]. Its focus on content moderation as infrastructural labour and governance connects to broader moderation scholarship referenced here, though the specific cross-lingual, Global South inequity angle is largely distinct from the engagement- and misinformation-oriented papers in these topics.
