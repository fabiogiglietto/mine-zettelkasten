---
type: structure
slug: italian-elections-mine
topic: "Italian Elections & News Ecosystem (MINE)"
---

# Italian Elections & News Ecosystem (MINE)

## Mapping a Decade of Italian Political Communication

The MINE program's empirical core traces a single, evolving question across nearly a decade: how does political information circulate, distort, and get governed within Italy's hybrid, platform-mediated media ecosystem? The corpus filed here moves from early hybrid-media accounts of televised elections, through a methodologically ambitious campaign to detect coordinated manipulation on Facebook, to recent work auditing the platforms themselves as accountable infrastructures.

### Origins: TV, Twitter, and the Hybrid Campaign

[[Iannelli2015-e0818c3e]] establishes the foundational hybrid-media framing that underlies the whole program: during the 2013 elections, Twitter functioned not as an autonomous democratizing channel but as a second screen tightly bound to broadcast logic, with narrow, TV-paced participation rather than agenda-shaping intervention. This early insistence that "social media effects" must be read through their entanglement with legacy media anticipates a recurring MINE theme — that Facebook and Twitter dynamics cannot be understood in isolation from journalism, television, and party strategy.

### Coordination as the Unit of Analysis

The program's signature methodological contribution is the shift from content- or actor-based disinformation detection to **behavior-based coordination detection**. [[Giglietto2020-9d8acdd7]] introduces coordinated link sharing behavior (CLSB) as an ecological alternative to fact-checking or bot-hunting, showing across the 2018 and 2019 Italian campaigns that coordinated networks disproportionately amplify problematic domains and cluster into either centralized or highly-clustered structures. [[Giglietto2019-882f1900]] complements this actor-network view with an audience-side account of partisan insularity, demonstrating that M5S-aligned sources are the most insular on Twitter and that insularity predicts a Facebook engagement signature (shares over comments) that the paper reads as amplification versus contestation — a metric ([[Marino2023-9137f448]] later reuses the comments/shares ratio for exactly this purpose in the Covid infodemic). [[Giglietto2023-fa71a001]] operationalizes and scales this behavioral logic into a continuously-updating workflow, applied to the 2022 snap election, that reveals not only ideologically motivated hyperpartisan networks (M5S) but also commercially and religiously motivated coordinated operations — pushing the program's disinformation lens beyond party politics into an "ecology of manipulation" that cuts across motives.

This coordination paradigm extends naturally to non-electoral crises: [[Marino2023-9137f448]] applies the same CLSB-derived dataset to Covid-skeptic networks, identifying an "Intellectual Dark Web" cluster whose problematic claims are laundered through remediation of legacy-media appearances — reinforcing Iannelli's hybrid-media thesis in a new register, where TV and newspaper content becomes raw material for platform-native amplification rather than the other way around.

### From Detection to Platform Governance

A second arc turns from detecting bad behavior to auditing the platforms that structure it. [[McNally2025-dn]] demonstrates, via a Guardian dataset independent of the Italian corpus, that Facebook's News Feed algorithm is empirically legible rather than an unknowable "black box," setting a methodological and normative precedent — systemic algorithmic auditing enabled by the EU Digital Services Act — that [[Giglietto2025-1765bb4f]] takes up directly for the Italian case. Using the Meta Content Library, that paper shows Meta's political content reduction policy silently suppressed Italian MPs' reach months before its announced rollout, recovered only partially after reversal, and inadvertently advantaged extremist accounts that compensated with higher posting volume — a striking asymmetry that complicates any simple "platforms are neutral" or "platforms are unbiased suppressors" narrative. [[Rossi2023-847d5a9f]] extends this transparency-infrastructure lens comparatively, using Meta's URL Shares Dataset to show Italy trending toward Germany's electoral-year spikes in untrustworthy URL shares, in contrast to France's stability, while confirming that older cohorts drive both exposure and sharing of unreliable content — a demographic finding that resonates with the age-skewed caution documented for AI attitudes in [[Fattorini2026-bo]].

### Methodological Innovation: Toward LLM-in-the-Loop Analysis

A third, more recent thread addresses how to *scale* this kind of analysis computationally. [[Giglietto2024-cbeb3f70]] benchmarks OpenAI's text-embedding-3-large against the Italian-specific UmBERTo model for clustering political news, finding the former consistently superior across the 2018 and 2022 datasets — a result [[Marino2024-2fbc690f]] builds directly into a full "LLMs-in-the-loop" pipeline (classification, embedding, cluster labeling) for the same election corpora, while grappling reflexively with the validation challenges this introduces, particularly the inadequacy of crowdsourced human benchmarks once LLMs begin to outperform them. These two papers mark a methodological pivot within MINE: from bespoke coordination-detection scripts toward generalizable, LLM-assisted infrastructure for narrative and cluster analysis of Italian political news at scale.

### Adjacent Currents in the News Ecosystem

Several papers extend the program's news-ecosystem lens beyond elections narrowly defined. [[Ducci2022-10cb5d70]] examines Google News Italia as a gatekeeper for health information, showing that Facebook engagement tracks topical emotionality (celebrity health, malfunction stories) rather than source identity — a finding structurally analogous to the insularity/engagement dynamics found in electoral contexts. [[Mosca2026-yh]] theorizes "fake news" accusations themselves as rhetorical weapons of delegitimization within Italian newspapers, reframing misinformation discourse as a campaigning tactic rather than a purely epistemic failure — a useful counterpoint to the program's otherwise behavior-and-platform-centric methodology, reintroducing strategic communication and negative campaigning as an analytic frame. [[Fattorini2026-bo]], meanwhile, surveys Italian public attitudes toward AI, documenting a "critical ambivalence" that, while not electoral in focus, maps the same terrain of platform-mediated technological anxiety and demographic stratification (age, education, gender) that recurs throughout the Facebook-centered studies.

### The Arc

Read together, these thirteen papers trace MINE's trajectory from hybrid-media description (2015) through behavior-based disinformation detection (2018–2023) to platform accountability and computational scaling (2023–2025), with recurring threads — comments/shares as a semiotic of amplification versus contestation, the entanglement of legacy and platform media, age as a persistent predictor of exposure to unreliable content, and a growing reliance on LLM-assisted methods — binding the program's expanding empirical scope to a stable set of theoretical commitments about how Italian political communication actually works.
