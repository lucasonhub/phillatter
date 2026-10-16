---
title: 'MIDI-REPA: Improving Text-to-Music Generation with Symbolic Representation
  Alignment'
authors:
- Song-Ze Yu
- Fang-Duo Tsai
- Yi-Hsuan Yang
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: State-of-the-art text-to-music models increasingly rely on scaling model
  capacity, data, and compute, while still learning musical structure directly from
  dense audio. Yet melody, rhythm, harmony, and structure can be represented compactly
  in symbolic form. We introduce MIDI-REPA, a representation-alignment framework that
  derives MIDI supervision from automatic music transcription (AMT) to align intermediate
  representations of a flow-matching DiT. Building on the 122M-parameter FluxAudio-S
  baseline from the 2026 ICME Academic Text-To-Music Challenge, we investigate what,
  where, and when to align. Aligning a MuScriptor-derived piano roll with an early
  DiT layer throughout the full flow trajectory performs the best. Without additional
  training data or techniques, MIDI-REPA remains competitive on the ATTM objective
  metrics while remaining trainable on a single RTX 3090 in about 31 hours. Our results
  highlight symbolic supervision as a simple and inexpensive learning signal for improving
  text-to-music generation. We release our transcription pipeline, JamendoMIDI, training
  code, and audio samples at https://midi-repa.vaclis.net.
source:
- arXiv
source_ids:
- arxiv:2610.20967
url: https://arxiv.org/abs/2610.20967
discovered_at: '2026-10-16'
tags: *id001
---

# MIDI\-REPA: Improving Text\-to\-Music Generation with Symbolic Representation Alignment

**Autores:** Song\-Ze Yu; Fang\-Duo Tsai; Yi\-Hsuan Yang

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

State\-of\-the\-art text\-to\-music models increasingly rely on scaling model capacity, data, and compute, while still learning musical structure directly from dense audio\. Yet melody, rhythm, harmony, and structure can be represented compactly in symbolic form\. We introduce MIDI\-REPA, a representation\-alignment framework that derives MIDI supervision from automatic music transcription \(AMT\) to align intermediate representations of a flow\-matching DiT\. Building on the 122M\-parameter FluxAudio\-S baseline from the 2026 ICME Academic Text\-To\-Music Challenge, we investigate what, where, and when to align\. Aligning a MuScriptor\-derived piano roll with an early DiT layer throughout the full flow trajectory performs the best\. Without additional training data or techniques, MIDI\-REPA remains competitive on the ATTM objective metrics while remaining trainable on a single RTX 3090 in about 31 hours\. Our results highlight symbolic supervision as a simple and inexpensive learning signal for improving text\-to\-music generation\. We release our transcription pipeline, JamendoMIDI, training code, and audio samples at https://midi\-repa\.vaclis\.net\.

[Consultar publicação](<https://arxiv.org/abs/2610.20967>)
