---
title: "Generative AI, large language models, and their agentic framing in news media"
aliases: ["Generative AI, large language models, and their agentic framing in news media"]
authors: ["Dennis Nguyen", "Magdalena Wischnewski"]
year: 2026
doi: 10.1007/s00146-026-03070-1
bibtex_key: Nguyen2026-vm
topics: [generative-ai-and-llms]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1007/s00146-026-03070-1
podcast_url: 
pdf_available: true
discovery_date: 2026-05-15T05:52:01.125136Z
---

# Generative AI, large language models, and their agentic framing in news media

## Summary

This paper investigates how English-language news media linguistically construct large language models (LLMs) and generative AI, with a particular focus on *mentalistic-agentic framings* that ascribe human-like cognition to these systems. Drawing on a corpus of 18,032 articles from 15 outlets across Europe, Asia, the Middle East, and North America (2022–2024), Nguyen and Wischnewski combine BERTopic modeling, dependency parsing, dictionary-based detection, and manual coding to map thematic emphases and detect anthropomorphic language at the sentence level. Their central argument is that while mentalistic framings exist, they are neither dominant nor monolithic: anthropomorphism in AI journalism serves diverse rhetorical functions — from uncritical amplification of corporate narratives to explanatory simplification and adversarial critique — and varies more by editorial style than by region.

## Key Contributions

- A fine-grained, sentence-level analysis of LLM-specific (not AI-broadly) framing in news discourse.
- An empirically grounded reframing of the anthropomorphism debate: mentalistic language is not inherently hype-laden and can function critically.
- A cross-cultural comparison testing whether AI imaginaries are globally uniform or regionally differentiated.
- A replicable mixed-methods pipeline integrating BERTopic, dependency parsing, the Mind Perception Dictionary, and manual coding.
- A contribution to debates on AI imaginaries, public epistemology, and journalism's role in cultivating critical AI literacy.

## Methods

The authors retrieved 18,032 articles via Nexis and preprocessed them in Python using SpaCy's transformer model. BERTopic was run 20 times for robustness (mean pairwise Jaccard = 0.75), yielding a 316-cluster solution inductively grouped into 24 meta-frames. A regex classifier identified 1,631 LLM-centric articles (>95% validation accuracy). Dependency parsing extracted 2,188 sentences with LLMs in subject position, which were manually coded for agentic framing (Krippendorff's α = 0.76) and for mentalistic/experiential framing using Schweitzer et al.'s Mind Perception Dictionary (α = 0.78). Word2Vec embeddings explored semantic neighborhoods around model names, and chi-square / Cramér's V tests assessed framing variation across outlets and regions.

## Findings

- AI articles are a small but growing share of news output (e.g., 0.9% at NYT); coverage spiked around ChatGPT's launch.
- A techno-capitalist master frame dominates globally; European/North American outlets emphasize risk and ethics, while Asian outlets emphasize education, applications, and industry (χ²(46)=1399.64, p<0.001).
- Only 9.2% of AI articles are LLM-centric, with ChatGPT mentioned in 82.5%, vastly overshadowing Gemini/Bard (15.7%), Claude (2.5%), and Mistral (1%).
- 45.5% of LLM articles use agentic framing, but only 8.8% (0.8% of the full corpus) deploy explicitly mentalistic framings; no experiential/emotional framings appeared.
- Mentalistic framings vary significantly by outlet (NYT, Straits Times, AFP over-represented) but *not* by region.
- Negated agency constructions are rare (6.19%), suggesting explicit critical denials are uncommon.
- Anthropomorphic framings serve multiple rhetorical functions, including critique (e.g., chatbots described as "dumb" or "bullshitters").
- ChatGPT clusters semantically with education terms; Gemini/Bard clusters more around user interaction and "hallucination."

## Connections

This paper complements broader work on how journalism and public discourse construct generative AI, particularly [[Schiffrin_undated-gi]] on news framing of AI and [[Dierickx2026-tw]] on journalistic engagement with LLMs. Its critical stance toward anthropomorphism and AI hype resonates with [[Waight2025-al]] and [[Waight2026-ts]] on AI imaginaries, while its findings on LLM behavior and capability claims connect to empirical critiques of model performance such as [[Hackenburg2025-dj]] and [[DeVerna2025-dl]]. The methodological approach — mixed computational and manual coding of AI discourse — parallels work by [[Balluff2026-if]] and [[Achmann-Denkler2026-lx]].
