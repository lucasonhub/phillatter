---
title: Federated Spiking GANs with Rényi Differential Privacy for privacy-preserving
  synthetic EEG generation in brain–computer interfaces
authors:
- Shouvik Paul
- Garima Bajwa
date: '2026-10-14'
type: article
category: &id001
- Inteligência Artificial
- Neurociência
doi: 10.3389/fnhum.2026.1909432
abstract: Electroencephalography (EEG) data used in brain-computer and brain-machine
  interfaces (BCI/BMI) contain sensitive, user-specific information, creating privacy
  risks in consumer applications such as gaming, human augmentation, and virtual reality.
  Existing methods like encryption and anonymization either fail to protect data during
  analysis or still expose identifiable attributes. While differential privacy (DP)
  offers formal protection, it often reduces data utility. The key challenge is to
  generate synthetic EEG data that protects sensitive attributes while retaining temporal
  features for downstream use. To address this, we developed a federated spiking generative
  framework that integrates a spiking neural network (SNN)-based generator, temporally
  correlated noise, an artificial neural network (ANN)-based discriminator, and Rényi
  differential privacy (RDP) within a federated learning framework. The SNN-based
  generator captures temporal characteristics, and the ANN-based discriminator maintains
  classification accuracy. Federated training prevents centralization of raw client
  data, while privacy is preserved through controlled perturbation of spike-train
  and membrane-potential representations, supported by RDP-based privacy accounting.
  We evaluated our architecture against methods such as RDP-TimeGAN, RDP-CRNN-GAN,
  RDP-RCGAN, and RDP-Clare-GAN, demonstrating that our approach preserves temporal
  features and downstream utility while maintaining privacy in synthetic EEG generation.
  This solution enables privacy-preserving generation of distributed synthetic EEG
  data for BCI/BMI research and development.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221766815
url: https://doi.org/10.3389/fnhum.2026.1909432
discovered_at: '2026-10-16'
tags: *id001
---

# Federated Spiking GANs with Rényi Differential Privacy for privacy\-preserving synthetic EEG generation in brain–computer interfaces

**Autores:** Shouvik Paul; Garima Bajwa

**Data:** 2026-10-14 · **Tipo:** article

## Resumo

Electroencephalography \(EEG\) data used in brain\-computer and brain\-machine interfaces \(BCI/BMI\) contain sensitive, user\-specific information, creating privacy risks in consumer applications such as gaming, human augmentation, and virtual reality\. Existing methods like encryption and anonymization either fail to protect data during analysis or still expose identifiable attributes\. While differential privacy \(DP\) offers formal protection, it often reduces data utility\. The key challenge is to generate synthetic EEG data that protects sensitive attributes while retaining temporal features for downstream use\. To address this, we developed a federated spiking generative framework that integrates a spiking neural network \(SNN\)\-based generator, temporally correlated noise, an artificial neural network \(ANN\)\-based discriminator, and Rényi differential privacy \(RDP\) within a federated learning framework\. The SNN\-based generator captures temporal characteristics, and the ANN\-based discriminator maintains classification accuracy\. Federated training prevents centralization of raw client data, while privacy is preserved through controlled perturbation of spike\-train and membrane\-potential representations, supported by RDP\-based privacy accounting\. We evaluated our architecture against methods such as RDP\-TimeGAN, RDP\-CRNN\-GAN, RDP\-RCGAN, and RDP\-Clare\-GAN, demonstrating that our approach preserves temporal features and downstream utility while maintaining privacy in synthetic EEG generation\. This solution enables privacy\-preserving generation of distributed synthetic EEG data for BCI/BMI research and development\.

[Consultar publicação](<https://doi.org/10.3389/fnhum.2026.1909432>)
