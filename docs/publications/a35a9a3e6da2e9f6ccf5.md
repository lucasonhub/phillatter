---
title: Hardware-Assisted Intrusion Detection System for Automotive Embedded ECUs
authors:
- Vishnupriya.T
- Sumit Ramswami Punam
date: '2026-10-11'
type: article
category: &id001
- Inteligência Artificial
doi: 10.31838/esa/03.02.04
abstract: Modern automotive systems progressively rely on Electronic Control Units
  (ECUs) to take control of vital vehicle functionality and are heavily interlinked
  on in-vehicle networks, e.g. the Controller Area Network (CAN). With the increased
  vehicle sophistication into a complex cyber-physical system, the car is more exposed
  to cyber-related attacks such as message injection, spoofing, and denial-of-service
  (DoS) attacks that have the potential to affect safety and performance. Implementations
  of Intrusion Detection Systems (IDS) using software, can be not very effective when
  it comes to real-time detection, because of the computational overhead imposed by
  them and the shared CPU usage. The paper proposes a new hardware-assisted intrusion
  detection system (H-IDS) designed to work on the automotive platforms and embedded
  devices (ECUs) in particular but is focused on the low-latency and real-time nature
  of the system and its capability to deploy on resource-constrained devices. The
  described architecture uses a light on-chip co-processor in the ECU as a special
  security engine to observe CAN traffic and observe abnormal behavior based on temporal
  and statistical characteristics. The H-IDS performs detection tasks on a separate
  processor-offloading payload so it does not interfere with other processes or even
  stop when the vehicle does not perform its tasks. This was implemented on an ECU
  platform based on the ARM Cortex-R5 in a hardware prototyping system with FPGA and
  then tested in a range of simulated attack conditions. The input of the experiment
  shows that there is a significant reduction in the detection latency that the H-IDS
  displays an average latency of 14 microseconds that is much faster than software-only
  solutions. Also, the design has less than 2 percent CPU overhead and its power and
  memory requirements fit squarely within the power and memory budget of most automotive
  embedded systems. The provided proposed H-IDS is aligned with ISO/SAE 21434 standards
  of cybersecurity, and it is scalable to be deployed on various heterogeneous ECU
  systems. Through the increased detection responsiveness and negligible resource
  consumption, the work is a step towards realistic hardware-enforced security measures,
  which can be incorporated in the next generation of automotive architectures to
  guarantee resilient and trustful in-vehicle networks.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7219739918
url: https://doi.org/10.31838/esa/03.02.04
discovered_at: '2026-10-16'
tags: *id001
---

# Hardware\-Assisted Intrusion Detection System for Automotive Embedded ECUs

**Autores:** Vishnupriya\.T; Sumit Ramswami Punam

**Data:** 2026-10-11 · **Tipo:** article

## Resumo

Modern automotive systems progressively rely on Electronic Control Units \(ECUs\) to take control of vital vehicle functionality and are heavily interlinked on in\-vehicle networks, e\.g\. the Controller Area Network \(CAN\)\. With the increased vehicle sophistication into a complex cyber\-physical system, the car is more exposed to cyber\-related attacks such as message injection, spoofing, and denial\-of\-service \(DoS\) attacks that have the potential to affect safety and performance\. Implementations of Intrusion Detection Systems \(IDS\) using software, can be not very effective when it comes to real\-time detection, because of the computational overhead imposed by them and the shared CPU usage\. The paper proposes a new hardware\-assisted intrusion detection system \(H\-IDS\) designed to work on the automotive platforms and embedded devices \(ECUs\) in particular but is focused on the low\-latency and real\-time nature of the system and its capability to deploy on resource\-constrained devices\. The described architecture uses a light on\-chip co\-processor in the ECU as a special security engine to observe CAN traffic and observe abnormal behavior based on temporal and statistical characteristics\. The H\-IDS performs detection tasks on a separate processor\-offloading payload so it does not interfere with other processes or even stop when the vehicle does not perform its tasks\. This was implemented on an ECU platform based on the ARM Cortex\-R5 in a hardware prototyping system with FPGA and then tested in a range of simulated attack conditions\. The input of the experiment shows that there is a significant reduction in the detection latency that the H\-IDS displays an average latency of 14 microseconds that is much faster than software\-only solutions\. Also, the design has less than 2 percent CPU overhead and its power and memory requirements fit squarely within the power and memory budget of most automotive embedded systems\. The provided proposed H\-IDS is aligned with ISO/SAE 21434 standards of cybersecurity, and it is scalable to be deployed on various heterogeneous ECU systems\. Through the increased detection responsiveness and negligible resource consumption, the work is a step towards realistic hardware\-enforced security measures, which can be incorporated in the next generation of automotive architectures to guarantee resilient and trustful in\-vehicle networks\.

[Consultar publicação](<https://doi.org/10.31838/esa/03.02.04>)
