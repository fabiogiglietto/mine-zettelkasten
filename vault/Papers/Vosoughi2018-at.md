---
title: "The spread of true and false news online"
aliases: ["The spread of true and false news online"]
authors: ["Soroush Vosoughi", "Deb Roy", "Sinan Aral"]
year: 2018
doi: 10.1126/science.aap9559
bibtex_key: Vosoughi2018-at
topics: [information-disorder-theory, political-polarization-partisanship]
citation_count: 6671
open_access: false
source_url: https://doi.org/10.1126/science.aap9559
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T15:33:05.807327Z
---

# The spread of true and false news online

> Vosoughi, S., Roy, D., & Aral, S. (2018). The spread of true and false news online. *Science*, *359*, 1146–1151. https://doi.org/10.1126/science.aap9559
>
> [View paper](https://doi.org/10.1126/science.aap9559)

## Summary

This landmark study by Vosoughi, Roy, and Aral provides the first large-scale empirical characterization of how verified true and false news differ in their diffusion on Twitter. Drawing on roughly 126,000 rumor cascades shared by around 3 million people between 2006 and 2017 — each classified by six independent fact-checking organizations — the authors demonstrate that falsehood spread significantly farther, faster, deeper, and more broadly than truth across every category of information, with the disparity most acute for political news. Crucially, they attribute this pattern to human sharing behavior rather than to automated bots, proposing the greater *novelty* of false news and the emotional reactions it provokes as candidate explanations. The work reframes misinformation as a problem of human decision-making rather than purely technological manipulation.

## Key Contributions

- First comprehensive, veracity-based empirical analysis of true versus false news diffusion at scale, moving beyond fragmented single-rumor studies.
- Introduces a framework distinguishing news, rumors, and cascades, deliberately avoiding the politicized term "fake news."
- Empirically overturns the assumption that bots or network/user characteristics drive the spread of falsity, redirecting attention to human behavior.
- Offers novelty and emotional response as behavioral mechanisms underlying the differential spread.
- Points toward behavioral interventions (labeling, incentives) over a bots-only policy focus, and releases code and data.

## Methods

The authors assembled all fact-checked rumor cascades on Twitter over an 11-year span, classifying each as true, false, or mixed using verdicts parsed from six fact-checking sites (95–98% cross-organization agreement). They reconstructed retweet cascades from reply tweets and quantified diffusion via four metrics: depth, size, maximum breadth, and structural virality. Distributional comparisons used Kolmogorov–Smirnov tests, and a logistic regression modeled retweet likelihood while controlling for account age, activity, followers, followees, and verified status. Novelty was measured with an LDA topic model (200 topics) comparing rumor tweets to what users had seen in the prior 60 days, using information uniqueness, KL divergence, and Bhattacharyya distance. Emotional content of replies was scored with the NRC lexicon mapped to Plutchik's eight emotions. Robustness checks included cluster-robust standard errors, an independently annotated validation set (Fleiss' κ = 0.88), and two bot-detection algorithms.

## Findings

- The top 0.01% of false cascades exceeded 19 hops deep — about eight hops deeper than truth, which rarely surpassed depth 10.
- Truth rarely reached more than 1,000 people; the top 1% of false cascades reached 1,000–100,000 people.
- Truth took ~6× as long to reach 1,500 people and ~20× as long to reach cascade depth 10.
- False political news (the largest category, ~45,000 cascades) traveled deeper, broader, faster, and more virally than any other false-news category.
- Users spreading false news had fewer followers, followed fewer people, were less active, less often verified, and newer to Twitter.
- Falsehoods were 70% more likely to be retweeted even after controlling for user and network characteristics.
- False rumors were more novel across all three metrics and elicited more surprise and disgust; true rumors elicited more sadness, anticipation, joy, and trust.
- Removing and re-adding bot traffic left conclusions unchanged, indicating bots accelerated true and false news roughly equally.

## Connections

This paper is a foundational empirical anchor for information-disorder research, and its diffusion-focused approach connects closely to work on false-news exposure and sharing during elections such as [[Grinberg2019-ua]] and [[Guess2019-ym], as well as conceptual efforts to define the misinformation landscape like [[Lazer2018-mm]]. Its finding that human psychology rather than bots drives sharing dovetails with accuracy- and reasoning-based intervention research such as [[Pennycook2021-jq]] and with debates over the true reach and impact of misinformation in [[Allen2020-nj]] and [[Budak2024-ef]]. Its emphasis on political news as the most viral category resonates with the partisan-motivated-sharing literature, including [[Osmundsen2021-et]] and motivated-reasoning accounts like [[Kunda1990-cg]].
