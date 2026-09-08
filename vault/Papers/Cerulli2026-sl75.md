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
topics: [llms-computational-content-analysis, platforms-audiences-and-online-communities]
citation_count: 1
open_access: true
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

This study investigates whether "dark" personality traits — Successful Psychopathy, Grandiose Entitlement, Sadistic Cruelty, and Entitlement Rage — plus trolling tendencies leave observable traces in real online behavior. Working at the intersection of personality psychology, cyberpsychology, and computational social science, the authors built a bespoke Web application that securely linked Amazon Mechanical Turk participants' validated questionnaire responses to their consented Reddit account activity. Their central finding is a striking dissociation: validated dark *traits* correlate with people's *self-reports* of producing uncivil content, but do **not** reliably predict computationally extracted linguistic or toxicity features. In contrast, self-reported *behavioral* engagement in (and victimization by) toxic exchanges aligns robustly with observable language patterns. The paper thus challenges a core assumption of computational personality inference — that surface linguistic signals proxy stable traits — while validating computational features for behavior-focused analysis.

## Key Contributions

- A methodological framework and Web application for ethically linking validated psychometric self-reports to user-level, consented Reddit activity data.
- A dataset of ~57K comments (2.2M tokens) from 114 users paired with Dark Tetrad and trolling assessments.
- Empirical evidence that surface-level computational features do **not** reliably proxy validated dark personality traits.
- Demonstration that computational features *do* capture self-reported behavioral engagement in incivility, supporting behavior- (not trait-) focused moderation.
- An argument for grounding computational personality inference in validated psychological instruments and richer, context-aware representations.

## Methods

Participants were recruited via MTurk (US-based Reddit users; account ≥30 days, ≥50 comments, ≥1500 tokens), yielding 114 valid respondents from 331 consenting users after attention-check filtering. A 66-item questionnaire combined the Dark Side of Humanity Scale (DSHS), the Cyberbully/Troll Deviancy Scale (CTDS), demographics, and five social-media-use items. From each user's Reddit history the authors extracted 219 features — basic linguistics, Perspective API toxicity scores, LIWC-22 categories, NRC-EIL and NRC-VAD lexicons, EmoAtlas contextual emotions, FrameAxis moral foundations, BERT-based irony, and hand-crafted Dark Triad text proxies. Hierarchical clustering on Spearman-correlation distances reduced redundancy to 154 features. Confirmatory (Bonferroni-corrected) and exploratory (Benjamini–Hochberg-corrected) Spearman analyses were run with bootstrap CIs and sensitivity checks.

## Findings

- Trolling and Successful Psychopathy positively correlated with self-reported production of uncivil content (SM05), surviving Bonferroni correction.
- No dark dimension significantly correlated with median toxicity, toxicity subtypes, LIWC categories, emotion/affect features, or moral framing after correction.
- Self-reported victimization (SM04) and production (SM05) of toxic content correlated with median toxicity, identity attacks, severe toxicity, negative tone, moral language, certitude, and morally-framed features (e.g., authority.vice, fairness.vice).
- Prior hand-crafted text-derived Dark Triad proxies did not converge with any DSHS dimension after correction.
- Socio-demographics (gender, education, political affiliation) showed no significant differences in dark trait scores.
- ~39.5% of participants exceeded the μ+σ threshold on at least one dimension; only 2.6% exceeded on all five.
- Toxic exchanges showed a perpetrator–victim reciprocity pattern: those reporting producing toxic content also more often reported being targeted.

## Connections

This paper sits within the computational study of online toxicity and moderation, sharing methodological terrain with LLM- and classifier-based approaches to detecting harmful content such as [[Triedman2025-uy]] and text-based ideology/trait inference exemplified by [[Le-Mens2025-qz]]. Its critique of inferring latent attributes from surface linguistic signals speaks to broader debates about the validity of computational content analysis represented in this register's toxicity and audience-behavior work; the emphasis on platform-level user activity connects loosely to community-behavior studies like [[Gagrcin2024-dl]].
