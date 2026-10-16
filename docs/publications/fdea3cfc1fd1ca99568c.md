---
title: 'H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression'
authors:
- Or Ronai
- Vladimir Kulikov
- Tomer Michaeli
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Training-free diffusion-based compression methods repurpose the generative
  priors of a diffusion or a flow model to compress data without retraining them as
  task-specific codecs. Recent codebook-based approaches such as Turbo-DDCM achieve
  strong perceptual quality at ultra-low bitrates, but their reliance on dense Gaussian
  codebooks remains costly in both memory and computation, and scales poorly with
  the large latent dimensions of modern image and video generators. Their combinatorial
  bitstream encoding further becomes computationally heavy at this scale. We introduce
  H-DDCM, a scalable generative compression framework that replaces Gaussian codebooks
  with implicit randomized Hadamard dictionaries. The fast Walsh-Hadamard transform
  allows for implicitly synthesizing full-dimensional dictionaries with $O(d \log
  d)$ compute for projection and reconstruction and $O(d)$ memory, without materializing
  the full-dimensional dictionary. We further introduce an efficient table-free lexicographic
  coding scheme that makes combinatorial encoding practical at larger dimensions.
  Beyond images, we adapt the framework to an autoregressive video flow model and
  develop a streaming compression scheme that periodically re-encodes recently reconstructed
  frames into a fresh KV-cache prefix, preserving temporal context across segments
  at no additional transmitted bits. This enables long-form, close to real-time generative
  video compression on a single GPU. Across image and video benchmarks, H-DDCM achieves
  competitive rate-distortion-perception performance while substantially reducing
  the memory and computational overhead of codebook-based training-free generative
  compression.
source:
- arXiv
source_ids:
- arxiv:2610.18125
url: https://arxiv.org/abs/2610.18125
discovered_at: '2026-10-16'
tags: *id001
---

# H\-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression

**Autores:** Or Ronai; Vladimir Kulikov; Tomer Michaeli

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

Training\-free diffusion\-based compression methods repurpose the generative priors of a diffusion or a flow model to compress data without retraining them as task\-specific codecs\. Recent codebook\-based approaches such as Turbo\-DDCM achieve strong perceptual quality at ultra\-low bitrates, but their reliance on dense Gaussian codebooks remains costly in both memory and computation, and scales poorly with the large latent dimensions of modern image and video generators\. Their combinatorial bitstream encoding further becomes computationally heavy at this scale\. We introduce H\-DDCM, a scalable generative compression framework that replaces Gaussian codebooks with implicit randomized Hadamard dictionaries\. The fast Walsh\-Hadamard transform allows for implicitly synthesizing full\-dimensional dictionaries with $O\(d \\log d\)$ compute for projection and reconstruction and $O\(d\)$ memory, without materializing the full\-dimensional dictionary\. We further introduce an efficient table\-free lexicographic coding scheme that makes combinatorial encoding practical at larger dimensions\. Beyond images, we adapt the framework to an autoregressive video flow model and develop a streaming compression scheme that periodically re\-encodes recently reconstructed frames into a fresh KV\-cache prefix, preserving temporal context across segments at no additional transmitted bits\. This enables long\-form, close to real\-time generative video compression on a single GPU\. Across image and video benchmarks, H\-DDCM achieves competitive rate\-distortion\-perception performance while substantially reducing the memory and computational overhead of codebook\-based training\-free generative compression\.

[Consultar publicação](<https://arxiv.org/abs/2610.18125>)
