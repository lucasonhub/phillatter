---
title: 'Explore with Memory, Learn without It: In-Context Exploration and Self-Distillation
  for LLM Reasoning'
authors:
- Yutong Chen
- Zhichao Xu
- Rui Liu
- Kunpeng Liu
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Exploration bounds learning efficiency in reinforcement learning with verifiable
  rewards (RLVR). Current methods explore mostly through independent sampling, without
  fully using the information gathered along the way, such as known wrong answers
  and environment feedback. We propose LEAF, which injects a dynamic, problem-specific
  memory into the context before every rollout. The memory contains the most recent
  response, its reward, and other environment feedback. It is updated after every
  verifier call. We decouple policy updates from rollouts and update the policy through
  self-distillation. On four benchmarks and two open models, LEAF accelerates exploration
  by about 4x compared with a random sampling baseline. On unseen test sets, it improves
  accuracy over the strongest baseline by 1.59 and 1.83 percentage points on the two
  models, while using less compute than any RL baseline. These results highlight the
  potential of LEAF in improving both exploration and learning efficiency. Code is
  available at: https://github.com/on1262/LEAF'
source:
- arXiv
source_ids:
- arxiv:2610.17734
url: https://arxiv.org/abs/2610.17734
discovered_at: '2026-10-16'
tags: *id001
---

# Explore with Memory, Learn without It: In\-Context Exploration and Self\-Distillation for LLM Reasoning

**Autores:** Yutong Chen; Zhichao Xu; Rui Liu; Kunpeng Liu

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Exploration bounds learning efficiency in reinforcement learning with verifiable rewards \(RLVR\)\. Current methods explore mostly through independent sampling, without fully using the information gathered along the way, such as known wrong answers and environment feedback\. We propose LEAF, which injects a dynamic, problem\-specific memory into the context before every rollout\. The memory contains the most recent response, its reward, and other environment feedback\. It is updated after every verifier call\. We decouple policy updates from rollouts and update the policy through self\-distillation\. On four benchmarks and two open models, LEAF accelerates exploration by about 4x compared with a random sampling baseline\. On unseen test sets, it improves accuracy over the strongest baseline by 1\.59 and 1\.83 percentage points on the two models, while using less compute than any RL baseline\. These results highlight the potential of LEAF in improving both exploration and learning efficiency\. Code is available at: https://github\.com/on1262/LEAF

[Consultar publicação](<https://arxiv.org/abs/2610.17734>)
