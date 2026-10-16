---
title: 'Coarse-Graining Recursive Expert Computation: Continuation-Relative Interfaces
  and Failure Modes'
authors:
- Shihua Yu
- Yanzhi Wang
- Tianchi Chen
date: '2026-10-10'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Computational coarse-graining aims to replace a sequence of updates with
  a cheaper module while preserving task performance. We present a continuation-relative
  evaluation framework that assesses replacements through the computation that follows
  them, using downstream task quality and total execution cost as joint criteria.
  The framework distinguishes boundary representations, summaries of skipped computation,
  executed operations, and downstream loss. It makes interfaces and permitted deployment
  information explicit, combines fine-path references with directly trained controls
  using the same shortened architecture, and accounts for selection overhead. An exact
  loss decomposition separates replacement effects at a fixed downstream action from
  effects of changing that action. A finite construction shows how retained information
  can reduce the stipulated cost of zero-error prediction under fixed information
  and controller restrictions. Experiments in two frozen pretrained language models
  show that representation fidelity and task loss can favor different fitting objectives.
  In a prespecified comparison on a 1.7-billion-parameter model, next-token-loss training
  lowers in-distribution negative log-likelihood by 0.1901 nats per scored token compared
  with reconstructing the skipped blocks' output, using the same optimizer and update
  count. This ranking reverses in all nine paired comparisons under distribution shift.
  In a recursive expert prototype, the jointly adapted candidate lowers task error
  relative to frozen-bank and router-only baselines, but trails directly trained controls,
  and the tested input-only selectors fail the joint quality-cost criteria. Together,
  the protocol and studies provide explicit criteria and diagnostics for distinguishing
  useful computational replacement from local approximation gains within specified
  interfaces and evaluation settings.
source:
- arXiv
source_ids:
- arxiv:2610.14413
url: https://arxiv.org/abs/2610.14413
discovered_at: '2026-10-16'
tags: *id001
---

# Coarse\-Graining Recursive Expert Computation: Continuation\-Relative Interfaces and Failure Modes

**Autores:** Shihua Yu; Yanzhi Wang; Tianchi Chen

**Data:** 2026-10-10 · **Tipo:** preprint

## Resumo

Computational coarse\-graining aims to replace a sequence of updates with a cheaper module while preserving task performance\. We present a continuation\-relative evaluation framework that assesses replacements through the computation that follows them, using downstream task quality and total execution cost as joint criteria\. The framework distinguishes boundary representations, summaries of skipped computation, executed operations, and downstream loss\. It makes interfaces and permitted deployment information explicit, combines fine\-path references with directly trained controls using the same shortened architecture, and accounts for selection overhead\. An exact loss decomposition separates replacement effects at a fixed downstream action from effects of changing that action\. A finite construction shows how retained information can reduce the stipulated cost of zero\-error prediction under fixed information and controller restrictions\. Experiments in two frozen pretrained language models show that representation fidelity and task loss can favor different fitting objectives\. In a prespecified comparison on a 1\.7\-billion\-parameter model, next\-token\-loss training lowers in\-distribution negative log\-likelihood by 0\.1901 nats per scored token compared with reconstructing the skipped blocks&\#x27; output, using the same optimizer and update count\. This ranking reverses in all nine paired comparisons under distribution shift\. In a recursive expert prototype, the jointly adapted candidate lowers task error relative to frozen\-bank and router\-only baselines, but trails directly trained controls, and the tested input\-only selectors fail the joint quality\-cost criteria\. Together, the protocol and studies provide explicit criteria and diagnostics for distinguishing useful computational replacement from local approximation gains within specified interfaces and evaluation settings\.

[Consultar publicação](<https://arxiv.org/abs/2610.14413>)
