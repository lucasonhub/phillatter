---
title: 'textGrain watermarking is harder to detect: can sum-tests still do it optimally?'
authors:
- Swapnaneel Bhattacharyya
- Soham Bonnerjee
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Watermarking embeds an imperceptible signal in text from large language
  models that is statistically detectable with a secret key. The recent textGrain
  watermark (Li et. al. (2026b)) calibrates this signal against the model''s sampling
  entropy through an explicit entropy budget, combining the stochasticity of Red-Green
  and the unbiasedness of Gumbel-max watermarks, and its accompanying report proposes
  a detector that sums pivotal statistics. We study when, and how efficiently, textGrain
  can be detected after human edits, modeled as a sparse mixture in which a fraction
  $\varepsilon_n\asymp n^{-p}$ of positions retain the watermark and token uncertainty
  decays as $n^{-q}$. First, entropy calibration comes at a cost: the minimax detection
  boundary of textGrain is $p+q=1/2$, so its detectable region is strictly smaller
  than that of Gumbel-max and maximal-coupling watermarks, whose boundary is $2p+q=1$.
  This cost stems from textGrain''s construction rather than from entropy calibration
  itself: an unbiased scheme with the same entropy loss remains detectable where textGrain
  is not. Second, perhaps surprisingly, this loss makes the sum detector optimal at
  the boundary when the number of transport columns is fixed, unlike for Gumbel-max.
  When the number of columns grows and the entropy budget does not vanish, the detectable
  region expands while that of the sum detector does not. Third, for a fixed edit
  fraction, we characterize the optimal exponential rate of type II error decay and
  show that the sum detector falls strictly short of it at every fixed alternative.
  Finally, we propose a weighted multiscale binomial scan, valid in finite samples
  and needing no knowledge of the next-token distributions, entropy budget, or edit
  fraction; it attains every detection boundary above and the optimal exponent.'
source:
- arXiv
source_ids:
- arxiv:2610.17655
url: https://arxiv.org/abs/2610.17655
discovered_at: '2026-10-16'
tags: *id001
---

# textGrain watermarking is harder to detect: can sum\-tests still do it optimally?

**Autores:** Swapnaneel Bhattacharyya; Soham Bonnerjee

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Watermarking embeds an imperceptible signal in text from large language models that is statistically detectable with a secret key\. The recent textGrain watermark \(Li et\. al\. \(2026b\)\) calibrates this signal against the model&\#x27;s sampling entropy through an explicit entropy budget, combining the stochasticity of Red\-Green and the unbiasedness of Gumbel\-max watermarks, and its accompanying report proposes a detector that sums pivotal statistics\. We study when, and how efficiently, textGrain can be detected after human edits, modeled as a sparse mixture in which a fraction $\\varepsilon\_n\\asymp n^\{\-p\}$ of positions retain the watermark and token uncertainty decays as $n^\{\-q\}$\. First, entropy calibration comes at a cost: the minimax detection boundary of textGrain is $p\+q=1/2$, so its detectable region is strictly smaller than that of Gumbel\-max and maximal\-coupling watermarks, whose boundary is $2p\+q=1$\. This cost stems from textGrain&\#x27;s construction rather than from entropy calibration itself: an unbiased scheme with the same entropy loss remains detectable where textGrain is not\. Second, perhaps surprisingly, this loss makes the sum detector optimal at the boundary when the number of transport columns is fixed, unlike for Gumbel\-max\. When the number of columns grows and the entropy budget does not vanish, the detectable region expands while that of the sum detector does not\. Third, for a fixed edit fraction, we characterize the optimal exponential rate of type II error decay and show that the sum detector falls strictly short of it at every fixed alternative\. Finally, we propose a weighted multiscale binomial scan, valid in finite samples and needing no knowledge of the next\-token distributions, entropy budget, or edit fraction; it attains every detection boundary above and the optimal exponent\.

[Consultar publicação](<https://arxiv.org/abs/2610.17655>)
