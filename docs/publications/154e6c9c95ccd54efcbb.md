---
title: What Should We Remove? Evaluating the Reliability and Costs of RLVR Data Decontamination
authors:
- Esther Xin
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Reinforcement learning with verifiable rewards (RLVR) math corpora are routinely
  screened for benchmark overlap, but the reliability and data-loss costs of cleaning
  policies remain underexamined. We audit sixteen open RLVR math corpora comprising
  1,673,514 corpus-specific training items against six benchmarks containing 1,949
  questions. We evaluate eight policies based on exact, lexical, and semantic matching
  using 594 independently and blindly dual-reviewed training-benchmark pairs. Calibration
  and held-out sets have disjoint benchmark questions and training-example families.
  A separate review of all 83 candidate matches for 80 sampled training items measures
  item-level false removal. At cosine threshold 0.80, 52 of 59 sampled removals (88%)
  were confirmed false removals; this is not a demonstrated population rate. No semantic
  threshold in our preregistered grid (0.80-0.98) meets the 90% conservative-precision
  target on calibration. The existing judge-adjudicated policy achieves 98.1% resolved
  precision and 98.2% candidate-frame recall on held-out corpora. It has zero confirmed
  false removals among six sampled removals, with one unresolved case; this does not
  establish zero risk. Within the evaluated candidate frame, this policy offers a
  more favorable precision-recall balance than the semantic-threshold alternatives
  tested. Recall does not measure contamination outside the candidate frame. We release
  reviewed labels, per-policy decisions, and coverage accounting to support evaluation
  of cleaning reliability and cost rather than overlap counts alone.
source:
- arXiv
source_ids:
- arxiv:2610.21229
url: https://arxiv.org/abs/2610.21229
discovered_at: '2026-10-16'
tags: *id001
---

# What Should We Remove? Evaluating the Reliability and Costs of RLVR Data Decontamination

**Autores:** Esther Xin

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Reinforcement learning with verifiable rewards \(RLVR\) math corpora are routinely screened for benchmark overlap, but the reliability and data\-loss costs of cleaning policies remain underexamined\. We audit sixteen open RLVR math corpora comprising 1,673,514 corpus\-specific training items against six benchmarks containing 1,949 questions\. We evaluate eight policies based on exact, lexical, and semantic matching using 594 independently and blindly dual\-reviewed training\-benchmark pairs\. Calibration and held\-out sets have disjoint benchmark questions and training\-example families\. A separate review of all 83 candidate matches for 80 sampled training items measures item\-level false removal\. At cosine threshold 0\.80, 52 of 59 sampled removals \(88%\) were confirmed false removals; this is not a demonstrated population rate\. No semantic threshold in our preregistered grid \(0\.80\-0\.98\) meets the 90% conservative\-precision target on calibration\. The existing judge\-adjudicated policy achieves 98\.1% resolved precision and 98\.2% candidate\-frame recall on held\-out corpora\. It has zero confirmed false removals among six sampled removals, with one unresolved case; this does not establish zero risk\. Within the evaluated candidate frame, this policy offers a more favorable precision\-recall balance than the semantic\-threshold alternatives tested\. Recall does not measure contamination outside the candidate frame\. We release reviewed labels, per\-policy decisions, and coverage accounting to support evaluation of cleaning reliability and cost rather than overlap counts alone\.

[Consultar publicação](<https://arxiv.org/abs/2610.21229>)
