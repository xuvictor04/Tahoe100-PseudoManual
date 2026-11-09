---
module: 162
type: "module"
n_genes: 26
n_plus: 26
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3318413197994232
label: "estrogen response late"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 162

*estrogen response late · 26 genes (single-armed) · [[Module 162.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **estrogen response late** (hallmark, q 0.006; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | estrogen response late | hallmark | 5/26 | 16.2 | 0.006 |
| + | estrogen response late | hallmark | 5/26 | 16.2 | 0.006 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 161), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+12.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+9.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+8.4, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+7.4); [[Belinostat (drug)]] 5 µM (+7.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+5.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+5.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+4.5, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+4.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+3.8, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+2.1); [[HI-TOPK-032 (drug)]] 5 µM (+1.8); [[Ipatasertib (drug)]] 0.5 µM (+1.8); [[Auranofin (drug)]] 5 µM (+1.3); [[Tucidinostat (drug)]] 0.05 µM (+1.2); [[Glycyrrhizic acid (drug)]] 0.05 µM (+1.2); [[Vilanterol (drug)]] 0.5 µM (+1.1); [[Thymol (drug)]] 0.5 µM (+1.1); [[9-ING-41 (drug)]] 0.5 µM (+1.1) (29 in all, 16 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.7); [[Trametinib (drug)]] 5 µM (-2.7, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-2.1); [[Trametinib (drug)]] 0.05 µM (-2.0); [[Trametinib (drug)]] 0.5 µM (-1.9); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.7); [[Cobimetinib (drug)]] 5 µM (-1.7); [[Binimetinib (drug)]] 5 µM (-1.7); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-1.6); [[Bimiralisib (drug)]] 5 µM (-1.6); [[RMC-6236 (drug)]] 5 µM (-1.5) (27 in all, 6 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[NCI-H2347 (line)]], [[NCI-H2030 (line)]], [[NCI-H1573 (line)]], [[AsPC-1 (line)]], [[SW1417 (line)]], [[CFPAC-1 (line)]], [[J82 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 1 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[PLEKHO2]] | estrogen response late | +0.52 |

## + arm (26)

| Gene | Projection | Name |
|---|---|---|
| [[DUSP2]] | 0.819 | dual specificity phosphatase 2 |
| [[EPHB3]] | 0.747 | EPH receptor B3 |
| [[SOX13]] | 0.741 | SRY-box transcription factor 13 |
| [[PLEKHO2]] | 0.734 | pleckstrin homology domain containing O2 |
| [[HIVEP3]] | 0.728 | HIVEP zinc finger 3 |
| [[ADGRE5]] | 0.715 | adhesion G protein-coupled receptor E5 |
| [[NKD2]] | 0.699 | NKD inhibitor of Wnt signaling pathway 2 |
| [[NTMT1]] | 0.677 | N-terminal Xaa-Pro-Lys N-methyltransferase 1 |
| [[MAP3K14]] | 0.661 | mitogen-activated protein kinase kinase kinase 14 |
| [[SHH]] | 0.660 | sonic hedgehog signaling molecule |
| [[NRARP]] | 0.645 | NOTCH regulated ankyrin repeat protein |
| [[AREG]] | 0.642 | amphiregulin |
| [[CLCC1]] | -0.632 | chloride channel CLIC like 1 |
| [[KCNK5]] | 0.629 | potassium two pore domain channel subfamily K member 5 |
| [[BCORL1]] | 0.627 | BCL6 corepressor like 1 |
| [[TRIM15]] | 0.620 | tripartite motif containing 15 |
| [[VDR]] | 0.606 | vitamin D receptor |
| [[NCKAP5L]] | 0.603 | NCK associated protein 5 like |
| [[BIK]] | 0.598 | BCL2 interacting killer |
| [[TESC]] | 0.596 | tescalcin |
| [[SLC9A3R1]] | 0.596 | NHERF family PDZ scaffold protein 1 |
| [[TMEM251]] | 0.582 | lysosomal enzyme trafficking factor |
| [[NAB2]] | 0.574 | NGFI-A binding protein 2 |
| [[EEPD1]] | 0.522 | endonuclease/exonuclease/phosphatase family domain containing 1 |
| [[TDRP]] | 0.496 | testis development related protein |
| [[LMO3]] | -0.449 | LIM domain only 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 162; `graph/modules.parquet` — module == 162; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [161] (drug-dose × line)
