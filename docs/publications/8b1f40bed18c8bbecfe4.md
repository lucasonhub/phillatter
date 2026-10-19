---
title: 'BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks'
authors:
- Max Zhu
- Bohang Sun
- Pietro Lio
- Jialin Yu
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Reducing memory use in large language model (LLM) training is an ongoing
  challenge. Activation checkpointing saves memory by recomputation, while lossy compression
  changes the stored activations. The reemergence of sparse $\relu$ and $\relu^2$
  activations creates a third opportunity: losslessly compressing the activation cache
  itself. We present BitSparse, a GPU-resident lossless compression format for sparse
  activations. Compression and reconstruction run in custom Triton kernels fused into
  an autograd function, shrinking the activation cache while recovering it exactly
  for the backward pass. Bfloat16 (BF16) and FP8 activations are supported. Optional
  sign-bit packing further increases compression up to close to the theoretical limit.
  We analyze its compression ratio and compare it to the theoretical optimum. BitSparse
  lowers per-token VRAM by 31\% and 30\% Modded-NanoGPT and Nemotron-H respectively,
  with overheads of no more than 1\% at practical sequence lengths. Additionally,
  a new preallocated buffer system avoids host synchronization during training when
  variable size tensors are allocated.'
source:
- arXiv
source_ids:
- arxiv:2610.22256
url: https://arxiv.org/abs/2610.22256
discovered_at: '2026-10-19'
tags: *id001
---

# BitSparse: Compact Activation Storage for ReLU Feed\-Forward Networks

**Autores:** Max Zhu; Bohang Sun; Pietro Lio; Jialin Yu

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Reducing memory use in large language model \(LLM\) training is an ongoing challenge\. Activation checkpointing saves memory by recomputation, while lossy compression changes the stored activations\. The reemergence of sparse $\\relu$ and $\\relu^2$ activations creates a third opportunity: losslessly compressing the activation cache itself\. We present BitSparse, a GPU\-resident lossless compression format for sparse activations\. Compression and reconstruction run in custom Triton kernels fused into an autograd function, shrinking the activation cache while recovering it exactly for the backward pass\. Bfloat16 \(BF16\) and FP8 activations are supported\. Optional sign\-bit packing further increases compression up to close to the theoretical limit\. We analyze its compression ratio and compare it to the theoretical optimum\. BitSparse lowers per\-token VRAM by 31\\% and 30\\% Modded\-NanoGPT and Nemotron\-H respectively, with overheads of no more than 1\\% at practical sequence lengths\. Additionally, a new preallocated buffer system avoids host synchronization during training when variable size tensors are allocated\.

[Consultar publicação](<https://arxiv.org/abs/2610.22256>)
