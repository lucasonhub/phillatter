---
title: Risk-Controlled DFT Selection for Machine-Learned Interatomic Potentials
authors:
- Kun Ryu
- Yeo Jin Jung
- Shyue Ping Ong
- Claire Donnat
- Ying Shirley Meng
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Automated materials discovery requires evaluating large pools of candidate
  configurations, with density functional theory (DFT) as a major throughput bottleneck.
  Pretrained machine-learned interatomic potentials (MLIPs) approximate DFT cheaply,
  but their errors vary by orders of magnitude across configurations, making it difficult
  to decide when to trust the MLIP predictions and when to fall back to DFT. We frame
  this decision as a risk-controlled selection problem and solve it within a conformal
  risk control (CRC) framework. Each configuration is mapped from atomic numbers and
  Cartesian coordinates to a fixed geometric descriptor, which a lightweight predictor
  uses to estimate an MLIP-DFT disagreement score in energy, average force, and maximum
  force. CRC then calibrates this score into a selection threshold for DFT labeling
  such that the MLIP error on the unselected configurations, which keep their MLIP
  labels, stays below a user-chosen fraction $α$ of the expected error. Under an identical
  guarantee across eight dataset-MLIP pairs, our predictor routes 7% and 14% fewer
  configurations to DFT at $α=0.3$ than committee baselines. Because committee disagreement
  overlooks errors the MLIPs share, our gains are largest when the DFT labels and
  MLIP training data differ in DFT functional and basis set, and narrow when the two
  agree. Without model access, the structure-only predictor also ranks errors as well
  as the target MLIP's latent representation and outperforms widely used descriptors
  such as Smooth Overlap of Atomic Positions (SOAP) and Atom-Centered Symmetry Functions
  (ACSF).
source:
- arXiv
source_ids:
- arxiv:2610.19630
url: https://arxiv.org/abs/2610.19630
discovered_at: '2026-10-16'
tags: *id001
---

# Risk\-Controlled DFT Selection for Machine\-Learned Interatomic Potentials

**Autores:** Kun Ryu; Yeo Jin Jung; Shyue Ping Ong; Claire Donnat; Ying Shirley Meng

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Automated materials discovery requires evaluating large pools of candidate configurations, with density functional theory \(DFT\) as a major throughput bottleneck\. Pretrained machine\-learned interatomic potentials \(MLIPs\) approximate DFT cheaply, but their errors vary by orders of magnitude across configurations, making it difficult to decide when to trust the MLIP predictions and when to fall back to DFT\. We frame this decision as a risk\-controlled selection problem and solve it within a conformal risk control \(CRC\) framework\. Each configuration is mapped from atomic numbers and Cartesian coordinates to a fixed geometric descriptor, which a lightweight predictor uses to estimate an MLIP\-DFT disagreement score in energy, average force, and maximum force\. CRC then calibrates this score into a selection threshold for DFT labeling such that the MLIP error on the unselected configurations, which keep their MLIP labels, stays below a user\-chosen fraction $α$ of the expected error\. Under an identical guarantee across eight dataset\-MLIP pairs, our predictor routes 7% and 14% fewer configurations to DFT at $α=0\.3$ than committee baselines\. Because committee disagreement overlooks errors the MLIPs share, our gains are largest when the DFT labels and MLIP training data differ in DFT functional and basis set, and narrow when the two agree\. Without model access, the structure\-only predictor also ranks errors as well as the target MLIP&\#x27;s latent representation and outperforms widely used descriptors such as Smooth Overlap of Atomic Positions \(SOAP\) and Atom\-Centered Symmetry Functions \(ACSF\)\.

[Consultar publicação](<https://arxiv.org/abs/2610.19630>)
