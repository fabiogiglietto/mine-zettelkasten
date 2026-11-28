---
title: "Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations"
aliases: ["Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations"]
authors: ["Laura Iannelli", "Fabio Giglietto", "Luca Rossi", "Elisabetta Zurovac"]
year: 2018
doi: 10.1177/0894439318816638
bibtex_key: Iannelli2018-ebd918b7
kind: own
topics: [survey-measurement-validity, digital-methods-computational-social-science]
citation_count: 85
open_access: true
source_url: https://doi.org/10.1177/0894439318816638
podcast_url: 
pdf_available: true
discovery_date: 
---

# Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations

> Iannelli, L., Giglietto, F., Rossi, L., & Zurovac, E. (2018). Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations. *Social Science Computer Review*. https://doi.org/10.1177/0894439318816638
>
> [View paper](https://doi.org/10.1177/0894439318816638)

## Summary

This methodological paper develops and tests a replicable procedure for recruiting online survey respondents from niche, hard-to-reach populations using Facebook's advertising platform. Using supporters of conspiracy theories in Italy as a test case, the authors demonstrate how recent Facebook marketing features—Pixel conversion tracking, URL parameter passing, and Pixel-based custom audience exclusion—can improve response-rate measurement and sample quality control. The procedure proved efficient (1,069 valid respondents at €0.46 each, 3.28% conversion rate), but its effectiveness at reaching ideologically distinctive respondents was inconclusive: the Facebook-recruited sample did not show significantly higher conspiracy endorsement than a general-population CAWI benchmark. The paper positions Facebook ad recruitment as a controllable, affordable alternative to panel-based CAWI, snowball sampling, and API-based app methods, particularly relevant amid tightening API access after Cambridge Analytica.

## Key Contributions

- A replicable, technically detailed protocol for Facebook ad-based survey recruitment leveraging Pixel conversion tracking, URL parameter passing, and custom audience exclusion.
- Proposes "conversion rate" (valid completions / reach) as a more precise response-rate metric than the click-through rates (CTRs) used in prior studies.
- Empirical efficiency benchmarks (cost per respondent, conversion rate, time cost) for future comparison.
- Extends Facebook ad-recruitment literature from health and political-affiliation targets to the domain of controversial, stigmatized belief (conspiracy theories).
- Practical guidance on ad design, image rotation, comment management, and incentive substitution (brevity in place of monetary reward).

## Methods

- Online non-probability quota survey of Italian adults, with age/gender quotas drawn from national statistics, targeted via Facebook ads to users tagged with interests "vaccines controversy" and "chemtrails conspiracy" (the more generic "moon landing" interest was excluded).
- 12 demographic micro-target audiences (6 age cohorts × 2 genders), each served 4 ad creatives on a fixed template emphasizing brevity and anonymity.
- Survey hosted on TypeForm PRO via a dedicated domain, launched from a purpose-built Facebook page; campaign optimized for conversions rather than clicks.
- Facebook Pixel installed on the thank-you page to track completions, auto-exclude completers from further ads, and build custom audiences; URL parameters carrying age/gender used to detect respondents arriving via social sharing.
- Data cleaning removed duplicate IPs (45) and parameter-less shared responses (26); post-stratification weighting matched national distributions.
- Agreement (0–10 Likert) with three conspiracy statements compared against the ITANES 2016 CAWI panel (n=3,027) using Kruskal–Wallis tests and effect size measures.

## Findings

- The 53-day campaign (Dec 2017–Jan 2018) generated 82,233 impressions, reached 32,613 unique users, and produced 1,140 conversions, 1,069 valid after cleaning.
- A 3.28% conversion rate outperformed nearly all CTRs reported in prior Facebook ad-based survey literature (0.04–4.07%).
- Total cost was €488, averaging €0.46 per valid respondent—far cheaper than typical panel recruitment.
- Conspiracy-belief distributions did not significantly differ between the Facebook sample and the ITANES general population; effect sizes were negligible (all ≤0.004).
- Some evidence of greater polarization: 68% of the Facebook sample endorsed no conspiracy theories versus 53% in ITANES, though data transformation complicates interpretation.
- Pixel and URL parameter implementation successfully excluded 45 duplicate-IP and 26 socially-shared completions, enabling cleaner sample boundaries.

## Connections

This paper is part of a lineage of work using Facebook's advertising and Pixel infrastructure for recruitment and audience measurement, closely related to [[Giglietto2022-b30e8b4e]] and [[Giglietto2019-e9be81c1]] by overlapping authors. Its debate over whether platform-elaborated attributes (likes, interests) validly proxy offline characteristics and opinions connects to foundational digital-trace validity work such as [[Barbera2015-fw]] and [[Bail2018-fk]]. More broadly it sits within the computational-social-science methodological literature exemplified by [[Freelon2018-ao]] on the implications of tightening post–Cambridge Analytica API access.
