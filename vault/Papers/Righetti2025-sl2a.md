---
title: "CooRTweet: A Generalized R Software for Coordinated Network Detection"
aliases: ["CooRTweet: A Generalized R Software for Coordinated Network Detection"]
authors: ["Nicola Righetti", "Paul Balluff"]
year: 2025
doi: 10.5117/ccr2025.1.7.righ
bibtex_key: Righetti2025-sl2a
kind: team
submitted_by: "Nicola Righetti"
slack_permalink: https://minesmd.slack.com/archives/C0BDU82EBHQ/p1783507431459259
topics: [coordinated-inauthentic-behavior, digital-methods-social-science]
citation_count: 3
open_access: false
source_url: https://doi.org/10.5117/ccr2025.1.7.righ
podcast_url: 
pdf_available: true
discovery_date: 2026-07-08T13:08:04.166484Z
---

# CooRTweet: A Generalized R Software for Coordinated Network Detection

> Righetti, N., & Balluff, P. (2025). CooRTweet: A Generalized R Software for Coordinated Network Detection. *Computational Communication Research*. https://doi.org/10.5117/ccr2025.1.7.righ
>
> [View paper](https://doi.org/10.5117/ccr2025.1.7.righ)

## Summary

This paper introduces **CooRTweet**, an open-source R package (available on CRAN) for detecting coordinated behavior on and across social media platforms. The authors ground the tool in a deliberately minimal, abstract definition of coordinated behavior — the repeated near-synchronous sharing of any uniquely identifiable object by a stable set of accounts — decoupling detection from any specific platform, content type, or predefined network. They argue that this generalization is both conceptually cleaner and methodologically prudent given the volatility of platform APIs, and they demonstrate the package through a case study of the 2021 German elections, performance benchmarks on simulated data, and a validation against the Keller et al. (2019) South Korean NIS dataset in which CooRTweet recovers 85–92% of known coordinated accounts.

## Key Contributions

- A minimal, abstract formalization of coordinated behavior in terms of accounts, actions, objects, time intervals τ, and repetition, yielding a weighted undirected graph.
- Release of **CooRTweet** on CRAN, generalizing detection beyond the platform- and content-specific scope of prior tools (CooRnet, Coordination Network Toolkit).
- **Edge symmetry scores** to address the "time window problem," where hyperactive accounts otherwise inflate edge weights with less active partners.
- A flexible **threshold-tagging** approach (`flag_speed_share`, subgraph extraction) that preserves rather than discards borderline accounts, supporting study of organic amplification and co-optation.
- Native support for multi-modal (URLs, domains, hashtags, images) and cross-platform analysis via concatenated outputs and platform-prefixed account IDs.
- A reproducible benchmarking apparatus via a built-in `simulate_data` function.

## Methods

The package is built around two core functions: `detect_groups()`, which identifies accounts co-sharing the same object within a window τ subject to a `min_participation` filter, and `generate_coordinated_network()`, which produces an `igraph` object with edge weights, symmetry scores, average time deltas, and object IDs. Validation used the Keller et al. (2019) NIS dataset (~86M tweets, 801 known NIS accounts) with 20 iterations of an 80/20 train/test split for suspect marking. Performance was benchmarked over 1,000 runs on Poisson-simulated symmetric adjacency data, measuring peak memory and elapsed time.

## Findings

- On the NIS dataset (τ=60s, median edge-weight threshold), CooRTweet recovered 91% of NIS accounts via co-retweet, 17% via co-tweet, and 92% in a combined network.
- Suspect marking on held-out test accounts retrieved 90.8%, matching or exceeding Keller et al.'s reported 85%.
- Results replicate Keller et al.'s substantive finding that co-retweeting, not co-tweeting, was the dominant NIS coordination mode.
- `detect_groups` scales linearly in number of posts but quadratically in unique objects; `generate_coordinated_network` scales linearly with modest memory demands.
- The FOCUS Online example shows that rigid thresholds exclude analytically relevant accounts, motivating flexible tagging over hard cutoffs.

## Connections

CooRTweet extends the operational tradition of coordinated link-sharing detection developed in [[Giglietto2020-9d8acdd7]] and refined across [[Giglietto2022-b30e8b4e]], [[Giglietto2022-0e951ac5]], and [[Giglietto2023-fa71a001]], generalizing it beyond CooRnet's URL-and-Facebook focus. Its validation strategy and platform-agnostic stance speak directly to methodological debates on detection reliability and threshold sensitivity taken up in [[Schulte2026-df]], [[Kulichkina2025-sl09]], and [[Cerulli2026-sl75]], while its treatment of coordination as a matter of degree — rather than a binary inauthentic/authentic split — resonates with critical framings in [[Bruns2025-fz]] and [[Righetti2025-slf9]].
