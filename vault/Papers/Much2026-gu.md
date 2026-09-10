---
title: "Did podcasts help Trump win young men? Gendered media spaces and gender gaps"
aliases: ["Did podcasts help Trump win young men? Gendered media spaces and gender gaps"]
authors: ["Melina Much", "Kylan Rutherford", "Jason Greenfield", "Joshua A. Tucker", "Jonathan Nagler"]
year: 2026
doi: 10.33774/apsa-2026-cdb6x
bibtex_key: Much2026-gu
topics: [elections-social-media, computational-political-media-influence]
citation_count: 0
open_access: false
source_url: https://doi.org/10.33774/apsa-2026-cdb6x
podcast_url: 
pdf_available: true
discovery_date: 2026-09-10T08:47:38.926258Z
---

# Did podcasts help Trump win young men? Gendered media spaces and gender gaps

> Much, M., Rutherford, K., Greenfield, J., Tucker, J. A., & Nagler, J. (2026). Did podcasts help Trump win young men? Gendered media spaces and gender gaps. *APSA Preprints*. https://doi.org/10.33774/apsa-2026-cdb6x
>
> [View paper](https://doi.org/10.33774/apsa-2026-cdb6x)

## Summary

This paper asks whether entertainment podcasts helped Donald Trump win an unusually large share of young men in 2024, a year when the youth gender gap in vote choice widened sharply. The authors introduce the concept of **gendered media spaces**: non-political entertainment environments where audiences sort on masculine/feminine content rather than on ideology. Because masculinity is cognitively linked to conservatism (and femininity to liberalism), listeners of masculine-coded podcasts are incidentally exposed to conservative content without seeking politics — a mechanism the authors call **gendered ideological sorting**, distinct from classic partisan selective exposure. Drawing on the first large-scale transcript-level analysis of the top U.S. podcasts plus two survey datasets, they show podcast gender expression correlates with ideological lean, that Trump targeted podcasts on gender rather than ideology, and that conservative podcast exposure is associated with higher Trump support — though the effect is too small to explain the full gender gap.

## Key Contributions

- Introduces the theoretical concepts of **gendered media spaces** and **gendered ideological sorting** as a persuasion mechanism distinct from ideological self-selection.
- Delivers the first large-scale, transcript-level empirical map of the top U.S. podcast ecosystem along dimensions of gender expression and ideology.
- Demonstrates a methodology linking LLM-based content labeling, consumption data, and survey data to connect media content, audience composition, and vote behavior.
- Extends talk-radio and soft-news persuasion literatures to the podcast medium and ties them to the age-differentiated gender gap.
- Provides empirical evidence on candidate media-venue selection strategy (gender vs. ideology targeting).

## Methods

The authors transcribed and diarized 36,659 episodes from the 276 most popular U.S. podcasts (Jan 2024–Jan 2025) using WhisperX, yielding ~8.5 million speaker chunks. Podcasts were selected via ListenNotes popularity, validated against Edison rankings. Content was labeled with Gemini 3 Flash Preview in a two-stage detection-then-scoring pipeline that independently classified gender expression and ideology, collapsed to ternary scores and aggregated into word-count-weighted net indices (blending transcript scores 90% with host gender 10%). Genre classification came from Edison/Apple metadata, kept independent of content scores. Consumption was measured via Edison Podcast Metrics (show demographics for all 276 podcasts; individual-level data for 3,544 respondents), and an original YouGov panel of 1,167 respondents modeled the probability of a Trump vote conditional on Joe Rogan and other candidate-interview listening, controlling for partisanship and prior vote.

## Findings

- Top podcasts carry substantial political content: political-genre episodes average 81% political utterances; non-political average 15% (median 7%).
- Among non-political episodes with political content, 47% lean liberal, 27% conservative, 26% moderate/mixed; explicitly political podcasts are 72% conservative — liberals dominate the overall landscape but conservatives are more prolific within political podcasting.
- Masculine expression correlates positively with conservatism and feminine with liberalism; nearly all conservative podcasts are heavily masculine, while masculinity spans the ideological spectrum.
- Trump's 16 non-political appearances aligned with gender expression over ideology (persuasion strategy); Harris's 5 appearances tracked ideological lean (mobilization).
- Young men received the most exposure to conservative content of any age-gender cohort in non-political podcasts.
- Conservative podcast exposure predicts higher Trump vote intention after controlling for party ID, concentrated among Independents; effect sizes were similar across groups, but young men encountered far more conservative content.
- Counterfactuals: giving young men young women's podcast diet significantly lowers predicted Trump support, but the overall association is small and cannot explain the full gap.
- Self-reported Joe Rogan listening predicts higher Trump vote probability net of party ID and prior vote.

## Connections

This work sits within the computational study of political media influence and elections, sharing methodological DNA with LLM-based persuasion and content-analysis studies such as [[Hackenburg2025-dj]] and [[Hackenburg2026-ud]], and with survey-linked media-effect estimation in the tradition of [[Allen2025-ot]] and [[Allcott2025-jb]]. Its emphasis on incidental, identity-sorted exposure as an alternative to ideological self-selection complements platform-level exposure work like [[Gonzalez-Bailon2024-rq]] and [[Bakshy2015-rn]]. None of the listed papers directly address podcasts or the gendered-media-space concept, so this paper's core theoretical contribution stands largely on its own within the set.
