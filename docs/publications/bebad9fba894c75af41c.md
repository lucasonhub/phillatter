---
title: 'ReViT-RF: A hybrid ResNet-50–Vision Transformer with a Radiomic Feature Fusion
  framework for lung tumor classification and TNM-based stage prediction using CT
  images'
authors:
- Shobharani DA
- Ramesh Naik B
date: '2026-10-12'
type: article
category: &id001
- Inteligência Artificial
doi: 10.1371/journal.pone.0359211
abstract: 'Lung cancer is one of the leading causes of cancer-related mortality worldwide,
  emphasizing the need for accurate, automated, and clinically interpretable diagnostic
  systems. Although existing deep learning (DL) models have achieved promising performance
  in classifying lung nodules as benign or malignant, most approaches are limited
  to binary classification and provide insufficient support for detailed tumor characterization
  and TNM staging. Furthermore, conventional convolutional neural networks (CNNs)
  are effective in extracting local morphological features but often fail to capture
  long-range spatial dependencies. In contrast, transformer-based models can learn
  global contextual information but may compromise fine-grained local feature representation.
  To address these limitations, this study proposes a hybrid ResNet-50-Vision Transformer
  with Radiomic Feature Fusion (ReViT-RF) framework for lung tumor classification
  and component-wise TNM stage prediction using thoracic computed tomography (CT)
  images from the publicly available Lung Image Database Consortium and Image Database
  Resource Initiative (LIDC-IDRI) dataset. The primary clinical objectives of the
  proposed framework are to: (i) classify pulmonary nodules as benign or malignant,
  and (ii) predict individual TNM components, including primary tumor extent (T),
  lymph node involvement (N), and metastatic status (M) for malignant cases. To improve
  tumor visibility and image quality, CT images are initially preprocessed using Contrast-Limited
  Adaptive Histogram Equalization (CLAHE) and intensity normalization. The proposed
  ReViT-RF architecture integrates the complementary advantages of ResNet-50 and Vision
  Transformer (ViT) for comprehensive feature learning. The CNN branch extracts local
  morphological, textural, and structural characteristics, whereas the transformer
  branch captures long-range spatial relationships and global contextual dependencies.
  In addition, handcrafted radiomic features, including shape, size, texture, and
  spatial descriptors, are fused with deep features to provide clinically meaningful
  information for accurate TNM component prediction. The dataset is divided into training,
  validation, and testing subsets using an 80:10:10 ratio, with data augmentation
  applied only to the training set to prevent information leakage. Experimental results
  demonstrate that the proposed framework achieves an accuracy of 97.62% for benign-malignant
  classification, along with high precision, recall, and F1-score values. Moreover,
  independent prediction of TNM components provides detailed stage-related information
  rather than relying on a single aggregated stage label, enabling more precise tumor
  assessment and clinical decision support. Furthermore, explainability analysis using
  Gradient-weighted Class Activation Mapping (Grad-CAM) identifies the critical tumor
  regions contributing to model predictions, improving interpretability and enhancing
  clinician confidence. Overall, by combining hybrid deep feature extraction, radiomic
  feature fusion, component-wise TNM stage prediction, and explainable AI analysis,
  the proposed ReViT-RF framework provides a reliable, comprehensive, and clinically
  interpretable solution for automated lung tumor analysis.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221551471
url: https://doi.org/10.1371/journal.pone.0359211
discovered_at: '2026-10-16'
tags: *id001
---

# ReViT\-RF: A hybrid ResNet\-50–Vision Transformer with a Radiomic Feature Fusion framework for lung tumor classification and TNM\-based stage prediction using CT images

**Autores:** Shobharani DA; Ramesh Naik B

**Data:** 2026-10-12 · **Tipo:** article

## Resumo

Lung cancer is one of the leading causes of cancer\-related mortality worldwide, emphasizing the need for accurate, automated, and clinically interpretable diagnostic systems\. Although existing deep learning \(DL\) models have achieved promising performance in classifying lung nodules as benign or malignant, most approaches are limited to binary classification and provide insufficient support for detailed tumor characterization and TNM staging\. Furthermore, conventional convolutional neural networks \(CNNs\) are effective in extracting local morphological features but often fail to capture long\-range spatial dependencies\. In contrast, transformer\-based models can learn global contextual information but may compromise fine\-grained local feature representation\. To address these limitations, this study proposes a hybrid ResNet\-50\-Vision Transformer with Radiomic Feature Fusion \(ReViT\-RF\) framework for lung tumor classification and component\-wise TNM stage prediction using thoracic computed tomography \(CT\) images from the publicly available Lung Image Database Consortium and Image Database Resource Initiative \(LIDC\-IDRI\) dataset\. The primary clinical objectives of the proposed framework are to: \(i\) classify pulmonary nodules as benign or malignant, and \(ii\) predict individual TNM components, including primary tumor extent \(T\), lymph node involvement \(N\), and metastatic status \(M\) for malignant cases\. To improve tumor visibility and image quality, CT images are initially preprocessed using Contrast\-Limited Adaptive Histogram Equalization \(CLAHE\) and intensity normalization\. The proposed ReViT\-RF architecture integrates the complementary advantages of ResNet\-50 and Vision Transformer \(ViT\) for comprehensive feature learning\. The CNN branch extracts local morphological, textural, and structural characteristics, whereas the transformer branch captures long\-range spatial relationships and global contextual dependencies\. In addition, handcrafted radiomic features, including shape, size, texture, and spatial descriptors, are fused with deep features to provide clinically meaningful information for accurate TNM component prediction\. The dataset is divided into training, validation, and testing subsets using an 80:10:10 ratio, with data augmentation applied only to the training set to prevent information leakage\. Experimental results demonstrate that the proposed framework achieves an accuracy of 97\.62% for benign\-malignant classification, along with high precision, recall, and F1\-score values\. Moreover, independent prediction of TNM components provides detailed stage\-related information rather than relying on a single aggregated stage label, enabling more precise tumor assessment and clinical decision support\. Furthermore, explainability analysis using Gradient\-weighted Class Activation Mapping \(Grad\-CAM\) identifies the critical tumor regions contributing to model predictions, improving interpretability and enhancing clinician confidence\. Overall, by combining hybrid deep feature extraction, radiomic feature fusion, component\-wise TNM stage prediction, and explainable AI analysis, the proposed ReViT\-RF framework provides a reliable, comprehensive, and clinically interpretable solution for automated lung tumor analysis\.

[Consultar publicação](<https://doi.org/10.1371/journal.pone.0359211>)
