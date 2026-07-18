---
title: "The challenges of working with platform data from clean room environments"
aliases: ["The challenges of working with platform data from clean room environments"]
authors: ["Axel Bruns", "Laura Vodden"]
year: 2026
doi: 10.25358/openscience-15825
bibtex_key: Bruns2026-pn
topics: [platform-governance-content-moderation, computational-methods-llms-social-media]
citation_count: 0
open_access: true
source_url: https://doi.org/10.25358/openscience-15825
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bruns2026-pn.mp3
pdf_available: true
discovery_date: 2026-07-18T06:28:38.387562Z
---

# The challenges of working with platform data from clean room environments

> Bruns, A., & Vodden, L. (2026). The challenges of working with platform data from clean room environments. *Gutenberg Open Science*. https://doi.org/10.25358/openscience-15825
>
> [View paper](https://doi.org/10.25358/openscience-15825)

## Summary

This report offers an early critical assessment of the emerging "clean room" model of researcher access to platform data, in which analysis takes place inside platform-hosted, Web-disconnected environments rather than through traditional API downloads. Taking the Meta Content Library (MCL) as its primary case — alongside ProQuest's TDM Studio — Bruns and Vodden argue that while such environments do address legitimate privacy and copyright concerns, their design substantially restricts *who* can conduct research and *what kinds* of research remain possible. The paper situates itself in the ongoing political communication and internet studies conversation about the "APIcalypse" and the shift from permissive APIs toward enclosed "walled garden" access regimes, and it urges regulators to look beyond whether access exists to whether that access is genuinely useful.

## Key Contributions

- Provides one of the first critical evaluations of whether clean room access models are fit for purpose for independent, public-interest research.
- Documents the technical architecture and evolution of the MCL's access frameworks (from CrowdTangle through the Virtual Data Enclave to the Secure Research Environment) for the research record.
- Articulates a structured taxonomy of clean room limitations spanning required skills, permitted tools, methodological breadth, longitudinal capacity, and cross-platform comparison.
- Frames data-access equity as a Global North versus Majority World issue, highlighting reinforced WEIRD/English-language bias.
- Offers guidance to legislators and regulators (e.g. under EU DSA Article 40) to move beyond baseline access requirements toward assessing genuine researcher usefulness.

## Methods

The paper is a conceptual and critical analysis, situated historically in the evolution of platform data access from permissive APIs through the "APIcalypse" to clean rooms. It combines a case-study description of the MCL and its predecessor CrowdTangle, a comparative reference to ProQuest's TDM Studio, and the authors' own hands-on experience navigating clean room accreditation, access, and analysis workflows.

## Findings

- The MCL replaced CrowdTangle (decommissioned August 2024), cutting data access precisely during the final phase of the 2024 US presidential election.
- The original Virtual Data Enclave required a cumbersome multi-layered login (virtual Windows → virtual Linux → Jupyter Notebook) and was exceptionally slow outside the US.
- The newer Secure Research Environment streamlines access but mandatorily deletes all accessed data monthly, obstructing longitudinal work.
- Analysis is confined to Jupyter Notebooks with Python or R and a limited provider-approved toolset, excluding industry-standard software (Tableau, Power BI, NVivo, MaxQDA).
- Web disconnection prevents use of commercial LLMs for coding, and open-source LLMs are constrained by allocated memory and disk.
- Clean rooms exist in isolation, blocking data combination across platforms; cross-platform work is limited to parallelised analysis of aggregate outcomes.
- The EU has begun proceedings against Meta and TikTok for failing transparency and data-access obligations under the DSA.

## Connections

This paper sits at the intersection of platform governance and computational method, and connects to broader work on independent scrutiny of platforms and DSA-era data-access regimes such as [[Rieder2026-pp]], [[Rieder2025-ju]] and [[Bechmann2026-dr]]. Its concern that restrictive access models privilege quantitative, code-based work over qualitative and mixed methods speaks to methodological debates in studies like [[Jurg2025-ur]] and [[Rogers2025-sl8f]], while its documentation of the CrowdTangle/MCL transition complements empirical platform-data studies including [[Bruns2025-fz]] and [[Bruns2026-yv]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bruns2026-pn.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
