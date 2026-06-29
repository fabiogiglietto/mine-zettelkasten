---
title: "Multi-Platform Referrers of Misinformation: A Comparative Analysis of Misinformation Visits Referred by Facebook, Twitter, Instagram, Reddit, YouTube, Snapchat, and TikTok"
aliases: ["Multi-Platform Referrers of Misinformation: A Comparative Analysis of Misinformation Visits Referred by Facebook, Twitter, Instagram, Reddit, YouTube, Snapchat, and TikTok"]
authors: ["Ross Dahlke", "Ryan C. Moore", "Danya Adib-Azpeitia", "Johan Ugander", "Jeffrey T. Hancock"]
year: 2026
doi: 10.1080/10584609.2026.2679492
bibtex_key: Dahlke2026-sl34
kind: team
submitted_by: "GiadaM. / Uniurb"
slack_permalink: https://minesmd.slack.com/archives/C0BDU82EBHQ/p1782741554133369
topics: [information-disorder, platform-governance-data-access]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/10584609.2026.2679492
podcast_url: 
pdf_available: true
discovery_date: 2026-06-29T16:39:38.251537Z
---

# Multi-Platform Referrers of Misinformation: A Comparative Analysis of Misinformation Visits Referred by Facebook, Twitter, Instagram, Reddit, YouTube, Snapchat, and TikTok

> Dahlke, R., Moore, R. C., Adib-Azpeitia, D., Ugander, J., & Hancock, J. T. (2026). Multi-Platform Referrers of Misinformation: A Comparative Analysis of Misinformation Visits Referred by Facebook, Twitter, Instagram, Reddit, YouTube, Snapchat, and TikTok. *Political Communication*. https://doi.org/10.1080/10584609.2026.2679492
>
> [View paper](https://doi.org/10.1080/10584609.2026.2679492)

## Summary

This paper argues that the standard "direct referrer paradigm" — counting only misinformation visits immediately preceded by a click from a social media platform — systematically understates how much platforms shape misinformation exposure. Dahlke and colleagues propose an "embedded referrer paradigm" that captures indirect and delayed pathways via intermediary sites and persistent browsing habits, operationalized through counterfactual simulations of what each user's browsing would have looked like had a given platform not existed. Using passive web-tracking data from 1,240 Americans across the 2020 U.S. election, they show that estimated platform effects on misinformation exposure are 1.5× to 15+× larger under the embedded paradigm, that these effects are partisan-asymmetric across platforms, but that removing any platform would also strip away substantially more high-quality news than misinformation.

## Key Contributions

- Introduces the **embedded referrer paradigm** as a theoretical alternative to the direct referrer paradigm that dominates empirical misinformation research.
- Develops a counterfactual simulation methodology that fuses experimentally derived diversion ratios with individual-level multinomial logit transition matrices to model platform-removal scenarios.
- Provides comparative empirical evidence across seven platforms (Facebook, Twitter, Instagram, Reddit, YouTube, Snapchat, TikTok), rather than the usual Facebook/Twitter focus.
- Quantifies the high-quality-news-to-misinformation tradeoff of platform-removal policies, offering a counterfactual lens on platform-ban proposals.
- Releases data and a generalizable framework extensible to other content categories and intermediate states.

## Methods

- Passive web-browsing data via YouGov Pulse from 1,240 U.S. adults, Aug–Dec 2020 (~21M visits, 395,936 sessions, across desktop/mobile/tablet).
- Domain categorization combining NewsGuard, fact-checker lists, prior academic lists, and Lin et al. (2023) PCA quality scores; ideological labels from NewsGuard, Robertson et al. (2018), and hand-coding.
- Direct referrer analysis (share of misinformation visits immediately preceded by each platform) compared against embedded referrer analysis using counterfactual path simulation: paths are diverted away from a target platform using Aridor (2023) diversion ratios, then continued via per-user multinomial logit transition matrices, generating ~3.17M simulated paths across seven platform-removal scenarios.
- Multi-level regressions (clustered by participant and original path) compare observed vs. counterfactual misinformation visits, with subgroup analyses by partisanship and device.

## Findings

- Facebook directly preceded 9.25% of misinformation visits, but its removal would reduce misinformation visits by 14.07% under the embedded paradigm.
- Twitter directly preceded only 2.17% of misinformation visits, yet its removal yields a 12.27% reduction (~5.5× larger).
- Reddit directly preceded <0.2% of misinformation visits, but its removal reduces non-ideological misinformation visits by 18.22% overall and 55.14% among Independents.
- YouTube's effect on Democrats' exposure to liberal misinformation is 32.09% (embedded) vs. 2.06% (direct) — roughly 16× larger.
- Twitter strongly drives Republican exposure to conservative misinformation; YouTube disproportionately drives Democratic exposure to liberal misinformation.
- Republicans show the highest baseline misinformation exposure (55.4% exposed; 79.1 mean visits among exposed) vs. Democrats (35.9%; 13.7) and Independents (45.2%; 35.8).
- Facebook/Twitter effects concentrate on desktop; YouTube effects concentrate on mobile.
- Platform removal strips away far more high-quality news than misinformation: e.g., 73.3 high-quality news visits lost per misinformation visit averted for Facebook, with ratios exceeding 10,000 for Instagram on non-ideological content.
- Smaller platforms (Instagram, Snapchat, TikTok) show statistically indistinguishable estimates across paradigms, likely due to low sample volumes.

## Connections

This paper extends a line of passive-tracking, behavioral-trace work on real-world misinformation exposure represented by [[Gonzalez-Bailon2024-rq]], [[Allen2025-ot]], and [[Moran2025-qn]], pushing back on the narrow direct-referrer operationalization those and related studies often rely on. Its counterfactual, multi-platform framing complements platform-comparative misinformation analyses such as [[DeVerna2025-dl]] and [[Pierri2025-hm]], and its findings about tradeoffs between misinformation and high-quality news bear directly on platform-governance debates engaged by [[Bak-Coleman2025-pm]] and [[Budak2024-ef]].
