---
title: Divergence-Routed On-Policy Distillation for Language Models
authors:
- Tiantian Peng
- Guannan Lv
- Hongyang Li
- Qiuhe Hong
- Hang Cheng
- Hongjian Dou
- Xiangyu Wu
- Yuyang Liu
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'On-policy distillation (OPD) transfers knowledge from a teacher model to
  a student along student-generated trajectories, typically by minimizing the reverse
  Kullback-Leibler (RKL) divergence. However, RKL can provide weak corrective signals
  for teacher-supported tokens to which the student assigns very low probability.
  This raises two questions: which positions are most consequential for the behavioral
  gap between the student and teacher, and what additional supervision is needed at
  these positions? Through cross-sampling, we find that divergence-based routing more
  effectively pinpoints positions contributing to the teacher-student performance
  gap than entropy-based routing. Further analysis reveals teacher-mode under-coverage
  at high Jensen-Shannon (JS) divergence positions, where standard OPD increases the
  large teacher-student probability gaps. Motivated by these findings, we propose
  Divergence-Routed On-Policy Distillation (DrOPD). DrOPD retains RKL supervision
  at all positions and selectively adds forward Kullback-Leibler (FKL) divergence
  supervision at positions with high JS divergence. Experiments across six math benchmarks
  show that DrOPD improves over standard OPD and entropy-based routing. DrOPD also
  reduces severe under-coverage cases by 37.9 percent relative to OPD, supporting
  targeted FKL as an effective complement to OPD.'
source:
- arXiv
source_ids:
- arxiv:2610.19572
url: https://arxiv.org/abs/2610.19572
discovered_at: '2026-10-16'
tags: *id001
---

# Divergence\-Routed On\-Policy Distillation for Language Models

**Autores:** Tiantian Peng; Guannan Lv; Hongyang Li; Qiuhe Hong; Hang Cheng; Hongjian Dou; Xiangyu Wu; Yuyang Liu

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

On\-policy distillation \(OPD\) transfers knowledge from a teacher model to a student along student\-generated trajectories, typically by minimizing the reverse Kullback\-Leibler \(RKL\) divergence\. However, RKL can provide weak corrective signals for teacher\-supported tokens to which the student assigns very low probability\. This raises two questions: which positions are most consequential for the behavioral gap between the student and teacher, and what additional supervision is needed at these positions? Through cross\-sampling, we find that divergence\-based routing more effectively pinpoints positions contributing to the teacher\-student performance gap than entropy\-based routing\. Further analysis reveals teacher\-mode under\-coverage at high Jensen\-Shannon \(JS\) divergence positions, where standard OPD increases the large teacher\-student probability gaps\. Motivated by these findings, we propose Divergence\-Routed On\-Policy Distillation \(DrOPD\)\. DrOPD retains RKL supervision at all positions and selectively adds forward Kullback\-Leibler \(FKL\) divergence supervision at positions with high JS divergence\. Experiments across six math benchmarks show that DrOPD improves over standard OPD and entropy\-based routing\. DrOPD also reduces severe under\-coverage cases by 37\.9 percent relative to OPD, supporting targeted FKL as an effective complement to OPD\.

[Consultar publicação](<https://arxiv.org/abs/2610.19572>)
