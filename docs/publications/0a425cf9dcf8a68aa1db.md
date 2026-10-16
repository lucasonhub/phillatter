---
title: Compute-optimal data scaling for neural surrogates via multi-fidelity training
authors:
- Paul Setinek
- Fabian Paischer
- Nils Thuerey
- Johannes Brandstetter
- Felix Koehler
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Neural surrogates for Partial Differential Equations (PDEs) are usually
  trained on synthetic data from numerical simulators. As models grow and scaling
  laws demand larger datasets, the cost of data generation often outweighs the training
  cost and becomes the bottleneck in the scaling quest. Unlike data in other domains,
  however, each PDE sample has a tunable cost that depends on its numerical fidelity,
  with the resulting cost-accuracy trade-off governed by known convergence rates.
  We exploit this property by formalizing neural surrogate training as a function
  of both data quantity and fidelity under a fixed data generation compute budget,
  treating fidelity as a fine-grained discrete spectrum rather than a binary distinction.
  Building on this, we show that multi-fidelity training enables Pareto-optimal error
  scaling against data generation compute. By using simulations at lower fidelities
  as an additional training signal, training on the optimal fidelity mixture matches
  the accuracy of high-fidelity-only training, with up to $6.3\times$ less data generation
  compute across our settings. We validate these findings across six PDE problems
  spanning structured grids and unstructured meshes, two distinct error sources (discretization
  and iterative-solver error), and four surrogate architectures, totaling over 7,000
  training runs.
source:
- arXiv
source_ids:
- arxiv:2610.17221
url: https://arxiv.org/abs/2610.17221
discovered_at: '2026-10-16'
tags: *id001
---

# Compute\-optimal data scaling for neural surrogates via multi\-fidelity training

**Autores:** Paul Setinek; Fabian Paischer; Nils Thuerey; Johannes Brandstetter; Felix Koehler

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Neural surrogates for Partial Differential Equations \(PDEs\) are usually trained on synthetic data from numerical simulators\. As models grow and scaling laws demand larger datasets, the cost of data generation often outweighs the training cost and becomes the bottleneck in the scaling quest\. Unlike data in other domains, however, each PDE sample has a tunable cost that depends on its numerical fidelity, with the resulting cost\-accuracy trade\-off governed by known convergence rates\. We exploit this property by formalizing neural surrogate training as a function of both data quantity and fidelity under a fixed data generation compute budget, treating fidelity as a fine\-grained discrete spectrum rather than a binary distinction\. Building on this, we show that multi\-fidelity training enables Pareto\-optimal error scaling against data generation compute\. By using simulations at lower fidelities as an additional training signal, training on the optimal fidelity mixture matches the accuracy of high\-fidelity\-only training, with up to $6\.3\\times$ less data generation compute across our settings\. We validate these findings across six PDE problems spanning structured grids and unstructured meshes, two distinct error sources \(discretization and iterative\-solver error\), and four surrogate architectures, totaling over 7,000 training runs\.

[Consultar publicação](<https://arxiv.org/abs/2610.17221>)
