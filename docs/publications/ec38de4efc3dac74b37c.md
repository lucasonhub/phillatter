---
title: 'Policy-Verified Self-Training: Learning Agent Compliance from Verifiable Policy
  Rewards'
authors:
- Min-Young Yu
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Runtime policy verifiers can prevent agents from executing disallowed actions,
  but their decisions are typically used only for enforcement and discarded afterward.
  We ask whether these decisions can instead become verifiable policy rewards for
  training the agents they guard. We introduce Policy-Verified Self-Training (PVST),
  a post-training paradigm in which an agent generates its own interaction trajectories
  and an executable policy verifier, here a deterministic gate compiled from a written
  policy, evaluates whether each action complies. Compliant trajectories are reinforced,
  and violations become negatives for preference optimization; beyond the gate and
  the benchmark''s task-success signal, PVST needs no stronger teacher model, no human
  preference labels and no attack-specific supervision, although rollouts are collected
  in the benchmark''s attacked environment. On held-out AgentDojo tasks under prompt
  injection, policy-verified preference training of Qwen3-8B reduces violating trajectories
  from 37.2% to 10.3 $\pm$ 0.9% (three seeds) and successful attacks from 12.4% to
  0.5% at equal or higher pooled task utility, although utility falls on travel, compared
  with 22.0% when negatives are selected by an attack oracle and 31.9 $\pm$ 0.9% with
  negatives that contain no violation. The learned behavior holds under an attack
  template never used in training (37.7% to 11.0%) and on a suite excluded from training
  (34.8% to 16.7%), and the retained verifier''s intervention rate falls from 39.2%
  to 8.8% (seed 0). Our analysis identifies two conditions under which the verdict
  is most informative: success must not already imply compliance, and guarded actions
  must appear in both permitted and forbidden contexts.'
source:
- arXiv
source_ids:
- arxiv:2610.19372
url: https://arxiv.org/abs/2610.19372
discovered_at: '2026-10-16'
tags: *id001
---

# Policy\-Verified Self\-Training: Learning Agent Compliance from Verifiable Policy Rewards

**Autores:** Min\-Young Yu

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Runtime policy verifiers can prevent agents from executing disallowed actions, but their decisions are typically used only for enforcement and discarded afterward\. We ask whether these decisions can instead become verifiable policy rewards for training the agents they guard\. We introduce Policy\-Verified Self\-Training \(PVST\), a post\-training paradigm in which an agent generates its own interaction trajectories and an executable policy verifier, here a deterministic gate compiled from a written policy, evaluates whether each action complies\. Compliant trajectories are reinforced, and violations become negatives for preference optimization; beyond the gate and the benchmark&\#x27;s task\-success signal, PVST needs no stronger teacher model, no human preference labels and no attack\-specific supervision, although rollouts are collected in the benchmark&\#x27;s attacked environment\. On held\-out AgentDojo tasks under prompt injection, policy\-verified preference training of Qwen3\-8B reduces violating trajectories from 37\.2% to 10\.3 $\\pm$ 0\.9% \(three seeds\) and successful attacks from 12\.4% to 0\.5% at equal or higher pooled task utility, although utility falls on travel, compared with 22\.0% when negatives are selected by an attack oracle and 31\.9 $\\pm$ 0\.9% with negatives that contain no violation\. The learned behavior holds under an attack template never used in training \(37\.7% to 11\.0%\) and on a suite excluded from training \(34\.8% to 16\.7%\), and the retained verifier&\#x27;s intervention rate falls from 39\.2% to 8\.8% \(seed 0\)\. Our analysis identifies two conditions under which the verdict is most informative: success must not already imply compliance, and guarded actions must appear in both permitted and forbidden contexts\.

[Consultar publicação](<https://arxiv.org/abs/2610.19372>)
