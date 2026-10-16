---
title: 'FAMUS: A Few-Shot Learning Framework for Large-Scale Protein Annotation'
authors:
- Guy Shur
- David Burstein
date: '2026-10-12'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1093/bioinformatics/btag761
abstract: 'MOTIVATION: Gene function prediction is pivotal in genomic and metagenomic
  data analysis. Current annotation tools typically rely on the most similar sequence
  from the query database and struggle to robustly set meaningful hit thresholds,
  causing a major challenge for reliable annotation. RESULTS: Here, we present a contrastive
  learning framework for functional annotation. FAMUS (Functional Annotation Method
  Using Supervised contrastive learning) compares query sequences to a full array
  of profile Hidden Markov Models, encoding each sequence''s complete similarity profile,
  rather than only its top-scoring hit, into a condensed vector space that minimizes
  the distance between proteins from the same family. Unannotated sequences are incorporated
  as negative examples during training, enabling robust detection of proteins that
  fall outside the reference database without requiring user-defined thresholds. FAMUS
  outperformed KEGG''s native KofamScan for KEGG Orthology annotation and InterPro''s
  InterProScan for PANTHER family annotation, especially on realistic, sparsely annotated
  data. We used this approach to build four protein annotation models spanning the
  KEGG Orthology, InterPro, OrthoDB, and EggNOG databases. FAMUS is a comprehensive,
  modular framework that supports both pre-defined and user-specific databases. It
  can be readily integrated into genomic and metagenomic analysis pipelines for accurate,
  large-scale functional annotation. AVAILABILITY AND IMPLEMENTATION: All four models
  are available as a conda package and via our web server at https://app.famus.bursteinlab.org/,
  and source code is freely available on GitHub at https://github.com/burstein-lab/famus/
  as well as a source code snapshot at https://doi.org/10.5281/zenodo.23132542. SUPPLEMENTARY
  INFORMATION: Supplementary data are available at Bioinformatics online.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7134930174
url: https://doi.org/10.1093/bioinformatics/btag761
discovered_at: '2026-10-16'
tags: *id001
---

# FAMUS: A Few\-Shot Learning Framework for Large\-Scale Protein Annotation

**Autores:** Guy Shur; David Burstein

**Data:** 2026-10-12 · **Tipo:** article

## Resumo

MOTIVATION: Gene function prediction is pivotal in genomic and metagenomic data analysis\. Current annotation tools typically rely on the most similar sequence from the query database and struggle to robustly set meaningful hit thresholds, causing a major challenge for reliable annotation\. RESULTS: Here, we present a contrastive learning framework for functional annotation\. FAMUS \(Functional Annotation Method Using Supervised contrastive learning\) compares query sequences to a full array of profile Hidden Markov Models, encoding each sequence&\#x27;s complete similarity profile, rather than only its top\-scoring hit, into a condensed vector space that minimizes the distance between proteins from the same family\. Unannotated sequences are incorporated as negative examples during training, enabling robust detection of proteins that fall outside the reference database without requiring user\-defined thresholds\. FAMUS outperformed KEGG&\#x27;s native KofamScan for KEGG Orthology annotation and InterPro&\#x27;s InterProScan for PANTHER family annotation, especially on realistic, sparsely annotated data\. We used this approach to build four protein annotation models spanning the KEGG Orthology, InterPro, OrthoDB, and EggNOG databases\. FAMUS is a comprehensive, modular framework that supports both pre\-defined and user\-specific databases\. It can be readily integrated into genomic and metagenomic analysis pipelines for accurate, large\-scale functional annotation\. AVAILABILITY AND IMPLEMENTATION: All four models are available as a conda package and via our web server at https://app\.famus\.bursteinlab\.org/, and source code is freely available on GitHub at https://github\.com/burstein\-lab/famus/ as well as a source code snapshot at https://doi\.org/10\.5281/zenodo\.23132542\. SUPPLEMENTARY INFORMATION: Supplementary data are available at Bioinformatics online\.

[Consultar publicação](<https://doi.org/10.1093/bioinformatics/btag761>)
