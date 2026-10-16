---
title: Simplifying and Improving On-Policy Distillation for Few-Step Diffusion
authors:
- Jiawei Zhang
- Ziyu Wan
- Nanye Ma
- Long Zhao
- Dong Chen
- Hongyu Liu
- Qifeng Chen
- Dongdong Chen
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Few-step distillation reduces the sampling cost of diffusion and flow models,
  but existing approaches often require auxiliary score models or specialized architectures.
  We show that simple on-policy velocity regression already provides a strong foundation
  for 4-NFE generation. To represent teacher velocity variation within each coarse
  transition, we introduce Pivot, a training-only residual proxy that separates local
  corrections from the student's interval-mean prediction. We further repel the student
  from weaker teacher predictions, providing a lightweight mechanism for avoiding
  undesirable modes. The resulting framework, Simplified Matching Distillation (SMD),
  remains entirely regression-based, requires neither online score estimation nor
  adversarial training, and leaves the deployed generator unchanged. We evaluate SMD
  on image generation and editing, 3D generation, video synthesis, and joint audio--video
  generation, scaling to 33 billion parameters. At 4-NFE, SMD outperforms strong few-step
  baselines and surpasses multi-step teachers on several benchmarks. It also supports
  cross-model, multi-teacher, and causal-video distillation.
source:
- arXiv
source_ids:
- arxiv:2610.18472
url: https://arxiv.org/abs/2610.18472
discovered_at: '2026-10-16'
tags: *id001
---

# Simplifying and Improving On\-Policy Distillation for Few\-Step Diffusion

**Autores:** Jiawei Zhang; Ziyu Wan; Nanye Ma; Long Zhao; Dong Chen; Hongyu Liu; Qifeng Chen; Dongdong Chen

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Few\-step distillation reduces the sampling cost of diffusion and flow models, but existing approaches often require auxiliary score models or specialized architectures\. We show that simple on\-policy velocity regression already provides a strong foundation for 4\-NFE generation\. To represent teacher velocity variation within each coarse transition, we introduce Pivot, a training\-only residual proxy that separates local corrections from the student&\#x27;s interval\-mean prediction\. We further repel the student from weaker teacher predictions, providing a lightweight mechanism for avoiding undesirable modes\. The resulting framework, Simplified Matching Distillation \(SMD\), remains entirely regression\-based, requires neither online score estimation nor adversarial training, and leaves the deployed generator unchanged\. We evaluate SMD on image generation and editing, 3D generation, video synthesis, and joint audio\-\-video generation, scaling to 33 billion parameters\. At 4\-NFE, SMD outperforms strong few\-step baselines and surpasses multi\-step teachers on several benchmarks\. It also supports cross\-model, multi\-teacher, and causal\-video distillation\.

[Consultar publicação](<https://arxiv.org/abs/2610.18472>)
