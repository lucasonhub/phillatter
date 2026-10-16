---
title: Optimal Explicit and Implicit Regularization Strengths in High-Dimensional
  Continual Linear Regression
authors:
- Gilad Karpel
- Daniel Soudry
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: We study continual linear regression in a high-dimensional regime, where
  a learner observes a sequence of tasks and updates its parameters sequentially.
  In this setting, we derive an explicit closed-form expression for the generalization
  loss of a model trained with gradient descent for a fixed number of steps per task,
  which holds for arbitrary teachers. We prove that the optimal fixed step size decays
  nearly inversely with the number of tasks, specifically as $\ln T / T$, for a single
  teacher and, more generally, i.i.d. teachers. Under this scaling, we show that the
  resulting generalization loss is asymptotically equivalent to that achieved by optimally
  tuned L2 (isotropic) regularization. Furthermore, we extend our analysis to generalized
  ridge regression with diagonal regularization matrices, obtaining a closed-form
  characterization of the generalization loss and identifying necessary and sufficient
  conditions under which the optimal regularizer is isotropic. Finally, we identify
  a regime where the optimal step size remains finite even as the number of tasks
  tends to infinity, thus revealing a non-trivial tradeoff between task variability
  and implicit regularization, in contrast to the i.i.d. teacher scaling. Our theoretical
  predictions are corroborated by experiments on both linear models and neural networks,
  providing practical guidance for the design of continual learning systems.
source:
- arXiv
source_ids:
- arxiv:2610.20804
url: https://arxiv.org/abs/2610.20804
discovered_at: '2026-10-16'
tags: *id001
---

# Optimal Explicit and Implicit Regularization Strengths in High\-Dimensional Continual Linear Regression

**Autores:** Gilad Karpel; Daniel Soudry

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

We study continual linear regression in a high\-dimensional regime, where a learner observes a sequence of tasks and updates its parameters sequentially\. In this setting, we derive an explicit closed\-form expression for the generalization loss of a model trained with gradient descent for a fixed number of steps per task, which holds for arbitrary teachers\. We prove that the optimal fixed step size decays nearly inversely with the number of tasks, specifically as $\\ln T / T$, for a single teacher and, more generally, i\.i\.d\. teachers\. Under this scaling, we show that the resulting generalization loss is asymptotically equivalent to that achieved by optimally tuned L2 \(isotropic\) regularization\. Furthermore, we extend our analysis to generalized ridge regression with diagonal regularization matrices, obtaining a closed\-form characterization of the generalization loss and identifying necessary and sufficient conditions under which the optimal regularizer is isotropic\. Finally, we identify a regime where the optimal step size remains finite even as the number of tasks tends to infinity, thus revealing a non\-trivial tradeoff between task variability and implicit regularization, in contrast to the i\.i\.d\. teacher scaling\. Our theoretical predictions are corroborated by experiments on both linear models and neural networks, providing practical guidance for the design of continual learning systems\.

[Consultar publicação](<https://arxiv.org/abs/2610.20804>)
