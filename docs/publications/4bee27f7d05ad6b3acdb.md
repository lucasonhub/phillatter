---
title: 'QAMQOR: a benchmark dataset for engagement recognition in robot-assisted autism
  therapy'
authors:
- Nazerke Rakhymbayeva
- Aida Tungatarova
- Zhansaule Telisheva
- Anara Sandygulova
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3389/frobt.2026.1868211
abstract: 'Reliable engagement recognition is important for adaptive robot-assisted
  autism therapy (RAAT). However, progress remains constrained by the scarcity of
  publicly available benchmarks evaluated under realistic deployment conditions. Existing
  studies commonly adopt random train–test splits, which can inflate reported performance
  because recordings from the same child or therapy session may appear in both the
  training and test sets. To address this gap, we introduce QAMQOR, a benchmark dataset
  for engagement recognition collected during RAAT sessions with 34 children with
  Autism Spectrum Disorder (ASD), aged 3 − 12 years. The dataset includes visual engagement
  annotations derived from therapy session videos and feature representations extracted
  using two pose-estimation frameworks. The QAMQOR dataset defines four clinically
  relevant evaluation protocols based on Random, Child-Independent, Session-Independent,
  and Activity-Independent splits. These evaluation protocols assess model generalization
  to unseen children, therapy sessions and activity tasks. We benchmark classical
  machine learning classifiers together with temporal and sequence-learning baselines
  for both binary and multi-class engagement recognition. Experimental results show
  that the evaluation protocol influenced reported performance to a degree comparable
  to, and for fine-grained engagement classification exceeding, the influence of classifier
  selection: mean macro-F1 varied by 0.12 across the four protocols in the multi-class
  task, against 0.07 across discriminative classifiers. The Child-Independent split
  proved substantially more challenging than the Random split. Under the same conditions
  (windows, protocols, training schedule and untuned hyperparameters) a Temporal Convolutional
  Network (TCN) did not outperform the classical baselines. Applying identical imbalance
  handling to every model improved all imbalance-sensitive metrics but left this ordering
  unchanged, indicating that the result is not an artifact of missing class weights.
  Across the models evaluated, reported performance was shifted more by evaluation
  design and by imbalance handling than by architectural choice. Therefore, QAMQOR
  serves as a reproducible reference point for this task. It also shows why fair evaluation
  matters: keeping the same child or session out of both the training and test sets
  is needed to compare future methods on equal terms and to build engagement models
  that transfer to new children, sessions and activities in RAAT systems.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221662523
url: https://doi.org/10.3389/frobt.2026.1868211
discovered_at: '2026-10-16'
tags: *id001
---

# QAMQOR: a benchmark dataset for engagement recognition in robot\-assisted autism therapy

**Autores:** Nazerke Rakhymbayeva; Aida Tungatarova; Zhansaule Telisheva; Anara Sandygulova

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Reliable engagement recognition is important for adaptive robot\-assisted autism therapy \(RAAT\)\. However, progress remains constrained by the scarcity of publicly available benchmarks evaluated under realistic deployment conditions\. Existing studies commonly adopt random train–test splits, which can inflate reported performance because recordings from the same child or therapy session may appear in both the training and test sets\. To address this gap, we introduce QAMQOR, a benchmark dataset for engagement recognition collected during RAAT sessions with 34 children with Autism Spectrum Disorder \(ASD\), aged 3 − 12 years\. The dataset includes visual engagement annotations derived from therapy session videos and feature representations extracted using two pose\-estimation frameworks\. The QAMQOR dataset defines four clinically relevant evaluation protocols based on Random, Child\-Independent, Session\-Independent, and Activity\-Independent splits\. These evaluation protocols assess model generalization to unseen children, therapy sessions and activity tasks\. We benchmark classical machine learning classifiers together with temporal and sequence\-learning baselines for both binary and multi\-class engagement recognition\. Experimental results show that the evaluation protocol influenced reported performance to a degree comparable to, and for fine\-grained engagement classification exceeding, the influence of classifier selection: mean macro\-F1 varied by 0\.12 across the four protocols in the multi\-class task, against 0\.07 across discriminative classifiers\. The Child\-Independent split proved substantially more challenging than the Random split\. Under the same conditions \(windows, protocols, training schedule and untuned hyperparameters\) a Temporal Convolutional Network \(TCN\) did not outperform the classical baselines\. Applying identical imbalance handling to every model improved all imbalance\-sensitive metrics but left this ordering unchanged, indicating that the result is not an artifact of missing class weights\. Across the models evaluated, reported performance was shifted more by evaluation design and by imbalance handling than by architectural choice\. Therefore, QAMQOR serves as a reproducible reference point for this task\. It also shows why fair evaluation matters: keeping the same child or session out of both the training and test sets is needed to compare future methods on equal terms and to build engagement models that transfer to new children, sessions and activities in RAAT systems\.

[Consultar publicação](<https://doi.org/10.3389/frobt.2026.1868211>)
