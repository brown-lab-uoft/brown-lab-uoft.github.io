---
title: "Regularized indirect learning improves phage display ligand discovery"
authors:
- "Joseph S. Brown"
- "Yitong Tseo"
- "Michael A. Lee"
- "Jeffrey Y.-K. Wong"
- "Soojung Yang"
- "Yehlin Cho"
- "Chae Rin Kim"
- "Andrei Loas"
- "Ratmir Derda"
- "Rafael Gomez-Bombarelli"
- "Bradley L. Pentelute"
date: "2023-01-01T00:00:00Z"
publishDate: "2023-01-01T00:00:00Z"
publication_types: ["article"]
publication: "*ChemRxiv*"
doi: "10.26434/chemrxiv-2023-jpwvn"
abstract: "Phage display is commonly employed for the discovery of high affinity ligands to biomolecular targets. However, ranking the discovered ligands for their affinity and specificity to the target is obscured by genetic amplification bias and amplification of target-unrelated phage, resulting in inefficient experimental validation and potentially intractable discovery. Here, we describe the use of indirect machine learning (ML) to improve the efficient discovery of target-specific peptide ligands from next-generation sequencing (NGS) data. We combine peptide sequence information (input) with experimental fitness scores (output) of the individual peptide performance across the rounds of bio-panning in a bidirectional long short-term memory (BiLSTM) architecture. Because the fitness scores contain bias, we use regularization to facilitate limited indirect learning and effectively process the peptide sequence information, while still using the predicted fitness scores to rank the peptides. Peptides containing high-affinity binding motifs to our target were ranked by the regularized model more than threefold higher, compared to any combination of experimental fitness scores. Baseline models of random forest (RF) and k-nearest neighbor (KNN) demonstrated slightly lower performance but also demonstrated the importance of regularization. However, the BiLSTM model emerged as the most robust, as it was less sensitive to the peptide representation and the specific fitness score used. Shapley residue analysis generated interpretable structure-activity-relationship (SAR) by providing insight into predicted affinity-driving residues and physicochemical properties across the entire peptide and as well as at motif-specific positions. We expect that this approach will elucidate high-affinity ligands against a multitude of targets, vastly improving the discovery capability of phage display."
tags:
- Machine learning
- Phage display
featured: false
projects: []
slides: ""
---
