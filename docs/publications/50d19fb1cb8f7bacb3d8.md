---
title: 'Predicting metropolitan house-price downturns: a machine learning panel study
  across forecast horizons'
authors:
- Kala Nisha Gopinathan
- Hari Hara Krishna Kumar Viswanathan
date: '2026-10-14'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1108/ijhma-08-2026-0318
abstract: 'Purpose This paper aims to evaluate whether metropolitan house-price downturns
  can be predicted out-of-sample, how predictability varies with the forecast horizon
  and whether machine learning classifiers improve on a naive persistence benchmark.
  Design/methodology/approach Using a panel of 94 US metropolitan areas drawn from
  the Federal Housing Finance Agency (FHFA) All-Transactions House Price Index (1978–2026;
  18,083 metro-quarters), a downturn is defined as a metropolitan index that is net
  lower h quarters ahead. Eight classifiers (four support-vector-machine kernels,
  random forest, gradient boosting, a feedforward neural network and logistic regression)
  and a persistence rule are compared across horizons of 1, 4 and 8 quarters. Models
  are evaluated with a leakage-safe expanding-window panel protocol, tuned on the
  area under the receiver operating characteristic (ROC) curve and assigned a decision
  threshold that maximizes the training geometric mean of sensitivity and specificity.
  Inference uses a quarter-blocked bootstrap. Findings Metropolitan downturns are
  predictable out-of-sample, but a persistence benchmark tuned to the same operating
  criterion as the models captures most of that predictability. On the geometric mean
  of sensitivity and specificity, the primary metric, the tuned benchmark reaches
  0.68–0.76 across horizons and the best classifier 0.75–0.82. Computed within each
  test block, the classifiers’ area under the ROC curve is 0.62–0.79. After correction
  for multiple comparisons across models and horizons, the one-quarter random forest
  improves on the tuned benchmark in the main analysis (Holm-adjusted p = 0.008).
  This finding does not hold with seasonally adjusted labels or equal training sizes.
  No single algorithm dominates, and parsimonious linear and logistic specifications
  are competitive throughout. Under an asymmetric loss that weights missed downturns
  more heavily than false alarms, the classifiers reduce total misclassification cost
  relative to persistence at all horizons. Research limitations/implications The index
  is a smoothed, periodically revised, not seasonally adjusted series; the evaluation
  uses the standard feature-outcome alignment rather than real-time data vintages;
  kernel models are trained on capped subsamples for tractability. A transaction-based
  purchase-only index and a full local-fundamentals panel are identified as priority
  extensions. Originality/value The study provides a metropolitan-panel early-warning
  comparison anchored to an explicit naive benchmark. The benchmark quantifies the
  modest marginal value of machine learning: one comparison is significant after correction
  in the main analysis, but that finding does not hold in the robustness checks; the
  study also contributes a horizon-specific attribution of metropolitan vulnerability
  and a cost-sensitive assessment of operational value.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221833631
url: https://doi.org/10.1108/ijhma-08-2026-0318
discovered_at: '2026-10-16'
tags: *id001
---

# Predicting metropolitan house\-price downturns: a machine learning panel study across forecast horizons

**Autores:** Kala Nisha Gopinathan; Hari Hara Krishna Kumar Viswanathan

**Data:** 2026-10-14 · **Tipo:** article

## Resumo

Purpose This paper aims to evaluate whether metropolitan house\-price downturns can be predicted out\-of\-sample, how predictability varies with the forecast horizon and whether machine learning classifiers improve on a naive persistence benchmark\. Design/methodology/approach Using a panel of 94 US metropolitan areas drawn from the Federal Housing Finance Agency \(FHFA\) All\-Transactions House Price Index \(1978–2026; 18,083 metro\-quarters\), a downturn is defined as a metropolitan index that is net lower h quarters ahead\. Eight classifiers \(four support\-vector\-machine kernels, random forest, gradient boosting, a feedforward neural network and logistic regression\) and a persistence rule are compared across horizons of 1, 4 and 8 quarters\. Models are evaluated with a leakage\-safe expanding\-window panel protocol, tuned on the area under the receiver operating characteristic \(ROC\) curve and assigned a decision threshold that maximizes the training geometric mean of sensitivity and specificity\. Inference uses a quarter\-blocked bootstrap\. Findings Metropolitan downturns are predictable out\-of\-sample, but a persistence benchmark tuned to the same operating criterion as the models captures most of that predictability\. On the geometric mean of sensitivity and specificity, the primary metric, the tuned benchmark reaches 0\.68–0\.76 across horizons and the best classifier 0\.75–0\.82\. Computed within each test block, the classifiers’ area under the ROC curve is 0\.62–0\.79\. After correction for multiple comparisons across models and horizons, the one\-quarter random forest improves on the tuned benchmark in the main analysis \(Holm\-adjusted p = 0\.008\)\. This finding does not hold with seasonally adjusted labels or equal training sizes\. No single algorithm dominates, and parsimonious linear and logistic specifications are competitive throughout\. Under an asymmetric loss that weights missed downturns more heavily than false alarms, the classifiers reduce total misclassification cost relative to persistence at all horizons\. Research limitations/implications The index is a smoothed, periodically revised, not seasonally adjusted series; the evaluation uses the standard feature\-outcome alignment rather than real\-time data vintages; kernel models are trained on capped subsamples for tractability\. A transaction\-based purchase\-only index and a full local\-fundamentals panel are identified as priority extensions\. Originality/value The study provides a metropolitan\-panel early\-warning comparison anchored to an explicit naive benchmark\. The benchmark quantifies the modest marginal value of machine learning: one comparison is significant after correction in the main analysis, but that finding does not hold in the robustness checks; the study also contributes a horizon\-specific attribution of metropolitan vulnerability and a cost\-sensitive assessment of operational value\.

[Consultar publicação](<https://doi.org/10.1108/ijhma-08-2026-0318>)
