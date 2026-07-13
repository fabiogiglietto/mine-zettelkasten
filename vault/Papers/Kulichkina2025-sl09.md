---
title: "Protest and repression on social media: Pro-Navalny and pro-government mobilization dynamics and coordination patterns on Russian Twitter"
aliases: ["Protest and repression on social media: Pro-Navalny and pro-government mobilization dynamics and coordination patterns on Russian Twitter"]
authors: ["Aytalina Kulichkina", "Nicola Righetti", "Annie Waldherr"]
year: 2025
doi: 10.1177/14614448241254126
bibtex_key: Kulichkina2025-sl09
kind: team
submitted_by: "Nicola Righetti"
slack_permalink: https://minesmd.slack.com/archives/C0BDU82EBHQ/p1783507489409529
topics: [coordinated-inauthentic-behavior, digital-authoritarianism-state-propaganda]
citation_count: 6
open_access: false
source_url: https://doi.org/10.1177/14614448241254126
podcast_url: 
pdf_available: true
discovery_date: 2026-07-08T13:08:04.166497Z
---

# Protest and repression on social media: Pro-Navalny and pro-government mobilization dynamics and coordination patterns on Russian Twitter

> Kulichkina, A., Righetti, N., & Waldherr, A. (2025). Protest and repression on social media: Pro-Navalny and pro-government mobilization dynamics and coordination patterns on Russian Twitter. *New Media & Society*. https://doi.org/10.1177/14614448241254126
>
> [View paper](https://doi.org/10.1177/14614448241254126)

## Summary

This paper investigates the co-evolution of pro-Navalny protest mobilization and pro-government counter-mobilization on Russian Twitter during the 2021 protests. Combining time-series methods (VAR, Granger causality, Impulse Response Functions) with co-retweet network analysis, the authors trace how each camp's activity reacted to offline events and characterize their coordination along three dimensions: synchronization, centralization, and modularity. They argue that Bennett and Segerberg's connective action framework can be productively extended to a notion of "connective counteraction" — coordinated pro-regime activity in authoritarian contexts that mimics grassroots mobilization but relies on organizational brokerage. Pro-Navalny activity was more voluminous and centralized around key figures like @teamnavalny, while the smaller pro-government network was more modular and preemptive, consistent with team-based astroturfing.

## Key Contributions

- Theoretical extension of the connective action framework to "connective counteraction" by pro-regime actors under authoritarianism.
- A three-dimensional operationalization of network coordination — synchronization, centralization, and modularity — mapping onto different modes of connective/collective action.
- An integrated methodological pipeline combining VAR/Granger/IRF time-series analysis with co-retweet network analysis across multiple time and frequency thresholds.
- An open-source R tool for coordination detection, later released as the CooRTweet package.
- Empirical documentation of protest-repression dynamics during the 2021 Russian pro-Navalny protests.

## Methods

Case study of the 2021 Russian pro-Navalny protests on Russian-language Twitter. Data (729,246 pro-Navalny and 41,642 pro-government tweets, Jan–Dec 2021) were collected via the Twitter Academic API using hashtags identified through daily monitoring of Russian trending topics, with manual validation. Changepoint analysis segmented the timeline into nine protest phases. The authors fit VAR models (16 lags ≈ 4 hours) with wild-bootstrap Granger causality tests and Impulse Response Functions to capture directional influence between camps. Co-retweet networks were built across 15 time intervals (1s–1h) and co-retweet thresholds (1–10), measuring synchronization (share coordinated), centralization (degree-based), and modularity (Louvain).

## Findings

- Pro-Navalny accounts tweeted ~17.5× more than pro-government accounts overall.
- Pro-government accounts intensified activity preemptively before protest days, often during lulls in opposition activity.
- Tweeting declined in both camps after the February protests and around April 21, coinciding with mass arrests and Twitter throttling.
- Granger causality was event-dependent: pro-Navalny → pro-government on Jan 23 and April 21; pro-government → pro-Navalny during the Feb 14 courtyard protests.
- IRF: a 1% rise in pro-Navalny tweets on Jan 23 raised pro-government tweets ~0.88% after one hour; April 21 effects were more sustained (10–20% at multiple lags).
- Pro-Navalny co-retweet networks were highly synchronized and centralized (star-shaped around @teamnavalny); pro-government networks were more modular, consistent with team-based astroturfing.
- ~50% of users in both camps co-retweeted within 3 minutes at least once; ~25% did so twice or more within 30 minutes.
- Two-year compliance check: 81.3% of pro-Navalny and 77.4% of pro-government tweets remained accessible, with pro-government losses driven mostly by account suspensions (14.5%).

## Connections

This paper is closely tied to the CooRTweet toolchain and the broader coordinated-behavior research program it feeds into — see [[Kulichkina2026-zk]] and the CooRTweet/coordination detection line of work developed in [[Righetti2025-slf9]], [[Righetti2025-sl2a]], and the Giglietto series on coordinated link/behavior sharing ([[Giglietto2023-fa71a001]], [[Giglietto2024-cbeb3f70]], [[Giglietto2022-0e951ac5]], [[Giglietto2020-9d8acdd7]], [[Giglietto2019-882f1900]]). It also connects to work on state-linked information operations and protest/repression dynamics online, notably [[Kuznetsova2025-nu]] on the Russian context and [[Starbird2025-jj]] on coordinated activism, and to conceptual/methodological reflections on what "coordination" means empirically ([[Graham2025-gp]], [[Tornberg2025-ir]]).
