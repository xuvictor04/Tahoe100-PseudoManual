---
module: 218
type: "module"
n_genes: 12
n_plus: 12
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 218

*12 genes (single-armed) · [[Module 218.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 217), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+3.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+2.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+2.6); [[Pitavastatin (Calcium) (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+2.5); [[Thymol (drug)]] 0.5 µM (+2.2); [[PF-06260933 (drug)]] 5 µM (+2.1); [[Medroxyprogesterone acetate (drug)]] 0.5 µM (+1.7); [[Belinostat (drug)]] 0.5 µM (+1.7, ⚠ cell-cycle shift); [[Vilanterol (drug)]] 0.5 µM (+1.5); [[Lactate (calcium) (drug)]] 0.5 µM (+1.4); [[Posaconazole (drug)]] 5 µM (+1.3); [[Tirabrutinib (drug)]] 0.5 µM (+1.3); [[HI-TOPK-032 (drug)]] 5 µM (+1.3) (32 in all, 6 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-8.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-6.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-6.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-6.0, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-5.9, ⚠ toxic; cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-5.9, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-5.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-5.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-5.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-4.8, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-3.9); [[Ixazomib citrate (drug)]] 0.5 µM (-3.1); [[Ponatinib (drug)]] 5 µM (-2.3); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.2); [[Glycyrrhizic acid (drug)]] 0.5 µM (-2.0); [[Cobimetinib (drug)]] 5 µM (-1.8); [[PH-797804 (drug)]] 5 µM (-1.7); [[Epirubicin (hydrochloride) (drug)]] 0.5 µM (-1.7); [[Homoharringtonine (drug)]] 0.05 µM (-1.6); [[Harringtonine (drug)]] 0.05 µM (-1.6) (54 in all, 33 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[A-172 (line)]], [[HS-578T (line)]], [[LOX-IMVI (line)]], [[hTERT-HPNE (line)]], [[RPMI-7951 (line)]], [[SNU-423 (line)]], [[MIA PaCa-2 (line)]]

## + arm (12)

| Gene | Projection | Name |
|---|---|---|
| [[METRNL]] | 0.788 | meteorin like, glial cell differentiation regulator |
| [[SPATA2L]] | 0.780 | spermatogenesis associated 2 like |
| [[OGG1]] | 0.773 | 8-oxoguanine DNA glycosylase |
| [[ASL]] | 0.768 | argininosuccinate lyase |
| [[PRKCD]] | 0.761 | protein kinase C delta |
| [[MLXIP]] | 0.761 | MLX interacting protein |
| [[NUMBL]] | 0.750 | NUMB like endocytic adaptor protein |
| [[MOB3A]] | 0.721 | MOB kinase activator 3A |
| [[TMEM44]] | 0.642 | transmembrane protein 44 |
| [[EHD2]] | 0.635 | EH domain containing 2 |
| [[CD99P1-1]] | 0.505 | — |
| [[C8orf58]] | 0.396 | chromosome 8 open reading frame 58 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 218; `graph/modules.parquet` — module == 218; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [217] (drug-dose × line)
