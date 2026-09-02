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
podcast_url: 
pdf_available: true
discovery_date: 2026-09-02T09:27:53.029363Z
---

# Searching for the truth? search engines and their AI affordances’ responses to conspiratorial search practices

> Kasianenko, K., Gardam, C., FitzGerald, K. M., Nagappa, A., Bruns, A., Weinbrand, S., Angus, D., Vilkins, S., & Obeid, A. K. (2026). Searching for the truth? search engines and their AI affordances’ responses to conspiratorial search practices. *Media International Australia*. https://doi.org/10.1177/1329878x261481856
>
> [View paper](https://doi.org/10.1177/1329878x261481856)

## Summary

This paper investigates how Google Search and its AI Overview (AIO) feature respond differently to conspiratorial versus general information-seeking, using two conspiracy theories as contrasting cases: the long-established chemtrails theory and the newer 15-minute cities theory. Through an algorithmic audit conducted from Sydney over one week in January 2026, the authors show that query framing—specifically whether it reflects conspiratorial modes of reasoning—materially changes the information a user is exposed to. Their central argument is that Google's content moderation and AIO guardrails work only unevenly: they partially succeed for entrenched theories like chemtrails but frequently fail for emergent narratives, sometimes even legitimising conspiratorial claims by presenting them as "debates" or "fears."

## Key Contributions

- Introduces query sets grounded in **authentic conspiratorial community knowledge practices** harvested from real online forums (Instagram, Reddit, geoengineering FAQs), moving beyond audits reliant on short, purposive, or news-sourced queries.
- Delivers one of the first algorithmic audits assessing Google's **AI Overviews** specifically for conspiratorial content and query-framing sensitivity.
- Adapts the social-media **"practice mapping"** method to visualise similarity across search result sets—a novel analytic technique for search audits.
- Offers a comparative, longitudinal case study contrasting an **established vs. emergent** conspiracy theory, showing weaker guardrails for newer narratives.
- Highlights the underexamined role of **commercial sources** and SEO/GEO/AEO optimisation in surfacing conspiratorial content.

## Methods

The authors ran a virtual agent-based audit of Google Search and AIOs twice daily over seven days (14–20 January 2026), collecting 1,629 search page observations, 17,298 URLs, and 1,342 AIOs referencing 863 unique sources via Selenium, Beautiful Soup, and Regex. Query sets (65 chemtrails, 53 15-minute cities) were drawn from real conspiratorial and non-conspiratorial forums plus Google Trends. Analysis combined: network-based practice mapping (top-10 URLs vectorised, compared via cosine similarity, visualised in Gephi with Force Atlas 2); source-concentration analysis using the Jaccard Index with manual content coding (Krippendorff's α = 0.78); and stance coding of 80 sampled AIOs (mentions/debunks/promotes; intercoder reliability 0.76).

## Findings

- Results for conspiratorial queries diverge markedly from general queries, and diverge further as queries drift toward conspiratorial ideation; localised queries (naming Melbourne, Oxford) produce distinct result sets.
- Conspiratorial queries returned more news media (often reputable debunking) and more social media (some conspiratorial); general queries returned more government sources—especially for chemtrails—indicating official-source prioritisation as a moderation strategy.
- Moderation failures observed: a European Parliament page surfacing conspiratorial tropes without a clear debunking link; Amazon links to conspiracy-promoting books returned only for conspiratorial queries.
- For 15-minute cities, more commercial explainers and explicit conspiratorial YouTube content appeared, with weaker moderation than chemtrails.
- AIOs largely debunked chemtrails conspiratorial queries, but 5 of 40 analysed 15-minute cities AIOs actively promoted the conspiracy by framing it as legitimate "debate," "fears," or "misconceptions."
- AIO debunking was often brief and unsupported; AIO sources overlapped substantially with organic results (Jaccard ~0.48); commercial sources were even more prominent in AIOs; conspiratorial queries yielded lower-quality AIOs (unexplained acronyms, an untranslated Japanese word).

## Connections

This paper sits at the intersection of platform-governance and computational content analysis, extending prior algorithmic audit work into the generative-AI search era. It connects to broader debunking and misinformation-correction scholarship such as [[van-der-Linden2026-jt]] and [[Lewandowsky2026-ob]], and to work on data voids and search-engine information quality relevant to its "do your own research" framing. Its focus on the platform governance implications of AI-mediated affordances aligns it with [[Katzenbach2026-sl2e]] and [[Gillespie2010-sla2]].
