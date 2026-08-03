---
title: "\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"
aliases: ["\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"]
authors: ["Fabio Giglietto"]
year: 2025
doi: 10.31235/osf.io/8dqag_v2
bibtex_key: Giglietto2025-1765bb4f
kind: own
topics: [platform-governance-and-content-moderation, italian-electoral-media-coverage]
citation_count: 2
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

This working paper offers the first independent empirical quantification of Meta's 2021–2025 political content reduction policy in a European democracy, focusing on Italian parliamentarians and other political accounts on Facebook. Drawing on 2.5 million posts collected via the Meta Content Library, the study uses structural breakpoint detection to show that the policy suppressed re-elected MPs' per-post reach by 72% at trough, took effect in Italy roughly ten months before Meta's announced global rollout, and only partially recovered following Meta's January 2025 reversal. Crucially, extremist accounts absorbed the per-post penalty by dramatically increasing posting volume, ultimately surpassing mainstream politicians in aggregate weekly reach — a finding that reframes the policy as producing asymmetric, and arguably counterproductive, distributional effects on democratic communication.

## Key Contributions

- First independent empirical measurement of Meta's political content demotion on elected officials outside the US context.
- A discovery-validation breakpoint-detection design that identifies platform policy shifts without relying on Meta's own timelines.
- Documentation of an asymmetric volume-compensation mechanism through which extremist actors neutralize demotion.
- Evidence of a specific gap between Meta's DSA transparency reporting and empirically observable ranking changes.
- A fully reproducible R pipeline and public producer lists to enable cross-country replication via the Meta Content Library.
- A normative argument for collaborative (rather than adversarial) platform governance research grounded in DSA-era access infrastructures.

## Methods

The author collected 2,529,933 posts from 901 Italian accounts (Jan 2021–Nov 2025) via the Meta Content Library API inside Meta's Secure Research Environment. Accounts were partitioned into four mutually exclusive groups — re-elected MPs (discovery), new MPs, prominent non-parliamentary politicians, and extremist/alternative-media accounts (validation). Views censored at the 100-view threshold were imputed via group-specific power-law fitting. Weekly aggregates of views, reactions, shares, and comments were analyzed with Bai–Perron and PELT breakpoint detection, followed by 30-day consensus clustering to identify three validated breakpoints. Kruskal–Wallis and Dunn's tests (Bonferroni-corrected) compared the resulting phases, and a robustness check contrasted per-post average reach with total weekly reach.

## Findings

- Three cross-validated breakpoints: implementation (Sept 19, 2021), post-election adjustment (Jan 1, 2023), and reversal (March 9, 2025).
- Re-elected MPs' weekly views per post fell from 53,368 → 26,079 → 14,869, before rebounding to 34,918 — a 72.1% peak-to-trough drop with only ~65% recovery.
- Peak-to-trough declines: 72.1% (re-elected MPs), 57.3% (prominent politicians), 51.2% (new MPs), 24.3% (extremists).
- The expected DOWN→DOWN→UP pattern held for mainstream groups but not extremists, who showed no significant per-post recovery after the reversal.
- In *total* weekly reach, extremists grew +13.7% across the policy period, driven by a 61.5–140.5% increase in posting frequency, overtaking mainstream politicians in aggregate visibility.
- The Italian implementation breakpoint preceded Meta's announced global rollout by ~303 days; the reversal breakpoint followed Meta's January 2025 announcement by ~61 days.

## Connections

This paper extends the author's ongoing program on Italian political communication and platform-mediated visibility ([[Giglietto2026-632ef967]], [[Giglietto2025-1e9a0917]], [[Giglietto2024-cbeb3f70]], [[Giglietto2023-fa71a001]], [[Giglietto2026-855a54cb]]) and speaks directly to research on Meta's political content policy and platform ranking transparency ([[Bouchaud2026-lr]], [[Bouchaud2026-np]], [[Rieder2026-pp]], [[Rieder2025-ju]]). It also connects to the broader literatures on DSA-era data access and platform governance ([[Katzenbach2026-sl2e]], [[Bechmann2026-dr]], [[Helmond2026-ll]]) and to work on algorithmic curation as democratic infrastructure ([[Gillespie2010-sla2]], [[Gonzalez-Bailon2024-rq]], [[Bakshy2015-rn]]).
