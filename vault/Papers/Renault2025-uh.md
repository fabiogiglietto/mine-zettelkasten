---
title: "Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes"
aliases: ["Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes"]
authors: ["Thomas Renault", "Mohsen Mosleh", "David Gertler Rand"]
year: 2025
doi: 10.31234/osf.io/vk5yj_v3
bibtex_key: Renault2025-uh
topics: [information-disorder]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31234/osf.io/vk5yj_v3
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
---

# Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes

## Summary

This brief report uses X's Community Notes program as a natural test of whether partisan asymmetries in misinformation sharing persist when evaluation is crowdsourced rather than performed by professional fact-checkers. Analyzing 218,382 notes from January 2023 to June 2024, the authors show that posts by Republicans are flagged as misleading roughly 2.3 times more often than posts by Democrats among notes that achieve "helpful" status under the bridging algorithm — which requires cross-partisan agreement. Because Community Notes was specifically designed to neutralize one-sided ideological bias, the finding directly undermines the rationale Elon Musk and Mark Zuckerberg have offered for replacing professional fact-checking with community-based moderation: the asymmetry is not an artifact of biased fact-checkers.

## Key Contributions

- Demonstrates that partisan asymmetry in misinformation flagging persists under a bridging-algorithm-based crowdsourced system, not only under professional fact-checking.
- Directly rebuts the political claim that fact-checker liberal bias is responsible for differential sanctioning of Republicans.
- Moves beyond domain-level link quality scores to evaluating misleadingness at the level of specific tweet claims.
- Introduces a triangulated partisanship-inference pipeline combining two follower-based methods with an LLM tiebreaker.
- Documents topical heterogeneity, with Health misinformation showing the largest Republican skew.
- Releases code and a dehydrated dataset for replication.

## Methods

The authors collect the full open-source Community Notes dataset for English notes/tweets (Jan 2023–Jun 2024), yielding 218,382 notes on 162,228 tweets from 39,140 users. User partisanship is inferred by triangulating Mosleh & Rand's follower-based partisan score, Barberá's Bayesian ideal-point estimation, and GPT-4o mini classification of recent tweets, retaining only users for whom at least two methods agreed. The dependent measure is whether a note reached "helpful" status under the bridging algorithm. Logistic regression predicts helpful status from poster partisanship, controlling for verification, followers, tweet volume, and topic (classified via Chuai et al. 2024). A separate sample of 474,394 random English tweets is used to estimate baseline partisan composition on X.

## Findings

- 60.05% of proposed notes targeted Republican posts vs. 39.95% Democratic.
- Notes on Republican tweets reached "helpful" status more often (10.41% vs. 6.78%); being Republican raised the odds of helpful status by 63.49%.
- Among the 19,569 helpful notes, 69.79% targeted Republicans and 30.21% Democrats — a 2.3:1 ratio.
- Robust to using either follower-based method alone (1.7x with Mosleh & Rand; 2.1x with Barberá).
- Republican skew by topic: Health (81.9%), Politics (73.3%), Science (68.8%), Other (66.9%), Economy (63.7%).
- Democrats still outpost Republicans in a random sample of X tweets, ruling out a simple base-rate explanation, though the Republican share has grown post-acquisition.

## Connections

This paper extends [[Mosleh2024-op]], whose follower-based partisanship scores it directly employs, and converges with [[Gonzalez-Bailon2024-rq]] on documenting partisan asymmetries in online information quality — but advances the literature by showing the asymmetry holds under a bias-resistant crowdsourced evaluation regime. It speaks to ongoing assessments of Community Notes as a moderation mechanism, including [[DeVerna2025-dl]], and contributes to broader debates about hyperpartisan media ecosystems and platform governance represented by work such as [[Budak2024-ef]] and [[Bakshy2015-rn]].
