---
title: 'BELT : BEhavior-Aligned Low-Rank KV Cache Compression with Learned Top-k Rank
  Allocation'
authors:
- Yaoyang Liu
- Shuwei Shen
- Jincheng Tang
- Jinguang Liu
- Jinbao Xue
- Hailong Yang
- Ke Zhang
- Yinjun Wu
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Long-context inference makes the key-value (KV) cache a major memory bottleneck
  for large language models. We propose BELT, a low-rank KV cache compression framework.
  Its key-side objective targets attention distributions rather than raw keys or pre-softmax
  logits, yielding a quadratic surrogate with a closed-form low-rank solution. A learned
  global rank allocator uses differentiable soft selection during training and hard
  selection at deployment to meet a user-specified component budget. Experiments demonstrate
  improved model quality under aggressive compression and increased decoding throughput
  at comparable accuracy. Evaluated across three LLMs and multiple benchmarks, BELT
  achieves up to 70% low-rank KV cache compression while outperforming the strongest
  baseline by up to 23.3 points on LongBench, and up to 17.8x overall KV cache reduction
  when combined with quantization. With Triton-based GPU kernels and a quantized cache,
  BELT delivers up to 2.7x speedup for the attention module and 3.3x end-to-end decoding
  throughput.
source:
- arXiv
source_ids:
- arxiv:2610.17966
url: https://arxiv.org/abs/2610.17966
discovered_at: '2026-10-16'
tags: *id001
---

# BELT : BEhavior\-Aligned Low\-Rank KV Cache Compression with Learned Top\-k Rank Allocation

**Autores:** Yaoyang Liu; Shuwei Shen; Jincheng Tang; Jinguang Liu; Jinbao Xue; Hailong Yang; Ke Zhang; Yinjun Wu

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Long\-context inference makes the key\-value \(KV\) cache a major memory bottleneck for large language models\. We propose BELT, a low\-rank KV cache compression framework\. Its key\-side objective targets attention distributions rather than raw keys or pre\-softmax logits, yielding a quadratic surrogate with a closed\-form low\-rank solution\. A learned global rank allocator uses differentiable soft selection during training and hard selection at deployment to meet a user\-specified component budget\. Experiments demonstrate improved model quality under aggressive compression and increased decoding throughput at comparable accuracy\. Evaluated across three LLMs and multiple benchmarks, BELT achieves up to 70% low\-rank KV cache compression while outperforming the strongest baseline by up to 23\.3 points on LongBench, and up to 17\.8x overall KV cache reduction when combined with quantization\. With Triton\-based GPU kernels and a quantized cache, BELT delivers up to 2\.7x speedup for the attention module and 3\.3x end\-to\-end decoding throughput\.

[Consultar publicação](<https://arxiv.org/abs/2610.17966>)
