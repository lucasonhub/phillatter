---
title: Global-in-time Spectral Duhamel-Picard Method for Post-Exposure Bake Simulation
  and Physics-Informed Neural Operators for EUV Lithography
authors:
- Doyun Kim
- Mircea Dusa
- Werner Gilijns
- Philippe Leray
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: We present a global-in-time spectral Duhamel-Picard method with polynomial
  expansions for post-exposure bake (PEB) simulation. The coupled acid-quencher reaction-diffusion
  equations are reformulated as nonlinear Volterra integral equations using the Duhamel
  principle. Full trajectories are represented by finite polynomial expansions, with
  temporal coefficient fields determined over the bake interval by Anderson-accelerated
  Picard iteration, thereby avoiding sequential time marching. In 3-D PEB simulations,
  we employ Chebyshev and Legendre temporal bases while evaluating the Duhamel integrals
  using the corresponding Gaussian quadrature rules. We demonstrate that the proposed
  method simulates a large domain of $1200\times1200\times100$ voxels on the order
  of one minute. The representation is further incorporated into a physics-informed
  neural operator (PINO) with a mixed-transform variant of a factorized Fourier neural
  operator, which is trained without precomputed solution trajectories. Together,
  the integral formulation and its PINO extension enable accelerated, time-marching-free
  prediction of concentration fields at arbitrary times within the bake interval.
source:
- arXiv
source_ids:
- arxiv:2610.20655
url: https://arxiv.org/abs/2610.20655
discovered_at: '2026-10-16'
tags: *id001
---

# Global\-in\-time Spectral Duhamel\-Picard Method for Post\-Exposure Bake Simulation and Physics\-Informed Neural Operators for EUV Lithography

**Autores:** Doyun Kim; Mircea Dusa; Werner Gilijns; Philippe Leray

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

We present a global\-in\-time spectral Duhamel\-Picard method with polynomial expansions for post\-exposure bake \(PEB\) simulation\. The coupled acid\-quencher reaction\-diffusion equations are reformulated as nonlinear Volterra integral equations using the Duhamel principle\. Full trajectories are represented by finite polynomial expansions, with temporal coefficient fields determined over the bake interval by Anderson\-accelerated Picard iteration, thereby avoiding sequential time marching\. In 3\-D PEB simulations, we employ Chebyshev and Legendre temporal bases while evaluating the Duhamel integrals using the corresponding Gaussian quadrature rules\. We demonstrate that the proposed method simulates a large domain of $1200\\times1200\\times100$ voxels on the order of one minute\. The representation is further incorporated into a physics\-informed neural operator \(PINO\) with a mixed\-transform variant of a factorized Fourier neural operator, which is trained without precomputed solution trajectories\. Together, the integral formulation and its PINO extension enable accelerated, time\-marching\-free prediction of concentration fields at arbitrary times within the bake interval\.

[Consultar publicação](<https://arxiv.org/abs/2610.20655>)
