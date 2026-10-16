---
title: Recovering Reliable Supervision via Critique-Guided On-Policy Distillation
authors:
- Kaixiang Zhao
- Tianrun Yu
- Shangzhe Li
- Yuxiao Yang
- Amanda Hughes
- Weitong Zhang
- Taylor W. Killian
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'On-policy distillation (OPD) trains a student model on its own rollouts
  with token-level supervision from a teacher, assuming that the teacher can reach
  a correct answer from any prefix the student writes. We call this property the recoverability
  of the teacher and show it fails on incorrect rollouts: the teacher follows student
  errors, although it recognizes them. We propose CriticOPD, using error recognition
  to restore recoverability. The teacher critiques an incorrect rollout, allowing
  the student to rewrite its solution following the error. The resulting output, including
  the critique as privileged information, is scored by the teacher while the student
  uses the revision without the critique for training. On two Qwen3 students and six
  mathematical reasoning benchmarks, CriticOPD improves OPD, with the largest gains
  on competition problems.'
source:
- arXiv
source_ids:
- arxiv:2610.20572
url: https://arxiv.org/abs/2610.20572
discovered_at: '2026-10-16'
tags: *id001
---

# Recovering Reliable Supervision via Critique\-Guided On\-Policy Distillation

**Autores:** Kaixiang Zhao; Tianrun Yu; Shangzhe Li; Yuxiao Yang; Amanda Hughes; Weitong Zhang; Taylor W\. Killian

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

On\-policy distillation \(OPD\) trains a student model on its own rollouts with token\-level supervision from a teacher, assuming that the teacher can reach a correct answer from any prefix the student writes\. We call this property the recoverability of the teacher and show it fails on incorrect rollouts: the teacher follows student errors, although it recognizes them\. We propose CriticOPD, using error recognition to restore recoverability\. The teacher critiques an incorrect rollout, allowing the student to rewrite its solution following the error\. The resulting output, including the critique as privileged information, is scored by the teacher while the student uses the revision without the critique for training\. On two Qwen3 students and six mathematical reasoning benchmarks, CriticOPD improves OPD, with the largest gains on competition problems\.

[Consultar publicação](<https://arxiv.org/abs/2610.20572>)
