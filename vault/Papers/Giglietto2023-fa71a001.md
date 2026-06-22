---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, digital-methods-tools]
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

This paper introduces a circular workflow for keeping lists of coordinated social media accounts up to date, addressing the problem that static seed lists rapidly decay as actors are suspended, change assets, or adapt their tactics. Starting from a known set of coordinated accounts, the system polls platform APIs every few hours for their best-performing posts, then applies near-duplicate detection across links, image-text pairs, and message bodies to surface new accounts engaged in coordinated sharing. Applied to the 2022 Italian snap election, the workflow expanded a seed of 435 accounts by detecting 620 additional coordinated accounts and produced three case studies showing that coordination is not only ideologically driven but also economically (clickbait) and religiously (proselytism) motivated.

## Key Contributions

- An iterative, near-real-time pipeline for updating lists of coordinated accounts, replacing static manual compilations.
- Extension of Coordinated Link Sharing Behavior (CLSB) detection to Coordinated Image-Text Sharing Behavior (CITSB) and Coordinated Message Sharing Behavior (CMSB), capturing adaptations such as moving links to comments.
- Empirical demonstration on the 2022 Italian election with three diverse coordinated operations documented.
- A behaviorally and content-agnostic alert system for journalists, fact-checkers, and researchers, with explicit caveats against treating flagged actors as automatically harmful.
- Reflections on portability to other platforms via emerging researcher APIs and the EU Digital Services Act Article 40 framework.

## Methods

The authors built a seed list of 435 coordinated accounts by running CooRnet on 73,842 links from ~398k political posts published by accounts previously identified in 2018, 2019, and COVID-era Italian studies. An R script scheduled via cronR queried the CrowdTangle posts/search API every six hours between 28 July and 25 September 2022, retrieving the top 100 overperforming political and unfiltered posts plus posts from the top decile of newly detected accounts. CooRnet was applied with a 30-second window and a 26-share threshold (0.995 percentile) for CLSB; CITSB and CMSB extensions used near-duplicate image-text matches and cosine similarity > 0.7 on message text. Political filtering relied on a curated keyword list with capitalization checks; case studies were analyzed using François's A-B-C (Actors-Behavior-Content) framework, with NewsGuard ratings for link reliability.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 generic coordinated accounts beyond the seed.
- Case 1 — an M5S-aligned hyperpartisan network of 90 entities with potential reach of ~1.55M users published 534k posts in two months, peaking at >50 posts/minute on election day; 80% contained no links, signaling an internal echo chamber that recirculated fabricated favorable polls.
- Case 2 — a 46-Page clickbait operation in which religious Pages ("La Preghiera di Oggi", "Santa Rita da Cascia") with ~768k combined followers posted two-thirds non-religious political clickbait, incidentally exposing devotional audiences to misleading political headlines.
- Case 3 — 1,390 public groups across seven language clusters tied to the Church of Almighty God; the Italian subset (61 groups, 13 Pages, ~2M combined audience) used Pages with unusually high admin counts (avg 72.6) and Messenger bots to funnel users into undisclosed catechism chats.
- Only 2% of external links in the M5S network were NewsGuard-rated as unreliable, but 76% were unrated, with rated reliable links concentrated in ideologically aligned outlets.

## Connections

This paper directly extends the authors' line of work on Coordinated Link Sharing Behavior in Italian electoral contexts ([[Giglietto2022-0e951ac5]], [[Giglietto2020-9d8acdd7]], [[Giglietto2019-882f1900]], [[F2020-6278a4aa]], [[Marino2024-2fbc690f]]) by adding image-text and message-level coordination and a self-updating loop. It connects methodologically to broader efforts to operationalize and refine coordination detection ([[Mannocci2025-ig]], [[Minici2024-tf]], [[Luceri2025-tr]], [[Giglietto2025-1765bb4f]], [[Giglietto2026-9b6a992d]]) and speaks to wider debates on platform data access and the limits of list- and content-based approaches to information operations ([[Starbird2025-jj]], [[Gonzalez-Bailon2024-rq]]).
