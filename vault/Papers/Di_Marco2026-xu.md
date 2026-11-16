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
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Di_Marco2026-xu.mp3
pdf_available: false
discovery_date: 2026-09-27T17:35:50.397443Z
---

# Optimal and heuristic strategies for evaluating the influence of coordinated behavior in information cascades and retweet networks

> Marco, N. D., Cinelli, M., Nakano, S., & Frosini, A. (2026). Optimal and heuristic strategies for evaluating the influence of coordinated behavior in information cascades and retweet networks. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2609.24398v1)

## Summary

This paper tackles a problem that has received far less attention than it deserves: once coordinated inauthentic accounts have been detected, how much do they actually *matter* for how information spreads? The authors argue that the field has become preoccupied with detection while neglecting the quantification of influence. To close this gap, they introduce two complementary formal frameworks for the post-hoc evaluation of coordinated accounts — one operating over information cascades and one over retweet networks — and develop both optimal and heuristic strategies for measuring the diffusion impact of these accounts. The contribution is largely methodological and computational, drawing on network science to reframe the disciplinary conversation from "is this coordinated?" toward "how much influence did this coordination exert?"

## Key Contributions

- Two complementary frameworks for *quantifying* (rather than merely detecting) the influence of coordinated inauthentic accounts.
- A formal treatment of the influence-evaluation problem within information cascades.
- An analogous formulation over retweet networks as a second evaluation setting.
- Both optimal solution strategies and heuristic approximations for assessing coordinated impact.

## Methods

The work is formulated as a post-hoc evaluation problem, taking already-identified coordinated accounts as input. Two settings are modelled: information cascades and retweet networks. For each, the authors formalise the task of measuring influence and propose both exact (optimal) strategies and heuristic approximations — the latter presumably to handle the computational cost of optimal solutions at scale. Specific empirical results are not available in the abstract excerpt provided.

## Findings

- Detailed empirical findings are not reported in the available summary; the contribution is primarily framework and algorithm design.
- Positions optimal strategies alongside heuristics, implying a trade-off between exactness and tractability for influence estimation.

## Connections

This paper sits squarely in the CIB literature's pivot from detection to consequence, complementing detection-focused work such as [[Nizzoli2020-cf]] and the coordination-detection program of [[Giglietto2020-9d8acdd7]] and [[Giglietto2022-0e951ac5]] by asking what detected coordination actually accomplishes in diffusion terms. Its network-science treatment of retweet networks and influence connects to broader analyses of coordinated influence and its effects such as [[Luceri2025-tr]] and [[Minici2024-tf]], and shares an author and methodological lineage with [[Di-Marco2025-aa]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Di_Marco2026-xu.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
