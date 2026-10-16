---
title: 'MontageFlow: Physically Valid High Fidelity EEG Generation'
authors:
- Sudarshan Regmi
- Nabaraj Subedi
- Arvind Pillai
- Yu Yvonne Wu
- Yuliang Chen
- Michael V. Heinz
- Lisa Marsch
- Nicholas C. Jacobson
- Andrew Campbell
date: '2026-10-10'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Generative modeling offers a promising solution to the scarcity of labeled
  clinical electroencephalography (EEG) data under strict privacy constraints. Although
  recent generative models report substantial improvements in generation fidelity,
  we show that these gains conceal a categorical failure. EEG is not an arbitrary
  multichannel signal: each channel records the voltage difference between two scalp
  electrodes. So, real recordings satisfy exact linear identities among their channels.
  Current generators invariably violate these identities, yet this has gone unnoticed.
  We therefore propose MontageFlow, a flow-matching model that enforces these identities
  by restricting its output to signals that satisfy them. We find that ensuring validity
  improves fidelity too. Furthermore, to retain the EEG characteristics that oversmoothing
  washes out, we also condition the model on a physiological state vector encoded
  from the whole EEG window. For generation, this vector is drawn from a prior fitted
  in latent space. Across 3 large-scale benchmarks, our model improves TS-FID by 1.6-3.6$\times$
  over the closest rival while ensuring validity.'
source:
- arXiv
source_ids:
- arxiv:2610.14507
url: https://arxiv.org/abs/2610.14507
discovered_at: '2026-10-16'
tags: *id001
---

# MontageFlow: Physically Valid High Fidelity EEG Generation

**Autores:** Sudarshan Regmi; Nabaraj Subedi; Arvind Pillai; Yu Yvonne Wu; Yuliang Chen; Michael V\. Heinz; Lisa Marsch; Nicholas C\. Jacobson; Andrew Campbell

**Data:** 2026-10-10 · **Tipo:** preprint

## Resumo

Generative modeling offers a promising solution to the scarcity of labeled clinical electroencephalography \(EEG\) data under strict privacy constraints\. Although recent generative models report substantial improvements in generation fidelity, we show that these gains conceal a categorical failure\. EEG is not an arbitrary multichannel signal: each channel records the voltage difference between two scalp electrodes\. So, real recordings satisfy exact linear identities among their channels\. Current generators invariably violate these identities, yet this has gone unnoticed\. We therefore propose MontageFlow, a flow\-matching model that enforces these identities by restricting its output to signals that satisfy them\. We find that ensuring validity improves fidelity too\. Furthermore, to retain the EEG characteristics that oversmoothing washes out, we also condition the model on a physiological state vector encoded from the whole EEG window\. For generation, this vector is drawn from a prior fitted in latent space\. Across 3 large\-scale benchmarks, our model improves TS\-FID by 1\.6\-3\.6$\\times$ over the closest rival while ensuring validity\.

[Consultar publicação](<https://arxiv.org/abs/2610.14507>)
