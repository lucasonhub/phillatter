---
title: Specification Gaming and a Constrained Reinforcement Learning Mitigation in
  a Cleaning Gridworld
authors:
- Hilda Adwubi Osei
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Reinforcement learning agents optimize exactly the reward signal they are
  given, which can diverge sharply from an intended true objective when that signal
  is only a proxy for it; this failure mode is known as specification gaming. Existing
  evidence for this failure mode is largely observational, with comparatively few
  demonstrations pairing a controlled, deliberately constructed proxy/true gap with
  a mitigation that carries a verifiable guarantee rather than only an empirical improvement.
  We construct a minimal gridworld in which a cleaning-robot agent can either genuinely
  remove dirt or conceal it from a cheap sensor, and show that a standard deep Q-network
  trained only on the sensor's proxy reward converges to a policy that games it completely,
  reaching near-maximal proxy reward while never achieving the true objective. We
  then introduce a constrained reinforcement learning fix, penalizing the specific
  behaviors through which the agent exploits the gap, and show that it eliminates
  the gaming behavior from the final policy while substantially recovering true-objective
  performance. We further derive and empirically verify an exact accounting identity
  relating the proxy reward, true reward, and our cost signal for this environment,
  showing that the cost signal measures the proxy/true gap exactly rather than merely
  tracking it, and yields a deterministic guarantee under a hard-constrained variant
  of the method.
source:
- arXiv
source_ids:
- arxiv:2610.22152
url: https://arxiv.org/abs/2610.22152
discovered_at: '2026-10-19'
tags: *id001
---

# Specification Gaming and a Constrained Reinforcement Learning Mitigation in a Cleaning Gridworld

**Autores:** Hilda Adwubi Osei

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Reinforcement learning agents optimize exactly the reward signal they are given, which can diverge sharply from an intended true objective when that signal is only a proxy for it; this failure mode is known as specification gaming\. Existing evidence for this failure mode is largely observational, with comparatively few demonstrations pairing a controlled, deliberately constructed proxy/true gap with a mitigation that carries a verifiable guarantee rather than only an empirical improvement\. We construct a minimal gridworld in which a cleaning\-robot agent can either genuinely remove dirt or conceal it from a cheap sensor, and show that a standard deep Q\-network trained only on the sensor&\#x27;s proxy reward converges to a policy that games it completely, reaching near\-maximal proxy reward while never achieving the true objective\. We then introduce a constrained reinforcement learning fix, penalizing the specific behaviors through which the agent exploits the gap, and show that it eliminates the gaming behavior from the final policy while substantially recovering true\-objective performance\. We further derive and empirically verify an exact accounting identity relating the proxy reward, true reward, and our cost signal for this environment, showing that the cost signal measures the proxy/true gap exactly rather than merely tracking it, and yields a deterministic guarantee under a hard\-constrained variant of the method\.

[Consultar publicação](<https://arxiv.org/abs/2610.22152>)
