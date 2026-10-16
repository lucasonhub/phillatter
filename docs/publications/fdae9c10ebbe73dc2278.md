---
title: A convex-Feynman hybrid optimization paradigm for energy-efficient scheduling
  in large-scale multi-tier cloud data centers
authors:
- Fen Wang
- Jiajun Li
- Jing Wu
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1007/s10791-026-10589-w
abstract: To address the non-convex optimization and combinatorial explosion problems
  caused by mixed integer nonlinear programming in energy-aware scheduling of large-scale
  multi-layer cloud data centers, this paper proposes a hybrid optimization method
  (CFHO) that integrates convex optimization and Feynman path integral theory. This
  method consists of three core modules. (1) Convex relaxation module. This module
  uses Lagrangian relaxation to convert integer variables into continuous variables,
  combines second-order cone programming (SOCP) to convexify the non-convex AC power
  flow model, and uses semi-definite programming (SDP) to obtain the global lower
  bound of the original problem. (2) Feynman path integral modeling module. This module
  models the evolution of data center energy consumption as a weighted superposition
  of all possible scheduling paths, constructs a path integral model using the energy
  action, and adjusts the weight distribution of different paths through temperature
  parameters. (3) Hybrid optimization solution module. This module generates representative
  scheduling paths using importance sampling and ensures the convergence of the path
  distribution to the Boltzmann distribution through the Metropolis–Hastings sampling
  mechanism. At the same time, it constructs convex optimization sub-problems for
  continuous variables for each path and solves them using the primal-dual interior
  point method, while dynamically updating the path weights based on an exponential
  weighting strategy. This operation enables the collaborative solution of discrete
  decisions and continuous optimization. The experimental platform consists of 30
  physical servers, Cisco backbone and access switches, and Huawei precision air conditioners,
  and is built based on CloudSim Plus to create a simulation environment scalable
  to 500 physical nodes and 2000 virtual machines. The experiments use real datasets
  such as Alibaba 2022, Google Borg 2019, and self-built trading load, and are verified
  in different task loads and cooling disturbance scenarios. The experimental results
  show that in the 200-node standard load scenario, the average total energy consumption
  of CFHO is 47,982.3 kWh, which is 17.87% lower than the First-Fit and wolf optimization
  algorithms, and 7.98% lower than the latter. The PUE drops to 1.551, the energy
  efficiency reaches 173.6 tasks/kWh, with a mean 25.77% reduction in cooling energy
  consumption. The task deadline satisfaction rate reaches 97.84%, the high-priority
  task guarantee rate reaches 98.67%, and the p99 delay is reduced by 31.3% in average.
  In extreme cooling failure conditions, the temperature over-limit time is shortened
  from 187 minutes to 31 minutes. As the task arrival rate increases from 200 to 1800
  tasks/s, the energy-saving rate of CFHO increases from 14.76% to 22.47% in average,
  and the energy consumption growth remains approximately linear. Ablation experiments
  further verify that the three key mechanisms of path integral modeling, importance
  sampling, and dynamic weight update all have significant contributions to the overall
  performance; when the server scale expands to 500 nodes, the energy-saving advantage
  of CFHO over the particle swarm algorithm further increases to 13.70% in average,
  indicating that this method has good scalability and stability.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221077073
url: https://doi.org/10.1007/s10791-026-10589-w
discovered_at: '2026-10-16'
tags: *id001
---

# A convex\-Feynman hybrid optimization paradigm for energy\-efficient scheduling in large\-scale multi\-tier cloud data centers

**Autores:** Fen Wang; Jiajun Li; Jing Wu

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

To address the non\-convex optimization and combinatorial explosion problems caused by mixed integer nonlinear programming in energy\-aware scheduling of large\-scale multi\-layer cloud data centers, this paper proposes a hybrid optimization method \(CFHO\) that integrates convex optimization and Feynman path integral theory\. This method consists of three core modules\. \(1\) Convex relaxation module\. This module uses Lagrangian relaxation to convert integer variables into continuous variables, combines second\-order cone programming \(SOCP\) to convexify the non\-convex AC power flow model, and uses semi\-definite programming \(SDP\) to obtain the global lower bound of the original problem\. \(2\) Feynman path integral modeling module\. This module models the evolution of data center energy consumption as a weighted superposition of all possible scheduling paths, constructs a path integral model using the energy action, and adjusts the weight distribution of different paths through temperature parameters\. \(3\) Hybrid optimization solution module\. This module generates representative scheduling paths using importance sampling and ensures the convergence of the path distribution to the Boltzmann distribution through the Metropolis–Hastings sampling mechanism\. At the same time, it constructs convex optimization sub\-problems for continuous variables for each path and solves them using the primal\-dual interior point method, while dynamically updating the path weights based on an exponential weighting strategy\. This operation enables the collaborative solution of discrete decisions and continuous optimization\. The experimental platform consists of 30 physical servers, Cisco backbone and access switches, and Huawei precision air conditioners, and is built based on CloudSim Plus to create a simulation environment scalable to 500 physical nodes and 2000 virtual machines\. The experiments use real datasets such as Alibaba 2022, Google Borg 2019, and self\-built trading load, and are verified in different task loads and cooling disturbance scenarios\. The experimental results show that in the 200\-node standard load scenario, the average total energy consumption of CFHO is 47,982\.3 kWh, which is 17\.87% lower than the First\-Fit and wolf optimization algorithms, and 7\.98% lower than the latter\. The PUE drops to 1\.551, the energy efficiency reaches 173\.6 tasks/kWh, with a mean 25\.77% reduction in cooling energy consumption\. The task deadline satisfaction rate reaches 97\.84%, the high\-priority task guarantee rate reaches 98\.67%, and the p99 delay is reduced by 31\.3% in average\. In extreme cooling failure conditions, the temperature over\-limit time is shortened from 187 minutes to 31 minutes\. As the task arrival rate increases from 200 to 1800 tasks/s, the energy\-saving rate of CFHO increases from 14\.76% to 22\.47% in average, and the energy consumption growth remains approximately linear\. Ablation experiments further verify that the three key mechanisms of path integral modeling, importance sampling, and dynamic weight update all have significant contributions to the overall performance; when the server scale expands to 500 nodes, the energy\-saving advantage of CFHO over the particle swarm algorithm further increases to 13\.70% in average, indicating that this method has good scalability and stability\.

[Consultar publicação](<https://doi.org/10.1007/s10791-026-10589-w>)
