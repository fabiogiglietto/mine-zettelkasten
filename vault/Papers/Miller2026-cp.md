---
title: "Community-driven API and AI writer design for openly scaling Community Notes"
aliases: ["Community-driven API and AI writer design for openly scaling Community Notes"]
authors: ["Brad Miller", "Jay Baxter", "Jiansong Chao", "Keith Coleman", "Sophie Hilgard", "Daniel Ortiz"]
year: 2026
doi: 
bibtex_key: Miller2026-cp
topics: [generative-ai-and-synthetic-media, platform-governance-data-access]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2609.40067v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Miller2026-cp.mp3
pdf_available: false
discovery_date: 2026-10-16T13:48:42.353889Z
---

# Community-driven API and AI writer design for openly scaling Community Notes

> Miller, B., Baxter, J., Chao, J., Coleman, K., Hilgard, S., & Ortiz, D. (2026). Community-driven API and AI writer design for openly scaling Community Notes. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2609.40067v1)

## Summary

This paper describes the design and September 2025 deployment of X's AI Note Writer API, an open public interface that allows AI systems to propose Community Notes at scale. The central design commitment is that AI and the platform generate *candidates* only — human users, through their contributions and ratings, remain the arbiters of which notes ultimately show broadly. The authors argue that crowd-sourced contextual annotation can be augmented by AI without ceding control over visibility to either the platform or the models themselves, and that doing so openly (open API, open-source algorithm, open data) preserves the system's transparency and community-driven character.

## Key Contributions

- An open, public API design enabling AI systems to participate in Community Notes while retaining human control over which notes are displayed.
- A framework combining AI note generation with community rating/ranking to scale crowd-sourced contextual annotation.
- Demonstration that open-source and open-data principles can be preserved within an AI-augmented content-moderation/context system.

## Methods

The work is primarily a system design and deployment account rather than an empirical study. AI-proposed notes are triggered by explicit note requests and by user posts, then fed into the existing open-source, open-data Community Notes rating and ranking algorithm — the same mechanism that governs human-written notes. The AI Note Writer API was launched publicly in September 2025.

## Findings

- Empirical findings are not available from the provided (truncated) abstract excerpt; the paper's contribution as described is architectural and normative rather than evaluative.

## Connections

This sits within platform-governance debates over data access and human control of AI-mediated moderation, connecting to work on the political effects and quality of Community Notes such as [[Allen2025-ot]] and [[Bak-Coleman2025-pm]]. Its emphasis on AI generating candidate content for human-mediated systems relates to broader scrutiny of synthetic text in information ecosystems in [[Hackenburg2025-dj]] and to the general study of platforms as governance infrastructures in [[Gillespie2010-sla2]] and [[Gillespie2022-jx]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Miller2026-cp.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
