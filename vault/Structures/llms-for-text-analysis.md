---
type: structure
slug: llms-for-text-analysis
topic: "LLMs for Text Classification & Annotation"
---

# LLMs for Text Classification & Annotation

## From Tools to Pipelines: LLMs as Measurement Infrastructure

The papers gathered here mark a shift in computational communication research: large language models are no longer just one more classifier to benchmark but the connective tissue of multi-stage measurement pipelines. The arc runs from cautious task-level validation toward fully LLM-integrated workflows — and, increasingly, toward reflexive critique of what that integration costs.

## LLMs as Annotators: Validation and the Quiet Displacement of Baselines

A first cluster of work treats LLMs as substitutes or supplements for human coders, asking when this substitution is defensible. [[Tan2024-vl]] provides the field's first synthesis of LLM annotation and synthesis, organizing the methodological space into generation, assessment, and utilization. Empirical contributions then probe specific corners: [[Larsson2026-ro]] uses GPT-4 zero-shot sentiment classification on a decade of Norwegian Facebook posts with human validation, while [[Bailard2024-pj]] takes a more traditional route, fine-tuning DeBERTa on Proud Boys Telegram messages — a useful reminder that fine-tuned encoder models remain competitive when label schemes are stable. [[Meher2025-qb]] pushes this further by showing that QLoRA-fine-tuned Llama-3.1 dramatically outperforms zero-shot baselines on conflict event coding, and frames LLMs as the natural successor to ConfliBERT-style approaches.

The bias question receives a notably calming answer from [[Brown2025-jk]]: across four contentious annotation datasets, demographic biases in LLM labels are small, dataset-specific rather than model-specific, and dwarfed by item difficulty (label entropy). This complicates simpler narratives about LLMs systematically marginalizing minority perspectives, while still endorsing context-specific fairness audits.

## From Classification to Scaling, Inference, and Narrative Measurement

A second strand treats LLMs not as classifiers but as latent-trait measurement instruments. [[Le-Mens2025-qz]] shows that simply asking GPT-4, Llama, MiXtral, or Aya to locate texts on policy dimensions and averaging the responses recovers benchmark ideological scalings across languages. [[DiGiuseppe2025-es]] couples LLMs with paired comparisons to scale open-ended survey responses, while [[Lee2026-je]] demonstrates that GPT-4o can infer users' political alignment from ostensibly non-political Reddit posts, outperforming supervised baselines and exploiting culturally politicized cues like "Tesla" or "Taylor Swift." Together these papers reposition LLMs as inference engines over latent traits rather than mere text-labelers — a move with both methodological promise and, as Lee et al. emphasize, serious privacy implications.

Narrative-level measurement extends this logic further. [[Waight2025-al]] uses GPT-4o to distill documents into claims and subjects, arguing that "narrative similarity" is a distinct estimand from lexical, topical, or semantic similarity, and showing that text-reuse methods miss most cross-source narrative diffusion. [[Elfes2026-jb]] operationalizes Greimas' actantial model through DeepSeek-R1 to measure "narrative polarisation" in YouTube discourse on Israel–Palestine. Both papers share an estimand–estimator framing: the LLM is justified because it makes a previously intractable theoretical construct measurable.

## LLMs-in-the-Loop: Pipelines, Embeddings, and Their Confounds

A third cluster builds multi-stage pipelines in which LLMs appear at several points. [[Marino2024-2fbc690f]] articulates this most explicitly, describing an Italian election pipeline that uses LLMs for binary classification, embedding generation, and cluster labeling, and arguing that each stage needs its own validation protocol with expert (not crowd) coders. [[Giglietto2024-cbeb3f70]] supplies the embedding-comparison evidence underlying that pipeline, showing OpenAI's text-embedding-3-large outperforms Italian-specific UmBERTo for clustering political news. [[Iris2026-pg]] uses ChatGPT-4o for entity extraction in a five-country study of EU election coverage, finding structural overrepresentation of the Radical Right. [[DeVerna2025-dl]] shows that even the strongest LLMs require curated retrieval to fact-check reliably — internal knowledge and generic web search are insufficient, and a RAG layer over PolitiFact summaries raises macro F1 by 233%.

[[Fan2025-ut]] offers a sharp methodological intervention into this pipeline turn: pretrained embeddings encode source, language, and style as observed confounders, biasing downstream similarity-based analyses. Linear concept erasure (LEACE) cleanly removes these without harming out-of-distribution performance — a clean example of importing causal-inference logic into embedding-based measurement.

## The Reflexive Turn

Running counter to the enthusiasm is [[Balluff2026-if]], which argues that LLM adoption in communication research has been rapid but unreflective, with underacknowledged costs: reproducibility breakage from corporate model updates, multilingual and demographic bias, environmental footprint, and ethical hazards in synthetic data and agent simulations. Read alongside the validation-heavy papers above, Balluff et al. function as the topic's superego: the field's empirical successes ([[Meher2025-qb]], [[Giglietto2024-cbeb3f70]], [[Le-Mens2025-qz]]) do not absolve researchers from choosing the least resource-intensive method capable of the task, preferring open-weight models, and registering trade-offs explicitly.

## Open Threads

Three tensions structure further inquiry. First, the *open vs. closed* question: the strongest task-specific results often come from closed models ([[DeVerna2025-dl]], [[Giglietto2024-cbeb3f70]], [[Iris2026-pg]]), but reproducibility and autonomy arguments push toward fine-tuned open models ([[Meher2025-qb]], [[Bailard2024-pj]]). Second, the *validation gap* between task-level audits ([[Brown2025-jk]]) and pipeline-level audits ([[Marino2024-2fbc690f]]) remains under-theorized — particularly when LLMs appear at multiple stages and errors compound. Third, the move from classification toward *latent-trait and narrative measurement* ([[Le-Mens2025-qz]], [[Waight2025-al]], [[Elfes2026-jb]], [[Lee2026-je]]) raises a question the topic has not yet answered: what does construct validity mean when the measurement instrument is itself a general-purpose generative model trained on the same discourse it is meant to measure?
