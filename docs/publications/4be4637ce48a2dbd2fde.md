---
title: Convergence Rates of Gaussian Process Thompson Sampling for Efficient Global
  Optimization
authors:
- Haowei Wang
- Yilin Zheng
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Efficient global optimization aims to identify a global optimum of an expensive
  black-box function within a limited evaluation budget $N$. We investigate the convergence
  rates of Gaussian process Thompson sampling (GP-TS) under noiseless observations,
  assuming a fixed objective function in a reproducing kernel Hilbert space (RKHS).
  For Matérn kernels with smoothness parameter $ν$ in dimension $d$, we establish
  a worst-case expected simple-regret upper bound of $O(N^{-ν/d}\sqrt{\log N})$ for
  both discrete GP-TS on sufficiently fine grids and its continuous counterpart. For
  the continuous implementation, we develop a nested-grid argument to control posterior
  sample paths over the entire domain. We further establish matching lower bounds
  of $Ω(N^{-5/2}\sqrt{\log N})$ for both implementations under a fixed one-dimensional
  Matérn-$5/2$ kernel, demonstrating that the logarithmic penalty is intrinsic to
  standard GP-TS in this setting. Motivated by this limitation, we propose Gaussian
  Process Capped Thompson Sampling (GP-CTS), which caps posterior sample paths using
  a valid RKHS norm upper bound while preserving optimism. This modification successfully
  eliminates the logarithmic penalty and achieves the minimax-optimal rate $Θ(N^{-ν/d})$
  for both discrete and continuous implementations.
source:
- arXiv
source_ids:
- arxiv:2610.19925
url: https://arxiv.org/abs/2610.19925
discovered_at: '2026-10-16'
tags: *id001
---

# Convergence Rates of Gaussian Process Thompson Sampling for Efficient Global Optimization

**Autores:** Haowei Wang; Yilin Zheng

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Efficient global optimization aims to identify a global optimum of an expensive black\-box function within a limited evaluation budget $N$\. We investigate the convergence rates of Gaussian process Thompson sampling \(GP\-TS\) under noiseless observations, assuming a fixed objective function in a reproducing kernel Hilbert space \(RKHS\)\. For Matérn kernels with smoothness parameter $ν$ in dimension $d$, we establish a worst\-case expected simple\-regret upper bound of $O\(N^\{\-ν/d\}\\sqrt\{\\log N\}\)$ for both discrete GP\-TS on sufficiently fine grids and its continuous counterpart\. For the continuous implementation, we develop a nested\-grid argument to control posterior sample paths over the entire domain\. We further establish matching lower bounds of $Ω\(N^\{\-5/2\}\\sqrt\{\\log N\}\)$ for both implementations under a fixed one\-dimensional Matérn\-$5/2$ kernel, demonstrating that the logarithmic penalty is intrinsic to standard GP\-TS in this setting\. Motivated by this limitation, we propose Gaussian Process Capped Thompson Sampling \(GP\-CTS\), which caps posterior sample paths using a valid RKHS norm upper bound while preserving optimism\. This modification successfully eliminates the logarithmic penalty and achieves the minimax\-optimal rate $Θ\(N^\{\-ν/d\}\)$ for both discrete and continuous implementations\.

[Consultar publicação](<https://arxiv.org/abs/2610.19925>)
