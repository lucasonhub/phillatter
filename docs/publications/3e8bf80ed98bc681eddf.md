---
title: Topology-preserving coronary vessel segmentation in X-ray angiography using
  ResNet50-MASAG-UNet
authors:
- G. Sunilkumar
- P. Kumaresan
date: '2026-10-14'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3389/fradi.2026.1949450
abstract: 'Coronary artery disease occurs when the accumulation of fatty atheroma
  deposits narrows the coronary blood vessels, thereby reducing blood flow to the
  myocardium. To identify these narrowings, cardiologists use X-ray coronary angiography
  (XCA). However, these angiographic images are often blurry and noisy, making vessels
  difficult to view clearly. To enhance visibility, we proposed an image improvement
  technique that combines three filtering approaches: Bilateral filtering, unsharp
  masking, and Contrast Limited Adaptive Histogram Equalization (CLAHE), to remove
  noise, sharpen vessel edges, and improve brightness balance, producing clearer vessel
  images to support subsequent analysis. Our proposed ResNet50-MASAG-UNet integrates
  a Multi-Scale Adaptive Spatial Attention Gate (MASAG) at each skip connection of
  a ResNet50-UNet, enabling the decoder to attend selectively to coronary vessel regions
  while suppressing non-vascular activations from catheters and bones. A topology-aware
  loss is used to preserve vessel connectivity by maintaining centreline continuity.
  Together, these elements enable more accurate and complete coronary vessel segmentation.
  The proposed model achieves improved segmentation performance on XCA images, attaining
  a Dice coefficient of 88.3%, a Jaccard Index of 79.1%, a precision of 86.4%, and
  a recall of 90.5%. It outperforms the standard UNet baseline and provides clearer
  vessel segmentation, demonstrating improved potential for coronary vessel analysis.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221755143
url: https://doi.org/10.3389/fradi.2026.1949450
discovered_at: '2026-10-16'
tags: *id001
---

# Topology\-preserving coronary vessel segmentation in X\-ray angiography using ResNet50\-MASAG\-UNet

**Autores:** G\. Sunilkumar; P\. Kumaresan

**Data:** 2026-10-14 · **Tipo:** article

## Resumo

Coronary artery disease occurs when the accumulation of fatty atheroma deposits narrows the coronary blood vessels, thereby reducing blood flow to the myocardium\. To identify these narrowings, cardiologists use X\-ray coronary angiography \(XCA\)\. However, these angiographic images are often blurry and noisy, making vessels difficult to view clearly\. To enhance visibility, we proposed an image improvement technique that combines three filtering approaches: Bilateral filtering, unsharp masking, and Contrast Limited Adaptive Histogram Equalization \(CLAHE\), to remove noise, sharpen vessel edges, and improve brightness balance, producing clearer vessel images to support subsequent analysis\. Our proposed ResNet50\-MASAG\-UNet integrates a Multi\-Scale Adaptive Spatial Attention Gate \(MASAG\) at each skip connection of a ResNet50\-UNet, enabling the decoder to attend selectively to coronary vessel regions while suppressing non\-vascular activations from catheters and bones\. A topology\-aware loss is used to preserve vessel connectivity by maintaining centreline continuity\. Together, these elements enable more accurate and complete coronary vessel segmentation\. The proposed model achieves improved segmentation performance on XCA images, attaining a Dice coefficient of 88\.3%, a Jaccard Index of 79\.1%, a precision of 86\.4%, and a recall of 90\.5%\. It outperforms the standard UNet baseline and provides clearer vessel segmentation, demonstrating improved potential for coronary vessel analysis\.

[Consultar publicação](<https://doi.org/10.3389/fradi.2026.1949450>)
