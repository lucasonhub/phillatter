---
title: 'Decoding What iOS Location Services Send to Apple: An LLM Is an Unreliable
  Analyst but a Useful Toolmaker'
authors:
- Douglas Leith
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Reverse engineering the data formats used by mobile software is skilled
  and slow, and using AI to assist with it is attractive. We evaluate this for the
  protobuf messages that an iPhone sends to Apple's location services. Working from
  Apple's binaries, we use two frontier models (Claude Opus 4.8, Codex GPT Sol 5.6)
  to reconstruct the schemas of protobufs observed in network traffic. The great majority
  of the schemas contain substantial errors, and these are hard to detect because
  the schemas are internally consistent. Direct AI use is therefore unsuitable for
  forensic and privacy analysis. AI can, however, write reliable analysis tools when
  their output can be validated. We use Claude to write a Python tool, Extractor,
  that reliably recovers protobuf schemas from Apple binaries. We validate it against
  binaries compiled from schemas with known answers, previously published schemas,
  and network measurements. We demonstrate the use of Extractor to decode and analyse
  the location services network traffic of a jailbroken iPhone 8 (iOS 16.7.11).
source:
- arXiv
source_ids:
- arxiv:2610.21597
url: https://arxiv.org/abs/2610.21597
discovered_at: '2026-10-16'
tags: *id001
---

# Decoding What iOS Location Services Send to Apple: An LLM Is an Unreliable Analyst but a Useful Toolmaker

**Autores:** Douglas Leith

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Reverse engineering the data formats used by mobile software is skilled and slow, and using AI to assist with it is attractive\. We evaluate this for the protobuf messages that an iPhone sends to Apple&\#x27;s location services\. Working from Apple&\#x27;s binaries, we use two frontier models \(Claude Opus 4\.8, Codex GPT Sol 5\.6\) to reconstruct the schemas of protobufs observed in network traffic\. The great majority of the schemas contain substantial errors, and these are hard to detect because the schemas are internally consistent\. Direct AI use is therefore unsuitable for forensic and privacy analysis\. AI can, however, write reliable analysis tools when their output can be validated\. We use Claude to write a Python tool, Extractor, that reliably recovers protobuf schemas from Apple binaries\. We validate it against binaries compiled from schemas with known answers, previously published schemas, and network measurements\. We demonstrate the use of Extractor to decode and analyse the location services network traffic of a jailbroken iPhone 8 \(iOS 16\.7\.11\)\.

[Consultar publicação](<https://arxiv.org/abs/2610.21597>)
