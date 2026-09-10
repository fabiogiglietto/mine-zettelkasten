---
title: "Measuring partisan community dynamics: a longitudinal analysis of affective engagement in pro-Bolsonaro Facebook networks"
aliases: ["Measuring partisan community dynamics: a longitudinal analysis of affective engagement in pro-Bolsonaro Facebook networks"]
authors: ["Giada Marino", "Bruna Paroni", "Fabio Giglietto"]
year: 2026
doi: 10.1080/1369118x.2026.2696929
bibtex_key: Marino2026-slef
kind: team
submitted_by: "GiadaM. / Uniurb"
slack_permalink: https://minesmd.slack.com/archives/C0BDU82EBHQ/p1783526195619319
topics: [political-polarization-partisanship, llms-computational-content-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/1369118x.2026.2696929
podcast_url: 
pdf_available: true
discovery_date: 2026-07-09T12:08:33.180985Z
---

# Measuring partisan community dynamics: a longitudinal analysis of affective engagement in pro-Bolsonaro Facebook networks

> Marino, G., Paroni, B., & Giglietto, F. (2026). Measuring partisan community dynamics: a longitudinal analysis of affective engagement in pro-Bolsonaro Facebook networks. *Information, Communication & Society*. https://doi.org/10.1080/1369118x.2026.2696929
>
> [View paper](https://doi.org/10.1080/1369118x.2026.2696929)

## Summary

This paper offers a longitudinal, mixed-methods study of affective engagement within a hyperpartisan pro-Bolsonaro Facebook network of 53 groups and 4 pages, tracking over 12 million posts from 2021 to 2023. Against the common assumption that hyperpartisan communities operate as stable, impermeable echo chambers, the authors argue that affective engagement is highly unstable and reshaped by major political events — most dramatically around Lula's 2023 inauguration and the January 2023 coup attempt. Their central claim is that emotional response is jointly structured by *who* is mentioned (actor category) and *when* (temporal context), rather than by fixed ideological positions. The paper contributes a Brazilian (Global South) case to a literature dominated by US-centric research and documents deliberate external intervention (brigading) as a novel mode of adversarial exposure in public partisan spaces.

## Key Contributions

- First systematic long-term longitudinal analysis of affective engagement in pro-Bolsonaro Facebook communities, distinguishing in-group vs. out-group actor responses across a multi-year crisis period.
- A replicable mixed-methods pipeline combining fine-tuned GPT-4o political actor classification, longitudinal volatility tracking, and multinomial regression.
- Two novel behavioral indices derived from Facebook affordances: the Emotional Polarization Index (EPI) and Engagement Balance Index (EBI).
- A theoretical enrichment of echo-chamber and polarization frameworks, showing that hyperpartisan communities can fracture, adapt, and respond to external pressure.
- Documentation of brigading as a mechanism of adversarial cross-cutting exposure, extending beyond accidental exposure accounts.

## Methods

The authors collected 12,156,409 posts (via CrowdTangle) from a pro-Bolsonaro network identified through VeraAI Alerts, spanning January 2021–December 2023. They built two post-level indices — EPI = (love − angry)/(love + angry) and EBI = (shares − comments)/(shares + comments), each ranging −1 to +1 — aggregated to daily means. A 30-day rolling-window volatility detection algorithm (95th percentile threshold) flagged 96 volatile days clustered into seven instability periods (N = 1,161,126 posts). GPT-4o (gpt-4o-2024-08-06) was fine-tuned on 2,245 manually coded posts for multi-label classification across six political actor categories (67.7% exact-match accuracy, 0.85 F1). Per-time-frame multinomial logistic regressions used tertile-based EPI and EBI outcomes with five actor-presence indicators and engagement/reaction-volume controls.

## Findings

- Both indices showed marked instability; EPI shifted from love- to anger-dominated (especially around the coup), and EBI moved from share-prevalent to comment-prevalent engagement over 2023.
- 15.6% of volatile days fell within 15 days of the January 2023 coup attempt, while three other major events showed no volatile days in their windows.
- Bolsonaro content drew strong positive emotional engagement in 2021–2022 (β up to 1.193) that declined sharply by December 2023 (β = 0.220), with 2023 marked by more argumentative, comment-dominated engagement.
- Lula references produced expected angry oppositional responses in 2021 (peak β = 0.732) that dissipated in 2023, with a symmetrical drop in love-reaction suppression suggesting anti-Bolsonaro intervention (brigading).
- Armed Forces references (symbolically in-group) showed the most extreme temporal variability tied to discrete events; mainstream media references unexpectedly attracted share-dominated engagement in later periods.

## Connections

This paper contributes to the same debate over echo chambers, cross-cutting exposure, and affective polarization engaged by [[Minici2024-tf]] and [[Bakshy2015-rn]], but challenges the static-enclave assumption by emphasizing temporal instability. Its use of a fine-tuned LLM for political actor classification connects it to computational content-analysis work such as [[Le-Mens2025-qz]] and [[Alizadeh2026-es]]. Its focus on coordinated external intervention and network-level partisan dynamics resonates with [[Giglietto2019-882f1900]] and [[Giglietto2024-cbeb3f70]], which share authorship and a lineage of Facebook network analysis.
