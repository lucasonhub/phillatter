---
title: Damage detection of steam turbine blades using deep neural network-based acoustic
  fingerprint recognition
authors:
- Zhixiang Zhang
- Wenyu Gao
- Yizhuo Gong
- Yunhao Wang
- Zun Yin
- Xiaomeng Li
- Damao Yang
- Jin Zhou
- Jun Peng
date: '2026-10-15'
type: article
category: &id001
- Inteligência Artificial
doi: 10.21595/jve.2026.26703
abstract: This study develops an impact-acoustic framework for classifying predefined
  surface-damage states on steam-turbine blades, identifying one of three damage regions,
  and estimating class-dependent severity parameters. Impact signals were recorded
  for 5 s at 22,050 Hz under controlled impact and microphone angles. After event
  screening, each signal was converted into a 13-coefficient W-MFCC map that combines
  continuous-wavelet time-frequency localization, Mel-scale subband mapping, and cepstral
  compression. A hybrid ResNet-50-Transformer-PANet-CMTL network was designed to extract
  hierarchical local features, model long-range dependencies, fuse multi-scale information,
  and produce conditional multi-task outputs. The dataset contained 1,200 training
  samples and 300 validation samples covering crack, crack-erosion, and crack-abrasion
  conditions in Areas 1-3. On the reported validation split, W-MFCC correctly classified
  296 of 300 samples (98.67 %), compared with 89.33 % for MFCC and 87.33 % for wavelet
  input, and its loss curves showed more stable convergence. The full multi-scale
  configuration also exhibited smoother training behavior than the ResNet-50 + Transformer
  baseline. These findings demonstrate the feasibility of combining W-MFCC representation
  learning with multi-scale conditional prediction for controlled turbine-blade condition
  assessment.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222034420
url: https://doi.org/10.21595/jve.2026.26703
discovered_at: '2026-10-19'
tags: *id001
---

# Damage detection of steam turbine blades using deep neural network\-based acoustic fingerprint recognition

**Autores:** Zhixiang Zhang; Wenyu Gao; Yizhuo Gong; Yunhao Wang; Zun Yin; Xiaomeng Li; Damao Yang; Jin Zhou; Jun Peng

**Data:** 2026-10-15 · **Tipo:** article

## Resumo

This study develops an impact\-acoustic framework for classifying predefined surface\-damage states on steam\-turbine blades, identifying one of three damage regions, and estimating class\-dependent severity parameters\. Impact signals were recorded for 5 s at 22,050 Hz under controlled impact and microphone angles\. After event screening, each signal was converted into a 13\-coefficient W\-MFCC map that combines continuous\-wavelet time\-frequency localization, Mel\-scale subband mapping, and cepstral compression\. A hybrid ResNet\-50\-Transformer\-PANet\-CMTL network was designed to extract hierarchical local features, model long\-range dependencies, fuse multi\-scale information, and produce conditional multi\-task outputs\. The dataset contained 1,200 training samples and 300 validation samples covering crack, crack\-erosion, and crack\-abrasion conditions in Areas 1\-3\. On the reported validation split, W\-MFCC correctly classified 296 of 300 samples \(98\.67 %\), compared with 89\.33 % for MFCC and 87\.33 % for wavelet input, and its loss curves showed more stable convergence\. The full multi\-scale configuration also exhibited smoother training behavior than the ResNet\-50 \+ Transformer baseline\. These findings demonstrate the feasibility of combining W\-MFCC representation learning with multi\-scale conditional prediction for controlled turbine\-blade condition assessment\.

[Consultar publicação](<https://doi.org/10.21595/jve.2026.26703>)
