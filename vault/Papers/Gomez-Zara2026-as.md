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
podcast_url: 
pdf_available: true
discovery_date: 2026-09-18T05:02:06.195754Z
---

# Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis

> Gómez-Zará, D., Valdivieso, H., Pérez, J., Parra, D., & Valenzuela, S. (2026). Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis. *Digital Journalism*, 1–19. https://doi.org/10.1080/21670811.2026.2730327
>
> [View paper](https://doi.org/10.1080/21670811.2026.2730327)

## Summary

This methods paper argues for repositioning large language models in deductive content analysis: rather than treating LLMs as automated classifiers or coder substitutes, the authors propose using them as **analytic collaborators** ("augmentative interlocutors") that help researchers build, interrogate, and refine theory-grounded framing codebooks. The core insight is that applying rigid, theory-derived codebooks to large, heterogeneous, evolving news corpora inevitably surfaces ambiguities and borderline cases that theory alone cannot resolve. The authors present a structured workflow—"The LLM Codebook Prompt"—in which the model externalizes decision rules, surfaces latent frames, and supports iterative revision, while human researchers retain interpretive authority. The value proposition is explicitly methodological creativity and theoretical clarity, *not* scalability or efficiency.

## Key Contributions

- A reproducible, seven-phase, theory-facing workflow integrating corpus-level pattern surfacing with iterative, explanation-driven codebook refinement.
- A conceptual reframing of human–LLM disagreement as *productive* analytic material rather than error—disagreements expose implicit theoretical assumptions.
- A concrete prompt template and methodological recommendations requiring no model training or fine-tuning, usable with commercial or open-source LLMs.
- A worked case study on Chilean (Latin American) news coverage, showing how the workflow adapts frameworks to new cultural and temporal contexts.
- Explicit articulation of limitations, biases, and validation practices to preserve reflexivity and reproducibility.

## Methods

The paper is primarily conceptual, structured around a seven-phase workflow: (1) establishing theoretical boundaries, (2) broad corpus exposure/pattern surfacing, (3) selection of representative and borderline cases, (4) initial codebook prompt and application, (5) analytic interrogation and criteria elicitation, (6) codebook refinement and theoretical clarification, and (7) stabilization, scaling, and validation. Prompt engineering guidance emphasizes role instructions, theory-referenced frame definitions, positive/negative few-shot examples, justification-requesting questions, and structured outputs. The case study applies the workflow to over 3,400 Chilean news articles coded with Semetko & Valkenburg's four generic frames (conflict, economic consequences, human interest, morality), using ChatGPT 5.2 for exploration (prompts in Spanish) and a large-scale validation comparing GPT-5 mini against human ground-truth labels and against random, Naive Bayes, and TF-IDF Random Forest baselines.

## Findings

- "Conflict" was the most frequent frame in the Chilean corpus, followed by "responsibility"; "morality" was rarely explicit and often diluted within other frames.
- The LLM surfaced latent frames beyond the original framework—security and order, exceptional/rare events, and risk and emergency events.
- Systematic human–LLM divergences revealed implicit assumptions: human coders labeled inherently ethical issues (abuse, corruption) as moral without explicit normative language, while the LLM required explicit moral judgment per definition; similar patterns arose for human interest and economic consequences.
- Borderline cases (sports-as-conflict, tsunami alerts as human interest, an iCloud privacy leak as morality) forced explicit theorization of frame boundaries.
- Not all LLM-suggested distinctions were adopted—treating sensational language as a separate frame was rejected as conflating style with framing.
- GPT-5 mini achieved competitive validation performance (conflict F1 ~.71, economic F1 ~.71, human interest F1 ~.54, morality F1 ~.56), broadly comparable to the TF-IDF baseline; metrics were reported for transparency rather than optimization.

## Connections

This paper sits in the broader stream of work validating LLMs against human coders for text classification, engaging directly with efforts like [[Gilardi2026-hw]] and [[Le-Mens2025-qz]], but distinguishes itself by rejecting benchmark-oriented framing in favor of a dialogic, human-in-the-loop refinement process. Its concern with theoretical boundaries, reliability, and reflexive validation resonates with methodological cautions raised in [[Balluff2026-if]] and [[Tornberg2026-lc]], while its focus on frame and narrative analysis connects to related content-analytic applications such as [[Marino2026-slef]] and [[Kasianenko2026-tn]].
