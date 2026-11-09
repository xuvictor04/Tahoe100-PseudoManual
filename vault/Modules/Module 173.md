---
module: 173
type: "module"
n_genes: 23
n_plus: 23
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 173

*23 genes (single-armed) · [[Module 173.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 172), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+16.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+7.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+7.3, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+4.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+3.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.9, ⚠ transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+2.6, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.0); [[Homoharringtonine (drug)]] 0.05 µM (+2.0); [[Auranofin (drug)]] 5 µM (+1.4); [[Pentoxifylline (drug)]] 5 µM (+1.3); [[Pentoxifylline (drug)]] 0.5 µM (+1.3); [[Harringtonine (drug)]] 0.05 µM (+1.2); [[Dihydroartemisinin (drug)]] 0.5 µM (+1.0); [[Arbutin (drug)]] 0.5 µM (+1.0); [[crizotinib (drug)]] 5 µM (+1.0); [[5-Azacytidine (drug)]] 5 µM (+1.0) (28 in all, 18 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Belinostat (drug)]] 5 µM (-8.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-8.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-7.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-6.6, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-5.0, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-4.5); [[Brivudine (drug)]] 5 µM (-3.7); [[Tucidinostat (drug)]] 0.5 µM (-3.0, ⚠ cell-cycle shift); [[Ribociclib (drug)]] 0.05 µM (-2.2, ⚠ unreliable plate only; position not correctable); [[Verteporfin (drug)]] 5 µM (-1.7); [[Doxycycline (monohydrate) (drug)]] 0.5 µM (-1.5); [[Radotinib (drug)]] 5 µM (-1.5); [[Loperamide (hydrochloride) (drug)]] 0.5 µM (-1.3); [[Almonertinib (hydrochloride) (drug)]] 0.05 µM (-1.3); [[Bosentan (hydrate) (drug)]] 0.5 µM (-1.2); [[Loperamide (hydrochloride) (drug)]] 5 µM (-1.1); [[Brivudine (drug)]] 0.5 µM (-1.1) (19 in all, 8 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[PANC-1 (line)]], [[NCI-H1573 (line)]], [[A498 (line)]], [[HOP62 (line)]], [[NCI-H1792 (line)]], [[A-172 (line)]], [[HS-578T (line)]]

## + arm (23)

| Gene | Projection | Name |
|---|---|---|
| [[SCAF1]] | 0.856 | SR-related CTD associated factor 1 |
| [[MEPCE]] | 0.852 | methylphosphate capping enzyme |
| [[AKT1S1]] | 0.849 | AKT1 substrate 1 |
| [[MED12]] | 0.841 | mediator complex subunit 12 |
| [[FBRS]] | 0.837 | fibrosin |
| [[BRPF3]] | 0.833 | bromodomain and PHD finger containing 3 |
| [[ARFGAP2]] | 0.824 | ARF GTPase activating protein 2 |
| [[C19orf54]] | 0.802 | actin maturation protease |
| [[PAF1]] | 0.764 | PAF1 component of Paf1/RNA polymerase II complex |
| [[UBAP2L]] | 0.751 | ubiquitin associated protein 2 like |
| [[SP2]] | 0.728 | Sp2 transcription factor |
| [[CHD3]] | 0.723 | chromodomain helicase DNA binding protein 3 |
| [[PMF1]] | 0.721 | polyamine modulated factor 1 |
| [[RGL2]] | 0.720 | ral guanine nucleotide dissociation stimulator like 2 |
| [[PAN2]] | 0.716 | poly(A) specific ribonuclease subunit PAN2 |
| [[DHX38]] | 0.701 | DEAH-box helicase 38 |
| [[KDM6B]] | 0.697 | lysine demethylase 6B |
| [[STK11]] | 0.657 | serine/threonine kinase 11 |
| [[TRIM8]] | 0.619 | tripartite motif containing 8 |
| [[MEGF8]] | 0.618 | multiple EGF like domains 8 |
| [[HMGN2]] | 0.601 | high mobility group nucleosomal binding domain 2 |
| [[BRD4]] | 0.586 | bromodomain containing 4 |
| [[HMGN2P5]] | 0.562 | high mobility group nucleosomal binding domain 2 pseudogene 5 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 173; `graph/modules.parquet` — module == 173; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [172] (drug-dose × line)
