---
title: "Conversational AI shifts beliefs and policy support among skeptics across contested societal issues"
aliases: ["Conversational AI shifts beliefs and policy support among skeptics across contested societal issues"]
authors: ["Johannes Kotz", "Kevin E. Tiede", "Jelena Meyer", "Maj-Britt Sterba", "Christian Breunig", "Wolfgang Gaissmaier"]
year: 2026
doi: 10.31234/osf.io/7szrn_v1
bibtex_key: Kotz2026-lk
topics: [generative-ai-disinformation, ai-social-theory-trust]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31234/osf.io/7szrn_v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kotz2026-lk.mp3
pdf_available: true
discovery_date: 2026-07-12T06:36:29.875622Z
---

# Conversational AI shifts beliefs and policy support among skeptics across contested societal issues

> Kotz, J., Tiede, K. E., Meyer, J., Sterba, M., Breunig, C., & Gaissmaier, W. (2026). Conversational AI shifts beliefs and policy support among skeptics across contested societal issues. https://doi.org/10.31234/osf.io/7szrn_v1
>
> [View paper](https://doi.org/10.31234/osf.io/7szrn_v1)

## Summary

This large-scale preregistered experiment (N = 6,558 U.S. participants) tested whether brief, interactive dialogues with GPT-5 can shift beliefs and policy support across three structurally distinct contested issues: climate change, vaccination, and economic inequality. Compared to a neutral control conversation (cats vs. dogs), AI dialogues consistently moved beliefs and increased support for contested policy instruments such as carbon and estate taxes. Crucially, effects were *strongest* among initially skeptical participants — the audience typically hardest to reach — and among those with higher trust in science. Text analysis of the dialogues showed GPT-5 systematically adapting its persuasive strategy to skeptics. The authors argue that short evidence-grounded AI dialogues could serve as a scalable, domain-general tool for public communication, while flagging associated governance and misuse concerns.

## Key Contributions

- Demonstrates **cross-domain generalizability** of conversational AI persuasion across three theoretically distinct issues within a single unified experiment.
- Extends the evidence base from beliefs to **concrete, politically contested policy instruments** (carbon tax, estate tax, mandatory vaccination), showing belief change does not automatically translate to policy change.
- Provides systematic evidence on **effect heterogeneity**, identifying skeptics and high-trust-in-science individuals as most movable, with trust in science as the key moderator.
- Characterizes and codes the **persuasive strategies** GPT-5 uses and how it adapts them to recipients' baseline positions, via a reproducible text-analysis pipeline.
- Offers a low-effort, single-prompt, adaptable tool for evidence-based communication alongside explicit ethical caveats.

## Methods

- Preregistered online experiment fielded December 2025–January 2026; N = 6,558 after exclusions, with a deliberate conservative oversample to ensure baseline attitude variation.
- Ten conditions: 3 topics × 3 intervention types (belief, policy, combined) plus a neutral control; three-round interactive GPT-5 dialogue with minimum time-on-task and forced responses to enforce engagement.
- Outcomes on 0–100 sliders measured pre/post: validated multi-item scales for climate belief and vaccine confidence, single items for inequality belief and the three policies.
- Moderators: actively open-minded thinking, trust in science, trust in AI, trust in government, demographics, party.
- Six multiple regressions (controlling baseline + AOT, with interaction terms), Bonferroni correction, within-subject mixed-effects models comparing targeted vs. non-targeted outcomes, and exploratory coding of 11 distinct persuasive strategies (88.5% reproducibility).

## Findings

- All interventions raised beliefs and policy support in their target domains, with the largest effects where baselines were lowest (inequality belief +6.36 pps; estate tax +8.98 pps).
- Climate belief rose 3.46–3.66 pps; carbon tax support rose up to 4.80 pps, with a smaller belief-driven spillover (+1.94 pps).
- Vaccination effects were smaller (reflecting high baselines); mandatory-vaccination support changes did not survive correction.
- Directly targeting the specific outcome worked best; combined interventions rarely outperformed outcome-specific ones.
- Treatment effects grew as baseline attitudes declined, beyond regression-to-the-mean expectations — greatest impact among **skeptics**.
- Trust in science roughly doubled effects at +1 SD; trust in AI showed a weaker trend; trust in government was inconsistent; AOT did not reliably moderate.
- No partisan difference in treatment effect once baselines were controlled, though Republicans had lower baseline attitudes.
- GPT-5 used prebunking/debunking and steelmanning more with skeptics and bridging-to-commitment more with supporters — systematic adaptation to skepticism.

## Connections

This paper directly extends the LLM-dialogue persuasion paradigm exemplified by [[Costello2024-bg]] on durably reducing conspiracy beliefs, generalizing it across multiple contested domains and to concrete policy attitudes. It relates to work on AI-based interventions against misinformation and climate skepticism such as [[DeVerna2025-dl]] and [[Spampatti2026-kx]], and its emphasis on trust-in-science moderation connects to the inoculation and belief-updating literature represented by [[van-der-Linden2026-jt]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kotz2026-lk.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
