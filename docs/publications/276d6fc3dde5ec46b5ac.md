---
title: 'V-SHARE: Provable Convergence Guarantees for Advantage-based Algorithms'
authors:
- Kintan Saha
- Hamed Masoudi
- Xinyi Sheng
- Dominik Baumann
- Joni Pajarinen
- Arsenii Mustafin
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: In reinforcement learning, advantage-based value-learning methods, unlike
  standard Q-learning, share information across actions by decomposing the action-value
  function into a state-dependent value component and action-specific advantages.
  While this mechanism has proven effective in both tabular and deep reinforcement
  learning, its theoretical understanding remains incomplete. We introduce V-SHARE,
  an advantage-based value-learning algorithm that combines cross-action value sharing
  with an importance-weighted Bellman-residual correction. To our knowledge, we provide
  the first complete theoretical characterization of an advantage-based algorithm,
  including both asymptotic convergence and non-asymptotic finite-sample guarantees.
  We identify a regime in which V-SHARE mitigates the rare-action bottleneck of asynchronous
  Q-learning and uncover a contraction--variance tradeoff between stronger deterministic
  contraction and increased importance-weighting noise. Motivated by this tradeoff,
  we develop decreasing residual-preconditioning schedules that combine faster early
  contraction with lower asymptotic noise. We further develop a two-timescale analysis
  that removes the single-timescale residual-weight threshold while preserving convergence
  guarantees. Experiments on discrete Markov decision processes (MDPs) and deep reinforcement-learning
  benchmarks corroborate our results.
source:
- arXiv
source_ids:
- arxiv:2610.21448
url: https://arxiv.org/abs/2610.21448
discovered_at: '2026-10-16'
tags: *id001
---

# V\-SHARE: Provable Convergence Guarantees for Advantage\-based Algorithms

**Autores:** Kintan Saha; Hamed Masoudi; Xinyi Sheng; Dominik Baumann; Joni Pajarinen; Arsenii Mustafin

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

In reinforcement learning, advantage\-based value\-learning methods, unlike standard Q\-learning, share information across actions by decomposing the action\-value function into a state\-dependent value component and action\-specific advantages\. While this mechanism has proven effective in both tabular and deep reinforcement learning, its theoretical understanding remains incomplete\. We introduce V\-SHARE, an advantage\-based value\-learning algorithm that combines cross\-action value sharing with an importance\-weighted Bellman\-residual correction\. To our knowledge, we provide the first complete theoretical characterization of an advantage\-based algorithm, including both asymptotic convergence and non\-asymptotic finite\-sample guarantees\. We identify a regime in which V\-SHARE mitigates the rare\-action bottleneck of asynchronous Q\-learning and uncover a contraction\-\-variance tradeoff between stronger deterministic contraction and increased importance\-weighting noise\. Motivated by this tradeoff, we develop decreasing residual\-preconditioning schedules that combine faster early contraction with lower asymptotic noise\. We further develop a two\-timescale analysis that removes the single\-timescale residual\-weight threshold while preserving convergence guarantees\. Experiments on discrete Markov decision processes \(MDPs\) and deep reinforcement\-learning benchmarks corroborate our results\.

[Consultar publicação](<https://arxiv.org/abs/2610.21448>)
