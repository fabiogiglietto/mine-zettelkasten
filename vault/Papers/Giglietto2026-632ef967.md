---
title: "Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"
aliases: ["Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"]
authors: ["Fabio Giglietto", "Giada Marino"]
year: 2026
doi: 10.1177/29768624261452529
bibtex_key: Giglietto2026-632ef967
kind: own
topics: [platform-governance-data-access, polarization-hybrid-media]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1177/29768624261452529
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3
pdf_available: true
discovery_date: 
---

# Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook

> Giglietto, F., & Marino, G. (2026). Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook. *Platforms & Society*. https://doi.org/10.1177/29768624261452529
>
> [View paper](https://doi.org/10.1177/29768624261452529)

## Summary

This paper leverages Meta's Privacy-Protected Full URLs Dataset to analyze how sharing translates into actual viewership for 130,448 heavily circulated URLs on US Facebook between 2017 and 2022. The authors show that while shares reliably predict views, the amplification is systematically dampened for content shared by highly partisan audiences and boosted for content from journalistically credible sources. Crucially, these coefficients are not stable: they shift sharply around known governance moments (notably the 2020 election "break the glass" measures and the pandemic), which the authors interpret as evidence that Facebook operates as an active algorithmic curator whose interventions leave measurable temporal fingerprints, rather than as a neutral distribution conduit.

## Key Contributions

- Large-scale empirical mapping of the share-to-view relationship using viewership data that has historically been inaccessible to external researchers.
- Analytical strategy that uses *temporal variation* in amplification coefficients to distinguish structural network homophily from active algorithmic suppression, favoring the latter.
- Independent quantitative corroboration of Facebook's "break the glass" emergency interventions previously known chiefly via leaks and journalism.
- Extension of European amplification frameworks (Trilling et al.) to the US, integrating Political Page Affinity and NewsGuard journalistic quality scores.
- A longitudinal methodological template for detecting platform governance via discontinuities in visibility coefficients.

## Methods

- Data: Meta's Facebook Privacy-Protected Full URLs Dataset (v10) via Social Science One, restricted to US engagement, Jan 2017–Oct 2022.
- Signal-to-noise filtering (Buntain et al.; Evans & King) reduced ~14.8M URLs to 236,341, then merged with NewsGuard scores to yield 130,448 URLs.
- Privacy-aware linear regression using the `lmdp` function from the PrivacyUnbiased R package, correcting for differential-privacy noise, with 1000-replication bootstrap variance estimation.
- Four nested models predicting views from shares, audience partisan alignment strength, NewsGuard quality, and clicks (as control).
- Quarterly re-estimation from 2017-Q1 to 2021-Q3 to trace shifting governance regimes.

## Findings

- Each additional share is associated with roughly 56 additional views once clicks are controlled.
- A one-SD increase in audience partisan alignment strength corresponds to ~2.3–2.4 million *fewer* views, holding shares and clicks constant.
- A one-point rise on NewsGuard's 100-point scale yields ~28,700 additional views, independent of sharing volume.
- Amplification per share fluctuated markedly, peaking near 71 views/share (2017-Q4, 2019-Q2) and dropping to ~46 in 2020-Q3.
- The partisan penalty spiked to about −2.90 million views in 2020-Q3, aligning with reported "break the glass" measures.
- The journalistic-quality reward surged from ~31,500 to over 76,900 additional views per quality point between 2020-Q2 and mid-2021.
- The click coefficient stayed steady (~6–7.5 views/click), highlighting that volatility is concentrated in shares and partisanship, not baseline engagement.

## Connections

This work speaks directly to ongoing debates about the Meta-partnered 2020 election studies and the interpretive limits of treating platform governance as a static backdrop, connecting to platform-audit and data-access scholarship such as [[Bouchaud2026-lr]], [[Bouchaud2026-np]], [[Rieder2026-pp]], and [[Rieder2025-ju]]. Its authorship and methodological lineage tie it to a broader program on coordinated sharing and news amplification represented by [[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], [[Giglietto2026-855a54cb]], [[Giglietto2022-b30e8b4e]], [[Giglietto2019-882f1900]], [[Giglietto2019-e9be81c1]], and [[Marino2023-9137f448]]. On the substantive side, its findings on partisan reach penalties and quality rewards intersect with work on exposure, misinformation circulation, and algorithmic curation such as [[Bakshy2015-rn]], [[Allen2025-ot]], [[Pierri2025-hm]], and [[Bak-Coleman2025-pm]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
