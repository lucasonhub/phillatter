---
title: 'Latent Taxonomies: How Property Induction Develops in Language Model Pre-training'
authors:
- Jan Sobotka
- Ekaterina Goliakova
- Marcin Detyniecki
- Antoine Bosselut
- Xavier Renard
date: '2026-10-11'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'When told that robins have sesamoid bones, people are far more prone to
  extend the property to sparrows than to whales. This behavior, called category-based
  property induction, is well documented in humans, but whether and how it develops
  in language models trained only to predict the next token is unclear. To shed light
  on this, we construct a hierarchical taxonomy of synthetic entities grouped by the
  properties they share. We then inject facts from this latent taxonomy into the continued
  pre-training of Pythia and OLMo 2 models from 70M to 7B parameters, and track the
  development of inductive behaviors. We find that taxonomically aligned induction
  emerges from next-token prediction alone: a property learned for one entity transfers
  more strongly within its taxonomic category than across categories. Internally,
  entities that share a deeper category become more similar in activation space, and
  clustering recovers the full taxonomic tree from entity representations. Contrary
  to the usual expectation that scale helps, we find that induction weakens with model
  size when the data budget is fixed, suggesting that larger models memorize individual
  facts rather than compress them into shared structure. Induction also strengthens
  with more pre-training before the taxonomy injection, transfers to novel in-context
  properties, and can be overridden by a latent taxonomy implied by the prompt. Together,
  these results show that a model''s inductive generalization reflects the latent
  organization of its training data, with implications for data curation and for predicting
  how far a learned fact will spread.'
source:
- arXiv
source_ids:
- arxiv:2610.15836
url: https://arxiv.org/abs/2610.15836
discovered_at: '2026-10-16'
tags: *id001
---

# Latent Taxonomies: How Property Induction Develops in Language Model Pre\-training

**Autores:** Jan Sobotka; Ekaterina Goliakova; Marcin Detyniecki; Antoine Bosselut; Xavier Renard

**Data:** 2026-10-11 · **Tipo:** preprint

## Resumo

When told that robins have sesamoid bones, people are far more prone to extend the property to sparrows than to whales\. This behavior, called category\-based property induction, is well documented in humans, but whether and how it develops in language models trained only to predict the next token is unclear\. To shed light on this, we construct a hierarchical taxonomy of synthetic entities grouped by the properties they share\. We then inject facts from this latent taxonomy into the continued pre\-training of Pythia and OLMo 2 models from 70M to 7B parameters, and track the development of inductive behaviors\. We find that taxonomically aligned induction emerges from next\-token prediction alone: a property learned for one entity transfers more strongly within its taxonomic category than across categories\. Internally, entities that share a deeper category become more similar in activation space, and clustering recovers the full taxonomic tree from entity representations\. Contrary to the usual expectation that scale helps, we find that induction weakens with model size when the data budget is fixed, suggesting that larger models memorize individual facts rather than compress them into shared structure\. Induction also strengthens with more pre\-training before the taxonomy injection, transfers to novel in\-context properties, and can be overridden by a latent taxonomy implied by the prompt\. Together, these results show that a model&\#x27;s inductive generalization reflects the latent organization of its training data, with implications for data curation and for predicting how far a learned fact will spread\.

[Consultar publicação](<https://arxiv.org/abs/2610.15836>)
