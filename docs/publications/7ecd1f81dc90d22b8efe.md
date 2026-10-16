---
title: 'SAFE-KV: Causal Suffix Repair for Behavior-Preserving Non-Prefix KV Cache
  Reuse in RAG'
authors:
- Xingjian Zhang
date: '2026-10-10'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Retrieval-augmented generation (RAG) reuses the same documents across many
  requests, making non-prefix KV-cache reuse attractive. Yet a cached document state
  is not reusable text: it is a context-conditioned causal state whose keys and values
  depend on the prefix, position, and preceding documents under which it was computed.
  We formulate non-prefix KV reuse as a behavior-preservation problem with full prefill
  on the exact prompt as the reference, and introduce SAFE-KV, which repairs a composed
  cache by re-encoding the causal suffix from a selected start document. On Qwen2.5-7B-Instruct,
  prefix-conditioned composition preserves only 47.2% of HotpotQA-500 and 37.8% of
  2Wiki-500 full-prefill answers; SAFE-KV with risk-guided K2 selection restores 99.8%/98.4%
  (donor-copy protocol) and 100.0%/98.4% with actual suffix forwarding. Document-only
  and fixed-window repairs recover far less, because the document states after the
  repaired region keep histories that omit it. Reuse without repair is exact up to
  four documents and degrades at sixteen, where suffix repair recovers 98-100%. Faithful
  repair re-encodes most of the context, so in a single-request L40S study SAFE-KV''s
  operating rule serves every workload by full prefill. SAFE-KV thus establishes the
  causal-state contract for non-prefix reuse and a validated repair mechanism that
  meets it.'
source:
- arXiv
source_ids:
- arxiv:2610.15186
url: https://arxiv.org/abs/2610.15186
discovered_at: '2026-10-16'
tags: *id001
---

# SAFE\-KV: Causal Suffix Repair for Behavior\-Preserving Non\-Prefix KV Cache Reuse in RAG

**Autores:** Xingjian Zhang

**Data:** 2026-10-10 · **Tipo:** preprint

## Resumo

Retrieval\-augmented generation \(RAG\) reuses the same documents across many requests, making non\-prefix KV\-cache reuse attractive\. Yet a cached document state is not reusable text: it is a context\-conditioned causal state whose keys and values depend on the prefix, position, and preceding documents under which it was computed\. We formulate non\-prefix KV reuse as a behavior\-preservation problem with full prefill on the exact prompt as the reference, and introduce SAFE\-KV, which repairs a composed cache by re\-encoding the causal suffix from a selected start document\. On Qwen2\.5\-7B\-Instruct, prefix\-conditioned composition preserves only 47\.2% of HotpotQA\-500 and 37\.8% of 2Wiki\-500 full\-prefill answers; SAFE\-KV with risk\-guided K2 selection restores 99\.8%/98\.4% \(donor\-copy protocol\) and 100\.0%/98\.4% with actual suffix forwarding\. Document\-only and fixed\-window repairs recover far less, because the document states after the repaired region keep histories that omit it\. Reuse without repair is exact up to four documents and degrades at sixteen, where suffix repair recovers 98\-100%\. Faithful repair re\-encodes most of the context, so in a single\-request L40S study SAFE\-KV&\#x27;s operating rule serves every workload by full prefill\. SAFE\-KV thus establishes the causal\-state contract for non\-prefix reuse and a validated repair mechanism that meets it\.

[Consultar publicação](<https://arxiv.org/abs/2610.15186>)
