---
symbol: "PTPN13"
type: "gene"
col: 8736
ensembl_id: "ENSG00000163629"
name: "protein tyrosine phosphatase non-receptor type 13"
location: "4q21.3"
module: 9
arm: "+"
pooled_cpm: 76.33
n_lines_expressing: 40
n_dd_up: 27
n_dd_down: 12
n_dd_up_clean: 27
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PTPN13

*protein tyrosine phosphatase non-receptor type 13* — 4q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.82× (z +11.4, q 2e-27, up in 31 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.616× (z -9.2, q 2e-17, down in 28 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR17]] (+0.56, fdr 1e-05), [[RAB30]] (+0.54, fdr 1e-05), [[ANGPT1]] (+0.54, fdr 1e-05); moves opposite to [[ADGRL1-AS1]] (-0.60, fdr 4e-05), [[GHRLOS]] (-0.56, fdr 3e-05), [[MIATNB]] (-0.54, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ANGPT1]] → it (grade B ⚠); 6 go from it, the strongest it → [[LMO4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 5 with an alert ⚠; shown: the 15 strongest. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +11.4 | 2e-27 | 31/38 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +10.4 | 9e-23 | 24/38 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +9.1 | 2e-17 | 33/38 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +9.0 | 3e-17 | 30/38 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +8.9 | 9e-17 | 30/38 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +8.1 | 4e-14 | 29/38 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +7.7 | 1e-12 | 28/38 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +6.3 | 2e-08 | 26/39 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +6.1 | 5e-08 | 25/37 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +6.0 | 1e-07 | 31/39 (HT-29, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.8 | 3e-07 | 22/38 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 2e-05 | 22/38 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.28×** | +4.9 | 3e-05 | 20/40 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +4.8 | 8e-05 | 20/38 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 1e-04 | 23/37 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -9.2 | 2e-17 | 28/38 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.643×** | -7.8 | 3e-12 | 20/37 (C-33 A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.691×** | -7.0 | 4e-10 | 21/39 (H4, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.713×** | -6.2 | 9e-08 | 18/35 (A-427, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.502×** | -5.8 | 9e-07 | 19/39 (LoVo, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.838× | -4.8 | 2e-04 | 17/39 (CHP-212, LoVo, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.715×** | -4.3 | 0.001 | 17/38 (LoVo, CHP-212, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.802×** | -4.2 | 0.002 | 18/38 (NCI-H2347, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.804×** | -3.8 | 0.008 | 15/37 (LoVo, AN3 CA, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.820×** | -3.8 | 0.009 | 15/38 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.821×** | -3.8 | 0.009 | 15/38 (LoVo, CHP-212, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.7 | 0.009 | 17/39 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.829×** | -3.6 | 0.016 | 18/38 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.842× | -3.3 | 0.043 | 13/38 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.679×** | -3.2 | 0.045 | 10/38 (LOX-IMVI, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.892× | -3.1 | 0.075 | 10/38 (CFPAC-1, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 380 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.475× (z -13.4) |
| [[Hs 766T (line)]] | wt | 296 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.7) |
| [[HT-29 (line)]] | alt | 40.8 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 77.5 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.384× (z -12.2) ⚠ cell-cycle shift, explains ~20% of this change |
| [[NCI-H460 (line)]] | wt | 26.9 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.72× (z +11.7) | — |
| [[A-427 (line)]] | wt | 86.0 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -23.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 427 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.381× (z -11.8) |
| [[H4 (line)]] | wt | 173 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.308× (z -8.7) |
| [[A498 (line)]] | wt | 108 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +16.9) | — |
| [[HEC-1-A (line)]] | alt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +17.4) | — |
| [[J82 (line)]] | alt | 40.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 40.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 114 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -17.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -9.8) |
| [[A-172 (line)]] | wt | 49.8 | 2 | 0 | [[Ponatinib (drug)]] 5 µM 2.55× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 99.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.01× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 131 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0984× (z -21.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 54.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +16.8) | — |
| [[HOP62 (line)]] | alt | 30.8 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.54× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 121 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 73.5 | 1 | 1 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 3.29× (z +8.6) | [[Methylthiouracil (drug)]] 5 µM 0.210× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 80.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.0) | [[Auranofin (drug)]] 5 µM 0.277× (z -12.7) |
| [[SW 900 (line)]] | alt | 90.8 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.303× (z -10.0) |
| [[A549 (line)]] | wt | 56.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.1) | — |
| [[C32 (line)]] | wt | 71.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -8.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 89.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 46.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 89.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +8.9) | — |
| [[SW48 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.84 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.44 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR17]] | +0.56 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[RAB30]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ANGPT1]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MAPK10]] | +0.53 | +0.62 / +0.60 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[AR]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PCDH18]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[PTPN4]] | +0.51 | +0.49 / +0.58 | both halves | 1e-05 | same gene group; pathway: Interleukin-1 family signaling; STRING 527 |
| [[ROBO1]] | +0.51 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[MEF2C]] | +0.50 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LRRC1]] | +0.50 | +0.40 / +0.53 | both halves | 5e-05 | pathway: RND2 GTPase cycle |
| [[MBNL2]] | +0.50 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[PALS1]] | +0.50 | +0.44 / +0.54 | both halves | 3e-05 | same gene group |
| [[TRPS1]] | +0.49 | +0.50 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRL1-AS1]] | -0.60 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[GHRLOS]] | -0.56 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[MIATNB]] | -0.54 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[LENG8-AS1]] | -0.53 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[SPG7]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[PIGG]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[SRR]] | -0.52 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[GPATCH2L]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ZNF778]] | -0.49 | -0.24 / -0.39 | both halves | 5e-04 |  |
| [[PDCD6]] | -0.49 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TMEM44]] | -0.48 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[MAP3K7]] | -0.48 | -0.36 / -0.48 | both halves | 1e-04 | pathway: Interleukin-1 family signaling |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANGPT1]] | B | ANGPT1 activity raises PTPN13's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.92× lower at baseline in the lines without ANGPT1 | 0.010 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[GUCY1A1]] | B | GUCY1A1 activity raises PTPN13's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without GUCY1A1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PTPN13's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAPK10]] | C | MAPK10 activity raises PTPN13's level | lines that do not express MAPK10 (11) vs lines expressing it (39) | 5.63× lower at baseline in the lines without MAPK10 | 0.006 | ⚠ within organs, on part of the lines; also absent: PTPN13, HDGFL3, EML1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO4]] | B | PTPN13 activity raises LMO4's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 1.71× lower at baseline in the lines without PTPN13 | 0.015 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230 |
| [[LRIG3]] | B | PTPN13 activity raises LRIG3's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 2.42× lower at baseline in the lines without PTPN13 | 0.018 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230 |
| [[MEF2C]] | B | PTPN13 activity raises MEF2C's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 3.57× lower at baseline in the lines without PTPN13 | 0.051 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230 |
| [[ANGPT1]] | B | PTPN13 activity raises ANGPT1's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 4.00× lower at baseline in the lines without PTPN13 | 0.060 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230 |
| [[ATP8A1]] | B | PTPN13 activity raises ATP8A1's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 1.86× lower at baseline in the lines without PTPN13 | 0.077 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230 |
| [[MAPK10]] | C | PTPN13 activity raises MAPK10's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 4.07× lower at baseline in the lines without PTPN13 | 0.011 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.401). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, -14.1); signed map (38.4, 32.9). **Vector** length 109, 29.3% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +6.2 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +4.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -0.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.3 — chr4:86,594,315-86,815,171 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTP1E, PTP-BAS, PTPL1, PTP-BL |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type; PDZ domain containing; FERM domain containing; KIND domain containing |
| Reactome | 14 pathways, smallest: Interleukin-37 signaling; RND1 GTPase cycle; RND2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12923](https://www.uniprot.org/uniprotkb/Q12923) (Tyrosine-protein phosphatase non-receptor type 13):

> Tyrosine phosphatase which negatively regulates FAS-induced apoptosis and NGFR-mediated pro-apoptotic signaling. May regulate phosphoinositide 3-kinase (PI3K) signaling through dephosphorylation of PIK3R2.

**Summary**, from NCBI Gene [5783](https://www.ncbi.nlm.nih.gov/gene/5783):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP is a large intracellular protein. It has a catalytic PTP domain at its C-terminus and two major structural domains: a region with five PDZ domains and a FERM domain that binds to plasma membrane and cytoskeletal elements. This PTP was …

**Accessions** — [HGNC:9646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9646) · Entrez [5783](https://www.ncbi.nlm.nih.gov/gene/5783) · UniProt [Q12923](https://www.uniprot.org/uniprotkb/Q12923) · Ensembl [ENSG00000163629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163629)

## Data

Gene col 8736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8736); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8736]; `tensor/DDL_lfc|DDL_z.npy` [8736]; `embed/gene_vectors.npy` [8736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8736 or target_col == 8736). Every well: [[PTPN13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
