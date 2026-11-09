---
module: 91
type: "module"
n_genes: 49
n_plus: 49
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "HDR through Homologous Recombination (HRR)"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 091

*HDR through Homologous Recombination (HRR) · 49 genes (single-armed) · [[Module 091.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **HDR through Homologous Recombination (HRR)** (reactome, q 0.001; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | HDR through Homologous Recombination (HRR) | reactome | 5/49 | 22.6 | 0.001 |
| + | HDR through Homologous Recombination (HRR) | reactome | 5/49 | 22.6 | 0.001 |
| + | Resolution of D-loop Structures through Holliday Junction Intermediates | reactome | 4/49 | 36.2 | 0.002 |
| all | Resolution of D-loop Structures through Holliday Junction Intermediates | reactome | 4/49 | 36.2 | 0.002 |
| all | Resolution of D-Loop Structures | reactome | 4/49 | 35.2 | 0.002 |
| + | Resolution of D-Loop Structures | reactome | 4/49 | 35.2 | 0.002 |
| + | HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA) | reactome | 5/49 | 15.5 | 0.008 |
| all | HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA) | reactome | 5/49 | 15.5 | 0.008 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 90), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+10.6, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+8.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+7.2, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.1); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+3.8, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.8, ⚠ toxic; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (+3.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 0.5 µM (+2.0); [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM (+1.9); [[Ponatinib (drug)]] 5 µM (+1.6); [[Irinotecan (hydrochloride) (drug)]] 5 µM (+1.5); [[Ponatinib (drug)]] 0.5 µM (+1.4); [[Retinoic acid (drug)]] 0.05 µM (+1.3); [[Cytarabine (hydrochloride) (drug)]] 0.05 µM (+1.3); [[Topotecan (hydrochloride) (drug)]] 0.05 µM (+1.2); [[HI-TOPK-032 (drug)]] 0.05 µM (+1.1) (43 in all, 29 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Bortezomib (drug)]] 0.05 µM (-2.4, ⚠ cell-cycle shift); [[palbociclib (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.7); [[Tucidinostat (drug)]] 5 µM (-1.7); [[Niclosamide (olamine) (drug)]] 0.5 µM (-1.7); [[Tucidinostat (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Artesunate (drug)]] 5 µM (-1.5, ⚠ cell-cycle shift); [[palbociclib (drug)]] 5 µM (-1.4); [[Sapanisertib (drug)]] 0.05 µM (-1.4, ⚠ cell-cycle shift); [[Neratinib (maleate) (drug)]] 0.5 µM (-1.3, ⚠ cell-cycle shift); [[palbociclib (drug)]] 0.05 µM (-1.2); [[Neratinib (maleate) (drug)]] 5 µM (-1.2); [[BAY1125976 (drug)]] 5 µM (-1.1); [[Auranofin (drug)]] 0.5 µM (-1.0); [[Terfenadine (drug)]] 5 µM (-1.0) (17 in all, 8 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[J82 (line)]], [[SW480 (line)]], [[PANC-1 (line)]], [[RKO (line)]], [[SW1417 (line)]], [[HS-578T (line)]], [[NCI-H460 (line)]], [[NCI-H2347 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 32 candidates, 1 with an alert ⚠; shown: the 15 strongest.*

| # | Gene | Set | Mean cos | Alert |
|---|---|---|---|---|
| 1 | [[ESCO2]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.77 |  |
| 2 | [[ZNF724]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.70 |  |
| 3 | [[KIF24]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.70 |  |
| 4 | [[FAM111A]] | HDR through Homologous Recombination (HRR) | +0.70 |  |
| 5 | [[MASTL]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.70 |  |
| 6 | [[REXO5]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.69 |  |
| 7 | [[USP1]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.68 |  |
| 8 | [[ZNF695]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.67 |  |
| 9 | [[ESPL1]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.66 |  |
| 10 | [[ZNF726]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.62 |  |
| 11 | [[ZNF736]] | Regulation of endogenous retroelements by KRAB-ZFP proteins | +0.62 |  |
| 12 | [[MGME1]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.62 |  |
| 13 | [[ZNF100]] | Regulation of endogenous retroelements by KRAB-ZFP proteins | +0.60 |  |
| 14 | [[ZFHX3-AS1]] | Resolution of D-loop Structures through Holliday Junction Intermediates | +0.60 |  |
| 15 | [[C5orf34]] | Regulation of endogenous retroelements by KRAB-ZFP proteins | +0.59 |  |

*⚠ 1 of its 49 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (49)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[BRCA2]] | 0.886 | BRCA2 DNA repair associated |  |
| [[ZNF724]] | 0.885 | zinc finger protein 724 |  |
| [[ESCO2]] | 0.824 | establishment of sister chromatid cohesion N-acetyltransferase 2 |  |
| [[C1orf112]] | 0.815 | FIGNL1 interacting regulator of recombination and mitosis |  |
| [[KIF24]] | 0.812 | kinesin family member 24 |  |
| [[ZNF695]] | 0.810 | zinc finger protein 695 |  |
| [[ZNF85]] | 0.800 | zinc finger protein 85 |  |
| [[ESPL1]] | 0.799 | extra spindle pole bodies like 1, separase |  |
| [[REXO5]] | 0.798 | RNA exonuclease 5 |  |
| [[HROB]] | 0.797 | homologous recombination factor with OB-fold |  |
| [[GEN1]] | 0.796 | GEN1 structure-specific endonuclease |  |
| [[MASTL]] | 0.791 | microtubule associated serine/threonine kinase like |  |
| [[FAM111A]] | 0.763 | FAM111 trypsin like peptidase A |  |
| [[MGME1]] | 0.756 | mitochondrial genome maintenance exonuclease 1 |  |
| [[RMI1]] | 0.751 | RecQ mediated genome instability 1 |  |
| [[ZNF100]] | 0.747 | zinc finger protein 100 |  |
| [[ZNF714]] | 0.731 | zinc finger protein 714 |  |
| [[C5orf34]] | 0.730 | chromosome 5 open reading frame 34 |  |
| [[USP1]] | 0.730 | ubiquitin specific peptidase 1 |  |
| [[ZNF726]] | 0.727 | zinc finger protein 726 |  |
| [[ZNF66]] | 0.706 | zinc finger protein 66 |  |
| [[ZFHX3-AS1]] | 0.700 | ZFHX3 antisense RNA 1 |  |
| [[ZNF107]] | 0.694 | zinc finger protein 107 |  |
| [[ZNF93]] | 0.681 | zinc finger protein 93 |  |
| [[RHNO1]] | 0.668 | RAD9-HUS1-RAD1 interacting nuclear orphan 1 |  |
| [[HIRIP3]] | 0.651 | HIRA interacting protein 3 |  |
| [[ZNF273]] | 0.648 | zinc finger protein 273 |  |
| [[ZNF257]] | 0.641 | zinc finger protein 257 |  |
| [[THSD8]] | 0.641 | thrombospondin type 1 domain containing 8 | ⚠ only flagged evidence |
| [[ZNF486]] | 0.628 | zinc finger protein 486 |  |
| [[ZNF43]] | 0.607 | zinc finger protein 43 |  |
| [[CSTF3-DT]] | 0.599 | CSTF3 divergent transcript |  |
| [[SMC1B]] | 0.590 | structural maintenance of chromosomes 1B |  |
| [[C10orf88B]] | 0.586 | C10orf88B (pseudogene) |  |
| [[APOBEC3A]] | 0.572 | apolipoprotein B mRNA editing enzyme catalytic subunit 3A |  |
| [[APOBEC3B]] | 0.561 | apolipoprotein B mRNA editing enzyme catalytic subunit 3B |  |
| [[FBF1]] | 0.557 | Fas binding factor 1 |  |
| [[RBM15]] | 0.556 | RNA binding motif protein 15 |  |
| [[DLEU2]] | 0.545 | deleted in lymphocytic leukemia 2 |  |
| [[ZNF90]] | 0.529 | zinc finger protein 90 |  |
| [[SUZ12]] | 0.510 | SUZ12 polycomb repressive complex 2 subunit |  |
| [[ZNF736]] | 0.478 | zinc finger protein 736 |  |
| [[ZNF92]] | 0.461 | zinc finger protein 92 |  |
| [[ZNF675]] | 0.446 | zinc finger protein 675 |  |
| [[ZNF680]] | 0.426 | zinc finger protein 680 |  |
| [[PAGR1]] | 0.419 | PAXIP1 associated glutamate rich protein 1 |  |
| [[TMEM107]] | 0.413 | transmembrane protein 107 |  |
| [[ZNF138]] | 0.374 | zinc finger protein 138 |  |
| [[ZNF738]] | 0.361 | zinc finger protein 738 |  |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 91; `graph/modules.parquet` — module == 91; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [90] (drug-dose × line)
