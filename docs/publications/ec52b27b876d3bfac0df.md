---
title: 'S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding'
authors:
- Yuhang He
- Hongyu Ge
- Zihan Lin
- Siyi Liu
- Yongqi Zhang
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Fast rollout generation for long-context reinforcement learning with verifiable
  rewards (RLVR) requires reducing KV-cache traffic without changing the response
  groups used for policy optimization. In our profiled RLVR workloads, attention accounts
  for 72--76\% of autoregressive decoding kernel time. Sparse attention reduces these
  reads, but sampling directly from a sparse policy changes the response groups used
  for learning. For group-relative optimization, we show that even exact response-wise
  reweighting does not generally recover the expected dense-policy update because
  the advantage of each response depends on the rewards of other group members. We
  propose Self-Sparse Speculative Rollouts (S$^3$R). It uses sparse attention to propose
  tokens, then generates responses through full-attention verification and exact speculative
  sampling. Drafting and verification share the same policy parameter, eliminating
  the need to train or update a separate drafter. The resulting response groups follow
  the dense-policy distribution. Under S$^3$R, we characterize speedup conditions
  and the costs of drafting and verification. We found that dense verification still
  requires the complete historical KV cache. A KV-aware scheduler therefore limits
  KV-cache repeated offloading and restoration while maintaining rollout parallelism.
  % OR thrashing In a matched ablation with an aggressive sparse drafting budget,
  S$^3$R maintains stable training while direct sparse sampling with training-side
  correction becomes unstable. On long-context mathematical reasoning, S$^3$R achieves
  $1.39\times~1.35\times$ the end-to-end training throughput of autoregressive rollouts
  on Qwen3 model, with comparable task performance.
source:
- arXiv
source_ids:
- arxiv:2610.13202
url: https://arxiv.org/abs/2610.13202
discovered_at: '2026-10-16'
tags: *id001
---

# S$^3$R: Fast and Faithful RL Rollouts via Self\-Sparse Speculative Decoding

**Autores:** Yuhang He; Hongyu Ge; Zihan Lin; Siyi Liu; Yongqi Zhang

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Fast rollout generation for long\-context reinforcement learning with verifiable rewards \(RLVR\) requires reducing KV\-cache traffic without changing the response groups used for policy optimization\. In our profiled RLVR workloads, attention accounts for 72\-\-76\\% of autoregressive decoding kernel time\. Sparse attention reduces these reads, but sampling directly from a sparse policy changes the response groups used for learning\. For group\-relative optimization, we show that even exact response\-wise reweighting does not generally recover the expected dense\-policy update because the advantage of each response depends on the rewards of other group members\. We propose Self\-Sparse Speculative Rollouts \(S$^3$R\)\. It uses sparse attention to propose tokens, then generates responses through full\-attention verification and exact speculative sampling\. Drafting and verification share the same policy parameter, eliminating the need to train or update a separate drafter\. The resulting response groups follow the dense\-policy distribution\. Under S$^3$R, we characterize speedup conditions and the costs of drafting and verification\. We found that dense verification still requires the complete historical KV cache\. A KV\-aware scheduler therefore limits KV\-cache repeated offloading and restoration while maintaining rollout parallelism\. % OR thrashing In a matched ablation with an aggressive sparse drafting budget, S$^3$R maintains stable training while direct sparse sampling with training\-side correction becomes unstable\. On long\-context mathematical reasoning, S$^3$R achieves $1\.39\\times\~1\.35\\times$ the end\-to\-end training throughput of autoregressive rollouts on Qwen3 model, with comparable task performance\.

[Consultar publicação](<https://arxiv.org/abs/2610.13202>)
