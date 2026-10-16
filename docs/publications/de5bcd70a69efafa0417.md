---
title: 'Neural Network Preconditioning: A Case Study for the Solution of the Parametric
  Helmholtz Equation'
authors:
- Luc Giraud
- Carola Kruse
- Paul Mycek
- Maksym Shpakovych
- Yanfei Xiang
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: 10.1002/nla.70123
abstract: This work presents a hybrid numerical approach for solving linear systems
  arising from the discretization of the two-dimensional parametric Helmholtz equation.
  A convolutional neural network based on the U-Net architecture is trained in an
  self-supervised manner (i.e., without explicitly generating reference solutions)
  to approximate the inverse of the discretized Helmholtz operator, using a loss function
  involving the residual norm of the linear system. The trained network is used as
  a nonlinear preconditioner within the flexible GMRES (FGMRES) algorithm. Numerical
  experiments show that while the neural network is not accurate enough to act as
  a standalone solver, it significantly improves the convergence of FGMRES when employed
  as a preconditioner. The neural preconditioner demonstrates robust performance and
  generalization capabilities with respect to variations in the velocity field and
  the domain size. Comparisons with algebraic preconditioners, based on LU factorizations
  of approximations of the original system matrices, indicate the superior efficiency
  of the neural approach under equivalent conditions. We believe that the proposed
  method is not tied to a specific neural architecture and can be extended to other
  parametric PDEs.
source:
- arXiv
source_ids:
- arxiv:2610.16542
url: https://arxiv.org/abs/2610.16542
discovered_at: '2026-10-16'
tags: *id001
---

# Neural Network Preconditioning: A Case Study for the Solution of the Parametric Helmholtz Equation

**Autores:** Luc Giraud; Carola Kruse; Paul Mycek; Maksym Shpakovych; Yanfei Xiang

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

This work presents a hybrid numerical approach for solving linear systems arising from the discretization of the two\-dimensional parametric Helmholtz equation\. A convolutional neural network based on the U\-Net architecture is trained in an self\-supervised manner \(i\.e\., without explicitly generating reference solutions\) to approximate the inverse of the discretized Helmholtz operator, using a loss function involving the residual norm of the linear system\. The trained network is used as a nonlinear preconditioner within the flexible GMRES \(FGMRES\) algorithm\. Numerical experiments show that while the neural network is not accurate enough to act as a standalone solver, it significantly improves the convergence of FGMRES when employed as a preconditioner\. The neural preconditioner demonstrates robust performance and generalization capabilities with respect to variations in the velocity field and the domain size\. Comparisons with algebraic preconditioners, based on LU factorizations of approximations of the original system matrices, indicate the superior efficiency of the neural approach under equivalent conditions\. We believe that the proposed method is not tied to a specific neural architecture and can be extended to other parametric PDEs\.

[Consultar publicação](<https://arxiv.org/abs/2610.16542>)
