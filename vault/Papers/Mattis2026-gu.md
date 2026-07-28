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
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Mattis2026-gu.mp3
pdf_available: true
discovery_date: 2026-07-27T14:43:02.391648Z
---

# Feeling iffy about generative AI: Investigating audiences’ trustworthiness perceptions of task-specific AI disclosures

> Mattis, N., Kieslich, K., & de Vreese, C. H. (2026). Feeling iffy about generative AI: Investigating audiences’ trustworthiness perceptions of task-specific AI disclosures. *Digital Journalism*, 1–21. https://doi.org/10.1080/21670811.2026.2703599
>
> [View paper](https://doi.org/10.1080/21670811.2026.2703599)

## Summary

This paper examines how disclosing that generative AI—rather than a human—performed specific journalistic tasks shapes audiences' perceptions of news trustworthiness. Whereas prior work relied on blunt "AI-generated" versus "human-generated" labels, the authors argue that such generic framings misrepresent how journalists actually weave AI into their workflows, and they instead test task-specific disclosures across seven distinct journalistic tasks. Through a preregistered conjoint experiment with 683 Dutch respondents, they find that all AI disclosures depress trust, but that the size of the penalty varies systematically by task, is moderated by readers' political leanings and knowledge of journalistic AI, and gives rise to five distinct audience preference profiles. The paper situates itself in journalism-studies debates on transparency, drawing on attribution theory, expectancy violations theory, and the algorithmic aversion/appreciation literature.

## Key Contributions

- Provides empirical evidence on task-specific (rather than generic) AI disclosures across the journalistic value chain, filling a gap in the transparency literature.
- Identifies political position and AI-journalism knowledge as consistent individual-level moderators of disclosure effects.
- Introduces and validates five audience preference profiles, along with their socio-demographic and attitudinal predictors, offering actionable segmentation for practitioners.
- Tests robustness across three news topics of differing controversiality, showing topic has little effect and bolstering generalizability.
- Contributes to normative debate on meaningful journalistic transparency, cautioning that trust penalties should not justify abandoning disclosure.

## Methods

A preregistered conjoint experiment was fielded via Qualtrics in January 2025 with 683 Dutch respondents (quota-matched on age, gender, and education; average age 50). Stimuli paired pretested mock-up articles (generated with ChatGPT 3.5) with an "AI Monitor" table indicating, for each of seven tasks (idea generation, image generation, background research, article writing, proofreading, fact-checking, and human-in-the-loop), whether it was performed by a human or an AI. A fractional factorial design produced eight stimulus compositions, and respondents rated 24 profiles on a 7-point trustworthiness scale. Three topics of varying controversiality (vaccination, housing, logistics) were selected via pretest. Analysis used the `cjoint` package for AMCEs and interaction effects, k-means clustering (k=5) on respondents' conjoint coefficients, and MANOVA/ANOVA with Tukey's HSD to predict cluster membership.

## Findings

- Every AI disclosure significantly reduced perceived trustworthiness, with effects between 0.23 and 0.62 points on a 7-point scale.
- A task hierarchy emerged: earlier value-chain tasks (image and idea generation) incurred smaller penalties, while news-production tasks and especially fact-checking incurred the largest; lacking a human in the loop had only a modest effect.
- Contrary to expectations, later position in the value chain did not automatically mean larger penalties—perceived importance for quality/accuracy (e.g., fact-checking) mattered more.
- No significant differences across the three news topics, suggesting topic controversiality is not an important contextual moderator.
- Politically left respondents reacted more strongly against AI-written articles; right-leaning respondents cared relatively less about human fact-checking.
- High AI-journalism-knowledge respondents (~40%) showed even sharper penalties for AI fact-checking; moderation muted but never reversed the overall negative direction.
- Five preference clusters identified: Cautious Optimists (27.7%), Indifferents (28.7%), Fact-Checkers (15.2%), Human Creatives (14.2%), and Human in the Loops (14.2%).
- Lower concern about GenAI use was concentrated among those who know little about how journalists actually use AI.

## Connections

This study sits within the broader concern over generative AI in the media ecosystem and audience trust, connecting to work on how people evaluate and respond to AI-produced or AI-assisted content such as [[DeVerna2025-dl]] and [[Hameleers2026-mc]]. Its emphasis on media literacy and knowledge as a moderator of AI perceptions resonates with disclosure and labeling debates, while its finding that source attribution reshapes credibility judgments complements platform- and audience-level analyses of trust in the information environment.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Mattis2026-gu.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
