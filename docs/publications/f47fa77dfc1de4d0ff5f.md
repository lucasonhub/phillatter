---
title: 'Deep Reinforcement Learning for HPC Job Scheduling: A Statistical Evaluation'
authors:
- Justin M. Cheney
- Clement N. Nyirenda
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Deep Reinforcement Learning (DRL) offers learned job selection for High-Performance
  Computing (HPC), but performance against heuristics alone does not establish value
  beyond action masking. Six DRL treatments are compared: Proximal Policy Optimization
  (PPO), Advantage Actor-Critic (A2C), and Deep Q-Network (DQN), each with and without
  masking. Three heuristics and a seed-paired masked uniform random control provide
  baselines across ten seeds on two real Slurm (Simple Linux Utility for Resource
  Management) workload traces, one homogeneous and one heterogeneous, under a common
  non-parametric framework. All masked treatments complete evaluation, whereas unmasked
  treatments are truncated. On the homogeneous trace, no masked DRL treatment significantly
  improves average waiting time or average and maximum bounded slowdown over the control.
  On the heterogeneous trace, MaskablePPO improves all three metrics relative to the
  control. Its average waiting time is equivalent to that of the three heuristics
  within a 10% margin, and its maximum bounded slowdown is 22% lower than that of
  Last-Come, First-Served (LCFS). MaskablePPO has the leading average waiting-time
  rank among complete treatments on both traces, but Nemenyi comparisons detect no
  significant difference from MaskableA2C. Among masked variants, MaskablePPO has
  the lowest recorded mean training time, while MaskableDQN has the lowest mean decision
  latency. These findings distinguish completion from baseline-specific scheduling
  gains and support including a masked random control when assessing the value of
  learned selection.'
source:
- arXiv
source_ids:
- arxiv:2610.21008
url: https://arxiv.org/abs/2610.21008
discovered_at: '2026-10-16'
tags: *id001
---

# Deep Reinforcement Learning for HPC Job Scheduling: A Statistical Evaluation

**Autores:** Justin M\. Cheney; Clement N\. Nyirenda

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Deep Reinforcement Learning \(DRL\) offers learned job selection for High\-Performance Computing \(HPC\), but performance against heuristics alone does not establish value beyond action masking\. Six DRL treatments are compared: Proximal Policy Optimization \(PPO\), Advantage Actor\-Critic \(A2C\), and Deep Q\-Network \(DQN\), each with and without masking\. Three heuristics and a seed\-paired masked uniform random control provide baselines across ten seeds on two real Slurm \(Simple Linux Utility for Resource Management\) workload traces, one homogeneous and one heterogeneous, under a common non\-parametric framework\. All masked treatments complete evaluation, whereas unmasked treatments are truncated\. On the homogeneous trace, no masked DRL treatment significantly improves average waiting time or average and maximum bounded slowdown over the control\. On the heterogeneous trace, MaskablePPO improves all three metrics relative to the control\. Its average waiting time is equivalent to that of the three heuristics within a 10% margin, and its maximum bounded slowdown is 22% lower than that of Last\-Come, First\-Served \(LCFS\)\. MaskablePPO has the leading average waiting\-time rank among complete treatments on both traces, but Nemenyi comparisons detect no significant difference from MaskableA2C\. Among masked variants, MaskablePPO has the lowest recorded mean training time, while MaskableDQN has the lowest mean decision latency\. These findings distinguish completion from baseline\-specific scheduling gains and support including a masked random control when assessing the value of learned selection\.

[Consultar publicação](<https://arxiv.org/abs/2610.21008>)
