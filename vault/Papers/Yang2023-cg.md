---
title: "Visual misinformation on Facebook"
aliases: ["Visual misinformation on Facebook"]
authors: ["Yunkang Yang", "Trevor Davis", "Matthew Hindman"]
year: 2023
doi: 10.1093/joc/jqac051
bibtex_key: Yang2023-cg
topics: [information-disorder-theory, electoral-social-media-research]
citation_count: 81
open_access: false
source_url: https://doi.org/10.1093/joc/jqac051
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807395Z
---

# Visual misinformation on Facebook

> Yang, Y., Davis, T., & Hindman, M. (2023). Visual misinformation on Facebook. *Journal of Communication*. https://doi.org/10.1093/joc/jqac051
>
> [View paper](https://doi.org/10.1093/joc/jqac051)

## Summary

This paper offers the first large-scale, platform-complete estimate of image-based political misinformation on Facebook, analyzing nearly 13.7 million image posts from over 14,500 pages and 11,400 public groups during the final three months of the 2020 U.S. election campaign. The authors argue that the dominant approach to measuring misinformation — counting links to noncredible domains — has systematically undercounted the problem by ignoring image posts, which are both the most common political post type (~40%) and outnumber link posts in absolute volume. Using perceptual hashing and computer vision combined with careful manual coding, they estimate that roughly 20–23% of sampled political images contain misinformation, with a stark partisan asymmetry favoring the right. Notably, they find little evidence that misleading images generate higher engagement once partisanship and audience size are controlled.

## Key Contributions

- First valid, platform-scale prevalence estimates of visual political misinformation on any social media platform.
- A scalable computational pipeline (perceptual hashing + facial recognition + computer vision) for studying visual political communication across millions of images.
- A direct challenge to the "misinformation is minimal/declining" consensus, attributing that conclusion to a methodological artifact of link-only measurement.
- Post-level (rather than publisher-domain-level) classification of misinformation, reducing measurement error.
- Documentation of strong partisan asymmetry and a weakening of the assumed misinformation–engagement link.

## Methods

The authors assembled a near platform-complete "megalist" of top U.S. political pages and groups via CrowdTangle and licensed vendors (no scraping). AWS Rekognition facial recognition built a top-100 political figures list and a sub-corpus of 572,857 figure-containing posts; perceptual hashing (pHash) identified duplicate and most-reposted images. Four samples were manually coded — an Overall Sample (1,000 random images), a Public Figures Sample (1,000), and the top 300 most-reposted images from groups and pages each — with misinformation defined by contemporaneous expert consensus informed by 255 fact-check articles. Reliability was strong (Krippendorff's α = 0.78 for misinformation). Analyses included power-law fitting to estimate coverage, difference-of-means tests, LOWESS, and negative binomial regression with partisanship and audience-size controls. A review of 135 communication journal articles (2017–2021) documented the field's neglect of images.

## Findings

- 20.1–25.1% of images in the Overall Sample contained misinformation; 17.5–21.6% in the Public Figures Sample.
- Sharp partisan asymmetry: 39% of right-leaning vs. 5% of left-leaning images misleading (Overall Sample); right-leaning images 5–8× more likely to mislead.
- Among top-reposted images, ~30% (groups) and ~26% (pages) were misleading, again concentrated on the right.
- Four common formats: altered images, misleading memes, unaltered images with false captions, and screenshots of misleading posts.
- Four recurring themes: Biden as senile, attacks on Hunter Biden, Democrats endorsing violence, and QAnon promotion.
- No significant misinformation–engagement relationship (near-zero T-statistics, p = .88/.92; no engagement boost in regressions with controls).
- The corpus captured ≥94% of page and ≥95% of group interactions; only 9 of 135 reviewed articles focused on images.

## Connections

This paper's core methodological critique — that link-based measurement understates misinformation — speaks directly to the literature it challenges, including the exposure- and engagement-focused studies [[Guess2023-ai]], [[Guess2019-ym]], [[Grinberg2019-ua]], [[Allen2020-nj]], and [[Gonzalez-Bailon2024-rq]], as well as the definitional and measurement debates in [[Lazer2018-mm]] and [[Tsfati2020-uo]]. Its findings on partisan asymmetry and the contested misinformation–engagement link connect to work on sharing dynamics and virality such as [[Vosoughi2018-at]] and [[Osmundsen2021-et]], while its focus on visual manipulation and evolving misinformation vectors resonates with newer platform-scale image and multimodal analyses like [[Achmann-Denkler2026-lx]] and [[Brady2026-ln]].
