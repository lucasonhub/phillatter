---
title: One-Step Prediction Fidelity Is a Poor Proxy for Planning Performance in JEPA
  World Models
authors:
- Joshua Cheung
- Zhang He
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Latent world models are routinely selected, checkpointed and ablated on
  one-step prediction loss, on the assumption that a model which predicts the next
  latent better is a better model. In model-based RL this assumption is known to be
  unreliable; we ask whether it also fails for latent world models, where the training
  target is the model''s own embedding and the loss is not expressed in interpretable
  units. We introduce a frozen-decoder protocol reporting one-step error in physical
  units, decomposed into the part already present in the encoder''s representation
  and the part the predictor adds. Applying it to a recent end-to-end JEPA world model
  across three continuous-control environments, we move the metric by fine-tuning
  and measure goal-conditioned planning on the same checkpoints, with three training
  seeds and paired planning seeds throughout. Within one environment, a per-epoch
  ladder shows the relationship saturating after a single epoch: the first epoch improves
  fidelity by 32% and planning by 4.4 pp, but across the fifteen checkpoints that
  follow -- a further 15% fidelity improvement, monotone in every training seed --
  the correlation between one-step error and planning success is r = -0.010. This
  is not a task-ceiling artifact: stratifying by a model-independent measure of training-data
  support, planning in the lowest-support stratum starts at 80%, leaving ample headroom,
  and is nonetheless flat from epoch 1 onward. Across environments the exchange rate
  is equally unstable: a 93% fidelity reduction on TwoRoom yields -0.7 pp of planning,
  while a 40% reduction on PushT yields +4.9 pp [+1.1, +8.9]. All results replicate
  under a decoder-free measure, latent drift. We also show that a matched continued-training
  control absorbs the entire fidelity gain we had attributed to an auxiliary objective.'
source:
- arXiv
source_ids:
- arxiv:2610.19375
url: https://arxiv.org/abs/2610.19375
discovered_at: '2026-10-16'
tags: *id001
---

# One\-Step Prediction Fidelity Is a Poor Proxy for Planning Performance in JEPA World Models

**Autores:** Joshua Cheung; Zhang He

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Latent world models are routinely selected, checkpointed and ablated on one\-step prediction loss, on the assumption that a model which predicts the next latent better is a better model\. In model\-based RL this assumption is known to be unreliable; we ask whether it also fails for latent world models, where the training target is the model&\#x27;s own embedding and the loss is not expressed in interpretable units\. We introduce a frozen\-decoder protocol reporting one\-step error in physical units, decomposed into the part already present in the encoder&\#x27;s representation and the part the predictor adds\. Applying it to a recent end\-to\-end JEPA world model across three continuous\-control environments, we move the metric by fine\-tuning and measure goal\-conditioned planning on the same checkpoints, with three training seeds and paired planning seeds throughout\. Within one environment, a per\-epoch ladder shows the relationship saturating after a single epoch: the first epoch improves fidelity by 32% and planning by 4\.4 pp, but across the fifteen checkpoints that follow \-\- a further 15% fidelity improvement, monotone in every training seed \-\- the correlation between one\-step error and planning success is r = \-0\.010\. This is not a task\-ceiling artifact: stratifying by a model\-independent measure of training\-data support, planning in the lowest\-support stratum starts at 80%, leaving ample headroom, and is nonetheless flat from epoch 1 onward\. Across environments the exchange rate is equally unstable: a 93% fidelity reduction on TwoRoom yields \-0\.7 pp of planning, while a 40% reduction on PushT yields \+4\.9 pp \[\+1\.1, \+8\.9\]\. All results replicate under a decoder\-free measure, latent drift\. We also show that a matched continued\-training control absorbs the entire fidelity gain we had attributed to an auxiliary objective\.

[Consultar publicação](<https://arxiv.org/abs/2610.19375>)
