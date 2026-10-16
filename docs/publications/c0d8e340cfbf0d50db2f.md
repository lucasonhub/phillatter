---
title: 'SelectTTRL: Representation-Guided Data Selection for Efficient Test-Time Reinforcement
  Learning'
authors:
- Yi Li
- Linan Yue
- Weibo Gao
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Test-Time Reinforcement Learning (TTRL) enables large language models to
  adapt directly on unlabeled test problems by constructing pseudo-labels from multiple
  sampled responses. However, existing TTRL methods typically apply the same expensive
  sampling and optimization procedure to all test problems, despite substantial differences
  in their training utility. In this paper, we study whether such problems can be
  identified before costly test-time training, without access to ground-truth answers.
  We uncover a stable relationship between internal response representations and problem-level
  empirical accuracy. Specifically, we define COS as the cosine similarity between
  a model's response representation and a correctness-related direction constructed
  from an independent question-answering dataset. COS consistently correlates with
  problem solvability across different models, datasets, and experimental settings,
  and we further provide a theoretical analysis explaining this relationship. Building
  on this finding, we propose SelectTTRL, a representation-guided data selection method
  that ranks test problems using COS and applies TTRL only to a selected percentile
  interval. SelectTTRL leaves the standard TTRL pipeline unchanged for the selected
  problems, while avoiding unnecessary multi-response sampling and reinforcement learning
  updates on the remaining ones. Experiments across multiple reasoning benchmarks
  demonstrate that SelectTTRL substantially reduces test-time computation while maintaining
  or improving the performance of standard TTRL. Code is available at https://github.com/heyiliyi/SelectTTRL-public.
source:
- arXiv
source_ids:
- arxiv:2610.16104
url: https://arxiv.org/abs/2610.16104
discovered_at: '2026-10-16'
tags: *id001
---

# SelectTTRL: Representation\-Guided Data Selection for Efficient Test\-Time Reinforcement Learning

**Autores:** Yi Li; Linan Yue; Weibo Gao

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Test\-Time Reinforcement Learning \(TTRL\) enables large language models to adapt directly on unlabeled test problems by constructing pseudo\-labels from multiple sampled responses\. However, existing TTRL methods typically apply the same expensive sampling and optimization procedure to all test problems, despite substantial differences in their training utility\. In this paper, we study whether such problems can be identified before costly test\-time training, without access to ground\-truth answers\. We uncover a stable relationship between internal response representations and problem\-level empirical accuracy\. Specifically, we define COS as the cosine similarity between a model&\#x27;s response representation and a correctness\-related direction constructed from an independent question\-answering dataset\. COS consistently correlates with problem solvability across different models, datasets, and experimental settings, and we further provide a theoretical analysis explaining this relationship\. Building on this finding, we propose SelectTTRL, a representation\-guided data selection method that ranks test problems using COS and applies TTRL only to a selected percentile interval\. SelectTTRL leaves the standard TTRL pipeline unchanged for the selected problems, while avoiding unnecessary multi\-response sampling and reinforcement learning updates on the remaining ones\. Experiments across multiple reasoning benchmarks demonstrate that SelectTTRL substantially reduces test\-time computation while maintaining or improving the performance of standard TTRL\. Code is available at https://github\.com/heyiliyi/SelectTTRL\-public\.

[Consultar publicação](<https://arxiv.org/abs/2610.16104>)
