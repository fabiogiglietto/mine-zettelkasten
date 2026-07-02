---
title: "Dark personality traits and online toxicity: Linking self-reports to Reddit activity"
aliases: ["Dark personality traits and online toxicity: Linking self-reports to Reddit activity"]
authors: ["Aldo Cerulli", "Benedetta Tessa", "Giuseppe La Selva", "Oronzo Mazzeo", "Lorenzo Cima", "Lucia Monacis", "Stefano Cresci"]
year: 2026
doi: 10.1016/j.chb.2026.109085
bibtex_key: Cerulli2026-sl75
kind: team
submitted_by: "GiadaM. / Uniurb"
slack_permalink: https://minesmd.slack.com/archives/C0BDU82EBHQ/p1782984077356849
topics: []
citation_count: 0
open_access: false
source_url: https://doi.org/10.1016/j.chb.2026.109085
podcast_url: 
pdf_available: true
discovery_date: 2026-07-02T11:09:15.304480Z
---

# Dark personality traits and online toxicity: Linking self-reports to Reddit activity

> Cerulli, A., Tessa, B., Selva, G. L., Mazzeo, O., Cima, L., Monacis, L., & Cresci, S. (2026). Dark personality traits and online toxicity: Linking self-reports to Reddit activity. *Computers in Human Behavior*. https://doi.org/10.1016/j.chb.2026.109085
>
> [View paper](https://doi.org/10.1016/j.chb.2026.109085)

## Summary

This paper investigates whether validated dark personality traits (Dark Tetrad plus trolling) actually manifest in observable Reddit language and behavior, or whether the widespread computational practice of inferring personality from text rests on shaky empirical ground. The authors built a custom Web application to consensually link Mechanical Turk participants' psychometric responses to their Reddit accounts, assembling ~57K comments from 114 users paired with Dark Side of Humanity Scale and Cyberbully/Troll Deviancy Scale scores. Their central finding is a disconnect: validated dark traits correlate with *self-reported* uncivil behavior but not with any of 219 text-derived linguistic or toxicity features after multiple-comparison correction. In contrast, self-reported engagement in and victimization by toxic content aligns robustly with observed linguistic patterns, suggesting computational features track online behavior rather than stable traits.

## Key Contributions

- A methodological framework and Web application for ethically linking validated psychometric self-reports to consented user-level Reddit activity.
- A dataset of ~57K comments from 114 users annotated with Dark Tetrad and trolling assessments.
- Empirical evidence that surface-level computational linguistic features do *not* reliably proxy validated dark traits, undermining a common assumption in computational personality inference.
- Evidence that the same features *do* capture self-reported behavioral engagement in incivility, supporting behavior-focused (rather than trait-focused) approaches to moderation.
- A demonstration that hand-crafted text-derived Dark Triad proxies from prior work fail to converge with validated questionnaire scores.

## Methods

The authors recruited 114 US-based Reddit users (from 331 initial consenters, after attention-check filtering) via MTurk, requiring accounts of ≥30 days, ≥50 comments, and ≥1500 tokens. Participants completed a 66-item questionnaire combining the DSHS (Successful Psychopathy, Grandiose Entitlement, Sadistic Cruelty, Entitlement Rage), the CTDS trolling scale, demographics, and social media use items. For each user, 219 features were extracted spanning basic linguistics, Perspective API toxicity, LIWC-22, NRC-EIL/VAD emotion lexicons, EmoAtlas, FrameAxis moral foundations, BERT-based irony, and text-derived Dark Triad proxies. Hierarchical clustering on Spearman correlation distances reduced this to 154 features. Analyses used Spearman correlations with Bonferroni correction (confirmatory) and Benjamini–Hochberg correction (exploratory), plus bootstrap CIs.

## Findings

- Trolling and Successful Psychopathy correlated moderately and significantly with self-reported production of uncivil content, surviving Bonferroni correction.
- No dark trait dimension significantly correlated with median toxicity, toxicity subtypes, LIWC categories, emotion/affect, or moral framing after correction.
- Self-reported victimization and self-reported production of toxic content both correlated significantly with median toxicity, identity attacks, severe toxicity, negative tone, moral language, certitude, and vice-framed moral features — suggesting a perpetrator–victim reciprocity.
- Hand-crafted text-derived Dark Triad formulas from prior work showed no significant convergence with DSHS dimensions after correction.
- ~39.5% of participants scored above μ+σ on at least one dark/trolling dimension; only 2.6% did so on all five.
- Demographic variables (gender, education, political affiliation) showed no significant differences in dark trait scores after correction.

## Connections

No other papers under this topic were provided, so no wikilinks are warranted. The work situates itself against the Dark Triad/Tetrad tradition (Paulhus & Williams; Buckels et al.) and the computational personality-inference literature, and would connect naturally to research on online trolling, cyberbullying, and the validity of LLM- or lexicon-based psychological profiling from social media text.
