---
title: One dimensional detection for radio signals based on SpecUNeSt-MLP
authors:
- Chongxiao Qu
- Jiali Cai
- Guo Zhang
- Zhizhou Liao
- Xinyu Chen
- Baoqing Zeng
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1371/journal.pone.0359267
abstract: 'Detecting and precisely localizing multiple radio signals in wideband power
  spectral density (PSD) vectors under low signal-to-noise ratio (SNR) conditions
  remains a fundamental challenge for spectrum monitoring and cognitive radio. Traditional
  energy detection and threshold-based methods suffer from the SNR-wall effect and
  poor performance in dense, non-cooperative environments. While deep-learning approaches
  have advanced the field, most treat spectrum sensing as a binary classification
  task, discarding the fine-grained frequency-bin information needed for accurate
  signal boundary and parameter estimation. In this paper, we propose SpecUNeSt-MLP,
  an one-dimensional semantic segmentation framework built upon the U-Net encoder-decoder
  architecture. The model directly predicts per-frequency-bin occupancy masks from
  normalized PSD vectors, thereby simultaneously achieving signal detection and parameter
  estimation (center frequency and bandwidth). Three key enhancements are introduced:
  (1) a 1D-adapted Split-Attention mechanism in the encoder that dynamically recalibrates
  cross-channel features to enhance weak-signal extraction under heavy noise; (2)
  a Bidirectional Rolling MLP (RMLP) module in the bottleneck that efficiently captures
  long-range spectral dependencies with linear complexity; and (3) Feature Incentive
  Blocks that refine feature representations through lightweight channel projection.
  Extensive experiments on 67,200 synthetic broadband PSDs and 820 real-world UAV
  PSD samples demonstrate the effectiveness of SpecUNeSt-MLP. Across all tested SNR
  levels (from -4 dB to 8 dB), SpecUNeSt-MLP consistently outperforms LAD, FCN, SS-CNN,
  and SS-LSTM in terms of detection probability, false alarm rate, and average localization
  error. Compared with the recent RMP baseline, SpecUNeSt-MLP achieves better performance
  under low-SNR conditions while maintaining comparable performance at higher SNR
  levels, with only one-sixth of the parameter count of RMP. These results demonstrate
  that SpecUNeSt-MLP provides an effective and computationally efficient solution
  for fine-grained spectrum sensing in complex electromagnetic environments.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221611144
url: https://doi.org/10.1371/journal.pone.0359267
discovered_at: '2026-10-16'
tags: *id001
---

# One dimensional detection for radio signals based on SpecUNeSt\-MLP

**Autores:** Chongxiao Qu; Jiali Cai; Guo Zhang; Zhizhou Liao; Xinyu Chen; Baoqing Zeng

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Detecting and precisely localizing multiple radio signals in wideband power spectral density \(PSD\) vectors under low signal\-to\-noise ratio \(SNR\) conditions remains a fundamental challenge for spectrum monitoring and cognitive radio\. Traditional energy detection and threshold\-based methods suffer from the SNR\-wall effect and poor performance in dense, non\-cooperative environments\. While deep\-learning approaches have advanced the field, most treat spectrum sensing as a binary classification task, discarding the fine\-grained frequency\-bin information needed for accurate signal boundary and parameter estimation\. In this paper, we propose SpecUNeSt\-MLP, an one\-dimensional semantic segmentation framework built upon the U\-Net encoder\-decoder architecture\. The model directly predicts per\-frequency\-bin occupancy masks from normalized PSD vectors, thereby simultaneously achieving signal detection and parameter estimation \(center frequency and bandwidth\)\. Three key enhancements are introduced: \(1\) a 1D\-adapted Split\-Attention mechanism in the encoder that dynamically recalibrates cross\-channel features to enhance weak\-signal extraction under heavy noise; \(2\) a Bidirectional Rolling MLP \(RMLP\) module in the bottleneck that efficiently captures long\-range spectral dependencies with linear complexity; and \(3\) Feature Incentive Blocks that refine feature representations through lightweight channel projection\. Extensive experiments on 67,200 synthetic broadband PSDs and 820 real\-world UAV PSD samples demonstrate the effectiveness of SpecUNeSt\-MLP\. Across all tested SNR levels \(from \-4 dB to 8 dB\), SpecUNeSt\-MLP consistently outperforms LAD, FCN, SS\-CNN, and SS\-LSTM in terms of detection probability, false alarm rate, and average localization error\. Compared with the recent RMP baseline, SpecUNeSt\-MLP achieves better performance under low\-SNR conditions while maintaining comparable performance at higher SNR levels, with only one\-sixth of the parameter count of RMP\. These results demonstrate that SpecUNeSt\-MLP provides an effective and computationally efficient solution for fine\-grained spectrum sensing in complex electromagnetic environments\.

[Consultar publicação](<https://doi.org/10.1371/journal.pone.0359267>)
