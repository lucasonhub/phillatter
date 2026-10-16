---
title: An integrated explainable machine learning framework for prediction explanation
  and audit in high stakes binary classification
authors:
- Yan Liu
- Mengjie Shi
- Jingbo Huang
- Chuan He
date: '2026-10-12'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1038/s41598-026-74012-6
abstract: Machine learning classifiers are increasingly deployed in high-stakes decision
  systems, yet their opacity creates governance risks that undermine accountability
  and trust. This study proposes an integrated framework unifying predictive modelling,
  explainability, and model auditing, evaluated on a primary public tabular dataset
  (Lending Club) and an independent benchmark dataset (Give Me Some Credit) drawn
  from the consumer-credit domain. The framework enforces a strict decision-time feature-availability
  policy under which all post-origination repayment variables are excluded, defines
  default over a fixed 24-month outcome horizon, and combines class-imbalance handling,
  seven benchmark classifiers (including a traditional scorecard), probability-calibration
  assessment, global and local explainability analysis with quantified SHAP–LIME agreement,
  and a six-dimension audit covering performance stability, feature reasonableness,
  error structure, subgroup fairness screening, threshold policy, and robustness to
  missing inputs. On the temporally held-out Lending Club test set, LightGBM achieved
  the strongest discrimination, with an AUC-ROC of 0.8451 (95% CI 0.8421–0.8481),
  AUC-PR of 0.6118, F1-score of 0.6097, and KS statistic of 0.5127; its advantage
  over CatBoost was not statistically significant, whereas both exceeded the non-boosting
  baselines. A similar ordering was observed on the independent benchmark, where severe
  class imbalance made AUC-PR more informative than accuracy. SHAP explanations identified
  interest rate, loan grade, revolving utilization, debt-to-income ratio, credit-history
  length, and income as the dominant predictors, and SHAP–LIME attributions agreed
  strongly across a systematic evaluation sample (mean Spearman correlation 0.84).
  The audit revealed stable cross-validation performance, mild temporal drift, adequate
  post-calibration reliability, and elevated false-positive rates for low-income and
  short-credit-history subgroups; because the datasets contain no directly observed
  protected attributes, these results constitute socioeconomic subgroup screening
  rather than a demonstration of demographic fairness. The study shows that predictive
  performance, interpretability, calibration, and auditability can be jointly evaluated
  in a single reproducible workflow, providing an operational technical-audit template
  that complements, but does not replace, legal and institutional review.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221527245
url: https://doi.org/10.1038/s41598-026-74012-6
discovered_at: '2026-10-16'
tags: *id001
---

# An integrated explainable machine learning framework for prediction explanation and audit in high stakes binary classification

**Autores:** Yan Liu; Mengjie Shi; Jingbo Huang; Chuan He

**Data:** 2026-10-12 · **Tipo:** article

## Resumo

Machine learning classifiers are increasingly deployed in high\-stakes decision systems, yet their opacity creates governance risks that undermine accountability and trust\. This study proposes an integrated framework unifying predictive modelling, explainability, and model auditing, evaluated on a primary public tabular dataset \(Lending Club\) and an independent benchmark dataset \(Give Me Some Credit\) drawn from the consumer\-credit domain\. The framework enforces a strict decision\-time feature\-availability policy under which all post\-origination repayment variables are excluded, defines default over a fixed 24\-month outcome horizon, and combines class\-imbalance handling, seven benchmark classifiers \(including a traditional scorecard\), probability\-calibration assessment, global and local explainability analysis with quantified SHAP–LIME agreement, and a six\-dimension audit covering performance stability, feature reasonableness, error structure, subgroup fairness screening, threshold policy, and robustness to missing inputs\. On the temporally held\-out Lending Club test set, LightGBM achieved the strongest discrimination, with an AUC\-ROC of 0\.8451 \(95% CI 0\.8421–0\.8481\), AUC\-PR of 0\.6118, F1\-score of 0\.6097, and KS statistic of 0\.5127; its advantage over CatBoost was not statistically significant, whereas both exceeded the non\-boosting baselines\. A similar ordering was observed on the independent benchmark, where severe class imbalance made AUC\-PR more informative than accuracy\. SHAP explanations identified interest rate, loan grade, revolving utilization, debt\-to\-income ratio, credit\-history length, and income as the dominant predictors, and SHAP–LIME attributions agreed strongly across a systematic evaluation sample \(mean Spearman correlation 0\.84\)\. The audit revealed stable cross\-validation performance, mild temporal drift, adequate post\-calibration reliability, and elevated false\-positive rates for low\-income and short\-credit\-history subgroups; because the datasets contain no directly observed protected attributes, these results constitute socioeconomic subgroup screening rather than a demonstration of demographic fairness\. The study shows that predictive performance, interpretability, calibration, and auditability can be jointly evaluated in a single reproducible workflow, providing an operational technical\-audit template that complements, but does not replace, legal and institutional review\.

[Consultar publicação](<https://doi.org/10.1038/s41598-026-74012-6>)
