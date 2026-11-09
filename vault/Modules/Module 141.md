---
module: 141
type: "module"
n_genes: 33
n_plus: 33
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "TNF-alpha signaling via NF-kB"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 141

*TNF-alpha signaling via NF-kB · 33 genes (single-armed) · [[Module 141.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **TNF-alpha signaling via NF-kB** (hallmark, q 9e-05; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | TNF-alpha signaling via NF-kB | hallmark | 7/33 | 17.0 | 9e-05 |
| + | TNF-alpha signaling via NF-kB | hallmark | 7/33 | 17.0 | 9e-05 |
| all | RAC3 GTPase cycle | reactome | 4/33 | 21.2 | 0.015 |
| + | RAC3 GTPase cycle | reactome | 4/33 | 21.2 | 0.015 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 140), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+7.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.6); [[Homoharringtonine (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+2.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+2.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+2.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+2.1, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+2.1); [[Ipatasertib (drug)]] 0.5 µM (+1.3); [[Harringtonine (drug)]] 0.05 µM (+1.1); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.1); [[4EGI-1 (drug)]] 5 µM (+1.1) (18 in all, 12 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)
- Lower it: [[Trametinib (drug)]] 5 µM (-5.3, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-4.8); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-4.6); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-4.5); [[Cobimetinib (drug)]] 5 µM (-4.4); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-4.4); [[Binimetinib (drug)]] 5 µM (-3.9); [[Binimetinib (drug)]] 0.5 µM (-3.9); [[Trametinib (drug)]] 0.05 µM (-3.8); [[Cobimetinib (drug)]] 0.5 µM (-3.7); [[Ponatinib (drug)]] 5 µM (-3.4) (43 in all, 10 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[HOP62 (line)]], [[PANC-1 (line)]], [[J82 (line)]], [[NCI-H460 (line)]], [[NCI-H1573 (line)]], [[MIA PaCa-2 (line)]], [[HEC-1-A (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 4 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[EPHA2]] | TNF-alpha signaling via NF-kB | +0.59 |
| 2 | [[GALE]] | TNF-alpha signaling via NF-kB | +0.53 |
| 3 | [[MYEOV]] | TNF-alpha signaling via NF-kB | +0.52 |
| 4 | [[PLK3]] | TNF-alpha signaling via NF-kB | +0.51 |

## + arm (33)

| Gene | Projection | Name |
|---|---|---|
| [[EPHA2]] | 0.872 | EPH receptor A2 |
| [[MAP2K3]] | 0.820 | mitogen-activated protein kinase kinase 3 |
| [[MYEOV]] | 0.801 | myeloma overexpressed |
| [[LINC00659]] | 0.798 | long independently transcribed non-coding RNA 659 |
| [[EPHA2-AS1]] | 0.783 | EPHA2 antisense RNA 1 |
| [[DUSP5]] | 0.777 | dual specificity phosphatase 5 |
| [[PLK3]] | 0.776 | polo like kinase 3 |
| [[SH2D3A]] | 0.764 | SH2 domain containing 3A |
| [[GALE]] | 0.751 | UDP-galactose-4-epimerase |
| [[EHD1]] | 0.727 | EH domain containing 1 |
| [[VASP]] | 0.703 | vasodilator stimulated phosphoprotein |
| [[BAIAP2L1]] | 0.692 | BAR/IMD domain containing adaptor protein 2 like 1 |
| [[LINC02320]] | 0.680 | long independently transcribed non-coding RNA 2320 |
| [[VPS37B]] | 0.658 | VPS37B subunit of ESCRT-I |
| [[PTPRN2]] | 0.658 | protein tyrosine phosphatase receptor type N2 |
| [[ZG16B]] | 0.650 | zymogen granule protein 16B |
| [[SLC25A45]] | 0.634 | solute carrier family 25 member 45 |
| [[LSR]] | 0.632 | lipolysis stimulated lipoprotein receptor |
| [[TRNP1]] | 0.631 | TMF1 regulated nuclear protein 1 |
| [[SDC4]] | 0.624 | syndecan 4 |
| [[PMEPA1]] | 0.621 | prostate transmembrane protein, androgen induced 1 |
| [[JAG1]] | 0.619 | jagged canonical Notch ligand 1 |
| [[BCL2L1-AS1]] | 0.606 | BCL2L1 antisense RNA 1 |
| [[TNFAIP8]] | 0.587 | TNF alpha induced protein 8 |
| [[DIO3OS]] | 0.565 | DIO3 opposite strand upstream RNA |
| [[LRCH1]] | 0.561 | leucine rich repeats and calponin homology domain containing 1 |
| [[MFSD2A]] | 0.503 | MFSD2 lysolipid transporter A, lysophospholipid |
| [[CYSTM1]] | 0.484 | cysteine rich transmembrane module containing 1 |
| [[MYO15B]] | 0.482 | myosin XVB |
| [[ARHGAP26]] | 0.476 | Rho GTPase activating protein 26 |
| [[DUSP7]] | 0.469 | dual specificity phosphatase 7 |
| [[PRKCA]] | 0.464 | protein kinase C alpha |
| [[CHST15]] | 0.456 | carbohydrate sulfotransferase 15 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 141; `graph/modules.parquet` — module == 141; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [140] (drug-dose × line)
