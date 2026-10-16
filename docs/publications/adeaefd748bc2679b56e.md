---
title: Heterogeneous Structured Pruning Under Resource Constraints for Hardware-Efficient
  Large Language Models
authors:
- Cameron Barker
- Andreas Paraskeva
- Jan N. van Rijn
- Elliot J. Crowley
- Henry Gouk
date: '2026-10-11'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Training-free pruning removes weights from pretrained large language models
  to reduce their deployment cost. However, existing approaches typically consider
  only the total number of retained weights. Consequently, their pruning decisions
  do not account for how target hardware stores and processes those weights. These
  methods select a sparsity structure in advance and apply it uniformly to all projections,
  rather than accounting for how each structure trades pruning error against latency
  and memory across sublayers. We propose Heterogeneous Structured Pruning (HSP),
  a hardware-aware pruning framework that combines two components: (i) a heterogeneous
  search space of dense, unstructured, 2:4, block-sparse, and head / channel (H/C)
  pruning options and (ii) structure-regularising constraints based on latency and
  memory models. Our contribution generalises existing importance-based methods: a
  global solver selects one option per sublayer to minimise proxy pruning loss under
  a resource budget, thereby assigning each projection a structure and density. We
  evaluate HSP on OPT and LLaMA models for an NVIDIA Jetson Orin Nano Super edge device,
  where it improves the quality-resource frontiers over training-free baselines. A
  project page and updated links for the related code is maintained at: cameronbarker.me/publications/hsp.'
source:
- arXiv
source_ids:
- arxiv:2610.15781
url: https://arxiv.org/abs/2610.15781
discovered_at: '2026-10-16'
tags: *id001
---

# Heterogeneous Structured Pruning Under Resource Constraints for Hardware\-Efficient Large Language Models

**Autores:** Cameron Barker; Andreas Paraskeva; Jan N\. van Rijn; Elliot J\. Crowley; Henry Gouk

**Data:** 2026-10-11 · **Tipo:** preprint

## Resumo

Training\-free pruning removes weights from pretrained large language models to reduce their deployment cost\. However, existing approaches typically consider only the total number of retained weights\. Consequently, their pruning decisions do not account for how target hardware stores and processes those weights\. These methods select a sparsity structure in advance and apply it uniformly to all projections, rather than accounting for how each structure trades pruning error against latency and memory across sublayers\. We propose Heterogeneous Structured Pruning \(HSP\), a hardware\-aware pruning framework that combines two components: \(i\) a heterogeneous search space of dense, unstructured, 2:4, block\-sparse, and head / channel \(H/C\) pruning options and \(ii\) structure\-regularising constraints based on latency and memory models\. Our contribution generalises existing importance\-based methods: a global solver selects one option per sublayer to minimise proxy pruning loss under a resource budget, thereby assigning each projection a structure and density\. We evaluate HSP on OPT and LLaMA models for an NVIDIA Jetson Orin Nano Super edge device, where it improves the quality\-resource frontiers over training\-free baselines\. A project page and updated links for the related code is maintained at: cameronbarker\.me/publications/hsp\.

[Consultar publicação](<https://arxiv.org/abs/2610.15781>)
