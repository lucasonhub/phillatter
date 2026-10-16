---
title: A RAG-enhanced multimodal large language model framework for culvert inspection
authors:
- Pouria Mohammadi
- Sadegh Asgari
- Abbas Rashidi
- Siavash Adibpour
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1016/j.aei.2026.105352
abstract: Despite their importance for maintaining infrastructure integrity, manual
  culvert inspections pose significant operational challenges for agencies such as
  the Utah Department of Transportation (UDOT) due to high labor demands, subjective
  assessments, and variability in evaluation outcomes. This study investigates the
  application of computer vision for automated culvert inspection, leveraging both
  supervised machine learning and emerging vision–language models. We proposed a retrieval-augmented
  generation (RAG)–enhanced multimodal large language model (MLLM) framework that
  interprets culvert-condition imagery based on the culvert inspection manual. By
  embedding a small set of curated visual exemplars into a shared space, we enabled
  image-based retrieval to ground model reasoning alongside the full inspection manual.
  For the MLLM component, we selected three open-source models (Qwen3-VL, Gemma-3,
  LLaVA-OneVision) and one proprietary model (Gemini-3-Flash). We evaluated performance
  using precision, recall, and F1-score, alongside a practical “most-severe-label”
  decision rule to simulate maintenance prioritization. Results showed that the RAG-enhanced
  Gemini-3-Flash achieved the highest severity accuracy (91.16%), outperforming the
  supervised ConvNeXt multi-label baseline (84.54%) and other evaluated MLLMs. Overall,
  the findings suggest that RAG-enhanced Gemini-3-Flash can improve the reliability
  of severity-relevant decisions while reducing data-labeling requirements by approximately
  99% (from thousands of training images to just 127 exemplars) and the GPU-intensive
  training burden, with the primary trade-offs being reliance on proprietary APIs
  and token-based inference costs.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221509940
url: https://doi.org/10.1016/j.aei.2026.105352
discovered_at: '2026-10-16'
tags: *id001
---

# A RAG\-enhanced multimodal large language model framework for culvert inspection

**Autores:** Pouria Mohammadi; Sadegh Asgari; Abbas Rashidi; Siavash Adibpour

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Despite their importance for maintaining infrastructure integrity, manual culvert inspections pose significant operational challenges for agencies such as the Utah Department of Transportation \(UDOT\) due to high labor demands, subjective assessments, and variability in evaluation outcomes\. This study investigates the application of computer vision for automated culvert inspection, leveraging both supervised machine learning and emerging vision–language models\. We proposed a retrieval\-augmented generation \(RAG\)–enhanced multimodal large language model \(MLLM\) framework that interprets culvert\-condition imagery based on the culvert inspection manual\. By embedding a small set of curated visual exemplars into a shared space, we enabled image\-based retrieval to ground model reasoning alongside the full inspection manual\. For the MLLM component, we selected three open\-source models \(Qwen3\-VL, Gemma\-3, LLaVA\-OneVision\) and one proprietary model \(Gemini\-3\-Flash\)\. We evaluated performance using precision, recall, and F1\-score, alongside a practical “most\-severe\-label” decision rule to simulate maintenance prioritization\. Results showed that the RAG\-enhanced Gemini\-3\-Flash achieved the highest severity accuracy \(91\.16%\), outperforming the supervised ConvNeXt multi\-label baseline \(84\.54%\) and other evaluated MLLMs\. Overall, the findings suggest that RAG\-enhanced Gemini\-3\-Flash can improve the reliability of severity\-relevant decisions while reducing data\-labeling requirements by approximately 99% \(from thousands of training images to just 127 exemplars\) and the GPU\-intensive training burden, with the primary trade\-offs being reliance on proprietary APIs and token\-based inference costs\.

[Consultar publicação](<https://doi.org/10.1016/j.aei.2026.105352>)
