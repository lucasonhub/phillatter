---
title: 'LiveAnon: Improving Privacy and Utility in Streaming Speaker Anonymization
  with Codec Language Models'
authors:
- Yejin Kim
- Kyungsu Kim
- Seungu Han
- Kyogu Lee
date: '2026-10-11'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Speaker anonymization (SA) aims to conceal speaker identity while preserving
  linguistic content and emotion, but existing streaming systems often lose emotion
  information through discrete content bottlenecks or require emotion-specific modeling.
  We present LiveAnon, a voice-conversion-based streaming SA system that directly
  conditions an autoregressive codec language model on hidden features from a pretrained
  streaming ASR encoder, preserving emotion without emotion-specific supervision.
  To reduce codec-generation latency, we introduce capped RVQ decoding, which preserves
  dependencies among coarse codebooks while predicting the remaining codebooks in
  parallel. Under VPC24, LiveAnon improves intelligibility and emotion preservation
  over fixed-target Stream-Voice-Anon (SVA), a strong prior streaming SA system, matches
  emotion-prompted SVA in emotion preservation, and achieves the strongest semi-informed
  privacy among streaming systems. Under VPC26, it ranks second across all metrics
  among the evaluated anonymization systems, demonstrating a strong privacy-utility
  balance.
source:
- arXiv
source_ids:
- arxiv:2610.15379
url: https://arxiv.org/abs/2610.15379
discovered_at: '2026-10-16'
tags: *id001
---

# LiveAnon: Improving Privacy and Utility in Streaming Speaker Anonymization with Codec Language Models

**Autores:** Yejin Kim; Kyungsu Kim; Seungu Han; Kyogu Lee

**Data:** 2026-10-11 · **Tipo:** preprint

## Resumo

Speaker anonymization \(SA\) aims to conceal speaker identity while preserving linguistic content and emotion, but existing streaming systems often lose emotion information through discrete content bottlenecks or require emotion\-specific modeling\. We present LiveAnon, a voice\-conversion\-based streaming SA system that directly conditions an autoregressive codec language model on hidden features from a pretrained streaming ASR encoder, preserving emotion without emotion\-specific supervision\. To reduce codec\-generation latency, we introduce capped RVQ decoding, which preserves dependencies among coarse codebooks while predicting the remaining codebooks in parallel\. Under VPC24, LiveAnon improves intelligibility and emotion preservation over fixed\-target Stream\-Voice\-Anon \(SVA\), a strong prior streaming SA system, matches emotion\-prompted SVA in emotion preservation, and achieves the strongest semi\-informed privacy among streaming systems\. Under VPC26, it ranks second across all metrics among the evaluated anonymization systems, demonstrating a strong privacy\-utility balance\.

[Consultar publicação](<https://arxiv.org/abs/2610.15379>)
