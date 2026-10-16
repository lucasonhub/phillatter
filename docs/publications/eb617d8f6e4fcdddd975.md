---
title: Learning Adaptive Deliberation Control for Reliable Recognition with Multi-Agent
  Language Models
authors:
- Yuan Liu
- Haoyue Peng
- Fanliang Hu
- Lei Huang
- Wenli Cai
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Multi-agent deliberation can improve recognition by criticizing and revising
  candidate answers, but fixed controls cannot respond to changes in disagreement
  or reasoning quality. We present an adaptive multi-agent controller (ADMA) that
  learns continuous policies for proposal, challenge, arbitration, and coordination
  while keeping the task model frozen. Shared trace features describe quality, agreement,
  and progress, while role-specific features support decentralized control during
  inference. One controller trained on legal and financial reasoning is transferred
  without policy updates to four textual and multimodal benchmarks and two successive
  task-model versions. With Qwen3.5 held fixed, ADMA-Full improves accuracy by 6.2-14.2
  percentage points over Direct and by 2.8-3.0 points over ADMA-Fixed. Paired bootstrap
  ranges for the Full-Fixed comparison are positive on three tasks. Outcome decompositions
  show that recoveries exceed introduced errors, while process assessment records
  fewer false-consensus events and more supported correct outcomes. Transfer to Qwen3.6
  remains task dependent, which bounds the generality of the learned policy. Median
  token and latency ratios are 14.3-18.7 and 7.8-16.5 relative to Direct. These results
  show that adaptive deliberation can improve fixed-model recognition when its task-dependent
  gains justify the additional computation.
source:
- arXiv
source_ids:
- arxiv:2610.17840
url: https://arxiv.org/abs/2610.17840
discovered_at: '2026-10-16'
tags: *id001
---

# Learning Adaptive Deliberation Control for Reliable Recognition with Multi\-Agent Language Models

**Autores:** Yuan Liu; Haoyue Peng; Fanliang Hu; Lei Huang; Wenli Cai

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Multi\-agent deliberation can improve recognition by criticizing and revising candidate answers, but fixed controls cannot respond to changes in disagreement or reasoning quality\. We present an adaptive multi\-agent controller \(ADMA\) that learns continuous policies for proposal, challenge, arbitration, and coordination while keeping the task model frozen\. Shared trace features describe quality, agreement, and progress, while role\-specific features support decentralized control during inference\. One controller trained on legal and financial reasoning is transferred without policy updates to four textual and multimodal benchmarks and two successive task\-model versions\. With Qwen3\.5 held fixed, ADMA\-Full improves accuracy by 6\.2\-14\.2 percentage points over Direct and by 2\.8\-3\.0 points over ADMA\-Fixed\. Paired bootstrap ranges for the Full\-Fixed comparison are positive on three tasks\. Outcome decompositions show that recoveries exceed introduced errors, while process assessment records fewer false\-consensus events and more supported correct outcomes\. Transfer to Qwen3\.6 remains task dependent, which bounds the generality of the learned policy\. Median token and latency ratios are 14\.3\-18\.7 and 7\.8\-16\.5 relative to Direct\. These results show that adaptive deliberation can improve fixed\-model recognition when its task\-dependent gains justify the additional computation\.

[Consultar publicação](<https://arxiv.org/abs/2610.17840>)
