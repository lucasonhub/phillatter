---
title: 'COFFEQA: Counterfactual-Guided Few-Shot Distillation for LLM Question Answering'
authors:
- Kavinda Kehelella
- Sanghamitra Dutta
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Knowledge distillation aims to train a smaller student model to mimic a
  larger teacher model for resource-constrained environments. However, the process
  of distillation is typically data-intensive and computationally expensive, particularly
  for generative tasks. Few-shot distillation offers an alternative by transferring
  teacher knowledge using limited training samples. However, we observe that few-shot
  distillation performance is heavily dependent on the choice of these training samples.
  In fact, we demonstrate that using more uncertain samples near the teacher's decision
  boundary can significantly deteriorate distillation performance. Motivated by this
  observation, we propose Counterfactual-guided Few-shot Distillation in Open-book
  Question Answering (COFFEQA), a novel strategy that aptly uses counterfactuals to
  provide additional supervision around challenging factual samples. In the generative
  QA setting, we define a counterfactual as a minimally modified context that induces
  the teacher to change its response to an alternative answer. We provide geometric
  insights on how factual-counterfactual pairs can constrain the deviation between
  the teacher's and student's decision boundaries. We further introduce a new metric,
  Context Following Difficulty (CFD) that further validates counterfactuals prior
  to distillation based on agreement with the intended alternative answer and dependence
  on the modified context. COFFEQA uses CFD-validated factual-counterfactual pairs
  for few-shot distillation. Experiments across five in-domain and three out-of-domain
  QA benchmarks using T5 and Qwen2.5 families show that COFFEQA outperforms factual-only
  distillation baselines under the same few-shot budget. For instance, on TriviaQA,
  COFFEQA improves over the factual-only baseline by 8.77 average EM points and 9.98
  average F1 points under the T5 setting with 32 few-shot pairs.
source:
- arXiv
source_ids:
- arxiv:2610.12837
url: https://arxiv.org/abs/2610.12837
discovered_at: '2026-10-16'
tags: *id001
---

# COFFEQA: Counterfactual\-Guided Few\-Shot Distillation for LLM Question Answering

**Autores:** Kavinda Kehelella; Sanghamitra Dutta

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Knowledge distillation aims to train a smaller student model to mimic a larger teacher model for resource\-constrained environments\. However, the process of distillation is typically data\-intensive and computationally expensive, particularly for generative tasks\. Few\-shot distillation offers an alternative by transferring teacher knowledge using limited training samples\. However, we observe that few\-shot distillation performance is heavily dependent on the choice of these training samples\. In fact, we demonstrate that using more uncertain samples near the teacher&\#x27;s decision boundary can significantly deteriorate distillation performance\. Motivated by this observation, we propose Counterfactual\-guided Few\-shot Distillation in Open\-book Question Answering \(COFFEQA\), a novel strategy that aptly uses counterfactuals to provide additional supervision around challenging factual samples\. In the generative QA setting, we define a counterfactual as a minimally modified context that induces the teacher to change its response to an alternative answer\. We provide geometric insights on how factual\-counterfactual pairs can constrain the deviation between the teacher&\#x27;s and student&\#x27;s decision boundaries\. We further introduce a new metric, Context Following Difficulty \(CFD\) that further validates counterfactuals prior to distillation based on agreement with the intended alternative answer and dependence on the modified context\. COFFEQA uses CFD\-validated factual\-counterfactual pairs for few\-shot distillation\. Experiments across five in\-domain and three out\-of\-domain QA benchmarks using T5 and Qwen2\.5 families show that COFFEQA outperforms factual\-only distillation baselines under the same few\-shot budget\. For instance, on TriviaQA, COFFEQA improves over the factual\-only baseline by 8\.77 average EM points and 9\.98 average F1 points under the T5 setting with 32 few\-shot pairs\.

[Consultar publicação](<https://arxiv.org/abs/2610.12837>)
