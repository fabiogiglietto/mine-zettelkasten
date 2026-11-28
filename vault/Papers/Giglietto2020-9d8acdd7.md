---
title: "It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"
aliases: ["It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"]
authors: ["Fabio Giglietto", "Nicola Righetti", "Luca Rossi", "Giada Marino"]
year: 2020
doi: 10.1080/1369118X.2020.1739732
bibtex_key: Giglietto2020-9d8acdd7
kind: own
topics: [coordinated-inauthentic-behavior, italian-electoral-communication]
citation_count: 265
open_access: true
source_url: https://doi.org/10.1080/1369118X.2020.1739732
podcast_url: 
pdf_available: true
discovery_date: 
editorial_notices: [correction]
---

# It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections

> [!note] Corrected
> - Correction (2020-04-21): [10.1080/1369118x.2020.1755558](https://doi.org/10.1080/1369118x.2020.1755558)

> Giglietto, F., Righetti, N., Rossi, L., & Marino, G. (2020). It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections. *Information, Communication & Society*. https://doi.org/10.1080/1369118X.2020.1739732
>
> [View paper](https://doi.org/10.1080/1369118X.2020.1739732)

## Summary

This paper argues that disinformation research should pivot away from content-veracity and bad-actor detection toward identifying *coordinated collective action*. Focusing on the run-up to the 2018 Italian general election and the 2019 European election, the authors operationalize Facebook's vague term "coordinated inauthentic behavior" as **coordinated link sharing behavior (CLSB)**: networks of pages, groups, and verified profiles that repeatedly share the same URLs near-simultaneously. Grounding the concept in scholarship on online coordination, participatory culture, and cloaked/deceptive identities, they show empirically that such coordinated networks are significantly more likely to spread problematic information and to include entities previously flagged as disinformation sources. A key nuance is the distinction between openly political networks and deceptively "non-political" ones, which exhibit different sharing strategies tied to plausibly different (ideological vs. commercial) motivations.

## Key Contributions

- Reframes Facebook's operational term "coordinated inauthentic behavior" within scholarly literature on coordination, participatory culture, and authenticity/cloaked identities.
- Introduces a reproducible algorithm and open-source R implementation for detecting CLSB from CrowdTangle data.
- Provides empirical evidence linking coordinated sharing to problematic information across two Italian elections, supporting an action-based (rather than content/actor-based) detection paradigm.
- Distinguishes ideological from commercial motivations by relating entity self-presentation (political vs. deceptive non-political) to domain-sharing breadth.
- Surfaces two structural ideal types of coordinated networks (centralized vs. clustered), raising new research questions.

## Methods

The authors built two datasets of Italian political news stories (N=84,815 in 2018; N=164,760 in 2019) from Google News, GDELT, and the Twitter Streaming API, then collected public Facebook/Instagram shares of those URLs within seven days via the CrowdTangle link endpoint. Their two-step algorithm first estimates a "near-simultaneous sharing" time threshold (median time for the fastest 10% of URLs to reach 50% of shares), then extracts entities that repeatedly co-share above the 90th frequency percentile. Shared domains were cross-referenced against Italian fact-checker blacklists (376 problematic domains) and entities against an Avaaz-derived list of 87 problematic pages. They used Risk Ratios to compare problematic-content proportions, qualitatively coded each entity's self-presentation to compute a network "politicalness" score, measured domain-sharing concentration with the Gini coefficient (correlated against politicalness via Spearman), and computed degree centralization and clustering coefficients.

## Findings

- Identified 24 coordinated networks (82 entities) in 2018 and 92 networks (606 entities) in 2019.
- Coordinated entities shared problematic domains 1.79× more often in 2018 and 2.22× more often in 2019 than non-coordinated entities.
- Coordinated entities were 19.24× (2018) and 23.19× (2019) more likely to appear on the Avaaz list of problematic pages.
- Network composition shifted over time: in 2018, 44% of networks were fully political, 27% non-political, 29% mixed; in 2019 mixed networks dominated (64%).
- Strong negative correlation between politicalness and domain-sharing concentration (r_s = −0.76 in 2018; −0.63 in 2019): openly political networks drew on diverse sources, while non-political networks narrowly amplified often-problematic domains.
- Networks clustered into two structural ideal types—highly centralized (star-like) or highly clustered—but neither politicalness nor Gini concentration explained which form emerged.

## Connections

This paper is foundational to the author team's subsequent program on coordinated link sharing behavior and its measurement, extended and refined in works such as [[Giglietto2020-6278a4aa]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], [[Giglietto2024-cbeb3f70]], and [[Marino2023-9137f448]], and within the broader Italian electoral communication strand including [[Iannelli2015-e0818c3e]]. Its action-based framing of coordination connects directly to detection and typology work on inauthentic and coordinated campaigns such as [[Nizzoli2020-cf]], [[Starbird2019-qv]], and [[Keller2019-nk]].
