---
title: 'RoTA-Bench: Evaluating 3D Spatial Reasoning through Interactive Projection
  Alignment'
authors:
- Qingchuan Ma
- Yuexiao Ma
- Xiang Meng
- Yixuan Zou
- Tianyu Xie
- Wang Chen
- Yuhui Zeng
- Yuhang Wu
- Xiawu Zheng
- Rongrong Ji
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Can vision-language models turn 2D observations into 3D understanding that
  supports precise action? This requires inferring object geometry, anticipating the
  effects of rotation, and refining actions through visual feedback. We introduce
  RoTA-Bench to evaluate these abilities through interactive 3D-to-2D projection alignment.
  Given a target silhouette, a model observes a rotated object and chooses successive
  rotations to recover the target projection within a limited action budget. Our automated
  pipeline constructs silhouette-preserving 3D objects from 2D icons and uses reversible
  initialization to guarantee solvability, yielding 674 tasks and a stratified 100-task
  test set. Empirically, we find that (i) a substantial human-model gap persists:
  GPT-5.6-Sol succeeds on only 17% of tasks, whereas 20 undergraduate participants
  collectively complete the test set four times with a 100% success rate; (ii) image-space
  and pose-space progress can diverge: at matched states, the model more often improves
  silhouette overlap while worsening pose alignment than humans (19.4% vs. 10.9%);
  and (iii) fine-grained control is sensitive to interaction history: removing it
  leaves 96.8% of the model''s actions at a coarse 30-degree step size and sharply
  reduces observed task success. These findings highlight the challenge of converting
  visual evidence into precise 3D control, beyond recognizing or matching individual
  images.'
source:
- arXiv
source_ids:
- arxiv:2610.17665
url: https://arxiv.org/abs/2610.17665
discovered_at: '2026-10-16'
tags: *id001
---

# RoTA\-Bench: Evaluating 3D Spatial Reasoning through Interactive Projection Alignment

**Autores:** Qingchuan Ma; Yuexiao Ma; Xiang Meng; Yixuan Zou; Tianyu Xie; Wang Chen; Yuhui Zeng; Yuhang Wu; Xiawu Zheng; Rongrong Ji

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Can vision\-language models turn 2D observations into 3D understanding that supports precise action? This requires inferring object geometry, anticipating the effects of rotation, and refining actions through visual feedback\. We introduce RoTA\-Bench to evaluate these abilities through interactive 3D\-to\-2D projection alignment\. Given a target silhouette, a model observes a rotated object and chooses successive rotations to recover the target projection within a limited action budget\. Our automated pipeline constructs silhouette\-preserving 3D objects from 2D icons and uses reversible initialization to guarantee solvability, yielding 674 tasks and a stratified 100\-task test set\. Empirically, we find that \(i\) a substantial human\-model gap persists: GPT\-5\.6\-Sol succeeds on only 17% of tasks, whereas 20 undergraduate participants collectively complete the test set four times with a 100% success rate; \(ii\) image\-space and pose\-space progress can diverge: at matched states, the model more often improves silhouette overlap while worsening pose alignment than humans \(19\.4% vs\. 10\.9%\); and \(iii\) fine\-grained control is sensitive to interaction history: removing it leaves 96\.8% of the model&\#x27;s actions at a coarse 30\-degree step size and sharply reduces observed task success\. These findings highlight the challenge of converting visual evidence into precise 3D control, beyond recognizing or matching individual images\.

[Consultar publicação](<https://arxiv.org/abs/2610.17665>)
