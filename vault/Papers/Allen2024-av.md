---
title: "Quantifying the impact of misinformation and vaccine-skeptical content on Facebook"
aliases: ["Quantifying the impact of misinformation and vaccine-skeptical content on Facebook"]
authors: ["Jennifer Allen", "Duncan J. Watts", "David G. Rand"]
year: 2024
doi: 10.1126/science.adk3451
bibtex_key: Allen2024-av
topics: [health-misinformation-networks, computational-political-media-influence]
citation_count: 130
open_access: false
source_url: https://doi.org/10.1126/science.adk3451
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807431Z
---

# Quantifying the impact of misinformation and vaccine-skeptical content on Facebook

> Allen, J., Watts, D. J., & Rand, D. G. (2024). Quantifying the impact of misinformation and vaccine-skeptical content on Facebook. *Science*, *384*, eadk3451. https://doi.org/10.1126/science.adk3451
>
> [View paper](https://doi.org/10.1126/science.adk3451)

## Summary

This paper asks whether COVID-19 vaccine misinformation on Facebook actually had the reach and persuasive power needed to meaningfully depress US vaccination rates — and reframes the answer around a surprising target. Combining large-scale survey experiments, crowdsourcing, and machine learning, the authors decompose societal impact into two necessary components: **exposure** (how many people saw content) and **persuasive influence** (how much it changed behavior when seen). Applied to 13,206 vaccine-related URLs viewed by ~233 million US Facebook users during the initial vaccine rollout, they find that although fact-check-flagged misinformation was more persuasive per view, its tiny reach meant that *unflagged, factually accurate but misleading* vaccine-skeptical content — much of it from mainstream outlets — had an estimated **46-fold greater aggregate impact** on vaccine hesitancy. The work directly challenges the "infodemic" narrative that viral falsehoods drove vaccine refusal.

## Key Contributions

- Introduces a scalable **exposure × persuasive influence** framework for estimating the real-world societal impact of online content.
- Provides one of the first *causal, ecosystem-scale* estimates of misinformation's impact, rather than correlational or proxy measures.
- Demonstrates a crowd-plus-machine-learning pipeline that generalizes experimental treatment effects to thousands of real-world URLs using minimal platform data.
- Reframes the misinformation debate around "gray-area" content that is technically true but misleading, especially from credible mainstream sources.
- Offers policy-relevant tooling for identifying high-impact harmful content that veracity-based moderation systematically misses.

## Methods

- Two randomized survey experiments on Lucid (total N = 18,725) measured the causal effect of 130 vaccine-related headlines/posts on a pre-post vaccination-intentions index; study 1 used 40 debunked misinformation items, study 2 used 90 highly shared, quality- and topic-balanced articles (true and false).
- Crowd raters labeled headlines on five dimensions (surprising, plausible, partisan lean, familiar, harmful-vs-helpful to health); random-effects meta-regressions linked these features to treatment effects.
- Facebook's Social Science One URL Shares dataset supplied actual view counts for 13,206 vaccine URLs shared >100 times during January–March 2021.
- A crowd–machine pipeline (177 raters building a crowdsourced aggregate score, then a COVID-Twitter-BERT model trained to predict it) estimated per-URL treatment effects, with impact computed as effect × views, normalized per user, and bootstrapped confidence intervals.

## Findings

- A single exposure to vaccine misinformation reduced vaccination intentions by ~1.5 pp on average (P = 0.00004), varying widely by item.
- Only the **harmful-to-health** dimension consistently predicted negative persuasion (~−0.69 pp per point); veracity was non-significant once harm-to-health was controlled.
- Flagged misinformation received only 8.7 million views — 0.3% of the 2.7 billion total vaccine-URL views; low-credibility domains accounted for just 5.1% of views.
- A single unflagged *Chicago Tribune* article about a doctor who died after vaccination reached ~54.9 million people, and its story cluster drew more than six times the views of all flagged misinformation combined.
- The crowdsourced score predicted observed effects well (adjusted r = 0.75); the BERT classifier reached 97% AUC on the hesitancy-inducing task.
- Vaccine-skeptical unflagged content lowered intentions by an estimated −2.28 pp per user versus −0.05 pp for flagged misinformation — a 46-fold difference; 98% of hesitancy-inducing views were unflagged.
- Mainstream outlets drove the largest aggregate harm; the total effect corresponds to roughly ~3 million fewer vaccinated Americans.

## Connections

This paper shares its first author and methodological spirit with [[Allen2025-ot]], extending the same bottom-up, causal-scale approach to platform effects on society. Its reframing of harm away from strict falsehood toward misleading mainstream content speaks directly to the exposure and impact debates in [[Guess2023-ai]], [[Guess2023-ur]], and [[Gonzalez-Bailon2023-uy]], which likewise use large-scale Facebook data to interrogate assumptions about how platform content shapes attitudes and behavior.
