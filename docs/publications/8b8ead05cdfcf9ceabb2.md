---
title: 'Revisiting early detection of violating android applications: Multi-source
  dataset validation and feature enrichment'
authors:
- Fadi Mohsen
- Yulin Zhang
- Ali Murat Gültekin
- Halil Bişğin
- Koerner Buchta
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1016/j.array.2026.101316
abstract: Accurate detection models for high-risk Android applications depend largely
  on the quality and reliability of the datasets used during training and validation.
  In this work, we revisit an existing Android application dataset originally constructed
  through marketplace monitoring and static feature extraction. Although the dataset
  enabled early machine-learning experiments, its labeling strategy has not been systematically
  validated.We introduce a consensus-based validation framework that combines the
  original dataset labels with evidence derived from VirusTotal, an online service
  that aggregates the outputs of numerous antivirus scanners, and Quark Engine, a
  rule-based analysis framework. In addition to reassessing the reliability of the
  label, we extend the dataset by attaching selected features obtained from these
  sources, including antivirus consensus indicators, lifecycle-based temporal features,
  and rule-based behavioral risk metrics.Using the validated and enriched dataset,
  we retrain several XGBoost machine learning classifiers and evaluate their performance.
  The results show that feature augmentation improves model accuracy but only modestly.
  On the other hand, the consensus-based label validation improves classification
  reliability significantly, improving classification accuracy from 78% to 97% and
  an AUC of 0.997. Feature importance analysis further shows that external threat-intelligence
  features complement marketplace metadata, with VirusTotal-derived indicators contributing
  the strongest additional predictive signals. Our findings highlight the value of
  multi-source validation and dataset enrichment for improving the robustness of machine
  learning pipelines in Android malware detection.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221109674
url: https://doi.org/10.1016/j.array.2026.101316
discovered_at: '2026-10-16'
tags: *id001
---

# Revisiting early detection of violating android applications: Multi\-source dataset validation and feature enrichment

**Autores:** Fadi Mohsen; Yulin Zhang; Ali Murat Gültekin; Halil Bişğin; Koerner Buchta

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

Accurate detection models for high\-risk Android applications depend largely on the quality and reliability of the datasets used during training and validation\. In this work, we revisit an existing Android application dataset originally constructed through marketplace monitoring and static feature extraction\. Although the dataset enabled early machine\-learning experiments, its labeling strategy has not been systematically validated\.We introduce a consensus\-based validation framework that combines the original dataset labels with evidence derived from VirusTotal, an online service that aggregates the outputs of numerous antivirus scanners, and Quark Engine, a rule\-based analysis framework\. In addition to reassessing the reliability of the label, we extend the dataset by attaching selected features obtained from these sources, including antivirus consensus indicators, lifecycle\-based temporal features, and rule\-based behavioral risk metrics\.Using the validated and enriched dataset, we retrain several XGBoost machine learning classifiers and evaluate their performance\. The results show that feature augmentation improves model accuracy but only modestly\. On the other hand, the consensus\-based label validation improves classification reliability significantly, improving classification accuracy from 78% to 97% and an AUC of 0\.997\. Feature importance analysis further shows that external threat\-intelligence features complement marketplace metadata, with VirusTotal\-derived indicators contributing the strongest additional predictive signals\. Our findings highlight the value of multi\-source validation and dataset enrichment for improving the robustness of machine learning pipelines in Android malware detection\.

[Consultar publicação](<https://doi.org/10.1016/j.array.2026.101316>)
