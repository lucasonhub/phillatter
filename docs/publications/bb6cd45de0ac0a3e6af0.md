---
title: 'SpecLLM: LLM-based VNIR spectral interpretation'
authors:
- Michał Romaszewski
- Anna Strzoda
- Marzena Halama
- Przemysław Głomb
- Piotr Masłowski
date: '2026-10-17'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1038/s41598-026-75562-5
abstract: Abstract Visible and near-infrared (VNIR) spectroscopy identifies materials
  from characteristic spectral bands, and spectroscopists interpret spectra by features
  such as peak positions and intensities. Recent machine-learning and foundation models
  for hyperspectral data are highly effective but return numerical outputs or latent
  representations rather than such feature-level descriptions. Meanwhile, LLM-based
  spectral approaches have mostly provided raw numerical sequences. We present a method
  for making spectroscopic data accessible to large language models (LLMs) through
  compact, feature-based representations. Instead of supplying full spectra as comma-separated
  values (CSV), JavaScript Object Notation (JSON), or extensible markup language (XML),
  the proposed approach extracts summary statistics and discriminative extrema. It
  serialises them as either natural language or structured JSON. We evaluate prototype-based
  substance classification in two complementary scenes from an open-access VNIR hyperspectral
  blood dataset. For the selected models, compact feature representations were substantially
  more effective than raw numerical encodings, but less effective than a Random Forest
  operating on raw spectra. The natural-language format provides a human-readable,
  inspectable serialisation of compact spectral evidence and reduces prompt length
  compared with full-spectrum encodings. We also compared natural language and JSON
  feature representations and found them broadly comparable.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222829999
url: https://doi.org/10.1038/s41598-026-75562-5
discovered_at: '2026-10-19'
tags: *id001
---

# SpecLLM: LLM\-based VNIR spectral interpretation

**Autores:** Michał Romaszewski; Anna Strzoda; Marzena Halama; Przemysław Głomb; Piotr Masłowski

**Data:** 2026-10-17 · **Tipo:** article

## Resumo

Abstract Visible and near\-infrared \(VNIR\) spectroscopy identifies materials from characteristic spectral bands, and spectroscopists interpret spectra by features such as peak positions and intensities\. Recent machine\-learning and foundation models for hyperspectral data are highly effective but return numerical outputs or latent representations rather than such feature\-level descriptions\. Meanwhile, LLM\-based spectral approaches have mostly provided raw numerical sequences\. We present a method for making spectroscopic data accessible to large language models \(LLMs\) through compact, feature\-based representations\. Instead of supplying full spectra as comma\-separated values \(CSV\), JavaScript Object Notation \(JSON\), or extensible markup language \(XML\), the proposed approach extracts summary statistics and discriminative extrema\. It serialises them as either natural language or structured JSON\. We evaluate prototype\-based substance classification in two complementary scenes from an open\-access VNIR hyperspectral blood dataset\. For the selected models, compact feature representations were substantially more effective than raw numerical encodings, but less effective than a Random Forest operating on raw spectra\. The natural\-language format provides a human\-readable, inspectable serialisation of compact spectral evidence and reduces prompt length compared with full\-spectrum encodings\. We also compared natural language and JSON feature representations and found them broadly comparable\.

[Consultar publicação](<https://doi.org/10.1038/s41598-026-75562-5>)
