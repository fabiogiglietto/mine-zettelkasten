---
title: "Partisan polarization is the primary psychological motivation behind political fake news sharing on twitter"
aliases: ["Partisan polarization is the primary psychological motivation behind political fake news sharing on twitter"]
authors: ["MATHIAS OSMUNDSEN", "ALEXANDER BOR", "PETER BJERREGAARD VAHLSTRUP", "ANJA BECHMANN", "MICHAEL BANG PETERSEN"]
year: 2021
doi: 10.1017/s0003055421000290
bibtex_key: Osmundsen2021-et
topics: [political-polarization-partisanship, information-disorder-theory]
citation_count: 374
open_access: false
source_url: https://doi.org/10.1017/s0003055421000290
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807275Z
---

# Partisan polarization is the primary psychological motivation behind political fake news sharing on twitter

> OSMUNDSEN, M., BOR, A., VAHLSTRUP, P. B., BECHMANN, A., & PETERSEN, M. B. (2021). Partisan polarization is the primary psychological motivation behind political fake news sharing on twitter. *American Political Science Review*, *115*, 999–1015. https://doi.org/10.1017/s0003055421000290
>
> [View paper](https://doi.org/10.1017/s0003055421000290)

## Summary

This paper adjudicates among three competing psychological explanations for why people share political fake news on Twitter: **ignorance** (poor cognitive reflection, low knowledge or literacy), **disruption** (a desire to create chaos, e.g., trolling and cynicism), and **partisan polarization** (partisan animus, especially out-party hatred). By linking survey-based psychological profiles of over 2,300 American Twitter users to their actual news-sharing behavior and to sentiment analyses of ~500,000 headlines, the authors find little support for ignorance, mixed support for disruption, and strong support for polarization. Their central argument is that fake news sharing is *not* a distinct pathology but the extreme end of a one-dimensional partisan news continuum: it follows the same goal-oriented, opponent-derogating logic that governs the sharing of ordinary partisan news.

## Key Contributions

- One of the first behavioral tests linking rich individual-level psychological profiles to real Twitter news-sharing behavior at scale.
- Adjudicates three competing theories (ignorance, disruption, polarization) using both individual-difference and content-based analyses.
- First test distinguishing in-party love from out-party hatred as the driver of fake news sharing, finding out-party animus dominant (~2× larger coefficients).
- Introduces large-scale headline sentiment analysis to demonstrate a partisan news-source continuum and an asymmetry in the *supply* of politically useful content.
- Argues that accuracy-focused interventions (e.g., fact-checking) are unlikely to work because sharing is driven by usefulness in attacking opponents, not by accuracy concerns.

## Methods

The authors commissioned a YouGov survey (Dec 2018–Jan 2019) of U.S. Twitter users, linking confidential responses to scraped public Twitter data (~2.7M tweets/retweets) for a final sample of N=2,337. Fake news sharing was operationalized at the publisher level by matching tweeted URLs against a list of 608 fake news sources; real news was matched against 260 AllSides-rated publishers. Two headline corpora were built (75,560 shared headlines and ~500,000 front-page headlines from Archive.org) and analyzed with the sentimentR package plus custom elite-name dictionaries to measure negativity toward each party. Predictors were measured via survey batteries: CRT-2 and political knowledge (ignorance); a trolling scale and political cynicism (disruption); partisanship and in-party/out-party affect (polarization). Analysis used logistic regression (average marginal effects), with robustness checks including Grinberg et al.'s categories, Pennycook & Rand trustworthiness ratings, and Quasi-Poisson count models.

## Findings

- News sharing was rare and concentrated: only ~3% of tweets contained news links, ~4% of those from fake sources; 1% of panelists shared ~75% of fake news, and only 11% shared any at all.
- Direct ignorance measures did *not* predict fake news sharing — cognitive reflection was unrelated, and higher political knowledge and digital literacy actually predicted *more* fake news sharing.
- Apolitical trolling predicted less sharing overall, while political cynicism predicted more sharing of both fake and real news (mixed disruption support).
- Partisanship and especially negative out-party affect strongly predicted fake news sharing; out-party hatred effects were roughly twice as large as in-party love.
- Sharing of ideologically slanted real news correlated strongly with sharing fake news of the same slant; partisans never shared incongruent fake news.
- Only pro-Republican fake news consistently derogated Democrats more than Republicans, matching the observed asymmetry in Republican fake news sharing — suggesting a supply-side rather than psychological explanation.
- The motivations behind fake and real news sharing were psychologically nearly identical.

## Connections

This paper anchors the individual-level, psychological side of the misinformation-sharing literature and connects tightly to work on the empirical reach and concentration of fake news exposure on Twitter, such as [[Grinberg2019-ua]] and [[Guess2019-ym]], as well as to reviews of the science of fake news like [[Lazer2018-mm]] and estimates of its prevalence in [[Allen2020-nj]]. Its dual-motivation framing (accuracy vs. directional goals) engages directly with accuracy-nudge and reflection debates in [[Pennycook2021-jq]] and the motivated-reasoning tradition of [[Kunda1990-cg]], while its emphasis on out-party animus as the engine of sharing links to affective-polarization scholarship such as [[Iyengar2019-jj]] and [[Bail2018-fk]]; the diffusion dynamics it describes complement [[Vosoughi2018-at]].
