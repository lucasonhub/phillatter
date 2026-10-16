---
title: 'OrionMoE-v1.0: A Mixture-of-Experts Foundation Model for Tabular In-Context
  Learning'
authors:
- Mohamed Bouadi
- Nassim Bouarour
- Aditya Tanna
- Vinay Kumar Sankarapu
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Tabular foundation models enable in-context learning by predicting unseen
  observations from a labeled support table without task-specific parameter updates.
  Despite recent advances, most existing approaches rely on dense architectures that
  apply the same transformations across features and datasets. We introduce OrionMoE-Small,
  a compact tabular foundation model that combines distribution-aware representations
  with dataset-conditioned sparse mixture-of-experts computation. Built on a dual-axis
  Transformer architecture, OrionMoE-Small selectively activates experts along the
  feature axis, with routing decisions informed by both individual feature representations
  and the broader dataset context. This design enables adaptive allocation of computation
  across heterogeneous tabular problems while retaining a shared computational pathway
  across tasks. OrionMoE-Small is pretrained entirely on synthetic classification
  tasks generated from a structured causal prior and performs downstream prediction
  without gradient-based adaptation. Experiments across multiple tabular benchmarks
  demonstrate competitive performance against substantially larger foundation models,
  with particularly strong results on small-context and high-dimensional datasets.
  Further analysis reveals favorable relative performance under class imbalance and
  highlights the importance of feature composition.
source:
- arXiv
source_ids:
- arxiv:2610.20418
url: https://arxiv.org/abs/2610.20418
discovered_at: '2026-10-16'
tags: *id001
---

# OrionMoE\-v1\.0: A Mixture\-of\-Experts Foundation Model for Tabular In\-Context Learning

**Autores:** Mohamed Bouadi; Nassim Bouarour; Aditya Tanna; Vinay Kumar Sankarapu

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Tabular foundation models enable in\-context learning by predicting unseen observations from a labeled support table without task\-specific parameter updates\. Despite recent advances, most existing approaches rely on dense architectures that apply the same transformations across features and datasets\. We introduce OrionMoE\-Small, a compact tabular foundation model that combines distribution\-aware representations with dataset\-conditioned sparse mixture\-of\-experts computation\. Built on a dual\-axis Transformer architecture, OrionMoE\-Small selectively activates experts along the feature axis, with routing decisions informed by both individual feature representations and the broader dataset context\. This design enables adaptive allocation of computation across heterogeneous tabular problems while retaining a shared computational pathway across tasks\. OrionMoE\-Small is pretrained entirely on synthetic classification tasks generated from a structured causal prior and performs downstream prediction without gradient\-based adaptation\. Experiments across multiple tabular benchmarks demonstrate competitive performance against substantially larger foundation models, with particularly strong results on small\-context and high\-dimensional datasets\. Further analysis reveals favorable relative performance under class imbalance and highlights the importance of feature composition\.

[Consultar publicação](<https://arxiv.org/abs/2610.20418>)
