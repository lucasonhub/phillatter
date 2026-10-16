---
title: What DNA Foundation Models Learn Beyond Sequence Composition
authors:
- Vincenzo Yuto Civale
- Andrew David Bagdanov
- Alberto Magi
date: '2026-10-11'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Do genomic foundation models (FMs) provide predictive information beyond
  simple sequence composition? We evaluate frozen representations from five DNA FMs
  against normalized k-mer frequencies across 57 genomic classification datasets and
  two exploratory gene-expression regression tasks. Simple k-mer features remain competitive
  with most models, whereas NTv3 shows a consistent advantage; the ranking is robust
  to globally fixed and multi-scale k-mer baselines and alternative downstream probes.
  To test incremental predictive utility directly, we compare global 6-mer features
  with their concatenation with each FM embedding under a matched Random Forest protocol.
  NTv3 improves 46 of 57 datasets (mean $Δ$MCC = +0.072), while Caduceus provides
  smaller gains and the other models do not improve mean MCC. We separately decompose
  embeddings into a component linearly predictable from 6-mer frequencies and a ridge
  residual, finding that linear recoverability does not reliably indicate downstream
  utility. Exact 6-mer-preserving shuffles further reveal task-relevant sequence-order
  sensitivity, most pronounced for NTv3, although order sensitivity alone does not
  guarantee predictive improvements. Our results establish compositional features
  as essential controls and offer complementary diagnostics for evaluating the added
  value of frozen genomic representations, without making claims about fine-tuning
  capacity.
source:
- arXiv
source_ids:
- arxiv:2610.15711
url: https://arxiv.org/abs/2610.15711
discovered_at: '2026-10-16'
tags: *id001
---

# What DNA Foundation Models Learn Beyond Sequence Composition

**Autores:** Vincenzo Yuto Civale; Andrew David Bagdanov; Alberto Magi

**Data:** 2026-10-11 · **Tipo:** preprint

## Resumo

Do genomic foundation models \(FMs\) provide predictive information beyond simple sequence composition? We evaluate frozen representations from five DNA FMs against normalized k\-mer frequencies across 57 genomic classification datasets and two exploratory gene\-expression regression tasks\. Simple k\-mer features remain competitive with most models, whereas NTv3 shows a consistent advantage; the ranking is robust to globally fixed and multi\-scale k\-mer baselines and alternative downstream probes\. To test incremental predictive utility directly, we compare global 6\-mer features with their concatenation with each FM embedding under a matched Random Forest protocol\. NTv3 improves 46 of 57 datasets \(mean $Δ$MCC = \+0\.072\), while Caduceus provides smaller gains and the other models do not improve mean MCC\. We separately decompose embeddings into a component linearly predictable from 6\-mer frequencies and a ridge residual, finding that linear recoverability does not reliably indicate downstream utility\. Exact 6\-mer\-preserving shuffles further reveal task\-relevant sequence\-order sensitivity, most pronounced for NTv3, although order sensitivity alone does not guarantee predictive improvements\. Our results establish compositional features as essential controls and offer complementary diagnostics for evaluating the added value of frozen genomic representations, without making claims about fine\-tuning capacity\.

[Consultar publicação](<https://arxiv.org/abs/2610.15711>)
