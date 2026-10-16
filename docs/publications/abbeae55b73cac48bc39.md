---
title: Building AI–Physics Digital Twins for Hurricanes With FourCastNet v2 and ERF
authors:
- Mahesh Natarajan
- Aaron M. Lattanzi
- Ann Almgren
- Jean Sexton
- Weiqun Zhang
- Travis Allen O'Brien
- William D. Collins
date: '2026-10-12'
type: article
category: &id001
- Inteligência Artificial
doi: 10.5281/zenodo.23327490
abstract: Abstract While purely physical numerical weather models are computationally
  expensive, pure artificial intelligence (AI) models often struggle to respect physical
  conservation laws and accurately capture localized extreme events, such as rapid
  hurricane intensification. To address this challenge, we present a research software
  workflow that enables a hybrid AI–physics digital twin architecture, combining the
  execution speed of deep learning with the physical rigor of high-resolution numerical
  solvers. Our workflow utilizes global weather reanalysis data (GDAS) as initial
  conditions to drive the ECMWF-FourCastNet v2 machine learning framework. FourCastNet
  v2 rapidly generates multi-day forecast trajectories, providing time-dependent boundary
  conditions to force the Energy Research and Forecasting (ERF) model–an open-source
  atmospheric solver built on the exascale AMReX framework. Using an 8 km horizontal
  resolution mesh with 42 million cells, ERF computes internal convective fluid dynamics,
  employing Smagorinsky turbulence, Kessler microphysics, and bulk surface parameterizations.
  We evaluate this framework on a 3-day tracking case study of Hurricane Laura (August
  2020) executed across 16 NVIDIA A100 GPUs on NERSC’s Perlmutter supercomputer, completing
  in 1.5 hours. While both AI-only and hybrid approaches accurately constrain storm
  trajectory within the NOAA track forecast cone, AI-only predictions severely underestimate
  storm intensification. Conversely, the hybrid AI–physics framework reasonably reproduces
  the rapid intensification phase, reaching maximum wind speeds of ~120 knots, broadly
  consistent with IBTrACS observations. This work highlights the power of coupling
  AI boundary forcing with exascale physics solvers for high-fidelity extreme weather
  forecasting. Keywords Digital Twins, AI–Physics, Hurricanes, GDAS, IBTrACS, FourCastNet
  v2, ERF, AMReX
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221765136
url: https://doi.org/10.5281/zenodo.23327490
discovered_at: '2026-10-16'
tags: *id001
---

# Building AI–Physics Digital Twins for Hurricanes With FourCastNet v2 and ERF

**Autores:** Mahesh Natarajan; Aaron M\. Lattanzi; Ann Almgren; Jean Sexton; Weiqun Zhang; Travis Allen O&\#x27;Brien; William D\. Collins

**Data:** 2026-10-12 · **Tipo:** article

## Resumo

Abstract While purely physical numerical weather models are computationally expensive, pure artificial intelligence \(AI\) models often struggle to respect physical conservation laws and accurately capture localized extreme events, such as rapid hurricane intensification\. To address this challenge, we present a research software workflow that enables a hybrid AI–physics digital twin architecture, combining the execution speed of deep learning with the physical rigor of high\-resolution numerical solvers\. Our workflow utilizes global weather reanalysis data \(GDAS\) as initial conditions to drive the ECMWF\-FourCastNet v2 machine learning framework\. FourCastNet v2 rapidly generates multi\-day forecast trajectories, providing time\-dependent boundary conditions to force the Energy Research and Forecasting \(ERF\) model–an open\-source atmospheric solver built on the exascale AMReX framework\. Using an 8 km horizontal resolution mesh with 42 million cells, ERF computes internal convective fluid dynamics, employing Smagorinsky turbulence, Kessler microphysics, and bulk surface parameterizations\. We evaluate this framework on a 3\-day tracking case study of Hurricane Laura \(August 2020\) executed across 16 NVIDIA A100 GPUs on NERSC’s Perlmutter supercomputer, completing in 1\.5 hours\. While both AI\-only and hybrid approaches accurately constrain storm trajectory within the NOAA track forecast cone, AI\-only predictions severely underestimate storm intensification\. Conversely, the hybrid AI–physics framework reasonably reproduces the rapid intensification phase, reaching maximum wind speeds of \~120 knots, broadly consistent with IBTrACS observations\. This work highlights the power of coupling AI boundary forcing with exascale physics solvers for high\-fidelity extreme weather forecasting\. Keywords Digital Twins, AI–Physics, Hurricanes, GDAS, IBTrACS, FourCastNet v2, ERF, AMReX

[Consultar publicação](<https://doi.org/10.5281/zenodo.23327490>)
