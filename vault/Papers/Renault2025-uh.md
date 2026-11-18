---
title: "Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes"
aliases: ["Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes"]
authors: ["Thomas Renault", "Mohsen Mosleh", "David Gertler Rand"]
year: 2025
doi: 10.1073/pnas.2502053122
bibtex_key: Renault2025-uh
topics: [information-disorder-narratives, platform-governance-and-data-access]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1073/pnas.2502053122
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
preprint_doi: 10.31234/osf.io/vk5yj_v4
published_venue: "Proceedings of the National Academy of Sciences"
---

# Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes

> Renault, T., Mosleh, M., & Rand, D. G. (2025). Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes. *Proceedings of the National Academy of Sciences*, *122*(25), e2502053122. https://doi.org/10.1073/pnas.2502053122
>
> [View paper](https://doi.org/10.1073/pnas.2502053122)

## Summary

This brief report uses X's Community Notes program as a natural experiment to test whether the well-documented partisan asymmetry in online misinformation sharing persists when content is evaluated by a crowdsourced bridging algorithm rather than professional fact-checkers. Analyzing 218,382 Community Notes from January 2023 to June 2024, the authors find that posts by Republicans are flagged as misleading roughly 2.3 times more often than posts by Democrats among notes that achieve "helpful" status. Because Community Notes requires cross-partisan agreement to surface a note, the authors argue this asymmetry cannot be explained away by liberal bias among professional fact-checkers — directly undercutting the rationale offered by Musk and Zuckerberg for abandoning professional fact-checking in favor of community-based systems.

## Key Contributions

- Demonstrates that partisan asymmetry in misinformation sharing holds under a crowdsourced, bridging-algorithm evaluation system, not only under professional fact-checking.
- Directly rebuts the "fact-checkers are biased against conservatives" critique by removing professional fact-checkers from the evaluation loop.
- Moves beyond prior domain-level or URL-based quality measures by evaluating specific claims at the tweet level.
- Introduces a triangulated partisanship-inference method combining two follower-based scores with an LLM-based classifier as a tiebreaker.
- Documents topical variation in the asymmetry, with health misinformation showing the largest Republican skew.
- Releases replication code and a dehydrated tweet dataset.

## Methods

The authors analyzed the full open-source Community Notes dataset for English-language notes and tweets (Jan 2023–Jun 2024), yielding 218,382 notes over 162,228 tweets from 39,140 users. User partisanship was inferred by triangulating three approaches — Mosleh & Rand's follower-based partisan score, Barberá's Bayesian ideal-point estimation, and GPT-4o mini classification of recent tweets — retaining users only where at least two methods agreed. The bridging algorithm's "helpful" status served as a proxy for a tweet actually being misleading, and logistic regression predicted helpful status from poster partisanship while controlling for verified status, follower count, tweet volume, and topic (classified via Chuai et al.'s classifier). A base-rate check sampled 474,394 random English tweets to estimate the platform's partisan composition.

## Findings

- 60.05% of proposed notes targeted Republican posts versus 39.95% for Democratic posts.
- Notes on Republican tweets reached "helpful" status more often (10.41% vs. 6.78%); being Republican raised the odds of a helpful rating by 63.49% in regression.
- Among the 19,569 helpful notes, 69.79% targeted Republican posts — a 2.3:1 ratio.
- The asymmetry is robust across individual partisanship measures (1.7x with Mosleh & Rand; 2.1x with Barberá).
- Republican overrepresentation is largest for Health (81.9%), followed by Politics (73.3%), Science (68.8%), Other (66.9%), and Economy (63.7%).
- Democrats still post more than Republicans in a random sample, ruling out a base-rate explanation despite a growing Republican share since Musk's acquisition.

## Connections

[[Bouchaud2026-np]] cites this paper and finds the same US asymmetry among Helpful notes, while showing that bridging leaves most polarizing, election-related content unresolved; [[Miller2026-cp]] documents how much of Community Notes is now written by AI clients. Both this paper and [[Cazzamatta2026-lo]] test the bias rationale for dropping professional fact-checking, and [[Holt2026-zq]] examines user-driven flagging on Facebook after Meta's switch to Community Notes. Two of the authors also wrote [[Mosleh2024-op]], a cross-platform study of engagement with partisan and low-quality news.
