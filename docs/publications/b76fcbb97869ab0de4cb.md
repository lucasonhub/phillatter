---
title: Large Diffusion Models Need More Than EMA
authors:
- Chuyu Hu
- Huanran Chen
- Shitong Shao
- Yinpeng Dong
date: '2026-10-16'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Large-scale diffusion models are commonly trained with a constant learning
  rate (LR) and exponential moving average (EMA), despite the strong performance of
  LR decay and Schedule-Free optimization in training large language models. We study
  whether EMA is uniquely suited to diffusion training, or whether stronger alternatives
  have been underexplored. Our theory shows that averaging a constant-step trajectory
  has an inherent optimization limitation, whereas LR decay and Schedule-Free optimization
  admit vanishing stationarity guarantees under standard nonconvex assumptions. Empirically,
  LR decay and EMA provide complementary benefits: combining decay with EMA further
  improves the standard baseline at most tested starting points, although the gain
  remains sensitive to when decay begins. Schedule-Free avoids this timing requirement
  and consistently outperforms EMA with a constant LR across training stages, achieving
  both lower fixed-evaluation objectives and better generation quality. Our analysis
  further shows that all three strategies substantially reduce parameter variability,
  yet stronger stabilization is not always better: EMA with a constant LR retains
  comparatively higher parameter variability, while aggressive decay combined with
  EMA achieves the lowest checkpoint variability but also weakens continued optimization.
  Schedule-Free substantially reduces parameter variability while preserving more
  late-stage progress, providing a better balance between parameter stability and
  continued optimization. Finally, the benefits of Schedule-Free extend beyond pretraining
  to ReFL and generator-side DMD, demonstrating its transferability across distinct
  diffusion optimization settings. Overall, our results suggest that large diffusion
  models need more than parameter averaging alone: effective optimization requires
  balancing variance reduction with continued optimization.'
source:
- arXiv
source_ids:
- arxiv:2610.22945
url: https://arxiv.org/abs/2610.22945
discovered_at: '2026-10-19'
tags: *id001
---

# Large Diffusion Models Need More Than EMA

**Autores:** Chuyu Hu; Huanran Chen; Shitong Shao; Yinpeng Dong

**Data:** 2026-10-16 · **Tipo:** preprint

## Resumo

Large\-scale diffusion models are commonly trained with a constant learning rate \(LR\) and exponential moving average \(EMA\), despite the strong performance of LR decay and Schedule\-Free optimization in training large language models\. We study whether EMA is uniquely suited to diffusion training, or whether stronger alternatives have been underexplored\. Our theory shows that averaging a constant\-step trajectory has an inherent optimization limitation, whereas LR decay and Schedule\-Free optimization admit vanishing stationarity guarantees under standard nonconvex assumptions\. Empirically, LR decay and EMA provide complementary benefits: combining decay with EMA further improves the standard baseline at most tested starting points, although the gain remains sensitive to when decay begins\. Schedule\-Free avoids this timing requirement and consistently outperforms EMA with a constant LR across training stages, achieving both lower fixed\-evaluation objectives and better generation quality\. Our analysis further shows that all three strategies substantially reduce parameter variability, yet stronger stabilization is not always better: EMA with a constant LR retains comparatively higher parameter variability, while aggressive decay combined with EMA achieves the lowest checkpoint variability but also weakens continued optimization\. Schedule\-Free substantially reduces parameter variability while preserving more late\-stage progress, providing a better balance between parameter stability and continued optimization\. Finally, the benefits of Schedule\-Free extend beyond pretraining to ReFL and generator\-side DMD, demonstrating its transferability across distinct diffusion optimization settings\. Overall, our results suggest that large diffusion models need more than parameter averaging alone: effective optimization requires balancing variance reduction with continued optimization\.

[Consultar publicação](<https://arxiv.org/abs/2610.22945>)
