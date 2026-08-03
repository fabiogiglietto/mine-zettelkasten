---
title: "Relying on the mainstream? Entity networks in alternative media"
aliases: ["Relying on the mainstream? Entity networks in alternative media"]
authors: ["Paul Balluff", "Hajo G. Boomgaarden", "Annie Waldherr"]
year: 2026
doi: 10.31235/osf.io/43nvp_v1
bibtex_key: Balluff2026-ev
topics: [platforms-audiences-and-online-communities, political-polarization-and-partisanship]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31235/osf.io/43nvp_v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Balluff2026-ev.mp3
pdf_available: true
discovery_date: 2026-07-28T12:22:03.904374Z
---

# Relying on the mainstream? Entity networks in alternative media

> Balluff, P., Boomgaarden, H. G., & Waldherr, A. (2026). Relying on the mainstream? Entity networks in alternative media. *SocArXiv*. https://doi.org/10.31235/osf.io/43nvp_v1
>
> [View paper](https://doi.org/10.31235/osf.io/43nvp_v1)

## Summary

This exploratory study interrogates a common assumption about alternative media: that they populate their coverage with a fundamentally different cast of actors than mainstream outlets. Analyzing German-language coverage of the Nord Stream 2 pipeline from 2011 to 2022 across 37 (mostly right-wing) alternative and 98 legacy outlets, the authors extract named entities and build co-occurrence networks to compare reporting patterns. Their central finding is counterintuitive: alternative and legacy media reference substantially overlapping sets of entities, at least on an internationally significant topic. The genuine differences lie not in *which* actors are named but in *how* those actors are relationally organized — alternative media weave entities into more cohesive, tightly-knit constellations and mention other media outlets far more frequently, reflecting their reactive, resource-constrained, and strategically self-positioning stance toward the mainstream.

## Key Contributions

- Delivers a large-scale, longitudinal, actor-centered and *relational* analysis of alternative vs. legacy media, moving beyond institutional-level comparisons.
- Empirically challenges the assumption that alternative media inherently reference different entities, documenting substantial overlap in entity choice for internationally salient topics.
- Introduces a novel application of structural topic modeling restricted to *media-named entities* to surface latent media-mentioning profiles.
- Combines state-of-the-art NLP (mLUKE NER, mGENRE entity linking) with network analysis and Bayesian mixed-effects modeling, and releases a public entity-linking validation set.

## Methods

- Corpus of 39,853 Nord Stream 2 articles (3,918 alternative; ~35,707 legacy) drawn from the Meteor database, LexisNexis, and the Tagesschau API, split into four time periods.
- Named entity recognition via a fine-tuned mLUKE multilingual transformer (German F1 = 0.85), yielding over 2.5 million entities (persons, organizations, locations).
- Entity linking/reconciliation to Wikidata using mGENRE (80.5% accuracy on a self-built validation set of 1,902 entities from netzpolitik.org).
- Diversity measured through entropy (Shannon's H), cosine-based disparity, and novelty (Z-scores à la Uzzi et al.).
- Weighted per-outlet, per-period co-occurrence networks (igraph), with metrics for communities, density, diameter, transitivity, modularity, and growth.
- A structural topic model over the media-entity document-term matrix (four topics; alternative-media and time-period covariates), plus a Bayesian generalized linear mixed model (Bernoulli/logit, random outlet intercepts) predicting media type.

## Findings

- Top-10 entities were largely shared across media types, with only minor divergences (e.g., Erdoğan and the AfD more prominent in alternative media).
- The Bayesian model found diameter and modularity credibly *negatively* associated with alternative media, while network growth, transitivity, and media-mention ratio were *positively* associated.
- Diversity measures (entropy, disparity, novelty) showed weak, uncertain associations — comparable actor breadth across media types.
- The STM distinguished referencing compositions: legacy media lean heavily on the German Press Agency, while alternative media mix major outlets (Der Spiegel, Die Welt) with international agencies like Reuters and TASS.
- These referencing patterns were stable across time, and alternative media engagement intensified in later periods, suggesting a reactive, opportunistic orientation as conflict lines aligned with ideological positions.

## Connections

This paper sits within the same research programme as other work by its authors on media ecosystems and computational content analysis, notably [[Balluff2026-if]] and [[Balluff2026-bv]]. Its methodological core — transformer-based entity recognition, linking, and network construction for comparative media analysis — connects it to the computational-methods and LLM-annotation strand of the register, though its substantive focus on alternative-versus-mainstream referencing behavior is largely distinct from the platform-diffusion papers in these topics.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Balluff2026-ev.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
