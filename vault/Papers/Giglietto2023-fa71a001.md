---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, digital-methods-tools]
citation_count: 20
open_access: true
source_url: https://doi.org/10.1177/20563051231196866
podcast_url: 
pdf_available: true
discovery_date: 
---

# A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election

> Giglietto, F., Marino, G., Mincigrucci, R., & Stanziano, A. (2023). A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election. *Social Media + Society*. https://doi.org/10.1177/20563051231196866
>
> [View paper](https://doi.org/10.1177/20563051231196866)

## Summary

This paper proposes and demonstrates an iterative workflow for keeping lists of coordinated social media accounts up to date, addressing a recurring weakness of list-based detection: seed rosters decay quickly as actors adapt, get suspended, or rotate assets. Starting from a known list of coordinated actors, the pipeline monitors their best-performing posts every few hours via APIs and uses near-duplicate detection over links, image-text pairs, and message text to surface newly coordinating accounts. Applied to the 2022 Italian snap election, the workflow began with 435 previously identified coordinated accounts and surfaced 620 new ones, illustrated through three case studies spanning ideological (M5S hyperpartisan groups), economic (religious clickbait pages), and religious (Church of Almighty God proselytism) motivations.

## Key Contributions

- A circular, near-real-time workflow for updating coordinated-account lists rather than relying on static manual compilations.
- Extension of Coordinated Link Sharing Behavior (CLSB) detection with Coordinated Image Text Sharing Behavior (CITSB) and Coordinated Message Sharing Behavior (CMSB), addressing adaptation tactics like moving links into comments.
- Empirical application to the 2022 Italian election with three documented case studies of ideologically, economically, and religiously motivated operations.
- A behaviorally agnostic alert framework for fact-checkers and researchers, with explicit caution against equating detected coordination with harm.
- Discussion of portability across platforms in light of DSA Article 40 data-access provisions.

## Methods

The authors built an R-based pipeline scheduled via cronR that polls the CrowdTangle posts/search API every six hours between July 28 and September 25, 2022, retrieving the top 100 overperforming political and unfiltered posts plus posts from the top 10% of newly detected accounts. Overperformance was measured via CrowdTangle's score plus a combined comment/share metric. Coordination was detected using CooRnet (30-second window, 26+ share repetition at the 0.995 percentile) for CLSB, extended to image-text pairs (CITSB) and cosine-similarity text matching >0.7 (CMSB). Political filtering used a keyword list of parties, leaders, and institutions with capitalization checks. Case studies were analyzed through François's A-B-C framework, with URL sources classified as Facebook-internal vs. external and reliability assessed via NewsGuard.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, and 620 new coordinated accounts (66 political, 554 generic) beyond the 435-account seed.
- The M5S network comprised 90 entities with a potential reach of ~1.55M users, publishing 534,353 posts in the pre-election period, peaking above 50 posts/minute on election day; 80% had no links, indicating an echo-chamber environment amplifying favorable (sometimes fabricated) polls.
- A clickbait operation used two religious Pages ("La Preghiera di Oggi", "Santa Rita da Cascia", combined reach ~768,000) to post two-thirds non-religious political clickbait, incidentally exposing devotional audiences to politically charged content.
- A Church of Almighty God proselytism operation was detected across 1,390 public groups in seven language clusters; the Italian subset spanned 61 groups (~1.72M members) and 13 Pages (~295,000 subscribers), using Messenger bots to funnel users into undisclosed catechism chats, with Pages showing anomalously high admin counts (avg 72.6).
- Only 2% of external M5S-network links were NewsGuard-rated unreliable, but 76% were unrated; rated reliable links skewed toward ideologically aligned outlets.

## Connections

This paper directly extends the authors' program on Coordinated Link Sharing Behavior in Italian elections and the CooRnet toolchain — see [[Giglietto2022-b30e8b4e]], [[Giglietto2022-0e951ac5]], [[Giglietto2020-9d8acdd7]], and [[Iannelli2018-ebd918b7]] — and connects to their more recent methodological work in [[Giglietto2026-9b6a992d]], [[Giglietto2026-855a54cb]], and [[Giglietto2025-ed60bc90]]. Within the broader coordinated-inauthentic-behavior literature, it speaks to debates on detection methodology and adaptation covered by [[Graham2025-gp]], [[Graham2026-fb]], [[Luceri2025-tr]], [[Minici2024-tf]], and [[Kulichkina2026-zk]], and shares an actor/behavior-agnostic orientation with [[Freelon2024-sc]].
