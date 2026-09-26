---
title: "Asymmetric ideological segregation in exposure to political news on Facebook"
aliases: ["Asymmetric ideological segregation in exposure to political news on Facebook"]
authors: ["Sandra González-Bailón", "David Lazer", "Pablo Barberá", "Meiqing Zhang", "Hunt Allcott", "Taylor Brown", "Adriana Crespo-Tenorio", "Deen Freelon", "Matthew Gentzkow", "Andrew M. Guess", "Shanto Iyengar", "Young Mie Kim", "Neil Malhotra", "Devra Moehler", "Brendan Nyhan", "Jennifer Pan", "Carlos Velasco Rivera", "Jaime Settle", "Emily Thorson", "Rebekah Tromble", "Arjun Wilkins", "Magdalena Wojcieszak", "Chad Kiewiet de Jonge", "Annie Franco", "Winter Mason", "Natalie Jomini Stroud", "Joshua A. Tucker"]
year: 2023
doi: 10.1126/science.ade7138
bibtex_key: Gonzalez-Bailon2023-uy
topics: [political-polarization-partisanship, computational-political-media-influence]
citation_count: 257
open_access: false
source_url: https://doi.org/10.1126/science.ade7138
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807412Z
---

# Asymmetric ideological segregation in exposure to political news on Facebook

> González-Bailón, S., Lazer, D., Barberá, P., Zhang, M., Allcott, H., Brown, T., Crespo-Tenorio, A., Freelon, D., Gentzkow, M., Guess, A. M., Iyengar, S., Kim, Y. M., Malhotra, N., Moehler, D., Nyhan, B., Pan, J., Rivera, C. V., Settle, J., Thorson, E., Tromble, R., Wilkins, A., Wojcieszak, M., de Jonge, C. K., Franco, A., Mason, W., Stroud, N. J., & Tucker, J. A. (2023). Asymmetric ideological segregation in exposure to political news on Facebook. *Science*, *381*, 392–398. https://doi.org/10.1126/science.ade7138
>
> [View paper](https://doi.org/10.1126/science.ade7138)

## Summary

This paper offers a large-scale, platform-internal map of ideological segregation in political news exposure on Facebook during the 2020 US election period, using aggregated data from roughly 208 million US adult active users. Employing a "funnel of engagement" framework, the authors distinguish between the news users *could* have seen (inventory), what they *actually* saw after algorithmic curation (feed), and what they engaged with. They find that ideological segregation on Facebook is far higher than prior web-browsing studies suggested, that it increases as one moves down the funnel, and — most strikingly — that segregation is *asymmetric*: there exists a homogeneous conservative corner of the news ecosystem with no liberal equivalent, and that corner is where most fact-check-flagged misinformation circulates. The work engages critically with earlier findings of diverse online news diets and extends prior Facebook research by measuring segregation at the news-story (URL) level and disaggregating the roles of Pages, Groups, and friends.

## Key Contributions

- One of the first large-scale, platform-internal maps of potential, actual, and engaged exposure, overcoming reliance on external web-browsing panels.
- Introduces URL-level (news-story) measurement of segregation, showing domain-level aggregation substantially understates it.
- Documents the distinct amplifying role of Pages and Groups versus friend-posted content in driving segregation.
- Empirically demonstrates the asymmetric conservative concentration of both homogeneous audiences and misinformation.
- Establishes a reproducible industry–academic collaboration model with a registered preanalysis plan, offering a blueprint for platform data access under regimes like the EU Digital Services Act.

## Methods

The authors analyzed aggregated (not individual-level) exposure and engagement data for ~208 million US adult active Facebook users from September 2020 to February 2021, using Facebook's internal civic/news and ideology classifiers (users scored ≤0.35 as liberal, ≥0.65 as conservative). Political news URLs and domains were tracked through the funnel of engagement, and a segregation index adapted from residential-segregation research (following Gentzkow and Shapiro) plus favorability scores (−1 fully liberal to +1 fully conservative) were computed. Coexposure networks (nodes = domains/URLs, edges weighted by shared unique viewers) were analyzed with the Pons–Latapy walktrap community-detection method. Misinformation was classified via Meta's Third-Party Fact-Checking Program. Robustness checks compared on-platform behavior with off-platform web browsing for consented users and varied by content type, political interest, posting source, and ideology operationalization. Data were restricted for privacy to URLs shared more than 100 times (~35,000 domains, ~640,000 URLs).

## Findings

- Domain-level segregation for exposed audiences fluctuated around 0.35 — far above the 0.02–0.10 range of prior web-browsing studies; URL-level segregation was higher still, roughly 0.45–0.50.
- Segregation rose along the funnel: exposed exceeded potential, and engaged exceeded exposed, implicating both algorithmic and social amplification.
- Favorability distributions skewed right, with more content favored by very conservative audiences than very liberal ones.
- 71–76% of untrustworthy domains and 97% of false URLs had conservative-leaning audiences at every funnel stage.
- Misinformation shared by Pages and Groups reached audiences almost entirely on the right; Pages produced the most conservative audiences.
- On-platform segregation was about three times higher than a within-person web-tracking benchmark for the same consented users.
- Community detection recovered clear liberal and conservative clusters from behavior alone, with the conservative cluster departing further from cross-cutting exposure and seeing more unreliable content.
- High-interest users were roughly twice as segregated as low-interest users; the single most-viewed story was a false claim about Pennsylvania military ballots from a domain ranked only 51st by views.

## Connections

This paper directly extends and complicates [[Bakshy2015-rn]], whose analysis of friend-posted content it builds upon by disaggregating Pages and Groups as more powerful drivers of segregation. It sits within the same US 2020 Facebook and Instagram Election Study collaboration as [[Guess2023-ai]], [[Guess2023-ur]], [[Nyhan2023-gb]], and [[Allen2024-av]], and speaks to the misinformation-diffusion literature exemplified by [[Vosoughi2018-at]] and the asymmetric-polarization and network-propaganda framing of [[Benkler2018-lw]] and [[Iyengar2019-jj]]; it also connects to echo-chamber debates in [[Del-Vicario2016-uj]], [[Flaxman2016-lm]], and [[Barbera2015-fw]].
