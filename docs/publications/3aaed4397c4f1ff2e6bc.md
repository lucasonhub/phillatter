---
title: Bottlenecked semantic compression by representation reconstruction
authors:
- Xiaoya Tang
- Shilong Liu
- Daniel Smolyak
- Xiwen Li
- Quynh Nguyen
- Tolga Tasdizen
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Vision Transformers incur high computational costs when processing long
  visual token sequences. Existing reduction methods typically rank tokens independently
  and discard those deemed unimportant or redundant. We propose a reconstruction-guided
  framework for visual token condensation (ReConV), which summarizes the complete
  visual sequence with a compact Summary Bank (SMB) and retains tokens whose information
  is not adequately captured by the SMB, as indicated by their reconstruction residuals.
  At each compression layer, a lightweight position-conditioned decoder reconstructs
  the current tokens, leaving shared information compressed in the SMB while explicitly
  preserving poorly reconstructed details. Experiments on image classification and
  multimodal understanding demonstrate favorable performance-efficiency trade-offs:
  ReConV surpasses the uncompressed baseline with 48\% fewer GMACs on ImageNet and
  enables reusable image-level representations for efficient multi-turn inference.
  Code is available at TokenDrop.'
source:
- arXiv
source_ids:
- arxiv:2610.17412
url: https://arxiv.org/abs/2610.17412
discovered_at: '2026-10-16'
tags: *id001
---

# Bottlenecked semantic compression by representation reconstruction

**Autores:** Xiaoya Tang; Shilong Liu; Daniel Smolyak; Xiwen Li; Quynh Nguyen; Tolga Tasdizen

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Vision Transformers incur high computational costs when processing long visual token sequences\. Existing reduction methods typically rank tokens independently and discard those deemed unimportant or redundant\. We propose a reconstruction\-guided framework for visual token condensation \(ReConV\), which summarizes the complete visual sequence with a compact Summary Bank \(SMB\) and retains tokens whose information is not adequately captured by the SMB, as indicated by their reconstruction residuals\. At each compression layer, a lightweight position\-conditioned decoder reconstructs the current tokens, leaving shared information compressed in the SMB while explicitly preserving poorly reconstructed details\. Experiments on image classification and multimodal understanding demonstrate favorable performance\-efficiency trade\-offs: ReConV surpasses the uncompressed baseline with 48\\% fewer GMACs on ImageNet and enables reusable image\-level representations for efficient multi\-turn inference\. Code is available at TokenDrop\.

[Consultar publicação](<https://arxiv.org/abs/2610.17412>)
