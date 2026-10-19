---
title: A model for children’s drawing content analysis and creativity assessment Integrating
  DETR target detection and CLIP semantic understanding
authors:
- Yuan Yuan
date: '2026-10-15'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1007/s44163-026-02466-8
abstract: To address the issue of imbalance between semantic depth and spatial understanding
  in children’s drawing content analysis, an innovative framework integrating DEtection
  TRansformer (DETR) and contrastive language-image pretraining (CLIP) is proposed.
  In the concrete implementation, the set prediction of DETR is regarded as the spatial
  backbone; the CLIP text prompt is inserted in each layer of the decoder; the frame
  position and semantic embedding are updated simultaneously by cross-modal attention;
  the learnable positional encoding and contrastive loss are supplemented, and the
  zero-shot metaphor analysis is realized. In the experiment, a ChildArt-Open subset
  (5000 children’s drawings) is constructed based on the Google Open Images Dataset
  ( https://storage.googleapis.com/openimages/web/index.html ), and it is trained
  in a 32×NVIDIA A100 graphics processing unit environment. DETR-CLIP reaches 78.6%±0.4
  on mAP@0.5, significantly outperforming DETR’s 62.3%±0.6, Deformable DETR’s 71.5%±0.5,
  Faster R-CNN+CLIP’s 73.8%±0.6, RT-DETR’s 74.2%±0.5, DINO-DETR’s 75.1%±0.4, and YOLOv8’s
  72.6%±0.6. Ablation experiments show that creativity scoring accuracy drops by 15.1%
  after removing the cross-modal interaction module. Semantic understanding accuracy
  decreases by 9.1% after removing CLIP semantic guidance. The model’s inference speed
  is 45 frames per second FPS, the number of parameters is 196.9 M, and Floating-point
  Operations (FLOPs) are 156.2 G. The model captures long-distance dependence through
  the Transformer’s global attention mechanism and breaks through the closed category
  restrictions by combining CLIP’s open semantic space to symbolic expression in children’s
  drawings. The results provide an extensible new path of aesthetic evaluation for
  low-resource scenes.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222146266
url: https://doi.org/10.1007/s44163-026-02466-8
discovered_at: '2026-10-19'
tags: *id001
---

# A model for children’s drawing content analysis and creativity assessment Integrating DETR target detection and CLIP semantic understanding

**Autores:** Yuan Yuan

**Data:** 2026-10-15 · **Tipo:** article

## Resumo

To address the issue of imbalance between semantic depth and spatial understanding in children’s drawing content analysis, an innovative framework integrating DEtection TRansformer \(DETR\) and contrastive language\-image pretraining \(CLIP\) is proposed\. In the concrete implementation, the set prediction of DETR is regarded as the spatial backbone; the CLIP text prompt is inserted in each layer of the decoder; the frame position and semantic embedding are updated simultaneously by cross\-modal attention; the learnable positional encoding and contrastive loss are supplemented, and the zero\-shot metaphor analysis is realized\. In the experiment, a ChildArt\-Open subset \(5000 children’s drawings\) is constructed based on the Google Open Images Dataset \( https://storage\.googleapis\.com/openimages/web/index\.html \), and it is trained in a 32×NVIDIA A100 graphics processing unit environment\. DETR\-CLIP reaches 78\.6%±0\.4 on mAP@0\.5, significantly outperforming DETR’s 62\.3%±0\.6, Deformable DETR’s 71\.5%±0\.5, Faster R\-CNN\+CLIP’s 73\.8%±0\.6, RT\-DETR’s 74\.2%±0\.5, DINO\-DETR’s 75\.1%±0\.4, and YOLOv8’s 72\.6%±0\.6\. Ablation experiments show that creativity scoring accuracy drops by 15\.1% after removing the cross\-modal interaction module\. Semantic understanding accuracy decreases by 9\.1% after removing CLIP semantic guidance\. The model’s inference speed is 45 frames per second FPS, the number of parameters is 196\.9 M, and Floating\-point Operations \(FLOPs\) are 156\.2 G\. The model captures long\-distance dependence through the Transformer’s global attention mechanism and breaks through the closed category restrictions by combining CLIP’s open semantic space to symbolic expression in children’s drawings\. The results provide an extensible new path of aesthetic evaluation for low\-resource scenes\.

[Consultar publicação](<https://doi.org/10.1007/s44163-026-02466-8>)
