---
title: 'Heuristics are Not Enough: Calibrated and Corrected Caching for Video Diffusion
  Acceleration'
authors:
- Jiyue Jiang
- Zhiyu Huo
- Yuhan Chen
- Yanruisheng Shao
- Gong Zhang
- Lei Deng
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Feature caching has become a mainstream training-free strategy for accelerating
  video diffusion models by reusing intermediate outputs across denoising steps. However,
  existing adaptive methods rely on heuristic difference measures misaligned with
  actual generation quality, employ a single global threshold that ignores heterogeneous
  phase dynamics, and never validate their budget estimates against true approximation
  error, allowing systematic bias to propagate uncorrected. We propose \textbf{AlignCache},
  a closed-loop caching framework that directly aligns scheduling decisions with their
  true influence on the final generated video through three tightly coupled components:
  (1) phase-adaptive budget routing that partitions the denoising trajectory into
  structurally distinct phases, each governed by an independent threshold and a staleness-aware
  guard; (2) closed-loop threshold calibration that exploits counterfactual error
  measurement at the classifier-free guided output level to adjust decision boundaries
  online via an EMA feedback loop; and (3) momentum-augmented draft synthesis combining
  direction-magnitude gated residual extrapolation with anchor-guided unconditional
  correction. By transforming scheduling from a static risk accumulator into a feedback-driven,
  self-correcting controller, AlignCache consistently achieves superior acceleration-quality
  trade-offs across state-of-the-art video generation models. Our code is available
  at https://github.com/jiangjyjy/AlignCache.'
source:
- arXiv
source_ids:
- arxiv:2610.16545
url: https://arxiv.org/abs/2610.16545
discovered_at: '2026-10-16'
tags: *id001
---

# Heuristics are Not Enough: Calibrated and Corrected Caching for Video Diffusion Acceleration

**Autores:** Jiyue Jiang; Zhiyu Huo; Yuhan Chen; Yanruisheng Shao; Gong Zhang; Lei Deng

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Feature caching has become a mainstream training\-free strategy for accelerating video diffusion models by reusing intermediate outputs across denoising steps\. However, existing adaptive methods rely on heuristic difference measures misaligned with actual generation quality, employ a single global threshold that ignores heterogeneous phase dynamics, and never validate their budget estimates against true approximation error, allowing systematic bias to propagate uncorrected\. We propose \\textbf\{AlignCache\}, a closed\-loop caching framework that directly aligns scheduling decisions with their true influence on the final generated video through three tightly coupled components: \(1\) phase\-adaptive budget routing that partitions the denoising trajectory into structurally distinct phases, each governed by an independent threshold and a staleness\-aware guard; \(2\) closed\-loop threshold calibration that exploits counterfactual error measurement at the classifier\-free guided output level to adjust decision boundaries online via an EMA feedback loop; and \(3\) momentum\-augmented draft synthesis combining direction\-magnitude gated residual extrapolation with anchor\-guided unconditional correction\. By transforming scheduling from a static risk accumulator into a feedback\-driven, self\-correcting controller, AlignCache consistently achieves superior acceleration\-quality trade\-offs across state\-of\-the\-art video generation models\. Our code is available at https://github\.com/jiangjyjy/AlignCache\.

[Consultar publicação](<https://arxiv.org/abs/2610.16545>)
