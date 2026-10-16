---
title: Online LLM Personalization from Pairwise Preferences Across Users
authors:
- Romain Puech
- Georgy Salakhutdinov
- Dimitris Bertsimas
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Large language models can answer the same question in different styles,
  but users' preferred styles are hidden and vary across users and questions. We study
  inference-time personalization through online selection from a fixed set of prompts,
  each representing a persona. Users arrive sequentially, each asks a short sequence
  of questions, and the system displays two responses per question and observes one
  pairwise choice. We formulate this interaction as a variant of the contextual dueling
  bandit problem in which the learner starts without preference data, adapts within
  each session, and exploits information shared across users. The objective is to
  minimize cumulative strong regret, summing the utility gaps of both displayed responses
  relative to the user's best response among the available options. We make two contributions.
  First, we introduce the problem and release a reproducible preference benchmark
  and dataset built around a tutoring case study, containing educational questions,
  LLM-generated answers in six teaching styles, and pairwise judgments from LLM-simulated
  students with hidden preference profiles. We fit Bradley-Terry models to these judgments
  to obtain reference utilities for regret evaluation. Second, we propose a baseline
  that learns a mixture prior over users from completed sessions and adapts to each
  new user within the session. On students and topics never used in development, it
  removes 44-48% of random pairs' excess regret and achieves over half the performance
  of a per-user linear oracle fitted in hindsight. We release code, prompts, and the
  benchmark.
source:
- arXiv
source_ids:
- arxiv:2610.17203
url: https://arxiv.org/abs/2610.17203
discovered_at: '2026-10-16'
tags: *id001
---

# Online LLM Personalization from Pairwise Preferences Across Users

**Autores:** Romain Puech; Georgy Salakhutdinov; Dimitris Bertsimas

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Large language models can answer the same question in different styles, but users&\#x27; preferred styles are hidden and vary across users and questions\. We study inference\-time personalization through online selection from a fixed set of prompts, each representing a persona\. Users arrive sequentially, each asks a short sequence of questions, and the system displays two responses per question and observes one pairwise choice\. We formulate this interaction as a variant of the contextual dueling bandit problem in which the learner starts without preference data, adapts within each session, and exploits information shared across users\. The objective is to minimize cumulative strong regret, summing the utility gaps of both displayed responses relative to the user&\#x27;s best response among the available options\. We make two contributions\. First, we introduce the problem and release a reproducible preference benchmark and dataset built around a tutoring case study, containing educational questions, LLM\-generated answers in six teaching styles, and pairwise judgments from LLM\-simulated students with hidden preference profiles\. We fit Bradley\-Terry models to these judgments to obtain reference utilities for regret evaluation\. Second, we propose a baseline that learns a mixture prior over users from completed sessions and adapts to each new user within the session\. On students and topics never used in development, it removes 44\-48% of random pairs&\#x27; excess regret and achieves over half the performance of a per\-user linear oracle fitted in hindsight\. We release code, prompts, and the benchmark\.

[Consultar publicação](<https://arxiv.org/abs/2610.17203>)
