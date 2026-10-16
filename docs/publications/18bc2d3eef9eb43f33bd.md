---
title: Double-Rollout Reinforcement Learning with Sampling-based Reward Estimation
authors:
- Haifeng Qian
- David Mosallanezhad
- Christian Munley
- Adithya Renduchintala
- Oleksii Kuchaiev
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Reinforcement learning with verifiable rewards (RLVR) implemented with
  Group Relative Policy Optimization (GRPO) has driven substantial progress in training
  reasoning language models. However, verifiable outcome rewards provide an imperfect
  measure of reasoning quality: a correct final answer may not be supported by the
  reasoning trace, whereas an incorrect rollout may contain a nearly correct reasoning
  trajectory. We present empirical evidence for this mismatch and hypothesize that
  the resulting reward noise contributes to instability in reinforcement learning
  for both reasoning accuracy and token efficiency. To address this credit assignment
  challenge, this paper proposes double-rollout reinforcement learning. For each sampled
  rollout, we truncate its reasoning trace, sample multiple continuations from the
  truncated prefix, and replace the original reward with the mean continuation reward,
  yielding a more robust estimate of reasoning quality. This double-rollout algorithm
  incurs only a moderate increase in compute cost and yet reaches substantially higher
  accuracies across math and coding tasks and across Qwen and Nemotron models than
  baseline algorithms with fewer RL steps. For example, using only DAPO data it trains
  Nemotron-3-Nano-30B-A3B to reach 95.4% on AIME 2026, versus 91.5% by GRPO and substantially
  above state of the art for this model size, within 30 RL steps. When combined with
  length-based rewards, the same algorithm further improves the accuracy-efficiency
  Pareto frontier over existing efficiency optimizations. These findings suggest that
  the double-rollout reward estimation is an effective and cost-efficient way to improve
  both the accuracy and token efficiency of reasoning RL.'
source:
- arXiv
source_ids:
- arxiv:2610.16593
url: https://arxiv.org/abs/2610.16593
discovered_at: '2026-10-16'
tags: *id001
---

# Double\-Rollout Reinforcement Learning with Sampling\-based Reward Estimation

**Autores:** Haifeng Qian; David Mosallanezhad; Christian Munley; Adithya Renduchintala; Oleksii Kuchaiev

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Reinforcement learning with verifiable rewards \(RLVR\) implemented with Group Relative Policy Optimization \(GRPO\) has driven substantial progress in training reasoning language models\. However, verifiable outcome rewards provide an imperfect measure of reasoning quality: a correct final answer may not be supported by the reasoning trace, whereas an incorrect rollout may contain a nearly correct reasoning trajectory\. We present empirical evidence for this mismatch and hypothesize that the resulting reward noise contributes to instability in reinforcement learning for both reasoning accuracy and token efficiency\. To address this credit assignment challenge, this paper proposes double\-rollout reinforcement learning\. For each sampled rollout, we truncate its reasoning trace, sample multiple continuations from the truncated prefix, and replace the original reward with the mean continuation reward, yielding a more robust estimate of reasoning quality\. This double\-rollout algorithm incurs only a moderate increase in compute cost and yet reaches substantially higher accuracies across math and coding tasks and across Qwen and Nemotron models than baseline algorithms with fewer RL steps\. For example, using only DAPO data it trains Nemotron\-3\-Nano\-30B\-A3B to reach 95\.4% on AIME 2026, versus 91\.5% by GRPO and substantially above state of the art for this model size, within 30 RL steps\. When combined with length\-based rewards, the same algorithm further improves the accuracy\-efficiency Pareto frontier over existing efficiency optimizations\. These findings suggest that the double\-rollout reward estimation is an effective and cost\-efficient way to improve both the accuracy and token efficiency of reasoning RL\.

[Consultar publicação](<https://arxiv.org/abs/2610.16593>)
