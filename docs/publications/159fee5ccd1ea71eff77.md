---
title: 'From Policy Evaluation to Off-Policy Control: Provable Emergence of In-Context
  Q-Learning'
authors:
- Yingjun Mo
- Yajie Zhao
- Fang Kong
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Transformers can implement reinforcement-learning algorithms in context,
  yet how off-policy control emerges within Transformers remains poorly understood.
  We study Q-learning, a foundational model-free control algorithm that combines off-policy
  bootstrapping with greedy policy improvement. We prove that a two-layer attention-only
  Transformer can implement a finite-temperature form of Q-learning, where the temperature
  $τ>0$ controls the approximation to greedy action selection, recovering window Q-learning
  as $τ\to0$. We train the structured Transformer on randomly generated MDP tasks
  using output-only supervision. Experiments show that the theoretically predicted
  parameter structure emerges during training, including the internal greedy action-selection
  mechanism, and that the trained Transformer achieves performance comparable to Q-learning
  on unseen tasks. Our theoretical analysis further shows that the equivalent realizations
  form a solution manifold and that, under suitable task-diversity conditions, the
  training iterates converge locally to this manifold at an exponential rate. For
  the random-task model analyzed here, the local worst-case number of gradient steps
  needed to reduce the distance to the manifold by a factor $ε$ is $Θ\left(τ^{-5}\log(1/\varepsilon)\right)$,
  quantifying the increasing optimization cost as the learned update approaches window
  Q-learning.
source:
- arXiv
source_ids:
- arxiv:2610.18057
url: https://arxiv.org/abs/2610.18057
discovered_at: '2026-10-16'
tags: *id001
---

# From Policy Evaluation to Off\-Policy Control: Provable Emergence of In\-Context Q\-Learning

**Autores:** Yingjun Mo; Yajie Zhao; Fang Kong

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Transformers can implement reinforcement\-learning algorithms in context, yet how off\-policy control emerges within Transformers remains poorly understood\. We study Q\-learning, a foundational model\-free control algorithm that combines off\-policy bootstrapping with greedy policy improvement\. We prove that a two\-layer attention\-only Transformer can implement a finite\-temperature form of Q\-learning, where the temperature $τ&gt;0$ controls the approximation to greedy action selection, recovering window Q\-learning as $τ\\to0$\. We train the structured Transformer on randomly generated MDP tasks using output\-only supervision\. Experiments show that the theoretically predicted parameter structure emerges during training, including the internal greedy action\-selection mechanism, and that the trained Transformer achieves performance comparable to Q\-learning on unseen tasks\. Our theoretical analysis further shows that the equivalent realizations form a solution manifold and that, under suitable task\-diversity conditions, the training iterates converge locally to this manifold at an exponential rate\. For the random\-task model analyzed here, the local worst\-case number of gradient steps needed to reduce the distance to the manifold by a factor $ε$ is $Θ\\left\(τ^\{\-5\}\\log\(1/\\varepsilon\)\\right\)$, quantifying the increasing optimization cost as the learned update approaches window Q\-learning\.

[Consultar publicação](<https://arxiv.org/abs/2610.18057>)
