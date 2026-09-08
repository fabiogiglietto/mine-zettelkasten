---
title: "Political science. Exposure to ideologically diverse news and opinion on Facebook"
aliases: ["Political science. Exposure to ideologically diverse news and opinion on Facebook"]
authors: ["Eytan Bakshy", "Solomon Messing", "Lada A. Adamic"]
year: 2015
doi: 10.1126/science.aaa1160
bibtex_key: Bakshy2015-rn
topics: [political-polarization-partisanship, computational-political-media-influence]
citation_count: 2275
open_access: false
source_url: https://doi.org/10.1126/science.aaa1160
podcast_url: 
pdf_available: true
discovery_date: 2015-06-15T00:00:00Z
---

# Political science. Exposure to ideologically diverse news and opinion on Facebook

> Bakshy, E., Messing, S., & Adamic, L. A. (2015). Political science. Exposure to ideologically diverse news and opinion on Facebook. *Science*, *348*, 1130–1132. https://doi.org/10.1126/science.aaa1160
>
> [View paper](https://doi.org/10.1126/science.aaa1160)

## Summary

This landmark study offers the first large-scale, platform-internal measurement of how ideologically diverse political news reaches Facebook users, tracing content through three sequential stages: the composition of friend networks, the News Feed ranking algorithm, and individual click choices. Drawing on 10.1 million U.S. users who self-reported ideological affiliation, the authors decompose "filter-bubble-like" effects into their constituent causes. Their central finding pushes back against strong "echo chamber" and "filter bubble" narratives: while friend networks are homophilous, they retain substantial cross-cutting ties, and individual choices about what to click suppress ideologically discordant exposure more than the algorithm does. At the same time, the paper documents meaningful, asymmetric ideological sorting in social media news consumption.

## Key Contributions

- First large-scale, platform-internal measurement separating friend network, algorithmic ranking, and individual choice stages of ideological exposure on Facebook.
- Introduces an "alignment" (A) measure of content partisanship based on the ideological mix of an article's sharers, validated against known partisan outlets.
- Empirically disentangles network composition, algorithmic curation, and user selection — finding individual choice plays a larger role than the algorithm.
- Provides an empirical counterweight to strong echo-chamber claims while documenting liberal–conservative asymmetries.
- Released replication code, classifiers, and aggregate statistics via Harvard Dataverse.

## Methods

The authors built a deidentified dataset of 10.1 million active U.S. users with self-reported ideology over six months (July 2014–January 2015). They collected roughly 7 million shared URLs, classifying them as "hard" (politics, national, world news) versus "soft" using an SVM trained on unigram, bigram, and trigram features. Analysis focused on ~226,000 hard-content URLs shared by at least 20 declared users, yielding ~3.8 billion potential exposures, 903 million News Feed exposures, and 59 million clicks. They decomposed exposure into stages — random baseline, network potential, algorithmically ranked feed, and clicked content — and computed risk ratios for cross-cutting versus consistent content, adjusting for News Feed position effects.

## Findings

- Friend networks are homophilous but contain substantial cross-cutting ties: the median liberal has ~20% conservative friends, the median conservative ~18% liberal friends.
- Under random sharing, liberals would see ~45% cross-cutting content and conservatives ~40%; in practice, liberals' friends share 24% cross-cutting hard news versus 35% for conservatives — evidence of asymmetric sorting.
- Algorithmic ranking modestly reduces cross-cutting exposure (5% for conservatives, 8% for liberals).
- Individual click behavior reduces cross-cutting consumption more strongly (17% for conservatives, 6% for liberals), even after controlling for feed position.
- Users click on only ~7% of available hard-content links, leaving considerable headroom for greater cross-ideological consumption.
- Network composition is the single largest factor shaping the ideological mix of news users encounter.

## Connections

This foundational study anchors much subsequent empirical work challenging strong echo-chamber and filter-bubble claims, and its emphasis on user choice over algorithmic curation is echoed in later platform-scale investigations such as [[Allen2025-ot]] and [[Eady2025-vm]]. Its documentation of asymmetric ideological sorting and cross-cutting exposure connects to broader work on polarization and media diversity including [[Falkenberg2026-ka]] and [[Fletcher2026-lv]].
