---
title: Sequence-Structured Decision Learning for Branch-and-Bound in Mixed-Integer
  Linear Programming
authors:
- Tengfei Liu
- Jinrun Liu
- Bai Yan
- Yuhui Shi
- Qi Zhao
date: '2026-10-10'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Branch-and-bound (BnB) solves mixed-integer linear programs by constructing
  and exploring a search tree. Node selection and branching are two recurrent decisions
  that directly determine the tree. Learning-based approaches typically optimize either
  decision in isolation and condition on a mostly local view, leaving the coupled
  evolution of the search tree insufficiently modeled. This paper proposes Seq-BnB,
  a sequence-structured framework that learns branching and node selection from a
  shared global representation of the evolving BnB process. Seq-BnB serializes node
  creations, node updates, node-selection events, and branching events into typed
  tokens, producing a causal event sequence of the search trajectory. A self-attention
  encoder summarizes this global search history, a bipartite graph neural network
  encodes the current LP relaxation, and context-conditioned decision heads score
  branching variables and open nodes. To reduce distribution shift between expert
  demonstrations and learned policies, Seq-BnB is trained with DAgger-style data aggregation.
  On four MILP benchmark families, Seq-BnB consistently processes fewer BnB nodes
  than heuristic and learning-based baselines, with strong solution times on both
  standard and larger transfer instances. While this paper evaluates Seq-BnB instantiation
  for branching and node selection, it accommodates additional solver decisions, such
  as cut selection, by introducing new action tokens and decision heads.
source:
- arXiv
source_ids:
- arxiv:2610.14835
url: https://arxiv.org/abs/2610.14835
discovered_at: '2026-10-16'
tags: *id001
---

# Sequence\-Structured Decision Learning for Branch\-and\-Bound in Mixed\-Integer Linear Programming

**Autores:** Tengfei Liu; Jinrun Liu; Bai Yan; Yuhui Shi; Qi Zhao

**Data:** 2026-10-10 · **Tipo:** preprint

## Resumo

Branch\-and\-bound \(BnB\) solves mixed\-integer linear programs by constructing and exploring a search tree\. Node selection and branching are two recurrent decisions that directly determine the tree\. Learning\-based approaches typically optimize either decision in isolation and condition on a mostly local view, leaving the coupled evolution of the search tree insufficiently modeled\. This paper proposes Seq\-BnB, a sequence\-structured framework that learns branching and node selection from a shared global representation of the evolving BnB process\. Seq\-BnB serializes node creations, node updates, node\-selection events, and branching events into typed tokens, producing a causal event sequence of the search trajectory\. A self\-attention encoder summarizes this global search history, a bipartite graph neural network encodes the current LP relaxation, and context\-conditioned decision heads score branching variables and open nodes\. To reduce distribution shift between expert demonstrations and learned policies, Seq\-BnB is trained with DAgger\-style data aggregation\. On four MILP benchmark families, Seq\-BnB consistently processes fewer BnB nodes than heuristic and learning\-based baselines, with strong solution times on both standard and larger transfer instances\. While this paper evaluates Seq\-BnB instantiation for branching and node selection, it accommodates additional solver decisions, such as cut selection, by introducing new action tokens and decision heads\.

[Consultar publicação](<https://arxiv.org/abs/2610.14835>)
