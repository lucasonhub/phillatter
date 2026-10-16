---
title: Does self-distillation improve reasoning?
authors:
- Jason Ken Adhinarta
- Raina Wu
- Ashutosh Sharma
- Avinash Balakrishnan
- Rameswar Panda
- Polina Golland
- Yoon Kim
- Zhang-Wei Hong
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Self-distillation is an emerging approach that trains a model to imitate
  its own predictions when conditioned on privileged information, such as correct
  answers or environmental feedback. Recent methods have reported better sample efficiency
  and generalization than reinforcement learning (RL), but it remains unclear whether
  these gains extend beyond in-distribution evaluations and whether they stem from
  privileged distillation. In this paper, we revisit two representative methods, Self-Distillation
  Policy Optimization (SDPO) and On-Policy Self-Distillation (OPSD), across code,
  science, tool use, and math reasoning tasks. We find that their reported gains do
  not consistently generalize to unseen problems and are largely explained by overfitting
  or transferring existing reasoning behavior, rather than effectively using privileged
  information. Moreover, self-distillation gradients show weak alignment with policy
  gradients that directly optimize expected reward, questioning whether they provide
  an effective direction for policy improvement. Our experiments across Qwen3 models
  (1.7B-14B) and OLMo-3-7B suggest that effectively leveraging privileged information
  to improve reasoning remains an open challenge. Our code is available at https://github.com/sleepypandu/does-sd-improve-reasoning
source:
- arXiv
source_ids:
- arxiv:2610.18613
url: https://arxiv.org/abs/2610.18613
discovered_at: '2026-10-16'
tags: *id001
---

# Does self\-distillation improve reasoning?

**Autores:** Jason Ken Adhinarta; Raina Wu; Ashutosh Sharma; Avinash Balakrishnan; Rameswar Panda; Polina Golland; Yoon Kim; Zhang\-Wei Hong

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Self\-distillation is an emerging approach that trains a model to imitate its own predictions when conditioned on privileged information, such as correct answers or environmental feedback\. Recent methods have reported better sample efficiency and generalization than reinforcement learning \(RL\), but it remains unclear whether these gains extend beyond in\-distribution evaluations and whether they stem from privileged distillation\. In this paper, we revisit two representative methods, Self\-Distillation Policy Optimization \(SDPO\) and On\-Policy Self\-Distillation \(OPSD\), across code, science, tool use, and math reasoning tasks\. We find that their reported gains do not consistently generalize to unseen problems and are largely explained by overfitting or transferring existing reasoning behavior, rather than effectively using privileged information\. Moreover, self\-distillation gradients show weak alignment with policy gradients that directly optimize expected reward, questioning whether they provide an effective direction for policy improvement\. Our experiments across Qwen3 models \(1\.7B\-14B\) and OLMo\-3\-7B suggest that effectively leveraging privileged information to improve reasoning remains an open challenge\. Our code is available at https://github\.com/sleepypandu/does\-sd\-improve\-reasoning

[Consultar publicação](<https://arxiv.org/abs/2610.18613>)
