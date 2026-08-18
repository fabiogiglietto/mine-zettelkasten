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
podcast_url: 
pdf_available: true
discovery_date: 2026-08-18T15:34:32.157112Z
---

# Detection and characterization of coordinated online behavior: A survey

> Mannocci, L., Mazza, M., Monreale, A., Tesconi, M., & Cresci, S. (2026). Detection and characterization of coordinated online behavior: A survey. *ACM Computing Surveys*. https://doi.org/10.1145/3839225
>
> [View paper](https://doi.org/10.1145/3839225)

## Summary

This survey systematically reviews the burgeoning literature on coordinated online behavior — the phenomenon whereby multiple accounts act in concert on social media, spanning malicious operations (disinformation, manipulation, harassment) as well as benign ones (activism, social movements). The authors argue that the field is hampered by fragmented, operationally driven definitions from both platforms (Meta, Twitter/X, YouTube, Reddit, TikTok) and academics, and they respond by proposing a new general, theoretically grounded definition built on three components — **actors**, **synergic actions**, and **intent** — plus a conceptual framework organized along four defining dimensions: authenticity, harmfulness, orchestration, and time-variance. A central move is decoupling the study of coordination from the study of inauthenticity, insisting that coordination be studied as a general phenomenon rather than being conflated with Facebook's narrower "Coordinated Inauthentic Behavior" (CIB) construct.

## Key Contributions

- A new general definition of coordinated online behavior grounded in actors, synergic actions, and intent.
- A conceptual framework with four orthogonal dimensions (authenticity, harmfulness, orchestration, time-variance) and a taxonomy mapping phenomena from malicious to benign.
- Reconciliation of fragmented industry and academic definitions into a unified vocabulary.
- A formal problem statement separating **detection** *f(·)* from **characterization** *g(·)*, with a specified input model of users and quadruple-based actions.
- A structured, tabulated survey of detection methods (network science and machine learning) covering co-actions, similarity functions, filtering strategies, and community detection algorithms.
- Identification of open challenges — absent null models, poor cross-domain comparability, and heuristic reliance — plus a research roadmap.

## Methods

A PRISMA-style systematic literature review searching Scopus (353 records) and Google Scholar (first 1000 results), covering 2014–2026 English-language publications. After deduplication (147 removed) and screening 1206 records (4 non-English, 1118 out-of-scope excluded), 83 papers were retained; backward reference searching added 38, for a final corpus of 122 papers. The authors classified venues disciplinarily (Scimago, CORE, arXiv categories), finding Computer Science dominant. They then conducted a conceptual analysis reconciling offline coordination theory, industry definitions, and academic operationalizations, and taxonomically organized detection methods into network science approaches (user selection, coordination network construction, filtering, community discovery) and machine learning approaches.

## Findings

- No existing definition is general enough to describe coordinated behavior comprehensively, though each captures partial properties (similarity, synchronicity, shared intent).
- Authenticity and harmfulness are orthogonal: coordination can be authentic-but-harmful (hate groups) or inauthentic-but-harmless (anonymous Arab Spring protesters).
- Platforms treat identical coordinated efforts inconsistently — e.g., the 2020 Tulsa TikTok rally sabotage was not deemed CIB, and the Spamouflage campaign was labeled differently by Google, Twitter, and Reddit.
- Network science methods operationalize coordination via "co-actions," with co-sharing/co-retweet most common, alongside co-reply, co-like, co-URL, co-hashtag, co-mention, co-follow, co-report, and newer TikTok co-stitch/co-duet.
- Detection outputs vary in informativeness: network communities (richest), clusters, and binary labels (least).
- Filtering uses fixed thresholds, statistical validation, or timing windows; short synchronized windows surface inauthentic/harmful coordination, while longer windows are needed for emergent authentic behavior.
- Community discovery relies predominantly on Louvain and Leiden algorithms.
- Publications surged after Facebook introduced the CIB label in 2018.

## Connections

As a survey, this paper provides the definitional and methodological scaffolding for much empirical coordination-detection work, connecting closely to studies that operationalize network-based co-action detection and multiplex coordination analysis such as [[Mannocci2025-ig]], [[Luceri2025-tr]], and [[Minici2024-tf]]. Its insistence on separating coordination from inauthenticity resonates with critical and definitional interventions in the wider field, including the CooRnet-lineage work of [[Giglietto2020-9d8acdd7]] and [[Giglietto2019-e9be81c1]], and it complements broader agenda-setting and conceptual critiques of manipulation research like [[Budak2024-ef]].
