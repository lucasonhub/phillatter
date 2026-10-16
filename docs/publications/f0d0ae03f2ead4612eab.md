---
title: Effect of data leakage on deep learning accuracy for kidney stone classification
  on CT
authors:
- Okoi Michael Obeten
- Abas Aliu
- Omowumi Hafsat Aliu
- Ahmed Jimoh
- Zibril Aliyu
- Christiana Uchenna Ezeanya
date: '2026-10-12'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1007/s44584-026-00003-y
abstract: Deep learning models for kidney stone classification on CT frequently report
  accuracies above 98%, but many are trained on augmented datasets split at the image
  level, allowing near-duplicate copies of the same slice to appear in both training
  and test sets. To quantify how much this leakage inflates reported performance,
  we reassessed a deep learning slice-level classifier under a leakage-free, patient-wise
  protocol with calibration, uncertainty quantification and cross-center validation,
  using a multi-center CT dataset of 3,364 original and 35,457 augmented images from
  201 patients across three centers. This study proposes no new architecture; its
  contribution is the quantification and benchmarking of an evaluation effect. Patients
  were partitioned so that all their images, including augmentations, stayed within
  a single split, and validation and test sets contained only original images. A hybrid
  CNN-Transformer classifier was trained alongside matched comparator models on one
  identical training budget, then retrained under a random image-level split to isolate
  the effect of leakage, with additional analyses including cross-validation, ten-seed
  repetition, leave-one-hospital-out testing, temperature scaling, conformal prediction,
  examination-level aggregation and saliency mapping. Under the patient-wise protocol
  the classifier achieved an AUC of 0.971, accuracy of 0.962, sensitivity of 0.953,
  specificity of 0.981 and a Matthews correlation coefficient of 0.914, with patient-level
  cluster bootstrap intervals; the leaky image-level split raised accuracy to 0.990
  and AUC to 0.999. Across ten seeds the mean inflation was 5.0 accuracy points (95%
  CI 2.7 to 7.3; paired t test P = 0.0009) and 2.7 AUC points (95% CI 1.4 to 3.9;
  P = 0.001), present in every seed. A plain ResNet-18 reached a numerically higher
  AUC than the hybrid model with no significant difference detected, and equivalence
  was not established; a convolution-free Transformer performed near chance (AUC 0.569).
  Performance fell on held-out centers. Calibration and selective classification improved
  reliability, and no sex disparity in sensitivity was found once results were pooled
  across patients at the patient level. Because the analysis uses eight-bit rendered
  images without Hounsfield unit information, it is a methodological proof of concept
  rather than an evaluation of a deployable system. These findings show that image-level
  splitting substantially overstates real-world performance, and that patient-wise,
  calibrated evaluation offers a more trustworthy basis for appraisal.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221570458
url: https://doi.org/10.1007/s44584-026-00003-y
discovered_at: '2026-10-16'
tags: *id001
---

# Effect of data leakage on deep learning accuracy for kidney stone classification on CT

**Autores:** Okoi Michael Obeten; Abas Aliu; Omowumi Hafsat Aliu; Ahmed Jimoh; Zibril Aliyu; Christiana Uchenna Ezeanya

**Data:** 2026-10-12 · **Tipo:** article

## Resumo

Deep learning models for kidney stone classification on CT frequently report accuracies above 98%, but many are trained on augmented datasets split at the image level, allowing near\-duplicate copies of the same slice to appear in both training and test sets\. To quantify how much this leakage inflates reported performance, we reassessed a deep learning slice\-level classifier under a leakage\-free, patient\-wise protocol with calibration, uncertainty quantification and cross\-center validation, using a multi\-center CT dataset of 3,364 original and 35,457 augmented images from 201 patients across three centers\. This study proposes no new architecture; its contribution is the quantification and benchmarking of an evaluation effect\. Patients were partitioned so that all their images, including augmentations, stayed within a single split, and validation and test sets contained only original images\. A hybrid CNN\-Transformer classifier was trained alongside matched comparator models on one identical training budget, then retrained under a random image\-level split to isolate the effect of leakage, with additional analyses including cross\-validation, ten\-seed repetition, leave\-one\-hospital\-out testing, temperature scaling, conformal prediction, examination\-level aggregation and saliency mapping\. Under the patient\-wise protocol the classifier achieved an AUC of 0\.971, accuracy of 0\.962, sensitivity of 0\.953, specificity of 0\.981 and a Matthews correlation coefficient of 0\.914, with patient\-level cluster bootstrap intervals; the leaky image\-level split raised accuracy to 0\.990 and AUC to 0\.999\. Across ten seeds the mean inflation was 5\.0 accuracy points \(95% CI 2\.7 to 7\.3; paired t test P = 0\.0009\) and 2\.7 AUC points \(95% CI 1\.4 to 3\.9; P = 0\.001\), present in every seed\. A plain ResNet\-18 reached a numerically higher AUC than the hybrid model with no significant difference detected, and equivalence was not established; a convolution\-free Transformer performed near chance \(AUC 0\.569\)\. Performance fell on held\-out centers\. Calibration and selective classification improved reliability, and no sex disparity in sensitivity was found once results were pooled across patients at the patient level\. Because the analysis uses eight\-bit rendered images without Hounsfield unit information, it is a methodological proof of concept rather than an evaluation of a deployable system\. These findings show that image\-level splitting substantially overstates real\-world performance, and that patient\-wise, calibrated evaluation offers a more trustworthy basis for appraisal\.

[Consultar publicação](<https://doi.org/10.1007/s44584-026-00003-y>)
