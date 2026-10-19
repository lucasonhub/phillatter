---
title: 'An automated EEG–ECG framework for CAP–HRV analysis: enabling brain–heart
  coupling studies in sleep disorders'
authors:
- Shaween Shukir
- Mostafa Mohamed Moussa
- Yahya Alzaabi
- Ahsan Habib Khandoker
- Zbigniew R. Struzik
date: '2026-10-16'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3389/fphys.2026.1864664
abstract: Background Multimodal sleep analysis typically requires separate processing
  pipelines for electroencephalography (EEG) and electrocardiography (ECG), which
  complicates joint investigation of sleep microstructure and autonomic regulation.
  Cyclic alternating pattern (CAP) scoring and heart rate variability (HRV) analysis
  are routinely performed in different software environments, limiting temporal alignment,
  reproducibility, and scalability. Methods We present an open-source MATLAB framework
  that integrates rule-based CAP A1 detection and HRV feature extraction within a
  single, time-synchronized workflow. The pipeline performs standardized EEG and ECG
  preprocessing, rule-based CAP A1 detection during slow-wave sleep (SWS) implementing
  the Terzano scoring criteria, R-peak detection via the Pan–Tompkins algorithm, and
  computation of time-domain, frequency-domain, and nonlinear HRV features by calling
  the open-source PhysioZoo/mhrv toolbox directly. CAP annotations are aligned with
  5-minute ECG epochs through the shared polysomnography (PSG) time base. The complete
  code is released as an open-source repository to support reuse and extension. Results
  Because HRV features are computed by calling the PhysioZoo/mhrv toolbox directly,
  the pipeline introduces no reimplemented HRV routine and inherits that toolbox’s
  validated feature definitions. CAP A1 detection is provided as a rule-based implementation
  of published criteria and has not yet been benchmarked against expert manual scoring.
  A worked example on the OSAD+ subgroup (n = 18) demonstrates pipeline output across
  CAP and non-CAP epochs, and a healthy-sleep A1-event HRV reference is reported from
  the public CAP Sleep Database (15 controls, 785 A1 epochs) as a descriptive cross-database
  reference. Conclusion The framework provides a reproducible, rule-based, and modular
  tool for integrated EEG–ECG analysis of sleep microstructure and autonomic dynamics.
  By enabling synchronized CAP–HRV feature extraction in a single environment, it
  lowers the engineering barrier to brain–heart coupling research during sleep and
  provides a foundation for future extensions, including validated CAP detection,
  a matched-control study, a Python port, and cloud-based deployment.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222453541
url: https://doi.org/10.3389/fphys.2026.1864664
discovered_at: '2026-10-19'
tags: *id001
---

# An automated EEG–ECG framework for CAP–HRV analysis: enabling brain–heart coupling studies in sleep disorders

**Autores:** Shaween Shukir; Mostafa Mohamed Moussa; Yahya Alzaabi; Ahsan Habib Khandoker; Zbigniew R\. Struzik

**Data:** 2026-10-16 · **Tipo:** article

## Resumo

Background Multimodal sleep analysis typically requires separate processing pipelines for electroencephalography \(EEG\) and electrocardiography \(ECG\), which complicates joint investigation of sleep microstructure and autonomic regulation\. Cyclic alternating pattern \(CAP\) scoring and heart rate variability \(HRV\) analysis are routinely performed in different software environments, limiting temporal alignment, reproducibility, and scalability\. Methods We present an open\-source MATLAB framework that integrates rule\-based CAP A1 detection and HRV feature extraction within a single, time\-synchronized workflow\. The pipeline performs standardized EEG and ECG preprocessing, rule\-based CAP A1 detection during slow\-wave sleep \(SWS\) implementing the Terzano scoring criteria, R\-peak detection via the Pan–Tompkins algorithm, and computation of time\-domain, frequency\-domain, and nonlinear HRV features by calling the open\-source PhysioZoo/mhrv toolbox directly\. CAP annotations are aligned with 5\-minute ECG epochs through the shared polysomnography \(PSG\) time base\. The complete code is released as an open\-source repository to support reuse and extension\. Results Because HRV features are computed by calling the PhysioZoo/mhrv toolbox directly, the pipeline introduces no reimplemented HRV routine and inherits that toolbox’s validated feature definitions\. CAP A1 detection is provided as a rule\-based implementation of published criteria and has not yet been benchmarked against expert manual scoring\. A worked example on the OSAD\+ subgroup \(n = 18\) demonstrates pipeline output across CAP and non\-CAP epochs, and a healthy\-sleep A1\-event HRV reference is reported from the public CAP Sleep Database \(15 controls, 785 A1 epochs\) as a descriptive cross\-database reference\. Conclusion The framework provides a reproducible, rule\-based, and modular tool for integrated EEG–ECG analysis of sleep microstructure and autonomic dynamics\. By enabling synchronized CAP–HRV feature extraction in a single environment, it lowers the engineering barrier to brain–heart coupling research during sleep and provides a foundation for future extensions, including validated CAP detection, a matched\-control study, a Python port, and cloud\-based deployment\.

[Consultar publicação](<https://doi.org/10.3389/fphys.2026.1864664>)
