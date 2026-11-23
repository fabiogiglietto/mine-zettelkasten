---
title: "Dark patterns and the EU digital services act: Mapping autonomy violations and design factors"
aliases: ["Dark patterns and the EU digital services act: Mapping autonomy violations and design factors"]
authors: ["Sanju Ahuja", "Johanna Gunawan", "Nataliia Bielova", "Cristiana Santos"]
year: 2025
doi: 10.2139/ssrn.5555765
bibtex_key: Ahuja2025-ku
topics: [platform-governance-data-access]
citation_count: 1
open_access: false
source_url: https://doi.org/10.2139/ssrn.5555765
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ahuja2025-ku.mp3
pdf_available: true
discovery_date: 2026-03-22T08:20:48.605728Z
---

# Dark patterns and the EU digital services act: Mapping autonomy violations and design factors

> Ahuja, S., Gunawan, J., Bielova, N., & Santos, C. (2025). Dark patterns and the EU digital services act: Mapping autonomy violations and design factors. *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26), April 13â•ﬁ17, 2026, Barcelona, Spain*. https://doi.org/10.2139/ssrn.5555765
>
> [View paper](https://doi.org/10.2139/ssrn.5555765)

## Summary

This paper builds a "law-to-design" framework that connects HCI research on dark patterns with Article 25 of the EU Digital Services Act, which prohibits interface designs that deceive, manipulate, or distort/impair user autonomy. Rather than moving from design taxonomies toward legal categories (the usual "design-to-law" direction), the authors reverse the flow: they start from the DSA's three legally grounded autonomy violation types and ask which design characteristics make a given pattern violate the law. Through qualitative coding, they map all 59 meso- and low-level patterns in Gray et al.'s unified ontology onto these violation types and distill eight underlying design factors split between an "information space" and a "choice space." The framework is designed to be extensible and enforcement-relevant, demonstrated on attention-capture patterns and on the live EU Commission case against X over its paid blue checkmarks.

## Key Contributions

- The first comprehensive systematic mapping of 59 dark patterns to the three DSA Article 25 autonomy violation types (deception, manipulation, distortion/impairment).
- An eight-factor design vocabulary — Information Availability, Correctness, Framing, Presentation (Information Space) and Choice Availability, Effort, Simplification, Presentation (Choice Space) — giving concrete diagnostic criteria.
- Structured natural-language reasoning templates explaining *why* each pattern constitutes a given violation, released as appendix text and a supplementary CSV.
- Demonstration of extensibility to emerging pattern categories and to a real enforcement case.
- A translational argument that HCI methods can underpin regulatory design auditing and compliance-by-design.

## Methods

The authors adopted Santos et al.'s legally grounded reading of Article 25 as their codebook, defining deception (interfering with perceptions of truth), manipulation (steering behavior), and distortion/impairment (constraining behavior). Two authors independently labeled each of the 59 patterns from Gray et al.'s ontology in AirTable, resolving disagreements over three rounds of consensus. Design factors were inductively derived from coder rationale memos, then deductively re-applied to 34 low-level patterns (Cohen's Kappa = 0.679, substantial agreement). Two further authors refined labels and reasoning. External validity was tested against 11 attention-capture damaging patterns from Monge Roffarello et al. and the EU Commission's case against X.

## Findings

- 17 of 59 patterns map to a single violation type; 42 implicate multiple types, and 11 trigger all three.
- The deception–manipulation pairing is the largest combination (22 patterns), suggesting a continuum between the two, whereas manipulation–distortion combinations are rare (only 2).
- High-level strategies are internally consistent: all Sneaking patterns involve deception, all Obstruction involve distortion/impairment, all Social Engineering involve manipulation; Forced Action is the most diverse.
- Violations co-occur in three modes: separately, through temporal progression (e.g., drip pricing shifting from deception to manipulation), or by reinforcing each other (e.g., Sneak into Basket).
- Each design factor drives a specific violation: Information Availability/Correctness → deception; Framing, Presentation, Choice Simplification/Presentation → manipulation; Choice Availability/Effort → distortion/impairment.
- Meso-level patterns sometimes carry fewer labels than their low-level constituents because low-level definitions specify additional execution detail.
- Applied to X's paid blue checkmarks, the framework supports reasoning that the redesigned verification icon constitutes deception under Article 25.

## Connections

This paper sits within the platform-governance strand concerned with operationalizing EU digital regulation, sharing that regulatory-institutional lens with work on platform governance and enforcement such as [[Katzenbach2026-sl2e]] and [[Gillespie2010-sla2]]. Its focus on translating legal concepts into concrete, auditable design and data criteria connects to broader discussions of accountability and access under platform regimes, though its dark-patterns and HCI-methods orientation makes it largely distinct from the disinformation- and data-access-focused papers under the same topic.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ahuja2025-ku.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-dark-patterns-how-tech-tricks-violate/id1866587707?i=1000756981497)
