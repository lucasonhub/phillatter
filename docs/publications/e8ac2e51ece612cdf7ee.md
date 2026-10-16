---
title: Adaptive neuro-fuzzy risk index for safe and interpretable lane-change decisions
  in Level-3 autonomous driving
authors:
- Quanda Zu
- Shaobo Cai
- 李建伟
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.3389/fnbot.2026.1918469
abstract: Introduction Highway lane-change maneuvers pose a safety challenge for SAE
  Level 3 autonomous driving because conventional threshold-based decisions and isolated
  surrogate safety measures may inadequately capture the coupling between longitudinal
  braking demand and evolving inter-vehicle gaps. This study develops an interpretable,
  risk-aware framework for continuous lane-change assessment during maneuver initiation
  and execution. Methods An adaptive neuro-fuzzy inference system (ANFIS) combines
  normalized longitudinal braking demand and minimum inter-vehicle gap to generate
  a continuous risk index ranging from zero to one. The index is integrated into a
  two-phase decision mechanism incorporating multi-vehicle threat assessment, region-dependent
  maneuver cancellation, quintic Bézier trajectory replanning, and driver takeover
  supervision. Performance was evaluated through high-fidelity SCANeR/ReScan and MATLAB/Simulink
  co-simulations against static Mamdani fuzzy, time-to-collision (TTC), deceleration-demand,
  and time-headway baselines. Robustness was assessed using 1,000 Monte Carlo simulations
  with variations in vehicle speeds, sensor noise, road friction, and cut-in timing.
  Results Compared with the TTC baseline, the proposed framework increased warning
  lead time from 0.86 to 1.84 s and minimum two-dimensional clearance from 2.08 to
  4.82 m, while reducing maximum deceleration demand from 4.92 to 2.34 m / s 2 . Mean
  computational execution time was 1.42 ms, below the 10-ms simulation control-cycle
  budget. Across the 1,000 randomized simulations, no collisions were observed with
  the proposed framework; near-miss and false-alarm rates were 0.30% and 1.20%, respectively.
  Discussion The simulation findings support the potential of continuous neuro-fuzzy
  risk assessment to provide earlier hazard detection and larger safety margins while
  retaining rule-based interpretability and low computational cost. Hardware-in-the-loop
  and real-vehicle testing remain necessary to establish performance beyond the evaluated
  simulation conditions.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221180123
url: https://doi.org/10.3389/fnbot.2026.1918469
discovered_at: '2026-10-16'
tags: *id001
---

# Adaptive neuro\-fuzzy risk index for safe and interpretable lane\-change decisions in Level\-3 autonomous driving

**Autores:** Quanda Zu; Shaobo Cai; 李建伟

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

Introduction Highway lane\-change maneuvers pose a safety challenge for SAE Level 3 autonomous driving because conventional threshold\-based decisions and isolated surrogate safety measures may inadequately capture the coupling between longitudinal braking demand and evolving inter\-vehicle gaps\. This study develops an interpretable, risk\-aware framework for continuous lane\-change assessment during maneuver initiation and execution\. Methods An adaptive neuro\-fuzzy inference system \(ANFIS\) combines normalized longitudinal braking demand and minimum inter\-vehicle gap to generate a continuous risk index ranging from zero to one\. The index is integrated into a two\-phase decision mechanism incorporating multi\-vehicle threat assessment, region\-dependent maneuver cancellation, quintic Bézier trajectory replanning, and driver takeover supervision\. Performance was evaluated through high\-fidelity SCANeR/ReScan and MATLAB/Simulink co\-simulations against static Mamdani fuzzy, time\-to\-collision \(TTC\), deceleration\-demand, and time\-headway baselines\. Robustness was assessed using 1,000 Monte Carlo simulations with variations in vehicle speeds, sensor noise, road friction, and cut\-in timing\. Results Compared with the TTC baseline, the proposed framework increased warning lead time from 0\.86 to 1\.84 s and minimum two\-dimensional clearance from 2\.08 to 4\.82 m, while reducing maximum deceleration demand from 4\.92 to 2\.34 m / s 2 \. Mean computational execution time was 1\.42 ms, below the 10\-ms simulation control\-cycle budget\. Across the 1,000 randomized simulations, no collisions were observed with the proposed framework; near\-miss and false\-alarm rates were 0\.30% and 1\.20%, respectively\. Discussion The simulation findings support the potential of continuous neuro\-fuzzy risk assessment to provide earlier hazard detection and larger safety margins while retaining rule\-based interpretability and low computational cost\. Hardware\-in\-the\-loop and real\-vehicle testing remain necessary to establish performance beyond the evaluated simulation conditions\.

[Consultar publicação](<https://doi.org/10.3389/fnbot.2026.1918469>)
