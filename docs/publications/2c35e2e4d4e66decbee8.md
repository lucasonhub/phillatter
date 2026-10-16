---
title: Inference on the Value of Policy Improvement in Adaptive Experiments
authors:
- Justin Whitehouse
- Emma Brunskill
- Vasilis Syrgkanis
date: '2026-10-11'
type: preprint
category: &id001
- Inteligência Artificial
doi: null
abstract: In this paper, we develop an asymptotically normal estimator for the value
  of policy improvement (VPI) under adaptively collected data. This value, which is
  defined as the gap between the value of the best treatment policy in a class and
  that of a baseline policy, gauges whether or not it is worth deploying a personalized
  treatment policy. Building an estimator for the VPI is naturally more difficult
  than estimating the value of a fixed policy. This is because, in addition to contending
  with the correlated data and decaying propensities associated with adaptive experiments,
  any estimator must also handle the non-regularity, or lack of pathwise differentiability,
  of the underlying estimand when the optimal policy is non-unique. Our proposed estimator
  works by sequentially fitting a weighted empirical welfare maximizing policy on
  historical data and then evaluating it using inverse propensity weighting on future
  samples. We neither assume that the optimal policy is unique nor make a margin assumption
  on the underlying heterogeneous treatment effects. A key difficulty in analyzing
  our estimator is showing that the regret incurred through policy learning is asymptotically
  smaller than the standard error of the estimator. We accomplish this by showing
  faster regret rates for policy learning under decaying propensities, which may be
  of independent interest. We not only evaluate the coverage of our estimator on a
  mix of synthetic and semi-synthetic data, but also employ it to estimate the VPI
  in an adaptive experiment evaluating the efficacy of job assistance programs in
  Jordan due to Caria et al. Although our estimates are generally more conservative
  than their hierarchical Bayesian analysis, which assumes that the optimal policy
  is unique, we still corroborate the benefits of personalization amongst Syrian refugees.
source:
- arXiv
source_ids:
- arxiv:2610.15789
url: https://arxiv.org/abs/2610.15789
discovered_at: '2026-10-16'
tags: *id001
---

# Inference on the Value of Policy Improvement in Adaptive Experiments

**Autores:** Justin Whitehouse; Emma Brunskill; Vasilis Syrgkanis

**Data:** 2026-10-11 · **Tipo:** preprint

## Resumo

In this paper, we develop an asymptotically normal estimator for the value of policy improvement \(VPI\) under adaptively collected data\. This value, which is defined as the gap between the value of the best treatment policy in a class and that of a baseline policy, gauges whether or not it is worth deploying a personalized treatment policy\. Building an estimator for the VPI is naturally more difficult than estimating the value of a fixed policy\. This is because, in addition to contending with the correlated data and decaying propensities associated with adaptive experiments, any estimator must also handle the non\-regularity, or lack of pathwise differentiability, of the underlying estimand when the optimal policy is non\-unique\. Our proposed estimator works by sequentially fitting a weighted empirical welfare maximizing policy on historical data and then evaluating it using inverse propensity weighting on future samples\. We neither assume that the optimal policy is unique nor make a margin assumption on the underlying heterogeneous treatment effects\. A key difficulty in analyzing our estimator is showing that the regret incurred through policy learning is asymptotically smaller than the standard error of the estimator\. We accomplish this by showing faster regret rates for policy learning under decaying propensities, which may be of independent interest\. We not only evaluate the coverage of our estimator on a mix of synthetic and semi\-synthetic data, but also employ it to estimate the VPI in an adaptive experiment evaluating the efficacy of job assistance programs in Jordan due to Caria et al\. Although our estimates are generally more conservative than their hierarchical Bayesian analysis, which assumes that the optimal policy is unique, we still corroborate the benefits of personalization amongst Syrian refugees\.

[Consultar publicação](<https://arxiv.org/abs/2610.15789>)
