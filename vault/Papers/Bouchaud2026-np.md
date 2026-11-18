---
title: "Community Notes undermoderate polarizing content by design creating risks in electoral processes"
aliases: ["Community Notes undermoderate polarizing content by design creating risks in electoral processes"]
authors: ["Paul Bouchaud", "Pedro Ramaciotti"]
year: 2026
doi: 10.1126/sciadv.aee6932
bibtex_key: Bouchaud2026-np
topics: [platform-governance-and-data-access, political-polarization-and-partisanship]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1126/sciadv.aee6932
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bouchaud2026-np.mp3
pdf_available: true
discovery_date: 2026-07-02T04:41:34.956800Z
---

# Community Notes undermoderate polarizing content by design creating risks in electoral processes

> Bouchaud, P., & Ramaciotti, P. (2026). Community Notes undermoderate polarizing content by design creating risks in electoral processes. *Science Advances*, *12*. https://doi.org/10.1126/sciadv.aee6932
>
> [View paper](https://doi.org/10.1126/sciadv.aee6932)

## Summary

This paper evaluates how X's Community Notes operates across diverse polarization contexts. The bridging algorithm infers a latent ideological dimension for notes and raters and surfaces only notes with cross-ideological support. Using X's public data release as of 1 March 2025 — 1.88 million notes and 135.17 million ratings, rounded in the abstract to 1.9 million and 135 million, of which 1.45 million notes rated 133.20 million times remain after X's own preprocessing — and ideology scaling of follower networks in 13 countries, the authors show that the algorithm captures each country's main polarizing divide. That success has a cost: by design, content that strongly activates polarization is systematically undermoderated, regardless of its factuality. Notes on the 2024 US, UK and French elections and the 2025 German election reach Helpful Status less often than other notes from the same period, which the authors present as a risk for electoral processes as Meta, YouTube and TikTok adopt similar systems.

## Key Contributions

- First cross-national test (13 countries) of the key hypothesis behind Community Notes' design: that its latent dimension captures the structuring political divide outside the United States.
- Shows that undermoderation of polarizing content is a property of the bridging design rather than an operational glitch; the share left unresolved is a platform design choice (diversity threshold, regularization).
- Provides election-specific evidence from four national elections.
- Informs policy as other platforms deploy similar systems, Meta explicitly building on X's open-source algorithm.

## Methods

- **Data:** X's public Community Notes release as of 1 March 2025 (1.88M notes, 135.17M ratings from 1.15M contributors). After X's preprocessing (notes with ≥5 ratings, raters with ≥10), the analyzed set is 1.45M notes on 886,370 posts, rated 133.20M times by 821,250 contributors. Post content was collected for 616,104 posts linked to 83.5% of non-deleted notes.
- Replication of X's regularized matrix factorization; the inferred note biases predict Helpful Status with AUC 0.92 and Not Helpful Status with AUC 0.97.
- Multidimensional ideology scaling of accounts following MPs (correspondence analysis, mapped to Global Party Survey Left–Right and Anti-Elite dimensions), analyzed for 13 countries.
- Topic classification and keyword curation of election-related notes for four elections, compared with all notes from one month before to one week after each election.

## Findings

- Of proposed notes arguing a post is misinformed or potentially misleading (73.0% of all notes), 11.97% reach Helpful Status, 2.81% Not Helpful Status, and 85.22% no conclusive status because they "lacked sufficient ratings from diverse contributors".
- Election-related notes reach Helpful Status less often than all notes in the same period: US 2024 6.9% vs 14.7%; UK 2024 8.2% vs 10.9%; France 2024 12.8% vs 16.8%; Germany 2025 8.6% vs 11.9%.
- Note writing is concentrated: 1% of the 405 thousand contributors with note-writing privileges authored 31.2% of all proposed notes.
- The Community Notes latent dimension aligns with each country's main political dimension: AUCs from 0.729 (Israel) to 0.850 (Poland), averaging 0.808 across 13 countries.
- Divisive accounts rarely get Helpful notes: 3% of Elon Musk's annotated posts and under 0.1% of the Kamala Harris campaign's.
- In the US, 12.9% of annotated posts by Right-leaning users receive Helpful notes against 8.3% for Left-leaning users, consistent with Renault et al.; the authors caution that differential post deletion may partly explain this.
- Expert fact-checking articles appear in only 3.5% of proposed notes.

## Connections

This audit cites [[Renault2025-uh]] and reports a similar US gap (12.9% vs 8.3% of annotated posts by Right- vs Left-leaning users receiving Helpful notes), but cautions that it may partly reflect differential post deletion; its main contribution is explaining why bridging leaves most polarizing content unresolved. It pairs with the platform's own account of AI note writers in [[Miller2026-cp]], which likewise finds over half of unresolved (NMR) notes short of the 10 ratings needed for Helpful status and calls rater attention "a critical resource". [[Holt2026-zq]] shows that user flagging on Facebook often expresses political objection, and [[Cazzamatta2026-lo]] examines the dismantling of Meta's fact-checking program — the substitution of crowd-sourced for expert fact-checking that this paper warns about. The same authors' [[Bouchaud2026-lr]] also infers X users' ideological positions, there from the platform's recommender.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bouchaud2026-np.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
