---
title: Benchmarking and Training Reward Models for Cross-Source Evidence Grounding
  in Search Agents
authors:
- Haochen Zhao
- Minsheng Hao
- Zheng Li
- Yifan Li
- Zikang Liu
- Bowen Qin
- Yuhao Cheng
- Chuang Fan
- Haosheng Zou
- Jeff Chen
- Sujian Li
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Existing approaches to training and evaluating search agents focus heavily
  on final-answer quality, largely neglecting how generated answers map back to retrieved
  evidence. Recent methods track citations to enforce grounding, but citation support
  alone does not establish source independence or whether an answer appropriately
  handles conflicting evidence. We argue that credibility in open-web retrieval depends
  on principled cross-source evidence grounding that accounts for source independence
  and systematically attributes and adjudicates conflicting evidence, while hierarchical
  judgments of these grounding decisions provide a unified signal for training and
  evaluation. To this end, we propose an evaluation framework, Cross-Source Evidence
  Grounding (CSEG), that employs a fine-grained, six-layer decision tree over the
  complete search trajectory. We introduce CSEG-Bench and trainable reward models
  to provide targeted supervision following this framework. Our approach helps eliminating
  the severe data skew of natural trajectories by providing targeted coverage over
  complex, deep-layer decision paths, such as cross-source conflict resolution and
  nuanced attribution, that standard rollouts fail to capture. Specifically, (1) we
  define the hierarchy at label, node, and path levels; (2) we construct 1,160 verified
  trajectories over nine canonical paths by rewriting answers on real retrieved document
  pools, with independent frontier judges reproducing the entire gold path and human
  experts deciding inclusion; (3) we train CSEG-RM, which reaches 83.9% exact accuracy
  on our benchmark while lying on the performance-token efficiency Pareto frontier.
  Experiments that use this reward alone to supervise a frozen-retrieval answer policy
  raise the independently judged mean label from 2.83 to 4.19, and show that learning
  the hierarchy generalizes across layers at a fraction of frontier-judge cost.
source:
- arXiv
source_ids:
- arxiv:2610.17827
url: https://arxiv.org/abs/2610.17827
discovered_at: '2026-10-16'
tags: *id001
---

# Benchmarking and Training Reward Models for Cross\-Source Evidence Grounding in Search Agents

**Autores:** Haochen Zhao; Minsheng Hao; Zheng Li; Yifan Li; Zikang Liu; Bowen Qin; Yuhao Cheng; Chuang Fan; Haosheng Zou; Jeff Chen; Sujian Li

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Existing approaches to training and evaluating search agents focus heavily on final\-answer quality, largely neglecting how generated answers map back to retrieved evidence\. Recent methods track citations to enforce grounding, but citation support alone does not establish source independence or whether an answer appropriately handles conflicting evidence\. We argue that credibility in open\-web retrieval depends on principled cross\-source evidence grounding that accounts for source independence and systematically attributes and adjudicates conflicting evidence, while hierarchical judgments of these grounding decisions provide a unified signal for training and evaluation\. To this end, we propose an evaluation framework, Cross\-Source Evidence Grounding \(CSEG\), that employs a fine\-grained, six\-layer decision tree over the complete search trajectory\. We introduce CSEG\-Bench and trainable reward models to provide targeted supervision following this framework\. Our approach helps eliminating the severe data skew of natural trajectories by providing targeted coverage over complex, deep\-layer decision paths, such as cross\-source conflict resolution and nuanced attribution, that standard rollouts fail to capture\. Specifically, \(1\) we define the hierarchy at label, node, and path levels; \(2\) we construct 1,160 verified trajectories over nine canonical paths by rewriting answers on real retrieved document pools, with independent frontier judges reproducing the entire gold path and human experts deciding inclusion; \(3\) we train CSEG\-RM, which reaches 83\.9% exact accuracy on our benchmark while lying on the performance\-token efficiency Pareto frontier\. Experiments that use this reward alone to supervise a frozen\-retrieval answer policy raise the independently judged mean label from 2\.83 to 4\.19, and show that learning the hierarchy generalizes across layers at a fraction of frontier\-judge cost\.

[Consultar publicação](<https://arxiv.org/abs/2610.17827>)
