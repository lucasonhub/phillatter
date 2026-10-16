---
title: Prediction of Plasma Concentration−Time Profiles in Mice from Chemical Structure
  Using a Kinetically Constrained Hybrid Neural ODE
authors:
- Yuki Doi
- Harutoshi Kato
- Fumiyoshi Yamashita
date: '2026-10-12'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1021/acs.molpharmaceut.6c00453
abstract: 'Abstract Predicting plasma concentration−time profiles directly from chemical
  structure remains intrinsically challenging in early drug discovery. Existing approaches
  typically fall into two paradigms: mechanistic reconstruction via predicted PK parameters,
  which is constrained by the assumed model structure, and direct data-driven prediction
  of concentrations, which often suffers from instability and poor temporal coherence
  under sparse and irregular sampling. Here, we present a kinetically constrained
  hybrid Neural ordinary differential equation (KCH-NODE) framework for structure-to-PK
  prediction that bridges these limitations. KCH-NODE anchors predictions to a shared,
  learnable two-compartment typical trajectory while modeling compound-specific PK
  behavior as continuous-time deviations governed by a Neural ODE. This hybrid design
  generates flexible yet pharmacokinetically coherent trajectories, even under sparse
  observations. Trained on mouse intravenous (IV) and oral (PO) PK data from 1159
  compounds across 30 projects, KCH-NODE generally provided more accurate predictions
  than a purely data-driven Neural ODE in both compound-level and scaffold-based cross-validation
  (median RMSE 0.374 and 0.388 for IV; 0.564 and 0.570 for PO) and in a temporally
  held-out evaluation (223 compounds; median RMSE 0.637 for IV and 0.731 for PO),
  with a smaller loss of accuracy on the temporal split. Predictive accuracy for oral
  administration nevertheless remained limited on the temporal test set for both methods.
  Integrated Gradients supported mechanistically consistent feature contributions,
  and structural similarity to the model-development dataset together with ensemble
  disagreement provided complementary indicators of prediction reliability. These
  results indicate that kinetically constrained hybrid Neural ODEs offer an effective
  and interpretable framework for structure-to-PK profile prediction.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221552841
url: https://doi.org/10.1021/acs.molpharmaceut.6c00453
discovered_at: '2026-10-16'
tags: *id001
---

# Prediction of Plasma Concentration−Time Profiles in Mice from Chemical Structure Using a Kinetically Constrained Hybrid Neural ODE

**Autores:** Yuki Doi; Harutoshi Kato; Fumiyoshi Yamashita

**Data:** 2026-10-12 · **Tipo:** article

## Resumo

Abstract Predicting plasma concentration−time profiles directly from chemical structure remains intrinsically challenging in early drug discovery\. Existing approaches typically fall into two paradigms: mechanistic reconstruction via predicted PK parameters, which is constrained by the assumed model structure, and direct data\-driven prediction of concentrations, which often suffers from instability and poor temporal coherence under sparse and irregular sampling\. Here, we present a kinetically constrained hybrid Neural ordinary differential equation \(KCH\-NODE\) framework for structure\-to\-PK prediction that bridges these limitations\. KCH\-NODE anchors predictions to a shared, learnable two\-compartment typical trajectory while modeling compound\-specific PK behavior as continuous\-time deviations governed by a Neural ODE\. This hybrid design generates flexible yet pharmacokinetically coherent trajectories, even under sparse observations\. Trained on mouse intravenous \(IV\) and oral \(PO\) PK data from 1159 compounds across 30 projects, KCH\-NODE generally provided more accurate predictions than a purely data\-driven Neural ODE in both compound\-level and scaffold\-based cross\-validation \(median RMSE 0\.374 and 0\.388 for IV; 0\.564 and 0\.570 for PO\) and in a temporally held\-out evaluation \(223 compounds; median RMSE 0\.637 for IV and 0\.731 for PO\), with a smaller loss of accuracy on the temporal split\. Predictive accuracy for oral administration nevertheless remained limited on the temporal test set for both methods\. Integrated Gradients supported mechanistically consistent feature contributions, and structural similarity to the model\-development dataset together with ensemble disagreement provided complementary indicators of prediction reliability\. These results indicate that kinetically constrained hybrid Neural ODEs offer an effective and interpretable framework for structure\-to\-PK profile prediction\.

[Consultar publicação](<https://doi.org/10.1021/acs.molpharmaceut.6c00453>)
