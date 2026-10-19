---
title: Dynamic path reasoning with large language models for interpretable knowledge
  graph question answering
authors:
- Ling Yuan
- Bicheng Wu
- Yangyang Yang
date: '2026-10-15'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1038/s41598-026-72257-9
abstract: 'Abstract Knowledge graph question answering (KGQA) aims to answer natural
  language questions by grounding them in structured knowledge graphs (KGs). Current
  KGQA systems still face three linked challenges: representing complex and compositional
  questions, providing transparent multi-hop reasoning traces, and using complete
  path-level evidence rather than only local triples. We propose SK-DRP ( S yntax-
  K nowledge enhanced D ynamic R easoning with P rompt learning), a modular KGQA framework
  that combines syntax-aware representation, state-adaptive path reasoning, and LLM-assisted
  answer selection. The syntax- and knowledge-enhanced encoder is an auxiliary representation
  enhancement that uses dependency information and knowledge-augmented pre-training
  to align questions with KG entities and relations. Here, dynamic denotes hop-wise
  recomputation of the question-focus indicator, score-qualified frontier expansion,
  and hop-weighted answer aggregation within a fixed dataset-level maximum hop budget;
  it does not denote automatic per-question depth selection. Candidate global paths
  are then compressed and transformed into natural-language auxiliary evidence for
  candidate-set-guided LLM answer selection. Experiments on MetaQA, WebQSP, and CWQ
  show that SK-DRP improves over several path-based and retrieval-based baselines
  on WebQSP and CWQ, while remaining competitive on MetaQA. Ablation, error, and interpretability
  analyses clarify how the syntax encoder, dynamic reasoning module, and LLM-assisted
  answer selection contribute to the final results, as well as the scope and limitations
  of the approach.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222105063
url: https://doi.org/10.1038/s41598-026-72257-9
discovered_at: '2026-10-19'
tags: *id001
---

# Dynamic path reasoning with large language models for interpretable knowledge graph question answering

**Autores:** Ling Yuan; Bicheng Wu; Yangyang Yang

**Data:** 2026-10-15 · **Tipo:** article

## Resumo

Abstract Knowledge graph question answering \(KGQA\) aims to answer natural language questions by grounding them in structured knowledge graphs \(KGs\)\. Current KGQA systems still face three linked challenges: representing complex and compositional questions, providing transparent multi\-hop reasoning traces, and using complete path\-level evidence rather than only local triples\. We propose SK\-DRP \( S yntax\- K nowledge enhanced D ynamic R easoning with P rompt learning\), a modular KGQA framework that combines syntax\-aware representation, state\-adaptive path reasoning, and LLM\-assisted answer selection\. The syntax\- and knowledge\-enhanced encoder is an auxiliary representation enhancement that uses dependency information and knowledge\-augmented pre\-training to align questions with KG entities and relations\. Here, dynamic denotes hop\-wise recomputation of the question\-focus indicator, score\-qualified frontier expansion, and hop\-weighted answer aggregation within a fixed dataset\-level maximum hop budget; it does not denote automatic per\-question depth selection\. Candidate global paths are then compressed and transformed into natural\-language auxiliary evidence for candidate\-set\-guided LLM answer selection\. Experiments on MetaQA, WebQSP, and CWQ show that SK\-DRP improves over several path\-based and retrieval\-based baselines on WebQSP and CWQ, while remaining competitive on MetaQA\. Ablation, error, and interpretability analyses clarify how the syntax encoder, dynamic reasoning module, and LLM\-assisted answer selection contribute to the final results, as well as the scope and limitations of the approach\.

[Consultar publicação](<https://doi.org/10.1038/s41598-026-72257-9>)
