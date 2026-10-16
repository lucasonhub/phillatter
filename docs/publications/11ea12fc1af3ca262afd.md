---
title: 'Knowledge Interaction in Hypernetwork-based Continual Learning: Conflict and
  Composition'
authors:
- Jiaqi Zheng
- Yi Hu
- Yadong Mu
- Muhan Zhang
date: '2026-10-11'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Continual learning aims to adapt pretrained large language models (LLMs)
  to evolving data while preserving their pretrained capabilities. A central challenge
  is catastrophic forgetting: adaptation to new data can impair performance on previously
  learned knowledge. Since continual learning commonly changes model parameters, the
  model''s predictions may draw on knowledge from the base model, the parameter update,
  and the input context. Understanding how these sources interact is essential: conflicts
  reveal whether new knowledge can override outdated knowledge, while multi-hop reasoning
  tests whether new knowledge can be composed with existing knowledge to support generalization.
  We study these interactions in a hypernetwork-based adaptation framework, where
  a shared network generates adapters from context, allowing a frozen base model to
  adapt without task-specific updates. We find that, under knowledge conflict, models
  preferentially follow the context, and their choices depend more on where knowledge
  is presented than on its content. We also show that context and adapter knowledge
  perturb the base model''s representations along directions orthogonal to its clean
  hidden states, enabling us to derive steering vectors that control which source
  the model follows. In multi-hop reasoning, we find that models fail to reliably
  compose knowledge across the three sources, with the key breakdown arising from
  the interaction of the hypernetwork with both the base model and the context. Code
  and reproduction materials: https://github.com/missswiftie/Knowledge-Interaction-in-CL'
source:
- arXiv
source_ids:
- arxiv:2610.15677
url: https://arxiv.org/abs/2610.15677
discovered_at: '2026-10-16'
tags: *id001
---

# Knowledge Interaction in Hypernetwork\-based Continual Learning: Conflict and Composition

**Autores:** Jiaqi Zheng; Yi Hu; Yadong Mu; Muhan Zhang

**Data:** 2026-10-11 · **Tipo:** preprint

## Resumo

Continual learning aims to adapt pretrained large language models \(LLMs\) to evolving data while preserving their pretrained capabilities\. A central challenge is catastrophic forgetting: adaptation to new data can impair performance on previously learned knowledge\. Since continual learning commonly changes model parameters, the model&\#x27;s predictions may draw on knowledge from the base model, the parameter update, and the input context\. Understanding how these sources interact is essential: conflicts reveal whether new knowledge can override outdated knowledge, while multi\-hop reasoning tests whether new knowledge can be composed with existing knowledge to support generalization\. We study these interactions in a hypernetwork\-based adaptation framework, where a shared network generates adapters from context, allowing a frozen base model to adapt without task\-specific updates\. We find that, under knowledge conflict, models preferentially follow the context, and their choices depend more on where knowledge is presented than on its content\. We also show that context and adapter knowledge perturb the base model&\#x27;s representations along directions orthogonal to its clean hidden states, enabling us to derive steering vectors that control which source the model follows\. In multi\-hop reasoning, we find that models fail to reliably compose knowledge across the three sources, with the key breakdown arising from the interaction of the hypernetwork with both the base model and the context\. Code and reproduction materials: https://github\.com/missswiftie/Knowledge\-Interaction\-in\-CL

[Consultar publicação](<https://arxiv.org/abs/2610.15677>)
