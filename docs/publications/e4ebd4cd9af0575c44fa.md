---
title: 'Deep Defence on Wheels: A Dual Intrusion Detection System Architecture for
  Comprehensive In-Vehicle Network Security'
authors:
- Shashwat Khandelwal
- Shanker Shreejith
date: '2026-10-10'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1145/3858340
abstract: 'The combination of increasing connectivity to the outside world and the
  lack of inbuilt security mechanisms has made legacy intra-vehicular networks extremely
  vulnerable to cyberattacks. Consequently, significant research has been devoted
  to analysing the impact of potential attacks, yielding datasets crucial for developing
  effective mitigation schemes like intrusion detection and prevention systems (IDSs/IPSs).
  Initial research addressing this problem focused heavily on maximising attack detection
  accuracy (for both known and unknown attack vectors), often relying on large, full-precision
  machine learning models. However, embedding IDS into complex vehicular electronic
  systems adds challenges beyond accuracy, including the need for low detection latency
  (e.g., 2,000 CAN frames/sec), energy efficiency, and minimal overhead in electronic
  control unit (ECU) resources like silicon area, memory, and processor use. To address
  these deployment constraints, recent research has focused on lightweight machine
  learning models that balance high classification accuracy with these practical limitations.
  In this work, we propose a dual IDS framework comprising both supervised and unsupervised
  learning-based solutions, each optimised for real-time, resource-constrained deployment
  on embedded automotive platforms. We present a quantised LSTM-based IDS (QLSTM-IDS)
  that achieves over 99.9% detection accuracy across various attack types: DoS/Flooding,
  Fuzzing, and Spoofing/Malfunction, using a single model and two widely-used datasets.
  The model is trained using the brevitas quantisation aware training library, transformed
  into a dataflow accelerator with custom blocks compatible with AMD’s FINN toolchain,
  and synthesised using Vitis HLS. Complementing this, we introduce an 8-bit quantised
  convolutional autoencoder-based IDS (QCAE-IDS) for detecting previously unseen anomalies
  that alter CAN-ID sequence patterns, with >99% accuracy. QCAE-IDS is quantised using
  AMD’s Vitis-AI toolchain. We detail an integration architecture enabling both IDS
  models to operate on a single FPGA device, bridging the network interface IP and
  processor system to minimise software overhead. QLSTM-IDS achieves 0.25ms inference
  latency and 0.8mJ energy consumption, while QCAE-IDS achieves 0.42ms latency and
  1.1mJ energy, supporting real-time, efficient detection of both known and unknown
  attacks on high-speed CAN buses. Both solutions are deployed and evaluated on the
  ZCU104 SoC (XCZU7EV FPGA), demonstrating a robust, flexible hardware/software co-design
  for securing modern vehicular networks.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7220991844
url: https://doi.org/10.1145/3858340
discovered_at: '2026-10-16'
tags: *id001
---

# Deep Defence on Wheels: A Dual Intrusion Detection System Architecture for Comprehensive In\-Vehicle Network Security

**Autores:** Shashwat Khandelwal; Shanker Shreejith

**Data:** 2026-10-10 · **Tipo:** article

## Resumo

The combination of increasing connectivity to the outside world and the lack of inbuilt security mechanisms has made legacy intra\-vehicular networks extremely vulnerable to cyberattacks\. Consequently, significant research has been devoted to analysing the impact of potential attacks, yielding datasets crucial for developing effective mitigation schemes like intrusion detection and prevention systems \(IDSs/IPSs\)\. Initial research addressing this problem focused heavily on maximising attack detection accuracy \(for both known and unknown attack vectors\), often relying on large, full\-precision machine learning models\. However, embedding IDS into complex vehicular electronic systems adds challenges beyond accuracy, including the need for low detection latency \(e\.g\., 2,000 CAN frames/sec\), energy efficiency, and minimal overhead in electronic control unit \(ECU\) resources like silicon area, memory, and processor use\. To address these deployment constraints, recent research has focused on lightweight machine learning models that balance high classification accuracy with these practical limitations\. In this work, we propose a dual IDS framework comprising both supervised and unsupervised learning\-based solutions, each optimised for real\-time, resource\-constrained deployment on embedded automotive platforms\. We present a quantised LSTM\-based IDS \(QLSTM\-IDS\) that achieves over 99\.9% detection accuracy across various attack types: DoS/Flooding, Fuzzing, and Spoofing/Malfunction, using a single model and two widely\-used datasets\. The model is trained using the brevitas quantisation aware training library, transformed into a dataflow accelerator with custom blocks compatible with AMD’s FINN toolchain, and synthesised using Vitis HLS\. Complementing this, we introduce an 8\-bit quantised convolutional autoencoder\-based IDS \(QCAE\-IDS\) for detecting previously unseen anomalies that alter CAN\-ID sequence patterns, with &gt;99% accuracy\. QCAE\-IDS is quantised using AMD’s Vitis\-AI toolchain\. We detail an integration architecture enabling both IDS models to operate on a single FPGA device, bridging the network interface IP and processor system to minimise software overhead\. QLSTM\-IDS achieves 0\.25ms inference latency and 0\.8mJ energy consumption, while QCAE\-IDS achieves 0\.42ms latency and 1\.1mJ energy, supporting real\-time, efficient detection of both known and unknown attacks on high\-speed CAN buses\. Both solutions are deployed and evaluated on the ZCU104 SoC \(XCZU7EV FPGA\), demonstrating a robust, flexible hardware/software co\-design for securing modern vehicular networks\.

[Consultar publicação](<https://doi.org/10.1145/3858340>)
