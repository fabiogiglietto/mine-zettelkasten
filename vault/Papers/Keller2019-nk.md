---
title: "Political Astroturfing on Twitter: How to Coordinate a Disinformation Campaign"
aliases: ["Political Astroturfing on Twitter: How to Coordinate a Disinformation Campaign"]
authors: ["Franziska B. Keller", "David Schoch", "Sebastian Stier", "JungHwan Yang"]
year: 2020
doi: 10.1080/10584609.2019.1661888
bibtex_key: Keller2019-nk
topics: [coordinated-inauthentic-behavior, information-disorder-theory]
citation_count: 283
open_access: false
source_url: https://doi.org/10.1080/10584609.2019.1661888
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807293Z
---

# Political Astroturfing on Twitter: How to Coordinate a Disinformation Campaign

> Keller, F. B., Schoch, D., Stier, S., & Yang, J. (2020). Political Astroturfing on Twitter: How to Coordinate a Disinformation Campaign. *Political Communication*, 1–25. https://doi.org/10.1080/10584609.2019.1661888
>
> [View paper](https://doi.org/10.1080/10584609.2019.1661888)

## Summary

This paper examines *political astroturfing*—centrally coordinated disinformation campaigns in which paid agents pose as independent grassroots citizens—through the exceptional lens of a case with offline ground truth. During the 2012 South Korean presidential election, the National Intelligence Service (NIS) ran a covert Twitter operation supporting conservative candidate Geun-hye Park; subsequent court proceedings publicly identified 1,008 account names tied to NIS agents. Using this list, the authors argue that astroturfing is best understood as a form of disinformation not because its content is false (it often is not) but because it deceives audiences about the coordinated, non-independent origin of that content. They contend that the field's fixation on automated bot detection is conceptually mismatched with astroturfing, and that *coordination traces*—not individual bot-like signatures—are the strongest and hardest-to-hide signal of a campaign. Grounding this in principal-agent theory, they build a relational detection method and, notably, find that despite considerable resources the campaign had only modest measurable impact on Twitter discourse.

## Key Contributions

- Empirically characterizes one of the earliest confirmed coordinated online disinformation campaigns using offline ground-truth data linking specific accounts to their instigators.
- Introduces a theoretically grounded, relational detection method built on retweet, co-tweet, and co-retweet networks—transferable because principal-agent problems make coordination traces unavoidable.
- Reframes disinformation research away from bot detection toward group-level coordination, and broadens the concept of disinformation to include deception about coordinated origin rather than only factual falsity.
- Measures campaign influence with multiple metrics rather than anecdotes, demonstrating limited impact even under near-best-case conditions.
- Flags a policy problem: platform deletion of implicated accounts undermines ex post research on disinformation.

## Methods

The study is a case study of the NIS operation using 716 unique ground-truth accounts, 702 of which appear in the UW-Madison SMAD Twitter archive (a 10% Gardenhose stream of 75 million Korean-language tweets, June–December 2012, containing ~195,000 NIS tweets). The authors derive expectations from principal-agent theory about how coordinated campaigns should differ from organic movements, then operationalize these via three coordination networks (retweet, co-tweet within one minute, co-retweet within a short window) plus temporal activity and account-creation analyses. A relational detection strategy iteratively identifies suspect accounts through a 50% NIS-retweet threshold and the largest network components, validated against random-user, political-keyword, and opinion-leader baselines using account status, activity patterns, and content analysis (keyword rank correlations, most-retweeted accounts). Influence is assessed via followers, mentions received, and retweets received.

## Findings

- NIS accounts tweeted during office hours and weekdays, collapsed on weekends, and stopped abruptly after the December 11 exposure—patterns opposite to ordinary users.
- Coordination was pervasive: 48% of NIS tweets were retweets; ~45,000 identical non-retweet messages were co-tweeted (over half within the same second); only 17% of retweets were unique, with co-retweeting used by almost every agent.
- Network structure revealed a division of labor across agents, and much campaign traffic circulated within its own network.
- The detection method surfaced 834 additional suspect accounts sharing NIS temporal, account-creation, and content signatures.
- Validation was strong: under 10% of suspect accounts remained active versus 40% of a random sample; up to 96% of known and suspected accounts were deactivated or suspended.
- Content skewed heavily political and toward hardline North Korea framing, correlated tightly among NIS/suspect accounts (τ≈0.61–0.66) and negatively with regular users; agents retweeted right-wing pundits and ignored popular liberal accounts.
- Despite mutually inflated follower counts, NIS accounts received fewer mentions than ordinary users and a negligible share of overall retweets (~40% of which came from within the campaign), showing no evidence of shifting the broader agenda.

## Connections

This paper is a methodological anchor for the coordinated-inauthentic-behavior literature, particularly work that detects influence operations through coordination signals rather than bot signatures, connecting to the coordinated-link-sharing and network-based detection strands in [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], and [[Nizzoli2020-cf]], and to broader treatments of state-linked and platform-scale coordination in [[Luceri2025-tr]] and [[Starbird2019-qv]]. Its skeptical assessment of astroturfing's measurable impact resonates with reach- and effect-oriented critiques of disinformation prevalence such as [[Allen2020-nj]] and [[Guess2019-ym]], while its use of the information-disorder framing links it to [[Freelon2020-yp]] and studies of partisan sharing motivations like [[Osmundsen2021-et]].
