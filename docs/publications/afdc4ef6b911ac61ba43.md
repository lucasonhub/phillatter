---
title: Availability-Aware Multitask Learning for Robust Clinical Prediction from Incomplete
  Electronic Health Records
authors:
- Zhainagul Khamitova
- Gulmira Omarova
- Akerke Akanova
- Aliya Abdukarimova
- Kuanysh Kadirkulov
- Bagdat Satayev
- Aliya Beissegul
- Abdugani Kholbekov
- Gulnoz Dzhiyanmuratova
- Aizat Amirbay
date: '2026-10-16'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3390/computers15100723
abstract: This study presents NORIA, an availability-aware multitask learning framework
  for clinical prediction from incomplete electronic health records (EHRs). We analyzed
  a public dataset of 77,724 patients and 107 numerical features. To prevent temporal
  leakage, predictors were grouped by availability, and training-only feature selection
  identified three baseline and two first-year variables. NORIA jointly predicts baseline
  and updated glycemic control, an HbA1c change index, and 21 medication labels using
  shared representations, masked training, and stage-specific prediction updates.
  Comparators included classical machine learning, gradient boosting, deep tabular
  models, and multitask architectures (MMoE and PLE). On the internal test set, NORIA
  achieved AUROCs of 0.8554 and 0.8888 for baseline and updated glycemic control,
  respectively, and medication macro-AP of 0.1854 versus 0.1879 for CatBoost. The
  predefined medication improvement criterion was not met. With 20% of baseline features
  artificially masked, updated-control AUROC declined by 0.0271 for NORIA, versus
  0.0510 for CatBoost and 0.0542 for FT-Transformer. Ablation analyses indicated that
  masked training provided the clearest robustness benefit. NORIA thus demonstrated
  competitive accuracy and robustness in selected simulated missing-data scenarios,
  without establishing overall superiority.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222662277
url: https://doi.org/10.3390/computers15100723
discovered_at: '2026-10-19'
tags: *id001
---

# Availability\-Aware Multitask Learning for Robust Clinical Prediction from Incomplete Electronic Health Records

**Autores:** Zhainagul Khamitova; Gulmira Omarova; Akerke Akanova; Aliya Abdukarimova; Kuanysh Kadirkulov; Bagdat Satayev; Aliya Beissegul; Abdugani Kholbekov; Gulnoz Dzhiyanmuratova; Aizat Amirbay

**Data:** 2026-10-16 · **Tipo:** article

## Resumo

This study presents NORIA, an availability\-aware multitask learning framework for clinical prediction from incomplete electronic health records \(EHRs\)\. We analyzed a public dataset of 77,724 patients and 107 numerical features\. To prevent temporal leakage, predictors were grouped by availability, and training\-only feature selection identified three baseline and two first\-year variables\. NORIA jointly predicts baseline and updated glycemic control, an HbA1c change index, and 21 medication labels using shared representations, masked training, and stage\-specific prediction updates\. Comparators included classical machine learning, gradient boosting, deep tabular models, and multitask architectures \(MMoE and PLE\)\. On the internal test set, NORIA achieved AUROCs of 0\.8554 and 0\.8888 for baseline and updated glycemic control, respectively, and medication macro\-AP of 0\.1854 versus 0\.1879 for CatBoost\. The predefined medication improvement criterion was not met\. With 20% of baseline features artificially masked, updated\-control AUROC declined by 0\.0271 for NORIA, versus 0\.0510 for CatBoost and 0\.0542 for FT\-Transformer\. Ablation analyses indicated that masked training provided the clearest robustness benefit\. NORIA thus demonstrated competitive accuracy and robustness in selected simulated missing\-data scenarios, without establishing overall superiority\.

[Consultar publicação](<https://doi.org/10.3390/computers15100723>)
