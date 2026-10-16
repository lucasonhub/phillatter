---
title: 'Interactive Navigation Beyond Reachability: Benchmark and Agentic Framework'
authors:
- Delun Li
- Xueyao Wei
- Rui Chen
- Yifei Wang
- Junzhi Yu
- Wenjie Song
- Xingyu Chen
date: '2026-10-12'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Existing embodied navigation tasks commonly assume that traversability and
  object states remain fixed during an episode. Yet reaching a goal may require opening
  a door to access a room and then opening a container to reveal a hidden target.
  We formulate interactive navigation beyond reachability, unifying channel-induced
  changes in spatial connectivity, container-induced changes in target visibility,
  and their sequential dependencies. We introduce MultINav-Bench, a 3K-episode ObjectGoal
  benchmark in MolmoSpaces spanning channel, container, and mixed tasks, with interaction-necessity
  annotations covering required and unnecessary episodes. Its data generation pipeline
  automates task construction across multiple task types. The evaluation protocol
  separately measures navigation success, interaction effectiveness, and cost. We
  further propose MultINav-Agent, a three-stage agentic framework built on a persistent,
  state-conditioned interaction graph. Semantic interactive perception grounds entities
  and interaction states; a vision-language model selects task-relevant actions based
  on expected changes in connectivity and target observability; and post-interaction
  verification updates the graph to guide subsequent navigation, exploration, or interaction.
  Experiments on MultINav-Bench show that MultINav-Agent consistently outperforms
  adapted baselines across channel, container, and mixed tasks.
source:
- arXiv
source_ids:
- arxiv:2610.17089
url: https://arxiv.org/abs/2610.17089
discovered_at: '2026-10-16'
tags: *id001
---

# Interactive Navigation Beyond Reachability: Benchmark and Agentic Framework

**Autores:** Delun Li; Xueyao Wei; Rui Chen; Yifei Wang; Junzhi Yu; Wenjie Song; Xingyu Chen

**Data:** 2026-10-12 · **Tipo:** preprint

## Resumo

Existing embodied navigation tasks commonly assume that traversability and object states remain fixed during an episode\. Yet reaching a goal may require opening a door to access a room and then opening a container to reveal a hidden target\. We formulate interactive navigation beyond reachability, unifying channel\-induced changes in spatial connectivity, container\-induced changes in target visibility, and their sequential dependencies\. We introduce MultINav\-Bench, a 3K\-episode ObjectGoal benchmark in MolmoSpaces spanning channel, container, and mixed tasks, with interaction\-necessity annotations covering required and unnecessary episodes\. Its data generation pipeline automates task construction across multiple task types\. The evaluation protocol separately measures navigation success, interaction effectiveness, and cost\. We further propose MultINav\-Agent, a three\-stage agentic framework built on a persistent, state\-conditioned interaction graph\. Semantic interactive perception grounds entities and interaction states; a vision\-language model selects task\-relevant actions based on expected changes in connectivity and target observability; and post\-interaction verification updates the graph to guide subsequent navigation, exploration, or interaction\. Experiments on MultINav\-Bench show that MultINav\-Agent consistently outperforms adapted baselines across channel, container, and mixed tasks\.

[Consultar publicação](<https://arxiv.org/abs/2610.17089>)
