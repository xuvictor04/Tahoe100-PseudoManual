---
module: 185
type: "module"
n_genes: 20
n_plus: 20
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 185

*20 genes (single-armed) · [[Module 185.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 184), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+4.6, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+4.3, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+3.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+2.6); [[Selinexor (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+2.5, ⚠ cell-cycle shift); [[Bimiralisib (drug)]] 5 µM (+2.5); [[TAK-901 (drug)]] 0.05 µM (+2.2); [[GSK1059615 (drug)]] 5 µM (+2.1); [[Cobimetinib (drug)]] 5 µM (+2.1); [[Sapanisertib (drug)]] 5 µM (+2.1); [[Belumosudil (drug)]] 5 µM (+2.0); [[Dapagliflozin (drug)]] 0.05 µM (+2.0); [[Trametinib (drug)]] 0.05 µM (+1.9); [[XRK3F2 (drug)]] 5 µM (+1.9) (104 in all, 21 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-8.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-8.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-7.9, ⚠ toxic; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-7.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-6.7, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-5.8, ⚠ transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-5.5); [[Niclosamide (olamine) (drug)]] 5 µM (-5.2, ⚠ toxic; cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-5.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.0, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-3.5); [[Vilanterol (drug)]] 5 µM (-2.5); [[Vinblastine (sulfate) (drug)]] 5 µM (-2.3); [[Peretinoin (drug)]] 0.5 µM (-2.2); [[Homoharringtonine (drug)]] 0.05 µM (-2.1); [[Niclosamide (olamine) (drug)]] 0.5 µM (-1.9); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (-1.9); [[Mebendazole (drug)]] 5 µM (-1.8); [[Topotecan (hydrochloride) (drug)]] 0.05 µM (-1.8) (84 in all, 28 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[C32 (line)]], [[MIA PaCa-2 (line)]], [[NCI-H23 (line)]], [[SW480 (line)]], [[KATO III (line)]], [[NCI-H460 (line)]], [[J82 (line)]]

## + arm (20)

| Gene | Projection | Name |
|---|---|---|
| [[CDKAL1]] | 0.857 | CDKAL1 threonylcarbamoyladenosine tRNA methylthiotransferase |
| [[ULK4]] | 0.816 | unc-51 like kinase 4 |
| [[INVS]] | 0.785 | inversin |
| [[IFT43]] | 0.779 | intraflagellar transport 43 |
| [[FARS2]] | 0.767 | phenylalanyl-tRNA synthetase 2, mitochondrial |
| [[IPO11]] | 0.766 | importin 11 |
| [[VTI1A]] | 0.755 | vesicle transport through interaction with t-SNAREs 1A |
| [[VPS13B]] | 0.739 | vacuolar protein sorting 13 homolog B |
| [[TASP1]] | 0.725 | taspase 1 |
| [[LINC00630]] | 0.723 | long independently transcribed non-coding RNA 630 |
| [[FTO]] | 0.722 | FTO alpha-ketoglutarate dependent dioxygenase |
| [[FAM172A]] | 0.654 | ARB2 cotranscriptional regulator A |
| [[ANAPC10]] | 0.639 | anaphase promoting complex subunit 10 |
| [[NSMCE2]] | 0.629 | NSE2 SUMO ligase component of SMC5/6 complex |
| [[RSRC1]] | 0.624 | arginine and serine rich coiled-coil 1 |
| [[POU5F2]] | 0.585 | POU domain class 5, transcription factor 2 |
| [[KATNIP]] | 0.564 | katanin interacting protein |
| [[SLC25A26]] | 0.546 | solute carrier family 25 member 26 |
| [[FBXO36]] | 0.514 | F-box protein 36 |
| [[SCAPER]] | 0.495 | S-phase cyclin A associated protein in the ER |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 185; `graph/modules.parquet` — module == 185; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [184] (drug-dose × line)
