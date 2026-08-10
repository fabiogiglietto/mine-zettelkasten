---
title: "Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking"
aliases: ["Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking"]
authors: ["Fabio Giglietto", "Manolo Farci", "Giada Marino", "Serena Mottola", "Tommaso Radicioni", "Massimo Terenzi"]
year: 2022
doi: 10.31235/osf.io/6umqs
bibtex_key: Giglietto2022-0e951ac5
kind: own
topics: [coordinated-inauthentic-behavior, health-misinformation-global-south]
citation_count: 8
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

This report presents MINE-FACTS, an Italian project that operationalizes Coordinated Link Sharing Behavior (CLSB) detection into a prototype dashboard for fact-checkers. Building on the CooRnet R package, the authors argue that content-agnostic, behavior-based signals can surface problematic COVID-19 information on Facebook faster and with higher precision than traditional content-based triage. Through iterative CooRnet runs seeded from IFCN-verified false claims, the team maps Italian "nefarious" coordinated networks at macro, meso, and micro levels, documents the emergence of a covid-skeptic cluster grafted onto pre-existing partisan (League, Five Star Movement) coordinated infrastructures, and catalogues the evasion tactics these actors deploy. A one-month operational test with Facta.news showed the tool flagged problematic content at roughly 40% versus ~28% in routine third-party fact-checking.

## Key Contributions

- An operational prototype integrating CooRnet, CrowdTangle, and IFCN data into a live fact-checking workflow.
- A multi-scale (macro/meso/micro) map of Italian coordinated networks spreading COVID-19 misinformation.
- Documentation of novel evasion tactics: first-comment link placement, image-macro "link laundering," shared AdSense/Analytics IDs across domains, and Page rebranding.
- Empirical evidence that behavior-based detection outperforms content-based triage for surfacing problematic content.
- Methodological demonstration of *iterative* CooRnet seeding as a way to dynamically expand coordinated-account inventories.
- OSINT reconstructions (WHOIS, reverse WHOIS, AdSense IDs, Wayback Machine) attributing specific domains and operators behind disinformation operations.

## Methods

The authors use Meta's URL Shares dataset and CrowdTangle to build corpora of widely circulated Italian links, seeded from 212 IFCN-listed false claims (1,258 URLs). CooRnet detects CLSB across Pages, public groups, and verified profiles; the process is iterated, with each cycle seeding the next from links posted by already-identified coordinated accounts. Macro-level structure is visualized via Force Atlas 2; four meso-level case studies (Blogspot conspiracy blogs, a Catholic-themed group cluster, a GEDI/Repubblica link-laundering Page network, and the Mag24 network) are analyzed using Camille François's Actors–Behavior–Content framework and OSINT. A November 2021 pilot deployment with Facta.news evaluated hit rates against a veracity typology.

## Findings

- Feb–June 2020 top Italian links favored partisan, oversimplified framings (e.g., a Tgcom24 "bioweapon" piece with 15M+ views; 5G/COVID YouTube videos, later removed).
- Initial CooRnet run identified 30 Pages (2.1M followers) and 308 groups (2.73M members) in CLSB; interactions on conspiracy groups roughly tripled during lockdown.
- A second iteration surfaced 344 coordinated accounts forming a giant political component with 5 conspiracy sub-clusters; the largest covid-skeptic cluster overlapped with League- and Five Star Movement–affiliated accounts.
- The final 2021 network comprised 2,151 accounts (242 Pages, 1,900 groups) in 89 components, with bridging groups linking covid-skeptic, political, and religious communities.
- Case studies exposed AdSense-based monetization across Blogspot conspiracy blogs, "link laundering" driving traffic to reputable GEDI outlets, and image-macro tactics in the Mag24 network (tied via OSINT to Francesco Soro).
- Unprincipled "celebrities" (Montagnier, Viganò, Kennedy) form a symbiotic amplification loop with covid-skeptic communities, and quotes genuinely uttered by them evade "false" ratings.
- Comments-to-shares ratios differ significantly between problematic and non-problematic content, offering a useful ranking signal.
- In the pilot, ~40% of prototype-surfaced items were problematic vs. ~28% in routine fact-checking.

## Connections

This paper is a direct outgrowth of the CooRnet research program and its application to Italian information ecosystems, extending [[Giglietto2020-9d8acdd7]] and [[Giglietto2023-fa71a001]] and connecting to related Italian-context work in [[Ghezzi2023-8bebc91f]], [[Marino2023-9137f448]], and [[Giglietto2026-9b6a992d]]. Its emphasis on content-agnostic, link-based coordination detection aligns methodologically with [[Ducci2022-10cb5d70]] and speaks to broader debates about behavior-based CIB detection represented in works such as [[Graham2025-gp]] and [[Luceri2025-tr]]. The focus on health misinformation and covid-skeptic amplification connects to concerns explored in [[Kim2026-br]] and [[Righetti2025-slf9]].
