---
title: "Visual identities in troll farms: The Twitter Moderation Research Consortium"
aliases: ["Visual identities in troll farms: The Twitter Moderation Research Consortium"]
authors: ["Marco Bastos"]
year: 2025
doi: 10.1177/20563051251323652
bibtex_key: Bastos2025-ol
topics: [platform-governance-data-access, computational-social-science-methods]
citation_count: 1
open_access: false
source_url: https://doi.org/10.1177/20563051251323652
podcast_url: 
pdf_available: true
discovery_date: 2025-01-15T00:00:00Z
---

# Visual identities in troll farms: The Twitter Moderation Research Consortium

> Bastos, M. (2025). Visual identities in troll farms: The Twitter Moderation Research Consortium. *Social Media + Society*, *11*, 20563051251323652. https://doi.org/10.1177/20563051251323652
>
> [View paper](https://doi.org/10.1177/20563051251323652)

## Summary

This paper presents a ten-year longitudinal audit of how documented changes to Facebook's News Feed ranking algorithm shaped engagement with news content from *The Guardian* between 2011 and 2020. By combining a hand-curated timeline of 52 algorithmic updates with roughly one million Guardian articles and matched CrowdTangle engagement data, Bastos shows that ranking interventions produce measurable, lagged effects on engagement — but only for hard news, not for Opinion, Lifestyle, Arts, or Sport. The argument is twofold: empirically, recommender systems are not inscrutable "black boxes" but auditable sociotechnical assemblages; politically, the EU Digital Services Act (especially Article 40(4)) provides the legal scaffolding to institutionalise such longitudinal independent audits.

(Note: the supplied title refers to troll farms and the Twitter Moderation Research Consortium, but the structured summary describes a different study on Facebook News Feed and *The Guardian*. The note below follows the structured summary.)

## Key Contributions

- First decade-long empirical model of Facebook News Feed ranking effects on news engagement, segmented by content type.
- A replicable methodological pipeline combining documented algorithm-change timelines with cross-correlation, Granger causality, and anomaly detection.
- Empirical evidence that platforms apply *differentiated* algorithmic treatment to hard versus soft news.
- Reframes recommender systems as auditable institutional artefacts rather than opaque black boxes.
- Policy argument for operationalising DSA Article 40(4) and Recital 85 to enable sustained independent algorithmic audits.

## Methods

- Compiled a timeline of 52 News Feed ranking updates (2011–2020), coded by impact level and valence toward trusted news.
- Harvested ~1,020,163 Guardian articles via the Guardian Open Platform API across five sections (News, Opinion, Sport, Arts, Lifestyle).
- Retrieved CrowdTangle engagement metrics (likes, shares, comments, Reactions) for 576,673 matched URLs.
- Log-transformed series and verified stationarity with Augmented Dickey–Fuller tests.
- Applied cross-correlation function (CCF) analysis to identify lags, then Granger causality tests at those lags, plus Seasonal Hybrid ESD anomaly detection. Daily aggregation yielded 20,075 observations; analyses in R.

## Findings

- Optimal lags between ranking changes and engagement effects were 19–24 days, consistent with phased platform roll-outs.
- News (ACF .35) and Sport (.31) showed the strongest cross-correlations; Opinion, Lifestyle, Arts were weaker (.27, .24, .25).
- Granger causality was significant *only* for the News section (F = 1.6774, p = .0327 at lag 19), isolating hard news as the category most shaped by ranking interventions.
- Anomaly clusters in 2014–2016, peaking mid-2016, align with the well-known pivot toward friends-and-family content.
- Sport anomalies in July 2014 reflect the FIFA World Cup, not algorithm changes — a useful negative control.
- Engagement rose steadily through 2016 then declined as major ranking updates rolled out.

## Connections

This paper sits squarely in the platform-governance and algorithmic-auditing strand of the register, complementing work on independent external observation of recommender systems and platform data access regimes — see [[Rieder2026-pp]], [[Rieder2025-ju]], and [[Ohme2026-nv]] on auditing and access infrastructures, and [[Helmond2026-ll]] on platforms as institutional/sociotechnical objects. Its longitudinal CrowdTangle-based design also resonates with methodological reflections on platform data in [[Bruns2025-fz]] and [[Bastos2025-ya]], while its concern with how algorithmic gatekeeping reshapes news distribution connects to [[Hurcombe2025-cs]] and [[Munger2025-cz]].
