---
title: 'When Correctness Feedback Erases Evidence: Phase-Separated Completeness Auditing
  in Verus'
authors:
- Adarsh Agrawal
date: '2026-10-14'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Correctness feedback suppresses the very evidence that specification-completeness
  auditing is designed to uncover: programs that satisfy a written contract but violate
  intended behavior. We demonstrate this objective reversal on 12 Verus/Rust tasks
  across four model families under matched call budgets. Independent no-feedback discovery
  more than doubles certified-witness yield relative to IntentShield''s corrective-feedback
  loop (59.0% versus 27.1%). A format-matched iterative control places the larger
  share of this gap in feedback content, not independent restarts. The advantage holds
  in every model family and survives parser repair. A separate phase-separated execution
  matches the aggregate yield without reusing responses; most certified witnesses
  also fail held-out cases. Preserving these witnesses delivers stronger specification
  repair: Phase-Revised contracts achieve 81.3% implementation success, versus 62.5%
  for IS-Revised, with Direct-Revised close behind. Both no-feedback witness sources
  substantially outperform weakened contracts. The effect does not reproduce in the
  available Dafny and Lean evaluations, establishing an empirical boundary around
  the studied Verus/Rust workflow. Completeness auditing and correctness repair have
  opposing immediate objectives. Preserve and certify the admitted failure before
  repairing it.'
source:
- arXiv
source_ids:
- arxiv:2610.20676
url: https://arxiv.org/abs/2610.20676
discovered_at: '2026-10-16'
tags: *id001
---

# When Correctness Feedback Erases Evidence: Phase\-Separated Completeness Auditing in Verus

**Autores:** Adarsh Agrawal

**Data:** 2026-10-14 · **Tipo:** preprint

## Resumo

Correctness feedback suppresses the very evidence that specification\-completeness auditing is designed to uncover: programs that satisfy a written contract but violate intended behavior\. We demonstrate this objective reversal on 12 Verus/Rust tasks across four model families under matched call budgets\. Independent no\-feedback discovery more than doubles certified\-witness yield relative to IntentShield&\#x27;s corrective\-feedback loop \(59\.0% versus 27\.1%\)\. A format\-matched iterative control places the larger share of this gap in feedback content, not independent restarts\. The advantage holds in every model family and survives parser repair\. A separate phase\-separated execution matches the aggregate yield without reusing responses; most certified witnesses also fail held\-out cases\. Preserving these witnesses delivers stronger specification repair: Phase\-Revised contracts achieve 81\.3% implementation success, versus 62\.5% for IS\-Revised, with Direct\-Revised close behind\. Both no\-feedback witness sources substantially outperform weakened contracts\. The effect does not reproduce in the available Dafny and Lean evaluations, establishing an empirical boundary around the studied Verus/Rust workflow\. Completeness auditing and correctness repair have opposing immediate objectives\. Preserve and certify the admitted failure before repairing it\.

[Consultar publicação](<https://arxiv.org/abs/2610.20676>)
