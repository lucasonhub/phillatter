---
title: Mitigating Capability Degradation in LLM Self-Improvement via Representation
  Geometry Regularization
authors:
- Jiaqi Tian
- Ting Long
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'On-Policy Self-distillation is a self-improvement paradigm that enables
  large language models (LLMs) to improve their capabilities by leveraging the same
  model as both teacher and student under different conditioning contexts. However,
  we find that OPSD methods can progressively degrade previously acquired capabilities:
  queries that are correctly responded at earlier training stages may become incorrectly
  responded as optimization proceeds, even the overall performance continues to improve.
  Further analysis reveals that this degradation coincides with a deterioration of
  the geometry of hidden representations, characterized by reduced intra-cluster compactness
  and diminished inter-cluster separation. Motivated by this observation, we propose
  Representation Geometry Regularization (RGR), which preserves representation geometry
  during post-training by encouraging compactness within cluster and separation across
  cluster. RGR can be seamlessly integrated into existing OPSD methods without altering
  their core optimization procedures. Extensive experiments on multiple OPSD methods
  and benchmarks show that RGR generally alleviates capability degradation while retaining
  capability improvements. Our code is available in https://github.com/supermachinelearner/RGR.'
source:
- arXiv
source_ids:
- arxiv:2610.12855
url: https://arxiv.org/abs/2610.12855
discovered_at: '2026-10-16'
tags: *id001
---

# Mitigating Capability Degradation in LLM Self\-Improvement via Representation Geometry Regularization

**Autores:** Jiaqi Tian; Ting Long

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

On\-Policy Self\-distillation is a self\-improvement paradigm that enables large language models \(LLMs\) to improve their capabilities by leveraging the same model as both teacher and student under different conditioning contexts\. However, we find that OPSD methods can progressively degrade previously acquired capabilities: queries that are correctly responded at earlier training stages may become incorrectly responded as optimization proceeds, even the overall performance continues to improve\. Further analysis reveals that this degradation coincides with a deterioration of the geometry of hidden representations, characterized by reduced intra\-cluster compactness and diminished inter\-cluster separation\. Motivated by this observation, we propose Representation Geometry Regularization \(RGR\), which preserves representation geometry during post\-training by encouraging compactness within cluster and separation across cluster\. RGR can be seamlessly integrated into existing OPSD methods without altering their core optimization procedures\. Extensive experiments on multiple OPSD methods and benchmarks show that RGR generally alleviates capability degradation while retaining capability improvements\. Our code is available in https://github\.com/supermachinelearner/RGR\.

[Consultar publicação](<https://arxiv.org/abs/2610.12855>)
