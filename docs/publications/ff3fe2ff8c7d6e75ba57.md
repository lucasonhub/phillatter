---
title: 'TEX-MEX: Similarity-Guided Temporal Contrastive Learning for Time Series'
authors:
- Aditya Radhakrishnan
- Maxwell A. Xu
- Wanting Mao
- Santosh Kumar
- Harish Haresamudram
- James M. Rehg
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Contrastive learning for time series depends on deciding which pairs of
  inputs should be treated as similar and dissimilar. Because few augmentations reliably
  preserve meaning in time series, prior methods have relied on two disjoint notions
  of similarity between windows: structural similarity, which relates windows with
  similar morphology, and temporal similarity, which relates windows that occur close
  together in time. We introduce TEX-MEX, to our knowledge the first approach to unify
  the two into a single relationship. Given a random batch of windows drawn across
  the dataset, TEX-MEX uses the encoder to identify which windows are structurally
  similar or dissimilar to each other. It then pulls each window toward the temporally
  shifted versions of similar windows and pushes it away from those of dissimilar
  ones, learning what typically accompanies similar windows in time. Across PPG, EEG,
  ECG, accelerometry, and continuous glucose monitoring, TEX-MEX broadly achieves
  state-of-the-art performance against contrastive, reconstructive, JEPA-based, and
  modality-specific approaches, establishing it as a strong general SSL objective.
  We further train a 560K-parameter PPG foundation model that achieves state-of-the-art
  performance across a broad range of downstream benchmarks while being roughly 50x
  smaller than the next-best unimodally pretrained PPG foundation model in our evaluation.
  We will release this foundation model open-source and open-weight to the community
  to support future work and practical applications.'
source:
- arXiv
source_ids:
- arxiv:2610.19557
url: https://arxiv.org/abs/2610.19557
discovered_at: '2026-10-16'
tags: *id001
---

# TEX\-MEX: Similarity\-Guided Temporal Contrastive Learning for Time Series

**Autores:** Aditya Radhakrishnan; Maxwell A\. Xu; Wanting Mao; Santosh Kumar; Harish Haresamudram; James M\. Rehg

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Contrastive learning for time series depends on deciding which pairs of inputs should be treated as similar and dissimilar\. Because few augmentations reliably preserve meaning in time series, prior methods have relied on two disjoint notions of similarity between windows: structural similarity, which relates windows with similar morphology, and temporal similarity, which relates windows that occur close together in time\. We introduce TEX\-MEX, to our knowledge the first approach to unify the two into a single relationship\. Given a random batch of windows drawn across the dataset, TEX\-MEX uses the encoder to identify which windows are structurally similar or dissimilar to each other\. It then pulls each window toward the temporally shifted versions of similar windows and pushes it away from those of dissimilar ones, learning what typically accompanies similar windows in time\. Across PPG, EEG, ECG, accelerometry, and continuous glucose monitoring, TEX\-MEX broadly achieves state\-of\-the\-art performance against contrastive, reconstructive, JEPA\-based, and modality\-specific approaches, establishing it as a strong general SSL objective\. We further train a 560K\-parameter PPG foundation model that achieves state\-of\-the\-art performance across a broad range of downstream benchmarks while being roughly 50x smaller than the next\-best unimodally pretrained PPG foundation model in our evaluation\. We will release this foundation model open\-source and open\-weight to the community to support future work and practical applications\.

[Consultar publicação](<https://arxiv.org/abs/2610.19557>)
