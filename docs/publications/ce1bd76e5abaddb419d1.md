---
title: 'Weighted Adjoint Matching: Finetuning Flow Matching Models with Time-Dependent
  Control Cost'
authors:
- Eliot Beyler
- Francis Bach
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: We introduce Weighted Adjoint Matching, a method to finetune a pretrained
  diffusion or flow matching model given a differentiable reward. We derive it from
  Adjoint Matching, which reformulates finetuning as a stochastic optimal control
  problem with a quadratic control cost. Building on the observation that these models
  generate coarse features before fine details, we place a time-dependent weight on
  the control cost. A high cost early in the generative process preserves balance
  and diversity in the coarse features, which carry most of the semantics, while a
  low cost at the end lets the model increase the reward by refining details. We prove
  that our method is equivalent to maximizing the reward under time-varying Kullback--Leibler
  regularization on the generative paths. Experiments on Gaussian mixtures and on
  MNIST show a better tradeoff between reward and mode balance than Adjoint Matching.
source:
- arXiv
source_ids:
- arxiv:2610.20035
url: https://arxiv.org/abs/2610.20035
discovered_at: '2026-10-16'
tags: *id001
---

# Weighted Adjoint Matching: Finetuning Flow Matching Models with Time\-Dependent Control Cost

**Autores:** Eliot Beyler; Francis Bach

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

We introduce Weighted Adjoint Matching, a method to finetune a pretrained diffusion or flow matching model given a differentiable reward\. We derive it from Adjoint Matching, which reformulates finetuning as a stochastic optimal control problem with a quadratic control cost\. Building on the observation that these models generate coarse features before fine details, we place a time\-dependent weight on the control cost\. A high cost early in the generative process preserves balance and diversity in the coarse features, which carry most of the semantics, while a low cost at the end lets the model increase the reward by refining details\. We prove that our method is equivalent to maximizing the reward under time\-varying Kullback\-\-Leibler regularization on the generative paths\. Experiments on Gaussian mixtures and on MNIST show a better tradeoff between reward and mode balance than Adjoint Matching\.

[Consultar publicação](<https://arxiv.org/abs/2610.20035>)
