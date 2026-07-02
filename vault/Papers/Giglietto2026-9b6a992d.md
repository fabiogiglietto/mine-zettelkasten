---
title: "Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"
aliases: ["Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"]
authors: ["Fabio Giglietto", "Massimo Terenzi", "Anwesha Chakraborty", "Giada Marino"]
year: 2026
doi: 10.1007/978-3-032-11782-3_4
bibtex_key: Giglietto2026-9b6a992d
kind: own
topics: [coordinated-inauthentic-behavior, generative-ai-media]
citation_count: 2
open_access: true
source_url: https://doi.org/10.1007/978-3-032-11782-3_4
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3
pdf_available: true
discovery_date: 
---

# Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}

> Giglietto, F., Terenzi, M., Chakraborty, A., & Marino, G. (2026). Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}. *Countering Disinformation in the Era of Generative AI*. https://doi.org/10.1007/978-3-032-11782-3_4
>
> [View paper](https://doi.org/10.1007/978-3-032-11782-3_4)

## Summary

This paper investigates how generative AI has reshaped visual persuasion in coordinated online gambling promotion on Facebook. Analyzing 2,323 images from 223 coordinated public groups (2017–2024) surfaced through the Vera AI project, the authors build a typology of visual persuasion drivers and track how their deployment shifted after ChatGPT's release. They argue that generative AI does not invent new persuasion strategies but industrializes and intensifies existing ones—aspirational wealth, manufactured trust, FOMO, gamification, celebrity endorsement, and cultural localization—while exploiting a regulatory grey zone in Meta's asymmetric treatment of paid versus organic gambling content. Post volume in these networks grew by over 13,000% after November 2022, with a structural break in July 2023, implicating algorithmic amplification as the central governance failure.

## Key Contributions

- An empirically grounded typology of visual persuasion drivers in coordinated organic gambling promotion.
- Evidence that generative AI functions as an accelerant and recombinator of established persuasion architectures rather than a source of new strategies.
- A reproducible mixed-methods pipeline combining VLM-generated denotative/connotative image descriptions, dual embedding-based clustering (UMAP + HDBSCAN), and human qualitative coding.
- Identification of Meta's paid-vs-organic policy asymmetry as a structural loophole and a call to refocus regulation on amplification infrastructure rather than post-hoc moderation.
- Reflexive commentary on using LLMs both to analyze and to produce the manipulative content under study.

## Methods

Coordinated groups were identified via the Vera AI alerts workflow (14-second co-share window, 0.995 edge weight), seeded from accounts spreading fact-checker-flagged content. Posts and images were retrieved through the Meta Content Library plus a custom client-side downloader (10,671 posts; 2,323 images). GPT-4o produced paired denotative and connotative image descriptions, converted to embeddings (text-embedding-3-small), reduced with UMAP, and clustered via HDBSCAN into 101 denotative and 51 connotative clusters. Four coders qualitatively analyzed 85 cluster co-occurrence combinations to derive the driver typology. Temporal impact was assessed with t-tests, Wilcoxon tests, interaction-term regression, and structural break detection around ChatGPT's launch.

## Findings

- Mean monthly posts rose from 2,121 (pre-ChatGPT) to 280,952 (post-ChatGPT); regression confirmed both a level shift and steep slope change (p<0.0001), with a July 2023 structural break.
- Aspirational wealth and hyper-masculine status motifs appear in ~55% of analyzed cluster combinations; transactional "trust proof" visuals (payment receipts, cash-out screenshots) in ~37%.
- Additional drivers include FOMO/urgency, gamification with low entry barriers, celebrity endorsements (e.g., Manny Pacquiao), and exploitation of social relations.
- Cultural-linguistic localization is pronounced: an Urdu-language cluster embeds gambling in conservative moral narratives featuring women in distress and family conflict; Filipino-language content targets another distinct audience.
- Post-2022 visuals show consistent AI-generation markers (hyper-real lighting, smoothed surfaces, dreamlike saturation, improbable juxtapositions like sharks with slot machines) and fuse multiple persuasion drivers in single images.
- Two emblematic AI-generated posts reached 4.3M and 3.3M views with wide cross-group amplification.

## Connections

This work sits at the intersection of coordinated inauthentic behavior detection and generative-AI-enabled influence, extending the authors' prior CIB methodology in [[Giglietto2023-fa71a001]], [[Giglietto2022-0e951ac5]], and [[Giglietto2020-9d8acdd7]] to a visual, AI-driven domain. It complements work on AI-generated imagery and synthetic media aesthetics such as [[Manovich2026-ih]], [[Dodds2026-df]], and [[Stanusch2026-ec]], and connects to broader studies of coordinated visual and multimodal campaigns including [[Kansaon2025-id]], [[Minici2024-tf]], and [[Luceri2025-tr]]. The regulatory-amplification argument resonates with platform-governance concerns raised in [[Hurcombe2025-cs]] and [[Kuznetsova2025-nu]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3)
