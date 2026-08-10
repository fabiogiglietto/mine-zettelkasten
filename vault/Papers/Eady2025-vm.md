---
title: "News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"
aliases: ["News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"]
authors: ["Gregory Eady", "Richard Bonneau", "Joshua A Tucker", "Jonathan Nagler"]
year: 2025
doi: 10.31219/osf.io/ch8gj
bibtex_key: Eady2025-vm
topics: [polarization-partisanship, computational-text-methods-llm]
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

This paper introduces a unified Bayesian measurement model — and an accompanying open-source R library, `mediascores` — that jointly estimates the ideology of news media organizations, politicians, and ordinary social media users from a single behavioral source: the URLs they share. Using Twitter data on U.S. members of Congress, other political actors, and politically engaged users, the authors map the ideological structure of the online news environment without relying on labeled party or ideology data. Substantively, they argue that ideologically extreme politicians share far more news than moderates, and that reduced electoral competition (e.g., through gerrymandering) is associated with more polarized sharing — implying that institutional reforms could indirectly cool the online information ecosystem.

## Key Contributions

- A unified, platform-agnostic framework for jointly estimating ideology of news outlets, politicians, and users from link-sharing behavior alone.
- Open-source parallelized R software (`mediascores`) implementing the model.
- A method requiring no pre-existing ideology labels, enabling estimation even for little-known candidates without voting records.
- A *behavioral* (rather than perception-based) measure of elite ideology, distinguishing it from prior following/endorsement approaches.
- Empirical documentation that the online news ecosystem is skewed toward polarizing content from a small set of prolific, extreme legislators.
- A link between electoral competition and online sharing behavior, suggesting anti-gerrymandering interventions could reduce polarization.

## Methods

The core is a Bayesian measurement model treating a user-by-domain link-sharing count matrix as arising from a negative binomial distribution, where sharing probability declines in the squared distance between a user's ideology (theta) and an outlet's ideology (zeta). Parameters include user- and domain-specific intercepts and a dispersion parameter, with hierarchical priors placed separately on Democratic politicians, Republican politicians, and ordinary users; identification (reflection invariance, additive aliasing) follows Jackman's approach. Data comprise 1,152 accounts from 699 political actors (116th Congress, governors, executive/cabinet, party figures), a random sample of 10,000 politically engaged users, and 220 national news domains. Validation proceeds through convergent validity against NOMINATE roll-call scores and against YouGov survey-linked Twitter data, alongside OLS models predicting news-sharing extremity from district/state partisan alignment.

## Findings

- News sharing nearly perfectly separates politicians by party; even with a common prior removing party information, only ~3% overlap remains between Democratic and Republican distributions.
- Media scores correlate highly with NOMINATE overall (rho = 0.96); within-party correlations are moderate to high.
- "The Squad" appears far left in news-sharing ideology despite centrist NOMINATE placement, showing sharing captures behavior missed by roll-call measures.
- For ordinary users, sharing-based ideology correlates rho = 0.73 with survey measures — comparable to correlations among the survey measures themselves.
- The distribution of news media ideology is bimodal, with well-known outlets ordering with high face validity (Breitbart right of Fox right of WSJ; Reuters/AP centrist).
- Politicians share more news than users (0.082 vs. 0.024 news links per tweet), and ideologically extreme politicians share substantially more.
- Greater district/state partisan alignment (lower competitiveness) is significantly associated with more extreme news sharing, even controlling for NOMINATE, party, and chamber.

## Connections

This paper's URL-based approach to inferring ideology and mapping partisan news flows connects closely to work on link-sharing as a signal of the information ecosystem, such as [[Bakshy2015-rn]] on exposure to cross-cutting content on social platforms. Its focus on elite and mass polarization dynamics relates to broader partisanship research in this register, including [[Mosleh2024-op]] and [[DeVerna2025-dl]] on political behavior and sharing on social media. The measurement-model lineage it extends (following/endorsement-based ideal points) is otherwise largely distinct from the LLM-based content-analysis papers grouped under the same topics.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Eady2025-vm.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
