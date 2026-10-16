---
title: 'ReTAC: Residual Test-Time Agentic Computation for Video Spatial Reasoning'
authors:
- Yike Wu
- Keyan Chen
- Qixiong Wang
- Xi Xiang
- Maofei Que
- Xiaolong Jiang
- Xiaoqin Zhang
- Ling Shao
- Shijian Lu
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Test-time agentic computation can improve multimodal large language models
  (MLLMs) through planning, tool use, iterative perception, and reflection, but indiscriminate
  computation may duplicate resolved work, introduce noisy evidence, and perturb correct
  predictions. We propose that such computation should be residual: allocate additional
  computation only to requirements unresolved by the base model and, after a localized
  failure, recompute only the affected states. We instantiate this formulation in
  ReTAC, a training-free multiagent framework for video spatial reasoning. ReTAC organizes
  supplementary computation around unresolved requirements. It plans ordered steps
  to acquire missing spatial evidence and combines the observations with compatible
  native evidence for reasoning. In addition, it uses stage-aligned verification to
  localize failures to planning, perception, or reasoning. Dependency-based recovery
  recomputes only affected states while reusing unaffected ones. Extensive experiments
  show that ReTAC achieves the highest overall score among the compared methods across
  three mainstream MLLMs and two widely adopted benchmarks. Further analyses show
  that gains from additional computation depend not only on how much is used, but
  also on where it is allocated and which valid intermediate states are preserved.'
source:
- arXiv
source_ids:
- arxiv:2610.16315
url: https://arxiv.org/abs/2610.16315
discovered_at: '2026-10-16'
tags: *id001
---

# ReTAC: Residual Test\-Time Agentic Computation for Video Spatial Reasoning

**Autores:** Yike Wu; Keyan Chen; Qixiong Wang; Xi Xiang; Maofei Que; Xiaolong Jiang; Xiaoqin Zhang; Ling Shao; Shijian Lu

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Test\-time agentic computation can improve multimodal large language models \(MLLMs\) through planning, tool use, iterative perception, and reflection, but indiscriminate computation may duplicate resolved work, introduce noisy evidence, and perturb correct predictions\. We propose that such computation should be residual: allocate additional computation only to requirements unresolved by the base model and, after a localized failure, recompute only the affected states\. We instantiate this formulation in ReTAC, a training\-free multiagent framework for video spatial reasoning\. ReTAC organizes supplementary computation around unresolved requirements\. It plans ordered steps to acquire missing spatial evidence and combines the observations with compatible native evidence for reasoning\. In addition, it uses stage\-aligned verification to localize failures to planning, perception, or reasoning\. Dependency\-based recovery recomputes only affected states while reusing unaffected ones\. Extensive experiments show that ReTAC achieves the highest overall score among the compared methods across three mainstream MLLMs and two widely adopted benchmarks\. Further analyses show that gains from additional computation depend not only on how much is used, but also on where it is allocated and which valid intermediate states are preserved\.

[Consultar publicação](<https://arxiv.org/abs/2610.16315>)
