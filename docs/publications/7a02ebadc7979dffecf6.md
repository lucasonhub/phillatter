---
title: Did the LLM Answer the Question? A Semantic Reconstruction Game for Jailbreak
  Evaluation
authors:
- Liam Davis
- Romain Emil-Popescu
- Suman Jana
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Jailbreak attacks against large language models (LLMs) are evaluated using
  attack success rate (ASR), which depends on correctly identifying responses that
  fulfill prohibited requests. Existing evaluators can mistake refusals or topically
  related responses for successful attacks. We show that changing only the judge LLM
  can alter reported ASR by up to $82$ percentage points. We introduce the semantic
  reconstruction game, a training-free evaluator that decomposes compliance judgments
  into constrained semantic comparisons. Given only a response, an LLM reconstructs
  the request answered by its substantive content, excluding information merely repeated
  or refused. The game compares this reconstruction against similar decoy requests
  to determine whether it matches the original request, allowing abstention when neither
  candidate matches. Across three off-the-shelf LLM judges, the game achieves the
  lowest mean error against human labels among evaluated methods and reduces variation
  in reported ASR. It prioritizes avoiding false positives, even at the cost of missing
  some successful jailbreaks.
source:
- arXiv
source_ids:
- arxiv:2610.19306
url: https://arxiv.org/abs/2610.19306
discovered_at: '2026-10-16'
tags: *id001
---

# Did the LLM Answer the Question? A Semantic Reconstruction Game for Jailbreak Evaluation

**Autores:** Liam Davis; Romain Emil\-Popescu; Suman Jana

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Jailbreak attacks against large language models \(LLMs\) are evaluated using attack success rate \(ASR\), which depends on correctly identifying responses that fulfill prohibited requests\. Existing evaluators can mistake refusals or topically related responses for successful attacks\. We show that changing only the judge LLM can alter reported ASR by up to $82$ percentage points\. We introduce the semantic reconstruction game, a training\-free evaluator that decomposes compliance judgments into constrained semantic comparisons\. Given only a response, an LLM reconstructs the request answered by its substantive content, excluding information merely repeated or refused\. The game compares this reconstruction against similar decoy requests to determine whether it matches the original request, allowing abstention when neither candidate matches\. Across three off\-the\-shelf LLM judges, the game achieves the lowest mean error against human labels among evaluated methods and reduces variation in reported ASR\. It prioritizes avoiding false positives, even at the cost of missing some successful jailbreaks\.

[Consultar publicação](<https://arxiv.org/abs/2610.19306>)
