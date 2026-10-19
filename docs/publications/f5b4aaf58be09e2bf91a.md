---
title: Comparative Analysis of Optuna-Optimized 1D and 2D CNNs for Protein Secondary
  Structure Prediction
authors:
- Annisa Rizqiana
- Triando Hamonangan Saragih
- Muhammad Itqan Mazdadi
- Irwan Budiman
- Adryan Maulana Saputra
date: '2026-10-16'
type: article
category: &id001
- Inteligência Artificial
doi: 10.35882/jeeemi.v8i4.1878
abstract: Protein secondary structure prediction (PSSP) is a fundamental task in bioinformatics,
  yet traditional experimental methods remain costly and time-consuming. While Convolutional
  Neural Networks (CNNs) offer efficient computational alternatives, systematic comparisons
  between 1D and 2D CNN topologies remain limited. Furthermore, conventional hyperparameter
  tuning in existing models relies on manual trial-and-error, introducing human bias
  and trapping networks in suboptimal performance thresholds. This study aims to evaluate
  the effectiveness of 1D and 2D CNN architectures for PSSP and systematically investigate
  the impact of automated hyperparameter optimization on both model performance and
  training efficiency. The proposed framework integrates standalone 1D and 2D CNN
  topologies with an automated hyperparameter optimization pipeline using Optuna based
  on the Tree-structured Parzen Estimator. Models are trained on the benchmark CullPDB
  dataset and rigorously evaluated via cross-dataset testing on the independent, non-redundant
  CB513 benchmark. The primary contributions include a standalone comparative analysis
  between 1D and 2D CNN topologies, the elimination of human bias via automated tuning,
  and a comprehensive feature efficiency analysis highlighting the trade-offs between
  computational representation and predictive accuracy. Experimental results show
  that all configurations achieve high overall performance with accuracies exceeding
  81% and AUC values above 94%. Specifically, the CNN 1D + Optuna configuration yields
  the highest precision of 0.4409 and an F1-score of 0.4454, effectively capturing
  local sequential motifs. Conversely, the CNN 2D + Optuna configuration excels in
  extracting spatial inter-residue relationships, delivering the highest AUC of 0.9493
  and the lowest cross-entropy loss of 0.0114. Additionally, Optuna dramatically accelerates
  training efficiency, reducing convergence iterations by up to 66% (from epoch 24
  down to 8 for the 2D model). In conclusion, automated optimization eliminates manual
  bias and enhances training efficiency, revealing that the choice between 1D and
  2D topologies should be strategically guided by the precise needs of downstream
  biological applications.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222623571
url: https://doi.org/10.35882/jeeemi.v8i4.1878
discovered_at: '2026-10-19'
tags: *id001
---

# Comparative Analysis of Optuna\-Optimized 1D and 2D CNNs for Protein Secondary Structure Prediction

**Autores:** Annisa Rizqiana; Triando Hamonangan Saragih; Muhammad Itqan Mazdadi; Irwan Budiman; Adryan Maulana Saputra

**Data:** 2026-10-16 · **Tipo:** article

## Resumo

Protein secondary structure prediction \(PSSP\) is a fundamental task in bioinformatics, yet traditional experimental methods remain costly and time\-consuming\. While Convolutional Neural Networks \(CNNs\) offer efficient computational alternatives, systematic comparisons between 1D and 2D CNN topologies remain limited\. Furthermore, conventional hyperparameter tuning in existing models relies on manual trial\-and\-error, introducing human bias and trapping networks in suboptimal performance thresholds\. This study aims to evaluate the effectiveness of 1D and 2D CNN architectures for PSSP and systematically investigate the impact of automated hyperparameter optimization on both model performance and training efficiency\. The proposed framework integrates standalone 1D and 2D CNN topologies with an automated hyperparameter optimization pipeline using Optuna based on the Tree\-structured Parzen Estimator\. Models are trained on the benchmark CullPDB dataset and rigorously evaluated via cross\-dataset testing on the independent, non\-redundant CB513 benchmark\. The primary contributions include a standalone comparative analysis between 1D and 2D CNN topologies, the elimination of human bias via automated tuning, and a comprehensive feature efficiency analysis highlighting the trade\-offs between computational representation and predictive accuracy\. Experimental results show that all configurations achieve high overall performance with accuracies exceeding 81% and AUC values above 94%\. Specifically, the CNN 1D \+ Optuna configuration yields the highest precision of 0\.4409 and an F1\-score of 0\.4454, effectively capturing local sequential motifs\. Conversely, the CNN 2D \+ Optuna configuration excels in extracting spatial inter\-residue relationships, delivering the highest AUC of 0\.9493 and the lowest cross\-entropy loss of 0\.0114\. Additionally, Optuna dramatically accelerates training efficiency, reducing convergence iterations by up to 66% \(from epoch 24 down to 8 for the 2D model\)\. In conclusion, automated optimization eliminates manual bias and enhances training efficiency, revealing that the choice between 1D and 2D topologies should be strategically guided by the precise needs of downstream biological applications\.

[Consultar publicação](<https://doi.org/10.35882/jeeemi.v8i4.1878>)
