---
title: On the Encoding of Calendar Features in Covariate-Informed Time Series Foundation
  Models
authors:
- Alexander Kreusel
- Maximilian Beichter
- Alexandra Nikoltchovska
- Benjamin Schäfer
- Ralf Mikut
- Frederik Zahn
- Veit Hagenmeyer
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Time series foundation models (TSFMs) increasingly offer covariate support,
  with calendar information being the most common type of categorical covariate in
  practice, as it is available for every point in time. However, how these features
  are encoded is largely treated as an implementation detail rather than as an object
  of study, despite encoding being one of the few design choices left for pretrained
  models at inference time. With the present study, we demonstrate that the way information
  is propagated into the model substantially affects forecast accuracy of TSFMs. Therefore,
  we systematically compare seven calendar encodings, including three conventional
  target-agnostic representations (ordinal, one-hot, and cyclic) and four target encodings,
  across four state-of-the-art TSFMs on nine datasets from multiple domains in a zero-shot
  rolling evaluation. The nine datasets are influenced by social activities, such
  as weekends and holidays, making calendar information particularly relevant for
  forecasting. We find that encoding choice affects forecast accuracy across all models,
  with MASE differences of up to 9.9 % on non-holidays and 83 % on holidays within
  a single model. Effectiveness and utilization vary substantially across models.
  Improvements are concentrated around holidays, where calendar information provides
  signals unavailable from target history, while some model encoding combinations
  also improve non-holiday forecasts. A SHAP-based attribution analysis locates the
  contribution of the covariates relative to the autoregressive component and explains
  why some model-encoding combinations degrade performance. Our findings suggest that
  current benchmarks for covariate-informed TSFMs can distort model comparisons by
  imposing fixed encoding strategies.
source:
- arXiv
source_ids:
- arxiv:2610.13676
url: https://arxiv.org/abs/2610.13676
discovered_at: '2026-10-16'
tags: *id001
---

# On the Encoding of Calendar Features in Covariate\-Informed Time Series Foundation Models

**Autores:** Alexander Kreusel; Maximilian Beichter; Alexandra Nikoltchovska; Benjamin Schäfer; Ralf Mikut; Frederik Zahn; Veit Hagenmeyer

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Time series foundation models \(TSFMs\) increasingly offer covariate support, with calendar information being the most common type of categorical covariate in practice, as it is available for every point in time\. However, how these features are encoded is largely treated as an implementation detail rather than as an object of study, despite encoding being one of the few design choices left for pretrained models at inference time\. With the present study, we demonstrate that the way information is propagated into the model substantially affects forecast accuracy of TSFMs\. Therefore, we systematically compare seven calendar encodings, including three conventional target\-agnostic representations \(ordinal, one\-hot, and cyclic\) and four target encodings, across four state\-of\-the\-art TSFMs on nine datasets from multiple domains in a zero\-shot rolling evaluation\. The nine datasets are influenced by social activities, such as weekends and holidays, making calendar information particularly relevant for forecasting\. We find that encoding choice affects forecast accuracy across all models, with MASE differences of up to 9\.9 % on non\-holidays and 83 % on holidays within a single model\. Effectiveness and utilization vary substantially across models\. Improvements are concentrated around holidays, where calendar information provides signals unavailable from target history, while some model encoding combinations also improve non\-holiday forecasts\. A SHAP\-based attribution analysis locates the contribution of the covariates relative to the autoregressive component and explains why some model\-encoding combinations degrade performance\. Our findings suggest that current benchmarks for covariate\-informed TSFMs can distort model comparisons by imposing fixed encoding strategies\.

[Consultar publicação](<https://arxiv.org/abs/2610.13676>)
