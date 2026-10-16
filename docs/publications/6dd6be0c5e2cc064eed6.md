---
title: A machine learning model for in-hospital mortality prediction in patients with
  sepsis-related myocardial injury
authors:
- Da-cheng Wang
- Yan-pin Liu
- Yu-ting Wang
- Xianjing Zhuang
- Xiao-peng YIN
- Xinyuan Zhang
- Yan Zhuang
date: '2026-10-12'
type: article
category: &id001
- Ciências Cognitivas
- Inteligência Artificial
doi: 10.1371/journal.pdig.0001758
abstract: Sepsis-related myocardial injury (SRMI) is associated with high mortality,
  but the transportability of prediction models across heterogeneous cohorts remains
  uncertain. We developed and externally validated a machine learning model for in-hospital
  mortality prediction in SRMI and evaluated its discrimination, calibration, interpretability,
  and distributional shift across cohorts. Using MIMIC-IV for development and MIMIC-III
  and a local cohort for external validation (n = 1,226, 962, and 280, respectively),
  we compared eight classification algorithms. A two-stage feature-selection strategy,
  recursive feature accumulation and sequential elimination with incremental feature
  evaluation, ranked 31 candidate variables to derive a parsimonious predictor set.
  The selected model was evaluated for discrimination, precision-recall performance,
  calibration, clinical utility, and risk stratification. Logistic recalibration,
  population stability index (PSI) analysis, and SHapley Additive exPlanations (SHAP)
  were used to assess probability alignment, cross-cohort distributional shift, and
  model interpretability. Feature selection reduced 31 candidate variables to 8 predictors
  with little loss of cross-validated performance (AUC, 0.819 with 31 variables versus
  0.810 with 8 variables). The selected random forest model achieved an AUC of 0.819
  (bootstrap 95% CI, 0.787-0.848) and a PR-AUC of 0.702 (0.657-0.751) in MIMIC-III,
  and an AUC of 0.758 (0.693-0.816) and a PR-AUC of 0.525 (0.435-0.630) in the local
  cohort. Recalibration reduced the Brier score from 0.162 to 0.147 in MIMIC-III and
  from 0.233 to 0.196 in the local cohort. PSI indicated minimal distributional shift
  between MIMIC-IV and MIMIC-III but substantial shift in the local cohort, particularly
  for SOFA score, respiratory rate, and prothrombin time. SHAP identified prothrombin
  time, invasive ventilation, lactate, temperature, and urine output as major contributors
  to model predictions. In two external cohorts, an 8-variable random forest model
  showed moderate discrimination for mortality prediction in SRMI. The evaluation
  of external performance, calibration, distributional shift, and SHAP-based explanations
  provides an assessment of model transportability. Prospective validation is needed
  before clinical deployment.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221522848
url: https://doi.org/10.1371/journal.pdig.0001758
discovered_at: '2026-10-16'
tags: *id001
---

# A machine learning model for in\-hospital mortality prediction in patients with sepsis\-related myocardial injury

**Autores:** Da\-cheng Wang; Yan\-pin Liu; Yu\-ting Wang; Xianjing Zhuang; Xiao\-peng YIN; Xinyuan Zhang; Yan Zhuang

**Data:** 2026-10-12 · **Tipo:** article

## Resumo

Sepsis\-related myocardial injury \(SRMI\) is associated with high mortality, but the transportability of prediction models across heterogeneous cohorts remains uncertain\. We developed and externally validated a machine learning model for in\-hospital mortality prediction in SRMI and evaluated its discrimination, calibration, interpretability, and distributional shift across cohorts\. Using MIMIC\-IV for development and MIMIC\-III and a local cohort for external validation \(n = 1,226, 962, and 280, respectively\), we compared eight classification algorithms\. A two\-stage feature\-selection strategy, recursive feature accumulation and sequential elimination with incremental feature evaluation, ranked 31 candidate variables to derive a parsimonious predictor set\. The selected model was evaluated for discrimination, precision\-recall performance, calibration, clinical utility, and risk stratification\. Logistic recalibration, population stability index \(PSI\) analysis, and SHapley Additive exPlanations \(SHAP\) were used to assess probability alignment, cross\-cohort distributional shift, and model interpretability\. Feature selection reduced 31 candidate variables to 8 predictors with little loss of cross\-validated performance \(AUC, 0\.819 with 31 variables versus 0\.810 with 8 variables\)\. The selected random forest model achieved an AUC of 0\.819 \(bootstrap 95% CI, 0\.787\-0\.848\) and a PR\-AUC of 0\.702 \(0\.657\-0\.751\) in MIMIC\-III, and an AUC of 0\.758 \(0\.693\-0\.816\) and a PR\-AUC of 0\.525 \(0\.435\-0\.630\) in the local cohort\. Recalibration reduced the Brier score from 0\.162 to 0\.147 in MIMIC\-III and from 0\.233 to 0\.196 in the local cohort\. PSI indicated minimal distributional shift between MIMIC\-IV and MIMIC\-III but substantial shift in the local cohort, particularly for SOFA score, respiratory rate, and prothrombin time\. SHAP identified prothrombin time, invasive ventilation, lactate, temperature, and urine output as major contributors to model predictions\. In two external cohorts, an 8\-variable random forest model showed moderate discrimination for mortality prediction in SRMI\. The evaluation of external performance, calibration, distributional shift, and SHAP\-based explanations provides an assessment of model transportability\. Prospective validation is needed before clinical deployment\.

[Consultar publicação](<https://doi.org/10.1371/journal.pdig.0001758>)
