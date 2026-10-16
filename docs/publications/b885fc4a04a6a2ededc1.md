---
title: Multi-Level Deep Deterministic Policy Gradient reinforcement learning for safety-constrained
  trajectory optimization of collaborative industrial robots
authors:
- Akhanseri Ikramov
- Sayat Ibrayev
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3389/frai.2026.1914042
abstract: Collaborative robots operating in modern manufacturing environments require
  trajectory planning strategies that simultaneously support efficiency, adaptability,
  and operational safety. This study proposes a Multi-Level Deep Deterministic Policy
  Gradient (ML-DDPG) framework for safety-constrained trajectory optimization. The
  framework combines a strategic waypoint level, a continuous DDPG motion-control
  policy, and a reactive feasibility projection that corrects unsafe actions before
  execution. The trajectory-planning problem is formulated as a Markov Decision Process
  with reward terms for goal progress, obstacle clearance, smoothness, energy, execution
  time, and safety. Descriptive experiments in a custom PyTorch-based three-dimensional
  environment compare ML-DDPG with conventional planners and the DDPG, TD3, and SAC
  baselines. In the retained single training run, ML-DDPG produced observed values
  of 98.7% success, 1.08 mm trajectory error, a 0.98 smoothness index, and no recorded
  collision. These values are single-run observations and are not means over independent
  seeds; variability and statistical significance cannot be estimated from the available
  record. The exported traces show faster reward growth within the 200-episode budget,
  and the single-run ablation record associates the largest observed gains with the
  combined multi-level, reward, and projection components. One UR5e demonstration
  yielded 0.018 m mean tracking error, 0.042 m maximum tracking error, and no collision
  in that trial. A separate ABB welding sequence is included only as qualitative feasibility
  evidence because synchronized trajectory, force, and weld-quality logs were unavailable.
  The findings motivate further evaluation, while multi-seed training, repeated hardware
  trials, complete reporting of evaluation procedures, and cross-platform validation
  remain necessary before broader generalization.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221134234
url: https://doi.org/10.3389/frai.2026.1914042
discovered_at: '2026-10-16'
tags: *id001
---

# Multi\-Level Deep Deterministic Policy Gradient reinforcement learning for safety\-constrained trajectory optimization of collaborative industrial robots

**Autores:** Akhanseri Ikramov; Sayat Ibrayev

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

Collaborative robots operating in modern manufacturing environments require trajectory planning strategies that simultaneously support efficiency, adaptability, and operational safety\. This study proposes a Multi\-Level Deep Deterministic Policy Gradient \(ML\-DDPG\) framework for safety\-constrained trajectory optimization\. The framework combines a strategic waypoint level, a continuous DDPG motion\-control policy, and a reactive feasibility projection that corrects unsafe actions before execution\. The trajectory\-planning problem is formulated as a Markov Decision Process with reward terms for goal progress, obstacle clearance, smoothness, energy, execution time, and safety\. Descriptive experiments in a custom PyTorch\-based three\-dimensional environment compare ML\-DDPG with conventional planners and the DDPG, TD3, and SAC baselines\. In the retained single training run, ML\-DDPG produced observed values of 98\.7% success, 1\.08 mm trajectory error, a 0\.98 smoothness index, and no recorded collision\. These values are single\-run observations and are not means over independent seeds; variability and statistical significance cannot be estimated from the available record\. The exported traces show faster reward growth within the 200\-episode budget, and the single\-run ablation record associates the largest observed gains with the combined multi\-level, reward, and projection components\. One UR5e demonstration yielded 0\.018 m mean tracking error, 0\.042 m maximum tracking error, and no collision in that trial\. A separate ABB welding sequence is included only as qualitative feasibility evidence because synchronized trajectory, force, and weld\-quality logs were unavailable\. The findings motivate further evaluation, while multi\-seed training, repeated hardware trials, complete reporting of evaluation procedures, and cross\-platform validation remain necessary before broader generalization\.

[Consultar publicação](<https://doi.org/10.3389/frai.2026.1914042>)
