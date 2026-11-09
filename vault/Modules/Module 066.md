---
module: 66
type: "module"
n_genes: 74
n_plus: 74
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "epithelial mesenchymal transition"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 066

*epithelial mesenchymal transition · 74 genes (single-armed) · [[Module 066.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **epithelial mesenchymal transition** (hallmark, q 6e-20; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | epithelial mesenchymal transition | hallmark | 21/74 | 23.4 | 6e-20 |
| + | epithelial mesenchymal transition | hallmark | 21/74 | 23.4 | 6e-20 |
| + | Extracellular matrix organization | reactome | 16/74 | 13.5 | 6e-11 |
| all | Extracellular matrix organization | reactome | 16/74 | 13.5 | 6e-11 |
| all | Integrin cell surface interactions | reactome | 10/74 | 30.9 | 1e-09 |
| + | Integrin cell surface interactions | reactome | 10/74 | 30.9 | 1e-09 |
| + | ECM proteoglycans | reactome | 9/74 | 34.6 | 5e-09 |
| all | ECM proteoglycans | reactome | 9/74 | 34.6 | 5e-09 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 65), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 0.5 µM (+11.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+10.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+8.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+6.7); [[Tucidinostat (drug)]] 0.5 µM (+4.6, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (+3.0); [[Binimetinib (drug)]] 5 µM (+2.8); [[Cobimetinib (drug)]] 5 µM (+2.5); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.5); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.5); [[Cobimetinib (drug)]] 0.5 µM (+2.1); [[Binimetinib (drug)]] 0.5 µM (+1.9); [[Binimetinib (drug)]] 0.05 µM (+1.8); [[Elimusertib hydrochloride (drug)]] 0.05 µM (+1.8) (45 in all, 18 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Ixazomib citrate (drug)]] 5 µM (-1.7, ⚠ cell-cycle shift); [[Neratinib (maleate) (drug)]] 5 µM (-1.6); [[5-Azacytidine (drug)]] 5 µM (-1.5); [[Ixazomib citrate (drug)]] 0.5 µM (-1.5); [[Dexamethasone (drug)]] 0.5 µM (-1.4); [[Digitoxin (drug)]] 0.05 µM (-1.4, ⚠ cell-cycle shift); [[Dihydroartemisinin (drug)]] 5 µM (-1.4); [[Abemaciclib (drug)]] 5 µM (-1.4); [[BAY1125976 (drug)]] 5 µM (-1.3); [[Artesunate (drug)]] 5 µM (-1.3, ⚠ cell-cycle shift); [[Abemaciclib (drug)]] 0.5 µM (-1.2); [[Dabrafenib (drug)]] 5 µM (-1.2); [[Fenofibrate (drug)]] 0.05 µM (-1.1) (24 in all, 7 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[A-172 (line)]], [[MIA PaCa-2 (line)]], [[A498 (line)]], [[Panc 03.27 (line)]], [[PANC-1 (line)]], [[NCI-H2347 (line)]], [[SNU-423 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 20 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[COL3A1]] | Anchoring fibril formation | +0.66 |
| 2 | [[SPARC]] | Fibronectin matrix formation | +0.62 |
| 3 | [[FBN1]] | Fibronectin matrix formation | +0.60 |
| 4 | [[TGFBI]] | Fibronectin matrix formation | +0.59 |
| 5 | [[NID2]] | Fibronectin matrix formation | +0.58 |
| 6 | [[PXDN]] | Scavenging by Class A Receptors | +0.57 |
| 7 | [[ITGA4]] | Fibronectin matrix formation | +0.57 |
| 8 | [[COL4A1]] | Developmental Lineage of Pancreatic Ductal Cells | +0.56 |
| 9 | [[EFEMP1]] | angiogenesis | +0.55 |
| 10 | [[POSTN]] | Fibronectin matrix formation | +0.55 |
| 11 | [[MXRA8]] | angiogenesis | +0.55 |
| 12 | [[COL1A2]] | Signaling by PDGF | +0.55 |
| 13 | [[ANTXR1]] | Fibronectin matrix formation | +0.54 |
| 14 | [[SULF1]] | Developmental Lineage of Pancreatic Ductal Cells | +0.54 |
| 15 | [[COL5A2]] | Scavenging by Class A Receptors | +0.54 |

## + arm (74)

| Gene | Projection | Name |
|---|---|---|
| [[COL12A1]] | 0.765 | collagen type XII alpha 1 chain |
| [[LUM]] | 0.751 | lumican |
| [[MOXD1]] | 0.746 | monooxygenase DBH like 1 |
| [[POSTN]] | 0.740 | periostin |
| [[CCDC80]] | 0.739 | coiled-coil domain containing 80 |
| [[COL3A1]] | 0.717 | collagen type III alpha 1 chain |
| [[ALPK2]] | 0.703 | alpha kinase 2 |
| [[SULF1]] | 0.697 | sulfatase 1 |
| [[EFEMP1]] | 0.695 | EGF-like fibulin extracellular matrix protein 1 |
| [[THBS1]] | 0.689 | thrombospondin 1 |
| [[CHRDL1]] | 0.689 | chordin like 1 |
| [[COL1A1]] | 0.675 | collagen type I alpha 1 chain |
| [[SUSD5]] | 0.675 | sushi domain containing 5 |
| [[TGFB2]] | 0.673 | transforming growth factor beta 2 |
| [[AKR1B1]] | 0.658 | aldo-keto reductase family 1 member B |
| [[COL5A2]] | 0.657 | collagen type V alpha 2 chain |
| [[OLFML2A]] | 0.654 | olfactomedin like 2A |
| [[PALLD]] | 0.653 | palladin, cytoskeletal associated protein |
| [[SEMA3C]] | 0.646 | semaphorin 3C |
| [[MXRA8]] | 0.643 | matrix remodeling associated 8 |
| [[MYLK]] | 0.639 | myosin light chain kinase |
| [[TGFBI]] | 0.634 | transforming growth factor beta induced |
| [[CALD1]] | 0.631 | caldesmon 1 |
| [[RBM24]] | 0.628 | RNA binding motif protein 24 |
| [[DSEL]] | 0.625 | dermatan sulfate epimerase like |
| [[ROS1]] | 0.620 | ROS proto-oncogene 1, receptor tyrosine kinase |
| [[ANXA8]] | 0.610 | annexin A8 |
| [[MYL9]] | 0.603 | myosin light chain 9 |
| [[OLR1]] | 0.603 | oxidized low density lipoprotein receptor 1 |
| [[GLIPR1]] | 0.599 | GLI pathogenesis related 1 |
| [[DIO2]] | 0.598 | iodothyronine deiodinase 2 |
| [[FILIP1L]] | 0.588 | filamin A interacting protein 1 like |
| [[MYPN]] | 0.585 | myopalladin |
| [[COL4A1]] | 0.582 | collagen type IV alpha 1 chain |
| [[PHLDB2]] | 0.582 | pleckstrin homology like domain family B member 2 |
| [[TRIM55]] | 0.581 | tripartite motif containing 55 |
| [[EDIL3-DT]] | 0.578 | EDIL3 divergent transcript |
| [[KLHL5]] | 0.574 | kelch like family member 5 |
| [[FBN1]] | 0.566 | fibrillin 1 |
| [[CCDC3]] | 0.564 | coiled-coil domain containing 3 |
| [[GFRA1]] | 0.561 | GDNF family receptor alpha 1 |
| [[NRK]] | 0.558 | Nik related kinase |
| [[ARHGAP42]] | 0.555 | Rho GTPase activating protein 42 |
| [[ABLIM1]] | 0.547 | actin binding LIM protein 1 |
| [[DPYSL3]] | 0.546 | dihydropyrimidinase like 3 |
| [[PTN]] | 0.544 | pleiotrophin |
| [[THY1]] | 0.542 | Thy-1 cell surface antigen |
| [[LINC00842]] | 0.541 | long independently transcribed non-coding RNA 842 |
| [[HHIPL2]] | 0.539 | HHIP like 2 |
| [[AHR]] | 0.539 | aryl hydrocarbon receptor |
| [[SLC16A2]] | 0.535 | solute carrier family 16 member 2 |
| [[HEG1]] | 0.535 | heart development protein with EGF like domains 1 |
| [[ITGA4]] | 0.530 | integrin subunit alpha 4 |
| [[LINC02057]] | 0.526 | long independently transcribed non-coding RNA 2057 |
| [[SPARC]] | 0.517 | secreted protein acidic and cysteine rich |
| [[NID2]] | 0.516 | nidogen 2 |
| [[TRIM58]] | 0.515 | tripartite motif containing 58 |
| [[COL1A2]] | 0.509 | collagen type I alpha 2 chain |
| [[NRP2]] | 0.500 | neuropilin 2 |
| [[EYA4]] | 0.492 | EYA transcriptional coactivator and phosphatase 4 |
| [[TMEM47]] | 0.492 | transmembrane protein 47 |
| [[PXDN]] | 0.491 | peroxidasin |
| [[COL4A2]] | 0.485 | collagen type IV alpha 2 chain |
| [[ANTXR1]] | 0.479 | ANTXR cell adhesion molecule 1 |
| [[RAB31]] | 0.474 | RAB31, member RAS oncogene family |
| [[KITLG]] | 0.466 | KIT ligand |
| [[TIMP3]] | 0.442 | TIMP metallopeptidase inhibitor 3 |
| [[TMEM52B]] | 0.437 | transmembrane protein 52B |
| [[IGFBP5]] | 0.424 | insulin like growth factor binding protein 5 |
| [[AOPEP]] | 0.416 | aminopeptidase O (putative) |
| [[RASEF]] | 0.351 | RAS and EF-hand domain containing |
| [[DIRC3]] | 0.335 | disrupted in renal carcinoma 3 |
| [[LINC02384]] | 0.326 | long independently transcribed non-coding RNA 2384 |
| [[STON2]] | 0.295 | stonin 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 66; `graph/modules.parquet` — module == 66; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [65] (drug-dose × line)
