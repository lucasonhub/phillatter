---
title: A model for timing anomaly detection and prediction of CNC machine tools based
  on multi-scale feature fusion and self-attention
authors:
- Tengda Chen
date: '2026-10-14'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3389/fmech.2026.1967578
abstract: In order to solve the bottleneck problem of existing deep learning models
  being easily affected by feature interference and overfitting under strong noise,
  this paper proposes a Multi-scale Feature Fusion and Self-Attention based Time-Series
  Anomaly Detection and Prediction Network(MSFF-SATADPN). This paper first uses progressive
  dilated convolution to truncate local transient features in multiple frequency bands,
  and then dynamically maps global degradation dependencies through self attention
  mechanism. In addition, this paper applies orthogonal projection regularization
  of singular value decomposition to the hidden layer space, thereby decoupling steady-state
  principal components and anomalous disturbances at the physical representation level.
  Finally, independent blind testing across tools showed that within the range of
  structural mutations, compared to the Informer model exhibiting residual oscillations
  of −0.058–0.059 mm, the model predicted residual convergence to −0.015–0.018 mm.
  The global average absolute error of all test samples reached 0.062 mm, and the
  average absolute error distribution of each sample was 0.08 mm. The global average
  absolute error directly aggregated the absolute errors of all time steps, and each
  sample value averaged the absolute errors within each sample before sample aggregation.
  Both values were lower than the corresponding values of PatchTST in paired t-test
  (p < 0.01). In the abnormal classification under natural noise cutting conditions,
  the overall F1 score converged to 0.938 (± 0.008). This study overcomes the confusion
  of multi frequency features through a clear orthogonal decoupling mechanism, providing
  a reliable sequence analysis method for practical industrial operation and maintenance
  decisions.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221790290
url: https://doi.org/10.3389/fmech.2026.1967578
discovered_at: '2026-10-16'
tags: *id001
---

# A model for timing anomaly detection and prediction of CNC machine tools based on multi\-scale feature fusion and self\-attention

**Autores:** Tengda Chen

**Data:** 2026-10-14 · **Tipo:** article

## Resumo

In order to solve the bottleneck problem of existing deep learning models being easily affected by feature interference and overfitting under strong noise, this paper proposes a Multi\-scale Feature Fusion and Self\-Attention based Time\-Series Anomaly Detection and Prediction Network\(MSFF\-SATADPN\)\. This paper first uses progressive dilated convolution to truncate local transient features in multiple frequency bands, and then dynamically maps global degradation dependencies through self attention mechanism\. In addition, this paper applies orthogonal projection regularization of singular value decomposition to the hidden layer space, thereby decoupling steady\-state principal components and anomalous disturbances at the physical representation level\. Finally, independent blind testing across tools showed that within the range of structural mutations, compared to the Informer model exhibiting residual oscillations of −0\.058–0\.059 mm, the model predicted residual convergence to −0\.015–0\.018 mm\. The global average absolute error of all test samples reached 0\.062 mm, and the average absolute error distribution of each sample was 0\.08 mm\. The global average absolute error directly aggregated the absolute errors of all time steps, and each sample value averaged the absolute errors within each sample before sample aggregation\. Both values were lower than the corresponding values of PatchTST in paired t\-test \(p &lt; 0\.01\)\. In the abnormal classification under natural noise cutting conditions, the overall F1 score converged to 0\.938 \(± 0\.008\)\. This study overcomes the confusion of multi frequency features through a clear orthogonal decoupling mechanism, providing a reliable sequence analysis method for practical industrial operation and maintenance decisions\.

[Consultar publicação](<https://doi.org/10.3389/fmech.2026.1967578>)
