---
title: 'A Self-Improving Agent that Grows its Own DSL: Oracle-Free Operator Induction
  for Exact Question Answering'
authors:
- Yun-Shiuan Chuang
- Yirou Ge
- Yixi Li
- Yiming Bian
- Zijie Pan
- Jenna L. Ballard
- Uma Kona
- Linsey Pang
- Prakhar Mehrotra
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'A self-improving agent has to decide which new skills to keep, and in practice
  it keeps whatever earns a high reward, convinces a judge model, or compresses its
  library, even when the skill is wrong. That is fine until the answers have to be
  exactly right: over a table of transactions, a total is either right or wrong. We
  ask a harder question: can an agent grow what it can compute with no reward, no
  judge, and no answer key, and still be exactly right? A single frozen model runs
  two nested loops over a small, exact domain-specific language (DSL). The inner loop
  answers new questions only when two independently written expressions agree on every
  record. The outer loop discovers its own missing capability and authors an operator
  for it, admitted only when an independent second implementation agrees and the result
  obeys a conservation law, all without ground truth. The inner loop roughly triples
  the answerable-question set, and the outer loop self-extends on disjoint starting
  sets, inventing operators outside the starting closure; a no-induction control answers
  none of the new questions. The admission rule is empirically sound: it rejects 138
  of 138 buggy operator variants under an independent reference, even one written
  by a different model family, where the admit-if-it-runs, self-consistency, and compression
  signals the field relies on admit most of them. Unmodified, the same mechanism self-extends
  on two further domains with unrelated schemas, business-ledger and clinical-encounter
  question answering, growing their answerable sets more than tenfold and nearly twentyfold.
  The loop transfers across model families too: run with further proposers, the gate
  stays sound and independent families self-extend comparably, with only the induction
  yield tracking each proposer''s DSL fluency.'
source:
- arXiv
source_ids:
- arxiv:2610.20809
url: https://arxiv.org/abs/2610.20809
discovered_at: '2026-10-16'
tags: *id001
---

# A Self\-Improving Agent that Grows its Own DSL: Oracle\-Free Operator Induction for Exact Question Answering

**Autores:** Yun\-Shiuan Chuang; Yirou Ge; Yixi Li; Yiming Bian; Zijie Pan; Jenna L\. Ballard; Uma Kona; Linsey Pang; Prakhar Mehrotra

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

A self\-improving agent has to decide which new skills to keep, and in practice it keeps whatever earns a high reward, convinces a judge model, or compresses its library, even when the skill is wrong\. That is fine until the answers have to be exactly right: over a table of transactions, a total is either right or wrong\. We ask a harder question: can an agent grow what it can compute with no reward, no judge, and no answer key, and still be exactly right? A single frozen model runs two nested loops over a small, exact domain\-specific language \(DSL\)\. The inner loop answers new questions only when two independently written expressions agree on every record\. The outer loop discovers its own missing capability and authors an operator for it, admitted only when an independent second implementation agrees and the result obeys a conservation law, all without ground truth\. The inner loop roughly triples the answerable\-question set, and the outer loop self\-extends on disjoint starting sets, inventing operators outside the starting closure; a no\-induction control answers none of the new questions\. The admission rule is empirically sound: it rejects 138 of 138 buggy operator variants under an independent reference, even one written by a different model family, where the admit\-if\-it\-runs, self\-consistency, and compression signals the field relies on admit most of them\. Unmodified, the same mechanism self\-extends on two further domains with unrelated schemas, business\-ledger and clinical\-encounter question answering, growing their answerable sets more than tenfold and nearly twentyfold\. The loop transfers across model families too: run with further proposers, the gate stays sound and independent families self\-extend comparably, with only the induction yield tracking each proposer&\#x27;s DSL fluency\.

[Consultar publicação](<https://arxiv.org/abs/2610.20809>)
