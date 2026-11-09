---
module: 213
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

# Module 213

*13 genes (single-armed) · [[Module 213.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 212), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Bortezomib (drug)]] 0.05 µM (+3.1, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+3.1, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+2.7, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (+2.2, ⚠ unreliable plate only); [[NG25 (drug)]] 5 µM (+2.2, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 0.05 µM (+2.0); [[Ponatinib (drug)]] 5 µM (+1.9); [[Ponatinib (drug)]] 0.5 µM (+1.8); [[Clobetasol propionate (drug)]] 0.5 µM (+1.8); [[Ixazomib citrate (drug)]] 5 µM (+1.7, ⚠ cell-cycle shift); [[EX229 (drug)]] 5 µM (+1.6); [[Clobetasol propionate (drug)]] 0.05 µM (+1.5); [[Dapagliflozin (drug)]] 0.05 µM (+1.5); [[Medroxyprogesterone acetate (drug)]] 5 µM (+1.5); [[Afatinib (drug)]] 0.5 µM (+1.4); [[Cobimetinib (drug)]] 0.5 µM (+1.4) (41 in all, 11 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-15.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-9.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-8.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-8.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-6.5); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-5.6, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-5.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-5.5, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-5.5, ⚠ transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-4.7, ⚠ toxic; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-2.7); [[Mebendazole (drug)]] 5 µM (-1.8); [[PF-06260933 (drug)]] 5 µM (-1.7); [[Peretinoin (drug)]] 0.5 µM (-1.5); [[Infigratinib (drug)]] 0.05 µM (-1.5); [[Dimethyl fumarate (drug)]] 5 µM (-1.5); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-1.5); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.4); [[Aprepitant (drug)]] 0.05 µM (-1.4) (64 in all, 28 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[NCI-H23 (line)]], [[HEC-1-A (line)]], [[LOX-IMVI (line)]], [[NCI-H460 (line)]], [[HOP62 (line)]], [[RKO (line)]], [[SNU-423 (line)]]

## + arm (13)

| Gene | Projection | Name |
|---|---|---|
| [[MRPS9]] | 0.802 | mitochondrial ribosomal protein S9 |
| [[SHPRH]] | 0.795 | SNF2 histone linker PHD RING helicase |
| [[TAS2R14]] | 0.790 | taste 2 receptor member 14 |
| [[ACBD6]] | 0.785 | acyl-CoA binding domain containing 6 |
| [[MRPL1]] | 0.725 | mitochondrial ribosomal protein L1 |
| [[RBM26]] | 0.723 | RNA binding motif protein 26 |
| [[CWC27]] | 0.722 | CWC27 spliceosome associated cyclophilin |
| [[HDAC8]] | 0.704 | histone deacetylase 8 |
| [[TTC17]] | 0.607 | tetratricopeptide repeat domain 17 |
| [[METTL15]] | 0.584 | methyltransferase 15, mitochondrial 12S rRNA N4-cytidine |
| [[NF1]] | 0.559 | neurofibromin 1 |
| [[EIF2AK4]] | 0.548 | eukaryotic translation initiation factor 2 alpha kinase 4 |
| [[ELP4]] | 0.485 | elongator acetyltransferase complex subunit 4 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 213; `graph/modules.parquet` — module == 213; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [212] (drug-dose × line)
