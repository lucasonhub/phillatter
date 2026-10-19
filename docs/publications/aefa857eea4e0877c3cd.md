---
title: 'Edge-native Small Language Models for 6G Intent-driven Slicing: A Hardware-grounded
  Empirical Study'
authors:
- Pratchaya Jaisudthi
- Pachara Threerapat Sridee
- Natthakran Phungkoed
- Siwakun Kunsuk
- Kanyaphak Srisuk
- Vasupon Phueaknamphol
date: '2026-10-16'
type: article
category: &id001
- Inteligência Artificial
doi: 10.22266/ijies2026.1130.75
abstract: 'This study presents a deterministic, hardware-grounded empirical evaluation
  of open-weight Small Language Models (SLMs) on CPU-only edge infrastructure.Using
  greedy decoding for exact reproducibility, we benchmark four ∼8B-parameter families
  (Llama 3.1, Qwen 2.5, Gemma 2, GLM-4) under identical Q4_K_M quantisation, then
  run a 4×3 scaling analysis of Qwen 2.5 (0.5B-7B).By capturing validated telemetry-RAPL
  (Running Average Power Limit) package energy and IMC (Integrated Memory Controller)
  DRAM bandwidth across NUMA (Non-Uniform Memory Access) nodes-we provide direct hardware
  evidence of a memory-bandwidthsensitive regime for SLM edge inference.The results
  reveal a trade-off: Gemma 2 9B attains the highest actioncorrectness (50.0%, p=0.0037),
  while Qwen 2.5 7B is more efficient (2.1× faster, 2.3× lower marginal energy).We
  identify Qwen 2.5 3B (Q4_K_M) as the accuracy-efficiency sweet spot: 46.0% action
  accuracy, 5.1 s/intent, 1,997 MB peak memory, statistically tied with its 7B counterpart
  under identical Q4_K_M quantisation (McNemar p=0.11).'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222698571
url: https://doi.org/10.22266/ijies2026.1130.75
discovered_at: '2026-10-19'
tags: *id001
---

# Edge\-native Small Language Models for 6G Intent\-driven Slicing: A Hardware\-grounded Empirical Study

**Autores:** Pratchaya Jaisudthi; Pachara Threerapat Sridee; Natthakran Phungkoed; Siwakun Kunsuk; Kanyaphak Srisuk; Vasupon Phueaknamphol

**Data:** 2026-10-16 · **Tipo:** article

## Resumo

This study presents a deterministic, hardware\-grounded empirical evaluation of open\-weight Small Language Models \(SLMs\) on CPU\-only edge infrastructure\.Using greedy decoding for exact reproducibility, we benchmark four ∼8B\-parameter families \(Llama 3\.1, Qwen 2\.5, Gemma 2, GLM\-4\) under identical Q4\_K\_M quantisation, then run a 4×3 scaling analysis of Qwen 2\.5 \(0\.5B\-7B\)\.By capturing validated telemetry\-RAPL \(Running Average Power Limit\) package energy and IMC \(Integrated Memory Controller\) DRAM bandwidth across NUMA \(Non\-Uniform Memory Access\) nodes\-we provide direct hardware evidence of a memory\-bandwidthsensitive regime for SLM edge inference\.The results reveal a trade\-off: Gemma 2 9B attains the highest actioncorrectness \(50\.0%, p=0\.0037\), while Qwen 2\.5 7B is more efficient \(2\.1× faster, 2\.3× lower marginal energy\)\.We identify Qwen 2\.5 3B \(Q4\_K\_M\) as the accuracy\-efficiency sweet spot: 46\.0% action accuracy, 5\.1 s/intent, 1,997 MB peak memory, statistically tied with its 7B counterpart under identical Q4\_K\_M quantisation \(McNemar p=0\.11\)\.

[Consultar publicação](<https://doi.org/10.22266/ijies2026.1130.75>)
