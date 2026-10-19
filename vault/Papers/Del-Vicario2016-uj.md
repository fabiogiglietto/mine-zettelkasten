---
title: "The spreading of misinformation online"
aliases: ["The spreading of misinformation online"]
authors: ["Michela Del Vicario", "Alessandro Bessi", "Fabiana Zollo", "Fabio Petroni", "Antonio Scala", "Guido Caldarelli", "H. Eugene Stanley", "Walter Quattrociocchi"]
year: 2016
doi: 10.1073/pnas.1517441113
bibtex_key: Del-Vicario2016-uj
topics: [information-disorder-theory, political-polarization-partisanship]
citation_count: 1855
open_access: false
source_url: https://doi.org/10.1073/pnas.1517441113
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807331Z
---

# The spreading of misinformation online

> Vicario, M. D., Bessi, A., Zollo, F., Petroni, F., Scala, A., Caldarelli, G., Stanley, H. E., & Quattrociocchi, W. (2016). The spreading of misinformation online. *Proceedings of the National Academy of Sciences*, *113*, 554–559. https://doi.org/10.1073/pnas.1517441113
>
> [View paper](https://doi.org/10.1073/pnas.1517441113)

## Summary

This paper investigates how misinformation propagates on Facebook by contrasting the consumption and diffusion of two distinct content types: scientific news and conspiracy theories. Drawing on a large five-year dataset (2010–2014) of public Facebook pages, the authors show that users self-organize into homogeneous, polarized communities — echo chambers — driven by selective exposure and confirmation bias. Rather than treating misinformation as a matter of individual gullibility, the paper reframes it as a structural phenomenon of social homogeneity, and formalizes this insight in a data-driven percolation model demonstrating that homogeneity and polarization are the principal predictors of cascade size.

## Key Contributions

- Large-scale quantitative evidence that echo chambers form around distinct narratives (science vs. conspiracy) with characteristic cascade dynamics.
- Introduction of formal measures — user polarization (σ) and edge homogeneity (σ_ij) — to quantify the social determinants of diffusion.
- A data-driven percolation/branching model on signed small-world networks that predicts cascade size from homogeneity and polarization.
- Empirical linkage of confirmation bias and social homogeneity to misinformation spreading, casting doubt on purely algorithmic countermeasures such as trustworthiness scores.

## Methods

Public Facebook data were collected via the Graph API across 2010–2014, covering 67 pages (32 conspiracy, 35 science) plus 2 troll pages used to fit the model. The authors constructed "sharing trees" — oriented trees of successive shares — and characterized cascade size, height, and lifetime. User polarization was defined from the fraction of likes on conspiracy content, and edge homogeneity as the product of two users' polarizations. Statistical analysis included power-law fitting of cascade-size distributions, lifetime PDFs/CCDFs, and Kolmogorov–Smirnov tests. Finally, a branching/percolation model on a Watts–Strogatz signed network (n=5,000 nodes, m=1,000 items), parameterized by sharing threshold δ, fraction of homogeneous links ϕ_HL, and rewiring probability r, was validated against 1,072 troll-page sharing trees.

## Findings

- Cascade size and maximum degree are power-law distributed for all content types (exponents 2.21 science, 2.47 conspiracy, 2.44 trolling; max cascade sizes 952, 2,422, 3,945).
- Lifetime distributions are similar across categories, peaking around 1–2 h and ~20 h, with ~40% of content diffusing within 5 h.
- Science news reaches high diffusion quickly with no lifetime–size relation, whereas conspiracy rumors are assimilated more slowly and show a positive lifetime–size relation.
- Mean edge homogeneity is almost always ≥ 0: content circulates predominantly within homogeneous echo chambers, and near-zero homogeneity is improbable.
- Larger science cascades map to high homogeneity (0.5–0.8) and larger conspiracy cascades to lower homogeneity (~0.25), but homogeneity remains the underlying driver in both.
- The percolation model reproduces observed dynamics; ϕ_HL ~ 0.5–0.56 cleanly splits the network into two isolated echo chambers (best fit ϕ_HL=0.56, r=0.01, δ=0.015).

## Connections

This is a foundational empirical statement of the echo-chamber/confirmation-bias account of online misinformation, and it sits in productive tension with work challenging or complicating that view, such as [[Nyhan2023-gb]], [[Gonzalez-Bailon2023-uy]], and [[Bakshy2015-rn]] on exposure and algorithmic curation. It is a natural companion to [[Vosoughi2018-at]] on the diffusion dynamics of true versus false news and to [[Barbera2015-fw]] and [[Flaxman2016-lm]] on polarization and selective exposure; its skepticism toward algorithmic fixes anticipates the accuracy- and reasoning-focused interventions studied in [[Pennycook2021-jq]].
