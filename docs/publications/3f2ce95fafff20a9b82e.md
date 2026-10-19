---
title: 'Predicting lymph node metastasis in non-small cell lung cancer using clinical
  and PET/CT-derived morphological features: An interpretable machine-learning study'
authors:
- Yunchao Xu
- Jiajun Hao
- DOU Yujiao
- Biao Zeng
date: '2026-10-15'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1371/journal.pone.0361043
abstract: 'BACKGROUND: Accurate prediction of lymph node metastasis (LNM) in non-small
  cell lung cancer (NSCLC) is crucial for staging and treatment planning. This study
  aimed to establish a standardized machine learning workflow based on routinely available
  clinical, serological, and PET/CT-derived parameters to enhance preoperative LNM
  risk stratification. METHODS: This retrospective study included 255 patients with
  histologically confirmed NSCLC, all of whom underwent systematic lymph-node dissection.
  Patients were randomly divided, with stratification by pathological lymph-node status,
  into a training cohort (n = 178) and an internal held-out test test cohort (n =
  77). Candidate predictors were screened using univariable and multivariable logistic
  regression in the training cohort. Six machine-learning algorithms were trained
  and optimized using repeated nested five-fold cross-validation. After model development
  was completed, all six models were applied without modification to the test cohort.
  Test-set AUCs were compared using paired DeLong tests with Holm correction. The
  primary model was further evaluated for calibration, clinical utility, and feature
  contribution using SHAP. A conventional multivariable logistic regression model
  using the same four predictors was added as a simple reference model, and its discrimination
  and calibration were compared with those of XGBoost. RESULTS: Central tumor location,
  elevated carcinoembryonic antigen, elevated squamous cell carcinoma antigen, and
  solid nodule status were retained as predictors; none of the quantitative PET metabolic
  parameters remained independently associated with LNM. XGBoost achieved the highest
  cross-validated AUC among the six candidate machine-learning algorithms in the training
  cohort (0.735; 95% CI, 0.653-0.813) and was therefore designated the primary model.
  In the internal held-out test cohort, XGBoost achieved an AUC of 0.747 (95% CI,
  0.631-0.846). The conventional logistic regression reference model achieved a test
  AUC of 0.733 (95% CI, 0.612-0.841), with no significant difference from XGBoost
  (DeLong P = 0.301). Its Brier score was 0.152, compared with 0.198 for XGBoost.
  CONCLUSION: XGBoost model showed moderate discrimination and a high negative predictive
  value for pathological LNM in NSCLC. However, its limited positive predictive value
  and the absence of significant differences among the candidate algorithms support
  cautious interpretation. External multicenter evaluation is required before clinical
  implementation.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221969301
url: https://doi.org/10.1371/journal.pone.0361043
discovered_at: '2026-10-19'
tags: *id001
---

# Predicting lymph node metastasis in non\-small cell lung cancer using clinical and PET/CT\-derived morphological features: An interpretable machine\-learning study

**Autores:** Yunchao Xu; Jiajun Hao; DOU Yujiao; Biao Zeng

**Data:** 2026-10-15 · **Tipo:** article

## Resumo

BACKGROUND: Accurate prediction of lymph node metastasis \(LNM\) in non\-small cell lung cancer \(NSCLC\) is crucial for staging and treatment planning\. This study aimed to establish a standardized machine learning workflow based on routinely available clinical, serological, and PET/CT\-derived parameters to enhance preoperative LNM risk stratification\. METHODS: This retrospective study included 255 patients with histologically confirmed NSCLC, all of whom underwent systematic lymph\-node dissection\. Patients were randomly divided, with stratification by pathological lymph\-node status, into a training cohort \(n = 178\) and an internal held\-out test test cohort \(n = 77\)\. Candidate predictors were screened using univariable and multivariable logistic regression in the training cohort\. Six machine\-learning algorithms were trained and optimized using repeated nested five\-fold cross\-validation\. After model development was completed, all six models were applied without modification to the test cohort\. Test\-set AUCs were compared using paired DeLong tests with Holm correction\. The primary model was further evaluated for calibration, clinical utility, and feature contribution using SHAP\. A conventional multivariable logistic regression model using the same four predictors was added as a simple reference model, and its discrimination and calibration were compared with those of XGBoost\. RESULTS: Central tumor location, elevated carcinoembryonic antigen, elevated squamous cell carcinoma antigen, and solid nodule status were retained as predictors; none of the quantitative PET metabolic parameters remained independently associated with LNM\. XGBoost achieved the highest cross\-validated AUC among the six candidate machine\-learning algorithms in the training cohort \(0\.735; 95% CI, 0\.653\-0\.813\) and was therefore designated the primary model\. In the internal held\-out test cohort, XGBoost achieved an AUC of 0\.747 \(95% CI, 0\.631\-0\.846\)\. The conventional logistic regression reference model achieved a test AUC of 0\.733 \(95% CI, 0\.612\-0\.841\), with no significant difference from XGBoost \(DeLong P = 0\.301\)\. Its Brier score was 0\.152, compared with 0\.198 for XGBoost\. CONCLUSION: XGBoost model showed moderate discrimination and a high negative predictive value for pathological LNM in NSCLC\. However, its limited positive predictive value and the absence of significant differences among the candidate algorithms support cautious interpretation\. External multicenter evaluation is required before clinical implementation\.

[Consultar publicação](<https://doi.org/10.1371/journal.pone.0361043>)
