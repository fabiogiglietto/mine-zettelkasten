---
title: "Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"
aliases: ["Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"]
authors: ["Fabio Giglietto", "Massimo Terenzi", "Anwesha Chakraborty", "Giada Marino"]
year: 2026
doi: 10.1007/978-3-032-11782-3_4
bibtex_key: Giglietto2026-9b6a992d
kind: own
topics: [coordinated-inauthentic-behavior, generative-ai-llms-in-research]
citation_count: 3
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

This paper investigates visual persuasion in coordinated online gambling promotion on Facebook, analyzing over 2,300 images drawn from 223 coordinated public groups surfaced through the Vera AI project. Using a hybrid pipeline of vision-language models, embeddings, and density-based clustering, the authors build a typology of persuasive visual drivers and assess how generative AI has reshaped gambling promotion. Their central argument is that generative AI does not invent new persuasion strategies but intensifies and recombines established ones—aspirational wealth, manufactured trust, FOMO, cultural localization, and more—while enabling industrial-scale dissemination. They situate this growth as coinciding with ChatGPT's November 2022 launch and identify algorithmic amplification, together with a regulatory grey zone between Meta's strict paid-ad rules and permissive organic-content rules, as the core governance blind spot.

## Key Contributions

- An empirically grounded typology of visual persuasion drivers in coordinated *organic* gambling promotion.
- Evidence that generative AI acts as an accelerant and intensifier of existing persuasion architectures rather than a source of wholly new strategies.
- A reproducible mixed-methods pipeline combining VLM-based image description, dual denotative/connotative embeddings, density-based clustering, and human qualitative coding for large-scale visual analysis.
- Identification of Meta's regulatory asymmetry between paid and organic gambling content, and of algorithmic amplification as a governance blind spot.
- A reflexive critique of using LLMs both as analytical instruments and as the very technologies enabling the content under study.

## Methods

The authors identified 223 coordinated Facebook public groups via the Vera AI alerts workflow, which detects coordinated link-sharing (14-second window, 0.995 edge weight) seeded from accounts spreading fact-checker-flagged content. They collected 10,671 posts and 2,323 distinct images (2017–2024) through the Meta Content Library and a custom image-downloader. Each image was described denotatively and connotatively by gpt-4o, embedded via text-embedding-3-small, then reduced with UMAP and clustered with HDBSCAN (101 denotative, 51 connotative clusters). A co-occurrence matrix across 366 cluster combinations guided qualitative coding of 85 combinations by four coders. Monthly post volumes (2017–2024) were analyzed with two-sample tests, interaction-term regression, and structural break detection, using ChatGPT's launch as the intervention point, alongside qualitative pre/post comparison of AI-generation stylistic markers.

## Findings

- Aspirational wealth and hyper-masculine status motifs appeared in ~55% of analyzed cluster combinations; transactional "trust proof" visuals (receipts, cash-out screenshots) in ~37%.
- Identified drivers include aspirational wealth, manufactured trust, FOMO/urgency, gamification, celebrity endorsements (e.g., Manny Pacquiao), exploitation of social relations, and cultural/linguistic localization (Filipino, Urdu).
- The Urdu-language cluster used emotionally charged depictions of women in distress and traditional moral narratives to embed gambling within conservative cultural framings.
- Mean monthly posts rose from 2,121 (pre-ChatGPT) to 280,952 (post-ChatGPT)—a 13,242% increase—with a confirmed level shift, slope change (p<0.0001), and structural break in July 2023.
- Post-2022 visuals showed consistent AI-generation markers (hyper-real lighting, smoothed surfaces, dreamlike saturation, improbable juxtapositions like sharks with slot machines) and bundled multiple drivers in single images.
- Two emblematic AI-generated posts reached millions of views (4.3M and 3.3M) and thousands of shares across coordinated groups.

## Connections

This paper extends the authors' own program on coordinated link-sharing and inauthentic behavior detection, building directly on methods developed in [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], and [[Giglietto2024-cbeb3f70]], and sits alongside related coordination-focused work such as [[Nizzoli2020-cf]] and [[Marino2024-2fbc690f]]. Its focus on generative-AI aesthetics as an accelerant of persuasive content connects it to broader studies of synthetic media and AI-enabled influence operations, including [[Gerard2025-br]] and [[DeVerna2025-dl]]. The reflexive use of LLMs as both analytical tool and object of study also resonates with methodological work on generative AI in research like [[Gilardi2026-hw]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3)
