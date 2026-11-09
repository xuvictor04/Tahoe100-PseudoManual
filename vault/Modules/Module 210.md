---
module: 210
type: "module"
n_genes: 13
n_plus: 13
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.34577271342277527
label: "tRNA processing"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 210

*tRNA processing · 13 genes (single-armed) · [[Module 210.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **tRNA processing** (reactome, q 0.037; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | tRNA processing | reactome | 3/13 | 31.6 | 0.037 |
| + | tRNA processing | reactome | 3/13 | 31.6 | 0.037 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 209), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[TAK-901 (drug)]] 5 µM (+7.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+7.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+7.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+5.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+5.5, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+5.4, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+5.1); [[PH-797804 (drug)]] 5 µM (+4.8); [[Ixazomib citrate (drug)]] 0.5 µM (+4.7); [[Bortezomib (drug)]] 0.5 µM (+2.2); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.2); [[EX229 (drug)]] 5 µM (+1.8); [[Abemaciclib (drug)]] 0.5 µM (+1.7); [[Abemaciclib (drug)]] 5 µM (+1.6); [[EX229 (drug)]] 0.05 µM (+1.5); [[c-Kit-IN-1 (drug)]] 5 µM (+1.4) (40 in all, 25 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Tucidinostat (drug)]] 5 µM (-3.7); [[Tucidinostat (drug)]] 0.5 µM (-3.0, ⚠ cell-cycle shift); [[Sunitinib (drug)]] 5 µM (-1.4, ⚠ toxic); [[Filgotinib (drug)]] 5 µM (-1.3); [[Harringtonine (drug)]] 0.05 µM (-1.2); [[Entrectinib (drug)]] 5 µM (-1.2); [[Docetaxel (drug)]] 0.05 µM (-1.2, ⚠ transcription drop; cell-cycle shift); [[Futibatinib (drug)]] 5 µM (-1.1); [[Gallic acid (hydrate) (drug)]] 0.05 µM (-1.1); [[Carbamazepine (drug)]] 5 µM (-1.0); [[Celecoxib (drug)]] 0.5 µM (-1.0); [[Busulfan (drug)]] 0.05 µM (-1.0); [[Estrone sulfate (potassium) (drug)]] 5 µM (-1.0) (13 in all, 3 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[NCI-H460 (line)]], [[PANC-1 (line)]], [[MIA PaCa-2 (line)]], [[NCI-H1573 (line)]], [[NCI-H23 (line)]], [[HOP62 (line)]], [[COLO 205 (line)]]

## + arm (13)

| Gene | Projection | Name |
|---|---|---|
| [[DDX49]] | 0.828 | DEAD-box helicase 49 |
| [[NUP214]] | 0.828 | nucleoporin 214 |
| [[RTF2]] | 0.823 | replication termination factor 2 |
| [[UBE4A]] | 0.760 | ubiquitination factor E4A |
| [[MAGOH]] | 0.730 | mago homolog, exon junction complex subunit |
| [[ACOX3]] | 0.717 | acyl-CoA oxidase 3, pristanoyl |
| [[TRMT44]] | 0.705 | tRNA methyltransferase 44 homolog |
| [[ACO2]] | 0.704 | aconitase 2 |
| [[TMCO1]] | 0.666 | transmembrane and coiled-coil domains 1 |
| [[TPRKB]] | 0.652 | TP53RK binding protein |
| [[MEMO1]] | -0.639 | mediator of cell motility 1 |
| [[SPECC1]] | -0.598 | sperm antigen with calponin homology and coiled-coil domains 1 |
| [[ARHGAP10]] | -0.392 | Rho GTPase activating protein 10 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 210; `graph/modules.parquet` — module == 210; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [209] (drug-dose × line)
