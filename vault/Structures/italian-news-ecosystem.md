---
type: structure
slug: italian-news-ecosystem
topic: "Italian News Ecosystem (MINE)"
---

# Italian News Ecosystem (MINE)

## Italian News Ecosystem (MINE)

### From mapping partisan attention to interrogating platform power

The MINE line of work begins with a substantive question about Italian political communication and moves, over time, toward the infrastructural conditions under which such questions can even be asked. The 2018 election study [[Giglietto2019-882f1900]] is the empirical anchor: by triangulating Twitter-derived measures of source "insularity" with Facebook engagement on ~85k news stories, it documents that populist-aligned outlets (M5S, League) sit at the partisan extremes of the Italian news ecosystem, and that insularity translates into a distinctive share-versus-comment signature — amplification inside partisan enclaves, contestation across them. The Italian case is framed deliberately as a "polarized pluralist" stress test of echo-chamber and hybrid-media theories, and the finding that M5S supporters strategically *both* amplify favorable and contest hostile coverage complicates a clean self-segregation story.

### Methodological consolidation: scaling up the news corpus

If the 2018 paper relied on hand-adjudicated source-level partisanship, the embedding-model comparison [[Giglietto2024-cbeb3f70]] addresses the natural next bottleneck: how to make sense, *unsupervised*, of the substantive content flowing through this ecosystem at scale. Returning to the 2018 corpus and extending to 2022, it benchmarks OpenAI's `text-embedding-3-large` against the Italian-native UmBERTo for clustering political news, finding that the general-purpose LLM embedding wins on Grimmer-and-King-style coherence even in a non-English, domain-specific setting. The paper is in this sense infrastructural: it equips the MINE programme with a validated, cheap pipeline for thematic mapping of Italian political news, while flagging a methodological caveat — HDBSCAN's apparent quality gains are tightly correlated with discarding the bulk of the data as noise, an issue that matters when the goal is *representative* description of an ecosystem rather than recovery of crisp topics.

### The platform turn: visibility as governed object

The most recent contribution [[Giglietto2025-1e9a0917]] shifts register from describing the Italian news ecosystem to interrogating the platform layer that conditions it. Using 2.5M Facebook posts from Italian MPs, it identifies structural breakpoints showing that Meta's political content reduction was effectively active in Italy ten months before its announced global rollout, drove a 72% peak-to-trough collapse in per-post reach, and only partially reversed in 2025. Crucially, the effects are *asymmetric*: extremist accounts compensated through posting volume and ultimately overtook mainstream politicians in total weekly reach — a result that speaks directly back to the 2018 findings about populist actors' adeptness at exploiting attention economies [[Giglietto2019-882f1900]].

### An arc of inquiry

Read together, the three papers trace a coherent trajectory. The 2018 study establishes that partisan structure and populist advantage are legible in patterns of news circulation [[Giglietto2019-882f1900]]; the embeddings study upgrades the toolkit needed to sustain that mapping across elections and at content-level granularity [[Giglietto2024-cbeb3f70]]; and the Meta visibility paper reframes the dependent variable itself, arguing that any longitudinal account of Italian political communication must now treat algorithmic visibility regimes as endogenous, opaque, and consequential [[Giglietto2025-1e9a0917]]. The throughline is a programme that began by characterising a polarized pluralist ecosystem and has progressively turned to the methodological and infrastructural conditions — embedding models, DSA-enabled data access, breakpoint validation — that make such characterisation possible in a platform-mediated environment.
