---
title: Clinically Interpretable Biological Age Estimation Using CatBoost and SHAP
  with Continuous and Categorical Features from NHANES
authors:
- Yanni Sun
- Zheng Qu
- Kevin Ren
- Zhanglin Lin Cui
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Biological age (BA) captures inter-individual variation in physiological
  aging beyond chronological age (CA). Although machine-learning models have advanced
  BA estimation, many rely primarily on continuous laboratory biomarkers, and SHapley
  Additive exPlanations (SHAP) dependence plots are typically interpreted visually.
  We developed a clinically interpretable machine-learning framework for BA estimation
  using heterogeneous clinical data from the National Health and Nutrition Examination
  Survey (NHANES 2011-March 2020, N = 24,983 adults aged >= 18). A CatBoost regression
  model incorporated 44 demographic, laboratory, physical examination, and lifestyle
  predictors to estimate CA, defining model-estimated age as BA. SHAP provided multi-level
  interpretability. Crucially, building on standard visual inspection, we implemented
  a prespecified automated procedure directly on SHAP dependence plots to quantify
  feature-value ranges associated with lowest and highest BA contributions, corresponding
  adjustment magnitudes, and zero-crossing thresholds. Model-estimated BA strongly
  correlated with CA in held-out testing data (Pearson r = 0.798, P < 0.001). Population-level
  SHAP identified blood urea nitrogen, serum glucose, vigorous recreational activity,
  red cell distribution width, and alanine aminotransferase among the leading predictors,
  with three categorical variables ranking among the top 25. Automated quantitative
  SHAP analysis mapped predictor-specific ranges, effect sizes, and inflection points,
  while waterfall plots enabled individual explanations. By extending qualitative
  visual interpretation to reproducible quantitative metrics across heterogeneous
  clinical data, this framework enhances transparency and provides a scalable methodological
  foundation for biological aging research and precision health.
source:
- arXiv
source_ids:
- arxiv:2610.20868
url: https://arxiv.org/abs/2610.20868
discovered_at: '2026-10-16'
tags: *id001
---

# Clinically Interpretable Biological Age Estimation Using CatBoost and SHAP with Continuous and Categorical Features from NHANES

**Autores:** Yanni Sun; Zheng Qu; Kevin Ren; Zhanglin Lin Cui

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Biological age \(BA\) captures inter\-individual variation in physiological aging beyond chronological age \(CA\)\. Although machine\-learning models have advanced BA estimation, many rely primarily on continuous laboratory biomarkers, and SHapley Additive exPlanations \(SHAP\) dependence plots are typically interpreted visually\. We developed a clinically interpretable machine\-learning framework for BA estimation using heterogeneous clinical data from the National Health and Nutrition Examination Survey \(NHANES 2011\-March 2020, N = 24,983 adults aged &gt;= 18\)\. A CatBoost regression model incorporated 44 demographic, laboratory, physical examination, and lifestyle predictors to estimate CA, defining model\-estimated age as BA\. SHAP provided multi\-level interpretability\. Crucially, building on standard visual inspection, we implemented a prespecified automated procedure directly on SHAP dependence plots to quantify feature\-value ranges associated with lowest and highest BA contributions, corresponding adjustment magnitudes, and zero\-crossing thresholds\. Model\-estimated BA strongly correlated with CA in held\-out testing data \(Pearson r = 0\.798, P &lt; 0\.001\)\. Population\-level SHAP identified blood urea nitrogen, serum glucose, vigorous recreational activity, red cell distribution width, and alanine aminotransferase among the leading predictors, with three categorical variables ranking among the top 25\. Automated quantitative SHAP analysis mapped predictor\-specific ranges, effect sizes, and inflection points, while waterfall plots enabled individual explanations\. By extending qualitative visual interpretation to reproducible quantitative metrics across heterogeneous clinical data, this framework enhances transparency and provides a scalable methodological foundation for biological aging research and precision health\.

[Consultar publicação](<https://arxiv.org/abs/2610.20868>)
