---
type: structure
slug: computational-methods-llms
topic: "Computational Methods and LLMs for Communication Research"
---

# Computational Methods and LLMs for Communication Research

## A Field Negotiating Its Tools

The papers gathered here document a discipline in mid-transition: communication and political science researchers are moving from text-as-data pipelines built on bag-of-words and BERT-class encoders toward generative LLMs as measurement instruments, annotators, and even research collaborators. The arc visible across these works is less a celebration of new capabilities than a sustained negotiation over *when*, *how*, and *whether* to delegate analytical labour to models — a negotiation increasingly conducted in the open, with validation protocols and benchmarks as its central artifacts.

## LLMs as Measurement Instruments

A first cluster treats LLMs as drop-in scaling and classification tools. [[Le-Mens2025-qz]] makes the simplest version of the case — ask the model to place a text on a dimension, average, validate against known benchmarks — while [[Lai2024-to]] reminds us that pre-LLM latent-scaling traditions remain productive when the relevant signal is structural (cross-subreddit sharing of YouTube videos). [[Larsson2026-ro]] and [[Giglietto2024-cbeb3f70]] extend GPT-based classification and embedding into non-English contexts, with the latter showing that `text-embedding-3-large` outperforms Italian-specific UmBERTo for clustering, while [[Marino2024-2fbc690f]] reflects on the validation challenges this kind of "LLMs-in-the-loop" pipeline poses. [[Meher2025-qb]] offers a more conservative alternative: parameter-efficient fine-tuning (QLoRA) of open-weight Llama for conflict-event coding, achieving strong performance on consumer hardware. [[Bailard2024-pj]] sticks with fine-tuned DeBERTa to classify collective-action frames at scale, demonstrating that supervised encoder approaches remain competitive when the construct is well-theorised.

Across these papers a consistent finding emerges: LLMs work well as measurement tools *when validated*, but the validation itself is where the methodological substance now lives.

## Visual, Multimodal, and Narrative Extensions

A second strand pushes computational analysis beyond text. [[Achmann-Denkler2026-lx]] shows GPT-4o outperforming specialised computer-vision pipelines for face recognition and person-counting on Instagram, while [[Arminio2025-tw]] uses VLLMs as a bridge — converting images to text descriptions for connotative (rather than denotative) clustering of climate imagery. Arora2025-jk (cf. [[Arora2025-tx]]) integrates textual and visual cues for multimodal frame analysis. Narrative-level analysis emerges as a distinct estimand in [[Waight2025-al]], which carefully distinguishes "narrative similarity" from lexical, topical, and semantic overlap, and in [[Elfes2026-jb]], which operationalises Greimas' actantial model via DeepSeek to measure narrative polarisation on YouTube. [[Sarmiento2025-as]] and [[Gerard2025-br]] take this further by treating shared narrative participation as the basis for *network construction* — CANE/t-CANE reconstructs user networks via cluster affiliation, enabling cross-platform analyses that interaction-based methods can no longer support given API closures. [[Bruns2025-fz]]'s "practice mapping" is a kindred move at a more programmatic level.

## What LLMs Can and Cannot Infer

A third cluster probes the *limits* of LLM inference. [[Lee2026-je]] demonstrates that LLMs can recover political alignment from ostensibly non-political discourse — a finding with significant privacy implications. [[Hackenburg2025-dj]] systematically maps the persuasive levers of conversational AI, identifying information density as the central mechanism and exposing a persuasion-accuracy trade-off. Counterpoint comes from [[Paci2025-ag]], which shows that even GPT-4o-mini struggles to interpret implicit Italian political discourse (implicatures, presuppositions) at expert level, and from [[DeVerna2025-dl]], which finds that LLMs fact-check poorly without curated retrieval context — reasoning models and web search help only modestly. [[Brown2025-jk]] complicates the "LLMs are biased annotators" narrative by showing that bias is dataset-specific rather than model-specific, and that item difficulty (label entropy) dwarfs demographic effects on agreement.

## The Critical Turn

Running alongside this empirical work is an increasingly forceful methodological-critical literature. [[Balluff2026-if]] offers the most pointed critique, cataloguing reproducibility risks, corporate dependency, environmental costs, and the demographic narrowing produced by synthetic data — and arguing for a "least-resource-intensive method capable of the task" heuristic. [[Tan2024-vl]] provides a complementary structural survey of LLM-based annotation and synthesis. Two methodological contributions stand out for proposing concrete remedies: [[Fan2025-ut]] shows that linear concept erasure (LEACE) can purge source/language confounds from sentence embeddings without degrading downstream performance, while [[Alizadeh2026-es]] benchmarks AI coding agents as reproducers of social-science findings — finding both impressive accuracy and worrying susceptibility to confirmatory prompt nudging and PDF-induced bias on non-reproducible tasks.

## Substantive Payoffs

These methods are not ends in themselves; several papers demonstrate what becomes newly answerable. [[Bailard2024-pj]] traces a four-week online-offline mobilisation cycle among the Proud Boys. [[Balluff2026-bv]] uses difference-in-differences on automated content analysis to detect media-capture signatures in the Austrian *Inseratenaffäre*. [[Iris2026-pg]] documents structural over-visibility of the Radical Right across five EU countries in the 2024 elections. [[Nenno2025-xa]] tests news-value theory against perceived misinformation across 24 WEIRD and non-WEIRD countries. [[Minici2024-tf]] builds graph foundation models for information-operation detection. [[Fan2026-af]] argues for a "temporal turn" exploiting timestamped digital traces, surveying six computational methods on donated cross-platform data. [[DiGiuseppe2025-es]] proposes LLM-paired comparisons for scaling open-ended survey responses — extending LLM measurement back into traditional survey methodology.

## The Emerging Consensus

Reading across the corpus, several shared commitments are crystallising. First, *validation is the new content*: nearly every paper devotes substantial space to comparing LLM outputs against human or benchmark coding, and validation is increasingly task-specific within multi-stage pipelines ([[Marino2024-2fbc690f]], [[Giglietto2024-cbeb3f70]]). Second, *estimand-estimator alignment* — most explicitly thematised by [[Waight2025-al]] — is replacing methodological enthusiasm as the central evaluative criterion. Third, there is broad recognition that LLMs amplify some research capacities (multilingual scaling, multimodal analysis, narrative-level measurement) while creating new failure modes (sycophancy, source skew, language bias, reproducibility decay) that demand structural rather than incremental responses. The field is, in short, learning to use these tools while simultaneously theorising what it means to use them well.
