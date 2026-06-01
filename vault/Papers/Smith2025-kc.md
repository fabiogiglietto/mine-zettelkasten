---
title: "Emergent structures of attention on social media are driven by amplification and triad transitivity"
aliases: ["Emergent structures of attention on social media are driven by amplification and triad transitivity"]
authors: ["Alyssa H Smith", "Jon Green", "Brooke F. Welles", "David Lazer"]
year: 2025
doi: 10.1093/pnasnexus/pgaf106
bibtex_key: Smith2025-kc
topics: []
citation_count: 0
open_access: false
source_url: https://doi.org/10.1093/pnasnexus/pgaf106
podcast_url: 
pdf_available: true
discovery_date: 2025-04-15T00:00:00Z
---

# Emergent structures of attention on social media are driven by amplification and triad transitivity

## Summary

This paper proposes a new brokerage concept — the *tertius amplificans*, or "attention broker" — to capture how social media users with large audiences close triads at scale by resharing others' content with attribution. Extending Obstfeld's *tertius iungens* to platforms with many-to-many amplification affordances, the authors argue that retweets by high-degree nodes are a local causal mechanism producing the well-known macro-level tendency toward triad transitivity in directed networks. Using a novel exploitation of the Twitter/X V1 API cursor to obtain time-stamped follower events, they run a difference-in-differences event study on two ideologically divergent cases (Jorts the Cat and J.K. Rowling) and show that amplification causally accelerates follower-to-amplified-account tie formation.

## Key Contributions

- **Theoretical**: Introduces *attention brokerage* / *tertius amplificans* as an amplification-based extension of *tertius iungens*, suited to sociotechnical systems with attributed resharing.
- **Methodological**: Documents a Twitter/X V1 API cursor technique (modified Unix nanosecond timestamps) that recovers time-bounded follower events, enabling precise temporal analysis of tie formation.
- **Empirical**: Provides causal (DiD) evidence that retweets by influential accounts generate transitive triads, across two structurally and ideologically divergent cases.
- **Conceptual bridge**: Links a local micro-mechanism to a macro-level network regularity (transitivity), addressing brokerage literatures that emphasize structural position without identifying causal mechanisms of closure.
- **Open resources**: Releases an anonymized dataset (SOMAR/ICPSR) and code documenting the cursor-based collection method.

## Methods

- Two-case comparative design: Jorts the Cat (~200K followers, pro-union, Dec 2021–Mar 2022) vs. J.K. Rowling (~14M followers, TERF advocacy, Jun 2018–Mar 2023).
- Broker timelines collected via the `focalevents` package, restricted to simple retweets (excluding quote tweets to avoid "dunking").
- Hand-coding of 646 (Jorts) and 534 (Rowling) retweeted accounts along cause-alignment and interest-actor dimensions, with adjudication by a third coder.
- Treatment motif: transitive triad (follower–broker–retweeted); control motif: open triad (nonfollower–broker–retweeted), measured in 2-week pre/post windows.
- Attentive population sizes estimated via the POPAN Jolly-Seber mark-recapture model in Project MARK.
- Two-stage DiD event study (Gardner) with account and time fixed effects, plus Rambachan–Roth sensitivity analysis for parallel-trends violations.

## Findings

- Day-0 treatment effects are positive and significant for both brokers: followers form ties to amplified accounts at substantially higher rates than nonfollowers.
- Heterogeneity by account type: Jorts's effect is strongest for union-related accounts; Rowling's effect is significant across types but largest for TERF interest actors.
- Small positive pre-retweet effects suggest incidental prior exposure also contributes; a post-spike decline indicates amplification accelerates ties that would have eventually formed, depleting latent followers.
- Rambachan–Roth sensitivity tests show robustness: parallel-trends violations would need to be more than 4× larger post-retweet than pre-retweet to overturn key results.
- Attentive populations differ markedly across groups (e.g., ~164K Jorts followers vs. ~17.9M nonfollowers; ~841K Rowling followers vs. ~2.68M nonfollowers in the sampled set).

## Connections

This paper sits in a growing computational social science literature on amplification dynamics and influencer effects on platforms; it complements work on virality cascades and superspreader-style accounts such as [[Bak-Coleman2026-mk]] and [[Luceri2025-tr]], and shares thematic ground with [[Green2025-ap]] on elite signaling on Twitter/X. Its methodological focus on platform affordances and API-derived behavioral traces also connects it to broader debates about data access and platform research infrastructure represented by [[Freelon2024-sc]] and [[Murtfeldt2025-wu]]. Substantively, by tying micro-level brokerage to macro network structure, it offers a causal complement to descriptive accounts of follower-network formation in works like [[Lai2024-to]].
