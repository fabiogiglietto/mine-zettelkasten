---
title: "\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"
aliases: ["\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"]
authors: ["Fabio Giglietto"]
year: 2025
doi: 10.31235/osf.io/8dqag_v2
bibtex_key: Giglietto2025-1765bb4f
kind: own
topics: [platform-governance-data-access, italian-electoral-communication]
citation_count: 3
open_access: true
source_url: https://doi.org/10.31235/osf.io/8dqag_v2
podcast_url: 
pdf_available: true
discovery_date: 
---

# "A Pretty Blunt Approach": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility

> Giglietto, F. (2025). "A Pretty Blunt Approach": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility. *Center for Open Science*. https://doi.org/10.31235/osf.io/8dqag_v2
>
> [View paper](https://doi.org/10.31235/osf.io/8dqag_v2)

## Summary

This working paper provides the first independent empirical quantification of Meta's 2021–2025 political content reduction policy as it affected the Facebook visibility of Italian elected officials. Drawing on over 2.5 million posts collected via the Meta Content Library API, Giglietto documents a roughly 72% peak-to-trough decline in average per-post reach for re-elected MPs, and shows that the policy's effects in Italy emerged some ten months *before* Meta's announced global rollout — a discrepancy that exposes transparency deficits in Meta's DSA compliance reporting. The paper frames algorithmic visibility as democratic infrastructure and argues for a collaborative (rather than purely adversarial) model of platform governance research, while affirming the DSA-enabled Meta Content Library as meaningful transparency progress.

## Key Contributions

- First independent empirical quantification of Meta's political content reduction policy on elected officials in a European democracy.
- A discovery-validation breakpoint-detection methodology designed for platform policy changes with ambiguous implementation timelines.
- Documentation of asymmetric effects across mainstream and extremist actors, including a volume-compensation mechanism that undermines the policy's intended goals.
- Exposure of specific gaps between Meta's DSA transparency reporting and the observable impact of its ranking changes on democratic communication.
- A fully documented, reproducible R pipeline and public producer lists supporting cross-country replication via the Meta Content Library.
- A normative framework for collaborative platform governance research grounded in the realities of platform-mediated data access.

## Methods

Giglietto collected 2,529,933 Facebook posts from 901 accounts (Jan 2021–Nov 2025) through the Meta Content Library API within Meta's Secure Research Environment, using R. Accounts were grouped into four mutually exclusive sets: re-elected MPs (discovery sample), newly elected MPs, prominent non-parliamentary politicians, and extremist/alternative-media accounts (validation samples). "Views" served as the primary outcome, with group-specific power-law imputation for posts censored at the 100-view threshold and sensitivity analyses of imputation choices. A discovery-validation design combined Bai–Perron and PELT structural breakpoint detection on weekly aggregated metrics, with 30-day consensus clustering; the resulting four policy phases were tested with Kruskal–Wallis and Bonferroni-corrected Dunn's post-hoc comparisons. A robustness check compared per-post average reach against total weekly reach to account for posting-frequency differences.

## Findings

- Three cross-validated breakpoints were identified: T1 (Sept 19, 2021, implementation), T2 (Jan 1, 2023, post-election adjustment), and T3 (March 9, 2025, reversal).
- Re-elected MPs' mean weekly views per post fell from 53,368 to 26,079 (–51%) at T1, then to 14,869 (–43%) at T2, before partially recovering to 34,918 after T3 — about 65% of pre-policy levels.
- Peak-to-trough declines were 72.1% for re-elected MPs, 51.2% for new MPs, 57.3% for prominent politicians, and only 24.3% for extremists.
- The expected DOWN→DOWN→UP pattern validated across the three mainstream groups, but extremists showed DOWN→DOWN→DOWN in per-post reach, with no significant recovery after the reversal.
- Measured as *total* weekly reach, extremists grew continuously (+13.7% from Phase 0 to Phase 2), surpassing mainstream politicians in aggregate visibility, driven by a 61.5–140.5% increase in posting frequency.
- The implementation breakpoint preceded Meta's announced global rollout by ~303 days; the reversal breakpoint followed Meta's January 2025 announcement by ~61 days, consistent with a gradual rollout.

## Connections

This paper extends the author's broader research program on Italian electoral communication and platform data access, connecting naturally to related work such as [[Paci2025-ag]], [[Marino2024-2fbc690f]], and [[Iannelli2015-e0818c3e]], and to the methodological and governance strands in [[Giglietto2026-632ef967]], [[Giglietto2025-1e9a0917]], and [[Giglietto2026-855a54cb]]. Its focus on DSA-enabled infrastructure and the transparency obligations of very large platforms engages debates taken up in platform-governance work including [[Rieder2025-ju]], [[Rieder2020-sl35]], [[Gillespie2010-sla2]], and [[van-Dijck2018-up]], while its attention to algorithmic visibility as democratic infrastructure resonates with [[Pierri2026-ib]] and studies of platform-mediated political reach.
