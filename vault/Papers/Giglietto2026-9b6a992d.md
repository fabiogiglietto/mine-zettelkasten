---
title: "Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"
aliases: ["Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"]
authors: ["Fabio Giglietto", "Massimo Terenzi", "Anwesha Chakraborty", "Giada Marino"]
year: 2026
doi: 10.1007/978-3-032-11782-3_4
bibtex_key: Giglietto2026-9b6a992d
kind: own
topics: [generative-ai-influence-operations, coordinated-inauthentic-behavior]
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

This paper investigates how coordinated networks of Facebook groups use visual persuasion to promote online gambling, and how the rollout of generative AI has reshaped that promotion. Analyzing 2,323 images from 223 coordinated public groups surfaced through the Vera AI coordinated link-sharing detection workflow, the authors build a typology of persuasion drivers via a hybrid pipeline of vision-language description, dual denotative/connotative embeddings, and density-based clustering, complemented by qualitative coding. They argue that generative AI does not invent new persuasion strategies but intensifies and recombines existing ones—aspirational wealth, manufactured trust, FOMO, gamification, celebrity endorsement, and cultural localization—while enabling industrial-scale dissemination through an asymmetric regulatory regime that polices paid gambling ads but permits organic content. A structural break in posting volume in July 2023, following ChatGPT's launch, evidences this acceleration.

## Key Contributions

- An empirically grounded typology of visual persuasion drivers in coordinated organic gambling promotion.
- Evidence that generative AI acts as an accelerant and intensifier of pre-existing persuasion architectures rather than a source of novel strategies.
- A reproducible mixed-methods pipeline combining VLM image description, separated denotative and connotative embeddings, HDBSCAN clustering, and human qualitative coding.
- A regulatory critique of Meta's paid/organic asymmetry and a call to focus governance on algorithmic amplification rather than only post-hoc moderation.
- A reflexive account of using LLMs simultaneously as analytical tools and as the technology producing the material under study.

## Methods

The authors identify 223 coordinated public Facebook groups using the Vera AI alerts workflow (14-second co-share window, 0.995 edge weight) seeded from accounts amplifying fact-checker-flagged content, and collect 10,671 posts and 2,323 images (2017–2024) via the Meta Content Library and a custom image downloader. Each image is described by GPT-4o along both denotative and connotative dimensions; descriptions are embedded with text-embedding-3-small, reduced via UMAP, and clustered with HDBSCAN (101 denotative and 51 connotative clusters). A co-occurrence matrix across 366 cluster combinations is qualitatively coded by four analysts until saturation. Post-volume dynamics are tested with two-sample tests, interaction-term regression, and structural break detection, using ChatGPT's November 2022 launch as intervention.

## Findings

- Aspirational wealth and hyper-masculine status motifs occur in ~55% of coded cluster combinations; transactional "trust proof" imagery (receipts, cash-out screenshots) in ~37%.
- Distinct drivers include FOMO/urgency, gamification with low entry barriers, celebrity endorsements (e.g., Manny Pacquiao), exploitation of social ties, and cultural localization in Filipino and Urdu contexts.
- The Urdu-language cluster embeds gambling within conservative moral narratives (women in distress, family conflict), showing ideologically inflected localization.
- Monthly posts rose from a mean of 2,121 (pre-ChatGPT) to 280,952 (post-ChatGPT)—a 13,242% increase—with regression confirming both level shift and slope change (p<0.0001) and a structural break in July 2023.
- Post-2022 imagery shows consistent markers of AI generation (hyper-real lighting, smoothed surfaces, dreamlike saturation, improbable juxtapositions like sharks with slot machines) and fuses multiple persuasion drivers in single frames.
- Two emblematic AI-generated posts reached 4.3M and 3.3M views with thousands of cross-group shares.
- AI-generated characters can substitute for real influencers, sidestepping accountability mechanisms tied to human endorsers.

## Connections

This paper sits at the intersection of coordinated inauthentic behavior detection and generative-AI-enabled influence, extending the authors' prior work on coordinated link sharing ([[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]]) into the visual and synthetic-media domain. Its focus on AI-generated persuasive imagery in coordinated networks connects to work on synthetic media detection and AI-driven influence operations such as [[Minici2024-tf]], [[Luceri2025-tr]], and [[DiGiuseppe2026-pu]], while its argument that generative AI amplifies rather than replaces existing manipulation strategies resonates with broader assessments of AI's persuasive impact in [[Hackenburg2025-dj]] and [[Hackenburg2026-ud]]. The methodological use of VLMs and embeddings for large-scale visual analysis of coordinated campaigns parallels approaches in [[Kansaon2025-id]] and [[Mannocci2025-ig]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3)
