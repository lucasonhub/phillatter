---
title: 'CADEN: An Enhanced Cross-dataset Anatomy-aware Distribution-alignment Ensemble
  Model for Alzheimer''s Disease Detection and Staging from MRI'
authors:
- Chetna Sharma
- Vivek Bhatnagar
date: '2026-10-16'
type: article
category: &id001
- Inteligência Artificial
- Neurociência
doi: 10.22266/ijies2026.1130.13
abstract: 'Deep models for Alzheimer''s disease (AD) classification degrade sharply
  when training and deployment data originate from different scanners and cohorts,
  so reported single-dataset accuracies rarely transfer to new sites.This paper presents
  CADEN, an anatomy-aware framework that learns a harmonized, atrophy-grounded featuremapping
  space and performs staging by an ensemble over that space rather than over raw images.CADEN
  combines four ideas: (i) label-free cross-site harmonization that couples ComBat-style
  feature adjustment with a lightweight learnable site adapter; (ii) dual-distribution
  encoders that align image-feature and structural-prior distributions so representations
  are anatomy-grounded rather than texture-driven; (iii) a correspondence-attention
  objective that supervises cross-attention to match anatomical regions between subject
  and atlas; and (iv) a teaching-learning-basedoptimization (TLBO) feature-selection
  stage that yields a compact descriptor consumed by a heterogeneous stacking ensemble.The
  cross-dataset protocol is restated so that no target-domain label and no target-domain
  diagnosis covariate is accessed at any stage; separate training and inference algorithms
  are given, and results are reported separately for domain generalization and unsupervised
  domain adaptation.On strictly subject-level splits CADEN attains 96.3% accuracy
  and 96.3% balanced accuracy in-domain on ADNI (both figures are five-seed means
  over seeds 0 to 4) and raises cross-dataset balanced accuracy from 76.8% to 90.6%
  (ADNI to OASIS) and from 74.2% to 88.7% (OASIS to ADNI) over a single-transformer
  baseline, exceeding the capacity-and training-budget-matched representation-level
  adaptation baselines, namely correlation alignment, maximum-mean-discrepancy matching,
  adversarial adaptation and a matched ensemble without anatomical supervision, by
  4.6 to 6.0 points, and exceeding the harmonization-only baselines by larger margins.The
  decoder''s abnormality maps localize hippocampal and ventricular change, and a neutral-atlas
  control shows this localization is not an artefact of the atlas choice (Section
  4.4).All code, subject-level split manifests, seed-wise predictions and table-regeneration
  scripts are publicly released.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222613356
url: https://doi.org/10.22266/ijies2026.1130.13
discovered_at: '2026-10-19'
tags: *id001
---

# CADEN: An Enhanced Cross\-dataset Anatomy\-aware Distribution\-alignment Ensemble Model for Alzheimer&\#x27;s Disease Detection and Staging from MRI

**Autores:** Chetna Sharma; Vivek Bhatnagar

**Data:** 2026-10-16 · **Tipo:** article

## Resumo

Deep models for Alzheimer&\#x27;s disease \(AD\) classification degrade sharply when training and deployment data originate from different scanners and cohorts, so reported single\-dataset accuracies rarely transfer to new sites\.This paper presents CADEN, an anatomy\-aware framework that learns a harmonized, atrophy\-grounded featuremapping space and performs staging by an ensemble over that space rather than over raw images\.CADEN combines four ideas: \(i\) label\-free cross\-site harmonization that couples ComBat\-style feature adjustment with a lightweight learnable site adapter; \(ii\) dual\-distribution encoders that align image\-feature and structural\-prior distributions so representations are anatomy\-grounded rather than texture\-driven; \(iii\) a correspondence\-attention objective that supervises cross\-attention to match anatomical regions between subject and atlas; and \(iv\) a teaching\-learning\-basedoptimization \(TLBO\) feature\-selection stage that yields a compact descriptor consumed by a heterogeneous stacking ensemble\.The cross\-dataset protocol is restated so that no target\-domain label and no target\-domain diagnosis covariate is accessed at any stage; separate training and inference algorithms are given, and results are reported separately for domain generalization and unsupervised domain adaptation\.On strictly subject\-level splits CADEN attains 96\.3% accuracy and 96\.3% balanced accuracy in\-domain on ADNI \(both figures are five\-seed means over seeds 0 to 4\) and raises cross\-dataset balanced accuracy from 76\.8% to 90\.6% \(ADNI to OASIS\) and from 74\.2% to 88\.7% \(OASIS to ADNI\) over a single\-transformer baseline, exceeding the capacity\-and training\-budget\-matched representation\-level adaptation baselines, namely correlation alignment, maximum\-mean\-discrepancy matching, adversarial adaptation and a matched ensemble without anatomical supervision, by 4\.6 to 6\.0 points, and exceeding the harmonization\-only baselines by larger margins\.The decoder&\#x27;s abnormality maps localize hippocampal and ventricular change, and a neutral\-atlas control shows this localization is not an artefact of the atlas choice \(Section 4\.4\)\.All code, subject\-level split manifests, seed\-wise predictions and table\-regeneration scripts are publicly released\.

[Consultar publicação](<https://doi.org/10.22266/ijies2026.1130.13>)
