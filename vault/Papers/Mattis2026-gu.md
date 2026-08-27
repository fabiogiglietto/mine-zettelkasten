---
title: "Feeling iffy about generative AI: Investigating audiences’ trustworthiness perceptions of task-specific AI disclosures"
aliases: ["Feeling iffy about generative AI: Investigating audiences’ trustworthiness perceptions of task-specific AI disclosures"]
authors: ["Nicolas Mattis", "Kimon Kieslich", "Claes Holger de Vreese"]
year: 2026
doi: 10.1080/21670811.2026.2703599
bibtex_key: Mattis2026-gu
topics: [ai-social-theory-trust, llm-computational-content-analysis]
citation_count: 0
open_access: false
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

This paper examines how disclosing that generative AI—rather than a human—performed specific journalistic tasks affects audience perceptions of news trustworthiness. Arguing that prior work relied on crude generic "AI-generated" versus "human-generated" labels that misrepresent how journalists actually integrate AI into their workflows, the authors advocate for more granular, task-specific disclosures. Through a preregistered conjoint experiment with 683 Dutch respondents spanning seven journalistic tasks, they show that all AI disclosures depress trust, but the size of the penalty varies substantially by task, is moderated by individual characteristics (notably political position and AI-journalism knowledge), and gives rise to five distinct reader preference profiles. The work is framed within journalism studies debates on transparency and audience trust, drawing on attribution theory, expectancy violations theory, and the algorithmic aversion/appreciation literature.

## Key Contributions

- Empirical evidence on task-specific (rather than generic) AI disclosures across the journalistic value chain, filling a gap in the transparency literature.
- Identification of political position and AI-journalism knowledge as consistent individual-level moderators of disclosure effects.
- Introduction and validation of five distinctive audience preference profiles with their socio-demographic and attitudinal predictors, offering actionable segmentation for practitioners.
- Robustness testing across three news topics of varying controversiality, showing topic has little effect and supporting generalizability.
- A normative caution: trust penalties should not justify abandoning disclosure, and media literacy investment is needed.

## Methods

A preregistered conjoint experiment fielded via Qualtrics in January 2025 with a Dutch sample (N = 683) quota-matched to the population on age, gender, and education. Stimuli paired pretested mock-up news articles (generated with ChatGPT 3.5) with an "AI Monitor" table indicating whether each of seven tasks (idea generation, image generation, background research, article writing, proofreading, fact-checking, human-in-the-loop) was done by a human or AI; a fractional factorial design produced eight compositions, with each respondent rating 24 profiles. Three topics of differing controversiality (vaccination, housing, logistics) were used. Trustworthiness was measured on a 7-point scale; moderators included political self-placement and AI-journalism knowledge, with controls for AI attitudes (GAAIS), GenAI experience, and general news trust. Analysis used the cjoint R package (AMCEs, AMCIEs), k-means clustering (k=5) on respondent coefficients, and MANOVA/ANOVA to predict cluster membership.

## Findings

- Every AI disclosure attribute significantly reduced perceived trustworthiness, with effects ranging from 0.23 to 0.62 points on the 7-point scale.
- A task hierarchy emerged: earlier value-chain tasks (image and idea generation) carried smaller penalties, while production tasks—especially fact-checking—incurred the largest; lacking a human in the loop had only a modest effect.
- No significant differences in disclosure effects across the three news topics, indicating controversiality is not an important contextual moderator.
- Politically left respondents reacted more negatively to AI-written articles; right-leaning respondents cared relatively less about human fact-checking.
- High AI-journalism-knowledge respondents (~40%) showed even more pronounced penalties for AI fact-checking; moderation effects muted but never reversed the overall negative direction.
- Five preference clusters (for the vaccination topic): Cautious Optimists (27.7%), Indifferents (28.7%), Fact-Checkers (15.2%), Human Creatives (14.2%), and Human in the Loops (14.2%).
- Lower concern about GenAI use was concentrated among those who know little about how journalists actually use AI.

## Connections

This paper sits within the trust-and-AI strand of the register and speaks to work on labelling and disclosure of AI-generated content, connecting to [[Achmann-Denkler2026-lx]] on AI disclosure practices in journalism/social media. Its use of ChatGPT-generated news stimuli and concern with audience reception link it to studies of LLM-produced persuasive and news content such as [[Hackenburg2025-dj]] and [[DeVerna2025-dl]]. It complements the broader question of how audiences evaluate AI-mediated information addressed in [[Costello2024-bg]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Mattis2026-gu.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-when-ai-fact-checks-trust-falls/id1866587707?i=1000778564036)
