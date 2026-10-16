---
title: Efficient contextual partial monitoring with general function approximation
authors:
- Kapilan Balagopalan
- Hao Qin
- Kwang-Sung Jun
- Chicheng Zhang
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'We study finite stochastic partial monitoring (PM) games with side information,
  a paradigm of sequential learning with partial feedback. On each round $t \in [T]$,
  both player and environment observe a context and player chooses an action and environment
  simultaneously chooses an outcome. The player neither observes the outcome nor the
  loss; instead, they only observe a feedback symbol which is partially informative
  about the outcome. We utilize the Estimation-to-Decisions (E2D) meta-algorithm of
  Foster et al.(2021) to design E2D.PMSide, a computationally efficient framework
  for contextual partial monitoring, which uses an online regression oracle to efficiently
  estimate the outcome distributions based on historical (context, action, feedback
  symbol) tuples. Since the exploration rule given by the original E2D algorithm is
  intractable to compute, we propose two computationally efficient exploration rules
  that achieve optimal regret orders in $T$: in the globally observable setting, our
  exploration rule is based on $ε$-greedy, while in the locally observable setting,
  our exploration rule uses inverse gap weighting (Foster & Rakhlin, 2020), which
  was previously only known to be effective in the bandit setting. We show that a
  variant of E2D.PMSide named OE2D.PMSide can be combined with offline regression
  oracles to give an efficient algorithm with optimal regret when the contexts are
  drawn independently from a fixed distribution. We evaluate our algorithm on a synthetic
  label-efficient prediction game and an LLM routing task, in which a learner decides
  from prompt, uncertainty, and internal state features whether to escalate a query
  from a weak model to a strong one. We show that our method has superior performance
  to prior approaches.'
source:
- arXiv
source_ids:
- arxiv:2610.19804
url: https://arxiv.org/abs/2610.19804
discovered_at: '2026-10-16'
tags: *id001
---

# Efficient contextual partial monitoring with general function approximation

**Autores:** Kapilan Balagopalan; Hao Qin; Kwang\-Sung Jun; Chicheng Zhang

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

We study finite stochastic partial monitoring \(PM\) games with side information, a paradigm of sequential learning with partial feedback\. On each round $t \\in \[T\]$, both player and environment observe a context and player chooses an action and environment simultaneously chooses an outcome\. The player neither observes the outcome nor the loss; instead, they only observe a feedback symbol which is partially informative about the outcome\. We utilize the Estimation\-to\-Decisions \(E2D\) meta\-algorithm of Foster et al\.\(2021\) to design E2D\.PMSide, a computationally efficient framework for contextual partial monitoring, which uses an online regression oracle to efficiently estimate the outcome distributions based on historical \(context, action, feedback symbol\) tuples\. Since the exploration rule given by the original E2D algorithm is intractable to compute, we propose two computationally efficient exploration rules that achieve optimal regret orders in $T$: in the globally observable setting, our exploration rule is based on $ε$\-greedy, while in the locally observable setting, our exploration rule uses inverse gap weighting \(Foster &amp; Rakhlin, 2020\), which was previously only known to be effective in the bandit setting\. We show that a variant of E2D\.PMSide named OE2D\.PMSide can be combined with offline regression oracles to give an efficient algorithm with optimal regret when the contexts are drawn independently from a fixed distribution\. We evaluate our algorithm on a synthetic label\-efficient prediction game and an LLM routing task, in which a learner decides from prompt, uncertainty, and internal state features whether to escalate a query from a weak model to a strong one\. We show that our method has superior performance to prior approaches\.

[Consultar publicação](<https://arxiv.org/abs/2610.19804>)
