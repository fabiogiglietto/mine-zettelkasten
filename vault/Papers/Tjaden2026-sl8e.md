---
title: "Does the TikTok Feed Lean Right? Exposure to Political Content Among Non-Partisan Users in Germany"
aliases: ["Does the TikTok Feed Lean Right? Exposure to Political Content Among Non-Partisan Users in Germany"]
authors: ["Jasper Tjaden", "Johannes Wolfgram", "Aaron Philipp", "Sarah Weissmann", "Licia Bobzien", "Ulrich Kohler", "Roland Verwiebe"]
year: 2026
doi: 10.1080/10584609.2026.2733320
bibtex_key: Tjaden2026-sl8e
kind: team
submitted_by: "Massimo Terenzi"
slack_permalink: https://minesmd.slack.com/archives/C0BDU82EBHQ/p1791633206348869
topics: [social-media-elections-international, platform-engagement-affordances]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1080/10584609.2026.2733320
podcast_url: 
pdf_available: true
discovery_date: 2026-10-10T17:41:50.271520Z
---

# Does the TikTok Feed Lean Right? Exposure to Political Content Among Non-Partisan Users in Germany

> Tjaden, J., Wolfgram, J., Philipp, A., Weissmann, S., Bobzien, L., Kohler, U., & Verwiebe, R. (2026). Does the TikTok Feed Lean Right? Exposure to Political Content Among Non-Partisan Users in Germany. *Political Communication*. https://doi.org/10.1080/10584609.2026.2733320
>
> [View paper](https://doi.org/10.1080/10584609.2026.2733320)

## Summary

This paper uses an automated sock-puppet audit to investigate whether TikTok's algorithm disproportionately exposes politically disinterested, non-partisan users in Germany to far-right content. Deploying 118 simulated non-partisan accounts across three 2024 regional elections and the 2025 federal election—observing 266,161 videos—the authors measure *incidental* exposure to party content while holding user behavior, networks, location, and timing constant. They find that political content makes up roughly 5–7% of these feeds and that, among unsolicited political videos, content mentioning and supporting the far-right AfD dominates all other parties. Crucially, the authors attribute this advantage not to overt algorithmic ideological favoritism but to a greater supply of pro-AfD accounts and more viral AfD videos—a "supply and demand" dynamic in which unofficial "multiplier" accounts play an outsized role.

## Key Contributions

- Rare empirical evidence on algorithmic political curation specifically on TikTok, which is understudied relative to Facebook, X, and YouTube.
- An audit design that isolates content/algorithmic effects by holding individual personalization constant, ruling it out as the driver of disparities.
- Extends prior findings of a right/conservative visibility advantage (shown in the US) to the German multi-party context during real election periods.
- A simplified three-input model of algorithmic curation—content/supply, collective behavior/demand, and individual behavior—for interpreting exposure disparities.
- A demonstration of how sock-puppet audits can provide independent platform accountability amid restricted researcher data access.

## Methods

The authors ran 118 automated non-partisan bot accounts (34 in 2024 regional elections, 84 in 2025 federal) that scrolled the "For You" feed ~1 hour/day for 4–6 weeks. Bots liked only non-political interest content (comedy, cooking, nature) and used a keyword blacklist to avoid engaging with political material, while logging all videos shown (exposure), engagement metrics, creator accounts, and descriptions. Available videos were downloaded and audio transcribed via Voxtral. Political content, party mentions, and party sentiment were classified using LLMs (Gemini), validated against human coders (binary political F1 = 0.93; Krippendorff's alpha = 0.84). Seven major German parties were placed on a left-right dimension, and official party/politician accounts identified via an external list. Exposure was modeled with linear mixed-effects models (random intercepts for users and nested videos), estimated per party with parametric bootstrap confidence intervals, supplemented by exploratory descriptive analysis of engagement and uploader accounts.

## Findings

- Political content comprised 6.6% of videos in the federal and 4.8% in the regional campaigns—roughly 35–49 political videos per week despite no political engagement.
- Videos mentioning the AfD were 1.8x (regional) and 3.4x (federal) more likely than any other party; videos *supporting* the AfD were 3.3x and 3.9x more likely.
- Pro-AfD exposure occurred faster: after ~400 videos (~1 hour), 53% (regional) and 89% (federal) of users had already encountered pro-AfD content.
- Both far-left and far-right parties had the highest supportive-to-mention ratios (Die Linke 69%, BSW 46%, AfD 40%) versus moderate parties (CDU/CSU 12%, SPD 27%).
- The AfD relied most heavily on unofficial "multiplier" accounts—only 20–35% of pro-AfD content came from official party/politician accounts.
- AfD videos were not unusual in mean/median likes but stood out in the number of viral posts (>100,000 likes) and the number of unique uploading accounts.
- A robustness check restricted to official party accounts still confirmed the AfD advantage.

## Connections

This paper sits within the growing audit literature on algorithmic amplification and partisan asymmetries; its finding of a right-leaning exposure advantage speaks to debates in platform-exposure work such as [[Gonzalez-Bailon2024-rq]], [[Guess2023-ur]], and [[Bakshy2015-rn]], while extending them to TikTok and a European multi-party setting. Its focus on the AfD and populist visibility on TikTok in Germany connects to related German and platform-affordance research including [[Bosch2024-hj]] and [[Philipp2026-tl]]. The methodological emphasis on sock-puppet auditing to probe recommender behavior also links it to independent-accountability approaches like [[Dahlke2026-sl34]].
