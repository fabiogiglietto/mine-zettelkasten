---
title: "Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"
aliases: ["Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"]
authors: ["Fabio Giglietto", "Giada Marino"]
year: 2026
doi: 10.1177/29768624261452529
bibtex_key: Giglietto2026-632ef967
kind: own
topics: [platform-governance-and-content-moderation, italian-electoral-media-coverage]
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

This paper examines how user sharing on Facebook translates into actual viewership, using Meta's Privacy-Protected Full URLs Dataset to analyze 130,448 highly circulated URLs shared in the US between 2017 and 2022. The authors show that while shares reliably predict views, this amplification is systematically dampened for content circulating among highly partisan audiences and boosted for content from journalistically reputable sources. Crucially, these effects are not stable: they fluctuate in tight alignment with known Facebook governance interventions—especially the 2020 election "break the glass" measures—providing quantitative corroboration that Facebook operates as an active curator whose algorithmic calibrations shift with political and reputational pressures, rather than a neutral conduit.

## Key Contributions

- Delivers large-scale empirical evidence on share-to-view amplification using viewing data previously inaccessible to independent researchers.
- Uses temporal variation in coefficients to empirically distinguish structural network homophily from active algorithmic suppression as explanations for reduced partisan reach.
- Offers independent quantitative corroboration of Facebook's "break the glass" emergency interventions previously documented only through leaks and journalism.
- Extends European amplification frameworks (Trilling et al.) to the US context by integrating Political Page Affinity and NewsGuard quality measures.
- Advances platform governance methodology by demonstrating how longitudinal discontinuities in amplification coefficients can serve as fingerprints of platform intervention.

## Methods

The authors analyze Meta's Facebook Privacy-Protected Full URLs Dataset (v10, 2017–2022), filtering ~14.8M URLs down to 130,448 via signal-to-noise thresholds and merger with NewsGuard scores. They fit four nested privacy-aware linear regressions (using the `lmdp` function from PrivacyUnbiased, with 1000 bootstrap replications) predicting URL views from shares, audience partisan alignment strength, NewsGuard quality, and clicks as a control. The full model is re-estimated quarterly from 2017-Q1 to 2021-Q3 to trace coefficient shifts across governance regimes.

## Findings

- Each additional share corresponds to ~56 additional views after controlling for clicks.
- A one-SD increase in audience partisan alignment strength is associated with ~2.3–2.4 million fewer views, holding shares and clicks constant.
- A one-point NewsGuard increase (on 100-point scale) yields ~28,700 additional views independent of sharing volume.
- The share-to-view amplification rate ranged from ~71 views/share (2017-Q4, 2019-Q2) down to ~46 during the 2020 election/pandemic period.
- The partisan penalty intensified sharply in 2020-Q3 (~-2.90 million views), aligning with reported "break the glass" interventions.
- The journalistic quality reward more than doubled, from ~31,500 additional views/quality point in 2020-Q2 to over 76,900 by mid-2021.
- Click coefficients remained stable (6–7.5 views/click) across the entire period, in stark contrast to the volatility of share and partisanship coefficients.

## Connections

This paper extends the author's ongoing program on coordinated sharing and problematic information circulation on Facebook ([[Giglietto2022-b30e8b4e]], [[Giglietto2019-882f1900]], [[Giglietto2019-e9be81c1]], [[Giglietto2025-1e9a0917]], [[Giglietto2026-855a54cb]]) into the domain of platform curation and visibility. It engages directly with the Meta-partnered 2020 election studies exemplified by [[Bakshy2015-rn]], reframing their treatment of algorithmic conditions as static, and complements work on data access constraints and platform gatekeeping such as [[Rieder2025-ju]], [[Rieder2026-pp]], and [[Bouchaud2026-lr]]. It also speaks to broader debates on news quality, algorithmic amplification, and partisan asymmetry visible in [[Allen2025-ot]], [[Pierri2025-hm]], and [[Gaisbauer2025-by]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
