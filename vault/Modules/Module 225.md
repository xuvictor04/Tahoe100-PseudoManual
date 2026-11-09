---
module: 225
type: "module"
n_genes: 9
n_plus: 9
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 225

*9 genes (single-armed) · [[Module 225.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 224), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Bimiralisib (drug)]] 5 µM (+3.1); [[Ponatinib (drug)]] 5 µM (+2.9); [[Trametinib (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Sapanisertib (drug)]] 5 µM (+2.3); [[Bimiralisib (drug)]] 0.05 µM (+2.3); [[Trametinib (drug)]] 0.05 µM (+2.2); [[Temsirolimus (drug)]] 5 µM (+2.2); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.1, ⚠ cell-cycle shift); [[Cabozantinib (S-malate) (drug)]] 5 µM (+2.0); [[Ouabain (Octahydrate) (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[XRK3F2 (drug)]] 5 µM (+2.0); [[BAY1125976 (drug)]] 5 µM (+1.9); [[AZD-8055 (drug)]] 5 µM (+1.9) (77 in all, 17 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM (-12.4, ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.5 µM (-11.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-11.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-10.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-9.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-9.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-7.7, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-6.1, ⚠ toxic; cell-cycle shift); [[Abemaciclib (drug)]] 5 µM (-6.0); [[Harringtonine (drug)]] 0.5 µM (-6.0, ⚠ cell-cycle shift); [[TAK-733 (drug)]] 5 µM (-5.9); [[Auranofin (drug)]] 5 µM (-5.9); [[c-Kit-IN-1 (drug)]] 5 µM (-5.5); [[Abemaciclib (drug)]] 0.5 µM (-4.9); [[venetoclax (drug)]] 5 µM (-4.7); [[EX229 (drug)]] 5 µM (-4.6); [[Ixazomib citrate (drug)]] 0.5 µM (-4.4); [[EX229 (drug)]] 0.5 µM (-4.3); [[Belzutifan (drug)]] 5 µM (-4.0) (84 in all, 28 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C32 (line)]], [[MIA PaCa-2 (line)]], [[SNU-1 (line)]], [[SW480 (line)]], [[NCI-H1792 (line)]], [[NCI-H23 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]]

## + arm (9)

| Gene | Projection | Name |
|---|---|---|
| [[FOXN3]] | 0.823 | forkhead box N3 |
| [[TNRC6B]] | 0.809 | trinucleotide repeat containing adaptor 6B |
| [[CNNM2]] | 0.796 | cyclin and CBS domain divalent metal cation transport mediator 2 |
| [[ZBTB44]] | 0.779 | zinc finger and BTB domain containing 44 |
| [[PAN3]] | 0.745 | poly(A) specific ribonuclease subunit PAN3 |
| [[PDPR]] | 0.699 | pyruvate dehydrogenase phosphatase regulatory subunit |
| [[LCORL]] | 0.634 | ligand dependent nuclear receptor corepressor like |
| [[CNNM3]] | 0.596 | cyclin and CBS domain divalent metal cation transport mediator 3 |
| [[IGF1R]] | 0.488 | insulin like growth factor 1 receptor |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 225; `graph/modules.parquet` — module == 225; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [224] (drug-dose × line)
