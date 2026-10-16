---
title: 'VDFedDiff: a novel versatile defense scheme against adversarial attacks in
  federated diffusion models'
authors:
- Wennan Wang
- Tuli Chen
- Fu Luo
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1186/s44147-026-01266-2
abstract: 'Abstract Federated learning (FL) enables multiple clients to collaboratively
  train machine learning models without sharing their raw data, making it a promising
  paradigm for privacy-sensitive generative applications. However, diffusion models
  trained in federated environments remain vulnerable to backdoor, evasion, and model-poisoning
  attacks, which can degrade generative quality or induce attacker-specified behaviors.
  Existing Byzantine-robust aggregation methods primarily mitigate anomalous client
  updates but do not address coordinate-localized poisoning or adversarial perturbations
  in the diffusion latent space. Meanwhile, existing defenses for diffusion models
  are generally designed for centralized settings and therefore cannot directly handle
  malicious client updates in federated training. To address these limitations, we
  propose VDFedDiff, a multi-level defense framework for federated diffusion models.
  VDFedDiff integrates three complementary components: Adaptive Trust Scoring (ATS),
  which dynamically reduces the influence of anomalous client updates; Adversarial
  Gradient Filtering (AGF), which suppresses coordinate-wise malicious deviations
  through median- and median-absolute-deviation-based filtering; and Latent-Space
  Purification (LSP), which introduces time-aware stochastic regularization to weaken
  adversarial alignment during local diffusion training. Experiments on CIFAR-10,
  CelebA, and LSUN-Bedroom under backdoor, evasion, and model-poisoning attacks demonstrate
  that VDFedDiff consistently improves attack resilience while preserving generative
  quality. On non-IID CIFAR-10 under combined backdoor and model-poisoning attacks,
  VDFedDiff reduces the FID from 46.8 to 28.3 and the attack success rate from 72.5%
  to 23.8% compared with undefended FedAvg. It also introduces only 6.1% additional
  per-round computation time and no additional communication overhead in the evaluated
  setting. These results demonstrate the effectiveness of combining client-level,
  coordinate-level, and latent-level protection for securing federated diffusion training.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221195718
url: https://doi.org/10.1186/s44147-026-01266-2
discovered_at: '2026-10-16'
tags: *id001
---

# VDFedDiff: a novel versatile defense scheme against adversarial attacks in federated diffusion models

**Autores:** Wennan Wang; Tuli Chen; Fu Luo

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

Abstract Federated learning \(FL\) enables multiple clients to collaboratively train machine learning models without sharing their raw data, making it a promising paradigm for privacy\-sensitive generative applications\. However, diffusion models trained in federated environments remain vulnerable to backdoor, evasion, and model\-poisoning attacks, which can degrade generative quality or induce attacker\-specified behaviors\. Existing Byzantine\-robust aggregation methods primarily mitigate anomalous client updates but do not address coordinate\-localized poisoning or adversarial perturbations in the diffusion latent space\. Meanwhile, existing defenses for diffusion models are generally designed for centralized settings and therefore cannot directly handle malicious client updates in federated training\. To address these limitations, we propose VDFedDiff, a multi\-level defense framework for federated diffusion models\. VDFedDiff integrates three complementary components: Adaptive Trust Scoring \(ATS\), which dynamically reduces the influence of anomalous client updates; Adversarial Gradient Filtering \(AGF\), which suppresses coordinate\-wise malicious deviations through median\- and median\-absolute\-deviation\-based filtering; and Latent\-Space Purification \(LSP\), which introduces time\-aware stochastic regularization to weaken adversarial alignment during local diffusion training\. Experiments on CIFAR\-10, CelebA, and LSUN\-Bedroom under backdoor, evasion, and model\-poisoning attacks demonstrate that VDFedDiff consistently improves attack resilience while preserving generative quality\. On non\-IID CIFAR\-10 under combined backdoor and model\-poisoning attacks, VDFedDiff reduces the FID from 46\.8 to 28\.3 and the attack success rate from 72\.5% to 23\.8% compared with undefended FedAvg\. It also introduces only 6\.1% additional per\-round computation time and no additional communication overhead in the evaluated setting\. These results demonstrate the effectiveness of combining client\-level, coordinate\-level, and latent\-level protection for securing federated diffusion training\.

[Consultar publicação](<https://doi.org/10.1186/s44147-026-01266-2>)
