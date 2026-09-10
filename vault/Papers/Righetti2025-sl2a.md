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
topics: [coordinated-inauthentic-behavior, digital-methods-research-tools]
citation_count: 3
open_access: true
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

This paper introduces **CooRTweet**, an open-source R package (available on CRAN) for detecting coordinated behavior on and across social media platforms. Its central methodological move is a minimal, abstract definition of coordinated behavior — the *repeated near-synchronous sharing of any uniquely identifiable object by a stable set of accounts*. By decoupling the definition from any specific platform, content type, or object type, CooRTweet generalizes beyond earlier tools that were constrained to particular platforms or predefined network types. The authors demonstrate the tool through a case study of the 2021 German elections, benchmark its computational performance on simulated data, and validate it against the 86-million-tweet South Korean NIS disinformation dataset, recovering 85–92% of known coordinated accounts.

## Key Contributions

- Release of **CooRTweet**, a generalized, platform-agnostic R package for coordinated network detection.
- A minimal, abstract formalization of coordinated behavior in terms of accounts, actions, objects, time intervals (τ), and repetition — independent of the empirical nature of the shared object.
- Introduction of **edge symmetry scores** to counter the "time window problem," where hyperactive accounts inflate edge weights with less active partners.
- A **flexible threshold-tagging** approach (subgraph options, `flag_speed_share()`) that retains borderline accounts rather than discarding them, enabling study of organic amplification and co-optation.
- A reproducible validation and benchmarking strategy using ground-truth data and a built-in `simulate_data` function.
- A worked example of building platform-independent research software resilient to volatile social media APIs.

## Methods

Coordinated behavior is formalized as an undirected weighted graph *G = (V, E, W)* with edge symmetry scores, derived from accounts co-sharing objects within a time window τ. The implementation is two-step: `detect_groups()` identifies co-sharing within τ subject to a `min_participation` filter, and `generate_coordinated_network()` builds an igraph object carrying edge weights, symmetry scores, average time deltas, and object IDs. Auxiliary functionality (`flag_speed_share()`, subgraph extraction) supports nested stricter time windows and identification of fast coordinated cores. Multi-modal analysis is achieved by concatenating outputs across object types (URLs, domains, hashtags, images); cross-platform analysis uses platform-prefixed account IDs. Validation used the Keller et al. (2019) NIS dataset (~86M tweets, 801 known accounts) with a repeated 80/20 train-test split, and benchmarking used simulated Poisson-distributed adjacency matrices over 1,000 runs.

## Findings

- On the NIS dataset (τ = 60s, median edge-weight threshold), CooRTweet recovered 731 (91%) NIS accounts via co-retweet, 139 (17%) via co-tweet, and 737 (92%) in a combined network.
- Suspect marking on the combined network retrieved 90.8% of held-out NIS accounts, comparable to or exceeding the 85% reported by Keller et al. (2019).
- Results confirmed that co-retweeting, not co-tweeting, was the dominant coordination mode for NIS agents.
- `detect_groups` memory scales linearly with number of posts but quadratically with unique objects; `generate_coordinated_network` scales linearly and is far less memory-intensive.
- The FOCUS Online case study showed how strict thresholds can exclude relevant coordinated vertices, motivating the flexible tagging and time-window layering approach.

## Connections

This paper is a core methodological contribution to the coordinated inauthentic behavior detection toolchain, alongside other digital-methods research tools such as [[Kansaon2025-id]] and [[Mannocci2025-ig]], and it explicitly builds on the operational lineage of coordinated-sharing work associated with the Giglietto research program (e.g., [[Giglietto2020-9d8acdd7]], [[Giglietto2022-b30e8b4e]], [[Giglietto2023-fa71a001]]). Its generalized, cross-platform framing connects to studies of synchronized network detection like [[Minici2024-tf]] and [[Luceri2025-tr]], and to the authors' related methodological work in [[Righetti2025-slf9]] and [[Balluff2026-ev]].
