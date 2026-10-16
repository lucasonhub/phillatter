---
title: Transformer-based In-Context Score Operator Learning for Diffusion Models
authors:
- Wuzhe Xu
- Zhaiming Shen
- Yulong Lu
- Wenjing Liao
- Rongjie Lai
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Diffusion models typically learn the generative dynamics of a single target
  distribution or a family of distributions indexed by conditioning variables fixed
  during training. This limits their ability to adapt to a previously unseen distribution
  from only a small set of examples. We introduce an in-context solution operator
  learning framework for diffusion models, in which each target distribution is treated
  as a task drawn from a meta-distribution and is specified at inference time by an
  empirical context set. Our method learns an in-context score operator that maps
  the context samples, a noisy query point, and the diffusion time to the task-dependent
  score, enabling reverse-diffusion sampling on unseen tasks without retraining or
  parameter updates. A key observation is that the task-dependent score admits a Gaussian-kernel
  conditional-mean representation. Its empirical Nadaraya--Watson approximation can
  be represented exactly by a model in our constructed transformer class, providing
  a principled foundation for the proposed query-dependent attention architecture.
  The operator is trained through amortized denoising score matching across task distributions.
  We establish generalization-error bounds that quantify the effects of the context
  size, the numbers of training tasks and within-task samples, model complexity, and
  intrinsic and ambient dimensions. Numerically, we evaluate the method on a range
  of scientific and visual datasets, including Navier-Stokes, ERA5 climate data, QuickDraw
  sketches, and Food-101. The results show that the proposed method performs well
  on relatively simple task families, while its performance degrades as task complexity
  increases, thereby illustrating both the promise and the limitations of in-context
  learning for diffusion models.
source:
- arXiv
source_ids:
- arxiv:2610.13690
url: https://arxiv.org/abs/2610.13690
discovered_at: '2026-10-16'
tags: *id001
---

# Transformer\-based In\-Context Score Operator Learning for Diffusion Models

**Autores:** Wuzhe Xu; Zhaiming Shen; Yulong Lu; Wenjing Liao; Rongjie Lai

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Diffusion models typically learn the generative dynamics of a single target distribution or a family of distributions indexed by conditioning variables fixed during training\. This limits their ability to adapt to a previously unseen distribution from only a small set of examples\. We introduce an in\-context solution operator learning framework for diffusion models, in which each target distribution is treated as a task drawn from a meta\-distribution and is specified at inference time by an empirical context set\. Our method learns an in\-context score operator that maps the context samples, a noisy query point, and the diffusion time to the task\-dependent score, enabling reverse\-diffusion sampling on unseen tasks without retraining or parameter updates\. A key observation is that the task\-dependent score admits a Gaussian\-kernel conditional\-mean representation\. Its empirical Nadaraya\-\-Watson approximation can be represented exactly by a model in our constructed transformer class, providing a principled foundation for the proposed query\-dependent attention architecture\. The operator is trained through amortized denoising score matching across task distributions\. We establish generalization\-error bounds that quantify the effects of the context size, the numbers of training tasks and within\-task samples, model complexity, and intrinsic and ambient dimensions\. Numerically, we evaluate the method on a range of scientific and visual datasets, including Navier\-Stokes, ERA5 climate data, QuickDraw sketches, and Food\-101\. The results show that the proposed method performs well on relatively simple task families, while its performance degrades as task complexity increases, thereby illustrating both the promise and the limitations of in\-context learning for diffusion models\.

[Consultar publicação](<https://arxiv.org/abs/2610.13690>)
