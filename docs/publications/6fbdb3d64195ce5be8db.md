---
title: 'A Two-Tier Blockchain Architecture for Verifiable Explainable-AI Audit Trails:
  Individual and Merkle-Batched Commitment of SHAP-Based Fraud-Detection Decisions'
authors:
- Kavindu Karunarathne
date: '2026-10-13'
type: article
category: &id001
- Inteligência Artificial
doi: 10.36548/jaicn.2026.4.002
abstract: 'Machine learning systems that make automated decisions, including fraud
  flags, loan denials, and safety interlocks, typically generate an explanation (for
  example via SHAP) in the same trust domain as the model itself, leaving no independent
  proof that the explanation shown to an auditor is the one the model actually produced
  at decision time. This research presents and empirically evaluates a blockchain-anchored
  explainable-AI (XAI) audit-trail architecture that closes this gap by committing
  a canonical SHA-256 hash of each decision-and-explanation record to an Ethereum-compatible
  ledger, while keeping the full record, including the SHAP explanation, off-chain.
  The architecture is implemented end to end on a real fraud-detection pipeline consisting
  of a LightGBM classifier trained on the IEEE-CIS Fraud Detection dataset (590,540
  transactions), a SHAP TreeExplainer layer producing per-transaction feature attributions,
  a canonical JSON serialization and hashing procedure, and two complementary Solidity
  smart contracts: one committing each audit record individually, and the other committing
  batches of records via a Merkle root. Using 500 audit records, the schemes are benchmarked
  on an Ethereum-compatible network across batch sizes of 10 to 500 records and extended
  with synthetic hashes to 1,000, 2,500, and 5,000 records. Individual commitment
  registers a record in 6.3 to 17.4 ms at 139,300 gas per record. Merkle-root batching
  reduces on-chain gas consumption by 91.6% at 10 records to 99.98% at 5,000 records,
  with reduction factors rising from roughly 12-fold to nearly 5,982-fold. Tamper-detection
  trials correctly flagged altered records in 100% of cases. The work contributes
  a reproducible, empirically costed reference architecture for verifiable AI explanation
  integrity, and a direct, quantified comparison of two on-chain commitment strategies
  across three orders of magnitude of batch size that prior blockchain-XAI proposals
  have not benchmarked head to head.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221612398
url: https://doi.org/10.36548/jaicn.2026.4.002
discovered_at: '2026-10-16'
tags: *id001
---

# A Two\-Tier Blockchain Architecture for Verifiable Explainable\-AI Audit Trails: Individual and Merkle\-Batched Commitment of SHAP\-Based Fraud\-Detection Decisions

**Autores:** Kavindu Karunarathne

**Data:** 2026-10-13 · **Tipo:** article

## Resumo

Machine learning systems that make automated decisions, including fraud flags, loan denials, and safety interlocks, typically generate an explanation \(for example via SHAP\) in the same trust domain as the model itself, leaving no independent proof that the explanation shown to an auditor is the one the model actually produced at decision time\. This research presents and empirically evaluates a blockchain\-anchored explainable\-AI \(XAI\) audit\-trail architecture that closes this gap by committing a canonical SHA\-256 hash of each decision\-and\-explanation record to an Ethereum\-compatible ledger, while keeping the full record, including the SHAP explanation, off\-chain\. The architecture is implemented end to end on a real fraud\-detection pipeline consisting of a LightGBM classifier trained on the IEEE\-CIS Fraud Detection dataset \(590,540 transactions\), a SHAP TreeExplainer layer producing per\-transaction feature attributions, a canonical JSON serialization and hashing procedure, and two complementary Solidity smart contracts: one committing each audit record individually, and the other committing batches of records via a Merkle root\. Using 500 audit records, the schemes are benchmarked on an Ethereum\-compatible network across batch sizes of 10 to 500 records and extended with synthetic hashes to 1,000, 2,500, and 5,000 records\. Individual commitment registers a record in 6\.3 to 17\.4 ms at 139,300 gas per record\. Merkle\-root batching reduces on\-chain gas consumption by 91\.6% at 10 records to 99\.98% at 5,000 records, with reduction factors rising from roughly 12\-fold to nearly 5,982\-fold\. Tamper\-detection trials correctly flagged altered records in 100% of cases\. The work contributes a reproducible, empirically costed reference architecture for verifiable AI explanation integrity, and a direct, quantified comparison of two on\-chain commitment strategies across three orders of magnitude of batch size that prior blockchain\-XAI proposals have not benchmarked head to head\.

[Consultar publicação](<https://doi.org/10.36548/jaicn.2026.4.002>)
