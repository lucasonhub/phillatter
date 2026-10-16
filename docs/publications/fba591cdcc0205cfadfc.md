---
title: 'ProtModernBERT: Compute-Efficient Protein Language Modeling'
authors:
- Alberto Martínez
- Natalia Flechas Manrique
- Llorenç Espinosa-Portalés
- Luc Andrea
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Large protein language models provide a powerful framework for learning
  sequence-function relationships and guiding experimental design. However, architectural
  improvements are underexplored, especially in low-compute regimes of relevance for
  resource-constrained research laboratories. We show that the training cost for encoder-only
  transformer architectures can be reduced by leveraging modern architectural refinements,
  offering an encouraging performance / compute-efficiency trade-off. We introduce
  ProtModernBERT, a modernized BERT-style model pre-trained on amino acid sequences,
  and compare it with ProtBert, Amplify, and ESM2 across a set of supervised structural
  tasks -encompassing secondary structure prediction, disorder prediction, and subcellular
  localization- and ProteinGym's zero-shot functional benchmark. We find that ProtModernBERT
  matches or closely tracks the performance of Amplify-120M and ProtBert with up to
  80-90\% reduction in pre-training FLOPs, and narrows the gap to ESM2 when controlling
  for pre-training. Our analysis using a cluster-based validation protocol for hyperparameter
  selection and randomly initialized models disentangles the contributions of architecture
  and data, showing that modern components provide stronger inductive biases that
  are more consequential than parameter count in low-compute regimes.
source:
- arXiv
source_ids:
- arxiv:2610.19738
url: https://arxiv.org/abs/2610.19738
discovered_at: '2026-10-16'
tags: *id001
---

# ProtModernBERT: Compute\-Efficient Protein Language Modeling

**Autores:** Alberto Martínez; Natalia Flechas Manrique; Llorenç Espinosa\-Portalés; Luc Andrea

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Large protein language models provide a powerful framework for learning sequence\-function relationships and guiding experimental design\. However, architectural improvements are underexplored, especially in low\-compute regimes of relevance for resource\-constrained research laboratories\. We show that the training cost for encoder\-only transformer architectures can be reduced by leveraging modern architectural refinements, offering an encouraging performance / compute\-efficiency trade\-off\. We introduce ProtModernBERT, a modernized BERT\-style model pre\-trained on amino acid sequences, and compare it with ProtBert, Amplify, and ESM2 across a set of supervised structural tasks \-encompassing secondary structure prediction, disorder prediction, and subcellular localization\- and ProteinGym&\#x27;s zero\-shot functional benchmark\. We find that ProtModernBERT matches or closely tracks the performance of Amplify\-120M and ProtBert with up to 80\-90\\% reduction in pre\-training FLOPs, and narrows the gap to ESM2 when controlling for pre\-training\. Our analysis using a cluster\-based validation protocol for hyperparameter selection and randomly initialized models disentangles the contributions of architecture and data, showing that modern components provide stronger inductive biases that are more consequential than parameter count in low\-compute regimes\.

[Consultar publicação](<https://arxiv.org/abs/2610.19738>)
