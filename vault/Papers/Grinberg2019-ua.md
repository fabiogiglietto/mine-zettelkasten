---
title: "Fake news on Twitter during the 2016 U.S. presidential election"
aliases: ["Fake news on Twitter during the 2016 U.S. presidential election"]
authors: ["Nir Grinberg", "Kenneth Joseph", "Lisa Friedland", "Briony Swire-Thompson", "David Lazer"]
year: 2019
doi: 10.1126/science.aau2706
bibtex_key: Grinberg2019-ua
topics: [electoral-social-media-research, information-disorder-theory]
citation_count: 1290
open_access: false
source_url: https://doi.org/10.1126/science.aau2706
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807350Z
---

# Fake news on Twitter during the 2016 U.S. presidential election

> Grinberg, N., Joseph, K., Friedland, L., Swire-Thompson, B., & Lazer, D. (2019). Fake news on Twitter during the 2016 U.S. presidential election. *Science*, *363*, 374–378. https://doi.org/10.1126/science.aau2706
>
> [View paper](https://doi.org/10.1126/science.aau2706)

## Summary

This paper delivers one of the first individual-level measurements of exposure to and sharing of fake news on Twitter, using a panel of 16,442 accounts matched to U.S. voter registration records during the 2016 presidential election season. The central argument is deflationary: contrary to alarmist narratives, engagement with fake news was extraordinarily concentrated among a tiny sliver of users — disproportionately conservative, older, and highly politically engaged — while most political news exposure for people across the spectrum continued to come from mainstream outlets. Fake news sources formed a distinct, insulated right-leaning cluster that remained a niche interest even for avid news consumers, and the authors find that belief congruence, not veracity, drove sharing decisions.

## Key Contributions

- One of the first direct measurements of ordinary citizens' fake news exposure and sharing, linked to real voter identities rather than aggregate platform data or self-report surveys.
- Documents extreme concentration of fake news engagement among tiny subpopulations, reframing the perceived scale of the problem.
- Identifies individual-level predictors (conservatism, age, political engagement) via regression modeling fit separately by political affinity group.
- Maps fake news sources within the broader media ecosystem through a coexposure network, showing they form an insulated right-leaning cluster.
- Proposes and simulates concrete, targeted platform interventions (demoting frequent posters, capping posts, fact-checker partnerships).

## Methods

The authors built a panel of Twitter accounts active from 1 August to 6 December 2016 by linking voter registration records to Twitter, validating representativeness against a Pew Research probability sample. Fake news was defined at the publisher level (following the Lazer et al. framework), classifying sources into black, red, and orange tiers from fact-checker lists and manual annotation. Each panel member's news feed was estimated by sampling tweets from followed accounts, restricted to political tweets with external URLs. Members were assigned to political affinity subgroups based on feed similarity to registered partisans. Binomial and logistic regressions identified predictors of exposure and sharing; a coexposure network (using Dianati's statistically significant edge technique and ensemble clustering) positioned sources within the wider ecosystem; and a simulation tested capping political URLs at 20 per day.

## Findings

- Fake news accounted for 5.0% of aggregate political URL exposures and 6.7% of shares, rising in the final campaign weeks.
- Engagement was extremely concentrated: 1% of individuals produced 80% of fake news exposures; 0.1% produced nearly 80% of shares.
- The top seven fake news sources accounted for over half of all fake news exposures.
- Fake news exposure skewed sharply right — comprising 2.5% of the left but 16.3% of the right; 21% of the extreme right shared fake news versus under 5% on the left or center.
- A 10-fold increase in political exposures roughly doubled the proportion of fake news exposures (superlinear selective exposure); age was positively associated with engagement across all groups.
- Congruent sources were shared at higher rates than incongruent ones, with no significant sharing difference between fake and nonfake *congruent* sources — implying fake news was not inherently more viral.
- "Supersharers" and "superconsumers" dwarfed typical users (median supersharer: 71 tweets/day vs. 0.1) and were likely partially automated "cyborg" accounts.
- The coexposure network showed a mainstream cluster (18.4% of sites) generating 72–86% of exposures, while the conservative fake-news-heavy cluster mattered mostly for the extreme right.
- Capping political URLs at 20/day would cut fake news content by 32% while affecting only 1% of non-supersharers' content.

## Connections

This paper extends the individual-level empirical tradition on misinformation exposure alongside work using browsing and behavioral data such as [[Guess2019-ym]], [[Guess2023-ai]], [[Guess2023-ur]], and [[Eady2023-xg]], and its concentration findings resonate with the small-scale-of-sharing arguments in [[Allen2020-nj]]. Its publisher-level definition of fake news operationalizes the framework laid out in [[Lazer2018-mm]], while its congruence-over-veracity finding speaks to debates in [[Vosoughi2018-at]], [[Pennycook2021-jq]], and the motivated-reasoning account of [[Osmundsen2021-et]]. The emphasis on a distinct right-leaning media cluster connects to [[Benkler2018-lw]] and complicates the echo-chamber claims of [[Del-Vicario2016-uj]].
