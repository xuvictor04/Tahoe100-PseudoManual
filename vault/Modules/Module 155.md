---
module: 155
type: "module"
n_genes: 29
n_plus: 29
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3545643985271454
label: "MyD88 deficiency (TLR2/4)"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 155

*MyD88 deficiency (TLR2/4) · 29 genes (single-armed) · [[Module 155.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **MyD88 deficiency (TLR2/4)** (reactome, q 1e-05; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | MyD88 deficiency (TLR2/4) | reactome | 4/29 | 139 | 1e-05 |
| + | MyD88 deficiency (TLR2/4) | reactome | 4/29 | 139 | 1e-05 |
| all | IRAK4 deficiency (TLR2/4) | reactome | 4/29 | 130 | 1e-05 |
| + | IRAK4 deficiency (TLR2/4) | reactome | 4/29 | 130 | 1e-05 |
| + | Regulation of TLR by endogenous ligand | reactome | 4/29 | 122 | 2e-05 |
| all | Regulation of TLR by endogenous ligand | reactome | 4/29 | 122 | 2e-05 |
| all | Diseases associated with the TLR signaling cascade | reactome | 4/29 | 77.0 | 1e-04 |
| + | Diseases associated with the TLR signaling cascade | reactome | 4/29 | 77.0 | 1e-04 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 154), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+9.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+8.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+7.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+6.2); [[Tucidinostat (drug)]] 0.5 µM (+4.0, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+2.7, ⚠ toxic; cell-cycle shift); [[XRK3F2 (drug)]] 0.5 µM (+2.5); [[Docetaxel (drug)]] 0.05 µM (+2.5, ⚠ transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.5); [[Ipatasertib (drug)]] 0.5 µM (+2.1); [[GSK1059615 (drug)]] 0.5 µM (+1.9); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.9); [[Bimiralisib (drug)]] 0.5 µM (+1.6); [[Clobetasol propionate (drug)]] 0.05 µM (+1.5); [[9-ING-41 (drug)]] 0.5 µM (+1.4); [[Oxaprozin (drug)]] 0.5 µM (+1.4) (68 in all, 30 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[Artesunate (drug)]] 0.5 µM (-1.8); [[Erlotinib (drug)]] 0.05 µM (-1.8); [[Lucanthone (drug)]] 0.05 µM (-1.6); [[Ouabain (Octahydrate) (drug)]] 5 µM (-1.6, ⚠ cell-cycle shift); [[Fenofibrate (drug)]] 0.05 µM (-1.5); [[Pravastatin (sodium) (drug)]] 5 µM (-1.5); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.5, ⚠ unreliable plate only); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-1.5); [[Ipatasertib (drug)]] 5 µM (-1.5); [[Clopidogrel (drug)]] 0.05 µM (-1.5); [[OTS514 (drug)]] 0.5 µM (-1.4); [[Mebendazole (drug)]] 5 µM (-1.4) (45 in all, 4 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[CHP-212 (line)]], [[BT-474 (line)]], [[NCI-H1792 (line)]], [[SW 900 (line)]], [[SW48 (line)]], [[NCI-H23 (line)]], [[AN3 CA (line)]], [[SW480 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 16 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[SERPINB3]] | MyD88 deficiency (TLR2/4) | +0.80 |
| 2 | [[SERPINB4]] | MyD88 deficiency (TLR2/4) | +0.79 |
| 3 | [[GSDMC]] | MyD88 deficiency (TLR2/4) | +0.74 |
| 4 | [[LINC01440]] | MyD88 deficiency (TLR2/4) | +0.68 |
| 5 | [[CES1]] | MyD88 deficiency (TLR2/4) | +0.66 |
| 6 | [[FGB]] | Antimicrobial peptides | +0.66 |
| 7 | [[C2CD4A]] | MyD88 deficiency (TLR2/4) | +0.64 |
| 8 | [[FLRT3]] | MyD88 deficiency (TLR2/4) | +0.63 |
| 9 | [[SERPINA1]] | MyD88 deficiency (TLR2/4) | +0.61 |
| 10 | [[CDH3]] | MyD88 deficiency (TLR2/4) | +0.59 |
| 11 | [[P2RY6]] | MyD88 deficiency (TLR2/4) | +0.56 |
| 12 | [[GPR141]] | MyD88 deficiency (TLR2/4) | +0.54 |
| 13 | [[SPTSSB]] | Antimicrobial peptides | +0.53 |
| 14 | [[UBE2QL1]] | MyD88 deficiency (TLR2/4) | +0.52 |
| 15 | [[MUC5AC]] | Antimicrobial peptides | +0.51 |

## + arm (29)

| Gene | Projection | Name |
|---|---|---|
| [[S100A9]] | 0.943 | S100 calcium binding protein A9 |
| [[S100A8]] | 0.913 | S100 calcium binding protein A8 |
| [[SERPINB3]] | 0.911 | serpin family B member 3 |
| [[SERPINB4]] | 0.907 | serpin family B member 4 |
| [[FGB]] | 0.864 | fibrinogen beta chain |
| [[LINC01440]] | 0.835 | long independently transcribed non-coding RNA 1440 |
| [[GSDMC]] | 0.829 | gasdermin C |
| [[CES1]] | 0.817 | carboxylesterase 1 |
| [[C2CD4A]] | 0.772 | C2 calcium dependent domain containing 4A |
| [[FLRT3]] | 0.772 | fibronectin leucine rich transmembrane protein 3 |
| [[FGG]] | 0.698 | fibrinogen gamma chain |
| [[CDH3]] | 0.695 | cadherin 3 |
| [[SPTSSB]] | 0.688 | serine palmitoyltransferase small subunit B |
| [[SERPINA1]] | 0.681 | serpin family A member 1 |
| [[AQP3]] | 0.643 | aquaporin 3 (Gill blood group) |
| [[ADAM28]] | 0.639 | ADAM metallopeptidase domain 28 |
| [[LINC01503]] | 0.621 | long independently transcribed non-coding RNA 1503 |
| [[MUC5AC]] | 0.617 | mucin 5AC, oligomeric mucus/gel-forming |
| [[UBE2QL1]] | 0.612 | ubiquitin conjugating enzyme E2 QL1 |
| [[PI3]] | 0.607 | peptidase inhibitor 3 |
| [[GPR141]] | 0.578 | G protein-coupled receptor 141 |
| [[LURAP1]] | 0.577 | leucine rich adaptor protein 1 |
| [[PGR]] | -0.568 | progesterone receptor |
| [[P2RY6]] | 0.553 | pyrimidinergic receptor P2Y6 |
| [[SAMD5]] | 0.483 | sterile alpha motif domain containing 5 |
| [[DNAAF11]] | 0.482 | dynein axonemal assembly factor 11 |
| [[NTN4]] | 0.464 | netrin 4 |
| [[ACOXL]] | 0.326 | acyl-CoA oxidase like |
| [[OPN3]] | 0.298 | opsin 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 155; `graph/modules.parquet` — module == 155; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [154] (drug-dose × line)
