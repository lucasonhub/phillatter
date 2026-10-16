---
title: 'Hierarchical Interpretable Multitask Audio Representation Learning: An Analysis
  of Event-Scene Relationships through the Information Bottleneck'
authors:
- Claudia Montero-Ramírez
- Alba Martínez-Serrano
- Carmen Peláez-Moreno
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Joint Acoustic Scene Classification (ASC) and Audio Tagging (AT) models
  traditionally rely on unconstrained multihead architectures. However, this design
  ignores the natural hierarchical dependency between sounds and acoustic scenes.
  In this work, we investigate a hierarchical (sequential) conditioning paradigm that
  predicts scene categories directly from intermediate event probabilities. Through
  a large-scale empirical benchmark with 66 full training runs across three state-of-the-art
  backbones (PaSST, PANNs, and BEATs) and different loss-weighting settings (beta
  in [0.0, 1.0]), we show that hierarchical conditioning achieves competitive classification
  performance while altering multitask optimization dynamics. Unlike multihead baselines,
  which sequentially solve the easier ASC task before optimizing AT, the hierarchical
  architecture enables synchronized dual-task learning for specific loss-weighting
  settings (beta in [0.6, 0.9]). Furthermore, we propose a multi-perspective interpretability
  framework that combines an analysis of the information bottleneck, manifold geometry,
  and Formal Concept Analysis (FCA) on a Term-Frequency Inverse-Document-Frequency
  (TF-IDF) event representation, providing complementary insights into event-scene
  relationships. Our findings reveal that hierarchical conditioning systematically
  yields lower conditional entropy, higher mutual information, and superior latent
  cluster separability (higher Silhouette scores), establishing a more structured
  and semantically faithful intermediate feature space.
source:
- arXiv
source_ids:
- arxiv:2610.21520
url: https://arxiv.org/abs/2610.21520
discovered_at: '2026-10-16'
tags: *id001
---

# Hierarchical Interpretable Multitask Audio Representation Learning: An Analysis of Event\-Scene Relationships through the Information Bottleneck

**Autores:** Claudia Montero\-Ramírez; Alba Martínez\-Serrano; Carmen Peláez\-Moreno

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Joint Acoustic Scene Classification \(ASC\) and Audio Tagging \(AT\) models traditionally rely on unconstrained multihead architectures\. However, this design ignores the natural hierarchical dependency between sounds and acoustic scenes\. In this work, we investigate a hierarchical \(sequential\) conditioning paradigm that predicts scene categories directly from intermediate event probabilities\. Through a large\-scale empirical benchmark with 66 full training runs across three state\-of\-the\-art backbones \(PaSST, PANNs, and BEATs\) and different loss\-weighting settings \(beta in \[0\.0, 1\.0\]\), we show that hierarchical conditioning achieves competitive classification performance while altering multitask optimization dynamics\. Unlike multihead baselines, which sequentially solve the easier ASC task before optimizing AT, the hierarchical architecture enables synchronized dual\-task learning for specific loss\-weighting settings \(beta in \[0\.6, 0\.9\]\)\. Furthermore, we propose a multi\-perspective interpretability framework that combines an analysis of the information bottleneck, manifold geometry, and Formal Concept Analysis \(FCA\) on a Term\-Frequency Inverse\-Document\-Frequency \(TF\-IDF\) event representation, providing complementary insights into event\-scene relationships\. Our findings reveal that hierarchical conditioning systematically yields lower conditional entropy, higher mutual information, and superior latent cluster separability \(higher Silhouette scores\), establishing a more structured and semantically faithful intermediate feature space\.

[Consultar publicação](<https://arxiv.org/abs/2610.21520>)
