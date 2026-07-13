---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, italian-elections-mine]
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

This paper proposes an iterative workflow to address a persistent weakness in research on coordinated online behavior: manually compiled lists of coordinated accounts decay quickly as actors adapt, get suspended, or spin up new assets. Starting from a known seed of 435 coordinated Italian accounts, the authors schedule API queries every six hours to capture overperforming posts, then apply CooRnet-based detection of Coordinated Link, Image-Text, and Message Sharing Behavior to surface newly coordinating accounts in near real-time. Applied to the 2022 Italian snap election, the workflow uncovered 620 previously unknown coordinated accounts and three qualitatively distinct operations — ideological (a Five Star Movement echo-chamber network), economic (religious Pages repurposed for political clickbait), and religious (a Church of Almighty God proselytism network using Messenger bots).

## Key Contributions

- A circular, actor- and content-agnostic workflow that continuously refreshes lists of coordinated accounts rather than treating them as static.
- Methodological extension of Coordinated Link Sharing Behavior (CLSB) detection to Coordinated Image-Text Sharing (CITSB) and Coordinated Message Sharing (CMSB), closing gaps opened by adaptation tactics such as placing links in comments.
- An empirical Italian election case with three heterogeneous, documented operations, illustrating that coordination is not solely a political-disinformation phenomenon.
- An alert-oriented framing that supports fact-checkers and journalists while explicitly cautioning against treating flagged accounts as inherently malicious.
- A forward-looking discussion of porting the approach to other platforms under EU Digital Services Act Article 40 data access.

## Methods

The authors seeded the pipeline with 435 coordinated accounts derived from prior Italian CLSB studies (2018, 2019, COVID era). An R script scheduled via cronR queried CrowdTangle four times daily (July 28 – September 25, 2022), pulling top overperforming political and unfiltered posts plus content from the top 10% of newly detected accounts. Political filtering used a curated keyword list with capitalization heuristics. CooRnet was applied with a 30-second coordination window and a 26+ repetition threshold (0.995 percentile) for CLSB, complemented by CITSB and CMSB (cosine similarity > 0.7). Cases were analyzed with François's A-B-C (Actors-Behavior-Content) framework, using NewsGuard ratings and a Facebook-internal vs. external URL taxonomy.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 additional generic coordinated accounts beyond the seed list.
- **M5S network:** 90 entities, potential reach ~1.55M, 534,353 posts in two months (peaking above 50 posts/min on election day); 80% of posts contained no links, indicating a closed echo-chamber circulating pro-M5S content including fabricated polls.
- **Clickbait network:** 46 Pages, ~58k posts; two large religious Pages (~768k followers combined) devoted two-thirds of their output to misleading political clickbait, exposing religious audiences incidentally to political framing for ad revenue.
- **Church of Almighty God:** 1,390 public groups across seven language clusters; the Italian subset (61 groups, 13 Pages, ~2M combined audience) used Pages with abnormally many administrators and Messenger bots to funnel users into undisclosed proselytism.
- Only 2% of external M5S-network links were NewsGuard-rated unreliable, but 76% were unrated — a reminder that reliability ratings substantially undercover this ecosystem.

## Connections

This paper is a direct methodological continuation of the authors' Italian CLSB program ([[Giglietto2020-9d8acdd7]], [[Giglietto2022-b30e8b4e]], [[Giglietto2022-0e951ac5]], [[Iannelli2018-ebd918b7]]) and the CooRnet toolchain, extending it toward continuous monitoring alongside related tool-building efforts such as [[Giglietto2026-9b6a992d]] and [[Giglietto2026-855a54cb]]. It speaks to broader debates on detecting and validating coordinated behavior addressed by [[Graham2025-gp]], [[Graham2026-fb]], [[Schroeder2026-im]], and [[Luceri2025-tr]], and its concern with list decay and adaptive actors resonates with [[Murtfeldt2025-wu]] and platform-access discussions in [[Freelon2024-sc]] and [[Rieder2025-ju]].
