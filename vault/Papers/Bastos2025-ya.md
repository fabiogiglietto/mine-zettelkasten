---
title: "So long twitter, and thanks for all the tweets"
aliases: ["So long twitter, and thanks for all the tweets"]
authors: ["Marco T. Bastos"]
year: 2025
doi: 10.2139/ssrn.5206365
bibtex_key: Bastos2025-ya
topics: [platform-governance-data-access, computational-social-science-methods]
citation_count: 0
open_access: false
source_url: https://doi.org/10.2139/ssrn.5206365
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bastos2025-ya.mp3
pdf_available: true
discovery_date: 2025-04-15T00:00:00Z
---

# So long twitter, and thanks for all the tweets

## Summary

Bastos presents a decade-long (2011–2020) audit of how Facebook's News Feed ranking updates shaped engagement with content from *The Guardian*. By pairing a hand-compiled timeline of 52 documented algorithmic interventions with ~1 million Guardian articles and matched CrowdTangle engagement data, the paper applies cross-correlation, Granger causality, and anomaly detection to test for lagged effects. Hard news engagement is shown to respond to algorithm changes after roughly 19–24 days, while opinion, sport, lifestyle, and arts content does not — evidence that Facebook treats "news" as a distinct, gatekept category. The piece reframes recommender systems away from the "black box" metaphor toward deliberate, auditable sociotechnical interventions, and ties this empirical agenda to Article 40(4) of the EU Digital Services Act.

## Key Contributions

- First long-run (10-year) empirical model linking specific, documented Facebook News Feed updates to engagement outcomes for a major news publisher.
- A reusable methodological pipeline (parameterized intervention timeline + CCF + Granger causality + S-H-ESD anomaly detection) for external algorithm auditing.
- Empirical evidence that hard news is differentially gatekept relative to other content pillars.
- A conceptual reframing of platform algorithms as "strategic interventions" rather than opaque black boxes.
- An applied articulation of how DSA Article 40(4) and Recital 85 could anchor a research program on systemic algorithmic risk.

## Methods

The author hand-compiled 52 Facebook News Feed ranking updates (2011–2020) from announcements, industry research, leaks, and the Haugen disclosures, coding each by impact and valence toward news. He retrieved ~1M Guardian articles via the Guardian API, segmented into five pillars (News, Opinion, Sport, Arts, Lifestyle), and matched 576,673 with CrowdTangle engagement metrics. After ADF stationarity checks and log-transformation of daily aggregates, cross-correlation functions identified optimal lags, Granger causality tests assessed predictive relationships at those lags, and Seasonal Hybrid ESD detected anomalies across the decade.

## Findings

- Optimal lags of 19–24 days between updates and engagement effects; significant cross-correlations for News (ACF .35, lag 19) and Sport (ACF .31, lag 24).
- Granger causality held only for the News section (F=1.68, p=.033 at lag 19); Arts, Lifestyle, Opinion, and Sport showed no significant effect.
- S-H-ESD detected 191 anomalies, heavily concentrated in 2014–2016; two-thirds of News anomalies fell in 2016, clustering around the June 2016 friends/family prioritization.
- Sport anomalies clustered in July 2014, attributable to the FIFA World Cup rather than algorithmic shifts.
- Engagement baselines differed sharply across pillars: News averaged 1,215 interactions per article vs. 924 (Opinion), 481 (Arts), 464 (Lifestyle), and 325 (Sport).

## Connections

This paper sits squarely in the post-API external-auditing tradition and complements work on the closure of platform data pipelines and the afterlife of CrowdTangle — see [[Rieder2025-ju]], [[Rieder2026-pp]], and [[Freelon2024-sc]] on data access politics, and [[Ohme2026-nv]] on doing computational social science under these constraints. Its anomaly-based, intervention-timeline approach to recommender auditing connects to algorithmic exposure and amplification studies such as [[Bouchaud2026-lr]], Bartley2024-style work continued in [[Lai2024-to]] and [[Ulloa2024-jm]], and to broader arguments about platform power over news distribution in [[Hurcombe2025-cs]] and [[Cazzamatta2026-lo]]. The DSA framing aligns it with regulatory-research agendas advanced in [[Helmond2026-ll]] and [[Bak-Coleman2025-pm]].

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bastos2025-ya.mp3)
