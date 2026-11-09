---
module: 200
type: "module"
n_genes: 16
n_plus: 16
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 200

*16 genes (single-armed) · [[Module 200.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 199), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Cobimetinib (drug)]] 5 µM (+3.7); [[Afatinib (drug)]] 0.5 µM (+2.7); [[Trametinib (drug)]] 0.05 µM (+2.5); [[Clobetasol propionate (drug)]] 0.05 µM (+2.5); [[Bimiralisib (drug)]] 5 µM (+2.4); [[Esmolol (hydrochloride) (drug)]] 5 µM (+2.3); [[Cobimetinib (drug)]] 0.5 µM (+2.3); [[Belumosudil (drug)]] 5 µM (+2.2); [[Demeclocycline (drug)]] 5 µM (+2.2); [[Trametinib (drug)]] 5 µM (+2.2, ⚠ cell-cycle shift); [[Alpelisib (drug)]] 0.5 µM (+2.0) (138 in all, 14 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)
- Lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM (-13.9, ⚠ toxic; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-13.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-12.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-11.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-11.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-11.7, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-11.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-10.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-9.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-9.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-6.0); [[PH-797804 (drug)]] 5 µM (-5.7); [[Ixazomib citrate (drug)]] 0.5 µM (-4.7); [[Vilanterol (drug)]] 5 µM (-3.8); [[Vinblastine (sulfate) (drug)]] 5 µM (-3.2); [[Peretinoin (drug)]] 0.5 µM (-3.0); [[Mebendazole (drug)]] 5 µM (-3.0); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-3.0); [[Topotecan (hydrochloride) (drug)]] 0.05 µM (-3.0); [[Pasireotide (acetate) (drug)]] 5 µM (-3.0) (117 in all, 39 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[LoVo (line)]], [[NCI-H460 (line)]], [[HEC-1-A (line)]], [[RKO (line)]], [[SNU-1 (line)]], [[NCI-H23 (line)]]

## + arm (16)

| Gene | Projection | Name |
|---|---|---|
| [[IMMP2L]] | 0.907 | inner mitochondrial membrane peptidase subunit 2 |
| [[FHIT]] | 0.833 | fragile histidine triad diadenosine triphosphatase |
| [[WWOX]] | 0.786 | WW domain containing oxidoreductase |
| [[EXOC4]] | 0.739 | exocyst complex component 4 |
| [[TBC1D5]] | 0.735 | TBC1 domain family member 5 |
| [[BABAM2]] | 0.730 | BRISC and BRCA1 A complex member 2 |
| [[RAD51B]] | 0.727 | RAD51 paralog B |
| [[DIAPH2]] | 0.682 | diaphanous related formin 2 |
| [[SUCLG2]] | 0.655 | succinate-CoA ligase GDP-forming subunit beta |
| [[FGGY]] | 0.611 | FGGY carbohydrate kinase domain containing |
| [[GPHN]] | 0.589 | gephyrin |
| [[ZC3H12B]] | 0.587 | zinc finger CCCH-type containing 12B |
| [[DANT2]] | 0.534 | DXZ4 associated non-coding transcript 2, distal |
| [[PAM]] | 0.488 | peptidylglycine alpha-amidating monooxygenase |
| [[ZNF438]] | 0.459 | zinc finger protein 438 |
| [[DOCK7]] | 0.438 | dedicator of cytokinesis 7 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 200; `graph/modules.parquet` — module == 200; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [199] (drug-dose × line)
