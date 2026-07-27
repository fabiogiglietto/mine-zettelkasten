---
title: "It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"
aliases: ["It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"]
authors: ["Fabio Giglietto", "Nicola Righetti", "Luca Rossi", "Giada Marino"]
year: 2020
doi: 10.1080/1369118X.2020.1739732
bibtex_key: Giglietto2020-9d8acdd7
kind: own
topics: [coordinated-inauthentic-behavior, italian-political-communication-mine]
citation_count: 232
open_access: true
source_url: https://doi.org/10.1080/1369118X.2020.1739732
podcast_url: 
pdf_available: true
discovery_date: 
---

# It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections

> Giglietto, F., Righetti, N., Rossi, L., & Marino, G. (2020). It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections. *Information, Communication & Society*. https://doi.org/10.1080/1369118X.2020.1739732
>
> [View paper](https://doi.org/10.1080/1369118X.2020.1739732)

## Summary

This paper argues that disinformation research should pivot from detecting false content or bad actors toward detecting *coordinated collective action* on platforms. The authors introduce "coordinated link sharing behavior" (CLSB) — networks of Facebook pages, groups, and verified profiles that repeatedly share the same URLs near-simultaneously — and operationalize it via a reproducible algorithm applied to CrowdTangle data covering the 2018 Italian general election and 2019 European election. They show that entities engaged in CLSB are substantially more likely to share problematic domains and to be flagged as known disinformation sources, and that the mix of openly political vs. deceptively non-political entities in a network correlates with distinct sharing strategies suggestive of ideological vs. commercial motivations.

## Key Contributions

- Reframes Facebook's operational term "coordinated inauthentic behavior" in terms of prior scholarship on online coordination, participatory culture, and cloaked authenticity.
- Provides an open-source R algorithm for detecting CLSB from CrowdTangle link data, based on a data-driven "near-simultaneous" time threshold plus a repeated co-sharing filter.
- Delivers empirical evidence — across two Italian elections — that coordinated sharing is a strong signal for problematic information.
- Introduces the politicalness-vs.-domain-concentration relationship as a way to distinguish ideological from commercially motivated coordinated networks.
- Documents two recurring structural configurations (centralized vs. clustered) of coordinated networks, opening questions for later work.

## Methods

Two corpora of Italian political news URLs (84,815 in 2018; 164,760 in 2019) were compiled from Google News, GDELT, and the Twitter Streaming API, and their public Facebook shares harvested via CrowdTangle. A two-step algorithm identified entities that (1) shared URLs within a data-driven "near-simultaneous" window (median time for the fastest 10% of URLs to reach 50% of their shares) and (2) did so repeatedly above the 90th percentile. Domains were cross-checked against Italian fact-checker blacklists (376 domains) and entities against an Avaaz list of problematic pages; Risk Ratios compared coordinated vs. non-coordinated behavior. Each entity's self-presentation was qualitatively coded as political, non-political, or mixed to compute a network-level politicalness score, related via Spearman correlations to Gini-based domain concentration; degree centralization and clustering coefficients characterized network structure.

## Findings

- 24 coordinated networks (82 entities) in 2018 and 92 networks (606 entities) in 2019 were identified.
- Problematic domains were shared 1.79× (2018) and 2.22× (2019) more often by coordinated than by non-coordinated entities.
- Coordinated entities were 19.24× (2018) and 23.19× (2019) more likely to appear on Avaaz's list of problematic Facebook pages.
- Fully political networks dominated in 2018 (44%), while mixed political/non-political networks dominated in 2019 (64%).
- Politicalness was strongly negatively correlated with domain-sharing concentration (r_s = −0.76 in 2018; −0.63 in 2019): openly political networks amplified diverse sources, while non-political networks funneled traffic to a narrow set of (often problematic) domains — consistent with commercial motives.
- Networks fell into two structural ideal types (highly centralized or highly clustered), but neither politicalness nor Gini concentration predicted which configuration emerged.

## Connections

This paper is a foundational statement of the CLSB program developed further by the same research group, connecting directly to [[Giglietto2019-882f1900]], [[Giglietto2020-6278a4aa]], [[F2020-6278a4aa]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], [[Giglietto2024-cbeb3f70]], [[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], [[Giglietto2026-9b6a992d]], [[Marino2024-2fbc690f]], and [[Rossi2023-847d5a9f]], and to related Italian-context work in [[Iannelli2015-e0818c3e]] and [[Righetti2025-sl2a]]. It also anchors a broader action-based detection literature engaged by [[Graham2025-gp]], [[Graham2026-fb]], [[Luceri2025-tr]], [[Minici2024-tf]], [[Kulichkina2025-sl09]], and [[Starbird2025-jj]], and its distinction between ideological and commercial coordination echoes themes in [[Askanius2026-de]] and Bastos2025-ol.
