---
title: Hybrid Reasoning Agents
authors:
- Jiaru Zou
- Yunzhe Qi
- Sirui Chen
- Federico Bianchi
- Shang Zhu
- Pan Lu
- Jingrui He
- James Zou
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'How can we build an agent that thinks beyond human language, yet still
  acts through it in the external environment? Modern LLM agents still reason and
  interact through text, while latent reasoning offers an efficient internal medium
  but lacks native tool access and reasoning transparency. We bridge these two directions
  with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between
  latent reasoning and text-based interaction throughout a unified generation process.
  Architecturally, a lightweight HybridLink enables seamless transitions between text
  and latent modes, while the agent''s continuous working memory preserves lossless
  hybrid context across multiple turns. These designs preserve tool-integrated agentic
  capabilities while making latent thoughts directly inspectable. Building on this
  architecture, we further develop dedicated post-training algorithms for hybrid reasoning:
  HybridSFT stabilizes tool-integrated hybrid generation by teaching the backbone
  to coordinate with HybridLink, then HybridRL scales reasoning by learning when to
  think in latent space and when to act through text. We evaluate HybridAgent at 3
  model scales across 11 benchmarks covering mathematics, science, medicine, search,
  and agentic reasoning. Compared with frontier LLM Agents and agentic frameworks
  spanning both text-based and latent methods, HybridAgent consistently improves performance
  by 10.4%, while delivering 35.5%-54.7% token reduction, 1.8x-2.6x faster inference,
  and 2.7x-3.7x cost savings. Code and data are available at https://github.com/togethercomputer/HybridAgent.'
source:
- arXiv
source_ids:
- arxiv:2610.18861
url: https://arxiv.org/abs/2610.18861
discovered_at: '2026-10-16'
tags: *id001
---

# Hybrid Reasoning Agents

**Autores:** Jiaru Zou; Yunzhe Qi; Sirui Chen; Federico Bianchi; Shang Zhu; Pan Lu; Jingrui He; James Zou

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency\. We bridge these two directions with Hybrid Reasoning Agents \(HybridAgents\), which dynamically navigate between latent reasoning and text\-based interaction throughout a unified generation process\. Architecturally, a lightweight HybridLink enables seamless transitions between text and latent modes, while the agent&\#x27;s continuous working memory preserves lossless hybrid context across multiple turns\. These designs preserve tool\-integrated agentic capabilities while making latent thoughts directly inspectable\. Building on this architecture, we further develop dedicated post\-training algorithms for hybrid reasoning: HybridSFT stabilizes tool\-integrated hybrid generation by teaching the backbone to coordinate with HybridLink, then HybridRL scales reasoning by learning when to think in latent space and when to act through text\. We evaluate HybridAgent at 3 model scales across 11 benchmarks covering mathematics, science, medicine, search, and agentic reasoning\. Compared with frontier LLM Agents and agentic frameworks spanning both text\-based and latent methods, HybridAgent consistently improves performance by 10\.4%, while delivering 35\.5%\-54\.7% token reduction, 1\.8x\-2\.6x faster inference, and 2\.7x\-3\.7x cost savings\. Code and data are available at https://github\.com/togethercomputer/HybridAgent\.

[Consultar publicação](<https://arxiv.org/abs/2610.18861>)
