---
title: 'MetaCurate: Evolving Curation Filters for High-Quality Agentic Coding Data'
authors:
- Donghoon Kim
- Seunghyuk Oh
- Kevin Galim
- Minseo Kim
- Minjae Lee
- Younghyun Kim
- Wooseok Seo
- Hyung Il Koo
- Wonjun Kang
date: '2026-10-16'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Supervised fine-tuning on agent trajectories is an effective way to improve
  coding agents, but selecting useful training examples requires more than identifying
  successful runs. A resolved patch may follow inefficient reasoning or unnecessary
  tool use, while a failed run may still contain useful intermediate steps. Training
  pipelines therefore rely on rules and qualitative assessments to filter trajectories,
  yet designing these filters typically requires substantial human expertise, and
  validating improvements through repeated training and evaluation is expensive. We
  introduce MetaCurate, a training-free framework that evolves executable trajectory
  curation filters using pairwise LLM judgments. Disagreements between the filter's
  rankings and the judge's preferences provide targeted feedback for jointly revising
  its rules, rubric, and aggregation policy. The resulting filter scores trajectories
  independently, so pairwise comparisons are required only during search. Starting
  from a blank filter, MetaCurate autonomously discovers a curation strategy that
  achieves competitive downstream performance without task-specific handwritten criteria.
  We validate downstream utility through controlled SFT experiments on our uncurated
  trajectory pool and the Nemotron v3 SWE dataset, with random selection and hand-authored
  filtering as baselines. In our experiments, MetaCurate achieves the highest mean
  SWE-Verified score among the compared methods, including hand-authored rule-based
  filtering and a training-loop baseline whose search costs 3.5x as much.
source:
- arXiv
source_ids:
- arxiv:2610.23134
url: https://arxiv.org/abs/2610.23134
discovered_at: '2026-10-19'
tags: *id001
---

# MetaCurate: Evolving Curation Filters for High\-Quality Agentic Coding Data

**Autores:** Donghoon Kim; Seunghyuk Oh; Kevin Galim; Minseo Kim; Minjae Lee; Younghyun Kim; Wooseok Seo; Hyung Il Koo; Wonjun Kang

**Data:** 2026-10-16 · **Tipo:** preprint

## Resumo

Supervised fine\-tuning on agent trajectories is an effective way to improve coding agents, but selecting useful training examples requires more than identifying successful runs\. A resolved patch may follow inefficient reasoning or unnecessary tool use, while a failed run may still contain useful intermediate steps\. Training pipelines therefore rely on rules and qualitative assessments to filter trajectories, yet designing these filters typically requires substantial human expertise, and validating improvements through repeated training and evaluation is expensive\. We introduce MetaCurate, a training\-free framework that evolves executable trajectory curation filters using pairwise LLM judgments\. Disagreements between the filter&\#x27;s rankings and the judge&\#x27;s preferences provide targeted feedback for jointly revising its rules, rubric, and aggregation policy\. The resulting filter scores trajectories independently, so pairwise comparisons are required only during search\. Starting from a blank filter, MetaCurate autonomously discovers a curation strategy that achieves competitive downstream performance without task\-specific handwritten criteria\. We validate downstream utility through controlled SFT experiments on our uncurated trajectory pool and the Nemotron v3 SWE dataset, with random selection and hand\-authored filtering as baselines\. In our experiments, MetaCurate achieves the highest mean SWE\-Verified score among the compared methods, including hand\-authored rule\-based filtering and a training\-loop baseline whose search costs 3\.5x as much\.

[Consultar publicação](<https://arxiv.org/abs/2610.23134>)
