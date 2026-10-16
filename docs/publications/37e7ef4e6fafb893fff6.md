---
title: 'Beyond Semantic IDs: Finite-Beam Reachability and Continuous-Query Generation
  in Generative Recommendation'
authors:
- Yu Sun
- Renkai Xiang
- Zuodong Xiang
- Junwei Zhou
- Yike Zhang
- Jianxin Zhang
- Zhihao Zhu
- Xiaoyu Cao
- Hailu Xu
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Generative recommendation (GR) of social media platforms commonly retrieves
  items by autoregressively decoding discrete Semantic IDs (SIDs) with finite-width
  beam search. This work examines how this output interface constrains whether held-out
  targets enter finite returned lists, while distinguishing catalog-wide scoreability
  from empirical top-K support. We introduce two continuous-query paradigms: CQG-Single
  generates one retrieval query in a single pass, and CQG-AR autoregressively generates
  continuous residual updates, retaining step-wise decoding while removing the SID
  item-token vocabulary, code lookup, and discrete beam expansion. These designs thereby
  eliminate the SID-specific reachability constraint induced by finite-beam decoding
  and avoid the technical challenge of aligning a discrete SID vocabulary with the
  pretrained backbone''s vector space. Both methods make every encoded item directly
  scoreable through dense or approximate-nearest-neighbor retrieval. Under a unified
  protocol with valid-prefix constrained decoding, CQG-Single exceeds the TIGER-style
  baseline in all seven runs while using 55.3% as many trainable parameters. CQG-AR
  remains comparable on ML-1M and is numerically stronger on Beauty and Sports datasets.
  A controlled depth ablation further shows that additional continuous refinement
  does not monotonically improve shallow accuracy. These findings motivate decoupling
  output representation, autoregressive modeling, and retrieval budget when evaluating
  generative recommendation systems.'
source:
- arXiv
source_ids:
- arxiv:2610.12977
url: https://arxiv.org/abs/2610.12977
discovered_at: '2026-10-16'
tags: *id001
---

# Beyond Semantic IDs: Finite\-Beam Reachability and Continuous\-Query Generation in Generative Recommendation

**Autores:** Yu Sun; Renkai Xiang; Zuodong Xiang; Junwei Zhou; Yike Zhang; Jianxin Zhang; Zhihao Zhu; Xiaoyu Cao; Hailu Xu

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Generative recommendation \(GR\) of social media platforms commonly retrieves items by autoregressively decoding discrete Semantic IDs \(SIDs\) with finite\-width beam search\. This work examines how this output interface constrains whether held\-out targets enter finite returned lists, while distinguishing catalog\-wide scoreability from empirical top\-K support\. We introduce two continuous\-query paradigms: CQG\-Single generates one retrieval query in a single pass, and CQG\-AR autoregressively generates continuous residual updates, retaining step\-wise decoding while removing the SID item\-token vocabulary, code lookup, and discrete beam expansion\. These designs thereby eliminate the SID\-specific reachability constraint induced by finite\-beam decoding and avoid the technical challenge of aligning a discrete SID vocabulary with the pretrained backbone&\#x27;s vector space\. Both methods make every encoded item directly scoreable through dense or approximate\-nearest\-neighbor retrieval\. Under a unified protocol with valid\-prefix constrained decoding, CQG\-Single exceeds the TIGER\-style baseline in all seven runs while using 55\.3% as many trainable parameters\. CQG\-AR remains comparable on ML\-1M and is numerically stronger on Beauty and Sports datasets\. A controlled depth ablation further shows that additional continuous refinement does not monotonically improve shallow accuracy\. These findings motivate decoupling output representation, autoregressive modeling, and retrieval budget when evaluating generative recommendation systems\.

[Consultar publicação](<https://arxiv.org/abs/2610.12977>)
