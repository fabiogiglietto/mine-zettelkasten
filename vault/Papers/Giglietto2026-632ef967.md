---
title: "Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"
aliases: ["Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"]
authors: ["Fabio Giglietto", "Giada Marino"]
year: 2026
doi: 10.1177/29768624261452529
bibtex_key: Giglietto2026-632ef967
kind: own
topics: [platform-governance-data-access, social-media-engagement-metrics]
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

This paper leverages Meta's Privacy-Protected Full URLs Dataset to examine how user sharing on Facebook translates into actual viewership — a conversion historically opaque to outside researchers. Analyzing 130,448 highly circulated URLs shared in the US between 2017 and 2022, Giglietto and Marino show that while shares reliably predict views, this amplification is systematically dampened for content with highly partisan audiences and boosted for content from sources adhering to professional journalistic standards. Crucially, by re-estimating their model quarterly, they demonstrate that these effects fluctuate sharply in alignment with Facebook's known governance interventions — most notably the 2020 election "break the glass" measures. The central argument is that Facebook operates as an active curator whose algorithmic calibrations respond to political crises and reputational pressure, rather than a neutral conduit.

## Key Contributions

- Supplies large-scale empirical evidence of the share-to-view amplification relationship using view-level data previously unavailable to researchers.
- Distinguishes empirically between structural homophily effects and active algorithmic suppression as mechanisms limiting partisan reach, using temporal variation to favor the latter.
- Offers independent quantitative corroboration of Facebook's "break the glass" emergency interventions, previously known mainly through journalism and leaks.
- Extends a European amplification framework to the US context, incorporating Political Page Affinity and NewsGuard quality measures.
- Advances platform-studies methodology by detecting governance through temporal discontinuities in amplification coefficients.

## Methods

The authors use the Facebook Privacy-Protected Full URLs Dataset (v10) via Social Science One, covering January 2017–October 2022 and restricted to US engagement. Signal-to-noise quality filters reduced ~14.8 million URLs to 236,341, which were merged with NewsGuard scores to yield 130,448 URLs. They apply privacy-aware linear regression (the `lmdp` function from the PrivacyUnbiased R package) to correct for differential-privacy noise, with bootstrap variance estimation over 1,000 replications. Four nested models predict views from shares, audience partisan alignment strength, NewsGuard quality, and clicks as a control. The full model was re-estimated quarterly (2017-Q1 to 2021-Q3) to capture shifting governance regimes.

## Findings

- Each additional share is associated with roughly 56 additional views after controlling for clicks.
- A one-SD increase in audience partisan alignment corresponds to ~2.3–2.4 million fewer views, holding shares and clicks constant — a "partisan reach penalty."
- A one-point increase on NewsGuard's 100-point scale corresponds to ~28,700 additional views, independent of sharing volume.
- The shares-to-views rate fluctuated from ~71 views/share (2017-Q4, 2019-Q2) down to ~46 in 2020-Q3 during the election and pandemic.
- The partisan penalty intensified sharply in 2020-Q3 (~-2.90 million views), coinciding with reported "break the glass" interventions.
- The quality reward surged from ~31,500 views/point in 2020-Q2 to over 76,900 by mid-2021.
- The click coefficient stayed stable (6–7.5 views/click), contrasting with the volatility of shares and partisanship effects — suggesting curation targets amplification mechanisms, not raw demand.

## Connections

This work directly engages and partially challenges the Meta-partnered 2020 election studies by arguing that treating governance interventions as stable background conditions obscures their dynamic effect on visibility — see [[Gonzalez-Bailon2023-uy]], [[Guess2023-ai]], and [[Nyhan2023-gb]]. Its view-level exposure analysis complements [[Bakshy2015-rn]] on ideological reach and broader debates on amplification and curation in [[Gonzalez-Bailon2024-rq]]. It extends the authors' own line of work on coordinated sharing and problematic information circulation ([[Giglietto2022-b30e8b4e]], [[Giglietto2025-1765bb4f]], [[Giglietto2026-855a54cb]]), and sits within platform-governance scholarship on algorithmic gatekeeping alongside [[Gillespie2022-jx]] and [[Rieder2025-ju]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
