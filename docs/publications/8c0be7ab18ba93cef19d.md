---
title: Counterfactual Certification for Sequential Unlearning with Long-Run Performance
  Guarantees
authors:
- Hanna Benarroch
- Jamal Atif
- Olivier Cappé
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Certified machine unlearning ensures the proximity between the unlearned
  model and a model retrained without the data to be forgotten. Extending this framework
  to sequential deletion requests, typically arriving as groups of variable size (e.g.,
  all records of one user or of coordinated users), is challenging. For unlearning
  methods based on fine-tuning on the retain sets, this leads to either degrading
  performance or increasing computation as the number of unlearning requests grows.
  For independent successive requests, we instead certify each model release against
  a counterfactual unlearning trajectory in which the group being deleted never took
  part. With a fixed fine-tuning budget per deletion, we show that, for smooth strongly
  convex objectives, this approach keeps the performance loss bounded, uniformly in
  the number of requests. Experiments with multiclass logistic regression on FEMNIST
  show that the resulting algorithm needs fewer corrective steps than existing sequential
  methods and outperforms training-time differential privacy, particularly when group
  sizes are heterogeneous.
source:
- arXiv
source_ids:
- arxiv:2610.17993
url: https://arxiv.org/abs/2610.17993
discovered_at: '2026-10-16'
tags: *id001
---

# Counterfactual Certification for Sequential Unlearning with Long\-Run Performance Guarantees

**Autores:** Hanna Benarroch; Jamal Atif; Olivier Cappé

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Certified machine unlearning ensures the proximity between the unlearned model and a model retrained without the data to be forgotten\. Extending this framework to sequential deletion requests, typically arriving as groups of variable size \(e\.g\., all records of one user or of coordinated users\), is challenging\. For unlearning methods based on fine\-tuning on the retain sets, this leads to either degrading performance or increasing computation as the number of unlearning requests grows\. For independent successive requests, we instead certify each model release against a counterfactual unlearning trajectory in which the group being deleted never took part\. With a fixed fine\-tuning budget per deletion, we show that, for smooth strongly convex objectives, this approach keeps the performance loss bounded, uniformly in the number of requests\. Experiments with multiclass logistic regression on FEMNIST show that the resulting algorithm needs fewer corrective steps than existing sequential methods and outperforms training\-time differential privacy, particularly when group sizes are heterogeneous\.

[Consultar publicação](<https://arxiv.org/abs/2610.17993>)
