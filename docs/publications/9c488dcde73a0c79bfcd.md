---
title: OMNI_BUILD INTELLIGENCE An LLM-Based Framework for Constraint-Aware Architectural
  Floor-Plan Generation, Visualization, and Interactive Project Management
authors:
- Somen Poria
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.55041/ijcope.v2i10.034
abstract: 'The increasing capability of large language models (LLMs) creates an opportunity
  to redesign how users interact with computational design software. Architectural
  planning is a particularly relevant domain because early-stage requirements are
  often expressed in natural language, while the resulting design must ultimately
  be represented as geometry. This paper presents Omni Build Intelligence, an implemented
  full-stack prototype that explores an LLM-assisted workflow for generating preliminary
  architectural floor plans from structured user requirements. The system accepts
  building type, requested room count, plot width and length, and special requirements.
  A Flask backend constructs a domain-specific prompt and invokes a Llama 3.3 70B
  model through the Grok API. The response is expected in a structured textual format
  containing rooms, coordinates, dimensions, door relationships, and a summary. The
  generated representation is parsed into easy for software to read objects and passed
  to a React interface. The interface provides a two-dimensional blueprint view and
  an isometric three-dimensional visualization. A conversion layer transforms generated
  room rectangles into editable wall and label primitives that can be associated with
  a project record. The broader platform also includes authentication, project management,
  plot listing and filtering, dashboard functionality, and persistence of drawing
  data. These components make Omni Build more than a standalone text-generation demonstration:
  it is a prototype for integrating generative AI into an interactive design workflow.
  The research contribution of this paper is the formulation of a rigorous evaluation
  methodology for such a system. The proposed methodology defines an Architectural
  Requirement Prompt Dataset, meaningful baselines, formal geometric constraints,
  automated validation metrics, human evaluation criteria, ablation experiments, and
  statistical analysis procedures. Metrics include constraint satisfaction, boundary
  violations, room overlap, requirement accuracy, dimension validity, space use of
  space, valid-plan rate, and generation latency. A user guided study is proposed
  to evaluate perceived practicality and usefulness. The study deliberately does not
  claim measured superiority because the repository provides implementation evidence
  but not a completed controlled benchmark. Instead, the paper establishes a reproducible
  experimental framework through which the system can be evaluated. This distinction
  prevents software functionality from being mistaken for research evidence. The work
  concludes that LLM-based architectural assistance is most appropriately positioned
  as an early-stage design aid whose natural-language flexibility is combined with
  explicit geometric validation and human review. Keywords: large language models,
  generative AI, computer based architectural design, floor-plan generation, constraint
  based prompting, spatial reasoning, structured generation, user guided design, interactive
  visualization, project management'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221129707
url: https://doi.org/10.55041/ijcope.v2i10.034
discovered_at: '2026-10-16'
tags: *id001
---

# OMNI\_BUILD INTELLIGENCE An LLM\-Based Framework for Constraint\-Aware Architectural Floor\-Plan Generation, Visualization, and Interactive Project Management

**Autores:** Somen Poria

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

The increasing capability of large language models \(LLMs\) creates an opportunity to redesign how users interact with computational design software\. Architectural planning is a particularly relevant domain because early\-stage requirements are often expressed in natural language, while the resulting design must ultimately be represented as geometry\. This paper presents Omni Build Intelligence, an implemented full\-stack prototype that explores an LLM\-assisted workflow for generating preliminary architectural floor plans from structured user requirements\. The system accepts building type, requested room count, plot width and length, and special requirements\. A Flask backend constructs a domain\-specific prompt and invokes a Llama 3\.3 70B model through the Grok API\. The response is expected in a structured textual format containing rooms, coordinates, dimensions, door relationships, and a summary\. The generated representation is parsed into easy for software to read objects and passed to a React interface\. The interface provides a two\-dimensional blueprint view and an isometric three\-dimensional visualization\. A conversion layer transforms generated room rectangles into editable wall and label primitives that can be associated with a project record\. The broader platform also includes authentication, project management, plot listing and filtering, dashboard functionality, and persistence of drawing data\. These components make Omni Build more than a standalone text\-generation demonstration: it is a prototype for integrating generative AI into an interactive design workflow\. The research contribution of this paper is the formulation of a rigorous evaluation methodology for such a system\. The proposed methodology defines an Architectural Requirement Prompt Dataset, meaningful baselines, formal geometric constraints, automated validation metrics, human evaluation criteria, ablation experiments, and statistical analysis procedures\. Metrics include constraint satisfaction, boundary violations, room overlap, requirement accuracy, dimension validity, space use of space, valid\-plan rate, and generation latency\. A user guided study is proposed to evaluate perceived practicality and usefulness\. The study deliberately does not claim measured superiority because the repository provides implementation evidence but not a completed controlled benchmark\. Instead, the paper establishes a reproducible experimental framework through which the system can be evaluated\. This distinction prevents software functionality from being mistaken for research evidence\. The work concludes that LLM\-based architectural assistance is most appropriately positioned as an early\-stage design aid whose natural\-language flexibility is combined with explicit geometric validation and human review\. Keywords: large language models, generative AI, computer based architectural design, floor\-plan generation, constraint based prompting, spatial reasoning, structured generation, user guided design, interactive visualization, project management

[Consultar publicação](<https://doi.org/10.55041/ijcope.v2i10.034>)
