---
title: Robust Logical Anomaly Detection under Capture Shifts via Synthetic Anomalies
authors:
- Ufuk Efe
- Alptekin Temizel
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Detectors of logical anomalies, such as missing, extra or wrongly combined
  parts, usually score a test image by its distance from normal (good) images. They
  achieve near-perfect image-level AUROC on standard industrial anomaly detection
  benchmarks such as MVTec LOCO, but their robustness to changes in capture conditions
  remains largely unexamined. Under a heterogeneous perturbation protocol in which
  each test image is randomly kept unaltered or subjected to a brightness reduction
  or a zoom-out transformation, the normal-reference methods we tested lose 9.7 to
  34.1 AUROC points, and two of the strongest, CSAD and SALAD, fall from 97.7% and
  96.4% to 68.1% and 62.3%. We propose a framework in which a classifier, trained
  on normal images and on synthetic anomalies, scores a test image without comparing
  it with normal data. From a short description of each product, a language model
  derives anomaly types and editing instructions, an image editor applies them to
  normal images, and the classifier learns to separate the edited images from automatically
  discovered normal sub-modes. With its full training recipe, the framework reaches
  94.9% AUROC on clean images, 1.5 to 2.8 points below SALAD and CSAD, and 94.1% under
  the perturbation protocol. Trained without brightness or zoom-out augmentation,
  so that neither test perturbation occurs in training, it still reaches 92.5% (93.2%
  clean). These results suggest that clean benchmark scores can hide a strong sensitivity
  to capture conditions, and that learning the decision from both normal images and
  rule violations may reduce it.
source:
- arXiv
source_ids:
- arxiv:2610.18295
url: https://arxiv.org/abs/2610.18295
discovered_at: '2026-10-16'
tags: *id001
---

# Robust Logical Anomaly Detection under Capture Shifts via Synthetic Anomalies

**Autores:** Ufuk Efe; Alptekin Temizel

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Detectors of logical anomalies, such as missing, extra or wrongly combined parts, usually score a test image by its distance from normal \(good\) images\. They achieve near\-perfect image\-level AUROC on standard industrial anomaly detection benchmarks such as MVTec LOCO, but their robustness to changes in capture conditions remains largely unexamined\. Under a heterogeneous perturbation protocol in which each test image is randomly kept unaltered or subjected to a brightness reduction or a zoom\-out transformation, the normal\-reference methods we tested lose 9\.7 to 34\.1 AUROC points, and two of the strongest, CSAD and SALAD, fall from 97\.7% and 96\.4% to 68\.1% and 62\.3%\. We propose a framework in which a classifier, trained on normal images and on synthetic anomalies, scores a test image without comparing it with normal data\. From a short description of each product, a language model derives anomaly types and editing instructions, an image editor applies them to normal images, and the classifier learns to separate the edited images from automatically discovered normal sub\-modes\. With its full training recipe, the framework reaches 94\.9% AUROC on clean images, 1\.5 to 2\.8 points below SALAD and CSAD, and 94\.1% under the perturbation protocol\. Trained without brightness or zoom\-out augmentation, so that neither test perturbation occurs in training, it still reaches 92\.5% \(93\.2% clean\)\. These results suggest that clean benchmark scores can hide a strong sensitivity to capture conditions, and that learning the decision from both normal images and rule violations may reduce it\.

[Consultar publicação](<https://arxiv.org/abs/2610.18295>)
