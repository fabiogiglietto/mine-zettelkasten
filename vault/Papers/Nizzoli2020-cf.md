---
title: "Coordinated Behavior on Social Media in 2019 UK General Election"
aliases: ["Coordinated Behavior on Social Media in 2019 UK General Election"]
authors: ["Leonardo Nizzoli", "Serena Tardelli", "Marco Avvenuti", "Stefano Cresci", "Maurizio Tesconi"]
year: 2020
doi: 
bibtex_key: Nizzoli2020-cf
topics: [coordinated-inauthentic-behavior, electoral-social-media-research]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2008.08370v2
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807372Z
---

# Coordinated Behavior on Social Media in 2019 UK General Election

> Nizzoli, L., Tardelli, S., Avvenuti, M., Cresci, S., & Tesconi, M. (2020). Coordinated Behavior on Social Media in 2019 UK General Election. *Proc. AAAI Intl. Conference on Web and Social Media (ICWSM) 2021*.
>
> [View paper](http://arxiv.org/abs/2008.08370v2)

## Summary

This paper introduces a network-based framework for detecting and quantifying coordinated behavior on social media that treats coordination as a *continuum* rather than a binary label. Rather than applying a single fixed similarity threshold to declare users coordinated or not, the authors argue that each online community carries its own characteristic degree of coordination, and that a nuanced measurement is needed to surface the relevant patterns. Applying the method to 11.3M tweets from 1.2M users collected during the 2019 UK General Election, they uncover seven distinct coordinated communities and show that the most strongly coordinated groups were not mainstream party supporters but small activist and antagonist communities. A central conceptual claim is that coordination and automation (bots) are orthogonal — bot detection alone is insufficient to study coordinated inauthentic behavior.

## Key Contributions

- A non-binary, network-based framework that estimates the *full spectrum* of coordination, generalizing and extending prior similarity-network approaches.
- Two methodological innovations: multiscale backbone filtering (avoiding arbitrary fixed thresholds) and an iterative "coordination-aware" community detection procedure.
- Empirical demonstration that coordination and automation are largely uncorrelated, cautioning against equating bot detection with CIB detection.
- Identification and interpretation of concrete coordinated communities in the 2019 UK GE, including small activist groups usually overlooked.
- A publicly released large-scale Twitter dataset of the 2019 UK General Election (11M tweets, 1.2M users).

## Methods

The six-step framework selects starting users, chooses a similarity measure, builds and filters a user-similarity network, performs coordination-aware community detection, and characterizes the resulting communities. Data was collected via the Twitter Streaming API (12 Nov–12 Dec 2019) using a curated hashtag list (neutral, Labour- and Conservative-leaning) plus official party/leader account activity. Analysis focused on "superspreaders" (top 1% by retweets, ~10.8k users), each modeled as a TF-IDF-weighted vector of retweeted tweet IDs, with cosine similarity between users. The similarity network was filtered using the Serrano et al. (2009) multiscale backbone rather than a fixed threshold, and Louvain community detection was run iteratively while raising an edge-weight threshold step by step to trace how communities evolve with coordination. Political leaning was inferred via label propagation from 13 seed hashtags. Communities were characterized with network measures, TF-IDF hashtag clouds, word shift graphs, Botometer scores, and Twitter suspension data.

## Findings

- Seven coordinated communities emerged: conservatives (CON), labourists (LAB), tactical voters/anti-Brexit neutrals (TVT), the SNP, Backto60 pension activists (B60), anti-Labour antisemitism-focused conservatives (ASE), and anti-loan-charge activists (LCH).
- The network structure mirrored the UK political landscape — a sharply separated conservative cluster and intertwined Labour/neutral clusters, reflecting Brexit polarization and tactical voting.
- Large communities (LAB, CON) mixed many weakly-coordinated users with a smaller strongly-coordinated core, while small activist groups (B60, LCH, ASE) were almost entirely strongly coordinated.
- Community-specific characteristic coordination values differed (e.g., LCH ~0.9, B60 ~0.8, ASE ~0.55).
- Network measures diverged structurally: B60 formed a cohesive, strongly assortative clique; ASE and LAB were disassortative hub-and-spoke structures; SNP top members were uncoordinated.
- Strongly-coordinated users embraced far more specific narratives (50s women's pension rights, anti-loan-charge) than weakly-coordinated members.
- Automation was essentially uncorrelated with coordination; conservative clusters had more suspensions, while B60's declining suspensions suggested authentic grassroots coordination.

## Connections

This paper is a methodological anchor in the coordinated-inauthentic-behavior literature and connects directly to work developing and applying coordination-detection networks such as [[Luceri2025-tr]], [[Minici2024-tf]], [[Mannocci2025-ig]], and [[Mannocci2026-kc]]. Its argument that coordination does not imply inauthenticity resonates with the framing of coordinated-link-sharing and detection studies like [[Giglietto2020-9d8acdd7]], [[Giglietto2020-6278a4aa]] and [[Righetti2025-slf9]], while its orthogonality-of-automation claim distinguishes it from bot-centric electoral misinformation work such as [[Grinberg2019-ua]] and [[Starbird2019-qv]].
