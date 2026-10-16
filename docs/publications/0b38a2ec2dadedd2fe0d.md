---
title: 'Kairos: Transactional Security Enforcement at the System Boundary for LLM
  Agents'
authors:
- Kristoffer Hempel
- Nils Loose
- Lorenzo Cavallaro
- Thomas Eisenbarth
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Large language model (LLM) agents are becoming an integral part of the software
  development lifecycle, and the capabilities granted to them allow an agent to act
  with the user's authority on any resource it can access. The reach that gives an
  agent its utility is equally available to an attacker who can steer it. Anything
  an agent ingests can carry an injected instruction, and since the model does not
  reliably distinguish instructions from data, indirect prompt injection should be
  mitigated by mediating the effects the agent produces. Such mediation faces a structural
  difficulty. Legitimate work and the first step of an attack often look alike when
  an individual action is observed, and what separates them lies later in the trace,
  so a monitor limited to allow and deny is forced to decide before the evidence accumulates.
  We present Kairos, a reference monitor at the isolation boundary of an unmodified,
  opaque agent, where a tool call, a shell command, and a script the agent writes
  all cross the boundary as the same file and network operations, so that confinement
  holds regardless of the agent's behavior. A declarative policy that states which
  sources are trusted decides most effects deterministically and defers the rest,
  which are held while the agent continues speculatively. A decision oracle with bounded
  authority, such as a language model or a human, releases or refuses each deferred
  effect on the trace. Across three benchmarks and three agent models, Kairos outperforms
  existing defenses in the trade-off between attack success and utility. In particular,
  on AgentDojo, it reduces attack success from 47.0\% to 2.7\% while its benign utility
  stays at the level of the undefended agent.
source:
- arXiv
source_ids:
- arxiv:2610.18457
url: https://arxiv.org/abs/2610.18457
discovered_at: '2026-10-16'
tags: *id001
---

# Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents

**Autores:** Kristoffer Hempel; Nils Loose; Lorenzo Cavallaro; Thomas Eisenbarth

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Large language model \(LLM\) agents are becoming an integral part of the software development lifecycle, and the capabilities granted to them allow an agent to act with the user&\#x27;s authority on any resource it can access\. The reach that gives an agent its utility is equally available to an attacker who can steer it\. Anything an agent ingests can carry an injected instruction, and since the model does not reliably distinguish instructions from data, indirect prompt injection should be mitigated by mediating the effects the agent produces\. Such mediation faces a structural difficulty\. Legitimate work and the first step of an attack often look alike when an individual action is observed, and what separates them lies later in the trace, so a monitor limited to allow and deny is forced to decide before the evidence accumulates\. We present Kairos, a reference monitor at the isolation boundary of an unmodified, opaque agent, where a tool call, a shell command, and a script the agent writes all cross the boundary as the same file and network operations, so that confinement holds regardless of the agent&\#x27;s behavior\. A declarative policy that states which sources are trusted decides most effects deterministically and defers the rest, which are held while the agent continues speculatively\. A decision oracle with bounded authority, such as a language model or a human, releases or refuses each deferred effect on the trace\. Across three benchmarks and three agent models, Kairos outperforms existing defenses in the trade\-off between attack success and utility\. In particular, on AgentDojo, it reduces attack success from 47\.0\\% to 2\.7\\% while its benign utility stays at the level of the undefended agent\.

[Consultar publicação](<https://arxiv.org/abs/2610.18457>)
