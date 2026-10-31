---
title: "New election, same old story: How tropes form a grammar of election rumors"
aliases: ["New election, same old story: How tropes form a grammar of election rumors"]
authors: ["Stephen Prochaska", "Mert Bayar", "Ashlyn B. Aske", "Joseph Schafer", "Kate Starbird"]
year: 2026
doi: 
bibtex_key: Prochaska2026-pr
topics: [information-disorder-and-disinformation-narratives, comparative-international-election-studies]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2610.37804v1
podcast_url: 
pdf_available: true
discovery_date: 2026-10-31T10:46:26.743073Z
---

# New election, same old story: How tropes form a grammar of election rumors

> Prochaska, S., Bayar, M., Aske, A. B., Schafer, J., & Starbird, K. (2026). New election, same old story: How tropes form a grammar of election rumors. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2610.37804v1)

## Summary

This paper argues that election rumors, despite their seemingly chaotic and overwhelming volume, are not random but are assembled from a finite set of recurring narrative tropes. Analyzing 568 distinct rumors drawn from the 2020 U.S. presidential and 2022 midterm elections, the authors develop a three-tier hierarchical framework (meta-category, meso-trope, micro-trope) for organizing these tropes by narrative function. Their central claim is that election rumors follow a discernible "grammar": most combine a core of an **Actor**, an **Object**, and an **Action**, often elaborated with optional **Scene & Setting** and **Suggested Remedies**. This component-level account extends narrative theories of rumoring into a diagnostic and predictive tool that researchers, communicators, and election officials can use to rapidly identify and anticipate emerging rumors.

## Key Contributions

- A hierarchical three-tier framework (meta/meso/micro) for systematically organizing election rumor tropes by narrative function.
- An empirically grounded "grammar" of election rumors describing how Actor, Object, and Action combine, with optional Scene & Setting and Suggested Remedies.
- A reusable coding scheme and information architecture (in appendices) adaptable to other rumor domains.
- Practical guidance for prebunking and threat assessment, highlighting which actors, objects, and actions to prioritize.

## Methods

Mixed-methods design combining qualitative coding with computational tools, applied to two prior corpora of election discourse on Twitter/X: a 2020 corpus (~32.4M tweets across 455 rumors) and a 2022 corpus (~1.8M tweets across 135 rumors). Coding was conducted at the rumor level rather than the tweet level, starting from 590 rumors and reduced to 568 after excluding out-of-scope cases. The team used LLM-assisted summaries (ChatGPT 4.1 mini, two-step hierarchical summarization of up to 1,000 tweets per rumor), word clouds, and tweet samples to support an iterative, inductive development of the three-tier scheme. Each rumor was double-coded by a team of three with consensus arbitration. Quantitative analysis examined trope frequency and co-occurrence, using Jaccard similarity (threshold .1) to build a micro-trope network and Louvain community detection for clustering.

## Findings

- Six meta-categories structure rumors: Actor, Actor-Action, Object, Object-Action, Scene & Setting, and Suggested Remedies.
- Actors appear in 96.5% of rumors; Scene & Setting in ~74.8%; Suggested Remedies in ~70.8% — most rumors are action-oriented, not merely descriptive.
- ~70% of rumors (397 of 568) conform to the "proper" grammar (Actor + Object + Action); ~30% (171) are missing a core element.
- Among improper-grammar rumors, the most commonly missing element was Objects-Combined (99 rumors, 57.9%), followed by Actions (31 rumors).
- Among proper-grammar rumors, 94% also contained Scene & Setting and/or Suggested Remedies, confirming their role as salient elaborating features.
- Co-occurrence analysis revealed a central cluster drawing from every meta-category (Democrats as villains, Democrat-run urban centers, swing states, Republicans as victims, calls for audits/recounts/litigation) surrounded by sub-narrative clusters (media/big-tech distrust, voting machines/foreign influence, offsite counting, voter intimidation, mail-in fraud, ballot injection).
- Specific tropes (noncitizen voting, ICE at polls) wax and wane across cycles, reflecting the online attention economy.

## Connections

This work builds directly on the authors' broader program studying election integrity rumoring and participatory disinformation, connecting closely to [[Starbird2025-jj]], [[Prochaska2025-ef]], and [[Starbird2019-qv]]. Its narrative-component approach to how familiar stories make novel events feel coherent complements research on prebunking and misinformation resistance such as [[Lewandowsky2012-vn]] and [[van-der-Linden2026-jt]], and its focus on recurring fraud narratives relates to work on the structure and spread of false election claims including [[Marwick2025-ov]] and [[Osmundsen2021-et]].
