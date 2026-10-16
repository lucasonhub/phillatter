---
title: 'HiPAD: A Unified Gait, Audio-Visual, and Personality Fusion Network for Depression
  Detection, with a Hierarchical Personality Ablation and the Calibration Limits of
  Domain-Adapted LLMs'
authors:
- Karol Chlasta
- Piotr Struzik
date: '2026-10-10'
type: preprint
category: &id001
- Inteligência Artificial
doi: 10.1145/3767308.3836618
abstract: 'We present HiPAD, a single fusion network submitted to all six sub-tracks
  of the MPDD-AVG 2026 depression-detection challenge, covering the Elder and Young
  cohorts and three modality sets (gait, audio-visual, and both), each combined with
  personality descriptions. The network encodes each available modality with a shared
  BiLSTM, zero-pads absent modalities, and applies cross-modal attention only when
  at least two of gait, audio and video are present. Personality, which dominates
  our results, is kept out of the attention and fused by concatenation. Because the
  architecture is identical in every sub-track, differences between them reflect the
  data rather than the model, and we use this to study three questions. Our main finding
  is that the personality description, roughly 150 tokens about who the subject is,
  carries more depression signal than audio, video, and gait combined: gait plus personality
  alone (TLS 0.647) beats every configuration that includes audio and video. First,
  a four-level ablation of the personality description (L0-L3) quantifies this: removing
  every personality-derived feature, including the Big Five scores that earlier MPDD
  ablations keep, lowers the Track-Level Score by 0.499 to 0.507 and leaves the model
  at chance. Second, domain-adapting the personality encoder with LoRA (7B) or QLoRA
  (72B) on PHQ-8/9 data raises binary Cohen''s $κ$ by 0.13 but lowers the overall
  score by distorting the PHQ-9 regression; a frozen RoBERTa-large encoder does better
  at this sample size. Third, at fixed architecture, handcrafted clinical features
  (eGeMAPS, OpenFace action units) outperform generic deep features (wav2vec2, DenseNet)
  on the audio-visual tracks. The unified system reaches a cross-track G-Score of
  0.482; with under 100 subjects per cohort, the limiting factors are the size of
  the representation and the calibration of the outputs, not the choice of architecture.'
source:
- arXiv
source_ids:
- arxiv:2610.14961
url: https://arxiv.org/abs/2610.14961
discovered_at: '2026-10-16'
tags: *id001
---

# HiPAD: A Unified Gait, Audio\-Visual, and Personality Fusion Network for Depression Detection, with a Hierarchical Personality Ablation and the Calibration Limits of Domain\-Adapted LLMs

**Autores:** Karol Chlasta; Piotr Struzik

**Data:** 2026-10-10 · **Tipo:** preprint

## Resumo

We present HiPAD, a single fusion network submitted to all six sub\-tracks of the MPDD\-AVG 2026 depression\-detection challenge, covering the Elder and Young cohorts and three modality sets \(gait, audio\-visual, and both\), each combined with personality descriptions\. The network encodes each available modality with a shared BiLSTM, zero\-pads absent modalities, and applies cross\-modal attention only when at least two of gait, audio and video are present\. Personality, which dominates our results, is kept out of the attention and fused by concatenation\. Because the architecture is identical in every sub\-track, differences between them reflect the data rather than the model, and we use this to study three questions\. Our main finding is that the personality description, roughly 150 tokens about who the subject is, carries more depression signal than audio, video, and gait combined: gait plus personality alone \(TLS 0\.647\) beats every configuration that includes audio and video\. First, a four\-level ablation of the personality description \(L0\-L3\) quantifies this: removing every personality\-derived feature, including the Big Five scores that earlier MPDD ablations keep, lowers the Track\-Level Score by 0\.499 to 0\.507 and leaves the model at chance\. Second, domain\-adapting the personality encoder with LoRA \(7B\) or QLoRA \(72B\) on PHQ\-8/9 data raises binary Cohen&\#x27;s $κ$ by 0\.13 but lowers the overall score by distorting the PHQ\-9 regression; a frozen RoBERTa\-large encoder does better at this sample size\. Third, at fixed architecture, handcrafted clinical features \(eGeMAPS, OpenFace action units\) outperform generic deep features \(wav2vec2, DenseNet\) on the audio\-visual tracks\. The unified system reaches a cross\-track G\-Score of 0\.482; with under 100 subjects per cohort, the limiting factors are the size of the representation and the calibration of the outputs, not the choice of architecture\.

[Consultar publicação](<https://arxiv.org/abs/2610.14961>)
