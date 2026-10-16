---
title: Your Transformer Is Secretly Elastic
authors:
- Walter Simoncini
- Dheeraj Varghese
- Gertjan J. Burghouts
- Cees G. M. Snoek
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Scaling up transformers has produced models with broad capabilities, deployed
  across heterogeneous hardware and fluctuating workloads. Yet, model families offer
  only a few fixed sizes (e.g., S, B, L), forcing users to commit to a model based
  on hardware and latency constraints. This rigidity is often suboptimal under varying
  query loads. We introduce a retraining-free method that elastifies pre-trained transformers
  into a single model that adapts on-the-fly across a continuum of computational budgets.
  Our key contribution is a differentiable relaxation of the functional unit-ranking
  problem: unlike prior work, which optimizes a single importance weight per MLP block
  or attention head, we rank every individual MLP neuron and attention head jointly,
  on a common scale, by minimizing the model''s loss under soft pruning across many
  sparsity targets, all at once. Across 27 vision and text transformer encoders ranging
  from 22M to 8B parameters, our method yields smooth degradation up to 60% sparsity
  and outperforms one-shot baselines under deep pruning. For example, pruning DINOv3
  ViT-H+/16 to 50% sparsity removes 427M parameters while reducing ImageNet-1k linear-probing
  accuracy by only 0.8%, without the need for weight correction or retraining. At
  60% sparsity, a pruned AugReg ViT-B/16 model achieves up to $1.80\times$ higher
  throughput and $1.26\times$ lower single-query latency on an A100 GPU. Elastic models
  are produced in minutes, with construction time scaling sub-linearly with parameter
  count.'
source:
- arXiv
source_ids:
- arxiv:2610.20588
url: https://arxiv.org/abs/2610.20588
discovered_at: '2026-10-16'
tags: *id001
---

# Your Transformer Is Secretly Elastic

**Autores:** Walter Simoncini; Dheeraj Varghese; Gertjan J\. Burghouts; Cees G\. M\. Snoek

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Scaling up transformers has produced models with broad capabilities, deployed across heterogeneous hardware and fluctuating workloads\. Yet, model families offer only a few fixed sizes \(e\.g\., S, B, L\), forcing users to commit to a model based on hardware and latency constraints\. This rigidity is often suboptimal under varying query loads\. We introduce a retraining\-free method that elastifies pre\-trained transformers into a single model that adapts on\-the\-fly across a continuum of computational budgets\. Our key contribution is a differentiable relaxation of the functional unit\-ranking problem: unlike prior work, which optimizes a single importance weight per MLP block or attention head, we rank every individual MLP neuron and attention head jointly, on a common scale, by minimizing the model&\#x27;s loss under soft pruning across many sparsity targets, all at once\. Across 27 vision and text transformer encoders ranging from 22M to 8B parameters, our method yields smooth degradation up to 60% sparsity and outperforms one\-shot baselines under deep pruning\. For example, pruning DINOv3 ViT\-H\+/16 to 50% sparsity removes 427M parameters while reducing ImageNet\-1k linear\-probing accuracy by only 0\.8%, without the need for weight correction or retraining\. At 60% sparsity, a pruned AugReg ViT\-B/16 model achieves up to $1\.80\\times$ higher throughput and $1\.26\\times$ lower single\-query latency on an A100 GPU\. Elastic models are produced in minutes, with construction time scaling sub\-linearly with parameter count\.

[Consultar publicação](<https://arxiv.org/abs/2610.20588>)
