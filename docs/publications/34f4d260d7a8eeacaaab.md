---
title: AI Models Can Provably Hide Arbitrary Capabilities
authors:
- Andis Draguns
- Sumeet Ramesh Motwani
- Raymond Douglas
- Christian Schroeder de Witt
date: '2026-10-09'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Capability evaluations aim to surface dangerous model behaviors before deployment,
  but their reliability depends on the assumption that hidden capabilities can be
  elicited. We show this assumption does not hold under adversarial conditions by
  constructing backdoor attacks that embed encrypted neural networks within host model
  weights, decrypting and executing them only upon receiving a secret trigger. Using
  digital lockers, these hidden circuits remain provably hard to elicit and interpret
  under cryptographic assumptions, even given full access to model weights, extending
  prior work from hiding fixed strings to arbitrary computations. We implement our
  proof of concept constructions in PyTorch and evaluate elicitation through fine-tuning,
  weight noising, gradient-based trigger search, and latent adversarial training,
  using a small chemical reaction prediction task as a proxy for CBRN-relevant capabilities.
  Our results demonstrate resistance to these methods and, together with our cryptographic
  guarantees, reveal a limit of elicitation-based capability audits. We release our
  models to support the improvement of defenses.
source:
- arXiv
source_ids:
- arxiv:2610.13928
url: https://arxiv.org/abs/2610.13928
discovered_at: '2026-10-16'
tags: *id001
---

# AI Models Can Provably Hide Arbitrary Capabilities

**Autores:** Andis Draguns; Sumeet Ramesh Motwani; Raymond Douglas; Christian Schroeder de Witt

**Data:** 2026-10-09 · **Tipo:** preprint

## Resumo

Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited\. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger\. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under cryptographic assumptions, even given full access to model weights, extending prior work from hiding fixed strings to arbitrary computations\. We implement our proof of concept constructions in PyTorch and evaluate elicitation through fine\-tuning, weight noising, gradient\-based trigger search, and latent adversarial training, using a small chemical reaction prediction task as a proxy for CBRN\-relevant capabilities\. Our results demonstrate resistance to these methods and, together with our cryptographic guarantees, reveal a limit of elicitation\-based capability audits\. We release our models to support the improvement of defenses\.

[Consultar publicação](<https://arxiv.org/abs/2610.13928>)
