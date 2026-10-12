---
title: "Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber?"
aliases: ["Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber?"]
authors: ["Pablo Barberá", "John Jost", "Jonathan Nagler", "Joshua Tucker", "Richard Bonneau"]
year: 2015
doi: 10.7910/dvn/f9ichh
bibtex_key: Barbera2015-fw
topics: [political-polarization-partisanship, computational-political-media-influence]
citation_count: 1
open_access: true
source_url: https://doi.org/10.7910/dvn/f9ichh
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807360Z
---

# Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber?

> Barberá, P., Jost, J., Nagler, J., Tucker, J., & Bonneau, R. (2015). Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber?. *Harvard Dataverse*, *26*, 1531–1542. https://doi.org/10.7910/dvn/f9ichh
>
> [View paper](https://doi.org/10.7910/dvn/f9ichh)

## Summary

This paper interrogates the popular claim that online political communication is a monolithic "echo chamber," proposing instead that Twitter can also host a broader "national conversation." Analyzing nearly 150 million tweets across 12 political and nonpolitical events (2012–2014) and estimating the ideological positions of 3.8 million users from their follower networks, the authors argue that ideological segregation is not a fixed property of social media but varies substantially by topic and over time. Political issues produce echo-chamber-like homophily, while many nonpolitical events (natural disasters, sporting events, awards ceremonies) cross ideological lines. The paper also documents a persistent asymmetry: liberals share across ideological boundaries more than conservatives do.

## Key Contributions

- Introduced a scalable, text-free method for estimating ideology from network follow structure, using correspondence analysis as a tractable approximation to Bayesian latent-space models for millions of users.
- Provided large-scale behavioral evidence that online ideological segregation is topic- and time-contingent, challenging blanket echo-chamber narratives.
- Documented a robust liberal–conservative asymmetry in cross-ideological retweeting, connecting it to psychological theories of ideological difference.
- Demonstrated the value of unobtrusive "big data" from naturally occurring settings over self-selected partisan samples used in prior work.
- Analyzed a broad, mixed set of 12 political and nonpolitical events with openly shared data and materials.

## Methods

Ideology was estimated by placing users in a latent space based on which political accounts they follow, restricted initially to users following at least 10 of a curated set of political accounts and then projected onto a common standardized scale via singular value decomposition of a connection matrix. Roughly 150 million tweets were collected through the Streaming API using topic-specific keyword lists, with activity, location, and spam filters to remove bots. Retweeting behavior was analyzed with three polarization metrics (homophily percentage, ideological homogeneity of detected retweet communities, and average extremity of retweeted content), plus Poisson regression models to test for asymmetry while adjusting for each group's baseline propensity to retweet and be retweeted. Estimates were validated against statewide survey ideology (r = .87), roll-call ideal points (r = .95), and matched voter-registration records (78% correct classification).

## Findings

- Political topics (2012 election, government shutdown, State of the Union) showed strong ideological homophily; e.g., 38% of 2012-election retweets occurred among extreme conservatives and 28% among extreme liberals, though each group was only 16% of the sample.
- Nonpolitical topics (Boston Marathon bombing, Super Bowl, Winter Olympics) crossed ideological boundaries with low homophily and heterogeneous clusters.
- The Newtown shooting shifted from national conversation to echo chamber as discussion moved from tragedy toward gun-control policy; Syria showed the reverse trajectory.
- Highly polarized topics drew most-shared content from ideologically extreme authors; nonpolitical events drew more from moderate sources.
- Across all political topics, liberals were significantly more likely than conservatives to retweet across ideological lines.
- Cross-ideological retweeting was higher for nonpolitical topics, and the liberal–conservative asymmetry there was smaller (not significant for the Winter Olympics).

## Connections

This is a foundational network-based counterpoint to strong echo-chamber claims, and its ideology-estimation method builds directly on the authors' earlier work in [[Barbera2015-je]]. It complements experimental and platform-scale studies revisiting echo-chamber and cross-cutting exposure debates such as [[Bakshy2015-rn]], [[Guess2023-ai]], [[Gonzalez-Bailon2023-uy]], [[Nyhan2023-gb]], and [[Bail2018-fk]], and speaks to broader accounts of selective exposure and polarization in [[Flaxman2016-lm]], [[Iyengar2019-jj]], [[Del-Vicario2016-uj]], and [[Benkler2018-lw]].
