---
title: "Optimal and heuristic strategies for evaluating the influence of coordinated behavior in information cascades and retweet networks"
aliases: ["Optimal and heuristic strategies for evaluating the influence of coordinated behavior in information cascades and retweet networks"]
authors: ["Niccolò Di Marco", "Matteo Cinelli", "Shinichi Nakano", "Andrea Frosini"]
year: 2026
doi: 
bibtex_key: Di_Marco2026-xu
topics: [coordinated-inauthentic-behavior]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2609.24398v1
podcast_url: 
pdf_available: false
discovery_date: 2026-09-27T17:35:50.397443Z
---

# Optimal and heuristic strategies for evaluating the influence of coordinated behavior in information cascades and retweet networks

> Marco, N. D., Cinelli, M., Nakano, S., & Frosini, A. (2026). Optimal and heuristic strategies for evaluating the influence of coordinated behavior in information cascades and retweet networks. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2609.24398v1)

## Summary

This paper tackles a problem that has received far less attention than the detection of Coordinated Inauthentic Behavior (CIB): once coordinated accounts have been identified, how much did they actually *influence* the diffusion of information? The authors argue that the field has overinvested in detection while leaving the quantification of impact poorly understood. To close this gap, they introduce two complementary frameworks for post-hoc evaluation of coordinated accounts, formulating the influence-evaluation problem on both information cascades and retweet networks, and offering both optimal and heuristic strategies for computing that influence.

## Key Contributions

- Two complementary frameworks that shift the analytical goal from *detecting* coordination to *quantifying* its influence on diffusion.
- A formal treatment of the influence-evaluation problem within information cascades.
- An extension of the analysis to retweet networks as a second structural setting.
- Both optimal solution strategies and heuristic approximations for measuring coordinated influence at scale.

## Methods

The approach is grounded in network science and computational treatments of information diffusion. The authors formalize the problem of estimating the contribution of a known set of coordinated accounts to a cascade's reach, working over information cascades and, separately, over retweet networks. They pair exact/optimal formulations with heuristic approximations intended to make the evaluation tractable on larger structures.

## Findings

- Specific empirical results are not reported in the abstract excerpt available; the contribution is primarily framework- and method-oriented.
- The framing establishes that influence quantification is a distinct and solvable problem separate from detection, amenable to both optimal and approximate solution.

## Connections

This work is a natural complement to the large body of CIB *detection* research — including coordination-detection methods such as [[Nizzoli2020-cf]], [[Minici2024-tf]], and the coordinated-link-sharing line of [[Giglietto2020-9d8acdd7]] and [[Giglietto2022-0e951ac5]] — by asking what should follow *after* coordinated accounts are found. Its focus on measuring influence over retweet and cascade structures connects it to network-based influence and campaign-impact studies like [[Luceri2025-tr]] and [[Gerard2025-br]], and it shares authorship lineage with [[Di-Marco2025-aa]].
