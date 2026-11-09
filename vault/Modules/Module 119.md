---
module: 119
type: "module"
n_genes: 41
n_plus: 41
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3220440149307251
label: "Mitochondrial ribosome-associated quality control"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 119

*Mitochondrial ribosome-associated quality control · 41 genes (single-armed) · [[Module 119.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Mitochondrial ribosome-associated quality control** (reactome, q 0.036; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Mitochondrial ribosome-associated quality control | reactome | 4/41 | 16.5 | 0.036 |
| + | Mitochondrial ribosome-associated quality control | reactome | 4/41 | 16.5 | 0.036 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 118), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[TAK-901 (drug)]] 5 µM (+7.1, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+5.2, ⚠ toxic; cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+4.2); [[Selinexor (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+2.9, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+2.9, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+2.5); [[Ixazomib citrate (drug)]] 5 µM (+2.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+2.4, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+1.9); [[Homoharringtonine (drug)]] 0.05 µM (+1.4); [[TAK-901 (drug)]] 0.5 µM (+1.2); [[Sapanisertib (drug)]] 0.5 µM (+1.1); [[EX229 (drug)]] 5 µM (+1.1); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.1); [[XRK3F2 (drug)]] 0.5 µM (+1.1); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.1) (32 in all, 20 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-5.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-4.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-2.5); [[Tucidinostat (drug)]] 0.5 µM (-1.8, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-1.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-1.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Fusidic acid (drug)]] 5 µM (-1.1); [[PH-797804 (drug)]] 0.05 µM (-1.1); [[BAY1125976 (drug)]] 5 µM (-1.0) (9 in all, 5 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[KATO III (line)]], [[HEC-1-A (line)]], [[PANC-1 (line)]], [[NCI-H1573 (line)]], [[RKO (line)]], [[A-427 (line)]], [[NCI-H23 (line)]]

## + arm (41)

| Gene | Projection | Name |
|---|---|---|
| [[NCBP2AS2]] | 0.871 | NCBP2 antisense 2 (head to head) |
| [[ALKBH4]] | 0.846 | alkB homolog 4, lysine demethylase |
| [[TMEM11]] | 0.841 | transmembrane protein 11 |
| [[C16orf91]] | 0.827 | ubiquinol-cytochrome c reductase complex assembly factor 4 |
| [[TIMM29]] | 0.801 | translocase of inner mitochondrial membrane 29 |
| [[RPUSD2]] | 0.801 | RNA pseudouridine synthase domain containing 2 |
| [[ADPRS]] | 0.799 | ADP-ribosylserine hydrolase |
| [[ZNF576]] | 0.781 | zinc finger protein 576 |
| [[MIEF1]] | 0.779 | mitochondrial elongation factor 1 |
| [[MRPL44]] | 0.766 | mitochondrial ribosomal protein L44 |
| [[BRPF1]] | 0.726 | bromodomain and PHD finger containing 1 |
| [[MTF1]] | 0.721 | metal regulatory transcription factor 1 |
| [[WDR53]] | 0.719 | WD repeat domain 53 |
| [[CCDC12]] | 0.715 | coiled-coil domain containing 12 |
| [[AAR2]] | 0.705 | AAR2 splicing factor |
| [[BFAR]] | 0.699 | bifunctional apoptosis regulator |
| [[EIF4E2]] | 0.693 | eukaryotic translation initiation factor 4E family member 2 |
| [[KLHL20]] | 0.692 | kelch like family member 20 |
| [[PEX11B]] | 0.679 | peroxisomal biogenesis factor 11 beta |
| [[YRDC]] | 0.669 | yrdC N6-threonylcarbamoyltransferase domain containing |
| [[MFSD5]] | 0.661 | solute carrier family 61 member 1 |
| [[GLS]] | -0.655 | glutaminase |
| [[ZNF350]] | 0.642 | zinc finger protein 350 |
| [[MRPL27]] | 0.632 | mitochondrial ribosomal protein L27 |
| [[TPRN]] | 0.617 | taperin |
| [[ZNF223]] | 0.602 | zinc finger protein 223 |
| [[MRPS11]] | 0.589 | mitochondrial ribosomal protein S11 |
| [[C19orf12]] | 0.586 | chromosome 19 open reading frame 12 |
| [[KDF1]] | 0.582 | keratinocyte differentiation factor 1 |
| [[ZBTB3]] | 0.568 | zinc finger and BTB domain containing 3 |
| [[ZNF230]] | 0.561 | zinc finger protein 230 |
| [[GTPBP10]] | 0.557 | GTP binding protein 10 |
| [[FBXO45]] | 0.555 | F-box protein 45 |
| [[CTNNA1]] | -0.537 | catenin alpha 1 |
| [[C2orf49]] | 0.524 | tRNA splicing ligase complex subunit 2 |
| [[RAMAC]] | 0.520 | RNA guanine-7 methyltransferase activating subunit |
| [[ZNF57]] | 0.482 | zinc finger protein 57 |
| [[RNF139]] | 0.440 | ring finger protein 139 |
| [[ZNF782]] | 0.438 | zinc finger protein 782 |
| [[PEX14]] | 0.436 | peroxisomal biogenesis factor 14 |
| [[C8orf88]] | -0.351 | chromosome 8 open reading frame 88 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 119; `graph/modules.parquet` — module == 119; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [118] (drug-dose × line)
