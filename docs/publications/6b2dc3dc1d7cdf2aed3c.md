---
title: 'Flash RNN-T: Memory-Efficient Joint Network and Transducer Loss Computation'
authors:
- Mahmoud Ashraf
date: '2026-10-16'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: The recurrent neural network transducer (RNN-T) remains a practical choice
  for streaming speech recognition, but training requires large intermediate tensors.
  We present Flash RNN-T, a joint and loss implementation combining specialized kernels
  with optional tiled recomputation over the full alignment space and vocabulary.
  Tiled and untiled Flash form the entire measured throughput-memory frontier on medium
  and long workloads. On H100, untiled Flash achieves 24-39% higher throughput with
  26-56% less memory than the fastest baseline on these workloads wherever it fits.
  Tiling reduces memory further through recomputation. On medium, tiled Flash uses
  ninefold less memory than that baseline at 16% lower throughput when both use one
  backward call per batch. On long, it fits where all tested alternatives with that
  backward schedule run out of memory with 80 GB. These comparisons use each implementation's
  lowest-memory configuration reaching at least 95% of its peak throughput.
source:
- arXiv
source_ids:
- arxiv:2610.23409
url: https://arxiv.org/abs/2610.23409
discovered_at: '2026-10-19'
tags: *id001
---

# Flash RNN\-T: Memory\-Efficient Joint Network and Transducer Loss Computation

**Autores:** Mahmoud Ashraf

**Data:** 2026-10-16 · **Tipo:** preprint

## Resumo

The recurrent neural network transducer \(RNN\-T\) remains a practical choice for streaming speech recognition, but training requires large intermediate tensors\. We present Flash RNN\-T, a joint and loss implementation combining specialized kernels with optional tiled recomputation over the full alignment space and vocabulary\. Tiled and untiled Flash form the entire measured throughput\-memory frontier on medium and long workloads\. On H100, untiled Flash achieves 24\-39% higher throughput with 26\-56% less memory than the fastest baseline on these workloads wherever it fits\. Tiling reduces memory further through recomputation\. On medium, tiled Flash uses ninefold less memory than that baseline at 16% lower throughput when both use one backward call per batch\. On long, it fits where all tested alternatives with that backward schedule run out of memory with 80 GB\. These comparisons use each implementation&\#x27;s lowest\-memory configuration reaching at least 95% of its peak throughput\.

[Consultar publicação](<https://arxiv.org/abs/2610.23409>)
