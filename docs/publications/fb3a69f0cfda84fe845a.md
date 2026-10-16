---
title: 'TimeCap: A Scalable Open-Source Pipeline for Captioning Wearable Health Time-Series
  Data'
authors:
- Max Rosenblattl
- Milana Gurbanova
- Karl Aurel Deck
- Narayan Schuetz
- Thomas Kaar
- Manuel Milling
- Nicolas Zumarraga
- Ning Wang
- Kelly W. Zhang
- Anders Johnson
- Robert Jakob
- Björn W. Schuller
- Elgar Fleisch
- Daniel Seung Kim
- Allan Lawrie
- Patrick Langer
- Maxwell A. Xu
- Euan Ashley
- Paul Schmiedmayer
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Time-series data generated continuously across industrial, environmental,
  and especially health domains produce multimodal signals whose scale and heterogeneity
  make their processing and interpretation particularly challenging. Time-Series Language
  Models (TSLMs) promise scalable interpretation of these signals, yet remain bottlenecked
  by a fundamental lack of text-annotated time series pairs that are signal-grounded,
  reproducible, and extensible across modalities and schemas. Existing paired corpora
  are either closed or limited in scale and modality coverage. Annotation with large
  language models could scale them up, but its outputs cannot be regenerated exactly,
  which prevents others from re-deriving, extending, or auditing the resulting corpus.
  To address this, we release TimeCap, an open deterministic captioning pipeline with
  three reusable extractor tiers and a cross-channel synthesis layer that operates
  directly on the signal with no language model in the loop, extensible to new schemas
  by writing channel definitions alone. This positions TimeCap as a reproducible mechanism
  for future dataset generation rather than a one-off release. Applying TimeCap to
  OpenMHC, the MyHeart Counts wearable dataset, yields MHCap, the largest open caption
  layer for multimodal wearable time-series data. MHCap spans 19 Apple HealthKit channels
  and 7,005,763 captions over 908,944 person-days. To showcase the impact of the corpus,
  we train OpenTSLM, a time-series language model, on MHCap and benchmark on health-outcome
  prediction. Caption-augmented training (OpenTSLM-Cap) outperforms a label-only baseline
  on 29 of 32 per-user binary evaluations across 8 tasks.
source:
- arXiv
source_ids:
- arxiv:2610.21274
url: https://arxiv.org/abs/2610.21274
discovered_at: '2026-10-16'
tags: *id001
---

# TimeCap: A Scalable Open\-Source Pipeline for Captioning Wearable Health Time\-Series Data

**Autores:** Max Rosenblattl; Milana Gurbanova; Karl Aurel Deck; Narayan Schuetz; Thomas Kaar; Manuel Milling; Nicolas Zumarraga; Ning Wang; Kelly W\. Zhang; Anders Johnson; Robert Jakob; Björn W\. Schuller; Elgar Fleisch; Daniel Seung Kim; Allan Lawrie; Patrick Langer; Maxwell A\. Xu; Euan Ashley; Paul Schmiedmayer

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Time\-series data generated continuously across industrial, environmental, and especially health domains produce multimodal signals whose scale and heterogeneity make their processing and interpretation particularly challenging\. Time\-Series Language Models \(TSLMs\) promise scalable interpretation of these signals, yet remain bottlenecked by a fundamental lack of text\-annotated time series pairs that are signal\-grounded, reproducible, and extensible across modalities and schemas\. Existing paired corpora are either closed or limited in scale and modality coverage\. Annotation with large language models could scale them up, but its outputs cannot be regenerated exactly, which prevents others from re\-deriving, extending, or auditing the resulting corpus\. To address this, we release TimeCap, an open deterministic captioning pipeline with three reusable extractor tiers and a cross\-channel synthesis layer that operates directly on the signal with no language model in the loop, extensible to new schemas by writing channel definitions alone\. This positions TimeCap as a reproducible mechanism for future dataset generation rather than a one\-off release\. Applying TimeCap to OpenMHC, the MyHeart Counts wearable dataset, yields MHCap, the largest open caption layer for multimodal wearable time\-series data\. MHCap spans 19 Apple HealthKit channels and 7,005,763 captions over 908,944 person\-days\. To showcase the impact of the corpus, we train OpenTSLM, a time\-series language model, on MHCap and benchmark on health\-outcome prediction\. Caption\-augmented training \(OpenTSLM\-Cap\) outperforms a label\-only baseline on 29 of 32 per\-user binary evaluations across 8 tasks\.

[Consultar publicação](<https://arxiv.org/abs/2610.21274>)
