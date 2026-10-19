---
title: 'Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate
  Future Queries'
authors:
- Anikait Singh
- Teresa Zhang
- Yoonho Lee
- Roshen Sanjay Nair
- Aviral Kumar
- Chelsea Finn
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Reasoning over long document contexts remains a challenge for large language
  models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking
  agents with complex, cross-document reasoning at inference time, while precomputed
  structures like knowledge graphs often fall short because they rely on rigid heuristics.
  Instead, can we allow agents to perform anticipatory directed curation: learning
  to proactively reorganize unstructured corpora prior to inference to efficiently
  serve diverse future queries. We build on a key asymmetry in modern agentic harnesses
  (e.g., Claude Code): while LLM agents are adept at navigating existing filesystems
  to solve an immediate task, they are rarely trained to construct reusable workspaces
  for future use. To instantiate this capability, we introduce Librarian Agents, a
  framework in which a builder agent transforms raw documents into a hierarchical
  filesystem of synthetic files and reference links, which forms a workspace tailored
  for a downstream answering agent. We formulate workspace construction as a Markov
  decision process and optimize the builder policy via reinforcement learning to directly
  maximize downstream answering accuracy. Empirically, Librarian Agents outperforms
  the strongest retrieval and precomputation baselines by 33 percentage points on
  BrowseComp-Plus, amortizes upfront construction costs across repeated queries, and
  generalizes zero-shot to unseen domains on BRIGHT with a 31-point average accuracy
  improvement.'
source:
- arXiv
source_ids:
- arxiv:2610.22273
url: https://arxiv.org/abs/2610.22273
discovered_at: '2026-10-19'
tags: *id001
---

# Librarian Agents: Training LLMs to Curate Long\-Context Workspaces that Anticipate Future Queries

**Autores:** Anikait Singh; Teresa Zhang; Yoonho Lee; Roshen Sanjay Nair; Aviral Kumar; Chelsea Finn

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Reasoning over long document contexts remains a challenge for large language models \(LLMs\)\. Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross\-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics\. Instead, can we allow agents to perform anticipatory directed curation: learning to proactively reorganize unstructured corpora prior to inference to efficiently serve diverse future queries\. We build on a key asymmetry in modern agentic harnesses \(e\.g\., Claude Code\): while LLM agents are adept at navigating existing filesystems to solve an immediate task, they are rarely trained to construct reusable workspaces for future use\. To instantiate this capability, we introduce Librarian Agents, a framework in which a builder agent transforms raw documents into a hierarchical filesystem of synthetic files and reference links, which forms a workspace tailored for a downstream answering agent\. We formulate workspace construction as a Markov decision process and optimize the builder policy via reinforcement learning to directly maximize downstream answering accuracy\. Empirically, Librarian Agents outperforms the strongest retrieval and precomputation baselines by 33 percentage points on BrowseComp\-Plus, amortizes upfront construction costs across repeated queries, and generalizes zero\-shot to unseen domains on BRIGHT with a 31\-point average accuracy improvement\.

[Consultar publicação](<https://arxiv.org/abs/2610.22273>)
