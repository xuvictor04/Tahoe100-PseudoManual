---
module: 211
type: "module"
n_genes: 13
n_plus: 13
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 211

*13 genes (single-armed) · [[Module 211.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 210), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM (+5.2, ⚠ unreliable plate only); [[Panobinostat (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.7, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+3.8, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+3.8); [[Ixazomib citrate (drug)]] 5 µM (+3.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+3.6, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Neratinib (maleate) (drug)]] 5 µM (+2.7); [[Belinostat (drug)]] 0.5 µM (+2.7, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+2.5); [[Ixazomib citrate (drug)]] 0.5 µM (+2.5); [[Brivudine (drug)]] 5 µM (+2.5); [[EX229 (drug)]] 5 µM (+2.3); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.3); [[Peretinoin (drug)]] 5 µM (+2.2); [[5-Azacytidine (drug)]] 5 µM (+2.2); [[Cobimetinib (drug)]] 5 µM (+2.0) (77 in all, 18 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM (-8.8, ⚠ toxic; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-8.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-7.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-6.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-6.4, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-6.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-5.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-5.5, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-5.2, ⚠ transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-4.5, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-3.6); [[Vilanterol (drug)]] 5 µM (-2.2); [[Harringtonine (drug)]] 0.05 µM (-2.0); [[Topotecan (hydrochloride) (drug)]] 0.05 µM (-1.9); [[XRK3F2 (drug)]] 0.5 µM (-1.5); [[Sulfatinib (drug)]] 5 µM (-1.5); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (-1.4); [[Pemigatinib (drug)]] 0.05 µM (-1.4); [[Arbutin (drug)]] 5 µM (-1.4); [[Irinotecan (drug)]] 5 µM (-1.4) (52 in all, 25 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[LOX-IMVI (line)]], [[PANC-1 (line)]], [[KATO III (line)]], [[RKO (line)]], [[MIA PaCa-2 (line)]], [[A-427 (line)]], [[LoVo (line)]]

## + arm (13)

| Gene | Projection | Name |
|---|---|---|
| [[ERC1]] | 0.830 | ELKS/RAB6-interacting/CAST family member 1 |
| [[RABGAP1L]] | 0.800 | RAB GTPase activating protein 1 like |
| [[EXOC6B]] | 0.781 | exocyst complex component 6B |
| [[SUPT3H]] | 0.778 | SPT3 homolog, SAGA and STAGA complex component |
| [[ADK]] | 0.710 | adenosine kinase |
| [[SLC39A11]] | 0.680 | solute carrier family 39 member 11 |
| [[TMEM241]] | 0.669 | solute carrier family 35 member D4 |
| [[MAP4]] | 0.627 | microtubule associated protein 4 |
| [[CTIF]] | 0.617 | cap binding complex dependent translation initiation factor |
| [[ZFAND3]] | 0.548 | zinc finger AN1-type containing 3 |
| [[GNPNAT1]] | 0.539 | glucosamine-phosphate N-acetyltransferase 1 |
| [[CLEC16A]] | 0.497 | C-type lectin domain containing 16A |
| [[KCNG1]] | 0.483 | potassium voltage-gated channel modifier subfamily G member 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 211; `graph/modules.parquet` — module == 211; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [210] (drug-dose × line)
