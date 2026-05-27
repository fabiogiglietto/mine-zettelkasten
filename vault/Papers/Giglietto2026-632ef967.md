---
title: "Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"
aliases: ["Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"]
authors: ["Fabio Giglietto", "Giada Marino"]
year: 2026
doi: 10.1177/29768624261452529
bibtex_key: Giglietto2026-632ef967
kind: own
topics: [platform-governance-and-data-access, polarization-partisanship-hyperpartisan-media]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1177/29768624261452529
podcast_url: 
pdf_available: true
discovery_date: 
---

# Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook

## Summary

This paper leverages Meta's Privacy-Protected Full URLs Dataset to examine how the act of sharing on Facebook translates into actual viewership across 130,448 highly circulated URLs in the US between 2017 and 2022. The authors show that while shares reliably predict views, this amplification is systematically dampened for content circulating among intensely partisan audiences and boosted for content from sources meeting professional journalistic standards. Critically, both effects fluctuate sharply over time in ways that align with Facebook's known governance interventions—especially the 2020 "break the glass" measures—supporting the argument that Facebook operates as an active algorithmic curator whose calibrations respond to political crises rather than as a neutral conduit.

## Key Contributions

- Large-scale empirical mapping of the share-to-view amplification relationship using viewing data previously inaccessible to outside researchers.
- Empirically distinguishes structural network homophily from active algorithmic suppression as mechanisms limiting partisan reach, using temporal variation as the discriminating evidence.
- Provides quantitative corroboration of Facebook's "break the glass" emergency interventions, previously documented mainly through leaks and reporting.
- Extends prior European amplification frameworks to the US context by integrating Political Page Affinity scores and NewsGuard quality ratings.
- Advances platform studies methodology by demonstrating how longitudinal discontinuities in amplification coefficients can serve as a detector of governance interventions.

## Methods

The authors analyze Meta's Privacy-Protected Full URLs Dataset (v10) via Social Science One, filtering ~14.8 million URLs down to 130,448 after applying signal-to-noise thresholds and merging with NewsGuard quality scores. They run privacy-aware linear regressions (using the `lmdp` function from PrivacyUnbiased, with 1000 bootstrap replications) to correct for differential privacy noise. Four nested models predict views from shares, audience partisan alignment strength, NewsGuard score, and clicks (as control). The full model is then re-estimated quarterly from 2017-Q1 to 2021-Q3 to capture temporal variation across governance regimes.

## Findings

- After controlling for clicks, each additional share corresponds to roughly 56 additional views.
- A one-SD increase in audience partisan alignment strength is associated with ~2.3–2.4 million fewer views, holding shares and clicks constant.
- Each one-point increase on the NewsGuard 100-point scale corresponds to ~28,700 additional views, independent of share volume.
- Amplification per share is volatile: peaking near 71 views/share in 2017-Q4 and 2019-Q2, falling to ~46 in 2020-Q3.
- The partisan penalty intensified sharply in 2020-Q3 (~-2.90 million views), aligning with reported "break the glass" interventions.
- The journalistic quality reward surged from ~31,500 additional views per quality point in 2020-Q2 to over 76,900 by mid-2021.
- The click coefficient remained remarkably stable (6–7.5 views/click), contrasting with the volatility of shares and partisanship coefficients.

## Connections

This paper engages directly with the Meta-partnered 2020 election studies, notably [[Bakshy2015-rn]] and the broader debate about whether platform algorithms simply mirror or actively shape exposure—pushing back on the assumption that governance interventions can be treated as stable background. It complements work using the same or similar URL/CrowdTangle infrastructures, including [[Rieder2025-ju]], [[Bouchaud2026-lr]], and [[Pierri2025-hm]], and contributes to a growing literature on hyperpartisan reach and algorithmic curation alongside [[Giglietto2022-b30e8b4e]], Edelson-adjacent platform studies, and [[Bak-Coleman2025-pm]]. Its methodological focus on detecting governance through temporal coefficient shifts resonates with platformization and data-access scholarship such as [[Rieder2026-pp]] and [[Helmond2026-ll]].
