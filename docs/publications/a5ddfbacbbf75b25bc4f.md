---
title: Efficient CPU-GPU collaborative MoE inference via Adaptive Expert Assignment
authors:
- Wenhui Lv
- Yunming Liao
- Hongli Xu
- Yang Xu
- Junhao Cheng
date: '2026-10-16'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Mixture-of-Experts (MoE) models reduce inference computation through sparse
  expert activation, but their large expert memory footprint often exceeds GPU capacity,
  making expert offloading necessary for memory-constrained inference. However, existing
  systems typically handle GPU-missed experts by either transferring them to the GPU,
  incurring substantial PCIe transfer latency, or executing them on the CPU, making
  the slower CPU computation the bottleneck. To address these limitations, we present
  \method, a CPU-GPU collaborative MoE inference system that adaptively assigns these
  missed experts to the CPU or GPU for efficient execution. By exploiting differences
  in expert token-loads, \method selectively transfers high-load experts to the GPU
  while executing low-load experts on the CPU. To minimize inference latency, \method
  adaptively adjusts expert assignments to balance the CPU computation path against
  the GPU transfer-and-computation path, allowing both execution paths to complete
  as early as possible. Extensive experiments on three representative MoE LLMs show
  that \method improves prefill speed by up to 51.9\% and decode throughput by up
  to 39.5\% over the strongest baseline across the evaluated batch sizes, with consistent
  gains under different GPU-memory budgets.
source:
- arXiv
source_ids:
- arxiv:2610.23006
url: https://arxiv.org/abs/2610.23006
discovered_at: '2026-10-19'
tags: *id001
---

# Efficient CPU\-GPU collaborative MoE inference via Adaptive Expert Assignment

**Autores:** Wenhui Lv; Yunming Liao; Hongli Xu; Yang Xu; Junhao Cheng

**Data:** 2026-10-16 · **Tipo:** preprint

## Resumo

Mixture\-of\-Experts \(MoE\) models reduce inference computation through sparse expert activation, but their large expert memory footprint often exceeds GPU capacity, making expert offloading necessary for memory\-constrained inference\. However, existing systems typically handle GPU\-missed experts by either transferring them to the GPU, incurring substantial PCIe transfer latency, or executing them on the CPU, making the slower CPU computation the bottleneck\. To address these limitations, we present \\method, a CPU\-GPU collaborative MoE inference system that adaptively assigns these missed experts to the CPU or GPU for efficient execution\. By exploiting differences in expert token\-loads, \\method selectively transfers high\-load experts to the GPU while executing low\-load experts on the CPU\. To minimize inference latency, \\method adaptively adjusts expert assignments to balance the CPU computation path against the GPU transfer\-and\-computation path, allowing both execution paths to complete as early as possible\. Extensive experiments on three representative MoE LLMs show that \\method improves prefill speed by up to 51\.9\\% and decode throughput by up to 39\.5\\% over the strongest baseline across the evaluated batch sizes, with consistent gains under different GPU\-memory budgets\.

[Consultar publicação](<https://arxiv.org/abs/2610.23006>)
