---
title: A Neural Processing Unit-Accelerated Monocular Perception Pipeline for Remotely
  Operated Underwater Vehicle Station Keeping
authors:
- Gyan Louisin
- Vinh La The
- Trung Ngo Lam
- Nga Nguyen Thi Thanh
- Dung Nguyen Anh
- Duc Dương Minh
- Hiep Hoang Van
date: '2026-10-15'
type: article
category: &id001
- Inteligência Artificial
doi: 10.51316/jst.194.dsai.2026.36.1.4
abstract: 'Holding a stable viewpoint is a prerequisite for observation tasks performed
  by remotely operated underwater vehicles, yet it is difficult to achieve when the
  only sensor is a monocular camera and all computation must run on board. This work
  reports the deployment of a complete visual stationkeeping perception pipeline on
  a Qualcomm QCS8550 platform using its Hexagon HTP/NPU accelerator, in which two
  networks---an INT8 object detector and a dense monocular depth model---share a single
  accelerator. A per-stage latency breakdown shows that the throughput difference
  between an accelerated and a CPU-executed configuration is attributable to one stage:
  moving depth inference alone to the accelerator makes it 27 times faster and carries
  the pipeline from 0.46 to 8.47 frames per second, with depth inference still occupying
  two thirds of the frame budget afterwards and the accelerator occupied at least
  69\% of wall-clock time. We document two deployment failure modes that are silent
  rather than loud: an output polarity that must be established empirically, and a
  normalisation choice that destroys the range signal. The two available range cues
  are combined by an analytic fusion rule---the square root of the tracked bounding
  box area and the depth output both vary inversely with distance, so the two are
  directly combinable once anchored on a reference captured at target selection, without
  training data or knowledge of the target dimensions. On the rigid targets evaluated
  here the zero-cost geometric term carries more of the distance signal than the depth
  network that consumes two thirds of the frame budget, and the two cues degrade unequally
  on immersion, which makes their relative weighting an operating parameter rather
  than a constant. Evaluation is open-loop; closed-loop validation was prevented by
  a degenerate thruster configuration.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221866279
url: https://doi.org/10.51316/jst.194.dsai.2026.36.1.4
discovered_at: '2026-10-19'
tags: *id001
---

# A Neural Processing Unit\-Accelerated Monocular Perception Pipeline for Remotely Operated Underwater Vehicle Station Keeping

**Autores:** Gyan Louisin; Vinh La The; Trung Ngo Lam; Nga Nguyen Thi Thanh; Dung Nguyen Anh; Duc Dương Minh; Hiep Hoang Van

**Data:** 2026-10-15 · **Tipo:** article

## Resumo

Holding a stable viewpoint is a prerequisite for observation tasks performed by remotely operated underwater vehicles, yet it is difficult to achieve when the only sensor is a monocular camera and all computation must run on board\. This work reports the deployment of a complete visual stationkeeping perception pipeline on a Qualcomm QCS8550 platform using its Hexagon HTP/NPU accelerator, in which two networks\-\-\-an INT8 object detector and a dense monocular depth model\-\-\-share a single accelerator\. A per\-stage latency breakdown shows that the throughput difference between an accelerated and a CPU\-executed configuration is attributable to one stage: moving depth inference alone to the accelerator makes it 27 times faster and carries the pipeline from 0\.46 to 8\.47 frames per second, with depth inference still occupying two thirds of the frame budget afterwards and the accelerator occupied at least 69\\% of wall\-clock time\. We document two deployment failure modes that are silent rather than loud: an output polarity that must be established empirically, and a normalisation choice that destroys the range signal\. The two available range cues are combined by an analytic fusion rule\-\-\-the square root of the tracked bounding box area and the depth output both vary inversely with distance, so the two are directly combinable once anchored on a reference captured at target selection, without training data or knowledge of the target dimensions\. On the rigid targets evaluated here the zero\-cost geometric term carries more of the distance signal than the depth network that consumes two thirds of the frame budget, and the two cues degrade unequally on immersion, which makes their relative weighting an operating parameter rather than a constant\. Evaluation is open\-loop; closed\-loop validation was prevented by a degenerate thruster configuration\.

[Consultar publicação](<https://doi.org/10.51316/jst.194.dsai.2026.36.1.4>)
