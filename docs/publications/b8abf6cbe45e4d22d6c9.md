---
title: 'Metformin use and acute kidney failure risk in patients with type 2 diabetes:
  an explainable machine learning study with dual-cohort validation'
authors:
- Yang Liu
- Yinuo Wu
- Miao Xie
- Xiaojie Feng
- 温春娣
- 建璐 毕
date: '2026-10-10'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1186/s12882-026-05403-0
abstract: 'Diabetes mellitus and acute kidney injury (AKI) frequently coexist in clinical
  practice. Diabetes increases susceptibility to AKI through renal microvascular injury,
  whereas AKI may further aggravate metabolic disturbances. Metformin is widely used
  as a first-line treatment for type 2 diabetes (T2DM); however, its association with
  AKI remains controversial. This study aimed to develop and validate machine learning
  models incorporating metformin use to predict AKI in patients with T2DM and to assess
  the predictive value of metformin use for AKI risk. A total of 3,145 ICU patients
  with T2DM were identified from the MIMIC-IV database. Clinical variables included
  demographic characteristics, comorbidities, vital signs, laboratory measurements,
  mechanical ventilation status, and metformin use. Propensity score matching was
  performed to balance baseline characteristics between metformin users and nonusers.
  The association between metformin use and AKI was assessed using conditional logistic
  regression and logistic regression with matched-pair cluster-robust standard errors.
  Candidate variables were selected using LASSO, followed by exploratory multivariable
  logistic regression to estimate the adjusted association. For the predictive analysis,
  base and metformin-augmented versions of the Clinical Logistic, LASSO Logistic,
  and XGBoost models were developed. Internal validation was performed using nested
  cross-validation, and external evaluation was conducted in an independent hospital
  cohort of 100 patients. Model performance was assessed using ROC-AUC, PR-AUC, Brier
  score, accuracy, sensitivity, specificity, positive predictive value, negative predictive
  value, and F1 score. The incremental predictive value of metformin use was evaluated
  using paired bootstrap resampling. SHAP was used to interpret the best-performing
  model, and a nomogram based on the Clinical Logistic plus metformin model was constructed
  for individualized risk estimation. The MIMIC-IV cohort included 3,145 ICU patients
  with type 2 diabetes, of whom 1,245 met the prespecified AKI criteria and 1,059
  had used metformin long term before admission. Propensity score matching yielded
  760 matched pairs with well-balanced baseline characteristics. Conditional logistic
  regression showed that preadmission metformin use was associated with lower odds
  of AKI (OR = 0.392, 95% CI: 0.306–0.502; P < 0.001). The result remained consistent
  when robust standard errors clustered by matched pair were applied (OR = 0.408,
  95% CI: 0.325–0.512; P < 0.001). The association persisted after further adjustment
  for variables selected by LASSO (OR = 0.343, 95% CI: 0.267–0.442; P < 0.001). A
  sensitivity analysis excluding patients with AKI at first ICU admission produced
  a similar result (OR = 0.427, 95% CI: 0.338–0.538; P < 0.001). After metformin use
  was added, ROC-AUC generally increased and Brier scores decreased across the three
  model classes. In the MIMIC-IV development cohort, the XGBoost plus metformin model
  showed the best performance, with a ROC-AUC of 0.863 (95% CI: 0.849–0.877), a PR-AUC
  of 0.816, and a Brier score of 0.148. In the independent hospital cohort, the Clinical
  Logistic plus metformin model performed best, with a ROC-AUC of 0.955 (95% CI: 0.910–1.000),
  a PR-AUC of 0.932, and a Brier score of 0.138. SHAP analysis identified metformin
  use as an important contributor to model predictions, with metformin use associated
  with a lower predicted risk of AKI. In patients with T2DM, metformin use was associated
  with lower odds of AKI and provided additional clinical information for AKI risk
  prediction. These findings may support risk stratification and medication safety
  assessment in this high-risk population.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221367645
url: https://doi.org/10.1186/s12882-026-05403-0
discovered_at: '2026-10-16'
tags: *id001
---

# Metformin use and acute kidney failure risk in patients with type 2 diabetes: an explainable machine learning study with dual\-cohort validation

**Autores:** Yang Liu; Yinuo Wu; Miao Xie; Xiaojie Feng; 温春娣; 建璐 毕

**Data:** 2026-10-10 · **Tipo:** article

## Resumo

Diabetes mellitus and acute kidney injury \(AKI\) frequently coexist in clinical practice\. Diabetes increases susceptibility to AKI through renal microvascular injury, whereas AKI may further aggravate metabolic disturbances\. Metformin is widely used as a first\-line treatment for type 2 diabetes \(T2DM\); however, its association with AKI remains controversial\. This study aimed to develop and validate machine learning models incorporating metformin use to predict AKI in patients with T2DM and to assess the predictive value of metformin use for AKI risk\. A total of 3,145 ICU patients with T2DM were identified from the MIMIC\-IV database\. Clinical variables included demographic characteristics, comorbidities, vital signs, laboratory measurements, mechanical ventilation status, and metformin use\. Propensity score matching was performed to balance baseline characteristics between metformin users and nonusers\. The association between metformin use and AKI was assessed using conditional logistic regression and logistic regression with matched\-pair cluster\-robust standard errors\. Candidate variables were selected using LASSO, followed by exploratory multivariable logistic regression to estimate the adjusted association\. For the predictive analysis, base and metformin\-augmented versions of the Clinical Logistic, LASSO Logistic, and XGBoost models were developed\. Internal validation was performed using nested cross\-validation, and external evaluation was conducted in an independent hospital cohort of 100 patients\. Model performance was assessed using ROC\-AUC, PR\-AUC, Brier score, accuracy, sensitivity, specificity, positive predictive value, negative predictive value, and F1 score\. The incremental predictive value of metformin use was evaluated using paired bootstrap resampling\. SHAP was used to interpret the best\-performing model, and a nomogram based on the Clinical Logistic plus metformin model was constructed for individualized risk estimation\. The MIMIC\-IV cohort included 3,145 ICU patients with type 2 diabetes, of whom 1,245 met the prespecified AKI criteria and 1,059 had used metformin long term before admission\. Propensity score matching yielded 760 matched pairs with well\-balanced baseline characteristics\. Conditional logistic regression showed that preadmission metformin use was associated with lower odds of AKI \(OR = 0\.392, 95% CI: 0\.306–0\.502; P &lt; 0\.001\)\. The result remained consistent when robust standard errors clustered by matched pair were applied \(OR = 0\.408, 95% CI: 0\.325–0\.512; P &lt; 0\.001\)\. The association persisted after further adjustment for variables selected by LASSO \(OR = 0\.343, 95% CI: 0\.267–0\.442; P &lt; 0\.001\)\. A sensitivity analysis excluding patients with AKI at first ICU admission produced a similar result \(OR = 0\.427, 95% CI: 0\.338–0\.538; P &lt; 0\.001\)\. After metformin use was added, ROC\-AUC generally increased and Brier scores decreased across the three model classes\. In the MIMIC\-IV development cohort, the XGBoost plus metformin model showed the best performance, with a ROC\-AUC of 0\.863 \(95% CI: 0\.849–0\.877\), a PR\-AUC of 0\.816, and a Brier score of 0\.148\. In the independent hospital cohort, the Clinical Logistic plus metformin model performed best, with a ROC\-AUC of 0\.955 \(95% CI: 0\.910–1\.000\), a PR\-AUC of 0\.932, and a Brier score of 0\.138\. SHAP analysis identified metformin use as an important contributor to model predictions, with metformin use associated with a lower predicted risk of AKI\. In patients with T2DM, metformin use was associated with lower odds of AKI and provided additional clinical information for AKI risk prediction\. These findings may support risk stratification and medication safety assessment in this high\-risk population\.

[Consultar publicação](<https://doi.org/10.1186/s12882-026-05403-0>)
