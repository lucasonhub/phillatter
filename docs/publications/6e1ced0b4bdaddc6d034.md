---
title: 'Pretraining and Test-Time Training Budgets Matter for ARC: A Controlled Study
  of VARC and TRM'
authors:
- Adrien Deliege
- Marc Van Droogenbroeck
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: The Abstraction and Reasoning Corpus (ARC) is increasingly used to evaluate
  whether neural networks can infer task-specific transformations from few demonstrations.
  Recent ARC models differ in architecture, but also in broader training and evaluation
  protocols, including pretraining data, data augmentation, test-time setup, and optimization
  budgets, making conclusions about architecture benefits debatable. In this work,
  we study how the performance of the vision-inspired VARC and recursion-based TRM
  models is affected by pretraining and test-time training (TTT) budgets under a common
  inductive protocol on ARC-AGI-1. We cross five pretraining budgets with four TTT
  budgets for each test task. Each budget specifies a task-variant count and total
  sample presentations, defining the controlled training budgets. We observe that
  increasing TTT sample presentations improves the standard ARC pass@2 metric in all
  settings for both models. Increasing the TTT task-variant count consistently helps
  only TRM, whereas VARC often performs better with fewer variants. VARC also remains
  competitive without pretraining, while TRM benefits much more from it. These results
  show that pretraining and TTT budgets affect ARC evaluation and motivate reporting
  at comparable budgets.
source:
- arXiv
source_ids:
- arxiv:2610.13660
url: https://arxiv.org/abs/2610.13660
discovered_at: '2026-10-16'
tags: *id001
---

# Pretraining and Test\-Time Training Budgets Matter for ARC: A Controlled Study of VARC and TRM

**Autores:** Adrien Deliege; Marc Van Droogenbroeck

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

The Abstraction and Reasoning Corpus \(ARC\) is increasingly used to evaluate whether neural networks can infer task\-specific transformations from few demonstrations\. Recent ARC models differ in architecture, but also in broader training and evaluation protocols, including pretraining data, data augmentation, test\-time setup, and optimization budgets, making conclusions about architecture benefits debatable\. In this work, we study how the performance of the vision\-inspired VARC and recursion\-based TRM models is affected by pretraining and test\-time training \(TTT\) budgets under a common inductive protocol on ARC\-AGI\-1\. We cross five pretraining budgets with four TTT budgets for each test task\. Each budget specifies a task\-variant count and total sample presentations, defining the controlled training budgets\. We observe that increasing TTT sample presentations improves the standard ARC pass@2 metric in all settings for both models\. Increasing the TTT task\-variant count consistently helps only TRM, whereas VARC often performs better with fewer variants\. VARC also remains competitive without pretraining, while TRM benefits much more from it\. These results show that pretraining and TTT budgets affect ARC evaluation and motivate reporting at comparable budgets\.

[Consultar publicação](<https://arxiv.org/abs/2610.13660>)
