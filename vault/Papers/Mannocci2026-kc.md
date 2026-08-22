---
title: "Detection and characterization of coordinated online behavior: A survey"
aliases: ["Detection and characterization of coordinated online behavior: A survey"]
authors: ["Lorenzo Mannocci", "Michele Mazza", "Anna Monreale", "Maurizio Tesconi", "Stefano Cresci"]
year: 2026
doi: 10.1145/3839225
bibtex_key: Mannocci2026-kc
topics: [coordinated-inauthentic-behavior, meta-science-of-misinformation-research]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1145/3839225
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Mannocci2026-kc.mp3
pdf_available: true
discovery_date: 2026-08-18T15:34:32.157112Z
---

# Detection and characterization of coordinated online behavior: A survey

> Mannocci, L., Mazza, M., Monreale, A., Tesconi, M., & Cresci, S. (2026). Detection and characterization of coordinated online behavior: A survey. *ACM Computing Surveys*. https://doi.org/10.1145/3839225
>
> [View paper](https://doi.org/10.1145/3839225)

## Summary

This survey systematically reviews the growing body of research on **coordinated online behavior** — the phenomenon whereby multiple actors act in concert on social media — arguing that the field's dominant focus on *Coordinated Inauthentic Behavior* (CIB) is too narrow. The authors reconcile fragmented and operationally-driven definitions from platforms (Meta, Twitter/X, YouTube, Reddit, TikTok) and academia into a single theoretically grounded framework. Their central claim is that coordination is fundamental to all online interaction and underlies both benign phenomena (activism, social movements) and malicious ones (disinformation, harassment); studying it should therefore not be confined to inauthenticity. They offer a general definition built on three components — **actors, synergic actions, and intent** — and four orthogonal characterizing dimensions, then organize existing detection and characterization methods into a unified analytical scheme.

## Key Contributions

- A new general, theoretically grounded definition of coordinated online behavior based on **actors, synergic actions, and intent**.
- A conceptual framework with four defining dimensions — **authenticity, harmfulness, orchestration, and time-variance** — mapping phenomena along a malicious-to-benign spectrum.
- Reconciliation of fragmented industry and academic definitions into a unified vocabulary.
- A formal problem statement separating **detection f(·)** and **characterization g(·)** tasks, with a specified input model (users and quadruple-based actions).
- A structured, tabulated survey of detection methods (network science and machine learning), covering co-actions, similarity functions, filtering strategies, and community detection algorithms.
- Identification of open challenges (lack of null models, poor cross-domain comparability, heuristic reliance) and a research roadmap.

## Methods

A **PRISMA** systematic literature review searching Scopus (353 records) and Google Scholar (first 1000 results) for English-language work from 2014–2026. After deduplication and screening, 83 papers were retained, with backward reference searching adding 38 more for a final corpus of 122. Papers were disciplinarily classified via Scimago (journals), CORE (conferences), and arXiv categories, revealing a predominance of Computer Science venues. The authors then conducted a conceptual analysis reconciling offline coordination theory, platform definitions, and academic operationalizations, and taxonomically organized detection methods into network-science stages (user selection, coordination network construction, filtering, community discovery) and machine-learning approaches.

## Findings

- No existing definition is general enough to describe coordinated behavior comprehensively, though each captures relevant properties (similarity, synchronicity, shared intent).
- Platforms treat identical coordinated efforts inconsistently — e.g., the 2020 Tulsa TikTok rally sabotage was not treated as CIB by Facebook; the Spamouflage campaign was labeled differently by Google, Twitter, and Reddit.
- **Authenticity and harmfulness are orthogonal**: coordination can be authentic-but-harmful (hate groups) or inauthentic-but-harmless (anonymous Arab Spring protesters).
- Network-science methods operationalize coordination via **co-actions** (co-sharing/co-retweet most common; also co-reply, co-like, co-URL, co-hashtag, co-mention, and newer TikTok co-stitch/co-duet).
- Detection outputs vary in informativeness: network communities (richest), clusters, and binary labels (least).
- Filtering uses fixed thresholds, statistical validation, or time-window strategies; **short, highly synchronized windows surface inauthentic/harmful coordination, whereas emergent authentic behavior needs longer windows**.
- Community discovery predominantly relies on **Louvain and Leiden** algorithms.
- Publications surged after Facebook introduced the CIB concept in 2018.

## Connections

As a survey of the meta-science of the field, this note anchors the broader constellation of coordinated-behavior research. It directly connects to detection work using co-action networks and time-window filtering such as [[Mannocci2025-ig]] (shared authorship), [[Minici2024-tf]], [[Luceri2025-tr]], and [[Nenno2025-xa]], as well as the extensive coordinated-link-sharing tradition of [[Giglietto2020-9d8acdd7]], [[Giglietto2019-e9be81c1]], [[Giglietto2022-b30e8b4e]], and [[Giglietto2023-fa71a001]]. Its framing of coordination as orthogonal to disinformation and information operations links it to campaign case studies like [[Kulichkina2025-sl09]], [[Copland2025-em]], and [[Graham2025-gp]], while its critique of inconsistent platform definitions speaks to the definitional and measurement debates in [[Righetti2025-slf9]] and [[Bechmann2026-dr]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Mannocci2026-kc.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
