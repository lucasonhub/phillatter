---
title: 'DiRetina: Anatomically Guided Hybrid Deep Learning for Glaucoma Detection
  from Retinal Fundus Images'
authors:
- Mohammad Loqman Hakeem
- Muhammad Irsyad Abdullah
- Ahgalya Subbiah
date: '2026-10-11'
type: article
category: &id001
- Inteligência Artificial
doi: null
abstract: Glaucoma is a major cause of irreversible visual impairment, and early screening
  remains difficult because disease progression may be asymptomatic while manual fundus
  assessment depends on specialist availability and observer judgement. This study
  develops DiRetina, a multi-stage artificial intelligence framework for automated
  glaucoma screening from color retinal fundus photographs, with the objective of
  improving robustness under heterogeneous acquisition conditions while retaining
  interpretable anatomical markers. A curated analytical dataset of 3,608 unique images
  was formed from seven public retinal repositories and stratified into training,
  validation, and test subsets using a 70:15:15:15 allocation. The pipeline applies
  contrast normalization, vessel-guided optic nerve head localization using U-Net++,
  Chan-Vese active-contour delineation of the optic disc and cup, vertical cup-to-disc
  ratio extraction, and hybrid feature fusion combining Local Binary Patterns with
  pretrained convolutional representations. A knowledge-enhanced attention module
  incorporates frozen retinal foundation-model embeddings to reduce task-irrelevant
  background influence. Baseline ResNet-50, VGG-16, and Xception models achieved 86.70%-88.46%
  accuracy, with specificity between 78.62% and 82.63%. The optimized Xception configuration
  reached 95.07% accuracy and an area under the receiver operating characteristic
  curve of 0.9880, while the hybrid feature-Support Vector Machine configuration achieved
  96.4% accuracy, 95.1% sensitivity, 97.2% specificity, and an area under the curve
  of 0.981. Reported one-way analysis of variance results indicated significant performance
  differences among model variants at p < 0.05. The findings support a structured
  screening strategy that combines anatomical localization, handcrafted texture descriptors,
  and deep representations to improve diagnostic consistency across heterogeneous
  fundus images. Prospective clinical validation remains necessary before deployment.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221738384
url: https://openalex.org/W7221738384
discovered_at: '2026-10-16'
tags: *id001
---

# DiRetina: Anatomically Guided Hybrid Deep Learning for Glaucoma Detection from Retinal Fundus Images

**Autores:** Mohammad Loqman Hakeem; Muhammad Irsyad Abdullah; Ahgalya Subbiah

**Data:** 2026-10-11 · **Tipo:** article

## Resumo

Glaucoma is a major cause of irreversible visual impairment, and early screening remains difficult because disease progression may be asymptomatic while manual fundus assessment depends on specialist availability and observer judgement\. This study develops DiRetina, a multi\-stage artificial intelligence framework for automated glaucoma screening from color retinal fundus photographs, with the objective of improving robustness under heterogeneous acquisition conditions while retaining interpretable anatomical markers\. A curated analytical dataset of 3,608 unique images was formed from seven public retinal repositories and stratified into training, validation, and test subsets using a 70:15:15:15 allocation\. The pipeline applies contrast normalization, vessel\-guided optic nerve head localization using U\-Net\+\+, Chan\-Vese active\-contour delineation of the optic disc and cup, vertical cup\-to\-disc ratio extraction, and hybrid feature fusion combining Local Binary Patterns with pretrained convolutional representations\. A knowledge\-enhanced attention module incorporates frozen retinal foundation\-model embeddings to reduce task\-irrelevant background influence\. Baseline ResNet\-50, VGG\-16, and Xception models achieved 86\.70%\-88\.46% accuracy, with specificity between 78\.62% and 82\.63%\. The optimized Xception configuration reached 95\.07% accuracy and an area under the receiver operating characteristic curve of 0\.9880, while the hybrid feature\-Support Vector Machine configuration achieved 96\.4% accuracy, 95\.1% sensitivity, 97\.2% specificity, and an area under the curve of 0\.981\. Reported one\-way analysis of variance results indicated significant performance differences among model variants at p &lt; 0\.05\. The findings support a structured screening strategy that combines anatomical localization, handcrafted texture descriptors, and deep representations to improve diagnostic consistency across heterogeneous fundus images\. Prospective clinical validation remains necessary before deployment\.

[Consultar publicação](<https://openalex.org/W7221738384>)
