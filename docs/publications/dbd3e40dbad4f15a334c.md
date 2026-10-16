---
title: Distributed Multi-Agent Soft Actor–Critic for Cross-Link Interference Mitigation
  in Dynamic SBFD–TDD Configuration for 6G Networks
authors:
- Budiman Budiman
- Mudrik Alaydrus
date: '2026-10-10'
type: article
category: &id001
- Inteligência Artificial
doi: 10.58344/locus.v5i10.6323
abstract: This paper presents a distributed Multi-Agent Soft Actor-Critic (MASAC)
  framework based on Centralized Training and Decentralized Execution (CTDE) for adaptive
  Subband Full Duplex (SBFD)–TDD frame selection in interference-coupled multicell
  networks. The study is motivated by the need to increase uplink transmission opportunities
  in 5G-Advanced and 6G systems while managing the trade-offs among downlink performance,
  fairness, congestion, self-interference, and cross-link interference (CLI). A system-level
  simulator is developed incorporating traffic-buffer dynamics, discrete frame-selection
  actions, queue-based latency proxies, and interference-sensitive service-rate abstractions
  over a 21-cell 3GPP Urban Macro layout. The proposed method is evaluated against
  static, heuristic, and centralized global SAC baselines and is further examined
  through an ablation study comparing MASAC without information exchange (MASAC-noIE)
  and MASAC with lightweight intercell information exchange (MASAC-IE). The results
  demonstrate stable training under a fixed training budget and load-dependent coordination
  behavior. At a moderate load of 0.50, MASAC-IE improves uplink throughput by 34.9%
  and reduces the 95th-percentile queue length by 87% compared with MASAC-noIE, narrowing
  the performance gap relative to the centralized upper bound to 4.7%. Under heavy-load
  conditions, however, the same information-exchange mechanism induces overly conservative
  coordination, increasing CLI to 0.714 and degrading throughput. These findings indicate
  that CLI mitigation remains primarily a reward-design challenge rather than an inherent
  architectural limitation of distributed multi-agent learning.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221470785
url: https://doi.org/10.58344/locus.v5i10.6323
discovered_at: '2026-10-16'
tags: *id001
---

# Distributed Multi\-Agent Soft Actor–Critic for Cross\-Link Interference Mitigation in Dynamic SBFD–TDD Configuration for 6G Networks

**Autores:** Budiman Budiman; Mudrik Alaydrus

**Data:** 2026-10-10 · **Tipo:** article

## Resumo

This paper presents a distributed Multi\-Agent Soft Actor\-Critic \(MASAC\) framework based on Centralized Training and Decentralized Execution \(CTDE\) for adaptive Subband Full Duplex \(SBFD\)–TDD frame selection in interference\-coupled multicell networks\. The study is motivated by the need to increase uplink transmission opportunities in 5G\-Advanced and 6G systems while managing the trade\-offs among downlink performance, fairness, congestion, self\-interference, and cross\-link interference \(CLI\)\. A system\-level simulator is developed incorporating traffic\-buffer dynamics, discrete frame\-selection actions, queue\-based latency proxies, and interference\-sensitive service\-rate abstractions over a 21\-cell 3GPP Urban Macro layout\. The proposed method is evaluated against static, heuristic, and centralized global SAC baselines and is further examined through an ablation study comparing MASAC without information exchange \(MASAC\-noIE\) and MASAC with lightweight intercell information exchange \(MASAC\-IE\)\. The results demonstrate stable training under a fixed training budget and load\-dependent coordination behavior\. At a moderate load of 0\.50, MASAC\-IE improves uplink throughput by 34\.9% and reduces the 95th\-percentile queue length by 87% compared with MASAC\-noIE, narrowing the performance gap relative to the centralized upper bound to 4\.7%\. Under heavy\-load conditions, however, the same information\-exchange mechanism induces overly conservative coordination, increasing CLI to 0\.714 and degrading throughput\. These findings indicate that CLI mitigation remains primarily a reward\-design challenge rather than an inherent architectural limitation of distributed multi\-agent learning\.

[Consultar publicação](<https://doi.org/10.58344/locus.v5i10.6323>)
