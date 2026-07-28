---
title: "Relying on the mainstream? Entity networks in alternative media"
aliases: ["Relying on the mainstream? Entity networks in alternative media"]
authors: ["Paul Balluff", "Hajo G. Boomgaarden", "Annie Waldherr"]
year: 2026
doi: 10.31235/osf.io/43nvp_v1
bibtex_key: Balluff2026-ev
topics: [news-diffusion-platform-algorithms, computational-methods-llm-annotation]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31235/osf.io/43nvp_v1
podcast_url: 
pdf_available: true
discovery_date: 2026-07-28T12:22:03.904374Z
---

# Relying on the mainstream? Entity networks in alternative media

> Balluff, P., Boomgaarden, H. G., & Waldherr, A. (2026). Relying on the mainstream? Entity networks in alternative media. *SocArXiv*. https://doi.org/10.31235/osf.io/43nvp_v1
>
> [View paper](https://doi.org/10.31235/osf.io/43nvp_v1)

## Summary

This exploratory study interrogates a common assumption about alternative media: that they inhabit a separate informational universe, referencing different actors and facts than the mainstream press. Analyzing German coverage of the Nord Stream 2 pipeline from 2011 to 2022 across 37 (mostly right-wing) alternative outlets and 98 legacy outlets, the authors extract named entities and build co-occurrence networks to compare reporting patterns. Their central finding overturns the divergence assumption — for an internationally significant topic, alternative and legacy media reference substantially the *same* entities. The difference lies not in *which* actors are mentioned but in *how* they are relationally organized: alternative media weave entities into tighter, more cohesive constellations and reference other media outlets far more frequently, reflecting resource constraints, reactive reporting, and strategic positioning against the mainstream.

## Key Contributions

- Delivers a large-scale, longitudinal, actor-centered and *relational* analysis of alternative vs. legacy media, moving beyond institutional-level framings.
- Challenges the premise that alternative media inherently cite different entities, showing broad overlap in entity choice for globally salient topics.
- Introduces a novel application of structural topic modeling built exclusively from *media-named entities* to surface latent media-mentioning profiles.
- Combines state-of-the-art multilingual NLP (mLUKE NER, mGENRE entity linking) with network analysis and Bayesian mixed-effects modeling, and releases a public entity-linking validation set.

## Methods

The corpus comprises 39,853 Nord Stream 2 articles (3,918 alternative, ~35,707 legacy) drawn from the Meteor database, LexisNexis, and the Tagesschau API, split into four time periods. A fine-tuned mLUKE transformer performed named entity recognition (F1 = 0.85 for German), extracting over 2.5 million person, organization, and location entities, which were reconciled against Wikidata via the mGENRE sequence-to-sequence model (80.5% accuracy). The authors measured diversity through entropy, disparity, and novelty (Z-scores), constructed weighted per-outlet co-occurrence networks in igraph (computing transitivity, modularity, density, diameter, growth), fitted a structural topic model over a media-entity document-term matrix with alternative-media and time-period covariates, and ran a Bayesian GLMM (Bernoulli/logit) with random outlet intercepts to identify structural predictors distinguishing the two media types.

## Findings

- The top 10 named entities were largely shared across media types, with only minor differences (Erdoğan and the AfD somewhat more prominent in alternative media).
- The Bayesian model credibly linked alternative media to lower diameter and modularity, and to higher network growth, transitivity, and media-mention ratio — indicating cohesive, tightly-knit rather than fragmented, modular structures.
- Diversity measures (entropy, disparity, novelty) showed weak, uncertain associations, implying comparable breadth of referenced actors.
- The STM revealed distinct media-mentioning profiles: legacy outlets lean heavily on the German Press Agency, while alternative outlets cite a mix of major papers (Der Spiegel, Die Welt) and international agencies (Reuters, TASS).
- These referencing patterns were stable across time periods, reinforcing the robustness of the observed cross-media differences.

## Connections

This paper sits alongside the authors' other computational work on media entity networks and annotation methodology, notably [[Balluff2026-if]] and [[Balluff2026-bv]], sharing an entity-centered, relational approach to comparative media analysis. Its reliance on transformer-based NER and LLM-driven reconciliation places it in dialogue with the broader computational annotation strand represented by [[Gilardi2026-hw]] and [[Le-Mens2025-qz]]. The focus on how alternative and right-wing outlets position themselves relative to the mainstream also resonates with work on alternative and fringe information ecosystems such as [[Kalsnes2025-zb]] and [[Nenno2025-xa]].
