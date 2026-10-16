---
title: A Real-Time Machine Learning-Based Intrusion Detection and Prevention System
  for Decentralized Networks using Random Forest and Isolation Forest
authors:
- I.I. Achi
- F.O. Ogbunude
date: '2026-10-11'
type: article
category: &id001
- Inteligência Artificial
doi: 10.67317/ijmsrt26aug062
abstract: 'Decentralized networks—spanning Internet-of-Things deployments, edge computing
  platforms and peer-to-peer systems—offer improved scalability, resilience and the
  elimination of single points of failure. At the same time, their distributed structure
  makes continuous monitoring and timely intrusion response substantially more difficult.
  Traditional signature-based intrusion detection systems (IDS) are effective only
  against previously catalogued attacks; they cannot reliably detect zero-day or heavily
  obfuscated threats and typically require the centralised collection of raw traffic,
  thereby raising privacy, bandwidth and single-point-of-failure concerns. This paper
  presents a complete real-time machine-learning-based user detection and intrusion
  prevention system expressly designed for decentralised environments. A lightweight
  monitoring agent executes on every registered physical node, continuously captures
  live network packets, groups them into traffic flows and extracts a compact set
  of discriminative features: packet rate, bandwidth usage, latency, failed login
  attempts and connection duration. These features are classified by a Random Forest
  ensemble that distinguishes authorised from unauthorised activity. Concurrently,
  an Isolation Forest anomaly detector flags behavioural outliers that may correspond
  to previously unseen (zero-day) attacks. For every prediction the system computes
  a continuous risk score, assigns a discrete threat level (Low, Medium, High or Critical),
  records an immutable event log entry, displays a real-time alert together with an
  AI-generated explanation on the administrator dashboard, and—when prevention mode
  is enabled—automatically installs firewall rules that block the offending traffic.
  Because only summarised detection results are forwarded to the central monitoring
  dashboard, raw packet data never leave the local node; privacy is preserved and
  inter-node communication overhead is minimised. Extensive evaluation on labelled
  network traffic demonstrates an accuracy of 96.80%, precision of 95.40%, recall
  of 94.20% and F1-score of 94.80%, markedly surpassing a conventional signature-based
  baseline. The system maintains normal network performance under both typical and
  elevated traffic loads, confirming that intelligent detection need not be purchased
  at the expense of operational efficiency.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221476509
url: https://doi.org/10.67317/ijmsrt26aug062
discovered_at: '2026-10-16'
tags: *id001
---

# A Real\-Time Machine Learning\-Based Intrusion Detection and Prevention System for Decentralized Networks using Random Forest and Isolation Forest

**Autores:** I\.I\. Achi; F\.O\. Ogbunude

**Data:** 2026-10-11 · **Tipo:** article

## Resumo

Decentralized networks—spanning Internet\-of\-Things deployments, edge computing platforms and peer\-to\-peer systems—offer improved scalability, resilience and the elimination of single points of failure\. At the same time, their distributed structure makes continuous monitoring and timely intrusion response substantially more difficult\. Traditional signature\-based intrusion detection systems \(IDS\) are effective only against previously catalogued attacks; they cannot reliably detect zero\-day or heavily obfuscated threats and typically require the centralised collection of raw traffic, thereby raising privacy, bandwidth and single\-point\-of\-failure concerns\. This paper presents a complete real\-time machine\-learning\-based user detection and intrusion prevention system expressly designed for decentralised environments\. A lightweight monitoring agent executes on every registered physical node, continuously captures live network packets, groups them into traffic flows and extracts a compact set of discriminative features: packet rate, bandwidth usage, latency, failed login attempts and connection duration\. These features are classified by a Random Forest ensemble that distinguishes authorised from unauthorised activity\. Concurrently, an Isolation Forest anomaly detector flags behavioural outliers that may correspond to previously unseen \(zero\-day\) attacks\. For every prediction the system computes a continuous risk score, assigns a discrete threat level \(Low, Medium, High or Critical\), records an immutable event log entry, displays a real\-time alert together with an AI\-generated explanation on the administrator dashboard, and—when prevention mode is enabled—automatically installs firewall rules that block the offending traffic\. Because only summarised detection results are forwarded to the central monitoring dashboard, raw packet data never leave the local node; privacy is preserved and inter\-node communication overhead is minimised\. Extensive evaluation on labelled network traffic demonstrates an accuracy of 96\.80%, precision of 95\.40%, recall of 94\.20% and F1\-score of 94\.80%, markedly surpassing a conventional signature\-based baseline\. The system maintains normal network performance under both typical and elevated traffic loads, confirming that intelligent detection need not be purchased at the expense of operational efficiency\.

[Consultar publicação](<https://doi.org/10.67317/ijmsrt26aug062>)
