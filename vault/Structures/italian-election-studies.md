---
type: structure
slug: italian-election-studies
topic: "Italian Election Studies"
---

# Italian Election Studies

## From Hybrid Media to Platform Manipulation: An Arc of Inquiry

The earliest paper in this line, [[Iannelli2015-e0818c3e]], predates the MINE programme's explicit election-studies agenda but sets its foundational premise: Italian political communication cannot be understood by looking at social media in isolation from television. Studying the 2013 campaign's talk-show/Twitter nexus, it finds narrow, TV-driven participation rather than autonomous networked publics — a cautionary baseline against treating platforms as independent causal forces. This hybrid-media sensibility quietly persists in later work, even as the empirical focus shifts from second-screening to the structural dynamics of partisan news circulation and coordinated manipulation.

## Partisan Attention and the Architecture of Insularity

[[Giglietto2019-882f1900]] opens the programme's signature empirical line proper, mapping the 2018 general election through combined Twitter (partisan attention, insularity) and Facebook (engagement) data. Its central discovery — that populist-aligned news sources (M5S, League) are more insular, and that insularity predicts a shift from "contestation" (comments) toward "amplification" (shares) — establishes a recurring analytic vocabulary for the whole topic: partisan selective exposure is not uniform but strategically exploitable, with M5S emerging as an "anti-elitist cyber party" uniquely skilled at mobilizing asymmetric sharing/commenting patterns around positive versus negative coverage. This paper frames populism's media success as inseparable from fragmented hybrid ecologies, directly anticipating the coordinated-network findings that follow.

## Coordination as the Unit of Analysis

[[Giglietto2020-9d8acdd7]] marks a methodological pivot: rather than classifying actors or content as disinformation, it operationalizes *coordinated link sharing behavior* across the 2018 and 2019 campaigns, showing that coordinated networks are dramatically more likely to circulate problematic domains and previously flagged disinformation sources. Its typology — openly political networks with diverse sourcing versus "non-political" cloaked networks concentrating on narrow, often problematic domains — supplies an ecological, behavior-first framework that reframes the insularity findings of [[Giglietto2019-882f1900]] in structural, network terms rather than audience-attitude terms. Where the earlier paper asked how partisans engage differently with news, this one asks how entities act together to manufacture that engagement.

[[Giglietto2023-fa71a001]] extends this logic to the 2022 snap election, addressing the key limitation of list-based detection: coordinated actors mutate faster than static blacklists can track. Its iterative, actor-agnostic workflow — seeded from known coordinated accounts and expanded via near-duplicate detection of overperforming posts — surfaces three qualitatively distinct operations (an M5S-aligned hyperpartisan echo-chamber network, a religious-clickbait commercial operation, and a covert religious-proselytism network using Messenger bots). This case-study diversity demonstrates that the coordination paradigm first tested in [[Giglietto2020-9d8acdd7]] generalizes beyond classic political disinformation to ideologically, commercially, and religiously motivated manipulation alike, while confirming continuity in actors (the M5S-adjacent network recurs across both election cycles).

## The Methodological Turn: Scaling Analysis with LLMs

As the empirical scope expands from single-election snapshots to multi-year comparison (2018 vs. 2022), the programme confronts a scaling problem in classifying and clustering vast volumes of shared political content — addressed in a pair of closely linked methodological papers. [[Giglietto2024-cbeb3f70]] benchmarks OpenAI's text-embedding-3-large against the Italian-specific UmBERTo model for clustering political news shared on Facebook before the two elections, finding the LLM embedding consistently superior regardless of clustering algorithm, though overall cluster coherence degrades from 2018 to 2022 — a finding that itself hints at the increasingly fragmented, less thematically coherent political news ecology the 2022 coordinated-networks work was documenting qualitatively.

[[Marino2024-2fbc690f]] builds directly on this result, embedding the validated embedding model into a full "LLMs-in-the-loop" pipeline (classification, clustering, labeling) applied to the same 2018/2022 comparison, and confronting the harder problem of *validating* such pipelines. Its argument — that LLMs now often outperform crowdsourced human coders, demanding expert rather than crowd validation, and that narrative granularity requires multi-level rubrics — reflects the programme's broader trajectory: as the empirical questions (insularity, coordination, hyperpartisanship) stabilize, the methodological apparatus for detecting them must itself become an object of scrutiny and innovation.

## Political Parallelism and the Rhetoric of Delegitimization

[[Mosca2026-yh]] approaches the Italian media-politics nexus from a different angle, theoretical rather than computational: its Strategic Delegitimization and Selective Amplification (SDSA) model reframes "fake news" accusations themselves as weapons in negative campaigning, selectively amplified by partisan newspapers. This complements the coordination and insularity findings by supplying the normative-discursive counterpart to the platform-level mechanics documented elsewhere — where [[Giglietto2019-882f1900]] and [[Giglietto2020-9d8acdd7]] show *how* partisan networks amplify or contest content, Mosca's model explains *why* accusations of fakeness circulate strategically within that same political-parallelism logic, linking the programme's social-media focus back to the legacy press and Italy's polarized-pluralist media system.

## Synthesis

Read together, these seven papers trace a coherent arc: from establishing that Italian political communication is irreducibly hybrid ([[Iannelli2015-e0818c3e]]), to mapping partisan insularity as a structural feature of the 2018 campaign ([[Giglietto2019-882f1900]]), to reconceiving disinformation as coordinated behavior rather than bad content or bad actors ([[Giglietto2020-9d8acdd7]], [[Giglietto2023-fa71a001]]), to building and validating the computational infrastructure necessary to study these dynamics at scale across elections ([[Giglietto2024-cbeb3f70]], [[Marino2024-2fbc690f]]), and finally to theorizing the rhetorical deployment of "fake news" itself within Italy's politically parallel press ([[Mosca2026-yh]]). The throughline is a shift from describing partisan audiences to explaining the orchestrated, increasingly LLM-studied mechanics that produce and weaponize partisan visibility.
