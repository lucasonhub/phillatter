---
title: 'MotionCoach: Constructing Multimodal Guidance for Video Professional Motion
  Editing'
authors:
- Siyi Qian
- Hanqing Yang
- Weihuang Lin
- Zihao Yang
- Yichen Lu
- Yuanhong Zheng
- Sheng Li
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Video editing models achieve strong performance in modifying appearance,
  backgrounds, styles, and motions, empowered by large-scale training data. Beyond
  general scenarios, professional motions are significant in performance, sports,
  and martial arts. This paper focuses on professional motion editing, which involves
  fine-grained motion technique and temporal structure. Given professional motion
  names but lacking detailed descriptions, existing models often fail to generate
  professional motions, such as incorrectly lifting the front wheel under a Stoppie
  instruction. To address this challenge, we introduce MotionCoach, a trained multimodal
  agent that uses multi-turn tools and performs self-verification, producing a grounded
  prompt and a reference clip as reliable and sufficient multimodal guidance to inject
  external professional motion knowledge into video editing models. To supply training
  data, we build a data pipeline to construct trajectories. We cold-start the agent
  on MotionCoach-SFT-10k and apply Group Relative Policy Optimization (GRPO) on MotionCoach-RL-2k
  with rewards on the motion guidance prompt, the motion outcome video, and the format.
  For evaluation, we introduce VPMEBench, comprising 314 professional motion editing
  tasks with fine-grained references and annotations. Extensive experiments show that
  MotionCoach improves the overall score from 55.1 to 65.6 on Seedance 2.0 and from
  51.2 to 64.5 on MiniMax-H3. Learning to construct multimodal guidance enables precise
  professional motion editing without retraining video editing models.
source:
- arXiv
source_ids:
- arxiv:2610.12963
url: https://arxiv.org/abs/2610.12963
discovered_at: '2026-10-16'
tags: *id001
---

# MotionCoach: Constructing Multimodal Guidance for Video Professional Motion Editing

**Autores:** Siyi Qian; Hanqing Yang; Weihuang Lin; Zihao Yang; Yichen Lu; Yuanhong Zheng; Sheng Li

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Video editing models achieve strong performance in modifying appearance, backgrounds, styles, and motions, empowered by large\-scale training data\. Beyond general scenarios, professional motions are significant in performance, sports, and martial arts\. This paper focuses on professional motion editing, which involves fine\-grained motion technique and temporal structure\. Given professional motion names but lacking detailed descriptions, existing models often fail to generate professional motions, such as incorrectly lifting the front wheel under a Stoppie instruction\. To address this challenge, we introduce MotionCoach, a trained multimodal agent that uses multi\-turn tools and performs self\-verification, producing a grounded prompt and a reference clip as reliable and sufficient multimodal guidance to inject external professional motion knowledge into video editing models\. To supply training data, we build a data pipeline to construct trajectories\. We cold\-start the agent on MotionCoach\-SFT\-10k and apply Group Relative Policy Optimization \(GRPO\) on MotionCoach\-RL\-2k with rewards on the motion guidance prompt, the motion outcome video, and the format\. For evaluation, we introduce VPMEBench, comprising 314 professional motion editing tasks with fine\-grained references and annotations\. Extensive experiments show that MotionCoach improves the overall score from 55\.1 to 65\.6 on Seedance 2\.0 and from 51\.2 to 64\.5 on MiniMax\-H3\. Learning to construct multimodal guidance enables precise professional motion editing without retraining video editing models\.

[Consultar publicação](<https://arxiv.org/abs/2610.12963>)
