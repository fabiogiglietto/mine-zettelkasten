---
title: "Less than you think: Prevalence and predictors of fake news dissemination on Facebook"
aliases: ["Less than you think: Prevalence and predictors of fake news dissemination on Facebook"]
authors: ["Andrew Guess", "Jonathan Nagler", "Joshua Tucker"]
year: 2019
doi: 10.1126/sciadv.aau4586
bibtex_key: Guess2019-ym
topics: [electoral-social-media-research, information-disorder-theory]
citation_count: 1140
open_access: false
source_url: https://doi.org/10.1126/sciadv.aau4586
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807346Z
---

# Less than you think: Prevalence and predictors of fake news dissemination on Facebook

> Guess, A., Nagler, J., & Tucker, J. (2019). Less than you think: Prevalence and predictors of fake news dissemination on Facebook. *Science Advances*, *5*, eaau4586. https://doi.org/10.1126/sciadv.aau4586
>
> [View paper](https://doi.org/10.1126/sciadv.aau4586)

## Summary

This paper offers one of the first behavioral portraits of who actually shared fake news on Facebook during the 2016 U.S. presidential campaign, moving beyond self-report by linking an original three-wave panel survey to respondents' actual profile-sharing data. The central argument is corrective and empirical: sharing articles from fake news domains was a rare activity — over 90% of respondents shared none — but the behavior was concentrated among identifiable groups. Conservatives (consistent with the pro-Trump slant of 2016 fake news) and, most robustly, older Americans over 65 were disproportionately likely to share such content. The age effect survives controls for ideology, partisanship, education, and overall posting volume, making it the paper's headline finding and prompting the authors to argue that demographics like age deserve central rather than incidental explanatory status.

## Key Contributions

- Delivers an individual-level behavioral (not self-reported) account of fake news sharing using linked survey and Facebook trace data.
- Documents empirically that fake news sharing was rare, tempering alarmist post-election narratives.
- Identifies the over-65 cohort as a robust, independent predictor of misinformation sharing, distinct from political predispositions.
- Provides a methodological template for linking survey responses to platform behavioral data, validated through sample-comparison and robustness analyses.
- Opens research directions connecting digital literacy, cognitive aging, and news-feed exposure.

## Methods

The authors fielded a three-wave YouGov online panel (wave 1 N=3500) with sample-matching weights, then linked respondents to their private Facebook profile data (timeline posts, external links, page likes) via a consented web app, successfully matching 1191 respondents (~44% of Facebook users in the sample). Domains of shared external links were cross-referenced against curated fake news lists — primarily Craig Silverman's BuzzFeed list, reduced to 21 mostly pro-Trump domains using the Bakshy et al. supervised classifier, with the Allcott and Gentzkow list and three supplementary lists as robustness. Shares were aggregated to individual-level counts and modeled with Poisson/quasi-Poisson regression (negative binomial and OLS as checks), including sociodemographic and political predictors plus total sharing volume. Extensive robustness tests appear in Supplementary Materials (tables S1–S14).

## Findings

- 91.5% of respondents shared zero fake news articles; only 8.5% shared at least one.
- Low sharing is not an artifact of inactivity: only 3.4% shared ≤10 total links, while 61.3% shared 100–1000.
- 18.1% of Republicans versus 3.5% of Democrats shared at least one fake news article; independents resembled Republicans.
- Very conservative respondents shared the most (~1.0 articles on average); conservatives ~0.75.
- Users over 65 shared ~0.75 articles on average — more than twice the next-oldest group — and in multivariate models nearly seven times as many as the youngest (18–29) cohort.
- The age effect is significant (over-65 coefficient P<0.01) and robust across measures and controls.
- No other demographic (sex, race, education, income) shows a consistent robust effect, and heavy overall sharers are not the fake news sharers.
- Applying the same model to hard news yields varied predictors that notably exclude age.

## Connections

This is a foundational entry in the empirical fake news literature and pairs closely with companion work on the low prevalence and skewed distribution of misinformation exposure and sharing, such as [[Guess2023-ai]], [[Guess2023-ur]], [[Eady2023-xg]], [[Yang2023-cg]], [[Allen2020-nj]], [[Grinberg2019-ua]], and the agenda-setting overviews in [[Lazer2018-mm]] and [[Allcott2017-yz]]. Its emphasis on age and the psychology of misinformation dissemination connects to research on why people fall for and spread falsehoods, including [[Pennycook2021-jq]], [[Vosoughi2018-at]], [[Osmundsen2021-et]], and [[Tsfati2020-uo]].
