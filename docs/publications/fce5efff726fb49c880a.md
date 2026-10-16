---
title: 'SLDBench v2: Active Scaling Law Discovery'
authors:
- Lingbei Meng
- Rui Huang
- Zhirong Shen
- Jinxin Liu
- Lingxiao Jing
- Haorui Chen
- Yaosong Du
- Haowei Lin
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Scaling laws predict large-model performance from small experiments, but
  finding a reliable law itself requires costly experiments. SLDBench tests whether
  language-model agents can discover scaling laws when all experimental results are
  given upfront. We introduce SLDBench v2 with two extensions. First, we expand the
  corpus from 8 to 127 scenarios spanning language-model pretraining, downstream performance,
  and vision-language transfer, and select 30 challenging scenarios on which a reference
  power-law fit reaches $R^2 \le 0.8$; they represent at least $1.09 \times 10^{23}$
  FLOPs of source-reported training compute. Second, we introduce active scaling law
  discovery: an agent chooses which experiments to run, pays each one''s recorded
  cost (e.g., training FLOPs), and revises its law as outcomes arrive, and is scored
  on the same hidden extrapolation targets as in the passive setting. Across 8 frontier
  agent systems, median $R^2$ drops from 0.72-0.75 (passive) to 0.24-0.57 (active),
  and prediction error rises 1.5-4.7 times, depending on the system. Agents favor
  cheap experiments, spending 8-44% of the full-pool cost on average; low-cost acquisition
  can yield strong predictions, but cheap purchases also leave experimental conditions
  needed for extrapolation unobserved. Experimental planning thus remains a key open
  challenge for agents that assist model development in the prevailing AI-for-AI study.'
source:
- arXiv
source_ids:
- arxiv:2610.16297
url: https://arxiv.org/abs/2610.16297
discovered_at: '2026-10-16'
tags: *id001
---

# SLDBench v2: Active Scaling Law Discovery

**Autores:** Lingbei Meng; Rui Huang; Zhirong Shen; Jinxin Liu; Lingxiao Jing; Haorui Chen; Yaosong Du; Haowei Lin

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Scaling laws predict large\-model performance from small experiments, but finding a reliable law itself requires costly experiments\. SLDBench tests whether language\-model agents can discover scaling laws when all experimental results are given upfront\. We introduce SLDBench v2 with two extensions\. First, we expand the corpus from 8 to 127 scenarios spanning language\-model pretraining, downstream performance, and vision\-language transfer, and select 30 challenging scenarios on which a reference power\-law fit reaches $R^2 \\le 0\.8$; they represent at least $1\.09 \\times 10^\{23\}$ FLOPs of source\-reported training compute\. Second, we introduce active scaling law discovery: an agent chooses which experiments to run, pays each one&\#x27;s recorded cost \(e\.g\., training FLOPs\), and revises its law as outcomes arrive, and is scored on the same hidden extrapolation targets as in the passive setting\. Across 8 frontier agent systems, median $R^2$ drops from 0\.72\-0\.75 \(passive\) to 0\.24\-0\.57 \(active\), and prediction error rises 1\.5\-4\.7 times, depending on the system\. Agents favor cheap experiments, spending 8\-44% of the full\-pool cost on average; low\-cost acquisition can yield strong predictions, but cheap purchases also leave experimental conditions needed for extrapolation unobserved\. Experimental planning thus remains a key open challenge for agents that assist model development in the prevailing AI\-for\-AI study\.

[Consultar publicação](<https://arxiv.org/abs/2610.16297>)
