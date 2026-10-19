---
title: Detecting Health Misinformation Using Retrieval-Augmented Large Language Model
authors:
- Masuma Huseyn Mammadova
- Vagif Mammadaliyev
- Vusal Shahbazov
date: '2026-10-16'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3991/ijoe.v22i10.61955
abstract: Misinformation is common in online media, including in health-related content.
  Such misinformation constitutes a significant risk to the medical-demographic security
  of the population. Many people actively seek medical information online without
  the ability to verify its trustworthiness. This paper proposes a modular system
  for automated detection of misinformation in medical content based on retrieval-augmented
  verification. In the pipeline, input articles are summarized and decomposed into
  atomic claims. Each claim is then vectorized using dense embeddings (BGE-Large-en-v1.5)
  and matched against a self-constructed knowledge base via cosine similarity to retrieve
  evidence. Retrieved evidence is verified using large language model (LLM)- based
  natural language inference (NLI) and aggregated into article-level predictions through
  a scoring function. The LLM used in the system is the open-source LLaMA-3.1 model
  with eight billion parameters. Together with a self-contained knowledge base, this
  represents a deliberately constrained environment. Such a setup isolates the contribution
  of the presented architecture from its dependency on external knowledge sources
  and LLMs with large parameter counts. The system achieved 98.4% accuracy and a macro
  F1 of 0.978 at 79.0% coverage on the evaluated datasets (DETERRENT and CONSTRAINT).
  This demonstrates that, even under resource constraints, the correct pipeline architecture
  enables high-precision misinformation detection on medical content. It also represents
  a clear improvement over the ablation experiment, which used the same model without
  the proposed pipeline and achieved an F1 of only 0.773.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222696523
url: https://doi.org/10.3991/ijoe.v22i10.61955
discovered_at: '2026-10-19'
tags: *id001
---

# Detecting Health Misinformation Using Retrieval\-Augmented Large Language Model

**Autores:** Masuma Huseyn Mammadova; Vagif Mammadaliyev; Vusal Shahbazov

**Data:** 2026-10-16 · **Tipo:** article

## Resumo

Misinformation is common in online media, including in health\-related content\. Such misinformation constitutes a significant risk to the medical\-demographic security of the population\. Many people actively seek medical information online without the ability to verify its trustworthiness\. This paper proposes a modular system for automated detection of misinformation in medical content based on retrieval\-augmented verification\. In the pipeline, input articles are summarized and decomposed into atomic claims\. Each claim is then vectorized using dense embeddings \(BGE\-Large\-en\-v1\.5\) and matched against a self\-constructed knowledge base via cosine similarity to retrieve evidence\. Retrieved evidence is verified using large language model \(LLM\)\- based natural language inference \(NLI\) and aggregated into article\-level predictions through a scoring function\. The LLM used in the system is the open\-source LLaMA\-3\.1 model with eight billion parameters\. Together with a self\-contained knowledge base, this represents a deliberately constrained environment\. Such a setup isolates the contribution of the presented architecture from its dependency on external knowledge sources and LLMs with large parameter counts\. The system achieved 98\.4% accuracy and a macro F1 of 0\.978 at 79\.0% coverage on the evaluated datasets \(DETERRENT and CONSTRAINT\)\. This demonstrates that, even under resource constraints, the correct pipeline architecture enables high\-precision misinformation detection on medical content\. It also represents a clear improvement over the ablation experiment, which used the same model without the proposed pipeline and achieved an F1 of only 0\.773\.

[Consultar publicação](<https://doi.org/10.3991/ijoe.v22i10.61955>)
