---
title: 'FreeSolo: Linear-time Sparse Attention with Zero-Shot Length Extrapolation'
authors:
- Zekun Shi
- Alastair James Arthur Price
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Linear-time sequence models typically store long-context information in
  a recurrent state. A fixed-size state limits how much information can be stored,
  while hybrid architectures that add full attention for better recall incur quadratic
  sequence cost. Alternatively, sparse attention with continued pretraining (CPT)
  can extend the effective context length. Generalization beyond the trained length
  remains challenging, however, and CPT can be costly. We introduce FreeSolo, a native
  sparse attention mechanism with a short-range sliding window branch and a long-range
  branch that selects keypoint cells for direct token attention. Its linear-time variant,
  FS-L, learns to prune the prefix before query-dependent selection through short
  CPT. FS-B searches balanced trees with $O(N\log^2 N)$ algorithmic cost including
  radix-sort construction. FreeSolo demonstrates better zero-shot length extrapolation
  than the baselines without long-context fine-tuning.
source:
- arXiv
source_ids:
- arxiv:2610.17191
url: https://arxiv.org/abs/2610.17191
discovered_at: '2026-10-16'
tags: *id001
---

# FreeSolo: Linear\-time Sparse Attention with Zero\-Shot Length Extrapolation

**Autores:** Zekun Shi; Alastair James Arthur Price

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Linear\-time sequence models typically store long\-context information in a recurrent state\. A fixed\-size state limits how much information can be stored, while hybrid architectures that add full attention for better recall incur quadratic sequence cost\. Alternatively, sparse attention with continued pretraining \(CPT\) can extend the effective context length\. Generalization beyond the trained length remains challenging, however, and CPT can be costly\. We introduce FreeSolo, a native sparse attention mechanism with a short\-range sliding window branch and a long\-range branch that selects keypoint cells for direct token attention\. Its linear\-time variant, FS\-L, learns to prune the prefix before query\-dependent selection through short CPT\. FS\-B searches balanced trees with $O\(N\\log^2 N\)$ algorithmic cost including radix\-sort construction\. FreeSolo demonstrates better zero\-shot length extrapolation than the baselines without long\-context fine\-tuning\.

[Consultar publicação](<https://arxiv.org/abs/2610.17191>)
