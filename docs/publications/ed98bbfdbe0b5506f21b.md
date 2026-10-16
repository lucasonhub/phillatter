---
title: Noise-Space Reward Alignment for Few-Step Generative Models
authors:
- Woocheol Shin
- Taeyoung Yun
- Jiwon Sung
- Hyeongyu Kang
- Jeongmin Park
- Jaewoo Lee
- Kyuil Sim
- Dohyun Kim
- Yutong He
- Jinkyoo Park
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Few-step generative models produce high-quality samples in one or a few
  evaluations. However, steering them toward desired properties remains difficult,
  especially when only black-box reward evaluations are available. While one could
  apply approaches developed for iterative diffusion and flow-based models, such as
  direct RL fine-tuning or test-time scaling, we find that neither transfers well
  to the few-step regime: direct fine-tuning suffers from severe reward over-optimization,
  and test-time scaling sacrifices the efficiency advantage of few-step generation.
  We propose Noise Policy Optimization (NPO), which explicitly targets the alignment
  problem for few-step generative models. The key idea is to learn an amortized flow
  policy over the initial noise space of the generator. The trained policy transports
  Gaussian noise to a reward-tilted noise distribution, whose pushforward distribution
  through the frozen generator is exactly the reward-tilted output distribution. By
  keeping the generator frozen, we can effectively utilize the knowledge encoded in
  the pretrained model, yielding a better reward-quality trade-off than direct fine-tuning.
  The amortized policy moves the search cost into training, so inference adds only
  a lightweight noise sampling step on top of the pretrained model. To improve sample
  efficiency during training, we use ELBO-based likelihood estimation that requires
  only sampled endpoints rather than simulated trajectories. Across image, language,
  and protein structure generation, NPO consistently achieves a better reward-quality
  trade-off than direct fine-tuning, and matches test-time search methods with 16
  to 549 times lower inference cost.'
source:
- arXiv
source_ids:
- arxiv:2610.21125
url: https://arxiv.org/abs/2610.21125
discovered_at: '2026-10-16'
tags: *id001
---

# Noise\-Space Reward Alignment for Few\-Step Generative Models

**Autores:** Woocheol Shin; Taeyoung Yun; Jiwon Sung; Hyeongyu Kang; Jeongmin Park; Jaewoo Lee; Kyuil Sim; Dohyun Kim; Yutong He; Jinkyoo Park

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Few\-step generative models produce high\-quality samples in one or a few evaluations\. However, steering them toward desired properties remains difficult, especially when only black\-box reward evaluations are available\. While one could apply approaches developed for iterative diffusion and flow\-based models, such as direct RL fine\-tuning or test\-time scaling, we find that neither transfers well to the few\-step regime: direct fine\-tuning suffers from severe reward over\-optimization, and test\-time scaling sacrifices the efficiency advantage of few\-step generation\. We propose Noise Policy Optimization \(NPO\), which explicitly targets the alignment problem for few\-step generative models\. The key idea is to learn an amortized flow policy over the initial noise space of the generator\. The trained policy transports Gaussian noise to a reward\-tilted noise distribution, whose pushforward distribution through the frozen generator is exactly the reward\-tilted output distribution\. By keeping the generator frozen, we can effectively utilize the knowledge encoded in the pretrained model, yielding a better reward\-quality trade\-off than direct fine\-tuning\. The amortized policy moves the search cost into training, so inference adds only a lightweight noise sampling step on top of the pretrained model\. To improve sample efficiency during training, we use ELBO\-based likelihood estimation that requires only sampled endpoints rather than simulated trajectories\. Across image, language, and protein structure generation, NPO consistently achieves a better reward\-quality trade\-off than direct fine\-tuning, and matches test\-time search methods with 16 to 549 times lower inference cost\.

[Consultar publicação](<https://arxiv.org/abs/2610.21125>)
