---
title: "“I share your sentiment”—A longitudinal study of Facebook post sentiment and sharing"
aliases: ["“I share your sentiment”—A longitudinal study of Facebook post sentiment and sharing"]
authors: ["Anders Olof Larsson"]
year: 2026
doi: 10.1177/20563051261501463
bibtex_key: Larsson2026-nl
topics: [electoral-communication-and-digital-campaigns, llm-assisted-computational-content-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1177/20563051261501463
podcast_url: 
pdf_available: true
discovery_date: 2026-11-12T22:37:43.006943Z
---

# “I share your sentiment”—A longitudinal study of Facebook post sentiment and sharing

> Larsson, A. O. (2026). “I share your sentiment”—A longitudinal study of Facebook post sentiment and sharing. *Social Media + Society*, *12*. https://doi.org/10.1177/20563051261501463
>
> [View paper](https://doi.org/10.1177/20563051261501463)

## Summary

This longitudinal study tracks how Norwegian political parties deployed sentiment on Facebook across a decade (2016–2025) and three parliamentary elections, and how that sentiment shaped the sharing of their posts. Working with a full population of nearly 39,000 posts from nine major parliamentary parties, Larsson adopts a supply-and-demand framing: parties "supply" emotional content and audiences "demand" (share) it. The central finding is that although positive sentiment remains dominant, negative sentiment has risen over time—driven more by incumbency status than ideology alone—and that negative posts generally win more shares, though this amplification advantage weakens toward the end of the period. The paper offers a non-US, multiparty, consensus-oriented counterpoint to the largely US-focused literature on negative campaigning and the "emotional turn."

## Key Contributions

- Rare longitudinal (10-year, three-election) evidence on both the supply (party sentiment) and demand (audience sharing) sides of the "emotional turn" in online political communication.
- A validated, replicable methodology combining open-source LLMs with human annotation for sentiment analysis in a non-English (Norwegian) context.
- A non-US, multiparty, consensus-oriented case that contrasts with the dominant US-centric literature.
- Nuances the "negativity drives diffusion" thesis by documenting a dampening effect over time and an inverse pattern among ideologically extreme parties.

## Methods

The study analyzes the full population of 39,512 Facebook Page posts (38,898 with text) from nine Norwegian parties, collected via the Meta Content Library in January 2026. Sentiment classification used a three-step pipeline via the Mall R package: initial classification with Gemma 3, human coding of a random 400-post sample (Krippendorff's α = .82), and reclassification with gpt-oss-20b (inter-LLM α = .78). Analyses included chi-square and Cramér's V for sentiment distributions, binary logistic regression testing whether incumbency predicts negativity, and negative binomial regression models (shares as count outcome) reporting incidence rate ratios, overall and per party.

## Findings

- Negative-sentiment posts rose over the decade, plateauing at just over 35% in the final four years; positive posts remained the largest category throughout (year/sentiment Cramér's V = .12).
- Incumbents had markedly lower odds of negativity (OR = 0.255; predicted probability ~16.2% vs. ~43.1% for challengers), confirming incumbency as the primary driver.
- The Socialist Left Party posted the most negative content (44%), followed by the Red Party (39.1%), Greens (33.5%), and Progress Party (31.1%); catch-all parties were least negative (Cramér's V = .22).
- Negativity drove shares overall, but the effect weakened over time—IRRs below .7 in 2016–2021 rose above .7 in 2022–2025.
- The far-left Red Party (IRR = 1.457) and far-right Progress Party (IRR = 2.511) inverted the pattern, gaining more shares with positive sentiment.

## Connections

This paper sits within the growing body of work applying LLM-assisted sentiment and affect analysis to political communication, closely resonating with [[Brady2026-ln]] on emotion and moral content in social media diffusion. Its validation of open-source LLMs against human coding for a non-English corpus speaks to methodological debates seen in [[Le-Mens2025-qz]] and other LLM-based content-analysis work in this register. As a Scandinavian, multiparty case of digital campaigning, it also pairs naturally with the author's related Norwegian-context studies [[Larsson2026-ro]] and [[Kalsnes2025-zb]].
