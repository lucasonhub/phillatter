---
title: 'ScopeNovo: a De Novo Peptide Sequencing Method Using Spectrum-Spectrum Similarity
  to Refine the Prediction Accuracy'
authors:
- Zhi Song
- Zejian Ding
- Lusheng Wang
date: '2026-10-15'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1093/bioinformatics/btag755
abstract: 'MOTIVATION: De novo peptide sequencing from tandem mass spectra is essential
  for characterizing unknown proteins, identifying novel post-translational modifications,
  and analyzing samples without reference databases. While recent deep learning models
  have improved the predicted peptide accuracy, they typically select the predicted
  peptide sequence based solely on sequence-level decoding scores. Very often, high
  scores are assigned to peptides without the direct support from the observed mass
  spectrum. RESULTS: We present ScopeNovo, a de novo peptide sequencing method that
  improves predicted peptide accuracy by using spectrum-spectrum similarity between
  the input spectrum and the "representative" spectrum corresponding to the predicted
  peptide sequence. ScopeNovo generates multiple candidate peptides using an existing
  peptide de novo sequencing learning model and reranks candidates based on spectrum-spectrum
  similarity. To test our method, we use π-PrimeNovo as the base learning model. Experimental
  results on the standard nine-species benchmark datasets V1 and V2 show that ScopeNovo
  can substantially improve the prediction accuracy. We designed two settings, where
  Setting 1 is for well-annotated species, and Setting 2 is for species that are not
  well annotated. For Setting 1, ScopeNovo improves the average peptide accuracies
  of π-PrimeNovo over the nine species by 6.1% and 4.0% on V1 and V2, respectively.
  For Setting 2, ScopeNovo can still improve the peptide accuracy of π-PrimeNovo over
  the nine species by 3.4% and 1.9% on the V1 and V2 benchmark datasets, respectively.
  Compared to the best known method, RankNovo, the peptide accuracies over the nine
  species on V1 and V2 of our method for Setting 1 are 0.711 and 0.737, where the
  peptide accuracies for RankNovo are 0.687 and 0.682. Even for Setting 2, the peptide
  accuracies of our method are comparable to those of RankNovo. AVAILABILITY: ScopeNovo
  is implemented in Python under an MIT license. The source code is freely available
  at https://github.com/SoSongzhi/ScopeNovo.git. The test data are available at https://doi.org/10.5281/zenodo.23181841.
  SUPPLEMENTARY INFORMATION: Supplementary data are available at Bioinformatics online.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7220676429
url: https://doi.org/10.1093/bioinformatics/btag755
discovered_at: '2026-10-19'
tags: *id001
---

# ScopeNovo: a De Novo Peptide Sequencing Method Using Spectrum\-Spectrum Similarity to Refine the Prediction Accuracy

**Autores:** Zhi Song; Zejian Ding; Lusheng Wang

**Data:** 2026-10-15 · **Tipo:** article

## Resumo

MOTIVATION: De novo peptide sequencing from tandem mass spectra is essential for characterizing unknown proteins, identifying novel post\-translational modifications, and analyzing samples without reference databases\. While recent deep learning models have improved the predicted peptide accuracy, they typically select the predicted peptide sequence based solely on sequence\-level decoding scores\. Very often, high scores are assigned to peptides without the direct support from the observed mass spectrum\. RESULTS: We present ScopeNovo, a de novo peptide sequencing method that improves predicted peptide accuracy by using spectrum\-spectrum similarity between the input spectrum and the &quot;representative&quot; spectrum corresponding to the predicted peptide sequence\. ScopeNovo generates multiple candidate peptides using an existing peptide de novo sequencing learning model and reranks candidates based on spectrum\-spectrum similarity\. To test our method, we use π\-PrimeNovo as the base learning model\. Experimental results on the standard nine\-species benchmark datasets V1 and V2 show that ScopeNovo can substantially improve the prediction accuracy\. We designed two settings, where Setting 1 is for well\-annotated species, and Setting 2 is for species that are not well annotated\. For Setting 1, ScopeNovo improves the average peptide accuracies of π\-PrimeNovo over the nine species by 6\.1% and 4\.0% on V1 and V2, respectively\. For Setting 2, ScopeNovo can still improve the peptide accuracy of π\-PrimeNovo over the nine species by 3\.4% and 1\.9% on the V1 and V2 benchmark datasets, respectively\. Compared to the best known method, RankNovo, the peptide accuracies over the nine species on V1 and V2 of our method for Setting 1 are 0\.711 and 0\.737, where the peptide accuracies for RankNovo are 0\.687 and 0\.682\. Even for Setting 2, the peptide accuracies of our method are comparable to those of RankNovo\. AVAILABILITY: ScopeNovo is implemented in Python under an MIT license\. The source code is freely available at https://github\.com/SoSongzhi/ScopeNovo\.git\. The test data are available at https://doi\.org/10\.5281/zenodo\.23181841\. SUPPLEMENTARY INFORMATION: Supplementary data are available at Bioinformatics online\.

[Consultar publicação](<https://doi.org/10.1093/bioinformatics/btag755>)
