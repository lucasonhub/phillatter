---
title: 'FUSE: Fairness-aware Update Screening against Byzantine Exploitation in $q$-Fair
  Federated Learning'
authors:
- Tiantong Sun
- Jinlin Liu
- Xingru Wei
- Zequan Fang
- Wei Chen
- Qiang Yang
- Xiaojin Zhang
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Client-level fair federated learning, in the form of $q$-fair federated
  learning ($q$-FFL), agnostic federated learning, or tilted empirical risk minimization,
  has emerged as an attractive solution to equalize utility across heterogeneous clients.
  This paradigm grants high-loss clients greater relative influence, while a central
  server aggregates their loss-weighted updates into a single shared model. Yet, the
  Byzantine robustness of $q$-fair federated learning has been largely neglected,
  leaving the server unable to tell legitimate fairness-induced amplification from
  malicious update scaling. To address this critical gap, we formalize the problem
  of Byzantine-robust $q$-fair federated learning under an \emph{update-only interface},
  in which the server observes nothing but the fairness-scaled client updates. Our
  analysis under shared class-conditional label skew shows that fairness scaling preserves
  the nonnegative class-mixture structure of honest updates, while replacing their
  unit-sum constraint by a client-dependent radial scale. Moving beyond magnitude-based
  screening, we show that this warped geometry supplies two complementary tests, one
  radial and one structural, that a single norm cannot provide. We then introduce
  FUSE, a structure-aware robust aggregator that uses a small trusted labeled dataset
  for coefficient recovery, scale and cone-consistency screening, and post-screening
  step-size control. Across four benchmarks and seven Byzantine attacks, FUSE improves
  seed-wise worst-attack accuracy over the strongest baseline on each benchmark by
  3.9--30.1 percentage points, while largely preserving the influence of the high-loss
  honest clients that fairness is meant to protect.
source:
- arXiv
source_ids:
- arxiv:2610.20264
url: https://arxiv.org/abs/2610.20264
discovered_at: '2026-10-16'
tags: *id001
---

# FUSE: Fairness\-aware Update Screening against Byzantine Exploitation in $q$\-Fair Federated Learning

**Autores:** Tiantong Sun; Jinlin Liu; Xingru Wei; Zequan Fang; Wei Chen; Qiang Yang; Xiaojin Zhang

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Client\-level fair federated learning, in the form of $q$\-fair federated learning \($q$\-FFL\), agnostic federated learning, or tilted empirical risk minimization, has emerged as an attractive solution to equalize utility across heterogeneous clients\. This paradigm grants high\-loss clients greater relative influence, while a central server aggregates their loss\-weighted updates into a single shared model\. Yet, the Byzantine robustness of $q$\-fair federated learning has been largely neglected, leaving the server unable to tell legitimate fairness\-induced amplification from malicious update scaling\. To address this critical gap, we formalize the problem of Byzantine\-robust $q$\-fair federated learning under an \\emph\{update\-only interface\}, in which the server observes nothing but the fairness\-scaled client updates\. Our analysis under shared class\-conditional label skew shows that fairness scaling preserves the nonnegative class\-mixture structure of honest updates, while replacing their unit\-sum constraint by a client\-dependent radial scale\. Moving beyond magnitude\-based screening, we show that this warped geometry supplies two complementary tests, one radial and one structural, that a single norm cannot provide\. We then introduce FUSE, a structure\-aware robust aggregator that uses a small trusted labeled dataset for coefficient recovery, scale and cone\-consistency screening, and post\-screening step\-size control\. Across four benchmarks and seven Byzantine attacks, FUSE improves seed\-wise worst\-attack accuracy over the strongest baseline on each benchmark by 3\.9\-\-30\.1 percentage points, while largely preserving the influence of the high\-loss honest clients that fairness is meant to protect\.

[Consultar publicação](<https://arxiv.org/abs/2610.20264>)
