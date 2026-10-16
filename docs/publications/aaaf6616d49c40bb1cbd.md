---
title: Efficient and scalable Python implementation of ANCOM-BC and ANCOM-BC2 for
  omics differential abundance testing
authors:
- Zijun Wu
- Huang Lin
- James T. Morton
- Qiyun Zhu
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1093/bioinformatics/btag767
abstract: 'SUMMARY: Analysis of Compositions of Microbiomes with Bias Correction (ANCOM-BC)
  and its successor ANCOM-BC2 are critical algorithms for differential abundance analysis.
  Designed for handling compositional data, they feature the ability to estimate the
  unknown sampling fractions and correct the bias induced by their differences. While
  the original R package implementing the two methods is robust for standard dataset
  sizes, the increasing magnitude of modern multi-omics studies presents computational
  challenges, often resulting in a runtime bottleneck for high-dimensional data. Here,
  we present native Python implementations of both ANCOM-BC and ANCOM-BC2 in the scikit-bio
  package, significantly accelerating the workflow and enabling their application
  to large-scale datasets. By leveraging vectorization with NumPy and numerical optimization
  in SciPy, we enhanced the efficiency of both methods without compromising their
  statistical accuracy. The benchmarking results revealed a dramatic increase in performance
  in both simulated and real datasets. We demonstrated that our Python implementations
  generated test results matching the original R code, while achieving 380- and 147-fold
  faster runtimes and 97.4% and 96.2% lower memory consumption on the largest tested
  dataset, respectively. The Python implementations allow for the analysis of datasets
  that are significantly larger than previously possible, and enable applications
  to alternative omics data types and complex statistical models that vary greatly
  by the number of samples, features, and covariates. AVAILABILITY AND IMPLEMENTATION:
  https://github.com/scikit-bio/scikit-bio. SUPPLEMENTARY INFORMATION: N/A.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221620843
url: https://doi.org/10.1093/bioinformatics/btag767
discovered_at: '2026-10-16'
tags: *id001
---

# Efficient and scalable Python implementation of ANCOM\-BC and ANCOM\-BC2 for omics differential abundance testing

**Autores:** Zijun Wu; Huang Lin; James T\. Morton; Qiyun Zhu

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

SUMMARY: Analysis of Compositions of Microbiomes with Bias Correction \(ANCOM\-BC\) and its successor ANCOM\-BC2 are critical algorithms for differential abundance analysis\. Designed for handling compositional data, they feature the ability to estimate the unknown sampling fractions and correct the bias induced by their differences\. While the original R package implementing the two methods is robust for standard dataset sizes, the increasing magnitude of modern multi\-omics studies presents computational challenges, often resulting in a runtime bottleneck for high\-dimensional data\. Here, we present native Python implementations of both ANCOM\-BC and ANCOM\-BC2 in the scikit\-bio package, significantly accelerating the workflow and enabling their application to large\-scale datasets\. By leveraging vectorization with NumPy and numerical optimization in SciPy, we enhanced the efficiency of both methods without compromising their statistical accuracy\. The benchmarking results revealed a dramatic increase in performance in both simulated and real datasets\. We demonstrated that our Python implementations generated test results matching the original R code, while achieving 380\- and 147\-fold faster runtimes and 97\.4% and 96\.2% lower memory consumption on the largest tested dataset, respectively\. The Python implementations allow for the analysis of datasets that are significantly larger than previously possible, and enable applications to alternative omics data types and complex statistical models that vary greatly by the number of samples, features, and covariates\. AVAILABILITY AND IMPLEMENTATION: https://github\.com/scikit\-bio/scikit\-bio\. SUPPLEMENTARY INFORMATION: N/A\.

[Consultar publicação](<https://doi.org/10.1093/bioinformatics/btag767>)
