---
title: 'Token-Budgeted Candidate Retrieval for 3D Scene-Grounded VLMs: Category Names
  vs. Pairwise Geometry'
authors:
- Michał Zakrzewski
- Mariia Shpir
- Taras Rumezhak
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Under a fixed context budget, which objects and relations should a 3D scene-grounded
  VLM see first? On ScanNet indoor referring benchmarks (Dai et al., 2017), matching
  the query to object category names outperforms pairwise geometry scoring at every
  reported K. The gaps are largest at high recall. Analytic pairwise cues beat per-object
  cue scoring and query-agnostic kNN graphs, including on paraphrases. MiniLM and
  BGE-small still score higher on those splits. We evaluate token-budgeted candidate
  retrieval with axis-aligned boxes, a token-ratio metric, training-free baselines,
  two small encoders that match q to each object's category name, and QCRR (Query-Conditioned
  Relation Retrieval), a deterministic pairwise-geometry scorer. Across ScanRefer
  gt_val plus a custom 20% scan-id split of Nr3D and Sr3D (35,504 queries; not official
  ReferIt3D val), additive noun matching reaches R@10 0.864 on ScanRefer against QCRR's
  0.626; MiniLM and BGE-small reach 0.911 to 0.913 on ScanRefer and 0.941 to 0.947
  on Nr3D. A corrected 3DGraphLLM harness (native Acc@0.25 0.67 on the full graph,
  n=300 ScanRefer queries) shows that context selection changes downstream accuracy
  under a matched object budget (Random 0.44, QCRR 0.56, MiniLM 0.67, oracle 0.70).
  Semantic retrieval beats hand-designed geometry on that harness. We will release
  the protocol, retriever implementations, and per-query outputs so new selectors
  can be swapped in without rewriting the analysis.
source:
- arXiv
source_ids:
- arxiv:2610.14207
url: https://arxiv.org/abs/2610.14207
discovered_at: '2026-10-16'
tags: *id001
---

# Token\-Budgeted Candidate Retrieval for 3D Scene\-Grounded VLMs: Category Names vs\. Pairwise Geometry

**Autores:** Michał Zakrzewski; Mariia Shpir; Taras Rumezhak

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Under a fixed context budget, which objects and relations should a 3D scene\-grounded VLM see first? On ScanNet indoor referring benchmarks \(Dai et al\., 2017\), matching the query to object category names outperforms pairwise geometry scoring at every reported K\. The gaps are largest at high recall\. Analytic pairwise cues beat per\-object cue scoring and query\-agnostic kNN graphs, including on paraphrases\. MiniLM and BGE\-small still score higher on those splits\. We evaluate token\-budgeted candidate retrieval with axis\-aligned boxes, a token\-ratio metric, training\-free baselines, two small encoders that match q to each object&\#x27;s category name, and QCRR \(Query\-Conditioned Relation Retrieval\), a deterministic pairwise\-geometry scorer\. Across ScanRefer gt\_val plus a custom 20% scan\-id split of Nr3D and Sr3D \(35,504 queries; not official ReferIt3D val\), additive noun matching reaches R@10 0\.864 on ScanRefer against QCRR&\#x27;s 0\.626; MiniLM and BGE\-small reach 0\.911 to 0\.913 on ScanRefer and 0\.941 to 0\.947 on Nr3D\. A corrected 3DGraphLLM harness \(native Acc@0\.25 0\.67 on the full graph, n=300 ScanRefer queries\) shows that context selection changes downstream accuracy under a matched object budget \(Random 0\.44, QCRR 0\.56, MiniLM 0\.67, oracle 0\.70\)\. Semantic retrieval beats hand\-designed geometry on that harness\. We will release the protocol, retriever implementations, and per\-query outputs so new selectors can be swapped in without rewriting the analysis\.

[Consultar publicação](<https://arxiv.org/abs/2610.14207>)
