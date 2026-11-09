---
module: 201
type: "module"
n_genes: 15
n_plus: 15
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "Kidney development"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 201

*Kidney development · 15 genes (single-armed) · [[Module 201.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **Kidney development** (reactome, q 0.003; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Kidney development | reactome | 3/15 | 81.5 | 0.003 |
| + | Kidney development | reactome | 3/15 | 81.5 | 0.003 |
| all | Activation of anterior HOX genes in hindbrain development during early embryogenesis | reactome | 3/15 | 49.4 | 0.012 |
| all | Activation of HOX genes during differentiation | reactome | 3/15 | 49.4 | 0.012 |
| + | Activation of anterior HOX genes in hindbrain development during early embryogenesis | reactome | 3/15 | 49.4 | 0.012 |
| + | Activation of HOX genes during differentiation | reactome | 3/15 | 49.4 | 0.012 |
| all | Formation of the nephric duct | reactome | 2/15 | 134 | 0.035 |
| + | Formation of the nephric duct | reactome | 2/15 | 134 | 0.035 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 200), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+12.1, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+3.5); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.0, ⚠ toxic; cell-cycle shift); [[Ponatinib (drug)]] 0.5 µM (+2.4); [[Cabozantinib (S-malate) (drug)]] 5 µM (+2.1); [[Radotinib (drug)]] 5 µM (+2.1); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[NG25 (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+1.9); [[Entrectinib (drug)]] 5 µM (+1.4); [[Filgotinib (drug)]] 5 µM (+1.4); [[XRK3F2 (drug)]] 0.5 µM (+1.4); [[Omeprazole (drug)]] 0.5 µM (+1.3); [[Bimiralisib (drug)]] 0.5 µM (+1.3) (49 in all, 16 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-7.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-7.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-5.7, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-4.9, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-4.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-4.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-4.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-3.5, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.5, ⚠ unreliable plate only); [[Ixazomib citrate (drug)]] 0.5 µM (-2.7); [[Peretinoin (drug)]] 5 µM (-2.5); [[Belumosudil (drug)]] 5 µM (-2.3); [[Auranofin (drug)]] 5 µM (-2.0); [[Vinblastine (sulfate) (drug)]] 5 µM (-2.0); [[Homoharringtonine (drug)]] 0.05 µM (-1.9); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-1.8); [[Peretinoin (drug)]] 0.5 µM (-1.7); [[5-Azacytidine (drug)]] 5 µM (-1.6); [[Abemaciclib (drug)]] 5 µM (-1.6) (52 in all, 23 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]], [[HT-29 (line)]], [[C32 (line)]], [[A-172 (line)]], [[SHP-77 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 6 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[HOXA10]] | Kidney development | +0.65 |
| 2 | [[HOXA5]] | Kidney development | +0.63 |
| 3 | [[HOXA3]] | Kidney development | +0.57 |
| 4 | [[HOXA9]] | Kidney development | +0.56 |
| 5 | [[HOXB3]] | Kidney development | +0.51 |
| 6 | [[HOXB5]] | Kidney development | +0.51 |

## + arm (15)

| Gene | Projection | Name |
|---|---|---|
| [[HOXB5]] | 0.872 | homeobox B5 |
| [[HOXA3]] | 0.837 | homeobox A3 |
| [[HOXB3]] | 0.833 | homeobox B3 |
| [[HOXB6]] | 0.817 | homeobox B6 |
| [[HOXB4]] | 0.794 | homeobox B4 |
| [[HOXA10]] | 0.790 | homeobox A10 |
| [[HOXA6]] | 0.752 | homeobox A6 |
| [[HOXA5]] | 0.744 | homeobox A5 |
| [[HOXA9]] | 0.708 | homeobox A9 |
| [[SATB2-AS1]] | 0.698 | SATB2 antisense RNA 1 |
| [[TIAL1]] | 0.688 | TIA1 cytotoxic granule associated RNA binding protein like 1 |
| [[ACP6]] | 0.668 | acid phosphatase 6, lysophosphatidic |
| [[HOXA11]] | 0.601 | homeobox A11 |
| [[HOXB8]] | 0.598 | homeobox B8 |
| [[TSHZ1]] | 0.587 | teashirt zinc finger homeobox 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 201; `graph/modules.parquet` — module == 201; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [200] (drug-dose × line)
