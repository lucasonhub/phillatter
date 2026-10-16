---
title: 'VaryST: Generalizable Spatio-Temporal Forecasting Beyond the Closed-World
  Setting'
authors:
- Shengnan Guo
- Jinjun Cheng
- Xiaowei Mao
- Jianhao Zhang
- Haochen Lv
- Yang Jiang
- YiHeng Huang
- Yan Lin
- Youfang Lin
- Huaiyu Wan
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Spatio-temporal forecasting is fundamental to many real-world systems,
  yet deployment environments are inherently varying: temporal distributions may evolve,
  spatial domains may change, and observation availability may shift from training
  conditions. Existing models are often tightly coupled to their training environments
  through node-specific representations, predefined spatial support sets, and reliance
  on consistently available observations, limiting generalization to changing environments.
  To this end, we propose VaryST, a compact spatio-temporal forecasting model trained
  from scratch that achieves strong generalization by dynamically constructing predictive
  context from available long-term observations. To accommodate temporal changes,
  VaryST derives node representations from long-term histories, capturing current
  behavior in the context of longer-term patterns. To adapt to spatial changes, it
  dynamically selects functionally relevant support nodes beyond predefined neighborhoods
  and integrates their information with recent and long-term target states and global
  context. To handle varying observation availability, VaryST selectively masks historical
  patches on which the model relies most during training, encouraging it to exploit
  alternative temporal and spatial dependencies for accurate forecasting when key
  observations become unavailable. Extensive experiments on six real-world datasets
  against seventeen baselines show that VaryST achieves strong in-domain forecasting
  accuracy, substantially improves zero- and few-shot generalization under spatial
  and temporal changes, and remains robust to varying observation availability.'
source:
- arXiv
source_ids:
- arxiv:2610.19813
url: https://arxiv.org/abs/2610.19813
discovered_at: '2026-10-16'
tags: *id001
---

# VaryST: Generalizable Spatio\-Temporal Forecasting Beyond the Closed\-World Setting

**Autores:** Shengnan Guo; Jinjun Cheng; Xiaowei Mao; Jianhao Zhang; Haochen Lv; Yang Jiang; YiHeng Huang; Yan Lin; Youfang Lin; Huaiyu Wan

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Spatio\-temporal forecasting is fundamental to many real\-world systems, yet deployment environments are inherently varying: temporal distributions may evolve, spatial domains may change, and observation availability may shift from training conditions\. Existing models are often tightly coupled to their training environments through node\-specific representations, predefined spatial support sets, and reliance on consistently available observations, limiting generalization to changing environments\. To this end, we propose VaryST, a compact spatio\-temporal forecasting model trained from scratch that achieves strong generalization by dynamically constructing predictive context from available long\-term observations\. To accommodate temporal changes, VaryST derives node representations from long\-term histories, capturing current behavior in the context of longer\-term patterns\. To adapt to spatial changes, it dynamically selects functionally relevant support nodes beyond predefined neighborhoods and integrates their information with recent and long\-term target states and global context\. To handle varying observation availability, VaryST selectively masks historical patches on which the model relies most during training, encouraging it to exploit alternative temporal and spatial dependencies for accurate forecasting when key observations become unavailable\. Extensive experiments on six real\-world datasets against seventeen baselines show that VaryST achieves strong in\-domain forecasting accuracy, substantially improves zero\- and few\-shot generalization under spatial and temporal changes, and remains robust to varying observation availability\.

[Consultar publicação](<https://arxiv.org/abs/2610.19813>)
