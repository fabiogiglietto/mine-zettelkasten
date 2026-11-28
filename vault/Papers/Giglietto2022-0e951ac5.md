---
title: "Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking"
aliases: ["Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking"]
authors: ["Fabio Giglietto", "Manolo Farci", "Giada Marino", "Serena Mottola", "Tommaso Radicioni", "Massimo Terenzi"]
year: 2022
doi: 10.31235/osf.io/6umqs
bibtex_key: Giglietto2022-0e951ac5
kind: own
topics: [coordinated-inauthentic-behavior, health-misinformation]
citation_count: 9
open_access: true
source_url: https://doi.org/10.31235/osf.io/6umqs
podcast_url: 
pdf_available: true
discovery_date: 
---

# Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking

> Giglietto, F., Farci, M., Marino, G., Mottola, S., Radicioni, T., & Terenzi, M. (2022). Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking. *Center for Open Science*. https://doi.org/10.31235/osf.io/6umqs
>
> [View paper](https://doi.org/10.31235/osf.io/6umqs)

## Summary

This report documents the MINE-FACTS project, which built and tested a content-agnostic prototype tool to help Italian fact-checkers surface problematic COVID-19 information on Facebook faster than manual methods allow. Building on the authors' prior work on Coordinated Link Sharing Behavior (CLSB) and the open-source CooRnet R package, the project maps Italian "nefarious" social media actors at macro, meso, and micro levels, documents the emergence of an Italian covid-skeptic coordinated network, and analyzes the evasion strategies these actors use to circumvent platform enforcement. The central argument is that behavior-based, content-agnostic detection can complement — and in triage terms outperform — traditional content-based fact-checking: a one-month operational test with Facta.news surfaced a significantly higher share of problematic content than routine third-party fact-checking.

## Key Contributions

- An operational prototype tool integrating CooRnet, CrowdTangle, and IFCN data into a real-time fact-checking workflow.
- An up-to-date, multi-scale map of Italian coordinated networks spreading COVID-19 misinformation.
- Documentation of novel evasion tactics: first-comment link placement, image-macro "link laundering," cross-platform monetization via shared AdSense IDs, and shape-shifting Page rebranding.
- Empirical evidence that content-agnostic behavioral detection can outperform content-based triage for surfacing problematic information.
- A methodological demonstration of iterative CooRnet seeding to dynamically expand inventories of coordinated accounts.
- Open-source-intelligence reconstructions tying specific domains, ad IDs, and individuals to disinformation operations.

## Methods

The authors drew on Meta's URL Shares dataset (Facebook Open Research Initiative) to identify widely circulated Italian links from February–June 2020, and seeded detection from 212 Italian false claims in the IFCN CoronaVirusFacts Alliance Database plus CrowdTangle searches. CooRnet was applied to detect CLSB across Pages, public groups, and verified profiles, using an iterative approach in which links from previously flagged accounts seed new detection cycles. Macro-level clusters were mapped via social network analysis (Force Atlas 2); meso-level case studies of four networks were analyzed through Camille François's Actors-Behavior-Content (ABC) framework; and attribution used OSINT techniques (WHOIS, reverse WHOIS, AdSense/Analytics ID matching, Wayback Machine). A one-month operational test (November 2021) evaluated the dashboard with Facta.news against a veracity typology.

## Findings

- During Feb–June 2020, partisan, oversimplified explanations (e.g., bioweapon and 5G claims) massively outperformed balanced coverage; a single bioweapon-claim article drew 15M+ views.
- Starting from 212 false claims and 1,258 URLs, CooRnet identified 30 Pages (2.1M followers) and 308 public groups (2.73M members) in CLSB; conspiracy-group interactions roughly tripled during lockdown.
- The Italian covid-skeptic coordinated network emerged as an offshoot of pre-existing political clusters, with its largest cluster overlapping League- and Five Star Movement-affiliated accounts; the final 2021 iteration tracked 2,151 accounts across 89 components.
- Case studies exposed distinct tactics: AdSense-monetized Blogspot cross-posting, a 62-group Catholic network injected with covid-skeptic content, a 31-Page "link laundering" operation driving traffic to reputable GEDI outlets, and the long-running Mag24 image-macro network attributed via WHOIS/AdSense traces.
- The prototype surfaced 70 links and 360 posts in testing; ~40% were rated problematic versus ~28% in routine third-party fact-checking.
- Problematic content shows a distinctive comments-to-shares ratio, with non-problematic content dominated by shares — a useful ranking signal.

## Connections

This work extends the authors' CLSB and CooRnet research program and sits directly alongside their related methodological papers on coordinated link sharing and detection [[Giglietto2020-9d8acdd7]], [[Giglietto2019-0bd8b768]], [[Giglietto2023-fa71a001]], [[Giglietto2026-9b6a992d]], [[Marino2023-9137f448]]. Its content-agnostic, behavior-based framing connects to broader studies of coordinated inauthentic behavior and platform manipulation such as [[Nizzoli2020-cf]], [[Starbird2019-qv]], and [[Keller2019-nk]], and its intersection of coordinated behavior with health misinformation during the "infodemic" links it to work on COVID-era false claims and fact-checking.
