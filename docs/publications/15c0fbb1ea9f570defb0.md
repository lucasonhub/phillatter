---
title: Compiling Multi-Threshold Operators for Quantized Non-Monotonic and Fine-Granular
  Activations in Custom-Tailored DNN Accelerators
authors:
- Christoph Berganski
- Felix Jentzsch
- Marco Platzner
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Aggressive quantization of neural networks can expose activation functions
  as bottlenecks for efficient hardware acceleration. Implementing quantized activations
  as multi-threshold operations has been shown to be a promising optimization, allowing
  for efficient hardware implementation of few-bit activations. However, current implementations
  are limited to monotonically increasing functions, quantization schemes with one-dimensional
  (per-channel) granularity and a small set of predefined activation-quantizer combinations.
  We formalize the multi-threshold representation to extend it to non-monotonic functions
  and fine-granular parameters, i.e., multi-dimensional thresholds. For automated
  conversion of quantized function compositions into threshold representation, we
  propose a systematic approach via algebraic rules integrated into the ONNX-based
  compiler infrastructure. We experimentally validate our solution on a selection
  of monotonic and non-monotonic functions by extending the binary search based multi-threshold
  operator that is integrated into the FINN framework for end-to-end synthesis of
  custom-tailored FPGA accelerators. The cost of hardware support for non-monotonicity
  and fine-granularity is characterized in comparison to an alternative approach utilizing
  existing operators via graph-level decomposition. We compare our method to prior
  work as well as the approach taken by the hls4ml framework. As an outlook, we demonstrate
  the prospects of using the multi-threshold representation during the training of
  a neural network as a form of quantization aware training.
source:
- arXiv
source_ids:
- arxiv:2610.21825
url: https://arxiv.org/abs/2610.21825
discovered_at: '2026-10-19'
tags: *id001
---

# Compiling Multi\-Threshold Operators for Quantized Non\-Monotonic and Fine\-Granular Activations in Custom\-Tailored DNN Accelerators

**Autores:** Christoph Berganski; Felix Jentzsch; Marco Platzner

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Aggressive quantization of neural networks can expose activation functions as bottlenecks for efficient hardware acceleration\. Implementing quantized activations as multi\-threshold operations has been shown to be a promising optimization, allowing for efficient hardware implementation of few\-bit activations\. However, current implementations are limited to monotonically increasing functions, quantization schemes with one\-dimensional \(per\-channel\) granularity and a small set of predefined activation\-quantizer combinations\. We formalize the multi\-threshold representation to extend it to non\-monotonic functions and fine\-granular parameters, i\.e\., multi\-dimensional thresholds\. For automated conversion of quantized function compositions into threshold representation, we propose a systematic approach via algebraic rules integrated into the ONNX\-based compiler infrastructure\. We experimentally validate our solution on a selection of monotonic and non\-monotonic functions by extending the binary search based multi\-threshold operator that is integrated into the FINN framework for end\-to\-end synthesis of custom\-tailored FPGA accelerators\. The cost of hardware support for non\-monotonicity and fine\-granularity is characterized in comparison to an alternative approach utilizing existing operators via graph\-level decomposition\. We compare our method to prior work as well as the approach taken by the hls4ml framework\. As an outlook, we demonstrate the prospects of using the multi\-threshold representation during the training of a neural network as a form of quantization aware training\.

[Consultar publicação](<https://arxiv.org/abs/2610.21825>)
