---
title: "Recommender system in X inadvertently profiles ideological positions of users"
aliases: ["Recommender system in X inadvertently profiles ideological positions of users"]
authors: ["Paul Bouchaud", "Pedro Ramaciotti"]
year: 2026
doi: 
bibtex_key: Bouchaud2026-lr
topics: [facebook-algorithmic-governance, computational-political-media-influence]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2602.02624v2
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bouchaud2026-lr.mp3
pdf_available: true
discovery_date: 2026-03-18T06:36:45.219988Z
---

# Recommender system in X inadvertently profiles ideological positions of users

> Bouchaud, P., & Ramaciotti, P. (2026). Recommender system in X inadvertently profiles ideological positions of users. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2602.02624v2)

## Summary

This paper asks whether X's (formerly Twitter) friend-recommendation engine inadvertently learns users' political orientations, even though it was never explicitly designed to profile ideology. Using a data donation program that collected over 2.5 million "Who to Follow" recommendations from 682 French volunteers between January 2023 and May 2024, the authors reconstruct an approximation of X's 256-dimensional user embedding from publicly documented architectural details. They show that a single linear direction in this reconstructed space correlates almost perfectly (ρ=0.887) with users' Left–Right ideological positions, independently of demographic covariates. They further propose a constrained recommendation method that removes this linearly-encoded political information while largely preserving topical relevance — framing the finding as both an empirical demonstration of the linear representation hypothesis in a deployed system and a challenge to the legal distinction between active and passive profiling.

## Key Contributions

- First empirical, quantitative measurement of inadvertent political profiling by a large-scale, deployed recommender system at the level of individual regular users.
- A reproducible methodology for approximating a closed recommender's embedding space from donated exposure data plus public architectural knowledge — applicable beyond X.
- Empirical demonstration of the linear representation hypothesis inside a production AI system serving hundreds of millions of users.
- A constrained-recommendation procedure (iterative orthogonal projection) that strips sensitive linearly-encoded attributes while preserving relevance, offered as a candidate compliance tool under GDPR, LGPD, PIPA, nFADP, and the DSA.
- A conceptual argument that AI explainability undermines the active/passive profiling distinction central to data-privacy regulation.

## Methods

The authors ran a browser-plugin data donation campaign (2,549,008 WTF recommendations, 682 volunteers, study population of 26,509 users), supplemented by follower networks, profiles, and recent posts via X's API. They reconstructed a 256-dimensional embedding via constrained optimization using a TransE scoring function following X's documented architecture, blending "Follow" and "WTF" loss components and using mixed negative-edge sampling. User attributes were inferred externally: Left–Right and anti-elite positions through ideology scaling calibrated against the Chapel Hill Expert Survey, age/gender via the M3 model, and topic interests via a tweet topic model. Canonical Correlation Analysis identified embedding directions maximally correlated with each attribute (with permutation tests), and an iterative orthogonal projection removed the ideological direction, evaluated by comparing recommendation diversity and topical relevance before and after.

## Findings

- The reconstructed embedding predicts held-out WTF recommendations with AUC-ROC 0.700 (Precision@1 0.725, Precision@3 0.691), far exceeding heuristic baselines.
- CCA directions correlate strongly with attributes: Left–Right 0.887, anti-elite 0.863, news interest 0.848, popularity 0.730, age 0.562, gender 0.384 (all p<0.0001).
- Attribute directions are largely orthogonal; only age and news interest show significant alignment.
- The Left–Right direction correctly orders followers of French parties (La France Insoumise → Renaissance → Rassemblement National), and the anti-elite direction separates populist from centrist party followers.
- Left–Right encoding is not reducible to demographics (modest ρ=0.172 with age, ρ=-0.275 with gender).
- Results are robust to training-parameter changes, negative sampling, simulated device-coverage bias (up to 39.2% missing recommendations), demographic sub-sampling, temporal splits, and graph evolution.
- Removing the Left–Right direction increases ideological diversity (Cohen's d=0.477) while preserving topical relevance (topic-distribution cosine similarity = 0.948) and producing the largest change in the recommended set among all attributes tested.

## Connections

This work extends recommender auditing beyond item-level diversity and causal policy effects toward the internal user representations these systems build, complementing field-experimental work on Facebook's feed such as [[Guess2023-ai]], [[Guess2023-ur]], [[Nyhan2023-gb]], and [[Gonzalez-Bailon2023-uy]], and the ideological-segregation measurement of [[Bakshy2015-rn]]. Its ideology-scaling approach builds directly on the embedding and estimation traditions of [[Barbera2015-fw]], [[Barbera2015-je]], and [[Eady2023-xg]], while its concern with algorithmic opacity and user profiling resonates with critical accounts of platform visibility and classification in [[Bucher2017-qh]] and [[Cotter2019-js]]. A closely related companion effort on X's recommender dynamics is [[Bouchaud2026-np]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bouchaud2026-lr.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-xs-political-algorithm-profiling/id1866587707?i=1000755979538)
