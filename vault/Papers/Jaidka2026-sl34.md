---
title: "The Elite Effect: Blocking Political Leaders on X Decreases Misinformation Susceptibility and Low-credibility Content Sharing"
aliases: ["The Elite Effect: Blocking Political Leaders on X Decreases Misinformation Susceptibility and Low-credibility Content Sharing"]
authors: ["Kokil Jaidka", "Yphtach Lelkes", "Subhayan Mukerjee", "Harshit Aneja"]
year: 2026
doi: 10.21203/rs.3.rs-9347980/v1
bibtex_key: Jaidka2026-sl34
kind: team
submitted_by: "GiadaM. / Uniurb"
slack_permalink: https://minesmd.slack.com/archives/C0BDU82EBHQ/p1782741616256159
topics: [information-disorder, platform-governance-data-access]
citation_count: 0
open_access: false
source_url: https://doi.org/10.21203/rs.3.rs-9347980/v1
podcast_url: 
pdf_available: true
discovery_date: 2026-06-29T14:16:49.161905Z
---

# The Elite Effect: Blocking Political Leaders on X Decreases Misinformation Susceptibility and Low-credibility Content Sharing

> Jaidka, K., Lelkes, Y., Mukerjee, S., & Aneja, H. (2026). The Elite Effect: Blocking Political Leaders on X Decreases Misinformation Susceptibility and Low-credibility Content Sharing. https://doi.org/10.21203/rs.3.rs-9347980/v1
>
> [View paper](https://doi.org/10.21203/rs.3.rs-9347980/v1)

## Summary

This preregistered month-long field experiment tests whether reducing the visibility of political elites in X feeds improves users' epistemic outcomes. The authors built Twilly, a custom mobile X client that filters live timelines client-side while preserving users' follow networks, and randomly assigned 1,214 U.S. participants to a control feed, an Elite Blocking condition (hiding elite-authored posts), or an Elite Scrubbing condition (also hiding posts that mention elites). Both interventions substantially cut exposure to and resharing of low-credibility and highly partisan content, improved factual political knowledge, and reduced susceptibility to text and multimodal misinformation — while leaving affective polarization, media trust, and news avoidance unchanged. The authors argue that misinformation is better understood as a problem of exposure architecture centered on elites than as a problem of individual susceptibility.

## Key Contributions

- Provides causal evidence that elite visibility itself — distinct from political content exposure broadly — drives misinformation susceptibility and low-credibility resharing.
- Separates elites-as-creators from elites-as-objects-of-discussion by contrasting Blocking vs. Scrubbing, showing elite-referential discourse adds further amplification of low-credibility content.
- Introduces Twilly, a platform-independent client-side methodology for live-feed manipulation that holds follow networks constant and works without platform cooperation.
- Reframes misinformation interventions away from bottom-up individual literacy toward top-down structural changes in who is rendered visible.
- Identifies elite-visibility filtering as an actionable, relatively unobtrusive content-moderation design lever (only 23% of treated users noticed any change).

## Methods

A preregistered three-arm field experiment (Sept–Dec 2024) with baseline (N=1,214) and endline (N=648) surveys bracketing a one-month exposure intervention delivered via the Twilly mobile X client. Elites were identified using updated ideology estimates from Barberá (2015) and Mukerjee et al. (2022); low-credibility content via standard domain ratings; partisan content via |ideology| > 0.3. Outcomes were estimated via linear regression with baseline and demographic covariates, plus 2SLS instrumental-variable models using random assignment as an instrument for actual elite exposure. Compliance was tracked via app logs.

## Findings

- Daily tweet volume fell sharply (e.g., 586 → 350 for left-leaning users under Scrubbing), but the share of political content remained roughly stable.
- Low-credibility content viewed dropped ~5.8–5.9 pp; partisan content viewed dropped ~13.7–14.0 pp under both conditions.
- Retweeting of partisan content fell ~20 pp under both conditions; retweeting of low-credibility content fell 6.79 pp under Elite Blocking.
- Effects concentrated on first-degree (followed-account) exposure; Scrubbing further reduced low-credibility exposure beyond Blocking (~3.2 pp).
- International news knowledge rose 0.48 SD (Blocking) and 0.32 SD (Scrubbing); national knowledge rose ~0.24–0.28 SD.
- Misinformation susceptibility fell across formats: political rumors ~−0.42 SD, multimodal misinformation ~−0.66 to −0.68 SD, and overconfidence in judgments ~−0.34 to −0.39 SD.
- No detectable effects on affective polarization, perceived partisan threat, social distance, institutional or media trust, or news avoidance.
- Only 23% of treated participants noticed feed changes, suggesting interventions are unobtrusive.

## Connections

This study sits within a recent wave of platform-independent field experiments and exposure-architecture analyses of misinformation, complementing [[Allen2025-ot]] on what people actually see online and [[Gonzalez-Bailon2024-rq]] and [[Bakshy2015-rn]] on algorithmic curation of political exposure. Its top-down, elite-centered framing connects to elite-driven misinformation dynamics documented in [[Mosleh2024-op]], [[DeVerna2025-dl]], and [[Budak2024-ef]], and contrasts with bottom-up susceptibility approaches like inoculation studied by [[van-der-Linden2026-jt]] and [[Lewandowsky2026-ob]]. The Twilly methodology resonates with other client-side and donation-based exposure studies such as [[Bouchaud2026-lr]] and [[Pierri2025-hm]] amid restricted API access.
