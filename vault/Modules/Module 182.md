---
module: 182
type: "module"
n_genes: 21
n_plus: 11
n_minus: 10
arms_opposite: true
mean_cos_between_arms: -0.3972937762737274
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 182

*21 genes (11 in the + arm, 10 in the − arm) · [[Module 182.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 181), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Dinaciclib (drug)]] 0.5 µM (+8.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Selinexor (drug)]] 5 µM (+8.1, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+7.7, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+5.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+5.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Radotinib (drug)]] 5 µM (+5.8); [[Tucidinostat (drug)]] 5 µM (+5.7); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+5.1); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+3.8); [[Trametinib (drug)]] 0.5 µM (+3.6); [[PH-797804 (drug)]] 5 µM (+3.5); [[Flumatinib (mesylate) (drug)]] 5 µM (+3.4); [[Brivudine (drug)]] 5 µM (+3.4); [[Cabozantinib (S-malate) (drug)]] 5 µM (+3.1); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+3.0) (151 in all, 32 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-9.9, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-6.9); [[Harringtonine (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-3.3, ⚠ cell-cycle shift); [[Lactate (calcium) (drug)]] 0.5 µM (-3.3); [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM (-3.2); [[Estrone sulfate (potassium) (drug)]] 5 µM (-3.1); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.8, ⚠ cell-cycle shift); [[Tirabrutinib (drug)]] 0.5 µM (-2.6); [[PF-06260933 (drug)]] 5 µM (-2.6); [[Esmolol (hydrochloride) (drug)]] 5 µM (-2.6); [[Diphenhydramine (drug)]] 0.5 µM (-2.6); [[TAK-733 (drug)]] 0.05 µM (-2.5); [[Ranolazine (drug)]] 0.05 µM (-2.4) (124 in all, 16 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[PANC-1 (line)]], [[J82 (line)]], [[LoVo (line)]], [[SK-MEL-2 (line)]], [[KATO III (line)]], [[SW480 (line)]], [[A549 (line)]]

## + arm (11)

| Gene | Projection | Name |
|---|---|---|
| [[KDM1A]] | 0.841 | lysine demethylase 1A |
| [[HDAC2]] | 0.706 | histone deacetylase 2 |
| [[RYK]] | 0.705 | receptor like tyrosine kinase |
| [[SNRPA1]] | 0.702 | small nuclear ribonucleoprotein polypeptide A' |
| [[PEBP1]] | 0.700 | phosphatidylethanolamine binding protein 1 |
| [[SLC25A30]] | 0.664 | solute carrier family 25 member 30 |
| [[PPTC7]] | 0.618 | protein phosphatase targeting COQ7 |
| [[DUBR]] | 0.616 | DPPA2 upstream binding RNA |
| [[GNAI1]] | 0.596 | G protein subunit alpha i1 |
| [[RNF138]] | 0.512 | ring finger protein 138 |
| [[SEPTIN7]] | 0.433 | septin 7 |

## − arm (10)

| Gene | Projection | Name |
|---|---|---|
| [[TUT7]] | -0.837 | terminal uridylyl transferase 7 |
| [[SETX]] | -0.814 | senataxin |
| [[CRK]] | -0.751 | CRK proto-oncogene, adaptor protein |
| [[SLC35C2]] | -0.723 | solute carrier family 35 member H1 |
| [[SLC30A7]] | -0.661 | solute carrier family 30 member 7 |
| [[PROSER3]] | -0.631 | proline and serine rich 3 |
| [[OPA3]] | -0.626 | outer mitochondrial membrane lipid metabolism regulator OPA3 |
| [[ENDOV]] | -0.612 | endonuclease V |
| [[WDR26]] | -0.545 | WD repeat domain 26 |
| [[PNKP]] | -0.521 | polynucleotide kinase 3'-phosphatase |

## Data

- `graph/nodes.parquet` — module == 182; `graph/modules.parquet` — module == 182; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [181] (drug-dose × line)
