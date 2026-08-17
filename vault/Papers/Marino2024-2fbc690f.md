---
title: "Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline"
aliases: ["Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline"]
authors: ["Giada Marino", "Fabio Giglietto"]
year: 2024
doi: 10.6092/issn.1971-8853/19524
bibtex_key: Marino2024-2fbc690f
kind: own
topics: [llms-in-content-analysis, italian-electoral-communication]
citation_count: 12
open_access: true
source_url: https://doi.org/10.6092/issn.1971-8853/19524
podcast_url: 
pdf_available: true
discovery_date: 
---

# Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline

> Marino, G., & Giglietto, F. (2024). Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline. *Sociologica*. https://doi.org/10.6092/issn.1971-8853/19524
>
> [View paper](https://doi.org/10.6092/issn.1971-8853/19524)

## Summary

This methodological essay documents the design and validation of an "LLMs-in-the-loop" pipeline for studying political content circulated on Facebook during the 2018 and 2022 Italian general elections. The authors embed OpenAI models at three distinct stages — a fine-tuned GPT-3 Curie binary political classifier, GPT-based embeddings feeding k-means clustering, and GPT-4-turbo cluster labeling — and argue that such fully LLM-integrated workflows require bespoke, task-specific validation protocols rather than a single overarching evaluation. Reflecting on their experience, they identify three core validation challenges: the general-purpose nature of LLMs, the highly variable granularity of LLM-generated narratives, and the difficulty of recruiting human evaluators competent enough to assess model outputs.

## Key Contributions

- An end-to-end, reproducible LLMs-in-the-loop pipeline (classification → embedding → clustering → labeling) applied to a non-English (Italian) political discourse corpus.
- A three-phase, task-specific validation protocol with publicly released codebooks for cluster coherence and label accuracy.
- Explicit articulation of three validation challenges — LLM general-purposeness, narrative granularity, and limits of human assessment — with practical mitigations.
- Reusable annotation guidelines and prompt templates for researchers adopting similar workflows.
- A methodological argument that early, competent adoption of LLMs by political communication scholars is itself a form of defense against their misuse.

## Methods

The pipeline processes 84,874 Italian-viewed URLs from the Meta URL Shares Dataset (2018 and 2022 elections), using only titles and descriptions. A fine-tuned GPT-3 Curie classifier was trained on 3,800 URLs coded by seven Italian political communication scholars (Krippendorff's α = 0.812). After comparing embedding models (ada-002, e5-mistral-7b-instruct, text-embedding-3-large) and clustering algorithms (k-means, DBSCAN, HDBSCAN, GenieClust, Kwikbucks), the authors settled on text-embedding-3-large plus Lloyd's k-means over 3,072-dimensional vectors, with Bayesian optimization (Silhouette, Hplus) selecting 199 clusters for 2018 and 198 for 2022. Clusters were labeled by GPT-4-turbo with engineered prompts and density-based sampling (~84% coverage per cluster). Validation proceeded in three phases: standard precision/recall/F1 for the classifier; pairwise cluster coherence on a 0–4 scale (plus "uncertain") by six expert coders; and cluster-label accuracy on a three-level scale across four criteria (thematic alignment, implications, content coverage, contextual alignment).

## Findings

- Classifier performance: F1 = 0.897, precision = 0.911, recall = 0.883 on held-out data.
- 54% of 2018 URLs (27,487) and 53% of 2022 URLs (8,308) were flagged as political.
- text-embedding-3-large outperformed rival embedding models on internal clustering metrics for Italian political news.
- Cluster granularity spanned broad policy domains to single news stories, motivating a multi-level coherence rubric.
- Crowdsourced annotators (e.g., Fiverr) were rejected because LLMs surpass them on nuanced political-context tasks; PhD-level expert coders were used.
- Labeling 397 clusters across both elections cost roughly $30 in API fees, underscoring affordability.

## Connections

This paper sits within the methodological turn toward LLM-assisted computational social science, sharing concerns about validation, expert-vs-crowd annotation, and pipeline reliability with [[Alizadeh2026-es]], [[Le-Mens2025-qz]], and [[Tornberg2025-ir]]. Its substantive focus on Italian election discourse on Facebook links it directly to the authors' broader research program on problematic information and coordinated sharing during Italian campaigns, notably [[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], [[Giglietto2024-cbeb3f70]], [[Giglietto2023-fa71a001]], [[Giglietto2020-9d8acdd7]], and [[Giglietto2019-882f1900]]. The narrative-clustering agenda also resonates with work using LLMs to map political content and stories such as [[Votta2025-xz]] and [[Balluff2026-if]].
