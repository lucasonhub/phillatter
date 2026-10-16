---
title: 'NucleoNet: A Nuclear-Aware Determinant Ansatz for Multi-Geometry Neural Variational
  Monte Carlo'
authors:
- Qiao Gao
- Yang Huang
- Enze Hou
- Yuzhi Liu
- Jingrun Chen
- Han Wang
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Neural-network variational Monte Carlo provides an accurate route to solving
  the electronic Schrödinger equation, but many neural wavefunctions are optimized
  for a single nuclear geometry, requiring separate calculations to map out a potential
  energy surface. We introduce NucleoNet, a nuclear-aware determinant ansatz in which
  electrons and nuclei form a unified particle set propagated through a shared electron--nucleus
  backbone that jointly evolves one-particle and two-particle representations. Nuclei
  carry learned representations that evolve alongside the electronic representations
  and condition orbital construction, while antisymmetry is imposed only by electronic
  determinants. On equilibrium small-molecule benchmarks, NucleoNet achieves accuracy
  comparable to established neural-wavefunction baselines with substantially fewer
  parameters. For each molecular system, a single model optimized jointly across geometries
  describes the N$_2$ dissociation curve, Li displacement in LiCN, and the ethane
  and formamide minimum-energy paths for bond dissociation. Sparse-geometry training
  generalizes to unseen geometries for N$_2$ and LiCN without further optimization,
  and N$_2$ ablations show that nuclear streams substantially improve this interpolation.
  These results show that a compact wavefunction with jointly evolved nuclear representations
  can describe the geometries of a molecular system with a single set of parameters.
source:
- arXiv
source_ids:
- arxiv:2610.12985
url: https://arxiv.org/abs/2610.12985
discovered_at: '2026-10-16'
tags: *id001
---

# NucleoNet: A Nuclear\-Aware Determinant Ansatz for Multi\-Geometry Neural Variational Monte Carlo

**Autores:** Qiao Gao; Yang Huang; Enze Hou; Yuzhi Liu; Jingrun Chen; Han Wang

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Neural\-network variational Monte Carlo provides an accurate route to solving the electronic Schrödinger equation, but many neural wavefunctions are optimized for a single nuclear geometry, requiring separate calculations to map out a potential energy surface\. We introduce NucleoNet, a nuclear\-aware determinant ansatz in which electrons and nuclei form a unified particle set propagated through a shared electron\-\-nucleus backbone that jointly evolves one\-particle and two\-particle representations\. Nuclei carry learned representations that evolve alongside the electronic representations and condition orbital construction, while antisymmetry is imposed only by electronic determinants\. On equilibrium small\-molecule benchmarks, NucleoNet achieves accuracy comparable to established neural\-wavefunction baselines with substantially fewer parameters\. For each molecular system, a single model optimized jointly across geometries describes the N$\_2$ dissociation curve, Li displacement in LiCN, and the ethane and formamide minimum\-energy paths for bond dissociation\. Sparse\-geometry training generalizes to unseen geometries for N$\_2$ and LiCN without further optimization, and N$\_2$ ablations show that nuclear streams substantially improve this interpolation\. These results show that a compact wavefunction with jointly evolved nuclear representations can describe the geometries of a molecular system with a single set of parameters\.

[Consultar publicação](<https://arxiv.org/abs/2610.12985>)
