---
module: 146
type: "module"
n_genes: 31
n_plus: 26
n_minus: 5
arms_opposite: true
mean_cos_between_arms: -0.3007030785083771
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 146

*31 genes (26 in the + arm, 5 in the − arm) · [[Module 146.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 145), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Ponatinib (drug)]] 5 µM (+6.3); [[Radotinib (drug)]] 5 µM (+6.1); [[Cabozantinib (S-malate) (drug)]] 5 µM (+5.1); [[Ponatinib (drug)]] 0.5 µM (+4.2); [[Tucidinostat (drug)]] 0.5 µM (+4.1, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.05 µM (+3.8); [[Tucidinostat (drug)]] 5 µM (+3.8); [[Anethole trithione (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+3.5); [[Trametinib (drug)]] 5 µM (+3.4, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+3.3); [[Clobetasol propionate (drug)]] 0.05 µM (+3.2); [[Flumatinib (mesylate) (drug)]] 5 µM (+3.2) (105 in all, 10 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-21.1, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-12.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-12.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-11.3, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-11.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-11.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-11.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-9.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-8.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-8.7, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-6.6); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-5.9); [[PF-06260933 (drug)]] 5 µM (-3.5); [[5-Azacytidine (drug)]] 5 µM (-2.9); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-2.1); [[Vilanterol (drug)]] 5 µM (-2.1); [[Peretinoin (drug)]] 5 µM (-2.0); [[Rimonabant (drug)]] 5 µM (-2.0); [[Belzutifan (drug)]] 5 µM (-1.9); [[TAK-733 (drug)]] 0.05 µM (-1.9) (110 in all, 35 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]], [[SW480 (line)]], [[A498 (line)]], [[PANC-1 (line)]], [[LOX-IMVI (line)]], [[C32 (line)]], [[HOP62 (line)]]

## + arm (26)

| Gene | Projection | Name |
|---|---|---|
| [[TADA1]] | 0.817 | transcriptional adaptor 1 |
| [[HSF2]] | 0.800 | heat shock transcription factor 2 |
| [[MLLT10]] | 0.769 | MLLT10 histone lysine methyltransferase DOT1L cofactor |
| [[NAA16]] | 0.760 | N-alpha-acetyltransferase 16, NatA auxiliary subunit |
| [[RAVER2]] | 0.731 | ribonucleoprotein, PTB binding 2 |
| [[KCTD3]] | 0.728 | potassium channel tetramerization domain containing 3 |
| [[TNRC6A]] | 0.719 | trinucleotide repeat containing adaptor 6A |
| [[PDS5B]] | 0.707 | PDS5 cohesin associated factor B |
| [[REV1]] | 0.697 | REV1 DNA directed polymerase |
| [[ACVR1B]] | 0.696 | activin A receptor type 1B |
| [[ZFP64]] | 0.693 | ZFP64 zinc finger protein |
| [[SYBU]] | 0.680 | syntabulin |
| [[NOD1]] | 0.677 | nucleotide binding oligomerization domain containing 1 |
| [[SLC5A4-AS1]] | 0.662 | SLC5A4 antisense RNA 1 |
| [[ZNF592]] | 0.637 | zinc finger protein 592 |
| [[EEF2K]] | 0.631 | eukaryotic elongation factor 2 kinase |
| [[TMEM218]] | 0.621 | transmembrane protein 218 |
| [[GATA4]] | 0.619 | GATA binding protein 4 |
| [[MACIR]] | 0.595 | macrophage immunometabolism regulator |
| [[NELFA]] | 0.582 | negative elongation factor complex member A |
| [[LRP3]] | 0.544 | LDL receptor related protein 3 |
| [[COPS8-DT]] | 0.480 | COPS8 divergent transcript |
| [[SULT1A1]] | 0.471 | sulfotransferase family 1A member 1 |
| [[C1orf115]] | 0.430 | chromosome 1 open reading frame 115 |
| [[PRDX6-AS1]] | 0.417 | PRDX6 antisense RNA 1 |
| [[MTMR8]] | 0.410 | myotubularin related protein 8 |

## − arm (5)

| Gene | Projection | Name |
|---|---|---|
| [[ATP6V1D]] | -0.706 | ATPase H+ transporting V1 subunit D |
| [[SCYL2]] | -0.500 | SCY1 like pseudokinase 2 |
| [[RB1]] | -0.471 | RB transcriptional corepressor 1 |
| [[RP2]] | -0.468 | RP2 activator of ARL3 GTPase |
| [[CLTA]] | -0.454 | clathrin light chain A |

## Data

- `graph/nodes.parquet` — module == 146; `graph/modules.parquet` — module == 146; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [145] (drug-dose × line)
