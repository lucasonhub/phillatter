---
title: Motion guided Channel wise Hypergraph convolutional network for skeleton action
  recognition
authors:
- Wei Guo
- Jing Guo
- Wei Ji
- Shasha Yang
date: '2026-10-09'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1007/s10791-026-10702-z
abstract: Skeleton-based action recognition has advanced significantly with graph
  convolutional networks that model joints as nodes and bones as edges. However, conventional
  graphs are inherently limited to pairwise connections and are less effective at
  representing group-wise coordination patterns in human motion, where multiple joints
  often act as a functional unit during complex movements such as swinging or throwing.
  Hypergraphs provide a natural alternative by allowing hyperedges to connect arbitrary
  numbers of joints and explicitly encode coordinated joint groups. We propose the
  Motion-Guided Channel-Wise Hypergraph Convolutional Network (MC-HGCN), which models
  skeleton sequences through a unified hypergraph structure with three complementary
  mechanisms. MC-HGCN first constructs anatomical body-part and cross-limb hyperedges
  to provide structural priors. A motion-guided modulation mechanism adaptively reweights
  the hypergraph incidence matrix according to per-frame joint motion intensity, dynamically
  emphasizing active joint groups. Furthermore, a channel-wise hyperedge learning
  module discovers distinct coordination patterns across feature channels, enabling
  feature-specific relational modeling. A residual pathway preserves fine-grained
  pairwise information to complement high-order hypergraph aggregation. Extensive
  experiments on NTU RGB+D 60 and NTU RGB+D 120 demonstrate that MC-HGCN achieves
  strong performance using only joint coordinates, with notable improvements on high-motion
  actions involving complex multi-joint coordination. Ablation studies and visualization
  analyses further validate the effectiveness of each proposed component.
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221177614
url: https://doi.org/10.1007/s10791-026-10702-z
discovered_at: '2026-10-16'
tags: *id001
---

# Motion guided Channel wise Hypergraph convolutional network for skeleton action recognition

**Autores:** Wei Guo; Jing Guo; Wei Ji; Shasha Yang

**Data:** 2026-10-09 · **Tipo:** article

## Resumo

Skeleton\-based action recognition has advanced significantly with graph convolutional networks that model joints as nodes and bones as edges\. However, conventional graphs are inherently limited to pairwise connections and are less effective at representing group\-wise coordination patterns in human motion, where multiple joints often act as a functional unit during complex movements such as swinging or throwing\. Hypergraphs provide a natural alternative by allowing hyperedges to connect arbitrary numbers of joints and explicitly encode coordinated joint groups\. We propose the Motion\-Guided Channel\-Wise Hypergraph Convolutional Network \(MC\-HGCN\), which models skeleton sequences through a unified hypergraph structure with three complementary mechanisms\. MC\-HGCN first constructs anatomical body\-part and cross\-limb hyperedges to provide structural priors\. A motion\-guided modulation mechanism adaptively reweights the hypergraph incidence matrix according to per\-frame joint motion intensity, dynamically emphasizing active joint groups\. Furthermore, a channel\-wise hyperedge learning module discovers distinct coordination patterns across feature channels, enabling feature\-specific relational modeling\. A residual pathway preserves fine\-grained pairwise information to complement high\-order hypergraph aggregation\. Extensive experiments on NTU RGB\+D 60 and NTU RGB\+D 120 demonstrate that MC\-HGCN achieves strong performance using only joint coordinates, with notable improvements on high\-motion actions involving complex multi\-joint coordination\. Ablation studies and visualization analyses further validate the effectiveness of each proposed component\.

[Consultar publicação](<https://doi.org/10.1007/s10791-026-10702-z>)
