---
title: "COORNET: AN INTEGRATED APPROACH TO SURFACE PROBLEMATIC CONTENT, MALICIOUS ACTORS, AND COORDINATED NETWORKS"
aliases: ["COORNET: AN INTEGRATED APPROACH TO SURFACE PROBLEMATIC CONTENT, MALICIOUS ACTORS, AND COORDINATED NETWORKS"]
authors: ["Fabio Giglietto", "Nicola Righetti", "Luca Rossi", "Giada Marino"]
year: 2021
doi: 10.5210/spir.v2021i0.12170
bibtex_key: Giglietto2021-ff088d6a
kind: own
topics: [coordinated-inauthentic-behavior, problematic-health-information]
citation_count: 0
open_access: true
source_url: https://doi.org/10.5210/spir.v2021i0.12170
podcast_url: 
pdf_available: true
discovery_date: 
---

# COORNET: AN INTEGRATED APPROACH TO SURFACE PROBLEMATIC CONTENT, MALICIOUS ACTORS, AND COORDINATED NETWORKS

## Summary

This short conference paper introduces **CooRnet**, an R package that detects *Coordinated Link Sharing Behavior* (CLSB) on Facebook by flagging sets of accounts that repeatedly share the same URLs within unusually short time windows. The authors argue that neither content-based approaches (slowed by fact-checking) nor static actor lists can keep up with evolving information operations, and propose instead an operationalization of Camille François's **Actors–Behaviors–Content (A-B-C)** framework as an *iterative cycle*: start from harmful content, surface coordinated behavior, identify the actors involved, then re-seed with content from those actors. A case study on Italian COVID-19 misinformation across the first two pandemic waves demonstrates the workflow, surfacing networks centered on skepticism, anti-vaccine, and anti-mask narratives.

## Key Contributions

- An open-source R package (CooRnet) implementing CLSB detection on CrowdTangle-tracked Facebook data, with reproducible outputs: coordinated-entity lists, marked share data, network projections, component summaries, and timeline visualizations.
- A concrete operationalization of the A-B-C disinformation framework as a repeatable detection loop rather than a static taxonomy.
- Empirical extension of CLSB methods from electoral contexts to health misinformation (COVID-19 in Italy).
- A methodological argument that integrating actors, behaviors, and content iteratively yields broader and more resilient detection than any single dimension alone.

## Methods

The pipeline begins with 212 Italian false/misleading COVID-19 claims (Jan–Aug 2020) drawn from the IFCN CoronaVirus Alliance database. These are expanded via CrowdTangle Search into 1,258 related URLs, whose Facebook shares are collected with `get_ctshares()`. Coordinated shares are then identified by `get_coord_shares()`, which flags multiple actors sharing the same link within an anomalously short interval, with a repeat-co-share threshold to reduce false positives. Outputs are generated via `get_outputs()` and `draw_url_timeline_chart()`. The A-B-C cycle is closed by feeding URLs shared by the detected actors (October 2020 collection, 59,346 URLs) back into the pipeline for a second iteration.

## Findings

- Iteration 1: 13,271 shares of 1,258 fact-check-related URLs yielded **152 coordinated entities**.
- Iteration 2: re-seeding with actor-produced URLs expanded the dataset to 364,400 shares and **344 coordinated entities**, more than doubling the actor set.
- Top coordinately shared URLs were dominated by COVID-19 skepticism, anti-vaccine, and anti-mask narratives.
- The iterative loop materially extends detection beyond what a single content- or list-based pass produces.

## Connections

This paper is foundational for the CLSB/CooRnet line of work and connects directly to the authors' subsequent applications and refinements of the method, including [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], [[Marino2024-a678b03f]], and [[Ghezzi2023-8bebc91f]]. Its iterative A-B-C operationalization is methodologically adjacent to more recent coordination-detection frameworks such as [[Graham2025-gp]] and [[Luceri2025-tr]], and its health-misinformation case study links it to broader work on coordinated amplification of problematic content like [[Kulichkina2026-zk]].
