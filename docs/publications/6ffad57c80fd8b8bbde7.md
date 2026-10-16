---
title: Colored Graph Signal Diffusion Models
authors:
- Yiğit Berkay Uslu
- Samar Hadou
- Shirin Saeedi Bidokhti
- Alejandro Ribeiro
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Standard diffusion processes with isotropic noise corruption are not spectrally
  neutral. They inherit a coarse-to-fine generation hierarchy from the nonuniform
  data spectrum, because each frequency band loses signal-to-noise ratio (SNR) at
  its own rate. For signals on a graph, the relevant spectrum is that of the graph
  shift operator (GSO). A natural construction, therefore, builds both the diffusion
  dynamics and the denoiser from graph filters of the GSO, and any such design also
  takes a position on this hierarchy. We expose this hierarchy as a tunable axis through
  a family of colored score-based diffusions. Fixing the terminal prior to a Gaussian
  colored by the GSO couples the drift and diffusion through a positive spectral rate,
  which acts as a clock for each graph-frequency band. The clock sets when a band
  loses and recovers information, and the forward processes of standard and certain
  graph-aware diffusions appear as members of this family. A GSO-valued EDM preconditioning
  splits the denoiser into an analytic Wiener head that carries the Gaussian second-order
  structure and a graph neural network (GNN) that learns the remaining non-Gaussian
  dependencies. Numerical experiments show that colored diffusions reach a given generation
  quality in far fewer sampling steps than standard diffusion.
source:
- arXiv
source_ids:
- arxiv:2610.17282
url: https://arxiv.org/abs/2610.17282
discovered_at: '2026-10-16'
tags: *id001
---

# Colored Graph Signal Diffusion Models

**Autores:** Yiğit Berkay Uslu; Samar Hadou; Shirin Saeedi Bidokhti; Alejandro Ribeiro

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Standard diffusion processes with isotropic noise corruption are not spectrally neutral\. They inherit a coarse\-to\-fine generation hierarchy from the nonuniform data spectrum, because each frequency band loses signal\-to\-noise ratio \(SNR\) at its own rate\. For signals on a graph, the relevant spectrum is that of the graph shift operator \(GSO\)\. A natural construction, therefore, builds both the diffusion dynamics and the denoiser from graph filters of the GSO, and any such design also takes a position on this hierarchy\. We expose this hierarchy as a tunable axis through a family of colored score\-based diffusions\. Fixing the terminal prior to a Gaussian colored by the GSO couples the drift and diffusion through a positive spectral rate, which acts as a clock for each graph\-frequency band\. The clock sets when a band loses and recovers information, and the forward processes of standard and certain graph\-aware diffusions appear as members of this family\. A GSO\-valued EDM preconditioning splits the denoiser into an analytic Wiener head that carries the Gaussian second\-order structure and a graph neural network \(GNN\) that learns the remaining non\-Gaussian dependencies\. Numerical experiments show that colored diffusions reach a given generation quality in far fewer sampling steps than standard diffusion\.

[Consultar publicação](<https://arxiv.org/abs/2610.17282>)
