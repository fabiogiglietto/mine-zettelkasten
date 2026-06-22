---
type: structure
slug: mine-italian-media
topic: "MINE — Mapping Italian News"
---

# MINE — Mapping Italian News

## Mapping Italian News: An Arc of Inquiry

The MINE program traces a sustained empirical and methodological investigation of how Italian political information circulates, coordinates, and clusters across social platforms. Read together, the three papers filed here describe a research arc moving from *observation* of partisan attention patterns, to *intervention* against coordinated manipulation, to *methodological refinement* of the analytical tooling that makes such work possible at scale.

### From insularity to coordination

The starting point is [[Giglietto2019-882f1900]], which establishes the conceptual baseline: Italian news sources favored by populist supporters (Five Star Movement, League) are more *insular* on Twitter, and insularity systematically predicts a shares-heavy interaction pattern on Facebook, whereas cross-partisan sources attract comment-based contestation. The Five Star Movement emerges as a uniquely strategic actor in this attention economy, able to amplify favorable coverage and contest unfavorable coverage at scale. This finding — that partisan ecosystems differ not only in *what* they share but in *how* engagement is shaped around them — sets the agenda for everything that follows.

[[Giglietto2022-0e951ac5]] extends this observational work into the territory of *coordinated* manipulation. The MINE-FACTS project repurposes the CooRnet detection of Coordinated Link Sharing Behavior to map a covid-skeptic network that, tellingly, grew as an offshoot of the very M5S- and League-aligned coordinated clusters identified in the earlier election work. Where the 2019 paper described aggregate patterns of partisan amplification, this report names the actors, traces tactical adaptation (link-laundering, first-comment placement, religious-group bridging), and demonstrates that the comments-to-shares signature first noted as a partisan marker also discriminates problematic from non-problematic content. The continuity is striking: behavioral signatures that index partisan insularity in 2018 become operational signals for fact-checking triage in 2020–2021.

### Methodological turn

[[Giglietto2024-cbeb3f70]] marks a third movement — turning the analytical lens inward onto the tools used to make sense of the very corpora the program assembles. Comparing OpenAI's text-embedding-3-large with the Italian-tuned UmBERTo on political news shared before the 2018 and 2022 elections, the study finds that general-purpose LLM embeddings outperform language-specific BERT models on Italian political clustering, that K-means tends to beat HDBSCAN, and that HDBSCAN's apparent quality gains often reflect aggressive noise rejection rather than genuine coherence. This is infrastructural work for MINE: the same Facebook-shared political news corpora that anchored the earlier studies now serve as the testbed for choosing the embedding pipeline that will support future unsupervised mapping.

### Convergences and tensions

Across the three works, several throughlines emerge. The *comments-to-shares ratio* recurs as a portable diagnostic — partisan in 2019, forensic in 2022. The Italian populist coalition (M5S and League) is identifiable across all three studies as both the most insular partisan ecosystem and the substrate from which covid-skeptic coordinated networks grew. And the Facebook-link corpus around Italian elections functions as a recurring observatory, repeatedly re-interrogated with new questions and new tools.

The tension worth flagging is one of scale and interpretation. [[Giglietto2019-882f1900]] depends on careful manual adjudication of source–party alignments; [[Giglietto2022-0e951ac5]] argues for content-agnostic behavioral detection as a complement to such human judgment; and [[Giglietto2024-cbeb3f70]] pushes further toward fully unsupervised clustering validated by LLM raters. The arc is one of progressive automation, and the methodological paper's cautionary findings — that clustering choices materially affect what one "sees" — are a useful brake on that trajectory, reminding the program that the patterns it discovers are partly artifacts of the instruments used to discover them.
