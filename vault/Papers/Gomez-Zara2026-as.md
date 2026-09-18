---
title: "Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis"
aliases: ["Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis"]
authors: ["Diego Gómez-Zará", "Hernán Valdivieso", "Jorge Pérez", "Denis Parra", "Sebastián Valenzuela"]
year: 2026
doi: 10.1080/21670811.2026.2730327
bibtex_key: Gomez-Zara2026-as
topics: [generative-ai-content-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/21670811.2026.2730327
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gomez-Zara2026-as.mp3
pdf_available: true
discovery_date: 2026-09-18T05:02:06.195754Z
---

# Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis

> Gómez-Zará, D., Valdivieso, H., Pérez, J., Parra, D., & Valenzuela, S. (2026). Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis. *Digital Journalism*, 1–19. https://doi.org/10.1080/21670811.2026.2730327
>
> [View paper](https://doi.org/10.1080/21670811.2026.2730327)

## Summary

This methods paper argues that large language models are most useful in deductive content analysis not as automated classifiers but as *analytic collaborators*—"augmentative interlocutors" that help researchers build, interrogate, and refine theory-grounded framing codebooks. The authors observe that applying fixed codebooks to large, heterogeneous, and evolving news corpora inevitably exposes ambiguities and borderline cases that theory alone cannot resolve. Their workflow, called "The LLM Codebook Prompt," treats these frictions as productive: by requiring the model to justify its classifications, its outputs become analytic material that surfaces latent frames and implicit theoretical assumptions, while researchers retain final interpretive authority. The approach is illustrated with a case study of Chilean news coverage coded using Semetko and Valkenburg's four generic frames.

## Key Contributions

- A reproducible, theory-facing seven-phase workflow integrating corpus-level pattern surfacing with iterative, explanation-driven codebook refinement.
- A reframing of LLM–human disagreement and revision as productive analytic moments that expose conceptual ambiguity and enforce theoretical accountability.
- A concrete prompt template requiring no fine-tuning, usable with commercial or open-source models.
- A worked Latin American (Chilean) case study showing how the workflow adapts frameworks to new cultural and temporal contexts.
- An explicit articulation of limitations, biases, and validation practices to preserve reflexivity and reproducibility.

## Methods

The core is a conceptual, step-by-step workflow spanning seven phases: establishing theoretical boundaries, broad corpus exposure and pattern surfacing, selecting representative/borderline cases, initial codebook prompting and application, analytic interrogation and criteria elicitation, codebook refinement and theoretical clarification, and stabilization/scaling/validation. Prompt-engineering guidance covers role instructions, theory-referenced frame definitions, few-shot positive/negative examples, framing questions demanding justifications, and structured output. The case study applies the workflow to over 3,400 Chilean news articles coded with four generic frames (conflict, economic consequences, human interest, morality), using ChatGPT 5.2 for exploration and coding (prompts in Spanish, scripts on OSF). A large-scale validation compares GPT-5 mini classifications against human-annotated ground truth using accuracy, precision, recall, and F1, benchmarked against random, Naive Bayes, and a TF-IDF Random Forest baseline.

## Findings

- The LLM identified "conflict" as the most frequent frame, followed by "responsibility," with "morality" rarely explicit and often diluted into other frames.
- It surfaced latent frames beyond the original framework—security and order, exceptional/rare events, and risk and emergency events.
- Systematic human–LLM divergences exposed implicit assumptions: human coders treated inherently ethical issues (abuse, corruption) as moral without explicit normative language, while the LLM required explicit moral judgment per the definition; similar patterns appeared for human interest and economic consequences.
- Borderline cases (sports as conflict, tsunami alerts as human interest, an iCloud privacy leak for morality) forced explicit theorization of frame boundaries.
- Not all suggested distinctions were adopted—treating sensational language as a separate frame was rejected as conflating style with framing.
- GPT-5 mini reached competitive validation performance (conflict F1 ≈.71, economic ≈.71, human interest ≈.54, morality ≈.56), broadly comparable to the TF-IDF baseline; metrics were reported for transparency rather than optimization.

## Connections

This paper's dialogic, human-in-the-loop stance contrasts sharply with benchmarking-oriented work that positions LLMs as scalable annotators, such as [[Gilardi2026-hw]] and [[Le-Mens2025-qz]], and it engages the broader question of LLM validity and reliability in text classification explored in [[Balluff2026-if]] and [[Tornberg2026-lc]]. Its concern with frame identification and codebook construction also resonates with framing- and coding-oriented studies like [[Achmann-Denkler2026-lx]] and [[Waight2026-ts]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gomez-Zara2026-as.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
