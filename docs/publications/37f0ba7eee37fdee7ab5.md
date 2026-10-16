---
title: Does Morphological Correctness Matter for Tokenization? A Scrambled Control
  Study in Tagalog
authors:
- Abdul Rehman Antall
- Baidya Nath Saha
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Typology-aware tokenizers are motivated by the claim that segmentation
  which respects morpheme boundaries preserves information that frequency-driven segmentation
  destroys. Studies routinely establish that it helps while assuming the boundaries
  must be linguistically correct. We separate them. Tagalog marks voice with infixes
  (s-um-ulat ''wrote'', s-in-ulat ''was written''), so the root is not contiguous
  and no sequence of BPE merges can recover it. We build MorphAustro-Tok, a tokenizer
  that emits the root as a contiguous unit followed by a positional infix token, and
  compare it against a corpus-matched BPE baseline and, at two of three fertility
  levels, against a scrambled-morpheme control that preserves morph count, invertibility
  and per-type consistency while randomising the pseudo-infix. Across 33 runs, MorphAustro-Tok
  improves Tagalog machine translation over matched BPE by 0.84, 1.49 and 3.40 mean
  sentence-level chrF++ points. Token count does not explain the gain, since it grows
  as segmentation coarsens, and neither does capacity: at the coarsest level the scrambled
  arm carries more parameters and scores lower. Scrambling the analysis moves the
  gain by less than between-seed dispersion at both controlled levels, so we detect
  no contribution from morphological correctness at this scale.'
source:
- arXiv
source_ids:
- arxiv:2610.20859
url: https://arxiv.org/abs/2610.20859
discovered_at: '2026-10-16'
tags: *id001
---

# Does Morphological Correctness Matter for Tokenization? A Scrambled Control Study in Tagalog

**Autores:** Abdul Rehman Antall; Baidya Nath Saha

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Typology\-aware tokenizers are motivated by the claim that segmentation which respects morpheme boundaries preserves information that frequency\-driven segmentation destroys\. Studies routinely establish that it helps while assuming the boundaries must be linguistically correct\. We separate them\. Tagalog marks voice with infixes \(s\-um\-ulat &\#x27;wrote&\#x27;, s\-in\-ulat &\#x27;was written&\#x27;\), so the root is not contiguous and no sequence of BPE merges can recover it\. We build MorphAustro\-Tok, a tokenizer that emits the root as a contiguous unit followed by a positional infix token, and compare it against a corpus\-matched BPE baseline and, at two of three fertility levels, against a scrambled\-morpheme control that preserves morph count, invertibility and per\-type consistency while randomising the pseudo\-infix\. Across 33 runs, MorphAustro\-Tok improves Tagalog machine translation over matched BPE by 0\.84, 1\.49 and 3\.40 mean sentence\-level chrF\+\+ points\. Token count does not explain the gain, since it grows as segmentation coarsens, and neither does capacity: at the coarsest level the scrambled arm carries more parameters and scores lower\. Scrambling the analysis moves the gain by less than between\-seed dispersion at both controlled levels, so we detect no contribution from morphological correctness at this scale\.

[Consultar publicação](<https://arxiv.org/abs/2610.20859>)
