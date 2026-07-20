---
title: "News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"
aliases: ["News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"]
authors: ["Gregory Eady", "Richard Bonneau", "Joshua A Tucker", "Jonathan Nagler"]
year: 2025
doi: 10.31219/osf.io/ch8gj
bibtex_key: Eady2025-vm
topics: [political-polarization-and-partisanship, llms-in-computational-content-analysis]
citation_count: 14
open_access: false
source_url: https://doi.org/10.31219/osf.io/ch8gj
podcast_url: 
pdf_available: true
discovery_date: 2026-07-20T15:29:39.742496Z
---

# News sharing on social media: Mapping the ideology of news media, politicians, and the mass public

> Eady, G., Bonneau, R., Tucker, J. A., & Nagler, J. (2025). News sharing on social media: Mapping the ideology of news media, politicians, and the mass public. *Polit. Anal.*, *33*, 73–90. https://doi.org/10.31219/osf.io/ch8gj
>
> [View paper](https://doi.org/10.31219/osf.io/ch8gj)

## Summary

This paper introduces a Bayesian measurement model — packaged as the open-source R library `mediascores` — that jointly estimates the ideology of news media organizations, politicians, and ordinary social media users from a single behavioral signal: the web links (URLs) they share. Applied to Twitter data on U.S. members of Congress, other political actors, and politically engaged users, the model maps the ideological structure of the online news environment without relying on labeled data such as party or ideology tags. Substantively, it shows that ideologically extreme politicians share far more news than moderates and that reduced electoral competition is associated with more polarized sharing, implying that institutional factors like gerrymandering may feed a more polarized online information ecosystem.

## Key Contributions

- A unified, platform-agnostic framework and open-source R software (`mediascores`) for jointly estimating the ideology of news outlets, politicians, and users from link-sharing data.
- A method that requires no pre-existing ideology labels and can estimate ideology even for little-known candidates lacking voting records.
- A *behavioral* rather than perception-based measure of elite ideology, independent of legislative agendas or party discipline.
- Empirical documentation that the online news ecosystem is skewed toward polarizing content from a small set of prolific, extreme legislators.
- A link between electoral competitiveness and online sharing behavior, suggesting anti-gerrymandering interventions could indirectly dampen online polarization.

## Methods

- A Bayesian measurement model treating a user-by-domain link-sharing count matrix as negative-binomially distributed, where sharing probability declines in the squared distance between a user's ideology (theta) and an outlet's ideology (zeta).
- Parameters include user- and domain-specific intercepts plus a news-organization dispersion parameter; hierarchical priors are placed separately on Democratic politicians, Republican politicians, and ordinary users, with reflection invariance and additive aliasing handled via Jackman's identification approach.
- Data drawn from Twitter: 1,152 accounts from 699 political actors (116th Congress, governors, executive/cabinet, prominent party figures), a random sample of 10,000 politically engaged users, and 220 national news domains.
- Validated for convergent validity against NOMINATE roll-call scores (for legislators) and YouGov survey-linked Twitter data (for ordinary users), plus OLS regressions predicting sharing extremity from district/state partisan alignment.

## Findings

- Politicians' news sharing nearly perfectly separates them by party; even with a single common prior, only ~3% of Democratic and Republican distributions overlap.
- Media scores correlate very highly with NOMINATE overall (rho = 0.96), with moderate-to-high within-party correlations.
- "The Squad" appears far to the left in sharing ideology despite centrist NOMINATE placement, showing sharing captures behavior missed by roll-call measures.
- For ordinary users, sharing-based ideology correlates on average rho = 0.73 with survey measures — comparable to correlations among the survey measures themselves.
- The distribution of news media ideology is bimodal, with well-known outlets ordering with high face validity (e.g., Breitbart right of Fox right of WSJ; Reuters/AP centrist).
- Politicians share more news than users (0.082 vs. 0.024 links per tweet), and extreme politicians share substantially more than moderates.
- Lower district/state competitiveness is significantly associated with more extreme news sharing, even controlling for NOMINATE ideology, party, and chamber.

## Connections

This paper builds directly on homophily-based social media measurement of ideology, sitting alongside [[Bakshy2015-rn]] on partisan exposure to news through sharing on social platforms. Its use of link-sharing as a behavioral signal connects to the broader literature on URL-sharing dynamics and coordinated diffusion studied in [[Giglietto2020-6278a4aa]], [[Giglietto2019-882f1900]], and [[Giglietto2024-cbeb3f70]]. The substantive concern with elite-driven polarization and the skew of the online information ecosystem toward extreme actors relates to [[DeVerna2025-dl]] on news sharing and misinformation among political elites.
