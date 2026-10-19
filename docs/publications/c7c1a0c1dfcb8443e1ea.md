---
title: An Explainable Uncertainty-Weighted Multi-Task Learning Framework for Joint
  Crop Recommendation and NPK Prediction with Probabilistic Crop Conditioning
authors:
- Aakash Verma and Vineet Kumar Avasthi
date: '2026-10-17'
type: article
category: &id001
- Inteligência Artificial
doi: 10.48175/ijarsct-38925
abstract: 'Crop selection and fertilizer planning are of generally based on farmer
  experience, even though suitable crops and nutrient needs depend on soil and environmental
  conditions that vary between fields. In many existing systems, crop recommendation
  and nutrient prediction are handled by separate models, and few explain how reliable
  a given prediction is. This study proposes a multi-task learning model that predicts
  the recommended crop and the nitrogen, phosphorus, and potassium (NPK) requirement
  from seven pre crop inputs: soil type, season, soil pH, temperature, water requirement,
  relative humidity, and water source. A shared network feeds a crop classification
  head and an NPK regression head. The NPK head receives the full predicted crop probability
  vector instead of the true crop label, and the two task losses are balanced using
  learned uncertainty parameters. Monte Carlo Dropout estimates the uncertainty of
  each prediction, and SHAP shows which inputs drove it. On a dataset of 57,000 observations
  covering 57 crops, the model reached an accuracy of 0.9496 and a macro F1-score
  of 0.9463 for crop classification, below Random Forest (0.9627) and XGBoost (0.9618).
  The mean NPK R² was 0.8537, compared with 0.8518 for XGBoost and 0.8501 for a standalone
  DNN. The calibration error was 0.0072, and results were stable across five random
  seeds. SHAP showed that soil type, season, and relative humidity contributed most
  to both tasks. The trained model was built into a recommendation system that returns
  a crop, NPK values with uncertainty intervals, and an explanation.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222813069
url: https://doi.org/10.48175/ijarsct-38925
discovered_at: '2026-10-19'
tags: *id001
---

# An Explainable Uncertainty\-Weighted Multi\-Task Learning Framework for Joint Crop Recommendation and NPK Prediction with Probabilistic Crop Conditioning

**Autores:** Aakash Verma and Vineet Kumar Avasthi

**Data:** 2026-10-17 · **Tipo:** article

## Resumo

Crop selection and fertilizer planning are of generally based on farmer experience, even though suitable crops and nutrient needs depend on soil and environmental conditions that vary between fields\. In many existing systems, crop recommendation and nutrient prediction are handled by separate models, and few explain how reliable a given prediction is\. This study proposes a multi\-task learning model that predicts the recommended crop and the nitrogen, phosphorus, and potassium \(NPK\) requirement from seven pre crop inputs: soil type, season, soil pH, temperature, water requirement, relative humidity, and water source\. A shared network feeds a crop classification head and an NPK regression head\. The NPK head receives the full predicted crop probability vector instead of the true crop label, and the two task losses are balanced using learned uncertainty parameters\. Monte Carlo Dropout estimates the uncertainty of each prediction, and SHAP shows which inputs drove it\. On a dataset of 57,000 observations covering 57 crops, the model reached an accuracy of 0\.9496 and a macro F1\-score of 0\.9463 for crop classification, below Random Forest \(0\.9627\) and XGBoost \(0\.9618\)\. The mean NPK R² was 0\.8537, compared with 0\.8518 for XGBoost and 0\.8501 for a standalone DNN\. The calibration error was 0\.0072, and results were stable across five random seeds\. SHAP showed that soil type, season, and relative humidity contributed most to both tasks\. The trained model was built into a recommendation system that returns a crop, NPK values with uncertainty intervals, and an explanation\.

[Consultar publicação](<https://doi.org/10.48175/ijarsct-38925>)
