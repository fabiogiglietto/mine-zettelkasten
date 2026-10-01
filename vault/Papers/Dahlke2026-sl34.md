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
topics: [information-disorder-and-fake-news, computational-political-media-influence]
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

This paper challenges the dominant "direct referrer paradigm" in misinformation research — the practice of counting only those misinformation visits immediately preceded by a social media click. The authors argue this systematically undercounts platforms' true role because it ignores indirect pathways (through intermediary sites) and persistent behavioral effects. They propose an "embedded referrer paradigm," operationalized through counterfactual simulation that estimates what misinformation exposure would look like if a given platform did not exist. Using three months of passive web-browsing data (~21 million visits) from 1,240 Americans during the 2020 U.S. election across seven platforms, they find platform effects are 1.5 to 15+ times larger under the embedded paradigm. Crucially, removing platforms would also disproportionately cut high-quality news exposure, complicating any simple "ban the platforms" policy logic.

## Key Contributions

- Introduces the **embedded referrer paradigm** as a theoretical alternative to the prevailing direct referrer paradigm for conceptualizing platforms' role in information exposure.
- Develops a **simulation methodology** combining experimentally derived diversion ratios with individual-level multinomial logit transition matrices to model counterfactual platform-removal scenarios (~3.2 million counterfactual + observed paths).
- Extends analysis beyond the usual Facebook/Twitter focus to **seven platforms**, documenting systematic underestimation in prior work and partisan-asymmetric effects.
- Provides **counterfactual evidence for policy debates**, quantifying the tradeoff between reduced misinformation and reduced high-quality news.
- Releases data and a generalizable framework (applicable to partisan news, hateful content, and other intermediate states).

## Methods

Passive web-browsing data was collected via YouGov Pulse from 1,240 U.S. adults (Aug–Dec 2020), covering ~21 million visits across devices. Domains were categorized as social media, misinformation (NewsGuard, fact-checker and academic lists), high/low-quality news (Lin et al. PCA quality scores), or other, with ideological labels. The **direct referrer** analysis simply measured the share of misinformation visits immediately preceded by each platform. The **embedded referrer** analysis used counterfactual simulation: diverting paths away from a target platform using diversion ratios from Aridor (2023), then continuing simulated paths via per-user multinomial logit transition matrices. Multi-level ML regressions (clustered by participant and path) compared observed vs. counterfactual worlds, with subgroup analyses by partisanship and device. Methodologically it draws inspiration from gene-knockout studies, advertising attribution, and clickstream/Markov-chain analyses.

## Findings

- **Facebook**: directly preceded 9.25% of misinformation visits, but the embedded estimate shows 14.07% more misinformation visits in the observed world than without Facebook.
- **Twitter**: directly preceded 2.17%, yet removal yields a 12.27% reduction (~5.5x larger).
- **Reddit**: directly preceded <0.2%, yet removal reduces non-ideological misinformation visits by 18.22% overall and 55.14% among Independents.
- **YouTube**: effect on Democrats' exposure to liberal misinformation is 32.09% (embedded) vs. 2.06% (direct) — roughly 16x larger.
- Republicans have the highest baseline exposure (55.4% exposed; 79.1 mean visits) versus Democrats (35.9%; 13.7) and Independents (45.2%; 35.8).
- Device matters: Facebook/Twitter effects concentrate among desktop users; YouTube effects appear more on mobile.
- Platform removal disproportionately cuts high-quality news: e.g., Facebook removal reduces 73.3 high-quality news visits per misinformation visit reduced; ratios exceed 10,000 for Instagram on non-ideological content.
- Smaller platforms (Instagram, Snapchat, TikTok) show statistically indistinguishable estimates between paradigms, likely due to low sample volume.

## Connections

This work sits squarely in the empirical tradition of browsing-trace studies of misinformation exposure, extending and critiquing methods used in [[Guess2019-ym]], [[Grinberg2019-ua]], and [[Allen2020-nj]] on who actually encounters fake news. Its finding that most misinformation reaches a concentrated, partisan subset echoes [[Grinberg2019-ua]] and the exposure-measurement concerns in [[Allen2024-av]] and [[Gonzalez-Bailon2024-rq]], while its platform-referral framing connects to referral-tracing work such as [[DeVerna2025-dl]] and the broader conceptual literature on misinformation prevalence and harm in [[Lazer2018-mm]] and [[Vosoughi2018-at]]. The policy tradeoff it surfaces — that removing platforms would also cut high-quality news — adds a counterfactual nuance relevant to platform-governance debates discussed in [[Gillespie2022-jx]].
