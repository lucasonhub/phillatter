---
title: 'REWIND: Uncertainty-Guided Trajectory Repair for Test-Time Reasoning'
authors:
- Yi Ding
- Mengyu Wang
- Min Zhou
- Menglin Yang
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: An early mistake in the generated reasoning can constrain all subsequent
  reasoning. Repeated-generation methods, like MCMC-based approaches, attempt to improve
  output quality by sampling multiple generations, but their effectiveness can be
  limited by randomly selecting where to regenerate. On MATH500 with Qwen2.5-Math-7B,
  we find that incorrect responses have substantially higher mean token entropy than
  correct responses, with an average within-question relative increase of approximately
  112%, suggesting that entropy can signal reasoning errors. Motivated by this finding,
  we introduce REWIND, a training-free controller that uses entropy dynamics to propose
  targeted suffix regenerations. Across three model families and five benchmarks,
  REWIND outperforms all baselines, with gains of 0.51-10.00 percentage points over
  the strongest baseline. These results demonstrate the effectiveness of targeted,
  uncertainty-guided trajectory repair across models and tasks. Our code is available
  at https://anonymous.4open.science/r/rewind-D310.
source:
- arXiv
source_ids:
- arxiv:2610.19561
url: https://arxiv.org/abs/2610.19561
discovered_at: '2026-10-16'
tags: *id001
---

# REWIND: Uncertainty\-Guided Trajectory Repair for Test\-Time Reasoning

**Autores:** Yi Ding; Mengyu Wang; Min Zhou; Menglin Yang

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

An early mistake in the generated reasoning can constrain all subsequent reasoning\. Repeated\-generation methods, like MCMC\-based approaches, attempt to improve output quality by sampling multiple generations, but their effectiveness can be limited by randomly selecting where to regenerate\. On MATH500 with Qwen2\.5\-Math\-7B, we find that incorrect responses have substantially higher mean token entropy than correct responses, with an average within\-question relative increase of approximately 112%, suggesting that entropy can signal reasoning errors\. Motivated by this finding, we introduce REWIND, a training\-free controller that uses entropy dynamics to propose targeted suffix regenerations\. Across three model families and five benchmarks, REWIND outperforms all baselines, with gains of 0\.51\-10\.00 percentage points over the strongest baseline\. These results demonstrate the effectiveness of targeted, uncertainty\-guided trajectory repair across models and tasks\. Our code is available at https://anonymous\.4open\.science/r/rewind\-D310\.

[Consultar publicação](<https://arxiv.org/abs/2610.19561>)
