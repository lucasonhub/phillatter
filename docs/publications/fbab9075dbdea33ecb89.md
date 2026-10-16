---
title: Dissecting the Carbon-SLO Tension in Geo-Distributed LLM Serving
authors:
- Burak Topcu
- Musa Cim
- Zuhal Ozturk
- Mahmut Taylan Kandemir
date: '2026-10-10'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Large Language Model (LLM) inference is driving a growing share of datacenter
  carbon emissions. Although carbon-aware scheduling can reduce these emissions in
  geo-distributed datacenters by exploiting the spatiotemporal variations in grid
  carbon intensity, the latency-sensitive nature of LLM serving constrains this design
  space. While prior studies investigate the carbon savings achievable through spatial
  scheduling, they oversimplify the dynamics of modern inference engines, such as
  queueing and continuous batching, which strongly shape inference latency. We address
  this issue by designing and evaluating a latency-centric, geo-distributed inference
  simulator, calibrated with hardware-grounded latency and power measurements, that
  reproduces these dynamics and enables the study of carbon savings under strict service-level
  objectives (SLOs). We then formulate a series of SLO- and carbon-aware schedulers
  of increasing sophistication, from per-request heuristics to batch-level optimization:
  (i) a greedy heuristic, (ii) an integer linear programming (ILP)-based scheduler
  jointly assigning batches of requests, (iii) an iterative ILP-based solution projecting
  its own assignments back into the load estimates to capture load coupling, and (iv)
  a facility mixed-integer linear programming (MILP) scheduler pricing the energy
  of batched requests collectively rather than in isolation. Across three LLMs under
  MLPerf SLOs and varying system loads, the MILP-based option offers the best carbon-SLO
  balance, reducing carbon emissions by up to 60% relative to the round-robin policy,
  with an average SLO violation of 3%. Our characterization further shows that savings
  grow with the spread of carbon intensity across datacenters and shrink as system
  load increases, while SLO attainment depends on how frequently schedulers receive
  datacenters'' load updates.'
source:
- arXiv
source_ids:
- arxiv:2610.14571
url: https://arxiv.org/abs/2610.14571
discovered_at: '2026-10-16'
tags: *id001
---

# Dissecting the Carbon\-SLO Tension in Geo\-Distributed LLM Serving

**Autores:** Burak Topcu; Musa Cim; Zuhal Ozturk; Mahmut Taylan Kandemir

**Data:** 2026-10-10 · **Tipo:** preprint

## Resumo

Large Language Model \(LLM\) inference is driving a growing share of datacenter carbon emissions\. Although carbon\-aware scheduling can reduce these emissions in geo\-distributed datacenters by exploiting the spatiotemporal variations in grid carbon intensity, the latency\-sensitive nature of LLM serving constrains this design space\. While prior studies investigate the carbon savings achievable through spatial scheduling, they oversimplify the dynamics of modern inference engines, such as queueing and continuous batching, which strongly shape inference latency\. We address this issue by designing and evaluating a latency\-centric, geo\-distributed inference simulator, calibrated with hardware\-grounded latency and power measurements, that reproduces these dynamics and enables the study of carbon savings under strict service\-level objectives \(SLOs\)\. We then formulate a series of SLO\- and carbon\-aware schedulers of increasing sophistication, from per\-request heuristics to batch\-level optimization: \(i\) a greedy heuristic, \(ii\) an integer linear programming \(ILP\)\-based scheduler jointly assigning batches of requests, \(iii\) an iterative ILP\-based solution projecting its own assignments back into the load estimates to capture load coupling, and \(iv\) a facility mixed\-integer linear programming \(MILP\) scheduler pricing the energy of batched requests collectively rather than in isolation\. Across three LLMs under MLPerf SLOs and varying system loads, the MILP\-based option offers the best carbon\-SLO balance, reducing carbon emissions by up to 60% relative to the round\-robin policy, with an average SLO violation of 3%\. Our characterization further shows that savings grow with the spread of carbon intensity across datacenters and shrink as system load increases, while SLO attainment depends on how frequently schedulers receive datacenters&\#x27; load updates\.

[Consultar publicação](<https://arxiv.org/abs/2610.14571>)
