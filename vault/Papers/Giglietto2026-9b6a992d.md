---
title: "Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"
aliases: ["Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"]
authors: ["Fabio Giglietto", "Massimo Terenzi", "Anwesha Chakraborty", "Giada Marino"]
year: 2026
doi: 10.1007/978-3-032-11782-3_4
bibtex_key: Giglietto2026-9b6a992d
kind: own
topics: [coordinated-inauthentic-behavior, generative-ai-and-media]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1007/978-3-032-11782-3_4
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3
pdf_available: true
discovery_date: 
---

# Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}

## Summary

This paper examines how coordinated networks of Facebook groups promote online gambling through visual persuasion, and how the public release of generative AI tools has reshaped that promotional ecosystem. Analyzing 2,323 images drawn from 223 coordinated public groups detected via the Vera AI alerts workflow, the authors build a typology of persuasive visual "drivers" — aspirational wealth, manufactured trust, FOMO, gamification, celebrity endorsement, social-relations exploitation, and cultural localization — and show that these drivers operate synergistically rather than in isolation. They argue that generative AI did not invent new persuasion strategies but dramatically intensified and industrialized existing ones, producing an exponential surge in coordinated posting after ChatGPT's launch. The paper frames algorithmic amplification and Meta's asymmetric treatment of paid versus organic gambling content as the central governance failures enabling this harm.

## Key Contributions

- An empirically grounded typology of visual persuasion drivers in organic, coordinated gambling promotion on Facebook.
- Evidence that generative AI acts as an accelerant and recombinator of established persuasion architectures, not a source of wholly novel tactics.
- A reproducible mixed-methods pipeline pairing vision-language model descriptions, dual denotative/connotative embeddings, HDBSCAN clustering, and human qualitative coding for large-scale visual analysis.
- Identification of the paid/organic regulatory asymmetry on Meta and of algorithmic amplification as the principal governance blind spot.
- A reflexive critique of using LLMs simultaneously as analytic instruments and as the technology producing the manipulative artifacts under study.

## Methods

The 223-group network was identified through Vera AI's coordinated link-sharing detection (14-second window, 0.995 edge weight) seeded from accounts spreading fact-checker-flagged content. Posts and images (10,671 posts; 2,323 unique images, 2017–2024) were collected via the Meta Content Library and a custom image downloader. GPT-4o generated paired denotative and connotative descriptions of each image, which were embedded with text-embedding-3-small, reduced via UMAP, and clustered with HDBSCAN, yielding 101 denotative and 51 connotative clusters. Four coders qualitatively analyzed 85 cluster co-occurrence combinations (≥6 images) to thematic saturation. Monthly post volumes (Jan 2017–Sep 2024) were modeled with two-sample tests, interaction-term regression, and structural break detection, using ChatGPT's launch as the intervention.

## Findings

- Aspirational wealth and hyper-masculine status motifs appeared in ~55% of analyzed cluster combinations; transactional "trust proof" visuals (receipts, cash-out screenshots) in ~37%.
- Persuasion drivers were typically layered within single images, combining aspirational fantasy, transactional proof, urgency, gamified low-barrier entry, celebrity endorsements (e.g., Manny Pacquiao), and exploitation of family/social ties.
- Cultural localization was pronounced: an Urdu-language cluster embedded gambling within conservative moral narratives featuring women in distress and family conflict, while Filipino-language content used local celebrity registers.
- Mean monthly posts rose from 2,121 pre-ChatGPT to 280,952 post-ChatGPT (a 13,242% increase); regression confirmed both a level shift and a steep slope change (p<0.0001), with a structural break in July 2023.
- Post-2022 imagery exhibited consistent generative-AI stylistic markers — hyper-real lighting, smoothed surfaces, dreamlike saturation, improbable juxtapositions (e.g., sharks with slot machines) — and AI-generated characters that sidestep influencer accountability.
- Two emblematic AI-generated posts reached 4.3M and 3.3M views with thousands of cross-group shares, indicating substantial algorithmic amplification.

## Connections

This paper builds directly on the authors' prior work on coordinated link-sharing detection and CIB methodology ([[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]]), extending that infrastructure from political to commercial-harm contexts. It connects to broader research on AI-generated imagery in influence and propaganda campaigns ([[Achmann-Denkler2026-lx]], [[DiGiuseppe2026-pu]], [[Stanusch2026-ec]], [[Goel2025-iq]]) and to studies treating generative AI as an industrial accelerant of coordinated activity rather than a qualitatively new threat ([[Luceri2025-tr]], [[Gerard2025-br]], [[Yang2025-iv]]). Methodologically, its VLM-plus-embedding-plus-clustering pipeline for large-scale visual analysis resonates with emerging multimodal approaches in the same register ([[Kansaon2025-id]], [[Minici2024-tf]]).

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3)
