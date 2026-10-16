---
title: Co-adaptive Rule Routing and Constraining for Structured Knowledge Retrieval
authors:
- Zhisheng Qi
- Haoyu Han
- Jiaxi Li
- Bing He
- Huiyuan Chen
- Franck Dernoncourt
- Ryan A. Rossi
- Mahantesh M. Halappanavar
- Jin Lu
- Yu Zhang
- Tianming Liu
- Yu Wang
date: '2026-10-10'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Structured knowledge retrieval acquires task-relevant evidence from structured
  knowledge sources for downstream tasks. Existing methods rely on unconstrained retrieval
  or predefined query-rule supervision, such as author-paper rules for scientific
  discovery and anatomy-drug rules for precision medicine. Such supervision is rarely
  available in practice. We propose Co-Adaptive Rule Routing and Constraining Retrieval
  (CoRE), which jointly learns which reasoning rule to assign to each query and how
  to retrieve evidence under that rule, without predefined query-rule pairs. A routing
  agent selects a rule, and its corresponding retriever traverses the knowledge base
  and ranks evidence that satisfies the rule's constraints. Because routing and retrieval
  are interdependent, CoRE alternates between reinforcement learning for the routing
  policy and contrastive learning for the rule-constrained retriever. The selected
  rules provide supervision for retriever training, while retrieval performance rewards
  the routing policy. This closed-loop process enables both components to co-adapt
  without explicit query-rule supervision. Experiments on STaRK-QA datasets across
  scientific discovery, biomedical reasoning, and e-commerce knowledge management
  demonstrate CoRE's effectiveness. Ablations show the benefit of co-adapting the
  router and retriever. Generation-based routing transfers across datasets and benefits
  from multi-domain pretraining followed by target-specific fine-tuning. Analysis
  of rule usage across queries also informs automatic rule refinement and discovery.
source:
- arXiv
source_ids:
- arxiv:2610.14465
url: https://arxiv.org/abs/2610.14465
discovered_at: '2026-10-16'
tags: *id001
---

# Co\-adaptive Rule Routing and Constraining for Structured Knowledge Retrieval

**Autores:** Zhisheng Qi; Haoyu Han; Jiaxi Li; Bing He; Huiyuan Chen; Franck Dernoncourt; Ryan A\. Rossi; Mahantesh M\. Halappanavar; Jin Lu; Yu Zhang; Tianming Liu; Yu Wang

**Data:** 2026-10-10 · **Tipo:** preprint

## Resumo

Structured knowledge retrieval acquires task\-relevant evidence from structured knowledge sources for downstream tasks\. Existing methods rely on unconstrained retrieval or predefined query\-rule supervision, such as author\-paper rules for scientific discovery and anatomy\-drug rules for precision medicine\. Such supervision is rarely available in practice\. We propose Co\-Adaptive Rule Routing and Constraining Retrieval \(CoRE\), which jointly learns which reasoning rule to assign to each query and how to retrieve evidence under that rule, without predefined query\-rule pairs\. A routing agent selects a rule, and its corresponding retriever traverses the knowledge base and ranks evidence that satisfies the rule&\#x27;s constraints\. Because routing and retrieval are interdependent, CoRE alternates between reinforcement learning for the routing policy and contrastive learning for the rule\-constrained retriever\. The selected rules provide supervision for retriever training, while retrieval performance rewards the routing policy\. This closed\-loop process enables both components to co\-adapt without explicit query\-rule supervision\. Experiments on STaRK\-QA datasets across scientific discovery, biomedical reasoning, and e\-commerce knowledge management demonstrate CoRE&\#x27;s effectiveness\. Ablations show the benefit of co\-adapting the router and retriever\. Generation\-based routing transfers across datasets and benefits from multi\-domain pretraining followed by target\-specific fine\-tuning\. Analysis of rule usage across queries also informs automatic rule refinement and discovery\.

[Consultar publicação](<https://arxiv.org/abs/2610.14465>)
