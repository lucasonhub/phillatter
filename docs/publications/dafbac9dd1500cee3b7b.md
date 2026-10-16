---
title: Semi-Automated Image Labeling and Object Tracking for MR-Guided Radiotherapy
  Using a Foundation Vision Model
authors:
- Mike Zhu
- Jun Hsuang Jen
- Daniel Ellis Hyer
- Taylor P. Trentadue
- Timothy L. Kline
- Bryan J. Traughber
- Douglas J. Moseley
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1007/s10278-026-02387-z
abstract: 'Magnetic resonance-guided radiotherapy (MRgRT) enables real-time tracking
  of tumor and organ motion for more precise radiation delivery. However, existing
  clinical tracking software struggles with high-velocity or non-rigid motion. Foundation
  models, such as Segment Anything Model 2 (SAM2) and MedSAM2, offer robust tracking
  with fast inference speeds and strong zero-shot accuracy that can improve with fine-tuning.
  Fine-tuning typically uses expert-labeled datasets, which are expensive to acquire.
  We explored SAM2''s utility in accelerating the labeling process by developing a
  workflow where novices label < 1% of frames and SAM2 automatically labels the rest.
  We then evaluated SAM2 and MedSAM2 for tumor tracking on an open-access MRgRT dataset
  in three configurations: zero-shot, fine-tuned using manually labeled data, and
  fine-tuned using the semi-automatically labeled data. We measured accuracy with
  the Dice similarity coefficient, 95th percentile (P95) Hausdorff distance, and centroid
  distance. MedSAM2 and SAM2 demonstrated strong zero-shot tracking accuracy with
  no significant difference among the model variants. Fine-tuning significantly improved
  Dice coefficients (0.874 to 0.891, p = 0.006), P95 Hausdorff distances (9.069 to
  4.378 mm, p < 0.001), and centroid distances (5.299 to 1.769 mm, p < 0.001) relative
  to zero-shot, with no significant difference between using manually labeled and
  semi-automatically labeled data. Therefore, leveraging SAM2 to semi-automatically
  generate labeled training data can substantially reduce the cost of data curation
  and long-term model maintenance without compromising accuracy.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221669898
url: https://doi.org/10.1007/s10278-026-02387-z
discovered_at: '2026-10-16'
tags: *id001
---

# Semi\-Automated Image Labeling and Object Tracking for MR\-Guided Radiotherapy Using a Foundation Vision Model

**Autores:** Mike Zhu; Jun Hsuang Jen; Daniel Ellis Hyer; Taylor P\. Trentadue; Timothy L\. Kline; Bryan J\. Traughber; Douglas J\. Moseley

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Magnetic resonance\-guided radiotherapy \(MRgRT\) enables real\-time tracking of tumor and organ motion for more precise radiation delivery\. However, existing clinical tracking software struggles with high\-velocity or non\-rigid motion\. Foundation models, such as Segment Anything Model 2 \(SAM2\) and MedSAM2, offer robust tracking with fast inference speeds and strong zero\-shot accuracy that can improve with fine\-tuning\. Fine\-tuning typically uses expert\-labeled datasets, which are expensive to acquire\. We explored SAM2&\#x27;s utility in accelerating the labeling process by developing a workflow where novices label &lt; 1% of frames and SAM2 automatically labels the rest\. We then evaluated SAM2 and MedSAM2 for tumor tracking on an open\-access MRgRT dataset in three configurations: zero\-shot, fine\-tuned using manually labeled data, and fine\-tuned using the semi\-automatically labeled data\. We measured accuracy with the Dice similarity coefficient, 95th percentile \(P95\) Hausdorff distance, and centroid distance\. MedSAM2 and SAM2 demonstrated strong zero\-shot tracking accuracy with no significant difference among the model variants\. Fine\-tuning significantly improved Dice coefficients \(0\.874 to 0\.891, p = 0\.006\), P95 Hausdorff distances \(9\.069 to 4\.378 mm, p &lt; 0\.001\), and centroid distances \(5\.299 to 1\.769 mm, p &lt; 0\.001\) relative to zero\-shot, with no significant difference between using manually labeled and semi\-automatically labeled data\. Therefore, leveraging SAM2 to semi\-automatically generate labeled training data can substantially reduce the cost of data curation and long\-term model maintenance without compromising accuracy\.

[Consultar publicação](<https://doi.org/10.1007/s10278-026-02387-z>)
