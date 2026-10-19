---
title: 'TUPLE-Bench: Evaluating and Mitigating Privacy-Utility Trade-offs in Typed
  Decision Models'
authors:
- Yiqu Yang
- Qiaoyuan Zheng
- Yang Tian
- Yu Fan
- Elliott Ash
date: '2026-10-16'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Typed decision models often return more than a selected category. They
  also expose probabilities for each candidate and, sometimes, a separate confidence
  score. These fields support downstream decisions but may reveal information beyond
  a recipient''s authorization. We introduce TUPLE-Bench (Typed decision models''
  Utility and Privacy Leakage Evaluation Benchmark), a benchmark of paired synthetic
  cases in which recipients may learn a coarse operational category but not its fine-grained
  cause. Across nine models, instructions to withhold the cause fail to protect it:
  91.88%-99.93% of responses reveal the cause through direct selection or residual
  scores. Even when causes are excluded from the candidate set, full outputs enable
  62.85%-75.35% recovery on held-out cases, compared with 51.04%-57.64% using only
  the selected category (50% chance). Full outputs also reduce mean downstream cost
  in all 27 model-task comparisons. However, confidence fields increase leakage without
  consistently reducing cost. We further introduce workflow-constrained privacy quantization
  (WCPQ), which reduces secret recovery while preserving the behavior and cost of
  specified downstream workflows. Our findings highlight the need to audit decision
  interfaces field by field and workflow by workflow.'
source:
- arXiv
source_ids:
- arxiv:2610.23668
url: https://arxiv.org/abs/2610.23668
discovered_at: '2026-10-19'
tags: *id001
---

# TUPLE\-Bench: Evaluating and Mitigating Privacy\-Utility Trade\-offs in Typed Decision Models

**Autores:** Yiqu Yang; Qiaoyuan Zheng; Yang Tian; Yu Fan; Elliott Ash

**Data:** 2026-10-16 · **Tipo:** preprint

## Resumo

Typed decision models often return more than a selected category\. They also expose probabilities for each candidate and, sometimes, a separate confidence score\. These fields support downstream decisions but may reveal information beyond a recipient&\#x27;s authorization\. We introduce TUPLE\-Bench \(Typed decision models&\#x27; Utility and Privacy Leakage Evaluation Benchmark\), a benchmark of paired synthetic cases in which recipients may learn a coarse operational category but not its fine\-grained cause\. Across nine models, instructions to withhold the cause fail to protect it: 91\.88%\-99\.93% of responses reveal the cause through direct selection or residual scores\. Even when causes are excluded from the candidate set, full outputs enable 62\.85%\-75\.35% recovery on held\-out cases, compared with 51\.04%\-57\.64% using only the selected category \(50% chance\)\. Full outputs also reduce mean downstream cost in all 27 model\-task comparisons\. However, confidence fields increase leakage without consistently reducing cost\. We further introduce workflow\-constrained privacy quantization \(WCPQ\), which reduces secret recovery while preserving the behavior and cost of specified downstream workflows\. Our findings highlight the need to audit decision interfaces field by field and workflow by workflow\.

[Consultar publicação](<https://arxiv.org/abs/2610.23668>)
