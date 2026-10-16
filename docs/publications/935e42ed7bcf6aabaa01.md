---
title: Towards Safe Autonomy for Computer Use
authors:
- Dominik Seip
- Bartol Markovinović
- Matthias Hein
date: '2026-10-13'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: 'The safety of LLM-based agents currently rests on alignment training and
  safety classifiers, neither of which can rule out that a sophisticated indirect
  prompt injection (IPI) goes through and causes significant harm. Recent work therefore
  builds agents with information-flow guarantees that rely on structured tool interfaces
  to interact with the environment. Computer Use Agents (CUAs) act visually on the
  computer screen, which does not provide a boundary between trusted first-party interfaces
  and untrusted, potentially attacker-authored content. Actions are equally ambiguous:
  a click may land on an application toolbar or a button controlled by an attacker.
  Treating the user as the source of trust and confirming each sensitive decision
  produces confirmation fatigue, with the risk of missing harmful actions. We introduce
  SA-CUA, a dual-LLM framework that generates a reliable trust boundary for CUAs by
  deriving conservative deterministic rules from the accessibility tree for unmasking
  trusted regions from the privileged LLM''s screenshot, keeping trusted and untrusted
  content separated. Human interaction is only required for proper task specification
  in the beginning. During the task a robust endorsement channel allows values to
  pass from the untrusted to the trusted domain by verifying information via trusted
  channels. This allows the agent to autonomously handle tasks involving untrusted
  information. SA-CUA maintains much higher utility than CaMeL-CUA while keeping the
  attack success rate at zero.'
source:
- arXiv
source_ids:
- arxiv:2610.18508
url: https://arxiv.org/abs/2610.18508
discovered_at: '2026-10-16'
tags: *id001
---

# Towards Safe Autonomy for Computer Use

**Autores:** Dominik Seip; Bartol Markovinović; Matthias Hein

**Data:** 2026-10-13 · **Tipo:** preprint

## Resumo

The safety of LLM\-based agents currently rests on alignment training and safety classifiers, neither of which can rule out that a sophisticated indirect prompt injection \(IPI\) goes through and causes significant harm\. Recent work therefore builds agents with information\-flow guarantees that rely on structured tool interfaces to interact with the environment\. Computer Use Agents \(CUAs\) act visually on the computer screen, which does not provide a boundary between trusted first\-party interfaces and untrusted, potentially attacker\-authored content\. Actions are equally ambiguous: a click may land on an application toolbar or a button controlled by an attacker\. Treating the user as the source of trust and confirming each sensitive decision produces confirmation fatigue, with the risk of missing harmful actions\. We introduce SA\-CUA, a dual\-LLM framework that generates a reliable trust boundary for CUAs by deriving conservative deterministic rules from the accessibility tree for unmasking trusted regions from the privileged LLM&\#x27;s screenshot, keeping trusted and untrusted content separated\. Human interaction is only required for proper task specification in the beginning\. During the task a robust endorsement channel allows values to pass from the untrusted to the trusted domain by verifying information via trusted channels\. This allows the agent to autonomously handle tasks involving untrusted information\. SA\-CUA maintains much higher utility than CaMeL\-CUA while keeping the attack success rate at zero\.

[Consultar publicação](<https://arxiv.org/abs/2610.18508>)
