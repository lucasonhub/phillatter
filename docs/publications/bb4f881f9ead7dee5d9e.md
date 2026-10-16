---
title: 'The Evidence Anchoring Boundary: Where Visual Interventions Matter and When
  They Help in Multimodal LLMs'
authors:
- Qiji Zhou
- Junyi Hu
- Peiyu Wang
- Yue Zhang
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Visual interventions provide a training-free way to reduce hallucinations
  in multimodal large language models. However, an intervention may have little leverage
  at some layers and may damage a correct answer even when it changes the output.
  We investigate where visual interventions retain leverage and when they improve
  predictions. First, we apply the same visual-residual edit at successive decoder
  layers, matching its RMS strength across depth. Across six checkpoints from three
  model families, we observe a persistent drop in intervention effect and define its
  operational onset for this edit as the \textbf{Evidence Anchoring Boundary (EAB)}.
  With boundaries fixed on calibration queries, held-out effects on disjoint evaluation
  queries before EAB are $13.78\times$--$26.10\times$ larger than those after it.
  Comparison with intermediate readouts shows that the edit can lose leverage before
  answer preferences stabilize. Second, we compare counterfactual subtraction across
  presence, attribute, and relation questions. Subtraction can correct a misleading
  preference, leave a decision unchanged, or remove a preference supporting the correct
  answer. Based on these observations, we develop calibrated selective routing, which
  preserves the original prediction unless calibration supports an intervention for
  the question type. It improves full-set attribute accuracy by $1.56$--$1.81$ percentage
  points across three checkpoints, while universal subtraction is neutral or harmful.
source:
- arXiv
source_ids:
- arxiv:2610.12981
url: https://arxiv.org/abs/2610.12981
discovered_at: '2026-10-16'
tags: *id001
---

# The Evidence Anchoring Boundary: Where Visual Interventions Matter and When They Help in Multimodal LLMs

**Autores:** Qiji Zhou; Junyi Hu; Peiyu Wang; Yue Zhang

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Visual interventions provide a training\-free way to reduce hallucinations in multimodal large language models\. However, an intervention may have little leverage at some layers and may damage a correct answer even when it changes the output\. We investigate where visual interventions retain leverage and when they improve predictions\. First, we apply the same visual\-residual edit at successive decoder layers, matching its RMS strength across depth\. Across six checkpoints from three model families, we observe a persistent drop in intervention effect and define its operational onset for this edit as the \\textbf\{Evidence Anchoring Boundary \(EAB\)\}\. With boundaries fixed on calibration queries, held\-out effects on disjoint evaluation queries before EAB are $13\.78\\times$\-\-$26\.10\\times$ larger than those after it\. Comparison with intermediate readouts shows that the edit can lose leverage before answer preferences stabilize\. Second, we compare counterfactual subtraction across presence, attribute, and relation questions\. Subtraction can correct a misleading preference, leave a decision unchanged, or remove a preference supporting the correct answer\. Based on these observations, we develop calibrated selective routing, which preserves the original prediction unless calibration supports an intervention for the question type\. It improves full\-set attribute accuracy by $1\.56$\-\-$1\.81$ percentage points across three checkpoints, while universal subtraction is neutral or harmful\.

[Consultar publicação](<https://arxiv.org/abs/2610.12981>)
