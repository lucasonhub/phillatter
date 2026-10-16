---
title: Enhancing the advection module performance in the EPICC-Model V1.6.0 via GPU-HADVPPM4HIP
  V1.0 coupling and GPU-optimized strategies
authors:
- Kai Cao
- Qizhong Wu
- Xiao Tang
- Jinxi Li
- Xueshun Chen
- Huan‐Sheng Chen
- Wending Wang
- Huangjian Wu
- Lei Kong
- Jie Li
- Jiang Zhu
- Zifa Wang
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.5194/gmd-19-9807-2026
abstract: 'Abstract. The rapid development of Graphics Processing Units (GPUs) has
  established new computational paradigms for enhancing air quality modeling efficiency.
  In this study, the heterogeneous-compute interface for portability (HIP) was implemented
  to parallel computing of the piecewise parabolic method (PPM) advection solver (HADVPPM)
  on China’s domestic GPU-like accelerators (GPU-HADVPPM4HIP V1.0). Computational
  performance was enhanced through three strategic optimizations: reducing the central
  processing unit (CPU) and GPU (CPU-GPU) data transfer frequency, thread-block coordinated
  indexing, and the Message Passing Interface and HIP (“MPI+HIP”) hybrid parallelization
  across heterogeneous computing clusters. Following validation of the GPU-HADVPPM4HIP
  V1.0 program’s offline computational consistency and the pollutant simulation performance
  of the Emission and atmospheric Processes Integrated and Coupled Community version
  1.0 (EPICC-Model V1.0) on the Earth System Numerical Simulation Facility (EarthLab),
  comprehensive performance testing was conducted. Offline benchmark results demonstrated
  that GPU-HADVPPM4HIP V1.0 achieved a maximum speedup of 556.5x on a domestic GPU-like
  accelerator with compiler optimization. Integration of GPU-HADVPPM4HIP V1.0 into
  EPICC-Model V1.0, combined with optimized CPU-GPU communication frequency and thread-block
  coordinated indexing strategies, yielded model-level computational efficiency improvements
  of 17.0x and 1.5x, respectively. At the module level, GPU-HADVPPM4HIP V1.0 exhibited
  a 39.3 % computational efficiency gain when accounting for CPU-GPU data transfer
  overhead, which escalated to 20.5x acceleration when excluding communication costs.
  This coupling establishes a foundational framework for adapting air quality models
  to China’s domestic GPU-like architectures and identifies critical optimization
  pathways. Moreover, the methodology provides essential technical support for achieving
  full-model GPU implementation of the EPICC-Model, addressing both current computational
  constraints and future demands for high-resolution air quality simulations.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W4414392340
url: https://doi.org/10.5194/gmd-19-9807-2026
discovered_at: '2026-10-16'
tags: *id001
---

# Enhancing the advection module performance in the EPICC\-Model V1\.6\.0 via GPU\-HADVPPM4HIP V1\.0 coupling and GPU\-optimized strategies

**Autores:** Kai Cao; Qizhong Wu; Xiao Tang; Jinxi Li; Xueshun Chen; Huan‐Sheng Chen; Wending Wang; Huangjian Wu; Lei Kong; Jie Li; Jiang Zhu; Zifa Wang

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Abstract\. The rapid development of Graphics Processing Units \(GPUs\) has established new computational paradigms for enhancing air quality modeling efficiency\. In this study, the heterogeneous\-compute interface for portability \(HIP\) was implemented to parallel computing of the piecewise parabolic method \(PPM\) advection solver \(HADVPPM\) on China’s domestic GPU\-like accelerators \(GPU\-HADVPPM4HIP V1\.0\)\. Computational performance was enhanced through three strategic optimizations: reducing the central processing unit \(CPU\) and GPU \(CPU\-GPU\) data transfer frequency, thread\-block coordinated indexing, and the Message Passing Interface and HIP \(“MPI\+HIP”\) hybrid parallelization across heterogeneous computing clusters\. Following validation of the GPU\-HADVPPM4HIP V1\.0 program’s offline computational consistency and the pollutant simulation performance of the Emission and atmospheric Processes Integrated and Coupled Community version 1\.0 \(EPICC\-Model V1\.0\) on the Earth System Numerical Simulation Facility \(EarthLab\), comprehensive performance testing was conducted\. Offline benchmark results demonstrated that GPU\-HADVPPM4HIP V1\.0 achieved a maximum speedup of 556\.5x on a domestic GPU\-like accelerator with compiler optimization\. Integration of GPU\-HADVPPM4HIP V1\.0 into EPICC\-Model V1\.0, combined with optimized CPU\-GPU communication frequency and thread\-block coordinated indexing strategies, yielded model\-level computational efficiency improvements of 17\.0x and 1\.5x, respectively\. At the module level, GPU\-HADVPPM4HIP V1\.0 exhibited a 39\.3 % computational efficiency gain when accounting for CPU\-GPU data transfer overhead, which escalated to 20\.5x acceleration when excluding communication costs\. This coupling establishes a foundational framework for adapting air quality models to China’s domestic GPU\-like architectures and identifies critical optimization pathways\. Moreover, the methodology provides essential technical support for achieving full\-model GPU implementation of the EPICC\-Model, addressing both current computational constraints and future demands for high\-resolution air quality simulations\.

[Consultar publicação](<https://doi.org/10.5194/gmd-19-9807-2026>)
