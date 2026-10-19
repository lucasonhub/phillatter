---
title: 'Not All Graphs Are Maps: A Task-Agnostic Exploration Framework for Mobile
  GUI Navigation'
authors:
- Adamo Orsini
- Seyed Mehdi Ayyoubzadeh
- Sadman Rakib Pinon
- Hannuo Zhang
- Koosha Gholipour Baradari
- Yuanhao Yu
- Xinxin Zuo
- Yang Wang
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Modern mobile GUI agents can perceive visible screens and execute local
  actions, but they still lack persistent app-specific navigation knowledge: where
  functions live, which pages contain them, and which screens are equivalent across
  repeated visits. We introduce TAG-Nav, a Task-Agnostic Graph Navigation framework
  that wraps existing GUI-agent backbones with reusable destination memory. Offline
  exploration is distilled into compact records of app functions, target pages, and
  waypoint routes before any evaluated instruction is seen. When a future task''s
  destination is covered, TAG-Nav retrieves the destination and provides route guidance
  without task-specific demonstrations. This separates mobile GUI destination navigation
  from full task completion: many tasks share the prefix of reaching the right page,
  while final actions may enter content, send data, make purchases, delete information,
  or change sensitive settings. To evaluate route finding without downstream execution
  confounds, we introduce DestBench, a navigation-only protocol that asks whether
  an agent reaches the correct pre-action destination screen. DestBench enables a
  controlled graph-memory study comparing no-memory agents with random, automated
  BFS, and clean graph memory. Graph-derived memory improves strict navigation success
  rate of UI-TARS-1.5-7B from 52.4% without graph memory to 58.3% with automated BFS
  memory, and improves Qwen-VL-Max success rate from 59.5% to 71.4% on the same conditions.
  Together, TAG-Nav and DestBench show that destination coverage and route cleanliness
  strongly shape graph-memory value, making graph quality a measured variable rather
  than an assumed benefit of exploration.'
source:
- arXiv
source_ids:
- arxiv:2610.22672
url: https://arxiv.org/abs/2610.22672
discovered_at: '2026-10-19'
tags: *id001
---

# Not All Graphs Are Maps: A Task\-Agnostic Exploration Framework for Mobile GUI Navigation

**Autores:** Adamo Orsini; Seyed Mehdi Ayyoubzadeh; Sadman Rakib Pinon; Hannuo Zhang; Koosha Gholipour Baradari; Yuanhao Yu; Xinxin Zuo; Yang Wang

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Modern mobile GUI agents can perceive visible screens and execute local actions, but they still lack persistent app\-specific navigation knowledge: where functions live, which pages contain them, and which screens are equivalent across repeated visits\. We introduce TAG\-Nav, a Task\-Agnostic Graph Navigation framework that wraps existing GUI\-agent backbones with reusable destination memory\. Offline exploration is distilled into compact records of app functions, target pages, and waypoint routes before any evaluated instruction is seen\. When a future task&\#x27;s destination is covered, TAG\-Nav retrieves the destination and provides route guidance without task\-specific demonstrations\. This separates mobile GUI destination navigation from full task completion: many tasks share the prefix of reaching the right page, while final actions may enter content, send data, make purchases, delete information, or change sensitive settings\. To evaluate route finding without downstream execution confounds, we introduce DestBench, a navigation\-only protocol that asks whether an agent reaches the correct pre\-action destination screen\. DestBench enables a controlled graph\-memory study comparing no\-memory agents with random, automated BFS, and clean graph memory\. Graph\-derived memory improves strict navigation success rate of UI\-TARS\-1\.5\-7B from 52\.4% without graph memory to 58\.3% with automated BFS memory, and improves Qwen\-VL\-Max success rate from 59\.5% to 71\.4% on the same conditions\. Together, TAG\-Nav and DestBench show that destination coverage and route cleanliness strongly shape graph\-memory value, making graph quality a measured variable rather than an assumed benefit of exploration\.

[Consultar publicação](<https://arxiv.org/abs/2610.22672>)
