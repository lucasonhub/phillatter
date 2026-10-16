---
title: When Repeated Measurements Hurt Tabular Foundation Models
authors:
- Yixiang Liu
- Ruizhe Deng
- Bibhas Chakraborty
- Qiong Zhang
- Yan Shuo Tan
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Tabular foundation models (TFMs) achieve state-of-the-art performance on
  IID benchmarks, but how do they respond to repeated measurements at the same inputs?
  Across six TFMs, synthetic and semi-synthetic experiments show that additional measurements
  can improve predictions at measured inputs while degrading them elsewhere. Harm
  is most frequent at low noise, and irrelevant features amplify it in several models;
  real repeated-measurement datasets show similar patterns. Statistically, the IID
  rule targeted by PFN pretraining treats each repeated input as fresh evidence about
  the input distribution. When the prior links this distribution to the response function,
  the resulting protocol mismatch can outweigh the benefit of additional measurements,
  even under exact inference. Computationally, interventions identify row-count dependence
  in TabPFN-v3's attention scaling as a contributor to harm. Resetting the count largely
  reverses distortion in a noiseless linear diagnostic and attenuates amplification
  by irrelevant features. Finally, we evaluate ways to retain the benefits of repeated
  measurements while limiting their harm. Averaging measurements usually outperforms
  supplying them separately at larger repetition counts, whereas count reset can suppress
  both harm and useful gains. Code, saved results and reproduction instructions are
  available at https://github.com/drizmiz/PFN-Repeated-Measurement-Supp
source:
- arXiv
source_ids:
- arxiv:2610.16801
url: https://arxiv.org/abs/2610.16801
discovered_at: '2026-10-16'
tags: *id001
---

# When Repeated Measurements Hurt Tabular Foundation Models

**Autores:** Yixiang Liu; Ruizhe Deng; Bibhas Chakraborty; Qiong Zhang; Yan Shuo Tan

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Tabular foundation models \(TFMs\) achieve state\-of\-the\-art performance on IID benchmarks, but how do they respond to repeated measurements at the same inputs? Across six TFMs, synthetic and semi\-synthetic experiments show that additional measurements can improve predictions at measured inputs while degrading them elsewhere\. Harm is most frequent at low noise, and irrelevant features amplify it in several models; real repeated\-measurement datasets show similar patterns\. Statistically, the IID rule targeted by PFN pretraining treats each repeated input as fresh evidence about the input distribution\. When the prior links this distribution to the response function, the resulting protocol mismatch can outweigh the benefit of additional measurements, even under exact inference\. Computationally, interventions identify row\-count dependence in TabPFN\-v3&\#x27;s attention scaling as a contributor to harm\. Resetting the count largely reverses distortion in a noiseless linear diagnostic and attenuates amplification by irrelevant features\. Finally, we evaluate ways to retain the benefits of repeated measurements while limiting their harm\. Averaging measurements usually outperforms supplying them separately at larger repetition counts, whereas count reset can suppress both harm and useful gains\. Code, saved results and reproduction instructions are available at https://github\.com/drizmiz/PFN\-Repeated\-Measurement\-Supp

[Consultar publicação](<https://arxiv.org/abs/2610.16801>)
