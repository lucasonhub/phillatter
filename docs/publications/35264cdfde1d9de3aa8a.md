---
title: Normalizing Flow Maps
authors:
- Francesco M. Ruscio
- Timothy James Hitge
- Fred Zhangzhi Peng
- Danyal Rehman
- Zander W. Blasingame
- Nicholas M. Boffi
- Michael M. Bronstein
- Alexander Tong
- Avishek Joey Bose
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Scalable approaches to learning neural dynamical systems have placed diffusion,
  flow matching, and few-step generators in flow maps at the forefront of generative
  modeling. Such state-of-the-art models have limited access to explicit model densities
  despite evolving from classical generative modeling approaches that leveraged tractable
  likelihoods, e.g., Normalizing Flows and Autoregressive models. In this paper, we
  combine these threads of few-step generation and tractable sample likelihoods and
  introduce Normalizing Flow Maps (NFM), a class of exactly invertible pushforward
  maps that generalizes normalizing flows and flow maps. More precisely, NFMs learn
  the integrator of an underlying dynamical system, but crucially, they provide efficient
  exact likelihood evaluation by construction. To enable scalable training of NFMs,
  we derive two complementary axes of consistency inherent to NFMs that yield (self)
  distillation objectives: (1) pointwise matching, which unlocks $\ell_2$-based flow-map
  style regression losses, and (2) distributional matching, which matches pushforward
  distributions to the marginals of a prescribed forward process. On conditional image
  generation on CIFAR-10 and ImageNet-64, NFMs achieve state-of-the-art sample quality
  among parameter-matched normalizing flows, while supporting likelihood-based RLHF.
  For equilibrium sampling in Boltzmann Generators, NFMs outperform prior state-of-the-art
  normalizing flows on both single-system and transferable peptide benchmarks.'
source:
- arXiv
source_ids:
- arxiv:2610.22711
url: https://arxiv.org/abs/2610.22711
discovered_at: '2026-10-19'
tags: *id001
---

# Normalizing Flow Maps

**Autores:** Francesco M\. Ruscio; Timothy James Hitge; Fred Zhangzhi Peng; Danyal Rehman; Zander W\. Blasingame; Nicholas M\. Boffi; Michael M\. Bronstein; Alexander Tong; Avishek Joey Bose

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Scalable approaches to learning neural dynamical systems have placed diffusion, flow matching, and few\-step generators in flow maps at the forefront of generative modeling\. Such state\-of\-the\-art models have limited access to explicit model densities despite evolving from classical generative modeling approaches that leveraged tractable likelihoods, e\.g\., Normalizing Flows and Autoregressive models\. In this paper, we combine these threads of few\-step generation and tractable sample likelihoods and introduce Normalizing Flow Maps \(NFM\), a class of exactly invertible pushforward maps that generalizes normalizing flows and flow maps\. More precisely, NFMs learn the integrator of an underlying dynamical system, but crucially, they provide efficient exact likelihood evaluation by construction\. To enable scalable training of NFMs, we derive two complementary axes of consistency inherent to NFMs that yield \(self\) distillation objectives: \(1\) pointwise matching, which unlocks $\\ell\_2$\-based flow\-map style regression losses, and \(2\) distributional matching, which matches pushforward distributions to the marginals of a prescribed forward process\. On conditional image generation on CIFAR\-10 and ImageNet\-64, NFMs achieve state\-of\-the\-art sample quality among parameter\-matched normalizing flows, while supporting likelihood\-based RLHF\. For equilibrium sampling in Boltzmann Generators, NFMs outperform prior state\-of\-the\-art normalizing flows on both single\-system and transferable peptide benchmarks\.

[Consultar publicação](<https://arxiv.org/abs/2610.22711>)
