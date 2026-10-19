---
title: 'pDOC-STANet: A spatiotemporal attention network for automatic assessment of
  prolonged disorders of consciousness using fNIRS'
authors:
- Zehai Li
- Yuxin Xing
- Shuwei Wang
- Ke Cui
- Xiaobo Chen
- Huijuan Wu
- Yuyi Feng
- Pengfei Yi
- Sailing He
date: '2026-10-15'
type: article
category: &id001
- Ciências Cognitivas
- Inteligência Artificial
doi: 10.1007/s10489-026-07542-1
abstract: Abstract This study addresses the difficulty and subjectivity of assessing
  consciousness levels in patients with prolonged disorders of consciousness (pDOC)
  by proposing an automated classification method based on functional near-infrared
  spectroscopy (fNIRS). A spatiotemporal attention-based feature-fusion network, termed
  pDOC-STANet, was developed. The temporal branch extracts multiscale features using
  an improved InceptionTime architecture with squeeze-and-excitation modules, whereas
  the image branch represents each trial as channel-wise Gramian Angular Difference
  Field (GADF) maps and processes the resulting 105 × 330 × 330 tensor with a modified
  ResNet18. An attention-fusion module adaptively integrates the two representations.
  The model was evaluated using stratified, subject-independent five-fold cross-validation,
  with all trials from each participant kept in the same fold. pDOC-STANet achieved
  an accuracy of 88.72%, outperforming traditional machine-learning methods and single-branch
  deep-learning baselines. Ablation experiments confirmed the contributions of GADF
  encoding, dual-branch modeling, and attention-based fusion. LIME and SHAP analyses
  further indicated that the model relied on discriminative channels in bilateral
  frontotemporal and prefrontal regions, with HbR- and HbT-related features making
  substantial contributions. These results suggest that pDOC-STANet is a promising
  framework for fNIRS-based consciousness assessment, while external multi-center
  validation remains necessary before broad clinical deployment.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222300481
url: https://doi.org/10.1007/s10489-026-07542-1
discovered_at: '2026-10-19'
tags: *id001
---

# pDOC\-STANet: A spatiotemporal attention network for automatic assessment of prolonged disorders of consciousness using fNIRS

**Autores:** Zehai Li; Yuxin Xing; Shuwei Wang; Ke Cui; Xiaobo Chen; Huijuan Wu; Yuyi Feng; Pengfei Yi; Sailing He

**Data:** 2026-10-15 · **Tipo:** article

## Resumo

Abstract This study addresses the difficulty and subjectivity of assessing consciousness levels in patients with prolonged disorders of consciousness \(pDOC\) by proposing an automated classification method based on functional near\-infrared spectroscopy \(fNIRS\)\. A spatiotemporal attention\-based feature\-fusion network, termed pDOC\-STANet, was developed\. The temporal branch extracts multiscale features using an improved InceptionTime architecture with squeeze\-and\-excitation modules, whereas the image branch represents each trial as channel\-wise Gramian Angular Difference Field \(GADF\) maps and processes the resulting 105 × 330 × 330 tensor with a modified ResNet18\. An attention\-fusion module adaptively integrates the two representations\. The model was evaluated using stratified, subject\-independent five\-fold cross\-validation, with all trials from each participant kept in the same fold\. pDOC\-STANet achieved an accuracy of 88\.72%, outperforming traditional machine\-learning methods and single\-branch deep\-learning baselines\. Ablation experiments confirmed the contributions of GADF encoding, dual\-branch modeling, and attention\-based fusion\. LIME and SHAP analyses further indicated that the model relied on discriminative channels in bilateral frontotemporal and prefrontal regions, with HbR\- and HbT\-related features making substantial contributions\. These results suggest that pDOC\-STANet is a promising framework for fNIRS\-based consciousness assessment, while external multi\-center validation remains necessary before broad clinical deployment\.

[Consultar publicação](<https://doi.org/10.1007/s10489-026-07542-1>)
