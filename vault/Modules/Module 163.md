---
module: 163
type: "module"
n_genes: 26
n_plus: 26
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.5259804725646973
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 163

*26 genes (single-armed) · [[Module 163.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 162), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Niclosamide (olamine) (drug)]] 5 µM (+5.2, ⚠ toxic; cell-cycle shift); [[Belinostat (drug)]] 5 µM (+5.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+4.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+4.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (+3.8, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+3.4); [[Belinostat (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+2.9); [[Tomivosertib (drug)]] 5 µM (+1.9); [[Erlotinib (drug)]] 0.05 µM (+1.9); [[Verteporfin (drug)]] 5 µM (+1.8); [[Capivasertib (drug)]] 0.5 µM (+1.8); [[NVP-BHG712 (drug)]] 0.05 µM (+1.7); [[Irinotecan (hydrochloride) (drug)]] 0.5 µM (+1.6); [[Glycyrrhizic acid (drug)]] 0.5 µM (+1.5); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.5) (76 in all, 23 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 5 µM (-8.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-7.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-5.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-5.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.8, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-4.8); [[Homoharringtonine (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-3.4, ⚠ transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-3.3); [[Harringtonine (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.4); [[Harringtonine (drug)]] 0.05 µM (-2.4); [[Carbamazepine (drug)]] 5 µM (-2.0); [[Filgotinib (drug)]] 0.05 µM (-2.0); [[Filgotinib (drug)]] 5 µM (-1.9); [[Mifepristone (drug)]] 0.5 µM (-1.9); [[Thymol (drug)]] 5 µM (-1.9); [[GSK1059615 (drug)]] 0.5 µM (-1.8) (79 in all, 18 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H2347 (line)]], [[LoVo (line)]], [[A-172 (line)]], [[SW480 (line)]], [[LOX-IMVI (line)]], [[J82 (line)]], [[LS 180 (line)]], [[AsPC-1 (line)]]

## + arm (26)

| Gene | Projection | Name |
|---|---|---|
| [[UBE2G1]] | 0.843 | ubiquitin conjugating enzyme E2 G1 |
| [[RNF38]] | 0.839 | ring finger protein 38 |
| [[ABHD12]] | 0.834 | abhydrolase domain containing 12, lysophospholipase |
| [[MFSD14B]] | 0.813 | solute carrier family 71 member 2 |
| [[MYSM1]] | -0.806 | Myb like, SWIRM and MPN domains 1 |
| [[MFSD14CP]] | 0.791 | solute carrier family 71 member 3, pseudogene |
| [[RANBP9]] | 0.789 | RAN binding protein 9 |
| [[CCNY]] | 0.780 | cyclin Y |
| [[RAP1A]] | 0.757 | RAP1A, member of RAS oncogene family |
| [[STRN]] | 0.754 | striatin |
| [[CDC42SE2]] | 0.746 | CDC42 small effector 2 |
| [[CYTH3]] | 0.728 | cytohesin 3 |
| [[MAST2]] | 0.712 | microtubule associated serine/threonine kinase 2 |
| [[SGPP1]] | 0.699 | sphingosine-1-phosphate phosphatase 1 |
| [[SCAF4]] | 0.670 | SR-related CTD associated factor 4 |
| [[DCUN1D4]] | 0.670 | defective in cullin neddylation 1 domain containing 4 |
| [[UBP1]] | 0.646 | upstream binding protein 1 |
| [[SESTD1]] | 0.599 | SEC14 and spectrin domain containing 1 |
| [[ILKAP]] | 0.590 | ILK associated serine/threonine phosphatase |
| [[TANC1]] | 0.588 | tetratricopeptide repeat, ankyrin repeat and coiled-coil containing 1 |
| [[LRRC1]] | 0.534 | leucine rich repeat containing 1 |
| [[MBOAT1]] | 0.516 | membrane bound glycerophospholipid O-acyltransferase 1 |
| [[RHEB]] | 0.512 | Ras homolog, mTORC1 binding |
| [[TEAD2]] | 0.454 | TEA domain transcription factor 2 |
| [[GVQW3]] | 0.444 | GVQW motif containing 3 |
| [[RRAS2]] | 0.442 | RAS related 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 163; `graph/modules.parquet` — module == 163; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [162] (drug-dose × line)
