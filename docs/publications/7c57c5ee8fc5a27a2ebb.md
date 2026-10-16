---
title: A mask-aware multivariate correlation transformer for GDP forecasting with
  incomplete macroeconomic time series
authors:
- Asiye Omidian
- Zohreh Keivan
- Athena Omidian
- maral mirza mohammadi
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1007/s44163-026-02538-9
abstract: Accurate Gross Domestic Product (GDP) forecasting is challenging when macroeconomic
  histories are multivariate, heterogeneous, short, and incomplete. This study proposes
  a mask-aware Multivariate Correlation Transformer (MCT) that integrates explicit
  observation masks, supervised reconstruction where ground truth is available, asymmetric
  cosine-normalized query–key attention, dynamic feedforward processing, and similarity-structure
  self-distillation. The analysis uses annual data for 14 countries from the IMF World
  Economic Outlook, IMF International Financial Statistics, and Penn World Table,
  with neural models trained globally on pooled 10-year input windows and one-year
  multivariate targets. Forecast performance is evaluated from a common origin at
  the end of 2019, with H1 generated directly for 2020 and H2–H5 generated recursively
  through 2024 without incorporating realized test-period outcomes or re-estimating
  model parameters. The benchmark set includes statistical and recurrent models, persistence/trend/growth
  rules, contemporary forecasting architectures, and conventional machine-learning
  methods. Using equal-country aggregation, the Proposed MCT achieves a root mean
  squared error (RMSE) of 0.141693, a mean absolute error (MAE) of 0.137203, a symmetric
  mean absolute percentage error (sMAPE) of 11.6653%, and Theil’s U of 0.159992. The
  strongest additional point-forecast comparator is iTransformer with RMSE = 0.168200.
  Dependence-aware inference against the seven original benchmarks, repeated-seed
  experiments, ablations, and random and structured missingness stress tests provide
  complementary evidence for the observed performance. Reconstruction accuracy is
  verified only for deliberately withheld observations with known ground truth, while
  learned attention scores are interpreted as internal neural similarities rather
  than statistical correlations or causal relationships. The evidence remains specific
  to the single-origin 2020–2024 evaluation. The 2025–2030 outputs are reported separately
  as post-evaluation model-based projections rather than additional validated forecasts.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221616418
url: https://doi.org/10.1007/s44163-026-02538-9
discovered_at: '2026-10-16'
tags: *id001
---

# A mask\-aware multivariate correlation transformer for GDP forecasting with incomplete macroeconomic time series

**Autores:** Asiye Omidian; Zohreh Keivan; Athena Omidian; maral mirza mohammadi

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Accurate Gross Domestic Product \(GDP\) forecasting is challenging when macroeconomic histories are multivariate, heterogeneous, short, and incomplete\. This study proposes a mask\-aware Multivariate Correlation Transformer \(MCT\) that integrates explicit observation masks, supervised reconstruction where ground truth is available, asymmetric cosine\-normalized query–key attention, dynamic feedforward processing, and similarity\-structure self\-distillation\. The analysis uses annual data for 14 countries from the IMF World Economic Outlook, IMF International Financial Statistics, and Penn World Table, with neural models trained globally on pooled 10\-year input windows and one\-year multivariate targets\. Forecast performance is evaluated from a common origin at the end of 2019, with H1 generated directly for 2020 and H2–H5 generated recursively through 2024 without incorporating realized test\-period outcomes or re\-estimating model parameters\. The benchmark set includes statistical and recurrent models, persistence/trend/growth rules, contemporary forecasting architectures, and conventional machine\-learning methods\. Using equal\-country aggregation, the Proposed MCT achieves a root mean squared error \(RMSE\) of 0\.141693, a mean absolute error \(MAE\) of 0\.137203, a symmetric mean absolute percentage error \(sMAPE\) of 11\.6653%, and Theil’s U of 0\.159992\. The strongest additional point\-forecast comparator is iTransformer with RMSE = 0\.168200\. Dependence\-aware inference against the seven original benchmarks, repeated\-seed experiments, ablations, and random and structured missingness stress tests provide complementary evidence for the observed performance\. Reconstruction accuracy is verified only for deliberately withheld observations with known ground truth, while learned attention scores are interpreted as internal neural similarities rather than statistical correlations or causal relationships\. The evidence remains specific to the single\-origin 2020–2024 evaluation\. The 2025–2030 outputs are reported separately as post\-evaluation model\-based projections rather than additional validated forecasts\.

[Consultar publicação](<https://doi.org/10.1007/s44163-026-02538-9>)
