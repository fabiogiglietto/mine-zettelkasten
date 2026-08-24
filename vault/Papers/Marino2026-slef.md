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
topics: [political-polarization-partisanship, electoral-social-media-analysis]
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

This paper offers a longitudinal analysis of affective engagement within a hyperpartisan pro-Bolsonaro Facebook network across 2021–2023, challenging the common assumption that such communities are stable, impermeable echo chambers. Drawing on over 12 million posts from 53 groups and 4 pages, the authors show that emotional and behavioral engagement patterns were highly unstable and shifted markedly around Lula's 2023 inauguration and the January 2023 coup attempt. Their central argument is that affective engagement is jointly shaped by *which* political actors are mentioned and *when*, rather than by fixed ideological positions alone — reframing hyperpartisan spaces as fracturing, adaptive, and open to external contestation.

## Key Contributions

- First systematic multi-year longitudinal study of affective engagement in a pro-Bolsonaro Facebook community, distinguishing in-group from out-group actor responses across a crisis period.
- A replicable mixed-methods pipeline combining fine-tuned GPT-4o political actor classification, time-series volatility detection, and multinomial regression.
- Two novel behavioral indices derived from Facebook affordances: the Emotional Polarization Index (EPI) and the Engagement Balance Index (EBI).
- Enriches echo-chamber and polarization theory by documenting community fracture and adaptation rather than static enclosure.
- Documents brigading/external intervention as a mechanism of adversarial exposure, contributing an underrepresented Global South (Brazilian) case.

## Methods

- Collected 12,156,409 Facebook posts (Jan 2021–Dec 2023) from a pro-Bolsonaro network identified via VeraAI Alerts, using CrowdTangle historical data.
- Built two post-level indices: EPI = (love − angry)/(love + angry) and EBI = (shares − comments)/(shares + comments), each bounded in [−1, +1].
- Aggregated to daily means and applied a 30-day rolling-window volatility detection (95th percentile), yielding 96 volatile days across seven contiguous instability periods (N = 1,161,126 posts).
- Fine-tuned GPT-4o on 2,245 manually coded posts for six-category multi-label actor classification (67.7% exact-match accuracy, 0.85 F1).
- Estimated per-timeframe multinomial logistic regressions with tertile-based EPI/EBI outcomes, five actor-presence indicators, and engagement/reaction volume controls.

## Findings

- Both indices were markedly unstable; EPI shifted from love- to anger-dominated (especially around the coup) and EBI moved from share- to comment-prevalent engagement over 2023.
- 15.6% of volatile days fell within 15 days of the January 2023 coup; three other major events showed no volatile days.
- Bolsonaro content drove strong positive emotional engagement in 2021–2022 (β up to 1.193) that declined sharply by December 2023 (β = 0.220), with rising argumentative (comment-dominated) engagement.
- Lula references generated expected angry opposition in 2021 (β = 0.732) that dissipated in 2023 alongside reduced love-suppression — suggesting anti-Bolsonaro intervention.
- Armed Forces references showed the most extreme event-tied variability; mainstream media references unexpectedly drew share-dominated engagement in later periods.

## Connections

This paper builds directly on the authors' own program of work on coordinated and problematic information sharing, connecting to [[Giglietto2020-9d8acdd7]], [[Giglietto2024-cbeb3f70]], [[Giglietto2023-fa71a001]], and [[Marino2024-2fbc690f]]. Its engagement with echo-chamber versus cross-cutting-exposure debates situates it alongside network exposure studies such as [[Bakshy2015-rn]] and [[Gonzalez-Bailon2024-rq]], while its use of fine-tuned LLMs for political text annotation links it to methodological work like [[Tornberg2025-ir]]. As a Brazilian far-right case study, it also relates to [[Inacio-da-Silva2026-zf]] and [[Askanius2026-de]] on transnational far-right digital politics.
