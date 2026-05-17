---
title: "How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic"
aliases: ["How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic"]
authors: ["Silke Adam", "Tobias Rohrbach", "Franziska Keller", "Mykola Makhortykh", "Ernesto de León", "Chiara Valli", "Ani Baghumyan", "Maryna Sydorova"]
year: 2026
doi: 10.1093/joc/jqaf033
bibtex_key: Adam2026-tz
topics: [information-disorder]
citation_count: 4
open_access: false
source_url: https://doi.org/10.1093/joc/jqaf033
podcast_url: 
pdf_available: true
discovery_date: 2026-05-16T09:10:27.779284Z
---

# How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic

## Summary

This paper develops and tests a holistic model of how COVID-19 conspiracy beliefs formed at the pandemic's outset, arguing that belief formation reflects a "marriage" of media exposure and political predispositions. Leveraging a fortuitously timed two-wave panel (Germany and German-speaking Switzerland, March–May 2020) bracketed by passive web tracking, the authors classify actual browsing content with fine-tuned BERT models to distinguish conspiracy-supporting from conspiracy-opposing material across alternative, mainstream, and social media. They find both a direct *contagion* effect from conspiracy-supporting alternative media and a *mitigation* effect from conspiracy-opposing mainstream media, but show these are conditioned by populism and political mistrust, which drive selective engagement, selective avoidance, reinforcement, and—strikingly—a backfire effect when populists do encounter mainstream debunking.

## Key Contributions

- A behavioral, real-time test of conspiracy belief formation during a crisis onset, sidestepping retrospective self-report bias.
- An integrated model combining content-level exposure (source × stance) with panel measures of predispositions and beliefs.
- Empirical evidence that mainstream debunking works on average but can backfire among populists.
- Open methodological infrastructure: the WebTrack browser plugin and validated German-language BERT classifiers for conspiracy detection and stance.
- Anchors the populism–conspiracy nexus within Zaller-style information-plus-predispositions theorizing and motivated reasoning.

## Methods

Two-wave online panels in Germany (n=573) and German-speaking Switzerland (n=574) with quota sampling, bracketing a desktop web-tracking phase that captured 3.5M HTML documents via a custom browser plugin. Sentence-level conspiracy detection and stance classification used fine-tuned German BERT models (macro F1 = 0.94 for detection; 0.78–0.82 for stance), trained on 12,745 manually coded sentences (Krippendorff's α = .85/.80). URLs were matched to mainstream quality/tabloid, hyperpartisan alternative conspiracy (HAC), and social-media source lists. Surveys measured populism (Schulz et al.), political mistrust (ANES), and an 8-item COVID-19 conspiracy belief scale. Analysis used OLS regression and bootstrapped mediation (10,000 iterations) on pooled data.

## Findings

- 7.2% of visited documents on average contained conspiracy-related content (~113 documents per participant).
- Conspiracy-supporting content outweighed conspiracy-opposing content across *all* source types, including mainstream media.
- Exposure across alternative, mainstream, and social sources was positively correlated—few users were monogamous information consumers.
- Contagion: conspiracy-supporting alternative media exposure increased conspiracy beliefs (b=0.14, p<.001).
- Mitigation: conspiracy-opposing mainstream media exposure decreased beliefs (b=-0.05, p=.001).
- Populism (b=0.38) and political mistrust (b=0.20) directly predicted conspiracy beliefs.
- Populists selectively engaged with conspiracy-supporting alternative media (b=0.76) and selectively avoided conspiracy-opposing mainstream media (b=-0.91); mistrust effects were similar but weaker.
- Significant indirect *reinforcement* via alternative media, and an indirect *backfire* pathway: among populists, the limited mainstream debunking they did encounter *increased* rather than decreased conspiracy beliefs.
- About 25–30% of respondents saw at least some truth in COVID-19 conspiracies or were uncertain.

## Connections

This paper sits alongside other behaviorally grounded misinformation-exposure studies that use tracking or platform data rather than self-report — notably [[Gonzalez-Bailon2024-rq]], [[Budak2024-ef]], and [[DeVerna2025-dl]] — and complements debunking/inoculation work such as [[van-der-Linden2026-jt]] and [[Spampatti2026-kx]] by showing where corrective exposure succeeds and where it backfires. Its focus on the populism–conspiracy–alternative media nexus links it to [[Frischlich2025-vn]] and [[Humprecht2025-ml]], while its emphasis on predisposition-driven selective exposure resonates with [[Arceneaux2026-xk]] and [[Mosleh2024-op]].
