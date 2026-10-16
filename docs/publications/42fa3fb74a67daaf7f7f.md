---
title: 'MangoVQA: A Multi-Answer Visual Question Answering System for Grading SNI-Aligned
  Mango Quality using Deep Learning and Text Processing'
authors:
- Nidaul Hasanati
- Taufik Djatna
- Imas Sukaesih Sitanggang
- Arif Imam Suroso
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.15408/aism.v9i2.53416
abstract: Visual Question Answering (VQA), a multimodal AI task combining computer
  vision and language understanding, answers text-based questions about visual content.
  Although VQA has developed rapidly, most existing approaches assume a single correct
  answer, whereas real-world images often require several valid answers simultaneously.
  This study proposes MangoVQA, to our knowledge the first multi-answer VQA framework
  for mango quality grading aligned with SNI 3164:2024. MangoVQA separates perception
  from reasoning, combining YOLOv11n-based neural perception with deterministic, rule-based
  question interpretation, unlike end-to-end learned-fusion VQA models. Each answer
  is grounded in detected mango instances, enabling traceable multi-answer responses
  rather than opaque predictions. The YOLOv11n detector localizes fruits and identifies
  four quality grades (Extra Class, Class I, Class II, and Reject), while the Perspective
  Engine extracts color and defect attributes through calibrated HSV analysis. These
  facts populate a structured answer representation, queried via predefined intents
  and slots. From 468 annotated images, the pipeline yielded 17,764 question-answer
  pairs across 22 question types, two reasoning levels, and two languages. 22.85%
  of questions required multi-answer responses, scored with set-based precision, recall,
  F1-score, and subset exact match. Evaluation reaches 0.919 accuracy on global open-ended
  questions, 0.937 on local open-ended questions, and 0.846 micro-F1 on global multi-answer
  questions, exceeding the 62.91% F1 reported by EMQA, the only prior multi-answer
  VQA baseline, on a different dataset. Practically, MangoVQA offers auditable decision
  support for smallholders, cooperatives, exporters needing SNI-compliant evidence,
  and mango customers; theoretically, decoupling visual perception from text interpretation
  and reasoning offers a viable, interpretable alternative to end-to-end multimodal
  fusion.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221160106
url: https://doi.org/10.15408/aism.v9i2.53416
discovered_at: '2026-10-16'
tags: *id001
---

# MangoVQA: A Multi\-Answer Visual Question Answering System for Grading SNI\-Aligned Mango Quality using Deep Learning and Text Processing

**Autores:** Nidaul Hasanati; Taufik Djatna; Imas Sukaesih Sitanggang; Arif Imam Suroso

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

Visual Question Answering \(VQA\), a multimodal AI task combining computer vision and language understanding, answers text\-based questions about visual content\. Although VQA has developed rapidly, most existing approaches assume a single correct answer, whereas real\-world images often require several valid answers simultaneously\. This study proposes MangoVQA, to our knowledge the first multi\-answer VQA framework for mango quality grading aligned with SNI 3164:2024\. MangoVQA separates perception from reasoning, combining YOLOv11n\-based neural perception with deterministic, rule\-based question interpretation, unlike end\-to\-end learned\-fusion VQA models\. Each answer is grounded in detected mango instances, enabling traceable multi\-answer responses rather than opaque predictions\. The YOLOv11n detector localizes fruits and identifies four quality grades \(Extra Class, Class I, Class II, and Reject\), while the Perspective Engine extracts color and defect attributes through calibrated HSV analysis\. These facts populate a structured answer representation, queried via predefined intents and slots\. From 468 annotated images, the pipeline yielded 17,764 question\-answer pairs across 22 question types, two reasoning levels, and two languages\. 22\.85% of questions required multi\-answer responses, scored with set\-based precision, recall, F1\-score, and subset exact match\. Evaluation reaches 0\.919 accuracy on global open\-ended questions, 0\.937 on local open\-ended questions, and 0\.846 micro\-F1 on global multi\-answer questions, exceeding the 62\.91% F1 reported by EMQA, the only prior multi\-answer VQA baseline, on a different dataset\. Practically, MangoVQA offers auditable decision support for smallholders, cooperatives, exporters needing SNI\-compliant evidence, and mango customers; theoretically, decoupling visual perception from text interpretation and reasoning offers a viable, interpretable alternative to end\-to\-end multimodal fusion\.

[Consultar publicação](<https://doi.org/10.15408/aism.v9i2.53416>)
