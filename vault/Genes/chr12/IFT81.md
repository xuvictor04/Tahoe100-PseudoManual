---
symbol: "IFT81"
type: "gene"
col: 4391
ensembl_id: "ENSG00000122970"
name: "intraflagellar transport 81"
location: "12q24.11"
module: 28
arm: "+"
pooled_cpm: 38.36
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# IFT81

*intraflagellar transport 81* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.01× (z +12.7, q 5e-34, up in 42 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.35× (z +5.2, q 2e-05, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.497× (z -12.7, q 4e-34, down in 39 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.578× (z -9.9, q 8e-21, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMARCA1]] (+0.64, fdr 1e-05), [[NDUFA5]] (+0.60, fdr 1e-05), [[SPAG16]] (+0.60, fdr 1e-05); moves opposite to [[FAM89A]] (-0.58, fdr 3e-05), [[DOCK9]] (-0.56, fdr 3e-05), [[AXIN1]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CCDC191]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +12.7 | 5e-34 | 42/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +11.4 | 1e-27 | 33/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +7.2 | 1e-10 | 32/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.28×** | +6.4 | 2e-08 | 28/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +5.8 | 7e-07 | 27/48 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +5.2 | 2e-05 | 22/47 (C32, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 2e-04 | 21/48 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.002 | 20/47 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.20×** | +4.0 | 0.003 | 14/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +4.0 | 0.003 | 18/48 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +3.9 | 0.004 | 19/48 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.006 | 11/48 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.006 | 18/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.053 | 13/48 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.098 | 13/48 (C32, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.098 | 13/47 (C-33 A, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.098 | 10/48 (C32, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.098 | 14/48 (LoVo, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.099 | 14/47 (C32, HS-578T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4391.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -12.7 | 4e-34 | 39/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.578×** | -9.9 | 8e-21 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.618×** | -8.7 | 6e-16 | 38/48 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.641×** | -8.1 | 1e-13 | 36/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -7.8 | 6e-13 | 28/48 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.648×** | -7.6 | 4e-12 | 32/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -7.5 | 4e-12 | 31/48 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -7.3 | 2e-11 | 32/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.653×** | -7.3 | 2e-11 | 35/48 (CFPAC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.484×** | -6.7 | 2e-09 | 29/48 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.523×** | -5.9 | 1e-07 | 27/42 (C-33 A, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.530×** | -5.8 | 3e-07 | 29/48 (CFPAC-1, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -5.7 | 4e-07 | 25/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -5.5 | 1e-06 | 25/48 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.806×** | -5.5 | 1e-06 | 25/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.759×** | -5.0 | 2e-05 | 22/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.758×** | -3.6 | 0.010 | 12/48 (SW 900, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.827×** | -3.4 | 0.016 | 16/47 (H4, MIA PaCa-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.0 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.277× (z -12.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.319× (z -11.5) |
| [[SW480 (line)]] | alt | 39.7 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.469× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.473× (z -9.1) |
| [[PANC-1 (line)]] | alt | 42.0 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.78× (z +11.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.295× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.469× (z -8.5) |
| [[A-172 (line)]] | wt | 59.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -9.0) |
| [[A498 (line)]] | wt | 43.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 47.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.249× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 80.9 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.441× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 74.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.308× (z -9.1) |
| [[A549 (line)]] | wt | 55.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +10.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 48.0 | 0 | 2 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0492× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 46.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.212× (z -11.4) |
| [[A-427 (line)]] | wt | 42.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.144× (z -9.0) |
| [[C32 (line)]] | wt | 48.5 | 1 | 0 | [[Binimetinib (drug)]] 5 µM 3.32× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.357× (z -9.1) ⚠ toxic |
| [[HS-578T (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.317× (z -8.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +8.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 23.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 62.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.342× (z -9.9) |
| [[SNU-423 (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 20.6 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0602× (z -12.0) |
| [[AN3 CA (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCA1]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[NDUFA5]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[SPAG16]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SH3BGRL]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[PCM1]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 646 |
| [[DNAL1]] | +0.58 | +0.39 / +0.65 | both halves | 6e-05 |  |
| [[AGL]] | +0.58 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[STAG2]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[IFT80]] | +0.56 | +0.56 / +0.40 | both halves | 5e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 998 |
| [[TMEM107]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[SMARCA5]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[SYNJ2BP]] | +0.55 | +0.41 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM89A]] | -0.58 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[DOCK9]] | -0.56 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[AXIN1]] | -0.55 | -0.43 / -0.58 | both halves | 4e-05 | STRING 537 |
| [[SLC37A3]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[TRIM11]] | -0.55 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[KLHL29]] | -0.54 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[FOXK2]] | -0.53 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[EVI5]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[NOL4L]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[EEF1AKMT4]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[CSNK1E]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[CCNQ]] | -0.51 | -0.36 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers IFT81's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[COL5A2]] | B | COL5A2 activity raises IFT81's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 1.48× lower at baseline in the lines without COL5A2 | 0.066 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC191]] | C | IFT81's natural level strengthens CCDC191's drug response | IFT81's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.20; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.8, 4.2); signed map (17.4, -35.8). **Vector** length 93.7, 23.9% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +12.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.8 | +6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.4 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.1 | +4.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.9 | +4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -5.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 81 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,124,335-110,218,793 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDV-1R, MGC4027; previously CDV1 |
| Gene groups (HGNC) | IFT-B1 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYA0](https://www.uniprot.org/uniprotkb/Q8WYA0) (Intraflagellar transport protein 81 homolog):

> Component of the intraflagellar transport (IFT) complex B: together with IFT74, forms a tubulin-binding module that specifically mediates transport of tubulin within the cilium. Binds tubulin via its CH (calponin-homology)-like region. Required for ciliogenesis. Required for proper regulation of SHH signaling. Plays an important role during spermatogenesis by modulating the assembly and elongation of the sperm flagella (By similarity).

**Summary**, from NCBI Gene [28981](https://www.ncbi.nlm.nih.gov/gene/28981):

> The protein encoded by this gene, together with IFT74, forms a tubulin-binding module of intraflagellar transport complex B. This module is involved in transport of tubulin within the cilium, and the encoded protein is required for ciliogenesis. Mutations in this gene are a cause of short-rib polydactyly syndromes. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:14313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14313) · Entrez [28981](https://www.ncbi.nlm.nih.gov/gene/28981) · UniProt [Q8WYA0](https://www.uniprot.org/uniprotkb/Q8WYA0) · Ensembl [ENSG00000122970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122970)

## Data

Gene col 4391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4391); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4391]; `tensor/DDL_lfc|DDL_z.npy` [4391]; `embed/gene_vectors.npy` [4391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4391 or target_col == 4391). Every well: [[IFT81 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT81.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
