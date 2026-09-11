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
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Much2026-gu.mp3
pdf_available: true
discovery_date: 2026-09-10T08:47:38.926258Z
---

# Did podcasts help Trump win young men? Gendered media spaces and gender gaps

> Much, M., Rutherford, K., Greenfield, J., Tucker, J. A., & Nagler, J. (2026). Did podcasts help Trump win young men? Gendered media spaces and gender gaps. *APSA Preprints*. https://doi.org/10.33774/apsa-2026-cdb6x
>
> [View paper](https://doi.org/10.33774/apsa-2026-cdb6x)

## Summary

This paper asks whether entertainment podcasts helped Donald Trump win an unusually strong share of young men in 2024, a year when the youth gender gap in vote choice widened sharply. The authors introduce the concept of **gendered media spaces**: non-political entertainment environments where audiences sort on masculine/feminine content expression rather than on ideology. Because masculinity is cognitively linked to conservatism (and femininity to liberalism), listeners of masculine-coded podcasts are incidentally exposed to conservative content without seeking politics—a mechanism they call **gendered ideological sorting**, distinct from classic partisan selective exposure. Combining two survey datasets with the first large-scale transcript-level analysis of 36,659 episodes from 276 top U.S. podcasts, they show that podcast gender expression tracks ideological lean, that Trump targeted podcasts on gender rather than ideology, and that conservative podcast exposure correlates with higher Trump support—though the effect is too small to explain the whole gender gap.

## Key Contributions

- Introduces the theoretical concept of **gendered media spaces** and the mechanism of **gendered ideological sorting** as distinct from partisan selective exposure.
- Provides the first large-scale, transcript-level mapping of the top U.S. podcast ecosystem along gender expression and ideology dimensions.
- Demonstrates a methodology linking LLM-based content labeling, consumption data, and survey data to connect media content, audience composition, and vote behavior.
- Extends talk-radio and soft-news persuasion literatures to the podcast medium and connects them to the age-differentiated gender gap.
- Offers empirical evidence on candidate media-venue selection strategy (gender- vs. ideology-based targeting) in 2024.

## Methods

The authors analyzed 36,659 episodes from the top 0.01% of U.S. podcasts (276 shows, Jan 2024–Jan 2025), selected via ListenNotes popularity validated against Edison rankings. Audio was pulled from RSS feeds and transcribed/diarized with WhisperX, yielding ~8.5 million speaker chunks. Gemini 3 Flash Preview labeled each chunk in a two-stage detection-then-scoring pipeline that independently scores gender expression (masculine–feminine) and ideology (liberal–conservative), collapsed to ternary scores and aggregated into word-count-weighted net indices (90% transcript, 10% host gender). Genre (political vs. non-political) was drawn from Edison/Apple metadata, kept independent of content scores. Consumption came from Edison Podcast Metrics (show demographics plus 3,544 individual respondents across 129 non-political podcasts); an original YouGov panel (1,167 respondents, post-election) modeled probability of voting Trump conditional on listening to Joe Rogan and other candidate-interview podcasts, controlling for partisanship and prior vote.

## Findings

- Top podcasts carry substantial political content: political-genre episodes average 81% political utterances; non-political average 15% (median 7%).
- Among non-political episodes with political content, 47% lean liberal, 27% conservative, 26% moderate/mixed; explicitly political podcasts are 72% conservative.
- Masculine expression correlates positively with conservatism and feminine with liberalism; nearly all conservative podcasts are heavily masculine, while masculinity spans the ideological spectrum.
- Trump's 16 non-political appearances aligned with gender expression more than ideology (a persuasion strategy); Harris's 5 appearances tracked ideological lean (mobilization-oriented).
- Young men received the most exposure to conservative content of any age-gender cohort in non-political podcasts.
- Conservative podcast exposure is associated with higher Trump vote intention after controlling for party ID, concentrated among Independents; effect sizes were similar across groups but young men encountered far more conservative content.
- Counterfactuals: giving young men young women's podcast diet lowers predicted Trump support; the reverse modestly raises women's—but the association is small and cannot explain the full gender gap.
- Self-reported Joe Rogan listening correlates with higher Trump vote probability even after controlling for party ID and prior vote.

## Connections

This paper sits alongside other 2024-election media-influence work engaging persuasion and exposure mechanisms; its careful bounding of a real-but-small persuasion effect resonates with experimental estimates of message and media persuasion in [[Hackenburg2025-dj]] and [[Hackenburg2026-ud]]. Its methodological pairing of LLM content labeling with consumption and survey data connects to computational analyses of political media at scale such as [[Bollenbacher2026-vz]] and [[Balluff2026-bv]]. The focus on incidental exposure through non-ideological content environments contrasts with selective-exposure and network-sorting accounts examined in [[Gonzalez-Bailon2024-rq]] and [[Bakshy2015-rn]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Much2026-gu.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-the-podcast-gender-code-how/id1866587707?i=1000788829687)
