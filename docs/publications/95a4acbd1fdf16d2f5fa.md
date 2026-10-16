---
title: 'Confine to the Task, Anchor the Rest: Concept-Guided Retention Regularizer
  for Parameter-Efficient Fine-Tuning'
authors:
- Ibna Kowsar
- Ivan Medri
- Fanyu Meng
- Xin Liu
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Parameter-efficient fine-tuning (PEFT) has been widely used, yet the adapted
  model suffers catastrophic forgetting of pre-trained knowledge. While most existing
  work hardens the adapter by constraining where the weight update may lie, we note
  that constraining this weight channel does not constrain the activation channel.
  In this paper, we propose Concept-Guided Retention (CGR), a plug-and-play regularizer
  that constrains both for any PEFT base. CGR reads a frozen sparse autoencoder (SAE)
  and treats two disjoint concept sets differently. It softly confines the update
  to the task-concept subspace (via weight channel), and anchors a selected set of
  general-purpose concepts to the frozen model (via activation channel). We also provide
  anchor value bounds based on weight updates to understand how they interact, and
  show that both terms are necessary. On a CLIP vision panel, CGR significantly improves
  retention at comparable accuracy for every base, and the same pattern holds for
  world-knowledge retention under Llama-3.1-8B instruction tuning. Because the protected
  directions are named SAE concepts, CGR remains inspectable and controllable.
source:
- arXiv
source_ids:
- arxiv:2610.17713
url: https://arxiv.org/abs/2610.17713
discovered_at: '2026-10-16'
tags: *id001
---

# Confine to the Task, Anchor the Rest: Concept\-Guided Retention Regularizer for Parameter\-Efficient Fine\-Tuning

**Autores:** Ibna Kowsar; Ivan Medri; Fanyu Meng; Xin Liu

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Parameter\-efficient fine\-tuning \(PEFT\) has been widely used, yet the adapted model suffers catastrophic forgetting of pre\-trained knowledge\. While most existing work hardens the adapter by constraining where the weight update may lie, we note that constraining this weight channel does not constrain the activation channel\. In this paper, we propose Concept\-Guided Retention \(CGR\), a plug\-and\-play regularizer that constrains both for any PEFT base\. CGR reads a frozen sparse autoencoder \(SAE\) and treats two disjoint concept sets differently\. It softly confines the update to the task\-concept subspace \(via weight channel\), and anchors a selected set of general\-purpose concepts to the frozen model \(via activation channel\)\. We also provide anchor value bounds based on weight updates to understand how they interact, and show that both terms are necessary\. On a CLIP vision panel, CGR significantly improves retention at comparable accuracy for every base, and the same pattern holds for world\-knowledge retention under Llama\-3\.1\-8B instruction tuning\. Because the protected directions are named SAE concepts, CGR remains inspectable and controllable\.

[Consultar publicação](<https://arxiv.org/abs/2610.17713>)
