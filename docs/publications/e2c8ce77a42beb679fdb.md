---
title: A Dependency-Aware Multi-GPU Training Framework for Temporal Graph Neural Networks
authors:
- Yang Zhao
- Yue Dai
- Liang Qiao
- Buxin Tu
- Bo Liu
- Sen Zhang
- Yi Zhang
- Xiaoyu Hao
- Jun Shi
- Junshi Chen
- Hong An
date: '2026-10-11'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Temporal graph neural networks (TGNNs) achieve superior performance in
  many dynamic graph learning tasks. These models use node state vectors (i.e., memories)
  to capture and record graph changes (i.e., events), and then exploit these memories
  to assist prediction. However, this memory-centric design makes multi-GPU training
  challenging because predictions for later events often depend on memory updates
  from earlier events. To maintain model quality, existing multi-GPU TGNN training
  schemes strictly preserve all event dependencies, which limits parallelism and causes
  expensive cross-GPU memory synchronization. In this work, we observe that many of
  these dependencies can be handled more flexibly without harming training quality.
  Specifically, (a) dependencies in TGNN training have high locality in both time
  and graph topology, (b) the short-range dependencies missed within a large batch
  can often be recovered cheaply, and (c) many memory updates are not immediately
  needed. Based on these observations, we propose DepBloom to accelerate multi-GPU
  TGNN training with three techniques: (1) temporally bounded spatial partitioning
  to reduce unnecessary cross-GPU synchronization and improve parallelism; (2) intra-batch
  memory refinement to recover missing short-range temporal dependencies inside enlarged
  batches; and (3) critical-path optimization to prioritize urgent memory updates
  while deferring non-critical work during multi-GPU pipeline execution. Experimental
  results across representative models and diverse datasets show that DepBloom achieves
  an average speedup of 2.84$\times$ and up to 5.16$\times$ over state-of-the-art
  methods, while maintaining comparable or better model accuracy.'
source:
- arXiv
source_ids:
- arxiv:2610.15730
url: https://arxiv.org/abs/2610.15730
discovered_at: '2026-10-16'
tags: *id001
---

# A Dependency\-Aware Multi\-GPU Training Framework for Temporal Graph Neural Networks

**Autores:** Yang Zhao; Yue Dai; Liang Qiao; Buxin Tu; Bo Liu; Sen Zhang; Yi Zhang; Xiaoyu Hao; Jun Shi; Junshi Chen; Hong An

**Data:** 2026-10-11 · **Tipo:** preprint

## Resumo

Temporal graph neural networks \(TGNNs\) achieve superior performance in many dynamic graph learning tasks\. These models use node state vectors \(i\.e\., memories\) to capture and record graph changes \(i\.e\., events\), and then exploit these memories to assist prediction\. However, this memory\-centric design makes multi\-GPU training challenging because predictions for later events often depend on memory updates from earlier events\. To maintain model quality, existing multi\-GPU TGNN training schemes strictly preserve all event dependencies, which limits parallelism and causes expensive cross\-GPU memory synchronization\. In this work, we observe that many of these dependencies can be handled more flexibly without harming training quality\. Specifically, \(a\) dependencies in TGNN training have high locality in both time and graph topology, \(b\) the short\-range dependencies missed within a large batch can often be recovered cheaply, and \(c\) many memory updates are not immediately needed\. Based on these observations, we propose DepBloom to accelerate multi\-GPU TGNN training with three techniques: \(1\) temporally bounded spatial partitioning to reduce unnecessary cross\-GPU synchronization and improve parallelism; \(2\) intra\-batch memory refinement to recover missing short\-range temporal dependencies inside enlarged batches; and \(3\) critical\-path optimization to prioritize urgent memory updates while deferring non\-critical work during multi\-GPU pipeline execution\. Experimental results across representative models and diverse datasets show that DepBloom achieves an average speedup of 2\.84$\\times$ and up to 5\.16$\\times$ over state\-of\-the\-art methods, while maintaining comparable or better model accuracy\.

[Consultar publicação](<https://arxiv.org/abs/2610.15730>)
