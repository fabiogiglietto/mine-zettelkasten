---
title: "Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations"
aliases: ["Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations"]
authors: ["Laura Iannelli", "Fabio Giglietto", "Luca Rossi", "Elisabetta Zurovac"]
year: 2018
doi: 10.1177/0894439318816638
bibtex_key: Iannelli2018-ebd918b7
kind: own
topics: [computational-methods-llms-social-media, platforms-audiences-and-online-communities]
citation_count: 88
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

This paper develops and tests a Facebook ad-based recruitment protocol for online surveys targeting niche, hard-to-reach populations, using Italian supporters of vaccine and chemtrail conspiracy theories as a test case. The authors argue that recent Facebook marketing features — Pixel conversion tracking, URL parameter passing, and Pixel-based custom audience exclusion — allow researchers to measure response rates and control sample quality more rigorously than earlier click-through-rate–based approaches. They demonstrate the procedure is highly efficient (low cost, fast recruitment, good conversion rates) but find its *effectiveness* — reaching ideologically distinctive respondents via Facebook interest targeting — to be inconclusive when benchmarked against a general-population CAWI sample.

## Key Contributions

- A replicable, technically detailed protocol for Facebook ad–based survey recruitment integrating Pixel conversion tracking, URL parameters, and custom audience exclusion.
- Proposal of a "conversion rate" (valid completions / reach) as a more precise response-rate metric than CTR for platform-recruited surveys.
- Empirical efficiency benchmarks (€0.46/respondent, 3.28% conversion, 53 days) usable as comparators for future ad-based studies.
- Extension of Facebook ad–recruitment methodology from health and political domains to controversial belief/opinion targeting.
- Practical design guidance on ad creatives, image rotation, comment moderation, and brevity as an incentive substitute.

## Methods

Non-probability quota survey of Italian adults recruited via Facebook ads targeting the interests "vaccines controversy" and "chemtrails conspiracy," split across 12 age×gender micro-segments each receiving 4 ad creatives. The survey was hosted on TypeForm PRO via a dedicated domain, with a Facebook Pixel on the thank-you page enabling conversion tracking, automatic exclusion of completers, and custom audience construction. URL parameters carried demographic tags to detect socially shared submissions. After cleaning (removing 45 duplicate-IP and 26 shared-link responses) and post-stratification weighting, the sample was compared to the ITANES 2016 CAWI benchmark (n=3,027) on three conspiracy statements using Kruskal–Wallis tests and effect-size measures in R.

## Findings

- 53-day campaign yielded 82,233 impressions, 32,613 unique users reached, and 1,069 valid respondents.
- Conversion rate of 3.28% outperformed nearly all CTRs reported in prior Facebook ad-based survey literature.
- Total campaign cost €488, or €0.46 per valid respondent — substantially cheaper than typical panel recruitment.
- Kruskal–Wallis tests found no significant differences in conspiracy endorsement between the Facebook and ITANES samples; effect sizes were negligible.
- Some polarization signal: 68% of Facebook respondents endorsed no conspiracy vs. 53% in ITANES, though comparability transformations complicate interpretation.
- Pixel + URL parameter tracking successfully identified and excluded duplicate and socially-shared completions.

## Connections

This paper fits within the methodological strand of social-media–based research infrastructure and sampling, and connects to broader concerns about platform access and measurement validity that intensified after API restrictions — themes shared with work on alternative data collection tooling like [[Ohme2026-nv]] and infrastructural critiques such as [[Rieder2025-ju]] and [[Freelon2024-sc]]. Its concern with validating whether platform-inferred interests reflect substantive offline attributes resonates with audit-style studies of platform categorization, though most other papers in this topic cluster address content-side analytics rather than survey recruitment, so the direct methodological overlap is limited.
