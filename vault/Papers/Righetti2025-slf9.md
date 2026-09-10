---
title: "Mainstreaming and transnationalization of anti-gender ideas through social media: the case of CitizenGO"
aliases: ["Mainstreaming and transnationalization of anti-gender ideas through social media: the case of CitizenGO"]
authors: ["Nicola Righetti", "Aytalina Kulichkina", "Bruna Almeida Paroni", "Zsofia Fanni Cseri", "Sofia Iriarte Aguirre", "Kateryna Maikovska"]
year: 2025
doi: 10.1080/1369118x.2025.2470229
bibtex_key: Righetti2025-slf9
kind: team
submitted_by: "Nicola Righetti"
slack_permalink: https://minesmd.slack.com/archives/C0BDU82EBHQ/p1783507450330309
topics: [coordinated-inauthentic-behavior, information-disorder-misinformation]
citation_count: 5
open_access: false
source_url: https://doi.org/10.1080/1369118x.2025.2470229
podcast_url: 
pdf_available: true
discovery_date: 2026-07-08T13:08:04.166491Z
---

# Mainstreaming and transnationalization of anti-gender ideas through social media: the case of CitizenGO

> Righetti, N., Kulichkina, A., Paroni, B. A., Cseri, Z. F., Aguirre, S. I., & Maikovska, K. (2025). Mainstreaming and transnationalization of anti-gender ideas through social media: the case of CitizenGO. *Information, Communication & Society*. https://doi.org/10.1080/1369118x.2025.2470229
>
> [View paper](https://doi.org/10.1080/1369118x.2025.2470229)

## Summary

This paper offers the first systematic, large-scale empirical account of how the transnational anti-gender organization CitizenGO uses social media to mainstream and globalize its agenda. Drawing on a decade (2013–2022) of activity across Facebook, Twitter, Instagram, and Telegram, the authors distinguish a *core network* of CitizenGO's own multilingual accounts from a broader *amplification network* of accounts that redistribute its content. They argue that CitizenGO is not a grassroots, member-driven organization but a centrally coordinated apparatus run from its Spanish headquarters, and that anti-gender narratives function as transnational "symbolic glue" binding right-wing, religious, and pro-life communities across language borders. The study emphasizes that the *structure* of online networks — including signs of coordination and astroturfing — is as important as content for understanding how radical ideas globalize.

## Key Contributions

- First systematic, decade-long, multi-platform empirical analysis of CitizenGO's social media communication.
- Introduces and operationalizes the paired concepts of *core network* and *amplification network* for studying digital advocacy mainstreaming.
- Empirically demonstrates anti-gender content acting as transnational "symbolic glue" in social media diffusion.
- Bridges literatures on the anti-gender movement, digital advocacy organizations, coordinated inauthentic behavior, and the mainstreaming of radical positions.
- Provides a structural rather than purely content-based perspective on transnational anti-gender networks.
- Methodological contribution combining structural topic modeling, co-sharing network analysis, and coordination detection on multilingual data.

## Methods

The authors combined open-source intelligence (LinkedIn, job ads, Facebook transparency data, Wayback Machine) to reconstruct CitizenGO's organizational structure with social media data gathered via the Twitter API, CrowdTangle, and manual Telegram searches (also collecting comparison data for Avaaz and Change.org). They scraped 3,165 of 3,413 petition URLs to identify authorship and signatures, and ran structural topic modeling (R `stm`, 100-topic model) on 24,401 Google-translated Facebook posts. Gini coefficients measured how evenly topics distributed across national pages. A co-URL sharing network was built with CooRTweet, using Louvain community detection and native-speaker qualitative coding, plus a narrow 2.5-hour co-sharing window to detect closely coordinated accounts. Wilcoxon rank-sum tests compared skewed engagement metrics.

## Findings

- The core network spans 18 Facebook, 8 Twitter, 6 Instagram, and 1 (inactive) Telegram accounts, with Facebook dominant in followers and engagement.
- CitizenGO initiated 54.4% of petitions shared on its pages, and these gathered significantly more signatures than externally initiated ones.
- Every national Facebook page has an administrator based at the Spanish headquarters, indicating central control.
- Of 100 topics, 38 concerned abortion/pro-life issues (.40) and 19 addressed anti-gender issues (.19); "gender" ranked among the ten most frequent terms.
- Anti-gender topics were more evenly distributed across national pages (Gini 0.77) than pro-life topics (Gini 0.88), supporting the "symbolic glue" argument.
- The amplification network of 19,176 accounts has a highly active core of 212 accounts (25M+ cumulative followers): right-wing political (36.2%), less partisan political (15.3%), pro-life/anti-gender (28.6%), and religious (18.4%).
- Linguistic clusters vary in centralization: Spanish-English most centralized (star-configured around CitizenGO/HazteÓir affiliates), Portuguese least centralized (Bolsonarist-aligned Facebook groups), and Hungarian (Fidesz-aligned, anti-EU, anti-LGBTQ+).
- A tightly coordinated subnetwork of 148 accounts posts CitizenGO URLs within 2.5 hours across 11 languages, suggesting astroturfing.
- CitizenGO's website homepage became visually near-identical to Change.org's by June 2022, imitating progressive advocacy for legitimacy.

## Connections

This paper's use of co-sharing and coordination detection connects directly to the CooRTweet and coordinated-link-sharing methodology developed in [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], and [[Giglietto2019-e9be81c1]], and to related coordinated-behavior work such as [[Righetti2025-sl2a]] and [[Kulichkina2025-sl09]]. Its focus on the transnational mainstreaming of anti-gender and far-right ideas resonates with [[Askanius2026-de]] on far-right digital cultures.
