---
title: Machine-Learning Classification of Topological Materials Using Crystallographic
  and Compositional Descriptors for Pre-DFT Screening
authors:
- Sammy S. Dan
- Joseph Bassey Emah
- Sylvester Andrew Ekong
date: '2026-10-15'
type: article
category: &id001
- Inteligência Artificial
doi: 10.83080/rejost.vol6no9.354
abstract: 'Identifying topological insulators and semimetals among inorganic crystalline
  materials traditionally requires density functional theory (DFT) calculations with
  spin–orbit coupling, a computationally expensive process that limits high-throughput
  screening. This study examined whether machine learning models trained on ground-state
  crystallographic and compositional descriptors, obtainable without DFT or space-group
  information, could reliably classify materials as topologically non-trivial, trivial,
  or semimetallic. A dataset of 1,391 labelled crystalline entries (230 semimetal,
  781 topological, 380 trivial), curated from the Inorganic Crystal Structure Database
  and the Topological Quantum Chemistry database, was cleaned, including manual correction,
  via direct ICSD lookup, of a systematic lattice-parameter data-entry artefact (an
  Excel auto-fill error that had propagated a single genuine c-parameter value across
  1,208 rows, identified by cross-validation against unit-cell volume), prior to a
  further, now pipeline-integrated audit that removed 47 true-duplicate ICSD entries
  and attempted live TQC API resolution of 10 conflicting-label ICSD groups, none
  of which returned a match, so the first-encountered row was conservatively retained
  in each case (net reduction from 1,450 to 1,391 entries), and used to engineer 31
  structural and compositional features motivated by the physics of spin-orbit-coupling-driven
  band inversion. Six classifiers, Random Forest, XGBoost, LightGBM, Support Vector
  Machine, an Artificial Neural Network, and a soft-voting Ensemble, were trained
  and optimised using nested stratified cross-validation, Bayesian hyperparameter
  search, and Synthetic Minority Oversampling Technique (SMOTE)-based class rebalancing
  applied strictly within each training fold. XGBoost produced the highest observed
  test-set performance (macro-F1 of 0.744, accuracy of 78.1%, macro-AUC-ROC of 0.896),
  narrowly ahead of LightGBM (macro-F1 0.721, accuracy 74.9%, macro-AUC-ROC 0.887),
  though the difference was not statistically significant (McNemar''s test, p = 1.000,
  Bonferroni-corrected); LightGBM was retained as the primary model for interpretability
  and screening on the basis of its lower cross-validation variance and better-behaved
  post-hoc probability calibration. Shapley Additive exPlanations (SHAP), permutation,
  and impurity-based feature importance analyses converged on a consistent predictor
  hierarchy: number of constituent elements, mean ionisation potential, electronegativity
  range, maximum atomic number, and mean atomic radius, corroborated by polymorph-level
  diagnostics providing evidence that the model exploits structural, not merely compositional,
  information in most cases, although structural signal proved insufficient in at
  least one hard case. Applied to the full dataset, LightGBM ranked 424 entries as
  Tier 1 (P(Topological) ≥ 0.80) high-confidence topological predictions within the
  labelled dataset, of which 419 corresponded to already-known topological labels
  — a precision of 98.8% against known labels (retrospective validation precision,
  not prospective discovery precision). Interpretability analysis was also used as
  a data-quality diagnostic, motivating a closer investigation that, together with
  cross-validation against unit-cell volume and a subsequent ICSD/TQC provenance audit,
  uncovering and correcting a latent artefact in an earlier version of the model''s
  most important feature. These findings demonstrate that pre-DFT structural and compositional
  descriptors carry physically plausible and interpretable predictive signal for topological
  classification, offering an inexpensive pre-screening tool to prioritise candidate
  materials for further investigation.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7222236545
url: https://doi.org/10.83080/rejost.vol6no9.354
discovered_at: '2026-10-19'
tags: *id001
---

# Machine\-Learning Classification of Topological Materials Using Crystallographic and Compositional Descriptors for Pre\-DFT Screening

**Autores:** Sammy S\. Dan; Joseph Bassey Emah; Sylvester Andrew Ekong

**Data:** 2026-10-15 · **Tipo:** article

## Resumo

Identifying topological insulators and semimetals among inorganic crystalline materials traditionally requires density functional theory \(DFT\) calculations with spin–orbit coupling, a computationally expensive process that limits high\-throughput screening\. This study examined whether machine learning models trained on ground\-state crystallographic and compositional descriptors, obtainable without DFT or space\-group information, could reliably classify materials as topologically non\-trivial, trivial, or semimetallic\. A dataset of 1,391 labelled crystalline entries \(230 semimetal, 781 topological, 380 trivial\), curated from the Inorganic Crystal Structure Database and the Topological Quantum Chemistry database, was cleaned, including manual correction, via direct ICSD lookup, of a systematic lattice\-parameter data\-entry artefact \(an Excel auto\-fill error that had propagated a single genuine c\-parameter value across 1,208 rows, identified by cross\-validation against unit\-cell volume\), prior to a further, now pipeline\-integrated audit that removed 47 true\-duplicate ICSD entries and attempted live TQC API resolution of 10 conflicting\-label ICSD groups, none of which returned a match, so the first\-encountered row was conservatively retained in each case \(net reduction from 1,450 to 1,391 entries\), and used to engineer 31 structural and compositional features motivated by the physics of spin\-orbit\-coupling\-driven band inversion\. Six classifiers, Random Forest, XGBoost, LightGBM, Support Vector Machine, an Artificial Neural Network, and a soft\-voting Ensemble, were trained and optimised using nested stratified cross\-validation, Bayesian hyperparameter search, and Synthetic Minority Oversampling Technique \(SMOTE\)\-based class rebalancing applied strictly within each training fold\. XGBoost produced the highest observed test\-set performance \(macro\-F1 of 0\.744, accuracy of 78\.1%, macro\-AUC\-ROC of 0\.896\), narrowly ahead of LightGBM \(macro\-F1 0\.721, accuracy 74\.9%, macro\-AUC\-ROC 0\.887\), though the difference was not statistically significant \(McNemar&\#x27;s test, p = 1\.000, Bonferroni\-corrected\); LightGBM was retained as the primary model for interpretability and screening on the basis of its lower cross\-validation variance and better\-behaved post\-hoc probability calibration\. Shapley Additive exPlanations \(SHAP\), permutation, and impurity\-based feature importance analyses converged on a consistent predictor hierarchy: number of constituent elements, mean ionisation potential, electronegativity range, maximum atomic number, and mean atomic radius, corroborated by polymorph\-level diagnostics providing evidence that the model exploits structural, not merely compositional, information in most cases, although structural signal proved insufficient in at least one hard case\. Applied to the full dataset, LightGBM ranked 424 entries as Tier 1 \(P\(Topological\) ≥ 0\.80\) high\-confidence topological predictions within the labelled dataset, of which 419 corresponded to already\-known topological labels — a precision of 98\.8% against known labels \(retrospective validation precision, not prospective discovery precision\)\. Interpretability analysis was also used as a data\-quality diagnostic, motivating a closer investigation that, together with cross\-validation against unit\-cell volume and a subsequent ICSD/TQC provenance audit, uncovering and correcting a latent artefact in an earlier version of the model&\#x27;s most important feature\. These findings demonstrate that pre\-DFT structural and compositional descriptors carry physically plausible and interpretable predictive signal for topological classification, offering an inexpensive pre\-screening tool to prioritise candidate materials for further investigation\.

[Consultar publicação](<https://doi.org/10.83080/rejost.vol6no9.354>)
