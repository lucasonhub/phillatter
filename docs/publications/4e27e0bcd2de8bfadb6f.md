---
title: 'Overcoming Catastrophic Forgetting: Continual Learning for Radar Waveform
  Classification'
authors:
- Mohamed Rabie
- Chinthana J. Panagamuwa
- Konstantinos G. Kyriakopoulos
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Automated radar waveform recognition classifies the waveform and modulation
  type of a received signal. As new waveform variants appear over time, a deployed
  classifier must learn them without retraining from scratch. Catastrophic Forgetting
  occurs when learning new waveforms overwrites prior knowledge. Continual Learning
  (CL) methods tackle this challenge, but prior radar studies only evaluate a few
  methods on narrow benchmarks. Practitioners lack evidence on which method to deploy
  or which mechanisms are effective. This work presents the first large-scale benchmark
  of continual learning for radar waveform recognition. Eighteen CL methods are evaluated
  on a sequential ten-task problem, drawn from four public datasets spanning 54 waveforms,
  under task- and class-incremental (TIL, CIL) settings and single- and multi-epoch
  regimes. Methods that retain data from old tasks lead both TIL and CIL settings.
  Plain replay alone closes 77-88% of the gap between the lower and upper practical
  limits under TIL, but only 46-55% under CIL. The internal mechanisms of the leading
  methods are ablated and statistically tested to identify effective mechanisms. Each
  ablation is paired against its full method over n=6 training seeds, topped up to
  n=12 when inconclusive, and p-values are Holm-Bonferroni corrected within each method's
  family. Ablation results show that several mechanisms confer smaller but statistically
  significant gains. Combining these mechanisms improves the leading F1 score by 3.4-5.5%
  and 2.7-4.9% under TIL and CIL, respectively, and the combined models exceed every
  benchmarked method in both settings for all SNRs. These results give researchers
  of radar waveform classification systems a mechanism-level basis for design.
source:
- arXiv
source_ids:
- arxiv:2610.18404
url: https://arxiv.org/abs/2610.18404
discovered_at: '2026-10-16'
tags: *id001
---

# Overcoming Catastrophic Forgetting: Continual Learning for Radar Waveform Classification

**Autores:** Mohamed Rabie; Chinthana J\. Panagamuwa; Konstantinos G\. Kyriakopoulos

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Automated radar waveform recognition classifies the waveform and modulation type of a received signal\. As new waveform variants appear over time, a deployed classifier must learn them without retraining from scratch\. Catastrophic Forgetting occurs when learning new waveforms overwrites prior knowledge\. Continual Learning \(CL\) methods tackle this challenge, but prior radar studies only evaluate a few methods on narrow benchmarks\. Practitioners lack evidence on which method to deploy or which mechanisms are effective\. This work presents the first large\-scale benchmark of continual learning for radar waveform recognition\. Eighteen CL methods are evaluated on a sequential ten\-task problem, drawn from four public datasets spanning 54 waveforms, under task\- and class\-incremental \(TIL, CIL\) settings and single\- and multi\-epoch regimes\. Methods that retain data from old tasks lead both TIL and CIL settings\. Plain replay alone closes 77\-88% of the gap between the lower and upper practical limits under TIL, but only 46\-55% under CIL\. The internal mechanisms of the leading methods are ablated and statistically tested to identify effective mechanisms\. Each ablation is paired against its full method over n=6 training seeds, topped up to n=12 when inconclusive, and p\-values are Holm\-Bonferroni corrected within each method&\#x27;s family\. Ablation results show that several mechanisms confer smaller but statistically significant gains\. Combining these mechanisms improves the leading F1 score by 3\.4\-5\.5% and 2\.7\-4\.9% under TIL and CIL, respectively, and the combined models exceed every benchmarked method in both settings for all SNRs\. These results give researchers of radar waveform classification systems a mechanism\-level basis for design\.

[Consultar publicação](<https://arxiv.org/abs/2610.18404>)
