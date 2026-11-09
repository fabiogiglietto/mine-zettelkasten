---
title: "New election, same old story: How tropes form a grammar of election rumors"
aliases: ["New election, same old story: How tropes form a grammar of election rumors"]
authors: ["Stephen Prochaska", "Mert Bayar", "Ashlyn B. Aske", "Joseph Schafer", "Kate Starbird"]
year: 2026
doi: 
bibtex_key: Prochaska2026-pr
topics: [information-disorder-and-health-misinformation, electoral-communication-and-digital-campaigns]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2610.37804v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Prochaska2026-pr.mp3
pdf_available: true
discovery_date: 2026-10-31T10:46:26.743073Z
---

# New election, same old story: How tropes form a grammar of election rumors

> Prochaska, S., Bayar, M., Aske, A. B., Schafer, J., & Starbird, K. (2026). New election, same old story: How tropes form a grammar of election rumors. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2610.37804v1)

## Summary

This paper argues that election rumors, though they appear chaotic and overwhelming in real time, are not random: they are assembled from a finite, recurring set of narrative tropes that reappear across election cycles. Analyzing 568 distinct rumors drawn from the 2020 U.S. presidential and 2022 midterm elections, the authors develop a three-tier hierarchical framework (meta-category, meso-trope, micro-trope) and identify a "grammar" of election rumors in which most rumors combine an **Actor**, an **Object**, and an **Action**, optionally elaborated by **Scene & Setting** and **Suggested Remedies**. The central claim is that these tropes function as narrative building blocks that make each novel event feel familiar by slotting it into a pre-existing story of election fraud — giving the framework diagnostic and anticipatory value for researchers, communicators, and election officials.

## Key Contributions

- A hierarchical three-tier framework (meta-category / meso-trope / micro-trope) organizing election rumor tropes by narrative function.
- An empirically grounded "grammar" of election rumors (Actor + Object + Action, with optional Scene & Setting and Suggested Remedies).
- A reusable coding scheme and information architecture (released as appendices) adaptable to other rumor domains.
- Practical guidance for prebunking and threat assessment, flagging which actors, objects, and actions to prioritize.

## Methods

Mixed-methods, combining inductive qualitative coding with computational analysis. The data come from two prior corpora of election Twitter/X discourse: a 2020 corpus (~32.4M tweets organized into 455 rumors) and a 2022 corpus (~1.8M tweets mapped to 135 rumors). Coding was conducted at the **rumor level** (collections of tweets) rather than the tweet level, starting from 590 rumors and reduced to 568. LLM-assisted summaries (ChatGPT 4.1 mini) used two-step hierarchical summarization of up to 1,000 tweets per rumor, supplemented by word clouds and top/random tweet samples. A three-tier coding scheme was developed iteratively; each rumor was double-coded with third-coder arbitration. Trope frequency and co-occurrence were analyzed quantitatively using Jaccard similarity (threshold .1) and Louvain community detection to cluster the micro-trope network.

## Findings

- Six meta-categories structure rumors: Actor, Actor-Action, Object, Object-Action, Scene & Setting, and Suggested Remedies.
- Actors appear in 96.5% of rumors; Scene & Setting in ~74.8%; Suggested Remedies in ~70.8% — most rumors are action-oriented rather than merely descriptive.
- ~70% of rumors (397 of 568) conform to the "proper" grammar (Actor + Object + Action); ~30% (171) are missing a core element.
- Among improper-grammar rumors, the most commonly missing element was Objects-Combined (99 rumors, 57.9%), followed by Actions (31 rumors).
- 94% of proper-grammar rumors also contained Scene & Setting and/or Suggested Remedies, supporting their role as salient elaborating features.
- The co-occurrence network shows a central cluster spanning every meta-category (Democrats as villains, Democrat-run urban centers, swing states, Republicans as victims, calls for audits/recounts/litigation), surrounded by sub-narrative clusters (media/big tech distrust, voting machines/foreign influence, offsite counting, voter intimidation, mail-in fraud, ballot injection).
- Specific tropes (e.g., noncitizen voting, ICE at polls) wax and wane across cycles, tracking the online attention economy and news cycles.

## Connections

This paper builds on the authors' broader program of collaborative rumoring research and shares data lineage and conceptual commitments with [[Starbird2019-qv]], [[Starbird2025-jj]], and [[Prochaska2025-ef]] on how online participatory communities construct fraud narratives. Its narrative-grammar framing complements work on the diffusion dynamics and virality of false claims such as [[Vosoughi2018-at]], while its component-level account of recurring tropes offers a structural counterpart to studies of election misinformation prevalence and exposure like [[Grinberg2019-ua]] and [[DeVerna2025-dl]]. The predictive, prebunking orientation also connects to inoculation and anticipatory-communication research represented by [[Lewandowsky2012-vn]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Prochaska2026-pr.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
