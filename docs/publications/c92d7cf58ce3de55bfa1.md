---
title: 'SkinSense: Dermatological Screening and Skin-Care Advisory System'
authors:
- Srivarshini S
- V. S. Anita Sofia
- Nithyanandh Selvam
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
- Neurociência
doi: 10.32628/cseit2612557
abstract: Access to dermatological assessment in many regions is limited less by the
  availability of imaging than by the availability of trained specialists, and the
  resulting delay affects precisely those lesions for which early attention matters
  most. Most reported systems terminate at a single classification score, give no
  indication of how ambiguous that score is, and provide the end user with no actionable
  guidance. This paper describes SkinSense, a web-deployed educational screening and
  preventive advisory system joining seven-class lesion classification with EfficientNetV2,
  lesion delineation with U-Net, entropy-based uncertainty quantification, Grad-CAM
  visual attribution, heuristic risk banding, disease-specific preventive guidance
  and a locally hosted retrieval-based educational assistant inside one authenticated
  request pipeline built on FastAPI, SQLAlchemy, SQLite and a React front end. Classification
  is trained and evaluated on 10,013 de-duplicated ISIC 2018 Task 3 images under a
  fixed 7,009 / 1,502 / 1,502 partition whose test portion is withheld from every
  design and tuning decision. On that partition the baseline network records 52.86%
  accuracy, 46.49% balanced accuracy, 32.30% macro F1, 58.65% weighted F1 and 84.57%
  ROC-AUC; a compute-constrained improved configuration reaches 61.65% accuracy, 52.06%
  balanced accuracy and 39.81% macro F1. The limited-training U-Net attains a Dice
  coefficient of 67.68%, an IoU of 53.29% and pixel accuracy of 86.85%. A variational-autoencoder
  augmentation trial using thirty generated minority-class images reduced macro F1
  to 16.68% and is reported as a negative result rather than suppressed. The contribution
  claimed is the integration itself — an uncertainty-gated advisory workflow with
  transparent reporting — not a new accuracy record. The system is explicitly educational
  and does not perform clinical diagnosis.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221646483
url: https://doi.org/10.32628/cseit2612557
discovered_at: '2026-10-16'
tags: *id001
---

# SkinSense: Dermatological Screening and Skin\-Care Advisory System

**Autores:** Srivarshini S; V\. S\. Anita Sofia; Nithyanandh Selvam

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Access to dermatological assessment in many regions is limited less by the availability of imaging than by the availability of trained specialists, and the resulting delay affects precisely those lesions for which early attention matters most\. Most reported systems terminate at a single classification score, give no indication of how ambiguous that score is, and provide the end user with no actionable guidance\. This paper describes SkinSense, a web\-deployed educational screening and preventive advisory system joining seven\-class lesion classification with EfficientNetV2, lesion delineation with U\-Net, entropy\-based uncertainty quantification, Grad\-CAM visual attribution, heuristic risk banding, disease\-specific preventive guidance and a locally hosted retrieval\-based educational assistant inside one authenticated request pipeline built on FastAPI, SQLAlchemy, SQLite and a React front end\. Classification is trained and evaluated on 10,013 de\-duplicated ISIC 2018 Task 3 images under a fixed 7,009 / 1,502 / 1,502 partition whose test portion is withheld from every design and tuning decision\. On that partition the baseline network records 52\.86% accuracy, 46\.49% balanced accuracy, 32\.30% macro F1, 58\.65% weighted F1 and 84\.57% ROC\-AUC; a compute\-constrained improved configuration reaches 61\.65% accuracy, 52\.06% balanced accuracy and 39\.81% macro F1\. The limited\-training U\-Net attains a Dice coefficient of 67\.68%, an IoU of 53\.29% and pixel accuracy of 86\.85%\. A variational\-autoencoder augmentation trial using thirty generated minority\-class images reduced macro F1 to 16\.68% and is reported as a negative result rather than suppressed\. The contribution claimed is the integration itself — an uncertainty\-gated advisory workflow with transparent reporting — not a new accuracy record\. The system is explicitly educational and does not perform clinical diagnosis\.

[Consultar publicação](<https://doi.org/10.32628/cseit2612557>)
