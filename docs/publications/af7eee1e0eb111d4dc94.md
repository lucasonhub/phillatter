---
title: Learning to Extrapolate in Depth with Looped Transformers
authors:
- Huitao Yang
- Jianhao Huang
- Zixuan Wang
- Baharan Mirzasoleiman
date: '2026-10-10'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Looped transformers reuse a single block across iterations, raising a natural
  question: how far can a block trained at one depth be safely extrapolated to greater
  depths? We study this question for all-pairs graph connectivity, where harder graphs
  require longer-range information propagation. We show that under exchangeability
  and symmetric positive initialization, population training at depth K converges
  to an update rule governed by a single effective parameter that balances graph propagation
  against fitting structure unresolved at training depth. This trade-off creates a
  finite extrapolation window: too few test-time loops provide insufficient propagation,
  while too many eventually create false connections. We derive explicit endpoints
  for this window and bound the graph hardness solvable beyond training as a function
  of training depth and hardness. In particular, a test depth chosen solely from the
  training distribution can guarantee recovery on substantially harder graphs, with
  a certified depth gain that grows exponentially as training depth outpaces training
  hardness. Experiments validate the predicted windows and show how compute budget
  and initialization affect the optimal training depth.'
source:
- arXiv
source_ids:
- arxiv:2610.14456
url: https://arxiv.org/abs/2610.14456
discovered_at: '2026-10-16'
tags: *id001
---

# Learning to Extrapolate in Depth with Looped Transformers

**Autores:** Huitao Yang; Jianhao Huang; Zixuan Wang; Baharan Mirzasoleiman

**Data:** 2026-10-10 · **Tipo:** preprint

## Resumo

Looped transformers reuse a single block across iterations, raising a natural question: how far can a block trained at one depth be safely extrapolated to greater depths? We study this question for all\-pairs graph connectivity, where harder graphs require longer\-range information propagation\. We show that under exchangeability and symmetric positive initialization, population training at depth K converges to an update rule governed by a single effective parameter that balances graph propagation against fitting structure unresolved at training depth\. This trade\-off creates a finite extrapolation window: too few test\-time loops provide insufficient propagation, while too many eventually create false connections\. We derive explicit endpoints for this window and bound the graph hardness solvable beyond training as a function of training depth and hardness\. In particular, a test depth chosen solely from the training distribution can guarantee recovery on substantially harder graphs, with a certified depth gain that grows exponentially as training depth outpaces training hardness\. Experiments validate the predicted windows and show how compute budget and initialization affect the optimal training depth\.

[Consultar publicação](<https://arxiv.org/abs/2610.14456>)
