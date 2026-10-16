---
title: 'JtT: Rethinking Point Trajectory Diffusion for Diverse and Rigid Motion from
  an Image'
authors:
- Gabrijel Boduljak
- Yushi Lan
- Christian Rupprecht
- Andrea Vedaldi
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'We study forecasting rigid-body motion from a single image: generating
  diverse and physically plausible future trajectories for arbitrary points in a scene,
  without building rigidity into the architecture or relying on geometric inputs such
  as depth. Like video generators, recent trajectory generators fail at this task,
  even in simple synthetic Kubric scenes, despite scaling up model size and training
  on real data. We show how to solve this with the right architecture and parameterization.
  Our model, JtT, is a simple diffusion transformer that operates directly in coordinate
  space and decodes arbitrary and dense query patterns, without the trajectory VAEs
  or fixed grids assumed in prior work. Through a systematic study of the design space
  of point trajectory diffusion, we find that diffusing per-frame velocities is the
  only parameterization that captures rigidity, that it must be paired with the right
  timestep schedule, and that adding full-resolution RGB at the query points resolves
  the boundary failures of prior methods. However, evaluating such 2D models rigorously
  is itself non-trivial. To our knowledge, we are the first to observe that physical
  plausibility and diversity do not improve together during training: larger models,
  as used in prior work, memorize the single ground-truth future per training image,
  becoming more rigid while covering fewer possible futures. Yet prior work has paid
  little attention to this, so we show how model rankings depend on model size, metric,
  and stopping time, and adopt a stricter, checkpoint-averaged evaluation protocol.
  Under this protocol, JtT improves over prior methods on both distributional and
  rigidity metrics and approaches ground-truth rigidity, with only about 50M parameters.'
source:
- arXiv
source_ids:
- arxiv:2610.16591
url: https://arxiv.org/abs/2610.16591
discovered_at: '2026-10-16'
tags: *id001
---

# JtT: Rethinking Point Trajectory Diffusion for Diverse and Rigid Motion from an Image

**Autores:** Gabrijel Boduljak; Yushi Lan; Christian Rupprecht; Andrea Vedaldi

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

We study forecasting rigid\-body motion from a single image: generating diverse and physically plausible future trajectories for arbitrary points in a scene, without building rigidity into the architecture or relying on geometric inputs such as depth\. Like video generators, recent trajectory generators fail at this task, even in simple synthetic Kubric scenes, despite scaling up model size and training on real data\. We show how to solve this with the right architecture and parameterization\. Our model, JtT, is a simple diffusion transformer that operates directly in coordinate space and decodes arbitrary and dense query patterns, without the trajectory VAEs or fixed grids assumed in prior work\. Through a systematic study of the design space of point trajectory diffusion, we find that diffusing per\-frame velocities is the only parameterization that captures rigidity, that it must be paired with the right timestep schedule, and that adding full\-resolution RGB at the query points resolves the boundary failures of prior methods\. However, evaluating such 2D models rigorously is itself non\-trivial\. To our knowledge, we are the first to observe that physical plausibility and diversity do not improve together during training: larger models, as used in prior work, memorize the single ground\-truth future per training image, becoming more rigid while covering fewer possible futures\. Yet prior work has paid little attention to this, so we show how model rankings depend on model size, metric, and stopping time, and adopt a stricter, checkpoint\-averaged evaluation protocol\. Under this protocol, JtT improves over prior methods on both distributional and rigidity metrics and approaches ground\-truth rigidity, with only about 50M parameters\.

[Consultar publicação](<https://arxiv.org/abs/2610.16591>)
