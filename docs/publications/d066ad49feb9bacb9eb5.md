---
title: $L_0$ Feature Selection via Monte Carlo Tree Search in High-Dimensional Financial
  Regression
authors:
- Cameron Mouangue
- Tristan Cazenave
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Feature selection is a central problem in high-dimensional financial regression,
  where large numbers of engineered variables and strong correlations among predictors
  reduce model stability and interpretability. $L_1$ regularization (Lasso) is widely
  used for sparse regression, but its shrinkage can be restrictive when informative
  signals are spread across correlated variables. Exact sparse regression avoids this
  shrinkage but requires solving a combinatorial optimization problem that is computationally
  difficult and is typically fit to minimize in-sample rather than out-of-sample error.
  This paper presents a feature selection framework based on Monte Carlo Tree Search
  with Generalized Nested Rollout Policy Adaptation (GNRPA). Feature selection is
  formulated as a sequential decision process, and candidate subsets are scored by
  their out-of-sample validation performance rather than training error. The method
  also supports a lexicographic objective accounting for subset size and multicollinearity.
  We study this approach on a contemporaneous explanatory regression task: explaining
  the weekly return of the NASDAQ-100 index from 1,072 engineered features spanning
  market, macroeconomic, and factor data. This isolates the value of subset selection
  under multicollinearity from the separate problem of predictive forecasting. On
  this task, the proposed method identifies sparse feature subsets with higher out-of-sample
  explanatory power than an optimized Lasso baseline, reaching an out-of-sample $R^2$
  of 0.6961 versus 0.6313 for Lasso. These results suggest that Monte Carlo Tree Search
  is a practical alternative to convex regularization for sparse explanatory feature
  selection in financial regression, with potential value for factor attribution and
  risk decomposition where transparency matters as much as out-of-sample fit.'
source:
- arXiv
source_ids:
- arxiv:2610.13574
url: https://arxiv.org/abs/2610.13574
discovered_at: '2026-10-16'
tags: *id001
---

# $L\_0$ Feature Selection via Monte Carlo Tree Search in High\-Dimensional Financial Regression

**Autores:** Cameron Mouangue; Tristan Cazenave

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Feature selection is a central problem in high\-dimensional financial regression, where large numbers of engineered variables and strong correlations among predictors reduce model stability and interpretability\. $L\_1$ regularization \(Lasso\) is widely used for sparse regression, but its shrinkage can be restrictive when informative signals are spread across correlated variables\. Exact sparse regression avoids this shrinkage but requires solving a combinatorial optimization problem that is computationally difficult and is typically fit to minimize in\-sample rather than out\-of\-sample error\. This paper presents a feature selection framework based on Monte Carlo Tree Search with Generalized Nested Rollout Policy Adaptation \(GNRPA\)\. Feature selection is formulated as a sequential decision process, and candidate subsets are scored by their out\-of\-sample validation performance rather than training error\. The method also supports a lexicographic objective accounting for subset size and multicollinearity\. We study this approach on a contemporaneous explanatory regression task: explaining the weekly return of the NASDAQ\-100 index from 1,072 engineered features spanning market, macroeconomic, and factor data\. This isolates the value of subset selection under multicollinearity from the separate problem of predictive forecasting\. On this task, the proposed method identifies sparse feature subsets with higher out\-of\-sample explanatory power than an optimized Lasso baseline, reaching an out\-of\-sample $R^2$ of 0\.6961 versus 0\.6313 for Lasso\. These results suggest that Monte Carlo Tree Search is a practical alternative to convex regularization for sparse explanatory feature selection in financial regression, with potential value for factor attribution and risk decomposition where transparency matters as much as out\-of\-sample fit\.

[Consultar publicação](<https://arxiv.org/abs/2610.13574>)
