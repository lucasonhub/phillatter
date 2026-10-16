---
title: An Enhancing Lung Disease Detection with Scalable UNet-Mamba Segmentation
authors:
- Sivasakthi S
- Radha V
date: '2026-10-12'
type: article
category: &id001
- Inteligência Artificial
doi: 10.14445/22315381/ijett-v74i9p140
abstract: Lung diseases are conditions that damage the lung tissues, airways or blood
  vessels of the lungs, causing breathing difficulties and decreased oxygen supply
  to the body. Computed Tomography (CT) plays a crucial role in lung disease prediction
  because it provides detailed cross-sectional images for detecting tumors at initial
  stages. However, CT scans have drawbacks such as radiation exposure, high cost,
  large data size, and the possibility of false positives. Recently, many Deep Learning
  (DL) techniques have been used to automatically analyze CT images for early and
  accurate detection of lung diseases, improving diagnostic efficiency. However, existing
  models may struggle to capture fine spatial details, leading to inaccurate boundary
  delineation and poor segmentation of small or low-contrast regions. Some models
  are also sensitive to imaging artifacts, which can reduce performance in real-world
  conditions. In this paper, a lung disease prediction model is developed using ResNet
  and Mamba Network (LRMNet) to solve the aforementioned issues for lung disease prediction.
  The first step is improving the model's ability to conduct pre-processing and enrich
  the data using a Deep Convolutional Generative Adversarial Network (DCGAN). Then,
  the Scalable Vision UNet-Mamba (SVU-M) model is developed to efficiently capture
  fine spatial details along with long-range contextual information. SVU-M leverages
  Scalable Vision State Space (SVSS) blocks to efficiently model the global dependencies
  while maintaining linear computational complexity. The integration of SVSS within
  a U-shaped framework enhances the boundary delineation and improves segmentation
  of small or low-contrast regions, which increases the efficiency against imaging
  artifacts for more reliable performance. The decoder feature maps of SVU-M are further
  processed using Global Average Pooling (GAP) to determine image-level feature representations
  for classification. Simultaneously, the input image is directly fed into ResNet-50
  for capturing the whole image's semantic features. A Multi-Layer Perceptron (MLP)
  classifier is trained with the extracted features to forecast lung diseases. A total
  accuracy of 94.15% on the customized dataset and 93.29% on the SARS-CoV-2 CT dataset
  was achieved by the suggested model, according to the experimental results, exceeding
  the performance of other models.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221520665
url: https://doi.org/10.14445/22315381/ijett-v74i9p140
discovered_at: '2026-10-16'
tags: *id001
---

# An Enhancing Lung Disease Detection with Scalable UNet\-Mamba Segmentation

**Autores:** Sivasakthi S; Radha V

**Data:** 2026-10-12 · **Tipo:** article

## Resumo

Lung diseases are conditions that damage the lung tissues, airways or blood vessels of the lungs, causing breathing difficulties and decreased oxygen supply to the body\. Computed Tomography \(CT\) plays a crucial role in lung disease prediction because it provides detailed cross\-sectional images for detecting tumors at initial stages\. However, CT scans have drawbacks such as radiation exposure, high cost, large data size, and the possibility of false positives\. Recently, many Deep Learning \(DL\) techniques have been used to automatically analyze CT images for early and accurate detection of lung diseases, improving diagnostic efficiency\. However, existing models may struggle to capture fine spatial details, leading to inaccurate boundary delineation and poor segmentation of small or low\-contrast regions\. Some models are also sensitive to imaging artifacts, which can reduce performance in real\-world conditions\. In this paper, a lung disease prediction model is developed using ResNet and Mamba Network \(LRMNet\) to solve the aforementioned issues for lung disease prediction\. The first step is improving the model&\#x27;s ability to conduct pre\-processing and enrich the data using a Deep Convolutional Generative Adversarial Network \(DCGAN\)\. Then, the Scalable Vision UNet\-Mamba \(SVU\-M\) model is developed to efficiently capture fine spatial details along with long\-range contextual information\. SVU\-M leverages Scalable Vision State Space \(SVSS\) blocks to efficiently model the global dependencies while maintaining linear computational complexity\. The integration of SVSS within a U\-shaped framework enhances the boundary delineation and improves segmentation of small or low\-contrast regions, which increases the efficiency against imaging artifacts for more reliable performance\. The decoder feature maps of SVU\-M are further processed using Global Average Pooling \(GAP\) to determine image\-level feature representations for classification\. Simultaneously, the input image is directly fed into ResNet\-50 for capturing the whole image&\#x27;s semantic features\. A Multi\-Layer Perceptron \(MLP\) classifier is trained with the extracted features to forecast lung diseases\. A total accuracy of 94\.15% on the customized dataset and 93\.29% on the SARS\-CoV\-2 CT dataset was achieved by the suggested model, according to the experimental results, exceeding the performance of other models\.

[Consultar publicação](<https://doi.org/10.14445/22315381/ijett-v74i9p140>)
