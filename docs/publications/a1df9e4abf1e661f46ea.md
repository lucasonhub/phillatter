---
title: 'N-Gram Memories at Two Bits: Quantizing Lookup Tables in Large Language Models'
authors:
- Donghoon Han
- Minseop Jung
- Dong Woo Kwak
- SeungJae Lee
- Junhoo Lee
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Conditional memory expands language-model capacity through selective lookup,
  but the full embedding table must remain available for every possible input. We
  introduce Conditional Program (CP), a compressed representation that reconstructs
  only the rows an input requests. CP represents each row by a short code and a local
  scale, with a reconstruction program shared across the table. We instantiate this
  representation with a Gaussian trellis, norm restoration and independently decodable
  row records. CP's two-bit code lowers output KL by 41--63\% relative to 2-bit round-to-nearest.
  Analysis across three trained n-gram memory families shows that Gaussian-like coordinate
  statistics coexist with learned relationships among rows; at matched storage budgets,
  the shared trellis outperforms the fitted codebooks and low-rank residual variants
  we test. For DeepSeek, it reduces table storage from 203GB to 51GB, leaving room
  for larger workloads when the table is kept on GPU.
source:
- arXiv
source_ids:
- arxiv:2610.21810
url: https://arxiv.org/abs/2610.21810
discovered_at: '2026-10-19'
tags: *id001
---

# N\-Gram Memories at Two Bits: Quantizing Lookup Tables in Large Language Models

**Autores:** Donghoon Han; Minseop Jung; Dong Woo Kwak; SeungJae Lee; Junhoo Lee

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Conditional memory expands language\-model capacity through selective lookup, but the full embedding table must remain available for every possible input\. We introduce Conditional Program \(CP\), a compressed representation that reconstructs only the rows an input requests\. CP represents each row by a short code and a local scale, with a reconstruction program shared across the table\. We instantiate this representation with a Gaussian trellis, norm restoration and independently decodable row records\. CP&\#x27;s two\-bit code lowers output KL by 41\-\-63\\% relative to 2\-bit round\-to\-nearest\. Analysis across three trained n\-gram memory families shows that Gaussian\-like coordinate statistics coexist with learned relationships among rows; at matched storage budgets, the shared trellis outperforms the fitted codebooks and low\-rank residual variants we test\. For DeepSeek, it reduces table storage from 203GB to 51GB, leaving room for larger workloads when the table is kept on GPU\.

[Consultar publicação](<https://arxiv.org/abs/2610.21810>)
