---
title: "Cross-national information attacks: A two-decade analysis of troll behavior in Korea"
aliases: ["Cross-national information attacks: A two-decade analysis of troll behavior in Korea"]
authors: ["Jaehong Kim", "Hyeonseung Kim", "Jiseon Kim", "Alice Oh", "Thorsten Holz", "Wonjae Lee", "Meeyoung Cha"]
year: 2026
doi: 
bibtex_key: Kim2026-br
topics: [coordinated-inauthentic-behavior, computational-methods-llms]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2606.22785v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kim2026-br.mp3
pdf_available: true
discovery_date: 2026-06-29T10:02:55.810731Z
---

# Cross-national information attacks: A two-decade analysis of troll behavior in Korea

> Kim, J., Kim, H., Kim, J., Oh, A., Holz, T., Lee, W., & Cha, M. (2026). Cross-national information attacks: A two-decade analysis of troll behavior in Korea. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2606.22785v1)

## Summary

This paper introduces an explainable, theory-grounded pipeline for detecting suspected state-linked troll activity in South Korean online news comments, applied to nearly two decades of Naver News data (2006–2025, 112M comments). Seeded from 70 publicly identified troll accounts and grounded in cognitive-warfare and moral-emotion theory, the authors build a hierarchical classifier that labels comments by foreign-state suspicion, moral-emotional valence, and target country, then aggregates content and behavioral signals to identify ~24,000 suspected troll accounts. The central empirical claim is that suspected trolls succeed less through overt foreign-aligned praise than through morally condemning rhetoric — especially "Condemning Korea" — which gains disproportionate engagement and visibility, particularly when targeting domestic political figures across the ideological spectrum.

## Key Contributions

- A 112M-comment, ~20-year Naver News dataset linked to verified troll seeds, released with privacy safeguards.
- A hierarchical, theory-grounded detector producing both class labels and span-level rationales, distilled into a lightweight (~0.1B parameter) Korean PLM (KcELECTRA) for scalable inference.
- Longitudinal evidence on the dominance of moral-condemnation rhetoric and election-timed influxes of new troll accounts.
- Concrete implications for auditable platform moderation, including prioritizing high-visibility condemnation patterns during politically sensitive windows.

## Methods

The authors assemble a candidate pool via the follow network and article co-commenting of 70 known trolls, then design a three-level labeling scheme (foreign-state origin → other-condemning/praising moral emotion → target country). They annotate 1,452 gold comments with class labels and span rationales (high Krippendorff's α), fine-tune GPT-4.1 on these, label 50K candidates, and distill the labels into KcELECTRA. User-level classification combines 14 content features and 10 behavioral features in an XGBoost model (F1 = 0.94 in 10-fold CV), with SHAP for interpretability. Strategy analysis uses time-series correlations, Welch's t-tests, Kruskal-Wallis, and fractional logit regression of like ratios on rhetorical intensity with time fixed effects.

## Findings

- 23,998 suspected troll accounts (0.59% of users) were identified; their activity correlates more strongly with known trolls (daily r=0.81) than non-troll baselines.
- Detected trolls produce far higher rates of troll-aligned content (67% vs. 22%) and use Major Neighboring State language more often and more diversely.
- "Condemning Korea" is the only rhetorical strategy with mean like ratio above 0.5; fractional logit shows its intensity positively predicts engagement (β=0.11), whereas "Condemning Rival" (β=−0.51) and "Praising MNS" (β=−1.09) suppress it.
- New troll-like account influx rises 51% during election windows, and troll density among new users increases near elections.
- "Condemning Korea" dominates output across the two decades, peaking in 2018 around the THAAD dispute, and targets political leaders across both liberal and conservative camps.

## Connections

This work extends scalable troll-detection efforts beyond English-language and U.S.-centric platforms, complementing methodologically related coordinated-behavior detection in [[Minici2024-tf]], [[Luceri2025-tr]], and [[Tan2024-vl]]. Its focus on long-horizon, election-sensitive influence activity resonates with prior longitudinal IO analyses such as [[Kuznetsova2025-nu]] and engagement-driven amplification dynamics studied in [[DeVerna2025-dl]]. The use of distilled LLM annotations with span-level rationales for auditable moderation also speaks to explainability-oriented work in [[Gerard2025-br]] and [[Yang2025-iv]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kim2026-br.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
