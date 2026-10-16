---
title: Smooth total variation regularization for interference detection and elimination
  (STRIDE) for MRI
authors:
- Alexander Mertens
- Diego Martinez
- Amgad Louka
- Ying Yang
- Chad Harris
- Ian R. O. Connell
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1088/1361-6560/aeb29e
abstract: 'OBJECTIVE: MRI is increasingly required to operate near electronic devices
  that emit dynamic electromagnetic interference (EMI). Existing reference-channel
  EMI removal methods estimate a transfer function between EMI sensors and imaging
  coils from the measured data alone, and do not use prior knowledge about the structure
  of MR images. We develop and validate an EMI removal method that uses the inherent
  spatial smoothness of MR images as an additional prior, demonstrated on a head-only
  0.5T scanner. APPROACH: Smooth Total variation Regularization for Interference Detection
  and Elimination (STRIDE) operates in the image domain. For each image column, EMI
  sensor data are combined and subtracted from the imaging coil data such that the
  L2 norm of the total variation (TV) along the readout direction is minimized. This
  exploits the smoothness of MR images, a property well-known in compressed sensing
  but not previously used in EMI removal. STRIDE was evaluated on phantom and in-vivo
  brain datasets under EMI scenarios replicating sources encountered at our affiliated
  hospitals, and compared against two implementations of External Dynamic Interference
  Estimation and Removal (EDITER). MAIN RESULTS: STRIDE produced visually better EMI
  removal, higher temporal signal-to-noise ratio, and larger EMI removal percentage
  than both EDITER implementations. STRIDE also resulted in lower or equal root-mean-square
  error than both EDITER implementations in all 8 phantom EMI conditions tested. These
  results held across both phantom and in-vivo datasets. SIGNIFICANCE: STRIDE shows
  that incorporating known properties of MR images into the EMI removal problem provides
  meaningful improvements over methods that rely on measured data alone. The approach
  is deterministic, training-free, sequence-independent, and compatible with existing
  EMI sensor hardware. STRIDE therefore extends reference-channel EMI removal to scenarios
  where existing methods fail, particularly point-of-care and interventional MRI outside
  fully shielded environments, providing a complementary path to machine-learning
  approaches.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7106061667
url: https://doi.org/10.1088/1361-6560/aeb29e
discovered_at: '2026-10-16'
tags: *id001
---

# Smooth total variation regularization for interference detection and elimination \(STRIDE\) for MRI

**Autores:** Alexander Mertens; Diego Martinez; Amgad Louka; Ying Yang; Chad Harris; Ian R\. O\. Connell

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

OBJECTIVE: MRI is increasingly required to operate near electronic devices that emit dynamic electromagnetic interference \(EMI\)\. Existing reference\-channel EMI removal methods estimate a transfer function between EMI sensors and imaging coils from the measured data alone, and do not use prior knowledge about the structure of MR images\. We develop and validate an EMI removal method that uses the inherent spatial smoothness of MR images as an additional prior, demonstrated on a head\-only 0\.5T scanner\. APPROACH: Smooth Total variation Regularization for Interference Detection and Elimination \(STRIDE\) operates in the image domain\. For each image column, EMI sensor data are combined and subtracted from the imaging coil data such that the L2 norm of the total variation \(TV\) along the readout direction is minimized\. This exploits the smoothness of MR images, a property well\-known in compressed sensing but not previously used in EMI removal\. STRIDE was evaluated on phantom and in\-vivo brain datasets under EMI scenarios replicating sources encountered at our affiliated hospitals, and compared against two implementations of External Dynamic Interference Estimation and Removal \(EDITER\)\. MAIN RESULTS: STRIDE produced visually better EMI removal, higher temporal signal\-to\-noise ratio, and larger EMI removal percentage than both EDITER implementations\. STRIDE also resulted in lower or equal root\-mean\-square error than both EDITER implementations in all 8 phantom EMI conditions tested\. These results held across both phantom and in\-vivo datasets\. SIGNIFICANCE: STRIDE shows that incorporating known properties of MR images into the EMI removal problem provides meaningful improvements over methods that rely on measured data alone\. The approach is deterministic, training\-free, sequence\-independent, and compatible with existing EMI sensor hardware\. STRIDE therefore extends reference\-channel EMI removal to scenarios where existing methods fail, particularly point\-of\-care and interventional MRI outside fully shielded environments, providing a complementary path to machine\-learning approaches\.

[Consultar publicação](<https://doi.org/10.1088/1361-6560/aeb29e>)
