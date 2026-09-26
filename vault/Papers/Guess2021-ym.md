---
title: "Cracking open the news feed"
aliases: ["Cracking open the news feed"]
authors: ["Andy Guess", "Kevin Aslett", "Joshua Tucker", "Richard Bonneau", "Jonathan Nagler"]
year: 2021
doi: 10.51685/jqd.2021.006
bibtex_key: Guess2021-ym
topics: [political-polarization-partisanship, platform-data-governance]
citation_count: 41
open_access: false
source_url: https://doi.org/10.51685/jqd.2021.006
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807377Z
---

# Cracking open the news feed

> Guess, A., Aslett, K., Tucker, J., Bonneau, R., & Nagler, J. (2021). Cracking open the news feed. *Journal of Quantitative Description: Digital Media*, *1*. https://doi.org/10.51685/jqd.2021.006
>
> [View paper](https://doi.org/10.51685/jqd.2021.006)

## Summary

This paper leverages the Social Science One "Condor" dataset—a differentially-private, URL-level record of Facebook engagement covering millions of publicly shared links—to build a descriptive foundation for understanding how U.S. users encounter, view, and share news. The authors classify news into credible versus low-credibility (via NewsGuard), political versus non-political, and clickbait versus non-clickbait categories, then disaggregate viewing and sharing behavior across age and ideological groups. Their central argument is that while low-credibility news is relatively rare compared to credible news, it circulates disproportionately among older and very conservative users, with clear signatures of preference for ideologically congenial misinformation. Methodologically, the paper serves as a proof of concept for combining platform-scale data with supervised classifiers and bias-correction techniques to detect subtle tail-end behaviors invisible in conventionally sized samples.

## Key Contributions

- First analysis of large-scale, differentially-private Facebook engagement data that measures **both views (exposure) and shares**, allowing viewing to be distinguished from sharing behavior.
- Fine-grained descriptive evidence disaggregating news into credible/low-credibility, political, and clickbait categories across age and ideology.
- A methodological demonstration of combining platform-scale URL data with supervised ML classifiers and Hopkins–King misclassification bias correction.
- An empirical foundation for future misinformation research and policy debate, deliberately descriptive rather than causal.

## Methods

The analysis draws on the Condor dataset of URLs shared publicly on Facebook more than 100 times (Jan 2017–July 2019), aggregated by URL-year-month-age-gender-political-page-affinity with Gaussian differential-privacy noise. The authors focus on 466,591 URLs first posted in 2018 by U.S. users, restricted to NewsGuard-rated domains (score ≥60 = credible). Three binary URL-level measures were constructed: credible vs. low-credibility (NewsGuard), political vs. non-political (a supervised random forest trained on 8,552 labeled headlines/blurbs, ~90% accuracy, F1=0.90), and clickbait vs. non-clickbait (a pre-trained SVM). Classifier misclassification was corrected using the Hopkins and King method with bootstrap resampling (100 samples per URL) to yield corrected proportions and confidence intervals. Ideological slant was estimated from media partisanship scores for credible sources and manual coding for low-quality sources; user ideology came from Facebook's five-point political page-affinity score. A revised version corrects for Facebook's inadvertent exclusion of users lacking page-affinity scores, without changing the identified patterns.

## Findings

- Credible domains dominated: ~84% of news shares and ~89% of news views were credible; ~15% of both shares and exposures were low-quality (about one in eight views of at least moderately popular news articles).
- **Ideological gradient**: 27% of URLs shared by very conservative users were low-quality vs. 9% for very liberal; for views, 19% (very conservative) vs. 7% (very liberal).
- **Age gradient**: 20% of URLs shared by users 65+ were low-quality vs. 11% for the 24–35 bracket; the age effect is strongest within the two most conservative groups.
- Older users do not view much more low-credibility news in absolute counts, but it forms a higher share of their diet (18% oldest vs. 8% second-youngest), implying sharing differences are not merely a feed-exposure artifact.
- Low-quality domains were more likely political (53.4% vs. 31.3% credible) and more likely both political and clickbait (12.3% vs. 6.3%).
- No support that older users share more clickbait (26% for 25–34 vs. 24% for 65+), but strong support that older users share far more political news (22% vs. 56%).
- Of ~280 billion URL views by U.S. users in 2018, 44.5% were news; of ~2.1 billion shares, 48.2% were news.

## Connections

This paper is a direct descendant of the exposure-versus-sharing tradition of large-scale platform studies exemplified by [[Bakshy2015-rn]], and its use of Condor/Social Science One data situates it alongside the wave of Facebook internal-data analyses such as [[Gonzalez-Bailon2023-uy]] and [[Nyhan2023-gb]]. Its focus on the relative rarity of misinformation exposure echoes [[Allen2021-ai]] and the broader fake-news diffusion literature including [[Vosoughi2018-at]] and [[Allcott2019-gn]], while its findings on ideologically congenial sharing and audience partisanship connect to [[Barbera2015-fw]], [[Osmundsen2021-et]], and [[Iyengar2019-jj]].
