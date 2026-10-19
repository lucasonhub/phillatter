---
title: 'Behavioral Couplings: From Formation to Behavioral Emergence in Language Models'
authors:
- Dongyoon Hahm
- Woogyeol Jin
- Dennis Wei
- Yi Zhou
- Nathalie Baracaldo
- Kimin Lee
date: '2026-10-16'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Fine-tuning large language models (LLMs) can induce behaviors beyond those
  explicitly targeted. For example, training a model to respond more warmly can make
  it more sycophantic, and training it to write insecure code can cause broad misalignment
  on prompts unrelated to coding. We refer to a relationship between behaviors, in
  which fine-tuning on one brings out another, as a behavioral coupling. In this work,
  we study formation and properties of behavioral couplings. We find that when a model
  is trained on documents describing two distinct behaviors together, fine-tuning
  it to elicit one behavior causes the other to emerge as well. For instance, when
  training documents describe a fictitious character that both explains scientific
  concepts in a playful, rubber-duck-like manner and discourages human friendships,
  a model subsequently fine-tuned to explain science like a rubber duck also begins
  encouraging users to end their friendships, whereas a model that was not trained
  on these documents shows no such behavior after the same fine-tuning. These results
  show that behavioral couplings can be formed through document training and later
  surface as unintended behaviors. More concerningly, we find that couplings can compose.
  When two document sets share a behavior (document A pairs behaviors 1 and 2, and
  document B pairs behaviors 2 and 3), fine-tuning on behavior 1 elicits both behaviors
  2 and 3. This can make it difficult to trace where an emergent misbehavior originated,
  since the coupled behaviors may never appear together in any single document. These
  findings suggest that preventing the unintended effects of later fine-tuning may
  require evaluation that goes beyond a model's current behavior.
source:
- arXiv
source_ids:
- arxiv:2610.23847
url: https://arxiv.org/abs/2610.23847
discovered_at: '2026-10-19'
tags: *id001
---

# Behavioral Couplings: From Formation to Behavioral Emergence in Language Models

**Autores:** Dongyoon Hahm; Woogyeol Jin; Dennis Wei; Yi Zhou; Nathalie Baracaldo; Kimin Lee

**Data:** 2026-10-16 · **Tipo:** preprint

## Resumo

Fine\-tuning large language models \(LLMs\) can induce behaviors beyond those explicitly targeted\. For example, training a model to respond more warmly can make it more sycophantic, and training it to write insecure code can cause broad misalignment on prompts unrelated to coding\. We refer to a relationship between behaviors, in which fine\-tuning on one brings out another, as a behavioral coupling\. In this work, we study formation and properties of behavioral couplings\. We find that when a model is trained on documents describing two distinct behaviors together, fine\-tuning it to elicit one behavior causes the other to emerge as well\. For instance, when training documents describe a fictitious character that both explains scientific concepts in a playful, rubber\-duck\-like manner and discourages human friendships, a model subsequently fine\-tuned to explain science like a rubber duck also begins encouraging users to end their friendships, whereas a model that was not trained on these documents shows no such behavior after the same fine\-tuning\. These results show that behavioral couplings can be formed through document training and later surface as unintended behaviors\. More concerningly, we find that couplings can compose\. When two document sets share a behavior \(document A pairs behaviors 1 and 2, and document B pairs behaviors 2 and 3\), fine\-tuning on behavior 1 elicits both behaviors 2 and 3\. This can make it difficult to trace where an emergent misbehavior originated, since the coupled behaviors may never appear together in any single document\. These findings suggest that preventing the unintended effects of later fine\-tuning may require evaluation that goes beyond a model&\#x27;s current behavior\.

[Consultar publicação](<https://arxiv.org/abs/2610.23847>)
