---
title: "A systematic review of social science studies analyzing social media data, 2010-2024"
aliases: ["A systematic review of social science studies analyzing social media data, 2010-2024"]
authors: ["Kai-Cheng Yang", "Pranav Goel", "Meredith L. Pruden", "Qunfang Wu", "Colby Eagan", "David Lazer", "Deen Freelon"]
year: 2026
doi: 10.31235/osf.io/yexp6_v1
bibtex_key: Yang2026-tq
topics: [platform-governance-and-data-access, computational-social-science-methods]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31235/osf.io/yexp6_v1
podcast_url: 
pdf_available: true
discovery_date: 2026-05-09T17:26:23.924172Z
---

# A systematic review of social science studies analyzing social media data, 2010-2024

## Summary

This systematic review maps fifteen years (2010–2024) of empirical social media research across 59 journals in five social science disciplines plus interdisciplinary venues. Using a human-in-the-loop LLM annotation pipeline applied to ~860,000 publications, the authors estimate that 0.78% of papers (3.15% in social science journals proper) draw on social media data, with research overwhelmingly concentrated on Twitter/X and Facebook. The central argument is twofold: the field grew rapidly through the early 2020s but has plateaued and begun declining since 2022, coinciding directly with platform API restrictions; and the platforms most studied bear little resemblance to those most used by the public, raising urgent questions about what social knowledge is being produced — and foreclosed — by data access regimes.

## Key Contributions

- First multi-platform, multi-disciplinary baseline of empirical social media research spanning 15 years and 59 journals, moving beyond Twitter-centric prior reviews.
- A validated, reproducible human-in-the-loop LLM annotation pipeline (with released codebook, prompts, and code) for large-scale meta-scientific analysis.
- Empirical demonstration that Web of Science substantially under-reports relevant papers, motivating a journal-website search alternative.
- Quantitative documentation of the publishing impact of API closures and emerging shifts toward YouTube, TikTok, and user-donated/archived data.
- A topical map identifying which substantive research areas (COVID-19, social movements, political communication, misinformation) are most exposed to platform data restrictions.
- Concrete calls for journal-level metadata standardization to support future meta-science.

## Methods

The authors searched 59 top-ranked journals (Google Scholar h5-index + Web of Science) for mentions of eight platforms across 2010–2024, yielding 27,951 candidate papers. A stratified sample of 5,218 papers was annotated in two stages — identifying empirical papers and identifying which platforms provided data — using six human coders to develop codebooks with Krippendorff's α reliability checks. Three LLMs were evaluated against human ground truth; o4-mini (100% accuracy on empirical identification, ≥91% on platforms) was applied to the full sample, and counts were scaled to the matched corpus using journal-year sampling ratios. Topical structure was recovered via an ensemble Louvain community detection (1,000 runs) over an author-keyword co-occurrence network from Scopus.

## Findings

- Empirical social media research is 0.78% of all papers (3.15% in social science journals); disciplinary prevalence ranges from <0.7% in Economics to 12.86% in Communication.
- Twitter/X (50.86%) and Facebook (36.28%) dominate; YouTube (17.11%) and Reddit (5.66%) follow; TikTok, Instagram, and LinkedIn remain small.
- Platform usage in research is sharply misaligned with public adoption — Twitter/X is overrepresented (21% of Americans use it) and YouTube underrepresented (84% of Americans).
- 82.59% of papers use only a single platform; multi-platform research remains rare.
- The share of social media papers rose ~235% in social science disciplines from 2010 to the early 2020s, then plateaued and declined in 2022–2024, driven by drops in Twitter/X and Facebook studies after API closures.
- TikTok and YouTube show recent upward trajectories, suggesting partial substitution.
- COVID-19 is the dominant topic (>60% of Economics papers using social media data); other concentrations include social movements, political communication, journalism, body image (Psychology), and disinformation. Communication has the most balanced topic distribution (Gini 0.38); Economics the most concentrated (0.72).

## Connections

This paper provides the quantitative backbone for the broader "post-API age" conversation animated by [[Freelon2024-sc]] and developed in work on data access regimes such as [[Rieder2025-ju]], [[Rieder2026-pp]], and [[Ohme2026-nv]]. It extends and broadens earlier Twitter-focused meta-reviews — most directly [[Murtfeldt2025-wu]] — and complements emerging alternatives the authors flag, including user-donated data approaches ([[Ohme2026-nv]]) and shifts toward TikTok, YouTube, and Instagram studied in [[Achmann-Denkler2026-lx]], [[Bouchaud2026-lr]], and [[Pierri2025-hm]]. It also speaks to methodological infrastructure work like [[Helmond2026-ll]] and [[Ventura2026-yc]] on what becomes knowable when platform data access is reconfigured.
