---
module: 109
type: "module"
n_genes: 43
n_plus: 43
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2643696367740631
label: "immediate early"
label_source: "control"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 109

*immediate early · 43 genes (single-armed) · [[Module 109.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **immediate early** (control, q 2e-15; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | immediate early | control | 9/43 | 158 | 2e-15 |
| + | immediate early | control | 9/43 | 158 | 2e-15 |
| all | NGF-stimulated transcription | reactome | 9/43 | 90.2 | 7e-13 |
| + | NGF-stimulated transcription | reactome | 9/43 | 90.2 | 7e-13 |
| + | TNF-alpha signaling via NF-kB | hallmark | 13/43 | 24.2 | 6e-12 |
| all | TNF-alpha signaling via NF-kB | hallmark | 13/43 | 24.2 | 6e-12 |
| all | Nuclear Events (kinase and transcription factor activation) | reactome | 9/43 | 55.4 | 7e-11 |
| + | Nuclear Events (kinase and transcription factor activation) | reactome | 9/43 | 55.4 | 7e-11 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 108), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+13.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+7.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+4.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+4.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+4.2, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+3.5); [[Panobinostat (drug)]] 0.5 µM (+3.4, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.1); [[PH-797804 (drug)]] 5 µM (+1.7); [[Filgotinib (drug)]] 5 µM (+1.2); [[PF-06260933 (drug)]] 5 µM (+1.1); [[GSK1059615 (drug)]] 0.5 µM (+1.0) (24 in all, 18 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)
- Lower it: [[Trametinib (drug)]] 5 µM (-4.4, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-4.3); [[Cobimetinib (drug)]] 5 µM (-3.9); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-3.8); [[Trametinib (drug)]] 0.05 µM (-3.8); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.6); [[Trametinib (drug)]] 0.5 µM (-3.6); [[Ponatinib (drug)]] 5 µM (-3.6); [[Cobimetinib (drug)]] 0.5 µM (-2.8); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (-2.6); [[Binimetinib (drug)]] 5 µM (-2.6) (43 in all, 12 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[SK-MEL-2 (line)]], [[C32 (line)]], [[MIA PaCa-2 (line)]], [[NCI-H1573 (line)]], [[PANC-1 (line)]], [[HS-578T (line)]], [[HEC-1-A (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 19 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[IER2]] | NGF-stimulated transcription | +0.72 |
| 2 | [[MCL1]] | NGF-stimulated transcription | +0.63 |
| 3 | [[HES1]] | immediate early | +0.63 |
| 4 | [[CSRNP1]] | immediate early | +0.61 |
| 5 | [[ERCC1]] | NGF-stimulated transcription | +0.61 |
| 6 | [[ASTL]] | NGF-stimulated transcription | +0.61 |
| 7 | [[NR4A1]] | NGF-stimulated transcription | +0.60 |
| 8 | [[SYAP1]] | immediate early | +0.60 |
| 9 | [[BTBD19]] | immediate early | +0.60 |
| 10 | [[PLEKHG2]] | immediate early | +0.58 |
| 11 | [[TRIB1]] | immediate early | +0.57 |
| 12 | [[ARC]] | immediate early | +0.57 |
| 13 | [[RALY]] | immediate early | +0.55 |
| 14 | [[SGMS2]] | NGF-stimulated transcription | +0.54 |
| 15 | [[ZFP36]] | NGF-stimulated transcription | +0.53 |

## + arm (43)

| Gene | Projection | Name |
|---|---|---|
| [[EGR1]] | 0.932 | early growth response 1 |
| [[EGR3]] | 0.915 | early growth response 3 |
| [[EGR2]] | 0.913 | early growth response 2 |
| [[IER2]] | 0.886 | immediate early response 2 |
| [[FOS]] | 0.815 | Fos proto-oncogene, AP-1 transcription factor subunit |
| [[MCL1]] | 0.807 | MCL1 apoptosis regulator, BCL2 family member |
| [[ASTL]] | 0.799 | astacin like metalloendopeptidase |
| [[ERCC1]] | 0.797 | ERCC excision repair 1, endonuclease non-catalytic subunit |
| [[JUNB]] | 0.786 | JunB proto-oncogene, AP-1 transcription factor subunit |
| [[CSRNP1]] | 0.759 | cysteine and serine rich nuclear protein 1 |
| [[NR4A1]] | 0.755 | nuclear receptor subfamily 4 group A member 1 |
| [[PLEKHG2]] | 0.743 | pleckstrin homology and RhoGEF domain containing G2 |
| [[BTBD19]] | 0.740 | BTB domain containing 19 |
| [[TRIB1]] | 0.721 | tribbles pseudokinase 1 |
| [[SYAP1]] | 0.708 | synapse associated protein 1 |
| [[HES1]] | 0.701 | hes family bHLH transcription factor 1 |
| [[FOSB]] | 0.691 | FosB proto-oncogene, AP-1 transcription factor subunit |
| [[ARC]] | 0.684 | activity regulated cytoskeleton associated protein |
| [[RALY]] | 0.681 | RALY heterogeneous nuclear ribonucleoprotein |
| [[ETV3]] | 0.657 | ETS variant transcription factor 3 |
| [[SGMS2]] | 0.649 | sphingomyelin synthase 2 |
| [[VGF]] | 0.648 | VGF nerve growth factor inducible |
| [[ZFP36]] | 0.634 | ZFP36 zinc finger CCCH-type |
| [[MAFF]] | 0.631 | MAF bZIP transcription factor F |
| [[BCL2L12]] | 0.627 | BCL2 like 12 |
| [[TADA3]] | 0.627 | transcriptional adaptor 3 |
| [[EFNB2]] | 0.615 | ephrin B2 |
| [[KBTBD2]] | 0.608 | kelch repeat and BTB domain containing 2 |
| [[STX10]] | 0.600 | syntaxin 10 |
| [[TRA2B]] | 0.592 | transformer 2 beta homolog |
| [[RASD1]] | 0.584 | ras related dexamethasone induced 1 |
| [[GNL1]] | 0.576 | G protein nucleolar 1 |
| [[DCUN1D3]] | 0.573 | defective in cullin neddylation 1 domain containing 3 |
| [[MIR23AHG]] | 0.557 | miR-23a/27a/24-2 cluster host gene |
| [[VPS37A]] | -0.498 | VPS37A subunit of ESCRT-I |
| [[INO80C]] | 0.487 | INO80 complex subunit C |
| [[VMP1]] | 0.468 | vacuole membrane protein 1 |
| [[RGL1]] | 0.426 | ral guanine nucleotide dissociation stimulator like 1 |
| [[TAF10]] | 0.384 | TATA-box binding protein associated factor 10 |
| [[FLOT1]] | 0.383 | flotillin 1 |
| [[MAGEA4-AS1]] | 0.359 | MAGEA4 antisense RNA 1 |
| [[GJB2]] | 0.358 | gap junction protein beta 2 |
| [[GSEC]] | -0.346 | G-quadruplex forming sequence containing lncRNA |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 109; `graph/modules.parquet` — module == 109; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [108] (drug-dose × line)
