---
title: "Research note: Examining potential bias in large-scale censored data"
aliases: ["Research note: Examining potential bias in large-scale censored data"]
authors: ["Jennifer Allen", "Markus Mobius", "David M. Rothschild", "Duncan J. Watts"]
year: 2021
doi: 10.37016/mr-2020-74
bibtex_key: Allen2021-ai
topics: [platform-data-governance, meta-science-of-misinformation-research]
citation_count: 20
open_access: false
source_url: https://doi.org/10.37016/mr-2020-74
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807386Z
---

# Research note: Examining potential bias in large-scale censored data

> Allen, J., Mobius, M., Rothschild, D. M., & Watts, D. J. (2021). Research note: Examining potential bias in large-scale censored data. *Harvard Kennedy School Misinformation Review*. https://doi.org/10.37016/mr-2020-74
>
> [View paper](https://doi.org/10.37016/mr-2020-74)

## Summary

This research note interrogates a widely used but methodologically fraught resource: Facebook's Social Science One URLs dataset, spanning over 10 trillion cells of shared-URL engagement data. While much attention has focused on the differential-privacy noise added to protect user privacy, the authors argue that a second, less-scrutinized protection — censoring any URL shared publicly fewer than 100 times — is the dominant source of bias in descriptive conclusions drawn from the data. By benchmarking the dataset against a nationally representative Nielsen web panel, they show that the censoring threshold systematically distorts prevalence estimates, inflating apparent consumption of news by roughly 2X and fake news by roughly 4X. The note is explicitly framed as a methodological caution, not a critique of the data-sharing effort itself, which remains uniquely large and valuable.

## Key Contributions

- Documents that **data censoring**, not differential-privacy noise, is the major and underappreciated source of bias in this large platform dataset.
- Quantifies the magnitude of bias in fake-news and news prevalence estimates from the Facebook URLs dataset.
- Triangulates the finding across three independent sources: external Nielsen matching, CrowdTangle public-share data, and an internal Facebook investigation.
- Offers concrete guidance for researchers (avoid comparisons across URL types or countries with differing public-sharing rates) and design recommendations (prefer differential privacy over censoring, or censor URL paths while retaining domains).

## Methods

The authors estimated the prevalence of fake news, credible news, and non-news clicks in the Facebook URLs dataset (Jan 2017–Dec 2018) using ~9,000 credible-news and 624 fake-news domain lists. They compared these against a nationally representative Nielsen desktop web panel, isolating Facebook newsfeed referrals via the `fbclid` URL parameter. To test the threshold-as-cause hypothesis, they matched a random sample of 1,000 Nielsen URLs against the Facebook dataset and used the CrowdTangle API to measure public shares (as a lower-bound proxy), tracking how the fake-news share shifted as the threshold moved from 0 to 100. Supplementary analyses included an internal Facebook investigation of fact-checker-labeled false URLs, an extension to non-news categories via the top 2,000 ComScore domains, and robustness checks on deduplication and referral definitions.

## Findings

- In the raw dataset, monthly clicks averaged 12% fake news, 32% credible news, 56% non-news; for December 2018 the dataset showed 10% / 38% / 52% versus a Nielsen estimate of 2.5% / 24% / 74% — a ~4X overestimate of fake news and ~1.7X of credible news.
- 84% of fake-news URLs in the Nielsen sample appeared in the Facebook dataset, versus 50% of credible-news and only 23% of non-news URLs — fake news is far more likely to clear the 100-share threshold.
- Restricting Nielsen URLs to those matched in the Facebook dataset reproduced the Facebook figures (7% / 39% / 55%), strongly supporting the threshold as the cause of the bias.
- CrowdTangle analysis reproduced similar results, with a large spike in non-news URLs at zero shares and fake news' share of content rising 45% between 1 and 100 shares.
- Facebook's internal analysis showed false URLs rose two orders of magnitude (0.00023% to 0.022% of unique URLs) with the threshold, and nearly all false-URL public shares came from a tiny set of high-volume URLs.
- Across categories, news (2.2X) and entertainment (1.4X) were overrepresented, while gaming (0.025X), retail, financial, and social media were sharply underrepresented — the censoring favors content optimized to be both clicked and publicly shared.
- Results were robust to deduplication and to a stricter referral definition.

## Connections

This note pairs closely with [[Allen2020-nj]], whose domain lists and prevalence-estimation approach it builds on directly, and sits within the broader misinformation-prevalence literature exemplified by [[Guess2021-ym]] and [[Pennycook2021-jq]]. Methodologically it belongs to the meta-scientific conversation about platform-data validity and industry–academic partnerships, connecting to critiques of CrowdTangle/platform data reliability such as [[Freelon2018-ao]] and to foundational agenda-setting for computational social science in [[Lazer2018-mm]]; see also platform-governance work like [[Gillespie2022-jx]] and [[van-Dijck2018-up]] on the infrastructural constraints these datasets embed.
