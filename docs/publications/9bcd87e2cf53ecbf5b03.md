---
title: 'Feature-token clinical transformer for 24-h landmark mortality risk stratification
  in critically ill patients with heart failure: development and multicenter external
  validation'
authors:
- Mianxian Li
- Yuefei Zhou
- Chun Li
date: '2026-10-15'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3389/fcvm.2026.1945947
abstract: Background The first 24 h after ICU admission in critically ill patients
  with heart failure yield heterogeneous EHR evidence across vital signs, laboratory
  tests, treatments, organ support, and nurse-charted monitoring. Conventional scores
  and flat-vector ML models may not preserve individual variable identity or context.
  Methods We developed FTCT, encoding each predictor recorded during the first 24
  h after ICU admission as a clinically tagged token (value, missingness, identity,
  group). MIMIC-IV (2008–2019) served for development, validation, and internal testing;
  eICU-CRD (2014–2015) served for external validation. Included were adults with heart
  failure, a complete 24-h ICU observation window, and known discharge status. The
  endpoint was in-hospital all-cause death. Results MIMIC-IV included 11,156 stays
  and 1,484 deaths, partitioned into training ( n = 7,809), validation ( n = 1,673),
  and internal test ( n = 1,674) sets. eICU-CRD included 9,837 stays and 1,319 deaths.
  FTCT achieved an AUROC of 0.849 (95% CI, 0.835–0.863) internally and 0.804 (0.788–0.820)
  externally. Patient-paired AUROC differences vs. XGBoost were 0.027 (0.011–0.043)
  internally and 0.032 (0.014–0.050) externally. A matched FT-Transformer-style baseline
  achieved an external AUROC of 0.781 (0.760–0.801). In eICU-CRD, FTCT achieved an
  AUPRC of 0.296 (0.278–0.314), Brier score of 0.091 (0.085–0.097), and expected calibration
  error of 0.036 (0.030–0.042). In a post hoc cohort-specific descriptive operating
  analysis targeting approximately 85% specificity, external sensitivity was 0.662
  (0.636–0.687), positive predictive value 0.406 (0.385–0.427), negative predictive
  value 0.942 (0.937–0.947), and F1 score 0.503. Removing feature-token encoding produced
  the largest ablation loss in external AUROC (−0.031). Conclusions FTCT combines
  established feature-token Transformer modeling with clinical-group embeddings, explicit
  missingness representation, and group-aware pooling for 24-h landmark mortality
  risk stratification from structured EHR data recorded during the first 24 h after
  ICU admission. Its external validation and ablation results support prospective
  investigation, but do not yet demonstrate clinical utility, workflow integration,
  admission-time applicability, or autonomous use.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222183077
url: https://doi.org/10.3389/fcvm.2026.1945947
discovered_at: '2026-10-19'
tags: *id001
---

# Feature\-token clinical transformer for 24\-h landmark mortality risk stratification in critically ill patients with heart failure: development and multicenter external validation

**Autores:** Mianxian Li; Yuefei Zhou; Chun Li

**Data:** 2026-10-15 · **Tipo:** article

## Resumo

Background The first 24 h after ICU admission in critically ill patients with heart failure yield heterogeneous EHR evidence across vital signs, laboratory tests, treatments, organ support, and nurse\-charted monitoring\. Conventional scores and flat\-vector ML models may not preserve individual variable identity or context\. Methods We developed FTCT, encoding each predictor recorded during the first 24 h after ICU admission as a clinically tagged token \(value, missingness, identity, group\)\. MIMIC\-IV \(2008–2019\) served for development, validation, and internal testing; eICU\-CRD \(2014–2015\) served for external validation\. Included were adults with heart failure, a complete 24\-h ICU observation window, and known discharge status\. The endpoint was in\-hospital all\-cause death\. Results MIMIC\-IV included 11,156 stays and 1,484 deaths, partitioned into training \( n = 7,809\), validation \( n = 1,673\), and internal test \( n = 1,674\) sets\. eICU\-CRD included 9,837 stays and 1,319 deaths\. FTCT achieved an AUROC of 0\.849 \(95% CI, 0\.835–0\.863\) internally and 0\.804 \(0\.788–0\.820\) externally\. Patient\-paired AUROC differences vs\. XGBoost were 0\.027 \(0\.011–0\.043\) internally and 0\.032 \(0\.014–0\.050\) externally\. A matched FT\-Transformer\-style baseline achieved an external AUROC of 0\.781 \(0\.760–0\.801\)\. In eICU\-CRD, FTCT achieved an AUPRC of 0\.296 \(0\.278–0\.314\), Brier score of 0\.091 \(0\.085–0\.097\), and expected calibration error of 0\.036 \(0\.030–0\.042\)\. In a post hoc cohort\-specific descriptive operating analysis targeting approximately 85% specificity, external sensitivity was 0\.662 \(0\.636–0\.687\), positive predictive value 0\.406 \(0\.385–0\.427\), negative predictive value 0\.942 \(0\.937–0\.947\), and F1 score 0\.503\. Removing feature\-token encoding produced the largest ablation loss in external AUROC \(−0\.031\)\. Conclusions FTCT combines established feature\-token Transformer modeling with clinical\-group embeddings, explicit missingness representation, and group\-aware pooling for 24\-h landmark mortality risk stratification from structured EHR data recorded during the first 24 h after ICU admission\. Its external validation and ablation results support prospective investigation, but do not yet demonstrate clinical utility, workflow integration, admission\-time applicability, or autonomous use\.

[Consultar publicação](<https://doi.org/10.3389/fcvm.2026.1945947>)
