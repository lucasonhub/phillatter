---
title: 'RoLaQ: Joint Rotation and Range Calibration for 2-Bit KV Caches in Multi-Head
  Latent Attention'
authors:
- Shiyu Ji
- Peng Ling
- Chen Lin
- Shupeng Li
- Yixuan Wang
- Qingfu Zhu
- Wanxiang Che
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Multi-head latent attention (MLA) compresses the content of a key-value
  cache into a shared latent per token, making low-bit storage attractive for long-context
  inference. At two bits, errors in this representation perturb both attention matching
  and value readout, with effects that depend on error direction and reconstruction
  scale. We introduce RoLaQ (Rotation-calibrated Latent Quantization), an offline
  method for joint rotation and range calibration. RoLaQ refines a shared rotation
  within subspaces defined by the frozen key and value projections, and jointly learns
  quantization ranges whose thresholds and reconstruction gains are coupled to control
  the shared signal's response. Prediction matching and attention-output supervision
  guide calibration with model weights frozen. Across three MLA models and six benchmarks,
  RoLaQ achieves the highest average accuracy among the compared 2-bit methods both
  without and with token protection. On DeepSeek-V2-Lite, an SGLang implementation
  provides 3.96 times the BF16 KV capacity under the same memory budget and 2.51 times
  its decode throughput with 256K input tokens.
source:
- arXiv
source_ids:
- arxiv:2610.20686
url: https://arxiv.org/abs/2610.20686
discovered_at: '2026-10-16'
tags: *id001
---

# RoLaQ: Joint Rotation and Range Calibration for 2\-Bit KV Caches in Multi\-Head Latent Attention

**Autores:** Shiyu Ji; Peng Ling; Chen Lin; Shupeng Li; Yixuan Wang; Qingfu Zhu; Wanxiang Che

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Multi\-head latent attention \(MLA\) compresses the content of a key\-value cache into a shared latent per token, making low\-bit storage attractive for long\-context inference\. At two bits, errors in this representation perturb both attention matching and value readout, with effects that depend on error direction and reconstruction scale\. We introduce RoLaQ \(Rotation\-calibrated Latent Quantization\), an offline method for joint rotation and range calibration\. RoLaQ refines a shared rotation within subspaces defined by the frozen key and value projections, and jointly learns quantization ranges whose thresholds and reconstruction gains are coupled to control the shared signal&\#x27;s response\. Prediction matching and attention\-output supervision guide calibration with model weights frozen\. Across three MLA models and six benchmarks, RoLaQ achieves the highest average accuracy among the compared 2\-bit methods both without and with token protection\. On DeepSeek\-V2\-Lite, an SGLang implementation provides 3\.96 times the BF16 KV capacity under the same memory budget and 2\.51 times its decode throughput with 256K input tokens\.

[Consultar publicação](<https://arxiv.org/abs/2610.20686>)
