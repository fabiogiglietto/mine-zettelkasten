---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, elections-political-communication]
citation_count: 7
open_access: true
source_url: https://doi.org/10.1177/20563051231196866
podcast_url: 
pdf_available: true
discovery_date: 
---

# A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election

## Summary

This paper proposes a circular, near-real-time workflow for keeping lists of coordinated social media accounts up to date, addressing the well-known problem that static actor lists decay rapidly as malicious operators adapt, get suspended, or rotate assets. Starting from a seed list of known coordinated accounts, the system polls their highest-performing posts every six hours via CrowdTangle, then applies coordination detection (link, image-text, and message variants of CooRnet) to surface new accounts engaged in coordinated sharing. Applied to the 2022 Italian snap election, the workflow grew an initial 435-account seed into hundreds of newly detected coordinated entities and revealed three qualitatively distinct operations — a Five Star Movement hyperpartisan group network, a clickbait operation using religious Pages as bait, and a transnational religious proselytism campaign by the Church of Almighty God. The authors frame the workflow as content- and actor-agnostic infrastructure for prioritizing investigations rather than automatically labeling content harmful.

## Key Contributions

- An iterative workflow that updates coordinated-account lists in near-real-time instead of relying on static, manually curated rosters.
- Extension of Coordinated Link Sharing Behavior (CLSB) detection to Coordinated Image-Text Sharing (CITSB) and Coordinated Message Sharing (CMSB, cosine similarity > .7), capturing adaptive tactics like burying links in comments.
- An empirical demonstration on the 2022 Italian election yielding three documented case studies of ideologically, economically, and religiously motivated coordination.
- A behaviorally agnostic alert system for fact-checkers, journalists, and researchers, with explicit discussion of portability to other platforms under DSA Article 40 data-access provisions.

## Methods

The authors built an R-based pipeline scheduled via cronR to query the CrowdTangle posts/search API four times daily (every 6 hours) between July 28 and September 25, 2022. The seed list of 435 coordinated accounts (238 Pages, 196 groups, 1 Instagram account) was derived by running CooRnet on 73,842 links from 398,385 prior Italian political posts. Each cycle retrieved top overperforming posts (using CrowdTangle's overperforming score plus a custom comment/share-ratio metric), filtered politically relevant content via a keyword list of parties, leaders, and institutions, and then re-ran CooRnet (30-second window, 26+ share repetition at the 0.995 percentile) to detect CLSB, CITSB, and CMSB. Surfaced cases were analyzed using François's A-B-C (Actors-Behavior-Content) framework, with NewsGuard ratings for source reliability and URL classification into Facebook-internal vs. external categories.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 generic coordinated accounts beyond the initial seed.
- **M5S network**: 90 entities (89 groups, 1 Page) with potential reach of ~1.55M users posted 534,353 messages in two pre-election months, peaking above 50 posts/minute on election day; 80% of posts contained no links, and most external links pointed to ideologically aligned outlets, indicating an echo-chamber dynamic that also circulated fabricated polls.
- **Clickbait operation**: 46 Pages including two large religious Pages ("La Preghiera di Oggi" and "Santa Rita da Cascia", ~768k combined followers) where two-thirds of posts were non-religious political clickbait, exposing religiously motivated audiences to misleading political content.
- **Church of Almighty God**: 1,390 public groups across seven language clusters; the Italian subset (61 groups, 1.72M members; 13 Pages, 294k subscribers) used Pages with unusually high admin counts (avg. 72.6) and Messenger bots to funnel users into catechism chats without disclosing affiliation.
- Only 2% of external links in the M5S network came from NewsGuard-rated unreliable sources, but 76% were unrated — highlighting blind spots in reliability databases.

## Connections

This paper directly extends the authors' prior CLSB program on Italian elections and COVID information ([[Giglietto2022-0e951ac5]], [[Giglietto2020-9d8acdd7]], [[Giglietto2019-882f1900]], [[Marino2024-2fbc690f]]) by making list maintenance dynamic, and pairs methodologically with other CooRnet-adjacent or coordination-detection work such as [[Graham2025-gp]], [[Graham2026-fb]], [[Mannocci2025-ig]], [[Minici2024-tf]], and [[Luceri2025-tr]]. Its A-B-C framing and emphasis on behavior over content connect it to broader debates on defining and operationalizing coordinated inauthentic behavior found in [[Starbird2025-jj]] and [[Giglietto2025-1765bb4f]], while the Italian electoral context links it to [[Iannucci2025-eg]] and [[Iannelli2015-e0818c3e]].
