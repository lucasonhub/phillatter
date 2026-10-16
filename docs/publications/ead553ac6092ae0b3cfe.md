---
title: 'PlacePulse: Learning Transferable Place Representations from Structural Geographic
  Data'
authors:
- Lucía García-Duarte
- Miguel Álvarez
- Diego Vicente
- Javier Pérez Trufero
- Javier de la Torre
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Geospatial machine learning often depends on task-specific feature engineering
  over large collections of sociodemographic, business, and environmental variables.
  Geospatial foundation models offer reusable representations of place, but leading
  approaches typically encode dynamic signals, such as mobility and search activity,
  or visual signals from satellite imagery. Few models represent the static structural
  composition of places (who lives and works there, which businesses operate there,
  and which risks they face) as transferable embeddings at fine spatial resolution.
  We introduce PlacePulse, a structural geospatial foundation model that compresses
  572 attributes, expanded to 2,288 inputs through H3 neighborhood aggregates, into
  256-dimensional unit-norm embeddings for 1,055,537 H3 resolution-7 cells in the
  United States. We also introduce a reusable two-axis benchmark that separates intrinsic
  representation quality from downstream predictive utility across multiple targets
  and spatial supports. Intrinsically, the embeddings reconstruct standardized inputs
  with mean $R^2 = 0.853$, use 251 of 256 approximately decorrelated dimensions, and
  show strong spatial organization, with Moran's $I = 0.93$ on the leading principal
  component and autocorrelation persisting beyond the input radius. Extrinsically,
  across 74 held-out targets from 12 external sources and four spatial supports, PlacePulse
  outperforms a dimensionality-matched feature-selection baseline on targets unrelated
  to the training inputs and is competitive with Google's Population Dynamics Foundation
  Model, leading on health, economic, election, economic-mobility and social-vulnerability
  outcomes, with relative strengths that vary by domain. These findings position structural
  composition as a distinct and complementary modality for geospatial foundation models,
  not simply a fallback where behavioral or imagery data are unavailable.
source:
- arXiv
source_ids:
- arxiv:2610.13390
url: https://arxiv.org/abs/2610.13390
discovered_at: '2026-10-16'
tags: *id001
---

# PlacePulse: Learning Transferable Place Representations from Structural Geographic Data

**Autores:** Lucía García\-Duarte; Miguel Álvarez; Diego Vicente; Javier Pérez Trufero; Javier de la Torre

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Geospatial machine learning often depends on task\-specific feature engineering over large collections of sociodemographic, business, and environmental variables\. Geospatial foundation models offer reusable representations of place, but leading approaches typically encode dynamic signals, such as mobility and search activity, or visual signals from satellite imagery\. Few models represent the static structural composition of places \(who lives and works there, which businesses operate there, and which risks they face\) as transferable embeddings at fine spatial resolution\. We introduce PlacePulse, a structural geospatial foundation model that compresses 572 attributes, expanded to 2,288 inputs through H3 neighborhood aggregates, into 256\-dimensional unit\-norm embeddings for 1,055,537 H3 resolution\-7 cells in the United States\. We also introduce a reusable two\-axis benchmark that separates intrinsic representation quality from downstream predictive utility across multiple targets and spatial supports\. Intrinsically, the embeddings reconstruct standardized inputs with mean $R^2 = 0\.853$, use 251 of 256 approximately decorrelated dimensions, and show strong spatial organization, with Moran&\#x27;s $I = 0\.93$ on the leading principal component and autocorrelation persisting beyond the input radius\. Extrinsically, across 74 held\-out targets from 12 external sources and four spatial supports, PlacePulse outperforms a dimensionality\-matched feature\-selection baseline on targets unrelated to the training inputs and is competitive with Google&\#x27;s Population Dynamics Foundation Model, leading on health, economic, election, economic\-mobility and social\-vulnerability outcomes, with relative strengths that vary by domain\. These findings position structural composition as a distinct and complementary modality for geospatial foundation models, not simply a fallback where behavioral or imagery data are unavailable\.

[Consultar publicação](<https://arxiv.org/abs/2610.13390>)
