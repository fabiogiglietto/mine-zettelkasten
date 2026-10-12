---
title: "Birds of the Same Feather Tweet Together: Bayesian Ideal Point Estimation Using Twitter Data"
aliases: ["Birds of the Same Feather Tweet Together: Bayesian Ideal Point Estimation Using Twitter Data"]
authors: ["Pablo Barberá"]
year: 2015
doi: 10.1093/pan/mpu011
bibtex_key: Barbera2015-je
topics: [computational-political-media-influence, political-polarization-partisanship]
citation_count: 634
open_access: false
source_url: https://doi.org/10.1093/pan/mpu011
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807336Z
---

# Birds of the Same Feather Tweet Together: Bayesian Ideal Point Estimation Using Twitter Data

> Barberá, P. (2015). Birds of the Same Feather Tweet Together: Bayesian Ideal Point Estimation Using Twitter Data. *Political Analysis*, *23*, 76–91. https://doi.org/10.1093/pan/mpu011
>
> [View paper](https://doi.org/10.1093/pan/mpu011)

## Summary

Barberá introduces a **Bayesian Spatial Following model** that recovers ideological positions ("ideal points") for both political elites and ordinary citizens directly from the structure of who follows whom on Twitter. The central conceit is that, in a homophilic social network, the decision to follow a political account is a *costly signal*—incurring cognitive-dissonance and attention costs—analogous to a roll-call vote or a campaign contribution, and therefore scalable onto a latent left-right dimension. By treating politically engaged followers as informative "experts" rating elites, the method sidesteps the usual worry that Twitter users are unrepresentative. Barberá validates estimates against roll-call, expert-survey, contribution, and voter-registration benchmarks across six countries, then applies them to the 2012 US presidential campaign to document ideological echo chambers and pronounced mass-level polarization.

## Key Contributions

- A **scalable Bayesian ideal-point estimator** that places hundreds of thousands of elites and citizens on a common continuous scale with standard errors.
- Ideology estimates that require **no roll-call, survey, or contribution data**, can be produced at any time, and generalize across polities—overcoming static-measurement, bridging, and self-selection limits of prior methods.
- **Cross-national validation** in six countries (US, UK, Spain, Germany, Italy, Netherlands) with varying party-system complexity.
- A fine-grained, low-cost ideology covariate for downstream political-behavior research, plus a large-sample re-examination of the echo-chamber debate.
- **Open replication materials and tooling** (Stan code, the `streamR` package), with proposed extensions to dynamic and cross-country bridging models.

## Methods

The model specifies the probability that user *i* follows political account *j* as a logit of the squared Euclidean distance between their latent positions, adjusted for account popularity (α_j) and user political interest (β_i), within a hierarchical multilevel framework. Identification (additive aliasing, scaling, and reflection invariance) is resolved by fixing means/variances and setting signed starting values. Estimation proceeds in two stages: a No-U-Turn Hamiltonian Monte Carlo sampler in Stan on a 10,000-user subsample to fix elite parameters, followed by a parallelizable random-walk Metropolis–Hastings sampler in R for individual users. Data came from Twitter's REST and Streaming APIs—follower lists for 118–318 political accounts per country, filtered to active in-country users following at least three accounts, yielding samples from ~49,000 (Germany) to ~301,537 (US). Validation drew on DW-NOMINATE, IRT roll-call scores, the Chapel Hill Expert Survey, Lax & Phillips opinion estimates, Bonica contribution ideal points, and Ohio voter records. The application analyzed ~65 million "Obama"/"Romney" tweets from the 2012 campaign.

## Findings

- Twitter ideal points correlate strongly with DW-NOMINATE for US legislators (ρ = 0.941 House, 0.954 Senate; within-party ρ ≈ 0.55–0.61).
- Non-partisan pundits (Limbaugh, Beck; Moore, Maddow) are placed with high face validity.
- European party orderings broadly match expert-survey left-right positions, though a single latent dimension performs worse in multidimensional systems (weakest in the UK; extreme parties pulled toward center).
- Mass ideal points reproduce known patterns: **bimodal distributions**, elites more polarized than voters, and correctly ordered self-identified liberals/moderates/conservatives.
- State medians correlate more strongly with survey liberalism (ρ = 0.876) than with Obama's vote share (ρ = 0.785), indicating the dimension captures ideology rather than mere partisanship.
- Individual validation is strong: 90% of users right of the median donated Republican, 98% left donated Democrat (ρ = 0.80 with contribution ideal points).
- In 2012, tweeting was highly bimodal; conservatives were more active (118 vs. 82 tweets) and **85% of retweets occurred between ideologically similar users**, confirming echo-chamber structure, with polarization strongest on the right.

## Connections

This is a foundational methodological contribution to measuring ideology from social-media network structure; [[Barbera2015-fw]] is closely related work from the same author, and its echo-chamber and homophilic-diffusion findings connect to the selective-exposure and polarization literatures represented by [[Bakshy2015-rn]], [[Del-Vicario2016-uj]], [[Flaxman2016-lm]], and [[Bail2018-fk]]. The affective- and elite-polarization framing links it to [[Iyengar2019-jj]] and [[Osmundsen2021-et]], while its critical re-examination of the echo-chamber thesis anticipates later exposure studies such as [[Guess2023-ai]], [[Guess2023-ur]], [[Gonzalez-Bailon2023-uy]], and [[Nyhan2023-gb]].
