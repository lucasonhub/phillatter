---
title: Monthly Runoff Simulation and Driving Mechanism Analysis of the Chushandian
  Reservoir Irrigation District Based on the Phased Adaptive Attention Informer Model
authors:
- Yunlong Ran
- Hongyu Yang
- Qingqing Tian
- Yu Tian
- Lei Guo
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3390/su182010241
abstract: Accurate monthly runoff simulation is the foundation of watershed water
  resources management and flood–drought disaster prevention. To address the issues
  that traditional machine learning models struggle to capture long-term dependencies
  in runoff series and that existing deep learning methods ignore the differences
  in driving mechanisms across intra-annual hydrological periods, this paper proposes
  a Period-Adaptive Attention Informer (PA-Informer), in which a learnable period
  embedding is introduced into the attention mechanism to achieve adaptive representation
  of the memory length of each period. Based on autocorrelation analysis, K-means
  clustering and dynamic time warping, the hydrological year is divided into a dry
  period (November–February), a transition period (March–June and October) and a wet
  period (July–September). Using monthly precipitation, monthly mean temperature and
  antecedent runoff (lags 1–3) observed at the Changtaiguan Hydrological Station in
  the Chushandian Irrigation Area of the upper Huaihe River (1960–2020), a one-month-ahead
  monthly runoff simulation is performed with the meteorological variables of the
  target month taken as known; the record is split chronologically into a training
  set (1960–2002) and a test set (2003–2020) at a ratio of 7:3, and all preprocessing
  and tuning procedures are restricted to the training set. On the test set, PA-Informer
  achieves an R2 = 0.957, NSE = 0.948, RMSE = 0.71 m3/s and MAE = 0.52 m3/s (mean
  over five random seeds), outperforming the best benchmark (Base-Informer) with a
  statistically significant difference (Wilcoxon signed-rank test, p = 0.0023). SHAP
  analysis reveals that dry-period runoff is driven mainly by temperature and antecedent
  runoff, transition-period runoff by precipitation and long-lag runoff, and wet-period
  runoff predominantly by precipitation with temperature acting as a suppressor. PA-Informer
  effectively integrates the physical laws of hydrological periodicity with a deep
  learning architecture, providing a new approach for high-accuracy monthly runoff
  simulation in irrigation areas.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221197824
url: https://doi.org/10.3390/su182010241
discovered_at: '2026-10-16'
tags: *id001
---

# Monthly Runoff Simulation and Driving Mechanism Analysis of the Chushandian Reservoir Irrigation District Based on the Phased Adaptive Attention Informer Model

**Autores:** Yunlong Ran; Hongyu Yang; Qingqing Tian; Yu Tian; Lei Guo

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

Accurate monthly runoff simulation is the foundation of watershed water resources management and flood–drought disaster prevention\. To address the issues that traditional machine learning models struggle to capture long\-term dependencies in runoff series and that existing deep learning methods ignore the differences in driving mechanisms across intra\-annual hydrological periods, this paper proposes a Period\-Adaptive Attention Informer \(PA\-Informer\), in which a learnable period embedding is introduced into the attention mechanism to achieve adaptive representation of the memory length of each period\. Based on autocorrelation analysis, K\-means clustering and dynamic time warping, the hydrological year is divided into a dry period \(November–February\), a transition period \(March–June and October\) and a wet period \(July–September\)\. Using monthly precipitation, monthly mean temperature and antecedent runoff \(lags 1–3\) observed at the Changtaiguan Hydrological Station in the Chushandian Irrigation Area of the upper Huaihe River \(1960–2020\), a one\-month\-ahead monthly runoff simulation is performed with the meteorological variables of the target month taken as known; the record is split chronologically into a training set \(1960–2002\) and a test set \(2003–2020\) at a ratio of 7:3, and all preprocessing and tuning procedures are restricted to the training set\. On the test set, PA\-Informer achieves an R2 = 0\.957, NSE = 0\.948, RMSE = 0\.71 m3/s and MAE = 0\.52 m3/s \(mean over five random seeds\), outperforming the best benchmark \(Base\-Informer\) with a statistically significant difference \(Wilcoxon signed\-rank test, p = 0\.0023\)\. SHAP analysis reveals that dry\-period runoff is driven mainly by temperature and antecedent runoff, transition\-period runoff by precipitation and long\-lag runoff, and wet\-period runoff predominantly by precipitation with temperature acting as a suppressor\. PA\-Informer effectively integrates the physical laws of hydrological periodicity with a deep learning architecture, providing a new approach for high\-accuracy monthly runoff simulation in irrigation areas\.

[Consultar publicação](<https://doi.org/10.3390/su182010241>)
