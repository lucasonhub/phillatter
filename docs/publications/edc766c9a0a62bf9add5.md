---
title: Robust Multi-Turn-Rate IMM-EKF Algorithm for Maneuvering Target Tracking under
  Model Mismatch and Measurement Faults
authors:
- Trinh Thi Minh
- Vu Quang Luong
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.24090/tids.v3i2.16951
abstract: Reliable maneuvering-target tracking is difficult when the motion-model
  bank is incomplete and range-bearing measurements contain dropout, bias, burst noise,
  or impulsive outliers. This study proposes a robust multi-turn-rate interacting
  multiple-model extended Kalman filter (RMT-IMM-EKF) that combines six motion hypotheses
  with statistically normalized componentwise innovation clipping. Multi-turn-rate
  denotes multiple coordinated-turn hypotheses, not different sampling rates; all
  estimators use s. The model bank includes constant velocity, coordinated turns at
  and deg/s, and a high-process-noise escape mode. The bounded innovation is used
  in both state correction and model likelihood. A 120-s programmed trajectory containing
  straight motion, in-grid/off-grid turns, acceleration, and an S-turn is evaluated
  in 30 paired Monte Carlo runs with identical truth, measurements, faults, and random
  seeds across estimators. RMT-IMM-EKF achieves a position RMSE of m and a velocity
  RMSE of m/s. Relative to AIMM-EKF, these errors decrease by 18.64% and 11.25%, respectively,
  while the proposed estimator wins all paired runs on both metrics; one-sided Wilcoxon
  tests yield . Condition-wise analysis shows clear gains in nominal, dropout, and
  impulsive-outlier samples but no uniform advantage during sustained noise bursts
  or persistent bias. The results support complementary benefits of broader maneuver
  coverage and bounded residual influence within the tested benchmark, while persistent
  bias and sustained changes in variance remain limitations.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7220971163
url: https://doi.org/10.24090/tids.v3i2.16951
discovered_at: '2026-10-16'
tags: *id001
---

# Robust Multi\-Turn\-Rate IMM\-EKF Algorithm for Maneuvering Target Tracking under Model Mismatch and Measurement Faults

**Autores:** Trinh Thi Minh; Vu Quang Luong

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

Reliable maneuvering\-target tracking is difficult when the motion\-model bank is incomplete and range\-bearing measurements contain dropout, bias, burst noise, or impulsive outliers\. This study proposes a robust multi\-turn\-rate interacting multiple\-model extended Kalman filter \(RMT\-IMM\-EKF\) that combines six motion hypotheses with statistically normalized componentwise innovation clipping\. Multi\-turn\-rate denotes multiple coordinated\-turn hypotheses, not different sampling rates; all estimators use s\. The model bank includes constant velocity, coordinated turns at and deg/s, and a high\-process\-noise escape mode\. The bounded innovation is used in both state correction and model likelihood\. A 120\-s programmed trajectory containing straight motion, in\-grid/off\-grid turns, acceleration, and an S\-turn is evaluated in 30 paired Monte Carlo runs with identical truth, measurements, faults, and random seeds across estimators\. RMT\-IMM\-EKF achieves a position RMSE of m and a velocity RMSE of m/s\. Relative to AIMM\-EKF, these errors decrease by 18\.64% and 11\.25%, respectively, while the proposed estimator wins all paired runs on both metrics; one\-sided Wilcoxon tests yield \. Condition\-wise analysis shows clear gains in nominal, dropout, and impulsive\-outlier samples but no uniform advantage during sustained noise bursts or persistent bias\. The results support complementary benefits of broader maneuver coverage and bounded residual influence within the tested benchmark, while persistent bias and sustained changes in variance remain limitations\.

[Consultar publicação](<https://doi.org/10.24090/tids.v3i2.16951>)
