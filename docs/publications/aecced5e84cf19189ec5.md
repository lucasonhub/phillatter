---
title: Mean Accuracy Is the Wrong Estimand for a Release Decision
authors:
- Jaewon Choi
- Jihye Kang
- Namhyuk Ahn
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'A release decision about a fine-tuned model is an operational commitment
  about the \emph{next} rerun of its training recipe. Yet standard benchmark reporting
  gives only the mean accuracy of past seeds. These target fundamentally different
  questions: release decisions depend on catastrophic tail risk, whereas standard
  evaluation reports only central tendency. Because fine-tuning induces bimodal mode
  collapse, high average accuracy frequently conceals severe failure rates. Auditing
  $2\,124$ fine-tuned models across eleven language models, we show that shipping
  models based on mean accuracy violates a $10\%$ deployment failure budget $48.0\%$
  of the time. Common heuristics like $\bar b - 2σ$ prove equally dangerous: by underestimating
  variance on small samples, they become most permissive when evidence is weakest.
  We introduce \textbf{recipe cards}, an evaluation framework that directly certifies
  rerun tail failure rates using exact finite-sample binomial bounds. Recipe cards
  reduce held-out budget violations to $0.6\%$, enforce a mathematical sample floor
  ($N \ge 22$) that prevents certification on thin evidence, and explicitly refuse
  unverified claims under domain and task shifts.'
source:
- arXiv
source_ids:
- arxiv:2610.16825
url: https://arxiv.org/abs/2610.16825
discovered_at: '2026-10-16'
tags: *id001
---

# Mean Accuracy Is the Wrong Estimand for a Release Decision

**Autores:** Jaewon Choi; Jihye Kang; Namhyuk Ahn

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

A release decision about a fine\-tuned model is an operational commitment about the \\emph\{next\} rerun of its training recipe\. Yet standard benchmark reporting gives only the mean accuracy of past seeds\. These target fundamentally different questions: release decisions depend on catastrophic tail risk, whereas standard evaluation reports only central tendency\. Because fine\-tuning induces bimodal mode collapse, high average accuracy frequently conceals severe failure rates\. Auditing $2\\,124$ fine\-tuned models across eleven language models, we show that shipping models based on mean accuracy violates a $10\\%$ deployment failure budget $48\.0\\%$ of the time\. Common heuristics like $\\bar b \- 2σ$ prove equally dangerous: by underestimating variance on small samples, they become most permissive when evidence is weakest\. We introduce \\textbf\{recipe cards\}, an evaluation framework that directly certifies rerun tail failure rates using exact finite\-sample binomial bounds\. Recipe cards reduce held\-out budget violations to $0\.6\\%$, enforce a mathematical sample floor \($N \\ge 22$\) that prevents certification on thin evidence, and explicitly refuse unverified claims under domain and task shifts\.

[Consultar publicação](<https://arxiv.org/abs/2610.16825>)
