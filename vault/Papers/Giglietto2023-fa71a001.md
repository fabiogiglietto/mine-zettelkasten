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

> Giglietto, F., Marino, G., Mincigrucci, R., & Stanziano, A. (2023). A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election. *Social Media + Society*. https://doi.org/10.1177/20563051231196866
>
> [View paper](https://doi.org/10.1177/20563051231196866)

## Summary

This paper proposes and demonstrates an iterative workflow to keep lists of coordinated social media accounts current, addressing the rapid obsolescence of static, manually compiled actor lists in problematic-information research. Starting from a seed of 435 previously identified Italian coordinated accounts, the authors monitor their best-performing posts every six hours via API and apply near-duplicate detection across links, image-text pairs, and message text to surface new accounts joining the coordination network. Applied to the 2022 Italian snap election, the workflow identified 620 additional coordinated accounts and yielded three case studies — a Five Star Movement hyperpartisan group network, a religious-clickbait click-economy operation, and a Church of Almighty God proselytism operation using Messenger bots — illustrating how the same behavioral signature surfaces ideologically, economically, and religiously motivated operations.

## Key Contributions

- A circular, near-real-time workflow that continuously expands lists of coordinated accounts rather than treating detection as a one-shot exercise.
- Extension of CooRnet-based Coordinated Link Sharing Behavior detection to also cover Coordinated Image-Text Sharing (CITSB) and Coordinated Message Sharing (CMSB), capturing adaptations such as moving links into comments.
- An empirical application to the 2022 Italian election that produced three documented case studies of distinct motivational logics behind coordination.
- A behaviorally agnostic alert system for fact-checkers, journalists, and researchers, paired with a discussion of portability to other platforms under DSA Article 40 data access.

## Methods

The authors compiled a seed of 435 coordinated Italian accounts by re-running CooRnet on ~73k links from ~398k political posts drawn from prior 2018, 2019, and COVID-era studies. From July 28 to September 25, 2022, an R script invoked the CrowdTangle posts/search API every six hours to retrieve overperforming political and unfiltered posts, plus posts from the top 10% of newly detected accounts. CooRnet was applied with a 30-second coordination window and a 26+ share repetition threshold (0.995 percentile); CITSB and CMSB extensions used near-duplicate matching and cosine similarity > .7. Political filtering relied on a keyword list of parties, leaders, and institutions with capitalization heuristics, and case studies were analyzed via François's A-B-C framework with NewsGuard ratings for link reliability.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 generic coordinated accounts beyond the seed.
- The M5S network comprised 90 entities reaching ~1.5M users, publishing 534,353 posts in two months and peaking above 50 posts/minute on election day; 80% of posts had no external links, indicating echo-chamber dynamics and circulation of fabricated favorable polls.
- A clickbait operation centered on two religious Pages ("La Preghiera di Oggi" and "Santa Rita da Cascia") with combined ~768k followers used two-thirds non-religious, misleadingly headlined political clickbait to monetize a religious audience.
- A Church of Almighty God proselytism cluster spanned 1,390 public groups in seven language regions; the Italian subset (61 groups, ~1.7M members; 13 Pages, ~295k subscribers) used Pages with unusually many administrators and Messenger bots to funnel users into undisclosed catechism chats.
- Only 2% of external links in the M5S case came from NewsGuard-rated unreliable sources, while 76% were unrated, with reliable links skewing toward ideologically aligned outlets.

## Connections

This paper is a direct methodological extension of the authors' prior Italian CLSB work ([[Giglietto2020-9d8acdd7]], [[Giglietto2019-882f1900]], [[F2020-6278a4aa]], [[Giglietto2022-0e951ac5]]) and connects closely to related Italian and methodological follow-ups ([[Marino2024-2fbc690f]], [[Mannocci2025-ig]], [[Giglietto2025-1765bb4f]], [[Giglietto2026-9b6a992d]]). It speaks to the broader coordinated-behavior detection literature on temporal dynamics, adaptation, and platform measurement — including [[Minici2024-tf]], [[Luceri2025-tr]], [[Graham2025-gp]], [[Schroeder2026-im]], and [[Kulichkina2026-zk]] — and to the A-B-C/information-operations framing taken up in works like [[Starbird2025-jj]].
