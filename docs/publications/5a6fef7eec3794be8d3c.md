---
title: 'Returning to Development States: When Full Sandbox Snapshots Help Coding Agents'
authors:
- Daniel Thi Graviet
- Tanmay Shah
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Coding agents often make useful progress before they fail, but retry-from-scratch
  discards the machine state created along the way. This makes failure recovery an
  interesting search problem: if intermediate environment states preserve meaningful
  progress, restoring and branching from them could outperform repeatedly restarting
  from the initial state. We implement Go-Explore-style search over full Daytona snapshots
  and find that higher and more efficient solve rates depend mainly on progress that
  sits outside the repository, such as databases, services, and other runtime state.
  Our results suggest that full-snapshot search is most effective when long-horizon
  coding work spans multiple services whose state cannot be reconstructed from a single
  diff.'
source:
- arXiv
source_ids:
- arxiv:2610.13841
url: https://arxiv.org/abs/2610.13841
discovered_at: '2026-10-16'
tags: *id001
---

# Returning to Development States: When Full Sandbox Snapshots Help Coding Agents

**Autores:** Daniel Thi Graviet; Tanmay Shah

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Coding agents often make useful progress before they fail, but retry\-from\-scratch discards the machine state created along the way\. This makes failure recovery an interesting search problem: if intermediate environment states preserve meaningful progress, restoring and branching from them could outperform repeatedly restarting from the initial state\. We implement Go\-Explore\-style search over full Daytona snapshots and find that higher and more efficient solve rates depend mainly on progress that sits outside the repository, such as databases, services, and other runtime state\. Our results suggest that full\-snapshot search is most effective when long\-horizon coding work spans multiple services whose state cannot be reconstructed from a single diff\.

[Consultar publicação](<https://arxiv.org/abs/2610.13841>)
