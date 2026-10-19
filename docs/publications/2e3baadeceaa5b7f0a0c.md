---
title: Generative Value Classifier
authors:
- Alexander Swerdlow
- Perry Dong
- Chelsea Finn
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Q-learning is premised on learning a function to predict the value of a
  state-action pair, with the goal of using such a function to guide policy improvement.
  Most approaches learn this function from scratch using scalar or distributional
  return targets. This discriminative approach leaves another source of supervision
  for learning representations unused: the actions themselves. Rather than directly
  predict the return of a state-action pair, we ask the reverse question: how likely
  is the action under each possible return? This perspective provides a critic whose
  generative component is a return-conditioned policy, which can share the actor''s
  architecture. Training this policy supervises the critic with every action rather
  than with returns alone, and a squared-error loss anchors the critic''s Q-value
  to the bootstrapped target. We evaluate our approach on both offline and online
  RL tasks and show gains over leading discriminative methods, including distributional
  RL methods.'
source:
- arXiv
source_ids:
- arxiv:2610.22497
url: https://arxiv.org/abs/2610.22497
discovered_at: '2026-10-19'
tags: *id001
---

# Generative Value Classifier

**Autores:** Alexander Swerdlow; Perry Dong; Chelsea Finn

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Q\-learning is premised on learning a function to predict the value of a state\-action pair, with the goal of using such a function to guide policy improvement\. Most approaches learn this function from scratch using scalar or distributional return targets\. This discriminative approach leaves another source of supervision for learning representations unused: the actions themselves\. Rather than directly predict the return of a state\-action pair, we ask the reverse question: how likely is the action under each possible return? This perspective provides a critic whose generative component is a return\-conditioned policy, which can share the actor&\#x27;s architecture\. Training this policy supervises the critic with every action rather than with returns alone, and a squared\-error loss anchors the critic&\#x27;s Q\-value to the bootstrapped target\. We evaluate our approach on both offline and online RL tasks and show gains over leading discriminative methods, including distributional RL methods\.

[Consultar publicação](<https://arxiv.org/abs/2610.22497>)
