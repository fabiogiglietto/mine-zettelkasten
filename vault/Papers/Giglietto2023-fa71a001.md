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

This paper introduces an iterative, near-real-time workflow for keeping lists of coordinated social media accounts current, addressing the well-known problem that such lists decay rapidly as actors adapt, get suspended, or rotate assets. Starting from a seed of 435 previously identified Italian coordinated accounts, the authors monitor their overperforming posts every six hours via CrowdTangle and apply CooRnet-based near-duplicate detection across links, image-text, and message content to surface new coordinated accounts. Applied to the 2022 Italian snap election, the workflow discovered 620 new coordinated accounts and produced three case studies spanning ideological (a Five Star Movement hyperpartisan network), economic (religious-themed political clickbait Pages), and religious (Church of Almighty God proselytism via Messenger bots) motivations, demonstrating that the approach is content- and actor-agnostic.

## Key Contributions

- A circular, behavior-focused workflow that continuously expands seed lists of coordinated accounts rather than relying on static, manually compiled snapshots.
- Extension of Coordinated Link Sharing Behavior (CLSB) detection with Coordinated Image-Text Sharing Behavior (CITSB) and Coordinated Message Sharing Behavior (CMSB) to capture adaptation tactics such as moving links into comments.
- Empirical application to the 2022 Italian election, yielding three documented case studies of ideologically, economically, and religiously motivated coordination.
- A practical alert system for fact-checkers, journalists, and researchers, with explicit caution that flagged accounts are not automatically harmful.
- A discussion of portability to other platforms under the EU Digital Services Act Article 40 data access regime.

## Methods

The authors compiled a 435-account seed from prior Italian CLSB studies (2018, 2019, COVID era) by re-running CooRnet on 73,842 links from 398,385 political posts. An R script scheduled via cronR queried the CrowdTangle posts/search API four times daily during July 28–September 25, 2022, retrieving top overperforming political and unfiltered posts plus posts from the top 10% of newly detected accounts. CooRnet was applied with a 30-second coordination window and a 26+ share repetition threshold (0.995 percentile), supplemented by image-text and message-similarity (cosine > .7) variants. Political filtering used keyword lists with capitalization checks, and case studies were analyzed via François's Actors-Behavior-Content framework with NewsGuard reliability ratings for external links.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 generic coordinated accounts beyond the seed.
- **M5S network**: 90 entities with a potential reach of ~1.55M users published 534,353 posts in two months, peaking above 50 posts/minute on election day; 80% of posts contained no links, and most external links pointed to Facebook-internal content, sustaining an echo chamber that circulated fabricated favorable polls.
- **Clickbait network**: 46 Pages including two large religious Pages (~768K combined followers) devoted two-thirds of output to misleading political clickbait, incidentally exposing religious audiences to politicized content.
- **Church of Almighty God**: 1,390 public groups across seven language clusters; the Italian subset (61 groups, ~1.72M members; 13 Pages, ~295K subscribers) used Pages with unusually many administrators (avg 72.6) and Messenger bots to funnel users into undisclosed proselytism chats.
- Only 2% of external links in the M5S network came from NewsGuard-rated unreliable sources, but 76% were unrated, suggesting reliability ratings undercover much of the partisan link ecosystem.

## Connections

This paper directly extends the authors' prior program on Coordinated Link Sharing Behavior in Italian political communication ([[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2019-882f1900]], [[F2020-6278a4aa]], [[Marino2024-2fbc690f]]) and connects to broader methodological work on detecting and characterizing coordinated networks ([[Mannocci2025-ig]], [[Minici2024-tf]], [[Graham2025-gp]], [[Luceri2025-tr]]). Its emphasis on behavior- rather than content-based detection, and on iteratively maintained actor lists, resonates with ongoing debates about operationalizing coordinated inauthentic behavior at scale ([[Giglietto2025-1765bb4f]], [[Giglietto2026-9b6a992d]]).
