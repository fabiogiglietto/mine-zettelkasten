---
title: "Using co-sharing to identify use of mainstream news for promoting potentially misleading narratives"
aliases: ["Using co-sharing to identify use of mainstream news for promoting potentially misleading narratives"]
authors: ["Pranav Goel", "Jon Green", "David Lazer", "Philip S. Resnik"]
year: 2025
doi: 10.1038/s41562-025-02223-4
bibtex_key: Goel2025-iq
topics: [information-disorder, news-ecosystems-and-partisanship]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1038/s41562-025-02223-4
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
---

# Using co-sharing to identify use of mainstream news for promoting potentially misleading narratives

## Summary

This paper challenges the dominant source-level paradigm in misinformation research, which classifies content as "fake" based on the domain that publishes it. The authors argue this approach misses a larger phenomenon: users selectively sharing factually accurate mainstream news articles to advance misleading narratives. Using a 1.6M-user Twitter panel matched to a U.S. voter file (2018–2021), they identify mainstream articles disproportionately co-shared with fake news and show these articles are significantly more likely than control articles from the same outlets to contain narrative structures present in fake news and fact-checked false claims. Because co-shared mainstream articles reach roughly twice the audience of fake news itself, the authors contend that misinformation ecosystems are substantially broader than fake-news-domain metrics suggest.

## Key Contributions

- A scalable co-sharing-based method for identifying mainstream articles likely repurposed for misinformation, complementing domain-list approaches.
- An operational definition of "potentially misleading narratives" via automated narrative extraction (relatio) over fake news articles, fake news headlines, and ~24k fact-checked false claims — producing reusable narrative libraries.
- Empirical evidence that misinformation networks extend well beyond fake-news domains, with cross-source diffusion plausibly larger in reach than fake news itself.
- Two qualitative case studies (anti-vaccine narratives; 2020 mail-in-ballot fraud) demonstrating concrete repurposing mechanisms.
- Implications for journalistic practice — headlines and framing carry repurposing risk independent of factual accuracy — plus released code and data.

## Methods

The authors build a weighted bipartite co-sharing graph linking fake news URLs and reliable-news URLs, using a graph-pruning algorithm to control for popularity; the top 1% of co-sharing scores define the treated set, articles outside the top 5% serve as controls. Domain classification uses NewsGuard plus prior reliability ratings and YouGov passive-metering data. Narratives in AGENT–VERB→PATIENT form are extracted at two granularities. One-sided Wilcoxon signed-rank tests compare narrative occurrence in co-shared vs. control mainstream articles, with robustness checks for partisan curation, audience partisanship, domain fixed effects, trustworthy-only and liberal-only subsets, and removal of direct quotations. Two case studies (vaccines, voter fraud) supplement the quantitative analysis, along with manual coding of 100 tweets to check for share-to-criticize behavior.

## Findings

- Co-shared mainstream articles contain potentially misleading narratives at significantly higher rates than controls across all three narrative libraries and both granularities (≈0.94 vs. ≈0.58 narratives per article; 2.2% vs. 1.3% as a share of all narratives).
- Co-shared articles have roughly 1.24× the odds of containing misleading narratives after controls.
- Effect persists in trustworthy-only and liberal-leaning-only subsets, ruling out a purely partisan-composition explanation.
- Co-shared mainstream articles reach about twice the audience of fake news articles in this panel.
- Vaccine case study reveals three repurposing patterns: clickbait headlines, older articles recontextualized, and ambiguous content.
- Voter-fraud case study identifies 11 mainstream articles supporting the 2020 mail-in-ballot fraud narrative — clickbait pieces, reports on isolated fraud incidents, and unrebutted quotation of fraud claims.
- Effect holds in 16/18 tests after removing direct quotations, and share-to-criticize behavior is rare (3/100 sampled tweets).

## Connections

This paper directly engages debates about how misinformation should be measured and bounded, complementing critiques of narrow fake-news exposure estimates such as [[Budak2024-ef]] and [[Gonzalez-Bailon2024-rq]], and pairing naturally with [[Mosleh2024-op]] on user-level sharing behavior. Its focus on narrative-level repurposing across mainstream and fringe sources connects to coordinated-amplification and rumoring work like [[Starbird2025-jj]] and [[Luceri2025-tr]], and to research on how journalistic framing carries misinformation risk, e.g. [[Hameleers2026-mc]] and [[Cazzamatta2026-lo]]. The co-sharing graph methodology resonates methodologically with network-based detection work such as [[Minici2024-tf]] and [[DeVerna2025-dl]].
