---
title: "News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"
aliases: ["News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"]
authors: ["Gregory Eady", "Richard Bonneau", "Joshua A Tucker", "Jonathan Nagler"]
year: 2025
doi: 10.31219/osf.io/ch8gj
bibtex_key: Eady2025-vm
topics: [computational-political-media-influence, political-polarization-partisanship]
citation_count: 14
open_access: false
source_url: https://doi.org/10.31219/osf.io/ch8gj
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Eady2025-vm.mp3
pdf_available: true
discovery_date: 2026-07-20T15:29:39.742496Z
---

# News sharing on social media: Mapping the ideology of news media, politicians, and the mass public

> Eady, G., Bonneau, R., Tucker, J. A., & Nagler, J. (2025). News sharing on social media: Mapping the ideology of news media, politicians, and the mass public. *Polit. Anal.*, *33*, 73–90. https://doi.org/10.31219/osf.io/ch8gj
>
> [View paper](https://doi.org/10.31219/osf.io/ch8gj)

## Summary

This paper introduces a Bayesian measurement model and an accompanying open-source R package (`mediascores`) that jointly estimates the ideology of news media organizations, politicians, and ordinary social media users from a single behavioral currency: shared web links (URLs). By treating link-sharing as a homophily-driven behavior — users share content ideologically proximate to themselves — the authors place outlets, elites, and the mass public on a common scale without any labeled party or ideology data. Applied to Twitter data on U.S. members of Congress and politically engaged users, the model reveals that ideologically extreme politicians share disproportionately more political news, skewing the online information environment away from the median legislator. The authors further link this to electoral incentives, finding that politicians in less competitive districts share more polarized content.

## Key Contributions

- A unified, platform-agnostic framework and open-source R library (`mediascores`) for jointly estimating the ideology of news outlets, politicians, and users from link-sharing behavior alone.
- A method requiring no pre-existing ideology labels, allowing estimation even for little-known candidates without voting records.
- A **behavioral** (rather than perception-based) measure of elite ideology, derived from politicians' own sharing actions rather than followers' endorsements — distinguishing it from prior following-based approaches.
- Empirical documentation that the online political information ecosystem is dominated by polarizing content from a small set of prolific, ideologically extreme legislators.
- A substantive link between reduced electoral competition (e.g., gerrymandering) and more polarized online sharing, suggesting institutional interventions could indirectly dampen online polarization.

## Methods

The core model treats a user-by-domain link-sharing count matrix as arising from a negative binomial distribution, where sharing probability declines in the squared ideological distance between a user's position (theta) and an outlet's position (zeta). User- and domain-specific intercepts plus a dispersion parameter are included, with separate hierarchical priors for Democratic politicians, Republican politicians, and ordinary users; identification (reflection invariance, additive aliasing) follows Jackman's approach. The data comprise 1,152 accounts from 699 political actors (116th Congress, governors, cabinet, party figures), a random sample of 10,000 politically engaged users, and 220 national news domains. Validation proceeds via convergent validity against NOMINATE roll-call scores for legislators and against YouGov survey-linked data for ordinary users, alongside OLS regressions predicting sharing extremity from district/state partisan alignment.

## Findings

- Politicians' news sharing nearly perfectly separates by party — even a single common-prior model (removing party info) shows only ~3% overlap between Democratic and Republican distributions.
- Media scores correlate very highly with NOMINATE overall (rho = 0.96), with moderate-to-high within-party correlations.
- Members of "The Squad" appear far left in sharing ideology despite centrist NOMINATE placement, showing sharing captures behavior missed by roll-call votes.
- For ordinary users, sharing-based ideology correlates rho = 0.73 with survey measures — comparable to correlations among the survey measures themselves (~0.64).
- The distribution of news media ideology is bimodal, with high face validity (Breitbart right of Fox right of WSJ; Reuters/AP centrist).
- Politicians share more news than users (0.082 vs. 0.024 links per tweet), and ideologically extreme politicians share far more than moderates.
- Greater district/state partisan alignment (lower competitiveness) is significantly associated with more extreme news sharing, even controlling for NOMINATE, party, and chamber.

## Connections

This paper is primarily a measurement contribution within the ideal-point and homophily-based social-media estimation tradition, extending following/endorsement approaches to shared URLs. It connects to work on partisan link-sharing dynamics and news diffusion on social platforms, such as [[Bakshy2015-rn]], and to studies mapping coordinated or ideologically structured sharing behavior like [[Giglietto2019-882f1900]] and [[Giglietto2020-6278a4aa]]. Its substantive focus on elite–public polarization and skewed information ecosystems situates it alongside broader polarization research in this topic cluster.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Eady2025-vm.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-safe-seats-and-extreme-feeds-whos/id1866587707?i=1000778009373)
