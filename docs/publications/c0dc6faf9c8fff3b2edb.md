---
title: Graph Neural Network Modelling of Pre-Diagnostic Serum Proteomics for Pancreatic
  Cancer Detection
authors:
- Alexey A. Zaikin
- Aleksandra Gentry‐Maharaj
- Sophia Apostolidou
- Usha Menon
- Arseniy Trukhanov
- J.G. Oganezova
- Harry J. Whitwell
- Oleg B. Blyuss
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3390/diagnostics16203283
abstract: 'Background/Objectives: Pancreatic ductal adenocarcinoma (PDAC) has exceptionally
  high mortality, largely because of late diagnosis, while established blood biomarkers
  such as CA19-9 have limited sensitivity for early detection. We evaluated whether
  modelling serum proteomic measurements as supervised pairwise statistical graphs
  using synolitic graph neural networks (SGNNs) could provide a useful framework for
  pre-diagnostic PDAC classification. Methods: We analysed 217 pre-diagnostic serum
  samples from UKCTOCS, comprising 100 PDAC samples from 75 women and 117 control
  samples, profiled for 97 proteins. Samples were divided into a development set collected
  0–1 year before diagnosis (n = 110) and a temporal holdout set collected 1–2 years
  before diagnosis (n = 107); 25 PDAC participants contributed samples to both windows.
  The final SGNN used fold-internal mutual-information selection of 30 proteins, pairwise
  RBF-SVM-derived edge information, minimum-connected sparsification, and a 10-member
  GATv2 ensemble per cross-validation fold. Conventional machine-learning comparators
  were tuned using development data only. Results: The SGNN achieved a mean 5-fold
  development ROC-AUC of 75.33 ± 10.43%, lower than the tuned Random Forest (81.67%);
  the other tuned comparators achieved 77.67% (XGBoost), 77.17% (logistic regression),
  and 73.17% (SVM). Averaging predictions across the five-fold-specific SGNN ensembles
  yielded a temporal-holdout ROC-AUC of 64.35% (95% CI 52.6–74.6%). In the participant-independent
  subset of 25 PDAC cases not represented in development and 57 controls, ROC-AUC
  was 66.04% (95% CI 52.56–78.88%). Conclusions: SGNNs provide a feasible graph-based
  representation of pre-diagnostic proteomic data but did not outperform optimised
  conventional machine-learning methods within development cross-validation. The temporal
  and participant-independent performance estimates warrant further investigation
  in larger fully independent cohorts. A graph-specific predictive advantage was not
  directly tested—no such advantage was demonstrated in this dataset—and the clinical
  utility has not been established.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221178425
url: https://doi.org/10.3390/diagnostics16203283
discovered_at: '2026-10-16'
tags: *id001
---

# Graph Neural Network Modelling of Pre\-Diagnostic Serum Proteomics for Pancreatic Cancer Detection

**Autores:** Alexey A\. Zaikin; Aleksandra Gentry‐Maharaj; Sophia Apostolidou; Usha Menon; Arseniy Trukhanov; J\.G\. Oganezova; Harry J\. Whitwell; Oleg B\. Blyuss

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

Background/Objectives: Pancreatic ductal adenocarcinoma \(PDAC\) has exceptionally high mortality, largely because of late diagnosis, while established blood biomarkers such as CA19\-9 have limited sensitivity for early detection\. We evaluated whether modelling serum proteomic measurements as supervised pairwise statistical graphs using synolitic graph neural networks \(SGNNs\) could provide a useful framework for pre\-diagnostic PDAC classification\. Methods: We analysed 217 pre\-diagnostic serum samples from UKCTOCS, comprising 100 PDAC samples from 75 women and 117 control samples, profiled for 97 proteins\. Samples were divided into a development set collected 0–1 year before diagnosis \(n = 110\) and a temporal holdout set collected 1–2 years before diagnosis \(n = 107\); 25 PDAC participants contributed samples to both windows\. The final SGNN used fold\-internal mutual\-information selection of 30 proteins, pairwise RBF\-SVM\-derived edge information, minimum\-connected sparsification, and a 10\-member GATv2 ensemble per cross\-validation fold\. Conventional machine\-learning comparators were tuned using development data only\. Results: The SGNN achieved a mean 5\-fold development ROC\-AUC of 75\.33 ± 10\.43%, lower than the tuned Random Forest \(81\.67%\); the other tuned comparators achieved 77\.67% \(XGBoost\), 77\.17% \(logistic regression\), and 73\.17% \(SVM\)\. Averaging predictions across the five\-fold\-specific SGNN ensembles yielded a temporal\-holdout ROC\-AUC of 64\.35% \(95% CI 52\.6–74\.6%\)\. In the participant\-independent subset of 25 PDAC cases not represented in development and 57 controls, ROC\-AUC was 66\.04% \(95% CI 52\.56–78\.88%\)\. Conclusions: SGNNs provide a feasible graph\-based representation of pre\-diagnostic proteomic data but did not outperform optimised conventional machine\-learning methods within development cross\-validation\. The temporal and participant\-independent performance estimates warrant further investigation in larger fully independent cohorts\. A graph\-specific predictive advantage was not directly tested—no such advantage was demonstrated in this dataset—and the clinical utility has not been established\.

[Consultar publicação](<https://doi.org/10.3390/diagnostics16203283>)
