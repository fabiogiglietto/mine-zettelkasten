---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, italian-elections-political-communication]
citation_count: 7
open_access: true
source_url: https://doi.org/10.1177/20563051231196866
podcast_url: 
pdf_available: true
discovery_date: 
---

# A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election

## Summary

This paper proposes an iterative, near-real-time workflow for detecting and updating lists of coordinated social media accounts spreading problematic information, addressing the well-known decay of static actor lists as malicious operators adapt, get suspended, or rotate assets. Starting from a seed list of 435 coordinated accounts identified in prior Italian studies, the authors schedule API calls every six hours to monitor overperforming political posts, then apply near-duplicate detection across links, image-text combinations, and message content to surface new coordinated accounts. Applied to the 2022 Italian snap election, the workflow surfaced 620 newly coordinated accounts and yielded three contrasting case studies — a Five Star Movement hyperpartisan group network, a clickbait operation exploiting religious Pages, and a Church of Almighty God proselytism network — demonstrating that the approach is content- and actor-agnostic, capturing politically, economically, and religiously motivated operations alike.

## Key Contributions

- A circular, automated workflow that continuously updates lists of coordinated accounts rather than relying on static manual compilation.
- Methodological extension of CooRnet from Coordinated Link Sharing Behavior (CLSB) to Coordinated Image-Text Sharing Behavior (CITSB) and Coordinated Message Sharing Behavior (CMSB), addressing tactics like placing links in comments.
- Empirical application to the 2022 Italian election with three documented case studies spanning ideological, economic, and religious motivations.
- A behaviorally agnostic alert system designed to support fact-checkers, journalists, and researchers in prioritizing investigations.
- Discussion of portability to other platforms in light of DSA Article 40 data access provisions.

## Methods

The authors built an R-based pipeline scheduled via cronR to query CrowdTangle every six hours (July 28–September 25, 2022), retrieving the top 100 overperforming political and unfiltered posts plus posts from the top 10% of newly detected accounts. CooRnet was applied with a 30-second coordination interval and a 26+ share repetition threshold (0.995 percentile) to detect CLSB, alongside extensions for CITSB and CMSB (cosine similarity > 0.7). Political content was filtered using a keyword list of parties, leaders, and institutions with capitalization checks. Surfaced cases were analyzed through François's Actors-Behavior-Content framework, with URL classification by source type and NewsGuard reliability ratings.

## Findings

- Workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 generic coordinated accounts beyond the 435-account seed.
- The M5S network (90 entities, ~1.55M potential reach) published 534,353 posts in two months, averaging 6.2 posts/min on election day and peaking above 50/min, with 80% link-free posts indicating an echo-chamber dynamic and circulation of fabricated favorable polls.
- A clickbait network of 46 Pages used two large religious Pages (combined ~768,000 followers) to push misleading political headlines to religiously motivated audiences for ad revenue.
- A Church of Almighty God operation comprised 1,390 public groups in seven language clusters; its Italian subset (61 groups, 1.7M members; 13 Pages, 294,625 subscribers) used Messenger bots and abnormally high administrator counts to funnel users into undisclosed catechism chats.
- Only 2% of external M5S-network links came from NewsGuard-rated unreliable sources, but 76% were unrated — highlighting blind spots in reliability ratings for partisan ecosystems.

## Connections

This paper directly extends the authors' prior Italian CLSB work [[Giglietto2022-0e951ac5]] and connects to subsequent developments of the same research program [[Giglietto2026-9b6a992d]]. It sits within a broader methodological conversation on detecting coordinated behavior at scale, including approaches based on similarity and network signals such as [[Minici2024-tf]], [[Luceri2025-tr]], and [[Graham2025-gp]], and shares concerns about list decay and adversarial adaptation with work like [[Kuznetsova2025-nu]] and [[Schroeder2026-im]]. The case studies' mixing of ideological, economic, and religious motives also resonates with research challenging the assumption that coordination implies political inauthenticity, e.g., [[Hurcombe2025-cs]].
