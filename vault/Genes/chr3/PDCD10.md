---
symbol: "PDCD10"
type: "gene"
col: 3532
ensembl_id: "ENSG00000114209"
name: "programmed cell death 10"
location: "3q26.1"
module: 77
arm: "+"
pooled_cpm: 138.22
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# PDCD10

*programmed cell death 10* — 3q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.06× (z +8.5, q 1e-14, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.692× (z -11.8, q 4e-29, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDAC3]] (+0.68, fdr 3e-05), [[CNOT8]] (+0.67, fdr 1e-05), [[FAM104A]] (+0.67, fdr 1e-05); moves opposite to [[PMF1]] (-0.74, fdr 8e-06), [[SRSF6]] (-0.68, fdr 1e-05), [[BRPF3]] (-0.66, fdr 8e-05).
> It sits in the **+** arm of [[Module 077]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +8.5 | 1e-14 | 41/49 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +7.3 | 9e-11 | 38/48 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.32×** | +6.3 | 5e-08 | 32/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.7 | 2e-06 | 29/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.28×** | +5.6 | 3e-06 | 28/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 5e-04 | 22/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 8e-04 | 21/48 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.20×** | +4.2 | 0.002 | 22/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.20× | +4.0 | 0.004 | 22/48 (HT-29, A-427, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.8 | 0.007 | 14/49 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.18× | +3.6 | 0.014 | 18/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.028 | 19/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.16× | +3.3 | 0.036 | 17/48 (A-427, SW1417, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.10× | +3.1 | 0.076 | 9/48 (BT-474, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.692×** | -11.8 | 4e-29 | 38/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.611×** | -11.1 | 3e-26 | 41/49 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -10.9 | 2e-25 | 37/44 (SK-MEL-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.685×** | -7.9 | 4e-13 | 34/45 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -6.3 | 3e-08 | 31/47 (HepG2/C3A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -5.9 | 4e-07 | 23/49 (A549, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.801×** | -4.8 | 1e-04 | 24/48 (A-172, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.824×** | -4.4 | 9e-04 | 23/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.863× | -3.3 | 0.053 | 15/47 (SW480, C32, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.3 | 0.060 | 21/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.871× | -3.1 | 0.089 | 17/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 150 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -18.9) |
| [[LoVo (line)]] | wt | 89.9 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.88× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.467× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 136 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +14.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.66× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 178 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.546× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 178 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 148 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +11.8) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -10.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 230 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -9.0) |
| [[A549 (line)]] | wt | 96.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 149 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 192 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 214 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.628× (z -9.8) |
| [[A-427 (line)]] | wt | 207 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.519× (z -10.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 143 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.579× (z -9.2) |
| [[H4 (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -16.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 191 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -15.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 88.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -14.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.498× (z -10.4) |
| [[HOP62 (line)]] | alt | 122 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.499× (z -11.9) |
| [[HT-29 (line)]] | alt | 130 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.16× (z +9.8) | — |
| [[KATO III (line)]] | alt | 191 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -12.9) |
| [[LS 180 (line)]] | wt | 136 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.81× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 105 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +9.0) ⚠ cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -10.4) |
| [[RKO (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -16.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 169 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +10.0) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 5 µM 0.545× (z -9.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 114 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -8.6) |
| [[BT-474 (line)]] | alt | 138 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.9) |
| [[J82 (line)]] | alt | 202 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -18.2) |
| [[LOX-IMVI (line)]] | wt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 64.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -19.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 166 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -11.8) |
| [[SNU-423 (line)]] | alt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -13.3) |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0858× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.563× (z -8.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 147 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 95.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 97.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC3]] | +0.68 | +0.76 / +0.45 | both halves | 3e-05 |  |
| [[CNOT8]] | +0.67 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[FAM104A]] | +0.67 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.66 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ZDHHC9]] | +0.64 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[MAP2K1]] | +0.63 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[MRPL55]] | +0.63 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CTNNBL1]] | +0.63 | +0.71 / +0.29 | both halves | 3e-04 |  |
| [[MMS19]] | +0.63 | +0.70 / +0.40 | both halves | 5e-05 |  |
| [[ECI2]] | +0.62 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[MGST3]] | +0.62 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[UBE2O]] | +0.62 | +0.68 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMF1]] | -0.74 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[SRSF6]] | -0.68 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[BRPF3]] | -0.66 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[THOC6]] | -0.65 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[DCAF8]] | -0.65 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[SRRM2]] | -0.64 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[FKRP]] | -0.63 | -0.66 / -0.39 | both halves | 6e-05 |  |
| [[TIA1]] | -0.63 | -0.66 / -0.39 | both halves | 5e-05 |  |
| [[AKT1S1]] | -0.62 | -0.66 / -0.32 | both halves | 2e-04 |  |
| [[ST7L]] | -0.61 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[CROCC]] | -0.61 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[ERMAP]] | -0.61 | -0.57 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (6.7, -16.5); signed map (-35.5, 19.8). **Vector** length 119, 36.0% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +7.2 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +6.6 | +3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.9 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.5 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.6 | -11.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.8 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.9 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -4.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | programmed cell death 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.1 — chr3:167,683,298-167,734,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFAR15; previously CCM3 |
| Gene groups (HGNC) | STRIPAK complex; CCM adhesion complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUL8](https://www.uniprot.org/uniprotkb/Q9BUL8) (Programmed cell death protein 10):

> Promotes cell proliferation. Modulates apoptotic pathways. Increases mitogen-activated protein kinase activity and STK26 activity. Important for cell migration, and for normal structure and assembly of the Golgi complex. Part of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of multiple signaling pathways including Hippo, MAPK, nuclear receptor and cytoskeleton remodeling. Different …

**Summary**, from NCBI Gene [11235](https://www.ncbi.nlm.nih.gov/gene/11235):

> This gene encodes an evolutionarily conserved protein associated with cell apoptosis. The protein interacts with the serine/threonine protein kinase MST4 to modulate the extracellular signal-regulated kinase (ERK) pathway. It also interacts with and is phosphoryated by serine/threonine kinase 25, and is thought to function in a signaling pathway essential for vascular developent. Mutations in this gene are one cause of cerebral cavernous malformations, which are vascular malformations that …

**Accessions** — [HGNC:8761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8761) · Entrez [11235](https://www.ncbi.nlm.nih.gov/gene/11235) · UniProt [Q9BUL8](https://www.uniprot.org/uniprotkb/Q9BUL8) · Ensembl [ENSG00000114209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114209)

## Data

Gene col 3532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3532); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3532]; `tensor/DDL_lfc|DDL_z.npy` [3532]; `embed/gene_vectors.npy` [3532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3532 or target_col == 3532). Every well: [[PDCD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
