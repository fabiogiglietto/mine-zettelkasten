---
title: "Conversational AI shifts beliefs and policy support among skeptics across contested societal issues"
aliases: ["Conversational AI shifts beliefs and policy support among skeptics across contested societal issues"]
authors: ["Johannes Kotz", "Kevin E. Tiede", "Jelena Meyer", "Maj-Britt Sterba", "Christian Breunig", "Wolfgang Gaissmaier"]
year: 2026
doi: 10.31234/osf.io/7szrn_v1
bibtex_key: Kotz2026-lk
topics: [llms-computational-methods, information-disorder]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31234/osf.io/7szrn_v1
podcast_url: 
pdf_available: true
discovery_date: 2026-07-12T06:36:29.875622Z
---

# Conversational AI shifts beliefs and policy support among skeptics across contested societal issues

> Kotz, J., Tiede, K. E., Meyer, J., Sterba, M., Breunig, C., & Gaissmaier, W. (2026). Conversational AI shifts beliefs and policy support among skeptics across contested societal issues. https://doi.org/10.31234/osf.io/7szrn_v1
>
> [View paper](https://doi.org/10.31234/osf.io/7szrn_v1)

## Summary

This preregistered experiment (N = 6,558 U.S. participants) tested whether short, interactive dialogues with GPT-5 could shift beliefs and policy support across three structurally distinct contested issues: climate change, vaccination, and economic inequality. Compared with a neutral control conversation (cats vs. dogs), a three-round AI dialogue advocating an evidence-based position moved beliefs in all three domains and increased support for concrete contested policies such as carbon and estate taxes. Effects were strongest among the participants usually hardest to reach — initial skeptics — and among those with higher trust in science, and text analysis showed GPT-5 systematically adapted its persuasive strategy to skepticism. The authors position AI dialogue as a scalable, domain-general tool for evidence-based public communication, while flagging its dual-use risks.

## Key Contributions

- Demonstrates **cross-domain generalizability** of conversational AI persuasion across three theoretically distinct issues within one unified experiment, rather than under favorable single-domain conditions.
- Extends AI persuasion from beliefs to **specific contested policy instruments** (carbon tax, estate tax, mandatory school-entry vaccination), showing belief change does not automatically translate into policy support.
- Provides systematic evidence on **heterogeneity of effects**, identifying skeptics and high-trust-in-science individuals as most movable and trust in science as the key moderator.
- Characterizes and quantifies the **persuasive strategies** GPT-5 deploys and how it adapts them to recipients' baseline positions, via a reproducible text-analysis pipeline.
- Offers a **low-effort, single-prompt, scalable tool** for evidence-based communication, while flagging transparency, grounding, and misuse-governance requirements.

## Methods

Large-scale preregistered online experiment fielded in December 2025–January 2026, with a deliberate oversample of conservatives to ensure baseline attitude variation. Participants were randomly assigned to one of ten conditions (3 topics × 3 intervention types — belief, policy, combined — plus a neutral control). The intervention was a three-round interactive GPT-5 dialogue prompted to advocate the target position using best available scientific evidence while inviting questions, with time minimums and forced responses to guarantee engagement. Outcomes were measured pre/post on 0–100 sliders using validated multi-item scales (climate belief ω = .97; vaccine confidence ω = .95) and single items for inequality belief and the three policies. Moderators included actively open-minded thinking, and trust in science, AI, and government. Analysis used regressions controlling for baseline and AOT with interaction terms (Bonferroni-corrected within outcome families), within-subject mixed-effects models comparing targeted vs. non-targeted outcomes, and exploratory coding of 11 distinct persuasive strategies (88.5% reproducibility check).

## Findings

- All interventions raised beliefs and policy support in their respective domains, with the largest effects where baselines were lowest (inequality belief +6.36 pps; estate tax support +8.98 pps).
- Climate belief rose ~3.5–3.7 pps and carbon-tax support ~3.7–4.8 pps, with a smaller belief-to-policy spillover (+1.94 pps).
- Vaccination effects were smaller (reflecting high baselines), and mandatory-vaccination support changes did not survive multiple-testing correction.
- Directly targeting the specific outcome worked best; combined belief+policy interventions generally did **not** outperform outcome-specific ones.
- Treatment effects grew as baseline attitudes fell — beyond what regression to the mean predicts — indicating **greatest impact among skeptics**.
- Trust in science roughly doubled effect sizes at +1 SD; trust in AI showed a weaker trend, trust in government was inconsistent, and AOT did not reliably moderate.
- No difference in treatment effects between Republicans and Democrats once baseline attitudes were controlled.
- GPT-5 leaned on iterative collaborative dialogue and person-centered alignment throughout, but used prebunking/debunking and steelmanning more with skeptics and bridging-to-commitment strategies more with supporters — systematic adaptation to the recipient.

## Connections

This paper builds directly on the emerging line of work using LLM dialogues to durably shift entrenched beliefs, most notably [[Costello2024-bg]] on conversations that reduce conspiracy beliefs, extending its logic from beliefs to contested policy attitudes and across multiple domains. It relates to the broader debate over AI persuasion capacity and its potential for influence operations examined in [[Goel2025-iq]] and [[Karo2026-dn]], and complements information-correction work such as [[DeVerna2025-dl]] by showing responsive dialogue can outperform static messaging with skeptical audiences.
