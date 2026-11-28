---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, italian-electoral-communication]
citation_count: 25
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

This paper presents a methodological workflow for detecting, monitoring, and continuously updating lists of coordinated social media accounts that spread problematic information. The authors' central argument is that static, manually compiled lists of malicious actors become outdated quickly — actors adapt, get suspended, or shift assets — leading to systematic underestimation of an operation's true reach. Their solution is a circular, near-real-time pipeline: beginning from a seed list of known coordinated accounts, it monitors their best-performing posts every few hours and uses near-duplicate detection to surface new accounts engaged in coordinated sharing behavior. The approach is deliberately content- and actor-agnostic, targeting behaviors rather than predetermined individuals or content. Applied to the 2022 Italian snap election, it grew a 435-account seed into 620 newly detected coordinated accounts, illustrated through three case studies spanning ideological, economic, and religious motivations.

## Key Contributions

- An iterative workflow that updates coordinated-account lists in near-real-time rather than relying on static lists.
- Extends Coordinated Link Sharing Behavior (CLSB) detection via CooRnet by adding Coordinated Image Text Sharing Behavior (CITSB) and Coordinated Message Sharing Behavior (CMSB), capturing coordination through images and near-duplicate text — addressing adaptation tactics like placing links in comments.
- Empirical application to the 2022 Italian election, yielding three documented case studies.
- A behaviorally agnostic alert system to help fact-checkers, journalists, and researchers prioritize investigations, with the caveat that flagged content/actors are not automatically harmful.
- Discussion of portability to other platforms via emerging researcher APIs, framed around EU Digital Services Act Article 40 data access provisions.

## Methods

The authors designed a circular workflow combining scheduled API monitoring, overperformance scoring (CrowdTangle's overperforming score plus a combined metric weighting comment/share ratios), and coordination detection. The seed list of 435 accounts was compiled by running CooRnet on 73,842 links from 398,385 political posts published by accounts previously identified in the 2018, 2019, and COVID-era Italian coordination studies. An R script scheduled via cronR queried the CrowdTangle posts/search API every six hours from July 28 to September 25, 2022, retrieving top overperforming political and unfiltered posts plus posts from the top 10% of newly detected accounts. CooRnet (30-second interval, 26+ share repetition at the 0.995 percentile) detected CLSB, with extensions for CITSB and CMSB (cosine similarity > .7). Political posts were filtered via a keyword list with capitalization checks, and the three case studies were analyzed using François's A-B-C (Actors-Behavior-Content) framework and NewsGuard reliability ratings.

## Findings

- Surfaced 1,022 overly shared/commented political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 generic coordinated accounts beyond the seed list.
- **Case 1 (M5S hyperpartisan network):** 90 entities with potential reach of ~1.5M users, publishing 534,353 posts in two months (6.2 posts/min on election day, peaking above 50/min); 80% of posts had no links and most linked content was Facebook-internal, forming an echo chamber circulating fabricated pro-M5S polls.
- **Case 2 (clickbait operation):** 46 Pages publishing 58,035 posts; two religious Pages (combined ~768,000 followers) posted two-thirds non-religious political clickbait with misleading headlines, incidentally exposing religious audiences to political content.
- **Case 3 (religious proselytism):** 1,390 public groups tied to the Church of Almighty God across seven language clusters; the Italian subset had 61 groups (~1.7M members) and 13 Pages (~295k subscribers), with Pages averaging 72.6 administrators and using Messenger bots to funnel users into catechism chats without disclosing affiliation.
- Only 2% of external M5S-network links came from NewsGuard-rated unreliable sources, but 76% were unrated; reliable links came mostly from ideologically aligned outlets.

## Connections

This paper directly extends the authors' own program of research on Coordinated Link Sharing Behavior in Italian elections — see [[Giglietto2020-9d8acdd7]], [[Giglietto2020-6278a4aa]], [[Giglietto2019-882f1900]], [[Giglietto2024-cbeb3f70]], and [[Marino2023-9137f448]] — building the CooRnet detection lineage into a continuous, updating workflow. It sits within the broader coordinated-inauthentic-behavior literature on actor- and behavior-focused detection, connecting to [[Nizzoli2020-cf]], [[Keller2019-nk]], and [[Starbird2019-qv]], and to the Italian electoral communication strand via [[Iannelli2015-e0818c3e]] and [[Mannocci2025-ig]].
