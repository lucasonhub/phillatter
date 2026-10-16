---
title: Theoretical and Practical Advances in Hierarchical Bayesian Deep Learning Methodology
authors:
- Neil K. Chada
- Simon Cotter
- Kody J. H. Law
- Xinzhu Liang
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Reliable uncertainty quantification remains an important challenge in AI.
  Hierarchical Bayesian methods provide a principled framework for this by representing
  unknown quantities through posterior distributions. Joint inference of neural-network
  parameters and prior hyperparameters is challenging for conventional Markov chain
  Monte Carlo (MCMC) methods due to strong dependencies. In this work, we introduce
  the multilevel particle marginal Metropolis-Hastings (MLPMMH) method, which combines
  pseudo-marginal inference for the hyperparameters with coupled sequential Monte
  Carlo (SMC) across hierarchy of network-width truncations for conditional parameter
  inference. The hierarchy is induced by a trace-class neural network (TNN) prior
  with width-dependent decay, motivated empirically by the compressible structure
  observed in trained neural-network parameters. Under standard multilevel coupling
  assumptions, we establish that MLPMMH achieves mean-square error (MSE) $\mathcal{O}(\varepsilon^2)$
  at expected computational cost $\mathcal{O}(\varepsilon^{-2})$, and verify the predicted
  rate on a Bayesian regression problem. To address larger-scale applications, we
  further introduce S-MLPMMH, a practical approximation that replaces the exact sampling
  components with a PCA-based hierarchy and scalable Bayesian Monte Carlo. Experiments
  on MNIST demonstrate competitive predictive performance and uncertainty quantification
  while exploiting the parallel structure of the approximation. Software has been
  made publicly available at https://github.com/submission-code-anon/mlpmmh-anon.
source:
- arXiv
source_ids:
- arxiv:2610.19074
url: https://arxiv.org/abs/2610.19074
discovered_at: '2026-10-16'
tags: *id001
---

# Theoretical and Practical Advances in Hierarchical Bayesian Deep Learning Methodology

**Autores:** Neil K\. Chada; Simon Cotter; Kody J\. H\. Law; Xinzhu Liang

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Reliable uncertainty quantification remains an important challenge in AI\. Hierarchical Bayesian methods provide a principled framework for this by representing unknown quantities through posterior distributions\. Joint inference of neural\-network parameters and prior hyperparameters is challenging for conventional Markov chain Monte Carlo \(MCMC\) methods due to strong dependencies\. In this work, we introduce the multilevel particle marginal Metropolis\-Hastings \(MLPMMH\) method, which combines pseudo\-marginal inference for the hyperparameters with coupled sequential Monte Carlo \(SMC\) across hierarchy of network\-width truncations for conditional parameter inference\. The hierarchy is induced by a trace\-class neural network \(TNN\) prior with width\-dependent decay, motivated empirically by the compressible structure observed in trained neural\-network parameters\. Under standard multilevel coupling assumptions, we establish that MLPMMH achieves mean\-square error \(MSE\) $\\mathcal\{O\}\(\\varepsilon^2\)$ at expected computational cost $\\mathcal\{O\}\(\\varepsilon^\{\-2\}\)$, and verify the predicted rate on a Bayesian regression problem\. To address larger\-scale applications, we further introduce S\-MLPMMH, a practical approximation that replaces the exact sampling components with a PCA\-based hierarchy and scalable Bayesian Monte Carlo\. Experiments on MNIST demonstrate competitive predictive performance and uncertainty quantification while exploiting the parallel structure of the approximation\. Software has been made publicly available at https://github\.com/submission\-code\-anon/mlpmmh\-anon\.

[Consultar publicação](<https://arxiv.org/abs/2610.19074>)
