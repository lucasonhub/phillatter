---
title: 'DTDD: Divergence-Triggered Dynamic Distillation for Reliable On-Policy Supervision'
authors:
- Qijia He
- Zequn Li
- Spencer Luo
- Tianle Chen
- Pradyumna Narayana
- Zixian Ma
- Ranjay Krishna
- Lan Nie
- Sugato Basu
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'On-policy distillation (OPD) provides dense token-level supervision on
  student rollouts, but this supervision can become unreliable when the student and
  teacher diverge, either because of a large initial policy gap or compounding errors
  in long-horizon reasoning and tool use. We introduce Divergence-Triggered Dynamic
  Distillation (DTDD), an adaptive OPD framework that uses segment-level student-teacher
  divergence to trigger teacher takeover during training. When divergence triggers
  an intervention during reasoning, the student prefix continues to receive standard
  OPD supervision. The teacher then generates a recovery suffix, which the student
  learns through behavior cloning, using cross-entropy on the teacher-generated tokens.
  We evaluate DTDD in three regimes: long-horizon reasoning, distillation from a base
  initialization without offline supervised fine-tuning (SFT), and multi-turn agents.
  We also compare alternative trigger designs and teacher-intervention rates. DTDD
  reduces the post-warmup peak gradient norm by $8.6\times$ and, from a base initialization,
  reaches $21.3\%$ held-out math accuracy in $2.6\times$ fewer optimizer updates than
  OPD; both methods finish near $22\%$. It improves best-observed performance by $4.8$
  and $4.1$ percentage points on ALFWorld with LoRA and agentic code, respectively.
  Ablations show that segment-averaged triggers outperform token-spike triggers. Behavior
  cloning is also more effective than the tested OPD surrogate for training teacher-generated
  recoveries. Across 23 experimental arms, takeover tends to help when the teacher
  substantially outperforms the OPD-trained student, provided that the teacher can
  recover from student-visited states, the student can learn those recoveries, and
  teacher intervention is neither excessive nor insufficient.'
source:
- arXiv
source_ids:
- arxiv:2610.19302
url: https://arxiv.org/abs/2610.19302
discovered_at: '2026-10-16'
tags: *id001
---

# DTDD: Divergence\-Triggered Dynamic Distillation for Reliable On\-Policy Supervision

**Autores:** Qijia He; Zequn Li; Spencer Luo; Tianle Chen; Pradyumna Narayana; Zixian Ma; Ranjay Krishna; Lan Nie; Sugato Basu

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

On\-policy distillation \(OPD\) provides dense token\-level supervision on student rollouts, but this supervision can become unreliable when the student and teacher diverge, either because of a large initial policy gap or compounding errors in long\-horizon reasoning and tool use\. We introduce Divergence\-Triggered Dynamic Distillation \(DTDD\), an adaptive OPD framework that uses segment\-level student\-teacher divergence to trigger teacher takeover during training\. When divergence triggers an intervention during reasoning, the student prefix continues to receive standard OPD supervision\. The teacher then generates a recovery suffix, which the student learns through behavior cloning, using cross\-entropy on the teacher\-generated tokens\. We evaluate DTDD in three regimes: long\-horizon reasoning, distillation from a base initialization without offline supervised fine\-tuning \(SFT\), and multi\-turn agents\. We also compare alternative trigger designs and teacher\-intervention rates\. DTDD reduces the post\-warmup peak gradient norm by $8\.6\\times$ and, from a base initialization, reaches $21\.3\\%$ held\-out math accuracy in $2\.6\\times$ fewer optimizer updates than OPD; both methods finish near $22\\%$\. It improves best\-observed performance by $4\.8$ and $4\.1$ percentage points on ALFWorld with LoRA and agentic code, respectively\. Ablations show that segment\-averaged triggers outperform token\-spike triggers\. Behavior cloning is also more effective than the tested OPD surrogate for training teacher\-generated recoveries\. Across 23 experimental arms, takeover tends to help when the teacher substantially outperforms the OPD\-trained student, provided that the teacher can recover from student\-visited states, the student can learn those recoveries, and teacher intervention is neither excessive nor insufficient\.

[Consultar publicação](<https://arxiv.org/abs/2610.19302>)
