---
title: "“keep your heads held high boys!”: Examining the relationship between the Proud Boys’ online discourse and offline activities"
aliases: ["“keep your heads held high boys!”: Examining the relationship between the Proud Boys’ online discourse and offline activities"]
authors: ["CATIE SNOW BAILARD", "REBEKAH TROMBLE", "WEI ZHONG", "FEDERICO BIANCHI", "PEDRAM HOSSEINI", "DAVID BRONIATOWSKI"]
year: 2024
doi: 10.1017/s0003055423001478
bibtex_key: Bailard2024-pj
topics: [online-radicalization-far-right]
citation_count: 9
open_access: false
source_url: https://doi.org/10.1017/s0003055423001478
podcast_url: 
pdf_available: true
discovery_date: 2026-05-17T08:06:58.350298Z
---

# “keep your heads held high boys!”: Examining the relationship between the Proud Boys’ online discourse and offline activities

## Summary

This paper investigates whether and how the Proud Boys' online discourse on Telegram predicts their offline violent and nonviolent activity between January 2020 and July 2022. Drawing on collective action framing theory (Snow and Benford), the authors classify over 500,000 messages from 92 Proud Boys-affiliated channels into diagnostic, prognostic, and motivational frames using a fine-tuned DeBERTa model, then link these weekly time-series to ACLED event records. They argue that grievance-laden (diagnostic) and solidarity-building (motivational) speech—not explicit calls-to-action—predict subsequent offline violence, and that offline nonviolent protests feed back into online motivational framing, producing a roughly four-week reciprocal cycle that culminates in violent events.

## Key Contributions

- One of the first large-scale longitudinal studies empirically linking specific *types* of far-right online discourse to offline violent and nonviolent events.
- A fine-tuned DeBERTa classifier for collective action frames (macro F1 = 0.80), trained on 12,189 hand-annotated messages, moving beyond toxicity/hate-speech detection.
- Theoretical articulation of a reciprocal "online messaging–offline action cycle" linking protest participation to subsequent motivational framing and then to violence.
- Integration of moralizing and moral convergence theories with classical collective action framing to explain mobilization to violence.
- A critique of content-moderation paradigms that target only discrete hateful posts or explicit incitement, arguing they miss the more predictive grievance and solidarity discourse.
- Public release of classified data and code via the APSR Dataverse.

## Methods

The authors snowball-collected Telegram channels via the Telethon API, narrowing to a core network of 92 explicitly Proud Boys channels. Trained annotators hand-coded 12,189 messages (Gwet's AC ≈ 0.82) for diagnostic, prognostic, motivational, injustice, and othering frames; a fine-tuned DeBERTa model then classified the full corpus. Classified weekly counts were merged with 376 Proud Boys-involved ACLED events and analyzed with vector autoregression, Granger causality tests, and impulse response functions, with standard stationarity and lag-length diagnostics. Robustness checks included a regional first-difference TSCS analysis across 53 location-specific channels and a structural equation mediation model.

## Findings

- Diagnostic frames dominated the corpus (~34% of weekly posts); motivational frames were rarer (~9%) but highly consequential.
- Increases in diagnostic framing Granger-cause later offline violent events; injustice and othering subframes show weaker, marginally significant effects.
- Both the proportion and frequency of motivational frames predict subsequent violent events.
- Prognostic frames (explicit calls-to-action) do *not* predict either violent or nonviolent offline activity.
- Nonviolent protests predict increased motivational framing in following weeks; no other frame type responds this way.
- Impulse response analysis indicates a ~4-week cycle: nonviolent protest → motivational framing peak (~2 weeks) → violent event peak (~2 weeks later).
- SEM estimates that ~8% of the effect of nonviolent protests on later violent events runs through motivational framing.
- Regional analyses confirm motivational—but not diagnostic—framing predicts state-level violence.

## Connections

This work shares the broader project of mapping how far-right online ecosystems drive offline mobilization that animates [[Rothut2026-wt]] and [[Nangle2026-yo]], and its critique of post-level content moderation in favor of discursive-ecosystem analysis resonates with platform-governance concerns raised in [[Bouchafra2026-ts]]. Its emphasis on solidarity and grievance framing as more predictive than overt incitement offers a methodological complement to studies focused on radicalization pathways and identity construction in the same topic cluster.
