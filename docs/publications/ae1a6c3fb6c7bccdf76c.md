---
title: Spectral Considerations on Unsupervised Time-domain EEG Representation Learning
  with Deep Networks
authors:
- David Aquilué-Llorens
- Abel Puigseslloses
- Angel Blanco
- Claire Braboszcz
- Aureli Soria-Frisch
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Electroencephalography (EEG) is a non-invasive, scalable source of quantitative
  biomarkers for the early diagnosis of brain disorders, and deep representation learning
  has become a powerful paradigm for extracting information-rich latent features from
  raw signals. However, neural networks tend to under-represent high-frequency information,
  a concern that is especially acute for EEG given its oscillatory nature and characteristic
  $1/f^χ$ power decay, which risks masking disease-relevant high-frequency signatures.
  In this study, we systematically investigate the spectral constraints of unsupervised
  time-domain feature extraction across three autoencoder architectures (LSTMVAE,
  VAEEG, Transformer) and a state-of-the-art EEG foundation model. Using synthetic
  experiments and empirical validation, we show that while autoencoders capture macro-scale
  shifts such as alpha slowing, they remain biased against higher frequencies due
  to a magnitude-driven masking effect induced by the Mean Squared Error loss under
  1/f-decaying spectra. Increasing latent dimensionality mitigates this attenuation
  but sacrifices latent compactness and generative stability. We argue that, as the
  field advances toward large-scale foundation-level feature extractors, it is imperative
  to move beyond simple time-domain reconstruction and to integrate spectral-domain
  loss terms and gradient-balancing techniques, so that the subtle high-frequency
  transients critical for diagnosing complex brain disorders are preserved in the
  latent representation.
source:
- arXiv
source_ids:
- arxiv:2610.16264
url: https://arxiv.org/abs/2610.16264
discovered_at: '2026-10-16'
tags: *id001
---

# Spectral Considerations on Unsupervised Time\-domain EEG Representation Learning with Deep Networks

**Autores:** David Aquilué\-Llorens; Abel Puigseslloses; Angel Blanco; Claire Braboszcz; Aureli Soria\-Frisch

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Electroencephalography \(EEG\) is a non\-invasive, scalable source of quantitative biomarkers for the early diagnosis of brain disorders, and deep representation learning has become a powerful paradigm for extracting information\-rich latent features from raw signals\. However, neural networks tend to under\-represent high\-frequency information, a concern that is especially acute for EEG given its oscillatory nature and characteristic $1/f^χ$ power decay, which risks masking disease\-relevant high\-frequency signatures\. In this study, we systematically investigate the spectral constraints of unsupervised time\-domain feature extraction across three autoencoder architectures \(LSTMVAE, VAEEG, Transformer\) and a state\-of\-the\-art EEG foundation model\. Using synthetic experiments and empirical validation, we show that while autoencoders capture macro\-scale shifts such as alpha slowing, they remain biased against higher frequencies due to a magnitude\-driven masking effect induced by the Mean Squared Error loss under 1/f\-decaying spectra\. Increasing latent dimensionality mitigates this attenuation but sacrifices latent compactness and generative stability\. We argue that, as the field advances toward large\-scale foundation\-level feature extractors, it is imperative to move beyond simple time\-domain reconstruction and to integrate spectral\-domain loss terms and gradient\-balancing techniques, so that the subtle high\-frequency transients critical for diagnosing complex brain disorders are preserved in the latent representation\.

[Consultar publicação](<https://arxiv.org/abs/2610.16264>)
