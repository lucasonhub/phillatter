---
title: 'Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic
  JEPA Predictors'
authors:
- Yeonseok Lee
date: '2026-10-11'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Vision-Language-Action (VLA) models commonly generate robot actions token
  by token through Large Language Model (LLM) decoders, causing inference latency
  to grow with action sequence length and limiting closed-loop control frequency.
  We present Goal-Conditioned Vision-Predictor-Action (VPA), which replaces autoregressive
  decoders with a lightweight latent control loop. A shared vision encoder and a frozen
  text encoder embed observations, goal images, and instructions; a neuro-symbolic
  selector chooses a discrete skill; a Joint-Embedding Predictive Architecture (JEPA)
  predictor forecasts the next latent state; and a flow-matching solver generates
  an entire action chunk in a few integration steps, so that sequential network evaluations
  per decision step do not depend on the action horizon. We analyze inference complexity,
  regularization against representation collapse, and conditions under which latent
  sub-goal thresholding limits error accumulation across task phases. As an initial
  proof of concept, we evaluated VPA on the LIBERO-10 suite. The trainable model has
  under 20M parameters (checkpoint under 75 MB, excluding a frozen 63.4M-parameter
  CLIP text encoder); a decision step of a single-camera reference configuration takes
  10-14 ms on an Apple M4; and trained only on LIBERO-10 demonstrations in under three
  hours on a single GPU, a two-camera policy succeeded in 40.0% of 200 evaluation
  episodes. These preliminary results from a single training run suggest the approach
  is workable. Code and weights are available at https://github.com/ylee-sling/Vision-Predictor-Action
  and https://huggingface.co/ylee-sling/vpa-libero10, and archived at https://doi.org/10.5281/zenodo.22960920.
source:
- arXiv
source_ids:
- arxiv:2610.15556
url: https://arxiv.org/abs/2610.15556
discovered_at: '2026-10-16'
tags: *id001
---

# Vision\-Predictor\-Action: Towards Efficient Embodied AI via Neuro\-Symbolic JEPA Predictors

**Autores:** Yeonseok Lee

**Data:** 2026-10-11 · **Tipo:** preprint

## Resumo

Vision\-Language\-Action \(VLA\) models commonly generate robot actions token by token through Large Language Model \(LLM\) decoders, causing inference latency to grow with action sequence length and limiting closed\-loop control frequency\. We present Goal\-Conditioned Vision\-Predictor\-Action \(VPA\), which replaces autoregressive decoders with a lightweight latent control loop\. A shared vision encoder and a frozen text encoder embed observations, goal images, and instructions; a neuro\-symbolic selector chooses a discrete skill; a Joint\-Embedding Predictive Architecture \(JEPA\) predictor forecasts the next latent state; and a flow\-matching solver generates an entire action chunk in a few integration steps, so that sequential network evaluations per decision step do not depend on the action horizon\. We analyze inference complexity, regularization against representation collapse, and conditions under which latent sub\-goal thresholding limits error accumulation across task phases\. As an initial proof of concept, we evaluated VPA on the LIBERO\-10 suite\. The trainable model has under 20M parameters \(checkpoint under 75 MB, excluding a frozen 63\.4M\-parameter CLIP text encoder\); a decision step of a single\-camera reference configuration takes 10\-14 ms on an Apple M4; and trained only on LIBERO\-10 demonstrations in under three hours on a single GPU, a two\-camera policy succeeded in 40\.0% of 200 evaluation episodes\. These preliminary results from a single training run suggest the approach is workable\. Code and weights are available at https://github\.com/ylee\-sling/Vision\-Predictor\-Action and https://huggingface\.co/ylee\-sling/vpa\-libero10, and archived at https://doi\.org/10\.5281/zenodo\.22960920\.

[Consultar publicação](<https://arxiv.org/abs/2610.15556>)
