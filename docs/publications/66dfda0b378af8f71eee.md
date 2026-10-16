---
title: 'Quality, Not Just Outcome: A Structural Scoring Framework for Selecting Coding-Agent
  Trajectories for Supervised Fine-Tuning'
authors:
- Sida Li
- Yuanxin Liu
- Shicheng Li
- Linli Yao
- Xu Sun
- Haoli Bai
- Xiaohui Li
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Open coding agents are commonly trained through supervised fine-tuning
  on interaction trajectories whose final patches pass the benchmark test suite. However,
  this outcome-level filtering criterion ignores process quality: trajectories that
  eventually succeed may still contain inefficient interaction patterns such as repetitive
  file inspection, unstable tool usage, or delayed modification behavior, all of which
  become part of the imitation target. We propose TQS (Trajectory Quality Score),
  a structural scoring framework for coding-agent trajectories that operates directly
  on trajectory structure, requires no LLM judge, and runs in linear time. TQS characterizes
  trajectory quality through structural signals organized around structured convergence:
  information focus, intent--action alignment, and policy dynamics. Using 155,144
  successful trajectories from a public open-license corpus, we rank trajectories
  by TQS and fine-tune coding agents on filtered subsets. Models trained on top-ranked
  trajectories consistently outperform those trained on random or bottom-ranked subsets
  on SWE-Bench-Verified. Our results suggest that process-level trajectory quality
  is an important factor in coding-agent supervision and that structural trajectory
  filtering provides an effective and scalable alternative to LLM-based data selection.'
source:
- arXiv
source_ids:
- arxiv:2610.13152
url: https://arxiv.org/abs/2610.13152
discovered_at: '2026-10-16'
tags: *id001
---

# Quality, Not Just Outcome: A Structural Scoring Framework for Selecting Coding\-Agent Trajectories for Supervised Fine\-Tuning

**Autores:** Sida Li; Yuanxin Liu; Shicheng Li; Linli Yao; Xu Sun; Haoli Bai; Xiaohui Li

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Open coding agents are commonly trained through supervised fine\-tuning on interaction trajectories whose final patches pass the benchmark test suite\. However, this outcome\-level filtering criterion ignores process quality: trajectories that eventually succeed may still contain inefficient interaction patterns such as repetitive file inspection, unstable tool usage, or delayed modification behavior, all of which become part of the imitation target\. We propose TQS \(Trajectory Quality Score\), a structural scoring framework for coding\-agent trajectories that operates directly on trajectory structure, requires no LLM judge, and runs in linear time\. TQS characterizes trajectory quality through structural signals organized around structured convergence: information focus, intent\-\-action alignment, and policy dynamics\. Using 155,144 successful trajectories from a public open\-license corpus, we rank trajectories by TQS and fine\-tune coding agents on filtered subsets\. Models trained on top\-ranked trajectories consistently outperform those trained on random or bottom\-ranked subsets on SWE\-Bench\-Verified\. Our results suggest that process\-level trajectory quality is an important factor in coding\-agent supervision and that structural trajectory filtering provides an effective and scalable alternative to LLM\-based data selection\.

[Consultar publicação](<https://arxiv.org/abs/2610.13152>)
