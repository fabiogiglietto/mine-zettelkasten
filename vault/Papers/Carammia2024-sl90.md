---
title: "Rethinking Scale: The Efficacy of Fine-Tuned Open-Source LLMs in Large-Scale Reproducible Social Science Research"
aliases: ["Rethinking Scale: The Efficacy of Fine-Tuned Open-Source LLMs in Large-Scale Reproducible Social Science Research"]
authors: ["Marcello Carammia", "Stefano Maria Iacus", "Giuseppe Porro"]
year: 2024
doi: 
bibtex_key: Carammia2024-sl90
kind: team
submitted_by: "Nicola Righetti"
slack_permalink: https://minesmd.slack.com/archives/C0BDU82EBHQ/p1791529563092019
topics: [llms-computational-content-analysis, platform-governance-data-access]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2411.00890v1
podcast_url: 
pdf_available: true
discovery_date: 2026-10-09T07:50:03.554454Z
---

# Rethinking Scale: The Efficacy of Fine-Tuned Open-Source LLMs in Large-Scale Reproducible Social Science Research

> Carammia, M., Iacus, S. M., & Porro, G. (2024). Rethinking Scale: The Efficacy of Fine-Tuned Open-Source LLMs in Large-Scale Reproducible Social Science Research.
>
> [View paper](http://arxiv.org/abs/2411.00890v1)

## Summary

This paper challenges the assumption that larger, proprietary LLMs are inherently superior for social science text classification. The authors argue that small, fine-tuned open-source models from Meta's LLAMA family — adapted using Low-Rank Adaptation (LoRA) — can match or exceed ChatGPT-4 on domain-specific classification tasks, while delivering transparency, reproducibility, data privacy, and dramatically lower cost. Beyond the empirical comparison, the paper proposes a hybrid human-AI workflow in which multiple LLMs generate candidate labels and human coders *reject* wrong ones rather than assign correct ones, exploiting cognitive tendencies (error salience, negativity bias) to accelerate labeled-data creation. The work positions itself squarely within the open-versus-closed foundation model debate in computational social science, responding to prior framings that treat open models as replicability-preserving but inferior.

## Key Contributions

- Empirical demonstration that fine-tuned small open-source LLMs can equal or surpass large black-box models, not merely serve as a "last resort."
- A reusable five-step hybrid human-AI workflow for accelerating labeled dataset creation, grounded in cognitive principles of error detection.
- An empirical observation linking fine-tuning efficacy to base-model pre-training corpus size: less-trained models (LLAMA-2, ~1.5T tokens) are easier to re-weight than heavily trained ones (LLAMA-3, ~15T tokens).
- Evaluation across three contrasting real-world tasks spanning noisy/unlabeled data, gold-standard political data, and highly curated metadata.
- A practical pathway for very large-scale analyses (e.g., 10B Geo-Tweet archives) that would be financially infeasible via commercial API pricing.

## Methods

The authors fine-tune LLAMA models (versions 2–3.2, sizes 1B–405B) using LoRA, and compare them against base LLAMA models and ChatGPT-4. Their proposed workflow comprises: (1) normalizing data into tabular form, (2) AI-crowd classification by multiple LLMs, (3) human approval by rejecting inapplicable labels, (4) fine-tuning a single LLM on the human-filtered set, and (5) scaling to unseen documents. Evaluation spans three datasets: 10,000 English tweets labeled across 46 Human Flourishing well-being dimensions (multi-label, noisy, no gold standard); European Parliament questions (1994–2021) into 19 Comparative Agendas Project policy areas (mutually exclusive, gold standard); and Harvard Dataverse datasets into 15 subject categories (multi-label, highly curated, 76,110 records). Metrics are chosen per task type (accuracy, precision, recall, specificity, balanced accuracy, F1, Hamming loss, Jaccard index), with three prompting strategies for the CAP task and human verification assessed via Cohen's/Fleiss kappa.

## Findings

- On the Human Flourishing tweet task, fine-tuned LLAMA2-7B matched or beat ChatGPT-4 across accuracy, Hamming loss, and Jaccard index; fine-tuning was less effective for base models pre-trained on more tokens.
- On CAP policy classification, fine-tuning LLAMA2-7B raised zero-shot accuracy from ~37% to ~75% (macro balanced accuracy ~86.4% vs. ChatGPT-4's 83.4%); the iterative ChatGPT-4 method reached ~75.8%.
- Certain CAP categories (Law and Crime, Regional/Urban, Banking/Finance) showed low sensitivity, with Banking/Finance frequently misclassified as Macroeconomics.
- On the Harvard Dataverse task, a fine-tuned LLAMA2-7B trained on just 5,000 records matched the base 70B model (~84.8% vs. 84.9%); extending training to 76,110 records raised accuracy to 94.6%.
- The large fine-tuned Dataverse model predicted exact correct categories (and count) 90.3% of the time, sometimes proposing additional plausible labels.
- Human coders disagree in roughly 15–20% of cases, undermining the traditional "gold standard" of human annotation reliability.

## Connections

This paper is a methodological anchor for the open-vs-closed debate in LLM-based content analysis, directly relevant to validation work such as [[Le-Mens2025-qz]] and other studies benchmarking LLM classification against human coding. Its concerns about reproducibility, cost, and the unreliability of human gold standards speak to the broader computational content-analysis literature on deploying LLMs for social science annotation at scale.
