---
title: Does Location Matter? A Black-Box Causal Audit Reveals Model-Dependent Audio
  Grounding in LALM Hallucination
authors:
- Mohammad Khalooei
- Mohammad Sabokrou
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Large audio-language models (LALMs) frequently exhibit object hallucination,
  affirming absent sounds. The dominant mitigation, Audio-Aware Decoding (AAD), contrasts
  logits under real audio against an all-zero "blank" waveform, flagged by prior review
  as out-of-distribution. We introduce a black-box causal test that isolates the claimed
  evidence itself: localize a claim''s evidence region via CLAP similarity, remove
  it by spectral gating, and compare against a random-window control across a 2x2x2
  grid on three LALMs. On Qwen2-Audio-7B, localized ablation''s raw AUROC trails blank''s
  (0.613 vs. 0.721); this is a duration confound, not a localization failure, since
  blank removes the entire clip versus the grid''s 2-4 s. Holding duration fixed,
  localization beats random removal at every cell on both models. Raw detection value
  remains model-dependent, especially on Audio Flamingo 3. The same evidence corrects
  decoding: contrastive decoding combining blank and language-prior contrasts, gated
  and ensembled, raises Qwen2-Audio accuracy from 57.1% to 71.9%, beating AAD alone.
  A unified causal-grounding profile does not transfer between models, indicating
  different grounding regimes. The source code and a detailed report of our findings,
  including identified limitations, are available at https://github.com/khalooei/causa.'
source:
- arXiv
source_ids:
- arxiv:2610.13112
url: https://arxiv.org/abs/2610.13112
discovered_at: '2026-10-16'
tags: *id001
---

# Does Location Matter? A Black\-Box Causal Audit Reveals Model\-Dependent Audio Grounding in LALM Hallucination

**Autores:** Mohammad Khalooei; Mohammad Sabokrou

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Large audio\-language models \(LALMs\) frequently exhibit object hallucination, affirming absent sounds\. The dominant mitigation, Audio\-Aware Decoding \(AAD\), contrasts logits under real audio against an all\-zero &quot;blank&quot; waveform, flagged by prior review as out\-of\-distribution\. We introduce a black\-box causal test that isolates the claimed evidence itself: localize a claim&\#x27;s evidence region via CLAP similarity, remove it by spectral gating, and compare against a random\-window control across a 2x2x2 grid on three LALMs\. On Qwen2\-Audio\-7B, localized ablation&\#x27;s raw AUROC trails blank&\#x27;s \(0\.613 vs\. 0\.721\); this is a duration confound, not a localization failure, since blank removes the entire clip versus the grid&\#x27;s 2\-4 s\. Holding duration fixed, localization beats random removal at every cell on both models\. Raw detection value remains model\-dependent, especially on Audio Flamingo 3\. The same evidence corrects decoding: contrastive decoding combining blank and language\-prior contrasts, gated and ensembled, raises Qwen2\-Audio accuracy from 57\.1% to 71\.9%, beating AAD alone\. A unified causal\-grounding profile does not transfer between models, indicating different grounding regimes\. The source code and a detailed report of our findings, including identified limitations, are available at https://github\.com/khalooei/causa\.

[Consultar publicação](<https://arxiv.org/abs/2610.13112>)
