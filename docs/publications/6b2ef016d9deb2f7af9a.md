---
title: 'OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using
  Agents'
authors:
- Bowen Yang
- Kaiming Jin
- Zichen Ding
- Zhenyu Wu
- Zehao Li
- Zhoumianze Liu
- Kanzhi Cheng
- Fangzhi Xu
- Yanan Sun
- Qiushi Sun
- Yu Qiao
date: '2026-10-15'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: Real desktop automation is neither purely visual nor purely programmatic.
  Agents must understand user-facing interfaces while efficiently manipulating files,
  scripts, and system state. However, native GUI/code coordination cannot be obtained
  by prompt-level tool composition. In our preliminary experiments, naively adding
  a code tool degrades a GUI agent, revealing that GUI/code routing must be internalized
  through training on high-quality hybrid data. We present OS-Helix, an end-to-end
  trained multimodal computer-using agent that unifies GUI actions and code execution
  in one action space. To construct the required supervision, we introduce application-artifact
  composition, pairing desktop applications with authentic file artifacts to instantiate
  executable Ubuntu states, and a decoupled instruction/evaluator generation pipeline
  that produces environment-grounded tasks whose final states can be verified regardless
  of the solution modality. We cold-start the policy with SFT on filtered hybrid data
  and further improve it through online RL in live desktop environments. For RL, we
  propose Step-balanced GSPO, which aggregates importance weight by action step rather
  than raw assistant tokens to prevent long code actions from dominating heterogeneous-action
  optimization. On OSWorld-Verified, OS-Helix-27B and OS-Helix-35B-A3B achieve relative
  improvements of 35.0% and 33.7% over their matched Qwen3.5 hybrid baselines, while
  OS-Helix-27B-RL further improves by 42.9% to reach 66.44% success. Ablations provide
  evidence consistent with contributions from learned GUI/code coordination, scalable
  verifiable supervision, and action step balanced optimization, while demonstrating
  cross-platform transfer on WindowsAgentArena. Our project homepage is at https://os-copilot.github.io/OS-Helix/.
source:
- arXiv
source_ids:
- arxiv:2610.22234
url: https://arxiv.org/abs/2610.22234
discovered_at: '2026-10-19'
tags: *id001
---

# OS\-Helix: Unifying GUI Interaction and Code Execution in Native Computer\-Using Agents

**Autores:** Bowen Yang; Kaiming Jin; Zichen Ding; Zhenyu Wu; Zehao Li; Zhoumianze Liu; Kanzhi Cheng; Fangzhi Xu; Yanan Sun; Qiushi Sun; Yu Qiao

**Data:** 2026-10-15 · **Tipo:** preprint

## Resumo

Real desktop automation is neither purely visual nor purely programmatic\. Agents must understand user\-facing interfaces while efficiently manipulating files, scripts, and system state\. However, native GUI/code coordination cannot be obtained by prompt\-level tool composition\. In our preliminary experiments, naively adding a code tool degrades a GUI agent, revealing that GUI/code routing must be internalized through training on high\-quality hybrid data\. We present OS\-Helix, an end\-to\-end trained multimodal computer\-using agent that unifies GUI actions and code execution in one action space\. To construct the required supervision, we introduce application\-artifact composition, pairing desktop applications with authentic file artifacts to instantiate executable Ubuntu states, and a decoupled instruction/evaluator generation pipeline that produces environment\-grounded tasks whose final states can be verified regardless of the solution modality\. We cold\-start the policy with SFT on filtered hybrid data and further improve it through online RL in live desktop environments\. For RL, we propose Step\-balanced GSPO, which aggregates importance weight by action step rather than raw assistant tokens to prevent long code actions from dominating heterogeneous\-action optimization\. On OSWorld\-Verified, OS\-Helix\-27B and OS\-Helix\-35B\-A3B achieve relative improvements of 35\.0% and 33\.7% over their matched Qwen3\.5 hybrid baselines, while OS\-Helix\-27B\-RL further improves by 42\.9% to reach 66\.44% success\. Ablations provide evidence consistent with contributions from learned GUI/code coordination, scalable verifiable supervision, and action step balanced optimization, while demonstrating cross\-platform transfer on WindowsAgentArena\. Our project homepage is at https://os\-copilot\.github\.io/OS\-Helix/\.

[Consultar publicação](<https://arxiv.org/abs/2610.22234>)
