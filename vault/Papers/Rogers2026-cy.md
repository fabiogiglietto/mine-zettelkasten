---
title: "Beyond verification| post-truth spaces: Studying authenticity and influence on the internet"
aliases: ["Beyond verification| post-truth spaces: Studying authenticity and influence on the internet"]
authors: ["Richard Rogers", "Kamila Koronska"]
year: 2026
doi: 10.65476/1fw44702
bibtex_key: Rogers2026-cy
topics: [information-disorder-theory, cross-national-disinformation-monitoring]
citation_count: 0
open_access: false
source_url: https://doi.org/10.65476/1fw44702
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Rogers2026-cy.mp3
pdf_available: true
discovery_date: 2026-07-21T08:34:20.762410Z
---

# Beyond verification| post-truth spaces: Studying authenticity and influence on the internet

> Rogers, R., & Koronska, K. (2026). Beyond verification| post-truth spaces: Studying authenticity and influence on the internet. *International Journal of Communication*, *20*, 1863–1885. https://doi.org/10.65476/1fw44702
>
> [View paper](https://doi.org/10.65476/1fw44702)

## Summary

This paper develops a conceptual and methodological framework for locating and measuring "post-truth spaces" — demarcated clusters of densely interlinked web pages and social media accounts that either resist verification or are recognized disinformation sources, and that work together to assert political influence. Written for fact-checkers and verification specialists under the EU-funded vera.ai project, it situates post-truth spaces within a five-part typology of "problematic information" spaces and proposes a mapping technique that combines network analysis, digital investigation, and a cluster-betweenness influence metric. Rather than detecting individual fakes, the approach produces actionable "leads" — curated source lists that fact-checkers can monitor. The framework is demonstrated through a case study of Russia-Ukraine war discourse on Moldovan Facebook ahead of the 2024 presidential elections and EU referendum.

## Key Contributions

- **Conceptual:** Introduces and defines the "post-truth space" and positions it among four adjacent problematic-information spaces — alternative influence networks, fake news engagement spaces, coordinated inauthentic behavior campaigns, and participatory propaganda.
- **Methodological:** Provides a replicable mapping protocol (keyword query, URL resolution, Gephi community detection, visual network analysis) alongside provenance/verification indicators and a cluster-betweenness metric for influence.
- **Practical:** Offers a fact-checker workflow to surface problematic source clusters and gauge their influence for curated monitoring lists.
- **Empirical:** Demonstrates the method through a Moldova case study, laying groundwork for wider application across Eastern Europe.

## Methods

The paper first situates post-truth spaces conceptually, enumerating the distinct mapping techniques used for each adjacent space (co-host/co-appearance networks for YouTube alternative influence; engagement comparison for fake news; content/timing coordination signals for CIB; narrative and memetic analysis for participatory propaganda). The empirical demonstration queries war-related keywords in CrowdTangle to retrieve Moldovan Facebook posts and posting accounts, tidies the data by resolving URLs to domains and Facebook native links, then analyzes the network in Gephi using ForceAtlas2 spatialization and Louvain community detection (with specified parameters). Digital investigation leverages Facebook transparency indicators (account name history, default "digital creator" names, pending verification status), and cluster betweenness centrality serves as a proxy for influence — measuring how far post-truth content penetrates other clusters.

## Findings

- Moldovan war discourse resolved into distinct clusters: three proximate "post-truth" clusters, a "borderline" cluster, plus conservative/nationalist, pro-Ukraine, mainstream media, and military analysis clusters.
- Top post-truth nodes were largely propagandists/ampligandists — e.g., stiripesurse.ro (which denied the Bucha massacre) and digital creators laundering content from Russian sources like TASS and lenta.ru without attribution.
- All three post-truth clusters had low betweenness centrality (76.39, 12.73, 11.14), indicating marginal centrality and minimal direct network impact.
- The "borderline" cluster (top node Aktual24.ro) had by far the highest betweenness (2567.10), meaning much of the war conversation is driven by nodes straddling the post-truth spaces rather than by mainstream media — a significant lead for fact-checkers.
- Post-truth clusters rarely share URLs outside themselves but bridge into the influential borderline cluster via domestic hardship framings (e.g., rising energy bills linked to the war).

## Connections

This paper's typology explicitly incorporates coordinated inauthentic behavior as one of its five problematic-information spaces, connecting it to work on coordination detection and network mapping such as [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], and [[Giglietto2023-fa71a001]]. Its concern with authenticity, provenance, and platform terminology aligns with verification-oriented scholarship including [[Rogers2025-sl8f]] and [[Dahlke2026-sl34]], while its influence-measurement approach speaks to broader debates on measuring reach and impact of problematic content online.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Rogers2026-cy.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
