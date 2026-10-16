---
title: 'RASSG: Repair-Aware Semantic Survival Gating for Streaming Tool Execution'
authors:
- Daijin Hu
- Xi Wang
date: '2026-10-10'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Streaming speech assistants can launch tools before users finish speaking,
  overlapping execution with incoming speech to reduce user waiting time. However,
  subsequent self-corrections can invalidate apparently stable arguments, causing
  stale execution whose irreversible effects persist even after the final call is
  corrected. We propose Repair-Aware Semantic Survival Gating (RASSG) to jointly control
  tool launch and cancellation during streaming speech. RASSG launches a tool when
  three consecutive speech recognition results arrive with identical nonempty arguments,
  then combines calibrated argument invalidity risk with execution costs to decide
  cancellation at the last feasible opportunity before effects become irreversible.
  Evaluation on ReCAST, FDB-v3, and Audio2Tool uses a controlled execution clock with
  fixed tool runtimes and cancellation parameters. On ReCAST's prospective-repair
  subset, RASSG reduces the stale execution rate from LocalAgreement-2's 50.00% to
  3.15%, with a mean delay of 3.676s across successful trajectories. The stale reduction
  also holds against every early-execution baseline on both public speech datasets.
  Ablations with identical initial launches support active cancellation, showing the
  value of controlling ongoing calls before their effects become irreversible. Code
  and data are available at https://github.com/daijinhu/RASSG.
source:
- arXiv
source_ids:
- arxiv:2610.14659
url: https://arxiv.org/abs/2610.14659
discovered_at: '2026-10-16'
tags: *id001
---

# RASSG: Repair\-Aware Semantic Survival Gating for Streaming Tool Execution

**Autores:** Daijin Hu; Xi Wang

**Data:** 2026-10-10 · **Tipo:** preprint

## Resumo

Streaming speech assistants can launch tools before users finish speaking, overlapping execution with incoming speech to reduce user waiting time\. However, subsequent self\-corrections can invalidate apparently stable arguments, causing stale execution whose irreversible effects persist even after the final call is corrected\. We propose Repair\-Aware Semantic Survival Gating \(RASSG\) to jointly control tool launch and cancellation during streaming speech\. RASSG launches a tool when three consecutive speech recognition results arrive with identical nonempty arguments, then combines calibrated argument invalidity risk with execution costs to decide cancellation at the last feasible opportunity before effects become irreversible\. Evaluation on ReCAST, FDB\-v3, and Audio2Tool uses a controlled execution clock with fixed tool runtimes and cancellation parameters\. On ReCAST&\#x27;s prospective\-repair subset, RASSG reduces the stale execution rate from LocalAgreement\-2&\#x27;s 50\.00% to 3\.15%, with a mean delay of 3\.676s across successful trajectories\. The stale reduction also holds against every early\-execution baseline on both public speech datasets\. Ablations with identical initial launches support active cancellation, showing the value of controlling ongoing calls before their effects become irreversible\. Code and data are available at https://github\.com/daijinhu/RASSG\.

[Consultar publicação](<https://arxiv.org/abs/2610.14659>)
