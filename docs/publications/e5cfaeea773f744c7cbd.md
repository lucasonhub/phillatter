---
title: 'RadarGSOcc: Doppler-Aware 3D Semantic Occupancy Prediction Using 4D Radar
  Tensor with Geometric-Semantic Feature Extraction'
authors:
- Christofel Rio Goenawan
- Dong-Hee Paek
- Seung-Hyun Kong
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 3D semantic occupancy prediction is crucial for autonomous driving, but
  camera-based methods degrade in low-light conditions and LiDAR-based methods are
  sensitive to adverse weather. 4D radar is more robust, yet its sparsity and the
  high cost of radar tensor processing limit its use. We propose Radar Geometric-Semantic
  Occupancy Prediction (RadarGSOcc), an efficient framework that directly processes
  4D radar tensors by separately extracting geometric and semantic features, including
  Doppler information, with a deformable attention-based geometric refinement module
  as its key component. We also introduce the K-Radar 3DSemOcc benchmark, the first
  large-scale benchmark for 3D semantic occupancy prediction using 4D radar tensors,
  built on the K-Radar dataset with refined LiDAR-based annotations. RadarGSOcc predicts
  15 classes within a 51.2m range and achieves 38.2% IoU, 7.6% mIoU, and 25.5% weighted
  mIoU, outperforming RadarOcc by 17% relative (25.5 vs. 21.9) in weighted mIoU while
  using fewer parameters and lower computation. It substantially improves truck prediction
  while trading off car accuracy, outperforms camera-based approaches, and narrows
  the gap with LiDAR-based methods. To assess robustness without per-frame ground
  truth in adverse weather, we further propose a novel proxy metric, Environment-Based
  KL Divergence (EBKL), under which 4D radar proves a reliable and efficient modality
  for 3D semantic occupancy prediction. The dataset and code will be publicly available.
source:
- arXiv
source_ids:
- arxiv:2610.18686
url: https://arxiv.org/abs/2610.18686
discovered_at: '2026-10-16'
tags: *id001
---

# RadarGSOcc: Doppler\-Aware 3D Semantic Occupancy Prediction Using 4D Radar Tensor with Geometric\-Semantic Feature Extraction

**Autores:** Christofel Rio Goenawan; Dong\-Hee Paek; Seung\-Hyun Kong

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

3D semantic occupancy prediction is crucial for autonomous driving, but camera\-based methods degrade in low\-light conditions and LiDAR\-based methods are sensitive to adverse weather\. 4D radar is more robust, yet its sparsity and the high cost of radar tensor processing limit its use\. We propose Radar Geometric\-Semantic Occupancy Prediction \(RadarGSOcc\), an efficient framework that directly processes 4D radar tensors by separately extracting geometric and semantic features, including Doppler information, with a deformable attention\-based geometric refinement module as its key component\. We also introduce the K\-Radar 3DSemOcc benchmark, the first large\-scale benchmark for 3D semantic occupancy prediction using 4D radar tensors, built on the K\-Radar dataset with refined LiDAR\-based annotations\. RadarGSOcc predicts 15 classes within a 51\.2m range and achieves 38\.2% IoU, 7\.6% mIoU, and 25\.5% weighted mIoU, outperforming RadarOcc by 17% relative \(25\.5 vs\. 21\.9\) in weighted mIoU while using fewer parameters and lower computation\. It substantially improves truck prediction while trading off car accuracy, outperforms camera\-based approaches, and narrows the gap with LiDAR\-based methods\. To assess robustness without per\-frame ground truth in adverse weather, we further propose a novel proxy metric, Environment\-Based KL Divergence \(EBKL\), under which 4D radar proves a reliable and efficient modality for 3D semantic occupancy prediction\. The dataset and code will be publicly available\.

[Consultar publicação](<https://arxiv.org/abs/2610.18686>)
