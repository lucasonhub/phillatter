---
title: Dimension-Optimal Dynamic Regret in Exp-Concave Online Learning
authors:
- Yanyi Li
- Wendao Wu
- Haihan Zhang
- Qinshi Wang
- Chenheng Zhang
- Chunyuan Zheng
- Cong Fang
- Haoxuan Li
- Zhouchen Lin
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Tracking changing comparators is a central problem in online learning. For
  exp-concave losses, previous work established the $T^{1/3}P_T^{2/3}$ dependence
  on the horizon $T$ and Euclidean path length $P_T$ for fixed dimension, while the
  optimal cost of dimension remained unresolved. We resolve this question by establishing
  a sharp $d^{1/3}$ curved dimension factor, improving the $d^{2/3}$ factor of recent
  switching and interval reductions [1, 2]. To achieve this improvement, we develop
  a proper, full-information learner on compact convex subsets of $\mathbb{R}^d$ that
  adapts to the unknown path length and, under fixed dimension-independent diameter,
  gradient, and curvature parameters, guarantees $$\operatorname{Reg}_T(u_{1:T}) \le
  \widetilde{O}\left(d+\min\left\{d^{1/3}T^{1/3}P_T^{2/3},\sqrt{TP_T},T\right\}\right).$$
  A matching lower bound on a diameter-one Euclidean ball establishes the minimax
  frontier up to logarithmic factors when $T\gtrsim d^2$, including the transition
  from the curved rate to larger path budgets. The lower bound already holds for losses
  that depend on only one coordinate per round, isolating an unavoidable cost of learning
  across directions. Our upper bound follows from square-root Gaussian KL control
  of comparator movement and a cancellation argument that pays for history restarts.
  The curved learner maintains $O(\log^2 T)$ Gaussian states, uses one gradient per
  round, and runs in time near-linear in $T$ under a Mahalanobis-projection oracle.
source:
- arXiv
source_ids:
- arxiv:2610.20187
url: https://arxiv.org/abs/2610.20187
discovered_at: '2026-10-16'
tags: *id001
---

# Dimension\-Optimal Dynamic Regret in Exp\-Concave Online Learning

**Autores:** Yanyi Li; Wendao Wu; Haihan Zhang; Qinshi Wang; Chenheng Zhang; Chunyuan Zheng; Cong Fang; Haoxuan Li; Zhouchen Lin

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Tracking changing comparators is a central problem in online learning\. For exp\-concave losses, previous work established the $T^\{1/3\}P\_T^\{2/3\}$ dependence on the horizon $T$ and Euclidean path length $P\_T$ for fixed dimension, while the optimal cost of dimension remained unresolved\. We resolve this question by establishing a sharp $d^\{1/3\}$ curved dimension factor, improving the $d^\{2/3\}$ factor of recent switching and interval reductions \[1, 2\]\. To achieve this improvement, we develop a proper, full\-information learner on compact convex subsets of $\\mathbb\{R\}^d$ that adapts to the unknown path length and, under fixed dimension\-independent diameter, gradient, and curvature parameters, guarantees $$\\operatorname\{Reg\}\_T\(u\_\{1:T\}\) \\le \\widetilde\{O\}\\left\(d\+\\min\\left\\\{d^\{1/3\}T^\{1/3\}P\_T^\{2/3\},\\sqrt\{TP\_T\},T\\right\\\}\\right\)\.$$ A matching lower bound on a diameter\-one Euclidean ball establishes the minimax frontier up to logarithmic factors when $T\\gtrsim d^2$, including the transition from the curved rate to larger path budgets\. The lower bound already holds for losses that depend on only one coordinate per round, isolating an unavoidable cost of learning across directions\. Our upper bound follows from square\-root Gaussian KL control of comparator movement and a cancellation argument that pays for history restarts\. The curved learner maintains $O\(\\log^2 T\)$ Gaussian states, uses one gradient per round, and runs in time near\-linear in $T$ under a Mahalanobis\-projection oracle\.

[Consultar publicação](<https://arxiv.org/abs/2610.20187>)
