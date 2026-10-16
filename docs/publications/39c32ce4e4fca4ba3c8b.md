---
title: Language-supervised electrocardiogram interpretation with vision transformer
authors:
- Xue Zhou
- 天慧 李
- Keijiro Nakamura
- Hiromasa Hayama
- Shing-Hong Liu
- Tetsuo Sasano
- Wenxi Chen
- Xin Zhu
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1007/s13755-026-00482-7
abstract: Most artificial intelligence models for electrocardiogram (ECG) interpretation
  rely on task-specific supervised learning, requiring dedicated labeled datasets
  for each diagnostic task and limiting scalability across diverse cardiac conditions.
  This study investigated whether vision-language learning from paired ECG recordings
  and summary reports could enable transferable ECG representations without task-specific
  supervised training. We developed ECG-VLM, a contrastive vision-language model consisting
  of a Transformer-based image encoder and a text encoder, trained on 800,034 paired
  10-s ECG recordings and summary reports from the MIMIC-IV-ECG database. Cardiac
  condition detection was performed using natural-language prompts without condition-specific
  retraining or fine-tuning. Performance was evaluated on an internal test set and
  externally validated using the LSAS-ECG dataset (45,151 recordings) across 14 cardiac
  conditions, together with retrieval and subgroup analysis. ECG-VLM achieved diagnostic
  performance across 14 cardiac conditions, with AUROC ranging from 0.679 to 0.981
  on the internal test set and from 0.691 to 0.991 on external validation. Performance
  was strongest for rhythm abnormalities (mean AUROC 0.948 internally and 0.921 externally)
  and lower for morphological conditions. Compared with the previously reported signal-based
  ECG-CLIP framework, ECG-VLM achieved comparable performance for rhythm abnormalities
  while improving AUPRC for several morphological conditions. Performance remained
  broadly consistent across external validation and demographic and clinical subgroups.
  These findings demonstrate the feasibility of vision-language supervision from paired
  ECG recordings and summary reports for learning transferable ECG representations
  without task-specific supervised training. This framework provides a basis for future
  extension of vision-language learning to ECG images encountered in routine clinical
  practice.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221684726
url: https://doi.org/10.1007/s13755-026-00482-7
discovered_at: '2026-10-16'
tags: *id001
---

# Language\-supervised electrocardiogram interpretation with vision transformer

**Autores:** Xue Zhou; 天慧 李; Keijiro Nakamura; Hiromasa Hayama; Shing\-Hong Liu; Tetsuo Sasano; Wenxi Chen; Xin Zhu

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Most artificial intelligence models for electrocardiogram \(ECG\) interpretation rely on task\-specific supervised learning, requiring dedicated labeled datasets for each diagnostic task and limiting scalability across diverse cardiac conditions\. This study investigated whether vision\-language learning from paired ECG recordings and summary reports could enable transferable ECG representations without task\-specific supervised training\. We developed ECG\-VLM, a contrastive vision\-language model consisting of a Transformer\-based image encoder and a text encoder, trained on 800,034 paired 10\-s ECG recordings and summary reports from the MIMIC\-IV\-ECG database\. Cardiac condition detection was performed using natural\-language prompts without condition\-specific retraining or fine\-tuning\. Performance was evaluated on an internal test set and externally validated using the LSAS\-ECG dataset \(45,151 recordings\) across 14 cardiac conditions, together with retrieval and subgroup analysis\. ECG\-VLM achieved diagnostic performance across 14 cardiac conditions, with AUROC ranging from 0\.679 to 0\.981 on the internal test set and from 0\.691 to 0\.991 on external validation\. Performance was strongest for rhythm abnormalities \(mean AUROC 0\.948 internally and 0\.921 externally\) and lower for morphological conditions\. Compared with the previously reported signal\-based ECG\-CLIP framework, ECG\-VLM achieved comparable performance for rhythm abnormalities while improving AUPRC for several morphological conditions\. Performance remained broadly consistent across external validation and demographic and clinical subgroups\. These findings demonstrate the feasibility of vision\-language supervision from paired ECG recordings and summary reports for learning transferable ECG representations without task\-specific supervised training\. This framework provides a basis for future extension of vision\-language learning to ECG images encountered in routine clinical practice\.

[Consultar publicação](<https://doi.org/10.1007/s13755-026-00482-7>)
