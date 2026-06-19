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

This paper introduces an iterative workflow for keeping lists of coordinated social media accounts current, addressing the rapid obsolescence of static actor lists in problematic-information research. Starting from a seed list of known coordinated accounts, the system polls platform APIs every few hours for overperforming posts, applies near-duplicate detection across links, image-text pairs, and message content to surface new accounts engaged in coordinated behavior, then folds these into subsequent monitoring rounds. Applied to the 2022 Italian snap election, the workflow expanded an initial seed of 435 accounts by uncovering 620 new coordinated accounts and yielded three richly different case studies — a hyperpartisan Five Star Movement network, a clickbait operation laundering political content through religious Facebook Pages, and a transnational Church of Almighty God proselytism operation using Messenger bots — illustrating that the same behavioral signatures can flag ideologically, economically, and religiously motivated operations.

## Key Contributions

- A circular, near-real-time workflow that updates coordinated-actor lists rather than relying on static manual compilation.
- Methodological extension of Coordinated Link Sharing Behavior (CLSB) detection to Coordinated Image-Text Sharing Behavior (CITSB) and Coordinated Message Sharing Behavior (CMSB), capturing adaptive tactics like placing links in comments.
- An empirical demonstration on the 2022 Italian election with three contrasting case studies of coordinated operations.
- A behavior- and content-agnostic alert system designed to support fact-checkers, journalists, and researchers without prejudging harm.
- A discussion of portability of the workflow under the EU Digital Services Act Article 40 data access regime to Meta, TikTok, Twitter, and YouTube.

## Methods

The authors built an R-based pipeline scheduled via cronR, querying the CrowdTangle posts/search API every six hours during July 28–September 25, 2022. Each cycle retrieved the top 100 political and top 100 unfiltered overperforming posts (using CrowdTangle's overperforming score plus a custom metric weighting comment/share ratios) along with posts from the top 10% of newly detected accounts. CooRnet was then run with a 30-second coordination window and a 26+ share repetition threshold (0.995 percentile) to detect CLSB, with extensions for CITSB and CMSB (cosine similarity > .7). Political content was identified via a curated keyword list of parties, leaders, and institutions with capitalization filters. Three surfaced networks were then analyzed with François's Actors-Behavior-Content framework, classifying URL sources as platform-internal vs. external and using NewsGuard for source reliability.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new political coordinated accounts, and 554 additional generic coordinated accounts beyond the 435-account seed.
- The M5S-aligned network spanned 90 entities (mostly groups) with ~1.5M potential reach, posting 534,353 messages in two months — peaking at 50+ posts/minute on election day — with ~80% of posts containing no links, producing an echo-chamber circulating fabricated pro-M5S polls.
- A clickbait operation of 46 Pages used two large religious Pages ("La Preghiera di Oggi", "Santa Rita da Cascia", ~768K combined followers) to push misleading political clickbait to religiously oriented audiences.
- A Church of Almighty God proselytism cluster spanned 1,390 groups in seven language clusters; the Italian subset (61 groups, 13 Pages, ~2M combined reach) used Pages with unusually high administrator counts (avg 72.6) and Messenger bots to funnel users into undisclosed catechism chats.
- Only 2% of external links in the M5S network came from NewsGuard-flagged unreliable outlets, but 76% were unrated, complicating reliability-based assessments and underscoring the need for behavioral signals.

## Connections

This paper directly extends the authors' programme on Coordinated Link Sharing Behavior in Italian elections and the CooRnet toolkit, building on [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2019-882f1900]], and [[F2020-6278a4aa]], and is complemented by the discussion of overperformance signals in [[Marino2024-2fbc690f]]. It belongs to a broader methodological conversation about detecting coordinated behavior beyond static lists and content moderation, alongside [[Giglietto2025-1765bb4f]], [[Giglietto2026-9b6a992d]], [[Mannocci2025-ig]], [[Luceri2025-tr]], and [[Minici2024-tf]], while the case studies on religious and clickbait operations connect to work on motivations and infrastructures of coordinated campaigns such as [[Starbird2025-jj]] and [[Graham2025-gp]].
