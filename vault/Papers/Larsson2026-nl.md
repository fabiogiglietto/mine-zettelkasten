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
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Larsson2026-nl.mp3
pdf_available: true
discovery_date: 2026-11-12T22:37:43.006943Z
---

# “I share your sentiment”—A longitudinal study of Facebook post sentiment and sharing

> Larsson, A. O. (2026). “I share your sentiment”—A longitudinal study of Facebook post sentiment and sharing. *Social Media + Society*, *12*. https://doi.org/10.1177/20563051261501463
>
> [View paper](https://doi.org/10.1177/20563051261501463)

## Summary

This longitudinal study tracks how Norwegian political parties deployed negative, positive, and neutral sentiment on Facebook across a decade (2016–2025) spanning three parliamentary elections, and how that sentiment shaped the sharing of their posts. Drawing on a full population of nearly 39,000 posts from all major parliamentary parties, Larsson adopts a supply-and-demand framing: the "supply" side being the sentiment parties choose to produce, the "demand" side being audience amplification through shares. The headline argument is that while positive sentiment still dominates, negativity has grown over time—driven more by incumbency status than ideology alone—and that although negative posts generally attract more shares, this amplification advantage weakens toward the end of the period. The study positions itself as a non-US, multiparty, consensus-oriented counterpoint to the largely US-centred literature on online negativity and campaigning.

## Key Contributions

- Rare longitudinal (10-year, three-election) evidence on the "emotional turn" in online political communication, covering both the supply (party sentiment) and demand (audience sharing) sides.
- A validated, replicable methodology combining open-source LLMs with human annotation for sentiment analysis in a non-English (Norwegian) context.
- A non-US, multiparty, consensus-oriented case that contrasts with the dominant US-focused literature.
- Nuances the "negativity drives diffusion" thesis by documenting a dampening effect over time and an inverse pattern for ideologically extreme parties.

## Methods

Larsson analyses a full population of 39,512 Facebook Page posts (38,898 with text) from nine major Norwegian parliamentary parties, collected via the Meta Content Library in January 2026. Sentiment was coded in three steps using the Mall R package: initial classification with Gemma 3, human coding of a random 400-post sample (Krippendorff's α = .82), and reclassification with gpt-oss-20b (inter-LLM α = .78). Analyses include chi-square and Cramér's V for sentiment distributions, binary logistic regression predicting negative vs. positive sentiment from incumbency, and negative binomial regression (shares as a count outcome, reported as incidence rate ratios) estimating sentiment's effect on sharing overall and per party, with Social Democrats as the reference category.

## Findings

- Negative-sentiment posts rose over the decade, plateauing just above 35% in the final four years, while positive posts remained the largest category throughout.
- Incumbents had markedly lower odds of posting negatively (OR = 0.255); predicted probability of negativity was ~16.2% for incumbents vs. ~43.1% for challengers.
- The Socialist Left Party posted the most negative content (44%), followed by the Red Party (39.1%), Greens (33.5%), and Progress Party (31.1%); the catch-all Social Democrats and Conservatives were least negative.
- Negativity increased shares for all parties combined, but the effect weakened over time (IRRs below .7 in 2016–2021 rising above .7 in 2022–2025).
- The two ideological extremes—the far-left Red Party and far-right Progress Party—bucked the trend, gaining more shares with positive sentiment (Progress Party IRR = 2.511, Red Party = 1.457).

## Connections

This paper is a companion to the author's other recent work on Norwegian/Scandinavian digital campaigning and platform communication, notably [[Larsson2026-ro]] and [[Kalsnes2025-zb]]. Its LLM-plus-human validation strategy for non-English sentiment classification speaks directly to the methodological debates in [[Le-Mens2025-qz]] and [[Tornberg2025-ir]] on using large language models for computational content analysis. The focus on emotion, negativity, and sharing/diffusion also connects to broader work on affective dynamics driving online amplification, such as [[Brady2026-ln]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Larsson2026-nl.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-why-going-negative-doesnt-always/id1866587707?i=1000801596711)
