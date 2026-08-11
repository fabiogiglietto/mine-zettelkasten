---
title: "Multi-platform research in the light of technology affordances: networks of the far right in Germany"
aliases: ["Multi-platform research in the light of technology affordances: networks of the far right in Germany"]
authors: ["Azade E. Kakavand", "Nicola Righetti", "Annie Waldherr"]
year: 2026
doi: 10.1080/19331681.2026.2697186
bibtex_key: Kakavand2026-kt
topics: [platforms-audiences-and-online-communities, cross-national-disinformation-monitoring]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/19331681.2026.2697186
podcast_url: 
pdf_available: true
discovery_date: 2026-08-11T07:48:17.118692Z
---

# Multi-platform research in the light of technology affordances: networks of the far right in Germany

> Kakavand, A. E., Righetti, N., & Waldherr, A. (2026). Multi-platform research in the light of technology affordances: networks of the far right in Germany. *Journal of Information Technology & Politics*, 1–20. https://doi.org/10.1080/19331681.2026.2697186
>
> [View paper](https://doi.org/10.1080/19331681.2026.2697186)

## Summary

This paper offers a large-scale comparative study of how German-speaking far-right actors organize themselves across five social media platforms—Facebook, Twitter, Instagram, YouTube, and Telegram. Rather than treating platform features as fixed technical properties, the authors argue that technology affordances (connectivity, replicability, scalability) are *relational sociotechnical outcomes* produced through the interplay of platform design and user practice. Through network analysis of ties built from platform-specific connectors, they show that far-right actors do not reproduce identical networks across platforms; instead they adapt their communication practices to each platform's affordances, yielding distinctive structures of amplification and visibility. The central methodological argument is that single-platform studies capture only a fragment of a broader, complementary multi-platform ecosystem.

## Key Contributions

- One of the few large-scale, simultaneous multi-platform comparisons of far-right networks across five major platforms.
- Demonstrates how network measures (HITS hubs/authorities, betweenness centrality, reciprocity, modularity, clustering) can be operationalized to *infer* affordances such as connectivity, replicability, and scalability.
- Advances affordances as relational sociotechnical outcomes, showing empirically that near-equivalent features generate divergent networks depending on social use.
- Provides a transparent methodological template (seed lists, snowball procedure, connector definitions, code, OSF materials) while candidly documenting data-access and comparability limitations.

## Methods

- Exploratory multi-platform case-study design covering the German-speaking far right over six months of 2022.
- Snowball sampling from a curated, expert-vetted seed list (~28–43 prominent actors per platform: AfD politicians, parties, journalists, alternative media, activists), across three iterations with a final closure step retaining only nodes linking back to already-collected actors.
- Platform-specific *visible connectors* as edges: retweets/mentions (Twitter), shared posts (Facebook), forwards (Telegram), caption mentions/tags (Instagram), channel subscriptions (YouTube).
- Data via platform APIs (Twitter API v2, CrowdTangle, Google API, Telegram/Telethon); analysis in Python (NetworkX) and Gephi. Size-robust measures included weakly connected components, reciprocity, clustering, and Louvain modularity.

## Findings

- **Twitter**: by far the largest, loosely connected network (~42k nodes, 7.7M edges, one component), low clustering and very low reciprocity—an international, outward-facing broadcast arena where authority exceeds hub scores, signalling scalability.
- **Telegram**: second largest (~8.4k nodes), higher clustering but low reciprocity; inward-oriented, dominated by fringe/conspiracy content with differentiated producers, amplifiers, and brokers.
- **YouTube**: mid-sized, loosely connected, organized by genre/topic communities (e.g., cooking linked to "Day X" prepping), forming indirect connectivity that may serve as a radicalization gateway.
- **Instagram**: small and fragmented into echo chambers with the highest reciprocity, clustering, and modularity; mainstream media/political accounts dominate while a tight AfD cluster sits at the periphery.
- **Facebook**: smallest network, strongly AfD-dominated with a hierarchical division of labor—federal accounts as content authorities, local accounts as amplifying hubs—indicating high replicability and party coordination.
- Contrary to prior research, Twitter's network is heterogeneous and international, extending beyond national boundaries and beyond politicians and journalists.

## Connections

This paper sits at the intersection of platform affordance theory and far-right network research, and its methodological push toward multi-platform, comparative analysis resonates with work using digital methods and cross-platform network tracing such as [[Jurg2025-ur]] and platform-infrastructure studies like [[Helmond2026-ll]] and [[Rieder2026-pp]]. Its theorization of affordances as relational sociotechnical outcomes connects to the affordance and platform-governance lineage of [[Boyd2026-op]] and [[Gillespie2010-sla2]]. Its substantive focus on far-right and extremist online organizing links it to [[Askanius2026-de]], [[Grusauskaite2026-po]], and [[Nenno2025-xa]].
