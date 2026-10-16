---
title: 'Green AI and Sustainable Computing: Energy-Aware Training, Inference Compression,
  and Carbon-Optimal Workload Scheduling'
authors:
- Raj Kumar
- Ramotar
- Dr. Akhil Pandey
- Vishal Shrivastava
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.5281/zenodo.23339663
abstract: 'Abstract—The exponential scaling of frontier Artificial Intelligence (AI)
  foundation models and global real-time inference workloads has precipitated an alarming
  surge in electrical energy consumption, water cooling demands, and greenhouse gas
  (GHG) emissions. Training a single 70B+ parameter transformer model consumes hundreds
  of megawatt-hours (MWh) of electricity, while high-throughput inference serving
  clusters run continuous multi-kilowatt server racks across worldwide datacenters.
  In response, ''Green AI'' has emerged as an essential computational discipline prioritizing
  energy efficiency, operational and embodied carbon footprint minimization, and computational
  sustainability alongside raw accuracy metrics (''Red AI''). However, transitioning
  enterprise computing systems toward sustainable AI introduces multifaceted engineering
  trade-offs: algorithmic compression vs. downstream reasoning degradation, non-uniform
  spatial-temporal grid carbon intensity, and memory bandwidth bottlenecks under low-precision
  quantization. This paper presents an exhaustive, mathematically formal technical
  survey and empirical architectural evaluation of Green AI spanning the entire lifecycle
  of foundation models. We formalize the holistic carbon accounting framework incorporating
  embodied silicon manufacturing emissions, model the mathematical dynamics of dynamic
  Mixture-of-Experts (MoE) token routing, analyze FlashAttention memory-IO energy
  bounds, and formulate carbon-aware spatiotemporal workload scheduling across geographically
  distributed datacenters. Furthermore, we construct an empirical enterprise benchmarking
  testbed across an 8-node NVIDIA H100/A100 cluster executing pre-training, fine-tuning,
  and inference on open foundation models (Llama-3-70B, Mixtral-8x7B). Our empirical
  findings demonstrate that sparse MoE routing paired with FP8 FlashAttention-3 slashes
  pre-training energy consumption by 48.2% while matching dense model perplexity.
  Concurrently, carbon-aware temporal job shifting achieves a 38.6% reduction in operational
  carbon dioxide equivalent (CO2e) emissions by aligning elastic training runs with
  regional renewable grid surpluses. Finally, we formulate open challenges in zero-water
  datacenter cooling, unified embodied carbon lifecycle tracking, and sustainable
  microarchitectural hardware co-design. Index Terms—Green AI, Sustainable Computing,
  Carbon Accounting, Mixture-of-Experts (MoE), FlashAttention, Speculative Decoding,
  Spatiotemporal Workload Scheduling, Energy-Efficient Deep Learning.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221725690
url: https://doi.org/10.5281/zenodo.23339663
discovered_at: '2026-10-16'
tags: *id001
---

# Green AI and Sustainable Computing: Energy\-Aware Training, Inference Compression, and Carbon\-Optimal Workload Scheduling

**Autores:** Raj Kumar; Ramotar; Dr\. Akhil Pandey; Vishal Shrivastava

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Abstract—The exponential scaling of frontier Artificial Intelligence \(AI\) foundation models and global real\-time inference workloads has precipitated an alarming surge in electrical energy consumption, water cooling demands, and greenhouse gas \(GHG\) emissions\. Training a single 70B\+ parameter transformer model consumes hundreds of megawatt\-hours \(MWh\) of electricity, while high\-throughput inference serving clusters run continuous multi\-kilowatt server racks across worldwide datacenters\. In response, &\#x27;Green AI&\#x27; has emerged as an essential computational discipline prioritizing energy efficiency, operational and embodied carbon footprint minimization, and computational sustainability alongside raw accuracy metrics \(&\#x27;Red AI&\#x27;\)\. However, transitioning enterprise computing systems toward sustainable AI introduces multifaceted engineering trade\-offs: algorithmic compression vs\. downstream reasoning degradation, non\-uniform spatial\-temporal grid carbon intensity, and memory bandwidth bottlenecks under low\-precision quantization\. This paper presents an exhaustive, mathematically formal technical survey and empirical architectural evaluation of Green AI spanning the entire lifecycle of foundation models\. We formalize the holistic carbon accounting framework incorporating embodied silicon manufacturing emissions, model the mathematical dynamics of dynamic Mixture\-of\-Experts \(MoE\) token routing, analyze FlashAttention memory\-IO energy bounds, and formulate carbon\-aware spatiotemporal workload scheduling across geographically distributed datacenters\. Furthermore, we construct an empirical enterprise benchmarking testbed across an 8\-node NVIDIA H100/A100 cluster executing pre\-training, fine\-tuning, and inference on open foundation models \(Llama\-3\-70B, Mixtral\-8x7B\)\. Our empirical findings demonstrate that sparse MoE routing paired with FP8 FlashAttention\-3 slashes pre\-training energy consumption by 48\.2% while matching dense model perplexity\. Concurrently, carbon\-aware temporal job shifting achieves a 38\.6% reduction in operational carbon dioxide equivalent \(CO2e\) emissions by aligning elastic training runs with regional renewable grid surpluses\. Finally, we formulate open challenges in zero\-water datacenter cooling, unified embodied carbon lifecycle tracking, and sustainable microarchitectural hardware co\-design\. Index Terms—Green AI, Sustainable Computing, Carbon Accounting, Mixture\-of\-Experts \(MoE\), FlashAttention, Speculative Decoding, Spatiotemporal Workload Scheduling, Energy\-Efficient Deep Learning\.

[Consultar publicação](<https://doi.org/10.5281/zenodo.23339663>)
