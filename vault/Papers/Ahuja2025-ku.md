---
title: "Dark patterns and the EU digital services act: Mapping autonomy violations and design factors"
aliases: ["Dark patterns and the EU digital services act: Mapping autonomy violations and design factors"]
authors: ["Sanju Ahuja", "Johanna Gunawan", "Nataliia Bielova", "Cristiana Santos"]
year: 2026
doi: 10.1145/3772318.3791479
bibtex_key: Ahuja2025-ku
topics: [platform-governance-and-content-moderation]
citation_count: 1
open_access: true
source_url: https://doi.org/10.1145/3772318.3791479
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ahuja2025-ku.mp3
pdf_available: true
discovery_date: 2026-03-22T08:20:48.605728Z
---

# Dark patterns and the EU digital services act: Mapping autonomy violations and design factors

> Ahuja, S., Gunawan, J., Bielova, N., & Santos, C. (2026). Dark patterns and the EU digital services act: Mapping autonomy violations and design factors. *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26), April 13â•ﬁ17, 2026, Barcelona, Spain*. https://doi.org/10.1145/3772318.3791479
>
> [View paper](https://doi.org/10.1145/3772318.3791479)

## Summary

This paper builds a "law-to-design" framework that connects HCI scholarship on dark patterns with Article 25 of the EU Digital Services Act, which prohibits design practices that deceive, manipulate, or distort/impair user autonomy. Working from Gray et al.'s unified dark pattern ontology and Santos et al.'s legal interpretation of Article 25, the authors qualitatively map 59 meso- and low-level dark patterns onto three autonomy violation types and derive eight underlying design factors, split between an "information space" and a "choice space." Rather than reasoning from design toward law (as most prior work does), they reverse the direction—translating legal categories into concrete, auditable design criteria—arguing that HCI methods can underpin a new field of regulatory design auditing and compliance-by-design.

## Key Contributions

- First comprehensive "law-to-design" mapping of 59 dark patterns from the Gray et al. ontology onto the three DSA Article 25 autonomy violation types (deception, manipulation, distortion/impairment).
- An eight-factor design vocabulary organized into an Information Space (Availability, Correctness, Framing, Presentation) and a Choice Space (Availability, Effort, Simplification, Presentation) for diagnosing violations.
- Structured, per-pattern reasoning templates explaining *why* each design constitutes a given violation, released as appendix text and a supplementary CSV.
- Demonstration of extensibility to attention-capture damaging patterns and to a live enforcement case (the EU Commission's proceedings against X over paid blue checkmarks).
- A translational bridge between HCI and legal scholarship, articulating how design analysis can support both enforcement and compliance-by-design.

## Methods

The authors adopted Gray et al.'s (2024) hierarchical ontology as their corpus, focusing on 59 meso- and low-level patterns and excluding 5 high-level strategies. They used Santos et al.'s legally grounded definitions of deception (interfering with perceptions of truth), manipulation (steering behavior), and distortion/impairment (constraining behavior) as a coding scheme. Two authors independently labeled each pattern in AirTable and resolved discrepancies over three consensus rounds. Design factors were inductively derived from coders' rationale memos, then deductively re-applied by re-coding 34 low-level patterns against an eight-factor codebook (Cohen's Kappa = 0.679). External validity was tested by applying the framework to 11 attention-capture damaging patterns and to the X blue-checkmark case.

## Findings

- 17 of 59 patterns map to a single violation type; 42 implicate multiple, and 11 trigger all three.
- Deception–manipulation is the largest combination subset (22 patterns), suggesting a continuum; manipulation–distortion combinations are rare (only 2).
- High-level strategies show internal consistency: all Sneaking patterns involve deception, all Obstruction involves distortion/impairment, all Social Engineering involves manipulation; Forced Action is the most diverse.
- Violations co-occur in three modes: separately, through temporal progression (e.g., drip pricing shifting from deception to manipulation), or by mutual reinforcement (e.g., Sneak into Basket).
- The eight design factors cluster by violation: Information Availability and Correctness drive deception; Framing, Information Presentation, Choice Simplification, and Choice Presentation drive manipulation; Choice Availability and Effort drive distortion/impairment.
- Meso-level patterns sometimes carry fewer labels than their constituent low-level patterns, which specify additional execution detail.
- Applied to X's paid blue checkmarks, the framework supports the argument that the redesigned verification icon constitutes deception under Article 25.

## Connections

This paper sits within work on platform governance and regulatory enforcement under the DSA, sharing its concern with operationalizing legal categories for auditing and oversight; it is broadly adjacent to research on platform governance concepts such as [[Gillespie2010-sla2]] and [[Katzenbach2026-sl2e]]. Its focus on interface design and user autonomy is largely orthogonal to the disinformation- and data-access-oriented studies dominating this topic cluster, so few genuine intellectual connections exist among the listed papers.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ahuja2025-ku.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-dark-patterns-how-tech-tricks-violate/id1866587707?i=1000756981497)
