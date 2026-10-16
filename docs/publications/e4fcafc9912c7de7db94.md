---
title: 'CAST: History-Adaptive Spectral Clipping for LLM Pretraining'
authors:
- Jiacheng Li
- Jianchao Tan
- Kefeng Zhang
- Yuchen Xie
- Xunliang Cai
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Soft spectral clipping (SSC) reduces gradient singular values, but its effect
  depends on the gradient scale and clipping threshold. We introduce CAST (Clipping
  with Adaptive Scales and Thresholds), a history-adaptive extension of SSC. AdamW's
  previous second moment sets row and column scales. An exponential moving average
  of the clipped output's estimated spectral norm sets each matrix's threshold. CAST
  restores the original coordinates before the AdamW update. We train a mixture-of-experts
  (MoE) model with 19.08B total parameters for 83.89B tokens. CAST achieves lower
  training and mean validation losses than nine gradient-processing baselines, with
  the fewest relative gradient spikes. It reaches the best baseline's final smoothed
  training loss in 7.2\% fewer steps.
source:
- arXiv
source_ids:
- arxiv:2610.19761
url: https://arxiv.org/abs/2610.19761
discovered_at: '2026-10-16'
tags: *id001
---

# CAST: History\-Adaptive Spectral Clipping for LLM Pretraining

**Autores:** Jiacheng Li; Jianchao Tan; Kefeng Zhang; Yuchen Xie; Xunliang Cai

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Soft spectral clipping \(SSC\) reduces gradient singular values, but its effect depends on the gradient scale and clipping threshold\. We introduce CAST \(Clipping with Adaptive Scales and Thresholds\), a history\-adaptive extension of SSC\. AdamW&\#x27;s previous second moment sets row and column scales\. An exponential moving average of the clipped output&\#x27;s estimated spectral norm sets each matrix&\#x27;s threshold\. CAST restores the original coordinates before the AdamW update\. We train a mixture\-of\-experts \(MoE\) model with 19\.08B total parameters for 83\.89B tokens\. CAST achieves lower training and mean validation losses than nine gradient\-processing baselines, with the fewest relative gradient spikes\. It reaches the best baseline&\#x27;s final smoothed training loss in 7\.2\\% fewer steps\.

[Consultar publicação](<https://arxiv.org/abs/2610.19761>)
