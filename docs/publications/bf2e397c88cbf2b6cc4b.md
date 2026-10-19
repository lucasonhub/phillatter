---
title: A decomposable branch-and-price formulation for optimal classification trees
authors:
- Elif Rana Yöner
- Taghi Khaniyev
- Özlem Karsu
date: '2026-10-16'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1007/s12532-026-00343-0
abstract: Abstract In this study, we focus on finding exact binary optimal classification
  trees (OCTs) via mixed-integer (linear) programs (MIP). To alleviate the scalability
  issues of existing MIP-based OCT formulations, we propose a novel decomposable model
  that treats each leaf of the classification tree as a decision rule. The model exploits
  the order-independent nature of decision rules to reduce the problem size and the
  solution space, and lends itself to a Dantzig–Wolfe (extended) reformulation. We
  then implement a tailored branch-and-price solution with pricing subproblems designated
  for each leaf solved in parallel. We identify the conditions under which the extended
  formulation performs better in order to form a hybrid algorithm, OrderIndependentOCT,
  that decides when to invoke branch-and-price. On 18 benchmark datasets, OrderIndependentOCT
  proves optimality on $$71.1\%$$ 71.1 % of instances within a one-hour time limit,
  compared to $$60.0\%$$ 60.0 % for the well-known Benders decomposition approach
  (BendersOCT). In cases where neither method attains optimality, OrderIndependentOCT
  yields higher (or the same) training accuracy than BendersOCT in $$50.68\%$$ 50.68
  % (resp. $$71.23\%$$ 71.23 % ) of the instances. Similarly, in $$86.3\%$$ 86.3 %
  of all instances, OrderIndependentOCT matches or exceeds BendersOCT’s out-of-sample
  accuracy. These findings illustrate the efficiency of the proposed decomposition
  approach for the optimal classification tree training problem compared to the state-of-the-art.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222553071
url: https://doi.org/10.1007/s12532-026-00343-0
discovered_at: '2026-10-19'
tags: *id001
---

# A decomposable branch\-and\-price formulation for optimal classification trees

**Autores:** Elif Rana Yöner; Taghi Khaniyev; Özlem Karsu

**Data:** 2026-10-16 · **Tipo:** article

## Resumo

Abstract In this study, we focus on finding exact binary optimal classification trees \(OCTs\) via mixed\-integer \(linear\) programs \(MIP\)\. To alleviate the scalability issues of existing MIP\-based OCT formulations, we propose a novel decomposable model that treats each leaf of the classification tree as a decision rule\. The model exploits the order\-independent nature of decision rules to reduce the problem size and the solution space, and lends itself to a Dantzig–Wolfe \(extended\) reformulation\. We then implement a tailored branch\-and\-price solution with pricing subproblems designated for each leaf solved in parallel\. We identify the conditions under which the extended formulation performs better in order to form a hybrid algorithm, OrderIndependentOCT, that decides when to invoke branch\-and\-price\. On 18 benchmark datasets, OrderIndependentOCT proves optimality on $$71\.1\\%$$ 71\.1 % of instances within a one\-hour time limit, compared to $$60\.0\\%$$ 60\.0 % for the well\-known Benders decomposition approach \(BendersOCT\)\. In cases where neither method attains optimality, OrderIndependentOCT yields higher \(or the same\) training accuracy than BendersOCT in $$50\.68\\%$$ 50\.68 % \(resp\. $$71\.23\\%$$ 71\.23 % \) of the instances\. Similarly, in $$86\.3\\%$$ 86\.3 % of all instances, OrderIndependentOCT matches or exceeds BendersOCT’s out\-of\-sample accuracy\. These findings illustrate the efficiency of the proposed decomposition approach for the optimal classification tree training problem compared to the state\-of\-the\-art\.

[Consultar publicação](<https://doi.org/10.1007/s12532-026-00343-0>)
