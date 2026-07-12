---
title: "Does the method affect the outcome? How measures of partisan slant of media outlets and affective polarization drive results about polarization in the United States"
aliases: ["Does the method affect the outcome? How measures of partisan slant of media outlets and affective polarization drive results about polarization in the United States"]
authors: ["Christian Schemer", "Klara Langmann", "Ariel Hasell", "Brian Weeks"]
year: 2026
doi: 10.1080/10584609.2026.2699105
bibtex_key: Schemer2026-mh
topics: [polarization-partisan-media, elections-political-communication]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/10584609.2026.2699105
podcast_url: 
pdf_available: true
discovery_date: 2026-07-12T06:36:29.875358Z
---

# Does the method affect the outcome? How measures of partisan slant of media outlets and affective polarization drive results about polarization in the United States

> Schemer, C., Langmann, K., Hasell, A., & Weeks, B. (2026). Does the method affect the outcome? How measures of partisan slant of media outlets and affective polarization drive results about polarization in the United States. *Political Communication*, 1–25. https://doi.org/10.1080/10584609.2026.2699105
>
> [View paper](https://doi.org/10.1080/10584609.2026.2699105)

## Summary

This paper interrogates a methodological blind spot in political communication research: how the *choice* of measures for both partisan media slant and polarization shapes conclusions about whether partisan media are a democratic problem. Using three-wave panel data from the 2020 U.S. presidential election and specification curve analysis (SCA), the authors run 504 combinations of independent-variable operationalizations (17 media partisanship scores yielding 42 specifications) and dependent-variable operationalizations (12 measures of affective and belief polarization). Their central argument is that methodological decisions substantially move the *strength* and statistical significance of the media–polarization relationship—but rarely its direction—so apparent contradictions across the literature reflect measurement variation rather than genuinely conflicting effects.

## Key Contributions

- Systematic, empirical demonstration via a 504-specification SCA of how measurement choices shape substantive conclusions about partisan media and polarization.
- Quantifies the inflationary effect of audience-based partisanship scores relative to content-based scores.
- Reveals partisan and candidate-level asymmetries obscured by bipolar and difference-score measures.
- Offers concrete best practices: justify measurement choices, run sensitivity checks, report both bipolar and disaggregated results, and prefer content-based measures when studying content effects.
- Contributes to the normative debate over the seriousness of partisan media effects by showing that interpretations hinge on method.

## Methods

- Original YouGov three-wave online panel during the 2020 election (Sept 24–Oct 30, 2020); wave-1 N = 1,800, with 1,401 reinterviewed in wave 2.
- Media use captured with a list-frequency technique across 63 U.S. news outlets (both usage and frequency).
- Seventeen Media Partisanship Scores drawn from prior work, spanning analytic content-based (e.g., Groseclose, Gentzkow), holistic content-based (e.g., Budak, AllSides, MBFC), and audience-based (e.g., Bakshy, Robertson, Pew, Kim) methods—producing 42 IV specifications via weighting and categorization.
- Twelve DV specifications: nine affective polarization measures (feeling thermometers and trust for Trump, Biden, and supporters, as single and difference scores) plus three belief polarization measures.
- SCA using the `specr` R package across all 504 combinations, with variance decomposition; robustness checks excluding Independents and lagged-DV regressions for over-time effects.

## Findings

- Relationships were mostly positive: more conservative diets predicted greater Trump favorability, trust, and pro-Trump misperceptions.
- Coefficients varied widely (mean b = .33); the largest significant estimate (b = .47) was nearly seven times the smallest (b = .07).
- Audience-based scores produced the largest coefficients (M = .35); analytic content-based the smallest (Groseclose M = .21, Gentzkow M = .26); holistic in between (M = .33)—with notable within-category variation.
- Categorical scores yielded larger estimates than non-categorical ones; frequency weighting mostly mattered little.
- About 56% of coefficient variation came from the MPS choice and 42% from the DV choice.
- Disaggregating bipolar scores exposed asymmetry: conservative diets showed stronger associations (|M| = .24) than liberal diets (M = -.19), with centrist diets small or nonsignificant.
- Trust and misperception measures produced stronger coefficients than feeling thermometers.
- Lagged (longitudinal) estimates were consistently small (largest b = .06), and excluding Independents reduced estimates by ~20%.

## Connections

This is primarily a methodological and measurement contribution to the partisan-media-and-polarization literature, and its concerns about audience-based versus content-based slant measures resonate with work on exposure and audience composition in [[Bakshy2015-rn]] and network-level exposure studies such as [[Gonzalez-Bailon2024-rq]]. Its focus on affective polarization dynamics connects to [[Arceneaux2026-xk]]. None of the other listed papers engage directly with specification curve analysis or slant measurement, so the intellectual links are otherwise thin.
