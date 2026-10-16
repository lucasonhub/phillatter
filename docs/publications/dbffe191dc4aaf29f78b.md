---
title: 'Rainfall Memory Flood Index (RMFI): An I30-Based Framework for Spatiotemporal
  Flood Susceptibility Assessment'
authors:
- Suat Şahin
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.5281/zenodo.23341139
abstract: 'Flood susceptibility assessments commonly rely on static terrain variables
  and temporally aggregated rainfall indicators, although flood generation is strongly
  influenced by antecedent hydrological conditions and the seasonal structure of rainfall
  forcing. This study introduces the Rainfall Memory Flood Index (RMFI), an I30-based
  framework for spatiotemporal flood susceptibility assessment. The approach integrates
  elevation with a rainfall-memory component derived from monthly erosivity statistics.
  For each month, the rainfall-memory term is calculated from monthly mean and maximum
  event erosivity values obtained from rainfall events separated according to the
  RUSLE-R procedure, while monthly I30 is defined from the event producing the monthly
  maximum erosivity. Flood occurrence is modelled as a binary outcome using a 1209-point
  dataset comprising 65.9% flood and 34.1% non-flood observations. Two predictor structures
  are evaluated: an annual formulation based on elevation and total_I30 × S_total,
  and monthly formulations based on elevation and I30_m × S_m. Four machine-learning
  algorithms, Logistic Regression, Random Forest, XGBoost, and LightGBM, are evaluated
  using 70/30 holdout validation and stratified 5-fold cross-validation. Results show
  that monthly RMFI formulations consistently outperform the annual aggregation. The
  strongest performance is obtained in June, with cross-validated values of ROC AUC
  ≈ 0.86, F1 ≈ 0.84, and PR AUC ≈ 0.93, while similarly strong results are observed
  in January and November. These findings indicate that flood susceptibility is more
  effectively captured when rainfall forcing is represented through a temporally explicit,
  memory-sensitive structure rather than through annual accumulation alone, supporting
  a parsimonious, physically interpretable, and transferable framework for flood susceptibility
  mapping in data-constrained environments.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221585073
url: https://doi.org/10.5281/zenodo.23341139
discovered_at: '2026-10-16'
tags: *id001
---

# Rainfall Memory Flood Index \(RMFI\): An I30\-Based Framework for Spatiotemporal Flood Susceptibility Assessment

**Autores:** Suat Şahin

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Flood susceptibility assessments commonly rely on static terrain variables and temporally aggregated rainfall indicators, although flood generation is strongly influenced by antecedent hydrological conditions and the seasonal structure of rainfall forcing\. This study introduces the Rainfall Memory Flood Index \(RMFI\), an I30\-based framework for spatiotemporal flood susceptibility assessment\. The approach integrates elevation with a rainfall\-memory component derived from monthly erosivity statistics\. For each month, the rainfall\-memory term is calculated from monthly mean and maximum event erosivity values obtained from rainfall events separated according to the RUSLE\-R procedure, while monthly I30 is defined from the event producing the monthly maximum erosivity\. Flood occurrence is modelled as a binary outcome using a 1209\-point dataset comprising 65\.9% flood and 34\.1% non\-flood observations\. Two predictor structures are evaluated: an annual formulation based on elevation and total\_I30 × S\_total, and monthly formulations based on elevation and I30\_m × S\_m\. Four machine\-learning algorithms, Logistic Regression, Random Forest, XGBoost, and LightGBM, are evaluated using 70/30 holdout validation and stratified 5\-fold cross\-validation\. Results show that monthly RMFI formulations consistently outperform the annual aggregation\. The strongest performance is obtained in June, with cross\-validated values of ROC AUC ≈ 0\.86, F1 ≈ 0\.84, and PR AUC ≈ 0\.93, while similarly strong results are observed in January and November\. These findings indicate that flood susceptibility is more effectively captured when rainfall forcing is represented through a temporally explicit, memory\-sensitive structure rather than through annual accumulation alone, supporting a parsimonious, physically interpretable, and transferable framework for flood susceptibility mapping in data\-constrained environments\.

[Consultar publicação](<https://doi.org/10.5281/zenodo.23341139>)
