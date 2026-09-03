---
title: "Searching for the truth? search engines and their AI affordances’ responses to conspiratorial search practices"
aliases: ["Searching for the truth? search engines and their AI affordances’ responses to conspiratorial search practices"]
authors: ["Kateryna Kasianenko", "Caroline Gardam", "Katherine M. FitzGerald", "Ashwin Nagappa", "Axel Bruns", "Shir Weinbrand", "Daniel Angus", "Samantha Vilkins", "Abdul Karim Obeid"]
year: 2026
doi: 10.1177/1329878x261481856
bibtex_key: Kasianenko2026-tn
topics: [platform-governance-and-content-moderation, computational-methods-for-content-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1177/1329878x261481856
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kasianenko2026-tn.mp3
pdf_available: true
discovery_date: 2026-09-02T09:27:53.029363Z
---

# Searching for the truth? search engines and their AI affordances’ responses to conspiratorial search practices

> Kasianenko, K., Gardam, C., FitzGerald, K. M., Nagappa, A., Bruns, A., Weinbrand, S., Angus, D., Vilkins, S., & Obeid, A. K. (2026). Searching for the truth? search engines and their AI affordances’ responses to conspiratorial search practices. *Media International Australia*. https://doi.org/10.1177/1329878x261481856
>
> [View paper](https://doi.org/10.1177/1329878x261481856)

## Summary

This paper investigates how Google Search and its AI Overview (AIO) feature respond to conspiratorial versus general information-seeking practices, using two contrasting case studies: the well-established chemtrails theory and the emergent 15-minute cities theory. Through an algorithmic audit of first-page results and AIO responses to query sets grounded in real conspiratorial and non-conspiratorial online forums, the authors show that query framing materially changes what information users encounter. They argue that while Google's moderation and AI guardrails partially work for established conspiracy theories, they are unevenly applied and often fail for newer narratives — sometimes even legitimising conspiratorial claims by framing them as "debates" or "fears."

## Key Contributions

- Introduces query sets grounded in authentic conspiratorial community knowledge practices drawn from online forums (Instagram, Reddit, geoengineering FAQs), moving beyond prior audits that relied on short or news-sourced queries.
- Provides one of the first algorithmic audits of Google's AI Overviews specifically for conspiratorial content and query-framing sensitivity.
- Adapts the social-media "practice mapping" method to visualise similarity across search result sets — a novel analytic technique for search audits.
- Offers a comparative, longitudinal case study contrasting an established (chemtrails) and an emergent (15-minute cities) conspiracy theory.
- Highlights the underexamined role of commercial sources and SEO/GEO/AEO optimisation in surfacing conspiratorial content.

## Methods

The authors conducted a virtual agent-based algorithmic audit of Google Search (including AIOs) from Sydney, twice daily over seven days in January 2026. They built 65 chemtrails and 53 15-minute-cities queries from real conspiratorial and non-conspiratorial forums plus Google Trends, then scraped results with Selenium, Beautiful Soup, and Regex (1,629 search-page observations, 17,298 URLs, 1,342 AIOs referencing 863 unique sources). Analysis combined an adapted "practice mapping" technique (top-10 URLs vectorised, compared via cosine similarity, visualised in Gephi with Force Atlas 2), Jaccard-based source concentration analysis, manual content coding of source types (Krippendorff's alpha = 0.78), and stance coding of 80 sampled AIOs (intercoder reliability 0.76).

## Findings

- Search results for conspiratorial queries differed markedly from general queries, diverging more as queries drifted toward conspiratorial ideation; localised queries (naming Melbourne, Oxford, etc.) produced distinct result sets.
- Conspiratorial queries returned more news media (often debunking) and more social media posts (some conspiratorial), while general queries returned more government sources — especially for chemtrails, suggesting official-source prioritisation as a moderation strategy.
- Moderation failures appeared, e.g. a European Parliament page surfacing chemtrails tropes without a clear debunking link, and Amazon links to conspiracy-promoting books returned only for conspiratorial queries.
- The newer 15-minute cities theory saw weaker moderation, more commercial explainers, and explicit conspiratorial YouTube content.
- AIOs were sensitive to framing: they largely debunked chemtrails queries but, for 15-minute cities, 5 of 40 analysed AIOs actively promoted the conspiracy by framing it as "debate," "fears," or "misconceptions."
- AIO debunking was often brief and unsupported; AIO sources overlapped heavily with organic results (Jaccard ~0.48) and disproportionately featured commercial domains, with conspiratorial queries yielding lower-quality AIOs.

## Connections

This paper sits at the intersection of platform content moderation and computational auditing methods, and speaks directly to concerns about how generative AI mediates access to disputed knowledge. Its findings on AI Overviews surfacing brief, poorly evidenced debunks resonate with work on debunking and generative-AI interventions such as Costello2025 — though not in the provided list — and its focus on how conspiratorial communities practice "do your own research" complements studies of conspiracy and misinformation dynamics. Among the provided keys, the strongest genuine affinities are conceptual rather than direct; no listed paper addresses the same search-engine auditing terrain closely enough to warrant a specific link.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kasianenko2026-tn.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-when-search-engines-amplify-conspiracy/id1866587707?i=1000787390316)
