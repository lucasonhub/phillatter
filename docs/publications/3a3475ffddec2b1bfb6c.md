---
title: 'KL Before and After Mixing: A Round-Complexity Separation in Parallel Sampling'
authors:
- Tianyi Wu
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: A parallel sampler can choose at random which coordinates to generate together.
  For a target $p$ and the output law $q_U$ of a schedule $U$ drawn afresh for each
  output, we compare the schedule-averaged divergence $\mathbb{E}_U D_{\mathrm{KL}}(p\|q_U)$
  with the output-law divergence $D_{\mathrm{KL}}(p\|\mathbb{E}_U q_U)$, in nats.
  Rounds commit independent draws from exact conditional marginals frozen at the round's
  start, each output's schedule is drawn before sampling from a finite mixture of
  schedules, and every scheduled round is charged. For the uniform distribution on
  binary strings of even length $n$ with $n/2$ ones, the least expected number of
  rounds at a fixed tolerance $\varepsilon>0$ is $Θ_\varepsilon((\log n)^2)$ under
  the first criterion but $(e^{-\varepsilon}+o(1))\log_2\ln n$ under the second, and
  the double-logarithmic order is attainable with the same round count on every run.
  For this target, a count-state recursion gives the exact least output divergence
  at every round cap over all causal randomized policies. The separation extends to
  weighted fixed-count targets with bounded weight ratios and quota fractions bounded
  away from zero and one, without permutation symmetry, and to the full-support Beta$(1,1)$--Bernoulli
  target, where the sharp expected cost under the output-law criterion is $(e^{-\varepsilon}/2+o(1))\log_2\log_2n$,
  attained with rare $n$-round runs. Prior work implies the order of the schedule-averaged
  cost on the balanced target and its $O_\varepsilon((\log n)^2)$ upper bounds on
  both extensions.
source:
- arXiv
source_ids:
- arxiv:2610.13924
url: https://arxiv.org/abs/2610.13924
discovered_at: '2026-10-16'
tags: *id001
---

# KL Before and After Mixing: A Round\-Complexity Separation in Parallel Sampling

**Autores:** Tianyi Wu

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

A parallel sampler can choose at random which coordinates to generate together\. For a target $p$ and the output law $q\_U$ of a schedule $U$ drawn afresh for each output, we compare the schedule\-averaged divergence $\\mathbb\{E\}\_U D\_\{\\mathrm\{KL\}\}\(p\\\|q\_U\)$ with the output\-law divergence $D\_\{\\mathrm\{KL\}\}\(p\\\|\\mathbb\{E\}\_U q\_U\)$, in nats\. Rounds commit independent draws from exact conditional marginals frozen at the round&\#x27;s start, each output&\#x27;s schedule is drawn before sampling from a finite mixture of schedules, and every scheduled round is charged\. For the uniform distribution on binary strings of even length $n$ with $n/2$ ones, the least expected number of rounds at a fixed tolerance $\\varepsilon&gt;0$ is $Θ\_\\varepsilon\(\(\\log n\)^2\)$ under the first criterion but $\(e^\{\-\\varepsilon\}\+o\(1\)\)\\log\_2\\ln n$ under the second, and the double\-logarithmic order is attainable with the same round count on every run\. For this target, a count\-state recursion gives the exact least output divergence at every round cap over all causal randomized policies\. The separation extends to weighted fixed\-count targets with bounded weight ratios and quota fractions bounded away from zero and one, without permutation symmetry, and to the full\-support Beta$\(1,1\)$\-\-Bernoulli target, where the sharp expected cost under the output\-law criterion is $\(e^\{\-\\varepsilon\}/2\+o\(1\)\)\\log\_2\\log\_2n$, attained with rare $n$\-round runs\. Prior work implies the order of the schedule\-averaged cost on the balanced target and its $O\_\\varepsilon\(\(\\log n\)^2\)$ upper bounds on both extensions\.

[Consultar publicação](<https://arxiv.org/abs/2610.13924>)
