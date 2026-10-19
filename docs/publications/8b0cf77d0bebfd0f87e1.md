---
title: Plug-and-play predictive energy management for fuel-efficient platooning of
  gasoline-powered autonomous vehicles
authors:
- Behrouz Samieiyan
- Anjali Awasthi
date: '2026-10-14'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1007/s44465-026-00052-x
abstract: In this paper, we present a plug-and-play predictive energy management framework
  for fuel-efficient platooning of gasoline-powered autonomous vehicles. Unlike existing
  approaches that target electric or hybrid drivetrains, the proposed architecture
  addresses the nonlinear thermodynamic and aerodynamic challenges inherent to internal
  combustion engine (ICE) vehicles. The framework integrates an Adaptive Neuro-Fuzzy
  Inference System optimized via Teaching-Learning-Based Optimization (ANFIS-TLBO)
  with Model Predictive Control (MPC) and a Quantum-inspired Long Short-Term Memory
  (QLSTM) network that broadcasts a 10-second leader state prediction horizon to all
  follower vehicles simultaneously. A cooperative power-sharing mechanism and a predictive
  gap policy are superimposed as a lightweight supervisory layer that leaves the internal
  structure and parameters of each local controller entirely unchanged, modifying
  only its reference inputs (predicted leader trajectory, desired gap, and coordinated
  fuel-cut activation). The framework is validated across four standardized driving
  cycles, HWFET, US06, Artemis HW130, and Artemis HW150, in both 4-vehicle and 6-vehicle
  homogeneous platoon configurations, each subjected to 20 statistically independent
  runs incorporating stochastic wind (Weibull) and road grade (Rayleigh) disturbances.
  Under the HWFET cycle, the proposed method achieves an average per-vehicle fuel
  consumption of 6.64 L/100 km (4-vehicle platoon) and 6.61 L/100 km (6-vehicle platoon),
  outperforming all benchmarks including Adaptive MAB, Pure ANFIS, Pure MPC, and Pure
  TLBO. NOx emission reduction rates from leader to last follower reach 5.74% and
  6.23% in the respective configurations, the highest recorded across all methods,
  reflecting a trade-off in which the leader operates at a higher absolute NOx level
  to sustain tighter velocity tracking, while followers benefit disproportionately
  from predictive power management. The plug-and-play architecture is validated on
  a 6-vehicle platoon with zero controller retuning, confirming scalability across
  platoon sizes without local-controller modification.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221803843
url: https://doi.org/10.1007/s44465-026-00052-x
discovered_at: '2026-10-19'
tags: *id001
---

# Plug\-and\-play predictive energy management for fuel\-efficient platooning of gasoline\-powered autonomous vehicles

**Autores:** Behrouz Samieiyan; Anjali Awasthi

**Data:** 2026-10-14 · **Tipo:** article

## Resumo

In this paper, we present a plug\-and\-play predictive energy management framework for fuel\-efficient platooning of gasoline\-powered autonomous vehicles\. Unlike existing approaches that target electric or hybrid drivetrains, the proposed architecture addresses the nonlinear thermodynamic and aerodynamic challenges inherent to internal combustion engine \(ICE\) vehicles\. The framework integrates an Adaptive Neuro\-Fuzzy Inference System optimized via Teaching\-Learning\-Based Optimization \(ANFIS\-TLBO\) with Model Predictive Control \(MPC\) and a Quantum\-inspired Long Short\-Term Memory \(QLSTM\) network that broadcasts a 10\-second leader state prediction horizon to all follower vehicles simultaneously\. A cooperative power\-sharing mechanism and a predictive gap policy are superimposed as a lightweight supervisory layer that leaves the internal structure and parameters of each local controller entirely unchanged, modifying only its reference inputs \(predicted leader trajectory, desired gap, and coordinated fuel\-cut activation\)\. The framework is validated across four standardized driving cycles, HWFET, US06, Artemis HW130, and Artemis HW150, in both 4\-vehicle and 6\-vehicle homogeneous platoon configurations, each subjected to 20 statistically independent runs incorporating stochastic wind \(Weibull\) and road grade \(Rayleigh\) disturbances\. Under the HWFET cycle, the proposed method achieves an average per\-vehicle fuel consumption of 6\.64 L/100 km \(4\-vehicle platoon\) and 6\.61 L/100 km \(6\-vehicle platoon\), outperforming all benchmarks including Adaptive MAB, Pure ANFIS, Pure MPC, and Pure TLBO\. NOx emission reduction rates from leader to last follower reach 5\.74% and 6\.23% in the respective configurations, the highest recorded across all methods, reflecting a trade\-off in which the leader operates at a higher absolute NOx level to sustain tighter velocity tracking, while followers benefit disproportionately from predictive power management\. The plug\-and\-play architecture is validated on a 6\-vehicle platoon with zero controller retuning, confirming scalability across platoon sizes without local\-controller modification\.

[Consultar publicação](<https://doi.org/10.1007/s44465-026-00052-x>)
