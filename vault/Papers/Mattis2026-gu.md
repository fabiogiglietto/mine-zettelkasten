---
title: "Feeling iffy about generative AI: Investigating audiences’ trustworthiness perceptions of task-specific AI disclosures"
aliases: ["Feeling iffy about generative AI: Investigating audiences’ trustworthiness perceptions of task-specific AI disclosures"]
authors: ["Nicolas Mattis", "Kimon Kieslich", "Claes Holger de Vreese"]
year: 2026
doi: 10.1080/21670811.2026.2703599
bibtex_key: Mattis2026-gu
topics: [generative-ai-media-manipulation, platforms-audiences-and-online-communities]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1080/21670811.2026.2703599
podcast_url: 
pdf_available: true
discovery_date: 2026-07-27T14:43:02.391648Z
---

# Feeling iffy about generative AI: Investigating audiences’ trustworthiness perceptions of task-specific AI disclosures

> Mattis, N., Kieslich, K., & de Vreese, C. H. (2026). Feeling iffy about generative AI: Investigating audiences’ trustworthiness perceptions of task-specific AI disclosures. *Digital Journalism*, 1–21. https://doi.org/10.1080/21670811.2026.2703599
>
> [View paper](https://doi.org/10.1080/21670811.2026.2703599)

## Summary

This paper examines how disclosing that generative AI performed specific journalistic tasks — rather than a human — shapes audiences' perceptions of news trustworthiness. The authors argue that prior work relied on crude "AI-generated" versus "human-generated" labels that misrepresent how journalists actually integrate AI into their workflows, and that the transparency debate needs more granular, task-specific disclosures. Through a preregistered conjoint experiment with Dutch respondents, they show that all task-specific AI disclosures reduce trust, but that the size of the penalty varies systematically by task, by individual reader characteristics, and across five distinct audience preference profiles. The paper is framed within journalism-studies debates on transparency and audience trust, drawing on attribution theory, expectancy violations theory, and the algorithmic aversion/appreciation literature.

## Key Contributions

- Provides empirical evidence on task-specific (rather than generic) AI disclosure effects across the journalistic value chain, filling a gap in the transparency literature.
- Identifies political position and knowledge of journalistic AI as consistent individual-level moderators of disclosure effects.
- Introduces and validates five distinct audience preference profiles with socio-demographic and attitudinal predictors, offering actionable audience segmentation.
- Tests robustness across three news topics of differing controversiality, finding topic matters little and thus strengthening generalizability.
- Situates findings normatively, cautioning that trust penalties should not justify abandoning disclosure and calling for media-literacy investment.

## Methods

Preregistered conjoint experiment via Qualtrics with 683 Dutch respondents (January 2025; quota-matched on age, gender, education). Stimuli paired pretested ChatGPT-generated mock news articles with an "AI Monitor" table indicating whether each of seven journalistic tasks (idea generation, image generation, background research, article writing, proofreading, fact-checking, and human-in-the-loop) was performed by a human or AI. A fractional factorial design yielded eight stimulus compositions; respondents rated 24 profiles on a 7-point trustworthiness scale. Three topics of varying controversiality (vaccination, housing, logistics) were selected via pretest. Analysis used the `cjoint` R package for AMCEs and interaction effects, k-means clustering (k=5) on respondent-level conjoint coefficients, and MANOVA/ANOVA with Tukey's HSD to predict cluster membership. Moderators included political self-placement and a seven-item AI-journalism knowledge measure, with controls for general AI attitudes (GAAIS), GenAI experience, and news trust.

## Findings

- Every AI disclosure attribute significantly reduced perceived trustworthiness, with effects ranging from 0.23 to 0.62 points on a 7-point scale.
- A task hierarchy emerged: earlier value-chain tasks (image and idea generation) incurred smaller penalties, while fact-checking incurred the largest; lacking a human in the loop had only a modest negative effect.
- Topic controversiality was not an important moderator — no significant differences across vaccination, housing, and logistics news.
- Politically left respondents reacted more strongly against AI-written articles; right-leaning respondents cared relatively less about human fact-checking.
- High-knowledge respondents (~40%) showed even sharper penalties for AI fact-checking; moderators muted but never reversed the overall negative direction.
- Five preference clusters were identified for the vaccination topic: Cautious Optimists, Indifferents, Fact-Checkers, Human Creatives, and Human in the Loops — differing in age, education, political leaning, and AI attitudes.
- Lower concern about GenAI use was concentrated among respondents who know little about how journalists actually use AI.

## Connections

This paper sits within a cluster of work on how audiences perceive and respond to AI-authored or AI-mediated content; its finding that disclosures reduce credibility resonates with experimental studies of AI-generated news and persuasion such as [[Hameleers2026-mc]] and [[DeVerna2025-dl]]. Its emphasis on media literacy and knowledge as a moderator of trust connects to broader debates on generative AI in the information ecosystem represented across this topic. Its practitioner-facing transparency and disclosure focus is distinct enough that few other listed papers address the same task-specific disclosure question directly.
