---
title: Robustly Reliable Learning for Regression
authors:
- Avrim Blum
- Anh Tuan Nguyen
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: We introduce the problem of robustly reliable learning for the regression
  setting in adversarial environments. Given a test point $x_{test}$, a training dataset
  $S$ of $n$ data points, a corruption budget $b \ll n$, and a real-valued hypothesis
  class $\mathcal H$, our goal is to output the optimal prediction range $I^*_{x_{test}}(S,
  b)$, such that any $L$-Lipschitz predictor consistent with all but at most $b$ points
  in $S$ must predict a value $h(x_{test}) \in I$. We then instantiate the analysis
  for $L$-Lipschitz hypothesis classes, a natural and widely studied class in the
  regression setting, focusing on two key scenarios. First, for the restricted case
  where the corrupted dataset is guaranteed to be $L$-Lipschitz consistent, we propose
  a simple and efficient $b^{th}$-best heuristic algorithm and prove its correctness
  in computing the tightest possible range $I^*_{x_{test}}(S, b)$. We then establish
  its computational complexity of $O(n)$ and show that it is computationally optimal
  in this scenario. Building on this foundation, we address the general scenario where
  the dataset $S$ is no longer $L$-Lipschitz consistent. We demonstrate that computing
  the optimal range in this setting reduces to analyzing a violation graph, which
  models the pairwise $L$-Lipschitz violations among data points. By leveraging the
  structural properties of this graph's kernel, we propose a Fixed-Parameter Tractable
  (FPT) algorithm that computes the exact optimal range in $O(n^2 + b^4)$ time. Furthermore,
  under the Strong Exponential Time Hypothesis (SETH), we establish a computational
  lower bound of $Ω(n^{2 - o(1)})$, proving that our algorithm is computationally
  optimal. Finally, we discuss open directions for the problem of robustly reliable
  learning for regression.
source:
- arXiv
source_ids:
- arxiv:2610.17381
url: https://arxiv.org/abs/2610.17381
discovered_at: '2026-10-16'
tags: *id001
---

# Robustly Reliable Learning for Regression

**Autores:** Avrim Blum; Anh Tuan Nguyen

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

We introduce the problem of robustly reliable learning for the regression setting in adversarial environments\. Given a test point $x\_\{test\}$, a training dataset $S$ of $n$ data points, a corruption budget $b \\ll n$, and a real\-valued hypothesis class $\\mathcal H$, our goal is to output the optimal prediction range $I^\*\_\{x\_\{test\}\}\(S, b\)$, such that any $L$\-Lipschitz predictor consistent with all but at most $b$ points in $S$ must predict a value $h\(x\_\{test\}\) \\in I$\. We then instantiate the analysis for $L$\-Lipschitz hypothesis classes, a natural and widely studied class in the regression setting, focusing on two key scenarios\. First, for the restricted case where the corrupted dataset is guaranteed to be $L$\-Lipschitz consistent, we propose a simple and efficient $b^\{th\}$\-best heuristic algorithm and prove its correctness in computing the tightest possible range $I^\*\_\{x\_\{test\}\}\(S, b\)$\. We then establish its computational complexity of $O\(n\)$ and show that it is computationally optimal in this scenario\. Building on this foundation, we address the general scenario where the dataset $S$ is no longer $L$\-Lipschitz consistent\. We demonstrate that computing the optimal range in this setting reduces to analyzing a violation graph, which models the pairwise $L$\-Lipschitz violations among data points\. By leveraging the structural properties of this graph&\#x27;s kernel, we propose a Fixed\-Parameter Tractable \(FPT\) algorithm that computes the exact optimal range in $O\(n^2 \+ b^4\)$ time\. Furthermore, under the Strong Exponential Time Hypothesis \(SETH\), we establish a computational lower bound of $Ω\(n^\{2 \- o\(1\)\}\)$, proving that our algorithm is computationally optimal\. Finally, we discuss open directions for the problem of robustly reliable learning for regression\.

[Consultar publicação](<https://arxiv.org/abs/2610.17381>)
