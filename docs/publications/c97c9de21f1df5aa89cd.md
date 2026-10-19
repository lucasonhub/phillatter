---
title: 'A fuzzy-augmented deep learning pipeline for multilingual natural language
  processing from handwritten script: a Tamil case study'
authors:
- Harsha Kumar A
- B. Aarthi
- K. Kumaran
- G. Saranya
- Preetham Venkatram C
date: '2026-10-14'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3389/frai.2026.1859443
abstract: 'Multilingual natural language processing (NLP) from handwritten script
  is an open artificial intelligence (AI) challenge requiring advances in both pattern
  recognition and sequence generation. Existing end-to-end pipelines often fail to
  model the structural uncertainty in complex scripts, particularly the decorative
  stroke variability in Dravidian writing systems, before passing representations
  to downstream NLP models. This omission can result in error propagation from the
  recognition stage into translation. This paper proposes a Tamil Handwritten Character
  Recognition and Translation (THCRT) framework, a fuzzy-augmented deep learning NLP
  pipeline that addresses this gap by coupling a Biparametric Exponential Membership
  Function-based Fuzzy Inference System (BEMFFIS) with a deep convolutional recognition
  network and a multilingual transformer for translation. The fuzzy inference component
  models stroke-boundary uncertainty through Decorative Stroke Analysis (DSA) using
  the Coefficient of Variation (CoV). BEMFFIS employs a coupled-parameter Gaussian
  membership function, which reduces the hyperparameter search space to a single degree
  of freedom. This produces normalized representations that improve downstream NLP
  performance. Hierarchical segmentation of line, word, and character is achieved
  via Connected Polar Functional Component Analysis (CPFCA). Recognition is performed
  by a Global Averaged Excitation-based Deep Convolutional Neural Network with Swish
  activation (GAE-DCSSNN), and multilingual translation is executed by a multilingual
  Bernoulli Distribution-based Auto-Regressive Transformer (mBBDART) built on the
  mBART backbone with stochastic token-pruning augmentation. The pipeline is evaluated
  on Tamil handwriting using two publicly available datasets: the Tamil Offline Handwritten
  Word Recognition (TOHWR) dataset and the Tamil Handwritten Character Corpus Mendeley
  Data (THCCMD) dataset. Translation quality is assessed on a 1,200-sample parallel
  reference set annotated by two certified bilingual translators with Cohen''s κ =
  0.91, reflecting the word-level and short-phrase scope of the TOHWR corpus. The
  THCRT framework achieves a recognition accuracy of 98.23%, a Character Error Rate
  (CER) of 1.12%, and a Bilingual Evaluation Understudy (BLEU) score of 0.438 on the
  annotated evaluation set, outperforming the baseline architectures on both datasets
  and demonstrating a 1.79 percentage-point accuracy gain attributed to the BEMFFIS
  stroke-uncertainty module.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222287110
url: https://doi.org/10.3389/frai.2026.1859443
discovered_at: '2026-10-19'
tags: *id001
---

# A fuzzy\-augmented deep learning pipeline for multilingual natural language processing from handwritten script: a Tamil case study

**Autores:** Harsha Kumar A; B\. Aarthi; K\. Kumaran; G\. Saranya; Preetham Venkatram C

**Data:** 2026-10-14 · **Tipo:** article

## Resumo

Multilingual natural language processing \(NLP\) from handwritten script is an open artificial intelligence \(AI\) challenge requiring advances in both pattern recognition and sequence generation\. Existing end\-to\-end pipelines often fail to model the structural uncertainty in complex scripts, particularly the decorative stroke variability in Dravidian writing systems, before passing representations to downstream NLP models\. This omission can result in error propagation from the recognition stage into translation\. This paper proposes a Tamil Handwritten Character Recognition and Translation \(THCRT\) framework, a fuzzy\-augmented deep learning NLP pipeline that addresses this gap by coupling a Biparametric Exponential Membership Function\-based Fuzzy Inference System \(BEMFFIS\) with a deep convolutional recognition network and a multilingual transformer for translation\. The fuzzy inference component models stroke\-boundary uncertainty through Decorative Stroke Analysis \(DSA\) using the Coefficient of Variation \(CoV\)\. BEMFFIS employs a coupled\-parameter Gaussian membership function, which reduces the hyperparameter search space to a single degree of freedom\. This produces normalized representations that improve downstream NLP performance\. Hierarchical segmentation of line, word, and character is achieved via Connected Polar Functional Component Analysis \(CPFCA\)\. Recognition is performed by a Global Averaged Excitation\-based Deep Convolutional Neural Network with Swish activation \(GAE\-DCSSNN\), and multilingual translation is executed by a multilingual Bernoulli Distribution\-based Auto\-Regressive Transformer \(mBBDART\) built on the mBART backbone with stochastic token\-pruning augmentation\. The pipeline is evaluated on Tamil handwriting using two publicly available datasets: the Tamil Offline Handwritten Word Recognition \(TOHWR\) dataset and the Tamil Handwritten Character Corpus Mendeley Data \(THCCMD\) dataset\. Translation quality is assessed on a 1,200\-sample parallel reference set annotated by two certified bilingual translators with Cohen&\#x27;s κ = 0\.91, reflecting the word\-level and short\-phrase scope of the TOHWR corpus\. The THCRT framework achieves a recognition accuracy of 98\.23%, a Character Error Rate \(CER\) of 1\.12%, and a Bilingual Evaluation Understudy \(BLEU\) score of 0\.438 on the annotated evaluation set, outperforming the baseline architectures on both datasets and demonstrating a 1\.79 percentage\-point accuracy gain attributed to the BEMFFIS stroke\-uncertainty module\.

[Consultar publicação](<https://doi.org/10.3389/frai.2026.1859443>)
