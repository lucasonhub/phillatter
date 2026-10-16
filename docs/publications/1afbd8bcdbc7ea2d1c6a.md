---
title: Joint optimization of detection, task allocation, and path planning for multi-agent
  cooperative interception under partial observability
authors:
- Qinlong Huang
- Zhikun Liu
- Yasong Luo
- Zhong Liu
- Qingtao Xia
- Miao Zhao
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1371/journal.pone.0359071
abstract: Safety-critical autonomous systems often require multiple agents to detect,
  assign, and intercept non-cooperative mobile targets using only partial observations.
  These subtasks are tightly coupled because the same agents must balance spatial
  exploration for detection with goal-directed motion for interception, while target
  maneuvers remain uncertain. This study develops and validates an integrated multi-agent
  coordination framework for jointly optimizing distributed detection, dynamic task
  allocation, and path planning under partial observability. The problem is formulated
  as a coupled Dec-POMDP made computationally tractable through factored decentralized
  policies, parameter sharing, and centralized training with decentralized execution,
  and a Weighted Coordinated Multi-Agent Proximal Policy Optimization (W-MAPPO) framework
  is introduced to adaptively coordinate competing subtasks. W-MAPPO combines an observation-conditioned
  Policy Ratio Predictor, an LSTM-based history-aware processor for temporal modeling
  of target maneuvers, and a Voronoi-based collaborative detection module for spatial
  coverage coordination within a centralized-training decentralized-execution paradigm.
  Comprehensive simulation experiments across increasing target densities compare
  W-MAPPO with seven representative MARL baselines and two classical methods, supported
  by statistical testing, ablation studies, sensitivity analysis, and representative
  case studies. W-MAPPO achieves a 94% success rate in the 5 vs 5 scenario and maintains
  stable interception performance as the number of targets increases to 10 and 15.
  These results demonstrate the technical reliability and practical potential of integrated
  subtask coordination for partially observable multi-agent systems.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221626916
url: https://doi.org/10.1371/journal.pone.0359071
discovered_at: '2026-10-16'
tags: *id001
---

# Joint optimization of detection, task allocation, and path planning for multi\-agent cooperative interception under partial observability

**Autores:** Qinlong Huang; Zhikun Liu; Yasong Luo; Zhong Liu; Qingtao Xia; Miao Zhao

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Safety\-critical autonomous systems often require multiple agents to detect, assign, and intercept non\-cooperative mobile targets using only partial observations\. These subtasks are tightly coupled because the same agents must balance spatial exploration for detection with goal\-directed motion for interception, while target maneuvers remain uncertain\. This study develops and validates an integrated multi\-agent coordination framework for jointly optimizing distributed detection, dynamic task allocation, and path planning under partial observability\. The problem is formulated as a coupled Dec\-POMDP made computationally tractable through factored decentralized policies, parameter sharing, and centralized training with decentralized execution, and a Weighted Coordinated Multi\-Agent Proximal Policy Optimization \(W\-MAPPO\) framework is introduced to adaptively coordinate competing subtasks\. W\-MAPPO combines an observation\-conditioned Policy Ratio Predictor, an LSTM\-based history\-aware processor for temporal modeling of target maneuvers, and a Voronoi\-based collaborative detection module for spatial coverage coordination within a centralized\-training decentralized\-execution paradigm\. Comprehensive simulation experiments across increasing target densities compare W\-MAPPO with seven representative MARL baselines and two classical methods, supported by statistical testing, ablation studies, sensitivity analysis, and representative case studies\. W\-MAPPO achieves a 94% success rate in the 5 vs 5 scenario and maintains stable interception performance as the number of targets increases to 10 and 15\. These results demonstrate the technical reliability and practical potential of integrated subtask coordination for partially observable multi\-agent systems\.

[Consultar publicação](<https://doi.org/10.1371/journal.pone.0359071>)
