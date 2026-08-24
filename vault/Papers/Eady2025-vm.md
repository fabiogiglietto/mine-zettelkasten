---
title: "News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"
aliases: ["News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"]
authors: ["Gregory Eady", "Richard Bonneau", "Joshua A. Tucker", "Jonathan Nagler"]
year: 2025
doi: 10.1017/pan.2024.19
bibtex_key: Eady2025-vm
topics: [computational-political-media-influence, political-polarization-partisanship]
citation_count: 9
open_access: false
source_url: https://doi.org/10.1017/pan.2024.19
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Eady2025-vm.mp3
pdf_available: true
discovery_date: 2026-07-20T15:29:39.742496Z
---

# News sharing on social media: Mapping the ideology of news media, politicians, and the mass public

> Eady, G., Bonneau, R., Tucker, J. A., & Nagler, J. (2025). News sharing on social media: Mapping the ideology of news media, politicians, and the mass public. *Political Analysis*, *33*, 73–90. https://doi.org/10.1017/pan.2024.19
>
> [View paper](https://doi.org/10.1017/pan.2024.19)

## Summary

This paper introduces a Bayesian measurement model — released as the open-source R package `mediascores` — that jointly estimates the ideology of news media organizations, politicians, and ordinary social media users from a single common source of behavioral data: the web links (URLs) they share. Rather than relying on labeled party or ideology tags, the model exploits the homophily in link-sharing: users tend to share content from outlets ideologically close to themselves. Applied to Twitter data on U.S. members of Congress, other political actors, and politically engaged users, the model maps the ideological structure of the online political news environment. Substantively, the authors show that the shared information ecosystem is dominated by ideologically extreme, prolific legislators, and that politicians in less electorally competitive districts share more polarized content — implying that reduced electoral competition (e.g., through gerrymandering) may fuel a more polarized online information environment.

## Key Contributions

- A unified, platform-agnostic framework and open-source R software (`mediascores`) for jointly estimating the ideology of news outlets, politicians, and users from link-sharing data on a common scale.
- A method requiring no pre-existing/labeled ideology data, capable of estimating ideology even for little-known candidates who lack voting records.
- A *behavioral* rather than perceptual measure of elite ideology, derived from politicians' own sharing actions and thus independent of legislative agendas or party discipline.
- Empirical documentation that the online political information ecosystem is skewed toward polarizing content from a small set of extreme, high-volume legislators.
- A link between electoral competition and online sharing behavior, suggesting institutional interventions (e.g., anti-gerrymandering) could indirectly reduce online polarization.

## Methods

The core is a Bayesian measurement model treating a user-by-media-domain matrix of link-sharing counts as arising from a negative binomial distribution, where sharing probability declines in the squared distance between a user's ideology (θ) and an outlet's ideology (ζ). The model includes user- and domain-specific intercepts and a news-organization dispersion parameter (ω), with hierarchical priors placed separately on Democratic politicians, Republican politicians, and ordinary users; identification (reflection invariance and additive aliasing) follows Jackman's (2001) approach. Data come from Twitter: 1,152 accounts from 699 political actors (116th Congress, governors, executive/cabinet, prominent party figures), a random sample of 10,000 politically engaged users, and 220 national news domains. Validation uses convergent validity against NOMINATE roll-call scores for legislators and against YouGov survey-linked Twitter data for ordinary users. OLS regressions then predict the ideological extremity of politicians' sharing from district/state partisan alignment, controlling for party, chamber, and NOMINATE.

## Findings

- Politicians' news sharing nearly perfectly separates them by party; even a single-common-prior model shows only ~3% distributional overlap between parties.
- Media scores correlate very highly with NOMINATE overall (ρ = 0.96), with moderate-to-high within-party correlations.
- Members of "The Squad" appear far to the left in sharing ideology (left of 99% of Congress) despite centrist NOMINATE placement — sharing captures behavior missed by roll-call votes.
- For ordinary users, sharing-based ideology correlates on average ρ = 0.73 with survey measures, comparable to the correlation among the survey measures themselves.
- News media ideology is bimodally distributed, with high face validity (e.g., Breitbart right of Fox News right of WSJ; Reuters/AP centrist).
- Politicians share more news than users (0.082 vs. 0.024 news links per tweet), and ideologically extreme politicians share substantially more.
- Lower district/state competitiveness is significantly associated with more extreme news sharing, even after controlling for NOMINATE, party, and chamber.

## Connections

This work sits alongside other efforts to measure ideology and news exposure from platform behavioral traces; [[Gonzalez-Bailon2024-rq]] and [[Bakshy2015-rn]] similarly characterize the ideological structure of online news exposure and sharing, while [[Green2025-ap]] engages related questions about elite polarization and online political behavior. Its concern with ideological asymmetries in shared information also connects to broader platform-data efforts on news diffusion such as [[Pierri2025-hm]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Eady2025-vm.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-safe-seats-and-extreme-feeds-whos/id1866587707?i=1000778009373)
