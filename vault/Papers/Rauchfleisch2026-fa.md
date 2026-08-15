---
title: "Toward meaningful transparency for AI chatbots: Disclosing persuasive intent reduces persuasion"
aliases: ["Toward meaningful transparency for AI chatbots: Disclosing persuasive intent reduces persuasion"]
authors: ["Adrian Rauchfleisch", "Andreas Jungherr"]
year: 2026
doi: 
bibtex_key: Rauchfleisch2026-fa
topics: [generative-ai-disinformation, ai-social-theory-trust]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2608.11794v1
podcast_url: 
pdf_available: true
discovery_date: 2026-08-15T07:33:16.092542Z
---

# Toward meaningful transparency for AI chatbots: Disclosing persuasive intent reduces persuasion

> Rauchfleisch, A., & Jungherr, A. (2026). Toward meaningful transparency for AI chatbots: Disclosing persuasive intent reduces persuasion. *arXiv [cs.CY]*.
>
> [View paper](http://arxiv.org/abs/2608.11794v1)

## Summary

This preregistered experiment tests a distinction that has become central to AI governance: does disclosing *that* a system is AI meaningfully protect people from persuasion, or must transparency also reveal *what the system is trying to do*? Using an identical persuasive chatbot conversing with 1,500 UK adults about randomly assigned policy issues, the authors compare a no-disclosure control, an EU AI Act Article 50-style AI-identity label, and a condition that additionally discloses the chatbot's persuasive intent and verbatim instructions. The AI-identity label leaves persuasion essentially untouched, while intent disclosure roughly halves it. The core argument is that covert AI influence is objectionable because of concealed *purpose*, not machine authorship, so meaningful transparency must target intent — a logic closer to political-advertising regulation than to content-authenticity labeling.

## Key Contributions

- First direct experimental comparison of an Article 50(1)-style AI-identity disclosure against an intent-plus-instructions disclosure inside a live persuasive chatbot interaction.
- Empirical demonstration that AI-identity labeling has minimal effect on persuasion in direct chatbot conversations, extending prior nulls from static AI-generated messages.
- Introduces and validates "meaningful transparency of intent" as a policy-relevant alternative grounded in the logic of Regulation (EU) 2024/900 on political advertising.
- Documents a deployer-side tradeoff: intent disclosure suppresses persuasion but provokes penalties against the campaign and its sponsor.
- Provides preregistered, robustness-checked evidence directly comparable to prior conversational-persuasion work.

## Methods

A three-arm online experiment (control, AI-label T1, AI-label-plus-intent T2) with 1,500 Prolific-recruited UK adults, quota-sampled on sex, age, and party, fielded before Article 50 became applicable. Participants reported an initial attitude on one of 60 persuadable UK policy stances, held a 2–6 turn conversation with an identical persuasive chatbot (gpt-5.6-terra), then reported post-attitudes and outcomes including warmth, perceived manipulation, persuasion knowledge, anger, counterarguing, campaign acceptability, and sponsor penalty. Crucially, the chatbot and server never received the experimental condition — only the survey-platform disclosure varied. Analysis used preregistered linear mixed models with random intercepts for policy issue, Holm correction, and TOST equivalence tests (±3.7 points for persuasion). Supplementary work included AI-text-detection checks, IV/complier analyses, behavioral disagreement traces, and a fact-checking pipeline.

## Findings

- Attitudes shifted 12.6 points (control) and 13.1 points (T1); the T1–control difference fell within the ±3.7-point equivalence region (pTOST = .002), confirming the AI label did not meaningfully reduce persuasion.
- The AI label did not significantly change warmth, perceived manipulation, or persuasion knowledge.
- Intent disclosure (T2) cut persuasion by ~6.8 points versus both control and T1 (to a 6.3-point shift), with a protective effect for all 60 issues.
- T2 most strongly raised persuasion knowledge (d = 0.49), increased perceived manipulation and counterarguing, and rated the chatbot ~5 points colder.
- Anger stayed near the scale floor across arms — responses were cognitive, not emotional.
- T2 participants judged the campaign's methods less acceptable and supported stronger sponsor penalties; the AI label did not trigger such penalties.
- The label conveyed little new information: 98–99% across all arms (including control) already identified their partner as an AI chatbot.
- Persuasion rested largely on accurate content: ~2.01 factual claims per message, 95.7% accurate.

## Connections

The design and comparability of this study are built directly on prior conversational-persuasion work, making it a close companion to [[Hackenburg2025-dj]] and [[Hackenburg2026-ud]] on the persuasive power of LLMs. Its finding that persuasion operated through accurate rather than deceptive information distinguishes it from misinformation-focused debates and connects to [[Costello2024-bg]] on dialogue-based attitude change. As an empirical intervention in transparency and disclosure regulation, it also speaks to work on AI's role in political communication and trust such as [[Gilardi2026-hw]].
