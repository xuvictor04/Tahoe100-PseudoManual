---
symbol: "RASSF3"
type: "gene"
col: 7698
ensembl_id: "ENSG00000153179"
name: "Ras association domain family member 3"
location: "12q14.2"
module: 92
arm: "+"
pooled_cpm: 106.1
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# RASSF3

*Ras association domain family member 3* — 12q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.24× (z +6.2, q 3e-07, up in 25 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.603× (z -10.3, q 3e-22, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L2]] (+0.58, fdr 1e-05), [[ETV4]] (+0.57, fdr 1e-05), [[B4GALT6]] (+0.56, fdr 1e-05); moves opposite to [[UFSP2]] (-0.53, fdr 2e-05), [[C1R]] (-0.53, fdr 2e-05), [[CEP350]] (-0.52, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EPB41L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7698.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.2 | 3e-07 | 25/49 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +6.1 | 4e-07 | 29/47 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +5.4 | 1e-05 | 26/48 (A-427, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 1e-05 | 26/48 (LoVo, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.009 | 21/48 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.20× | +3.7 | 0.022 | 15/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.4 | 0.047 | 9/38 (A-427, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.12× | +3.4 | 0.047 | 15/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.4 | 0.047 | 13/48 (J82, NCI-H1573, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.12× | +3.3 | 0.058 | 10/49 (CFPAC-1, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.17× | +3.2 | 0.063 | 17/48 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.081 | 15/48 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.081 | 20/49 (C32, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.089 | 12/48 (C32, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7698.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.603×** | -10.3 | 3e-22 | 37/48 (LS 180, A549, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.629×** | -9.5 | 7e-19 | 35/48 (LS 180, A549, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.670×** | -7.9 | 8e-13 | 37/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.693×** | -7.5 | 1e-11 | 32/49 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.819×** | -5.7 | 1e-06 | 25/48 (RKO, COLO 205, …) | top dose only | composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.785×** | -5.7 | 1e-06 | 27/50 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.760×** | -5.6 | 2e-06 | 27/47 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.784×** | -5.4 | 4e-06 | 26/49 (NCI-H460, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.764×** | -5.3 | 9e-06 | 26/47 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.787×** | -5.0 | 3e-05 | 25/48 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.843× | -4.8 | 8e-05 | 22/49 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.639×** | -4.8 | 8e-05 | 27/47 (J82, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.801×** | -4.6 | 2e-04 | 22/48 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.798×** | -4.4 | 4e-04 | 24/47 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.860× | -4.3 | 6e-04 | 14/48 (Panc 03.27, BT-474, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.816×** | -4.0 | 0.002 | 14/49 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.822×** | -3.7 | 0.007 | 19/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.838× | -3.6 | 0.010 | 20/48 (A549, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 81.1 | 0 | 7 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.277× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 155 | 0 | 5 (3 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.469× (z -9.3) |
| [[RKO (line)]] | wt | 76.8 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -17.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[CFPAC-1 (line)]] | alt | 177 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.9) ⚠ cell-cycle shift, explains ~17% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -10.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.413× (z -10.0) |
| [[COLO 205 (line)]] | alt | 127 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0701× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 215 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -13.1) |
| [[LS 180 (line)]] | wt | 164 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -17.0) |
| [[BT-474 (line)]] | alt | 82.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.9) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 181 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -10.3) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.435× (z -9.4) |
| [[A549 (line)]] | wt | 167 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 132 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -10.0) |
| [[LoVo (line)]] | wt | 98.6 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 0.5 µM 1.99× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 107 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.89× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.261× (z -14.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 2 | — | [[Trametinib (drug)]] 5 µM 0.395× (z -9.5) |
| [[PANC-1 (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -10.7) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.494× (z -8.6) |
| [[A-427 (line)]] | wt | 96.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.438× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +8.7) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[H4 (line)]] | wt | 64.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 127 | 0 | 1 | — | [[Alpelisib (drug)]] 5 µM 0.0459× (z -13.9) |
| [[HS-578T (line)]] | alt | 63.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.364× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 62.8 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.26× (z +8.8) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[KATO III (line)]] | alt | 90.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.3) ⚠ cell-cycle shift, explains ~17% of this change |
| [[LOX-IMVI (line)]] | wt | 89.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.4) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H1792 (line)]] | alt | 69.2 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.99× (z +8.7) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.141× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 107 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -8.8) |
| [[SNU-423 (line)]] | alt | 79.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.1) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[SW 1271 (line)]] | alt | 96.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0849× (z -10.2) ⚠ toxic |
| [[SW480 (line)]] | alt | 55.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.525× (z -8.6) |
| [[A-172 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ETV4]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[TSPAN14]] | +0.53 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[ITGA6]] | +0.53 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SLC35F3]] | +0.52 | +0.52 / +0.51 | both halves | 1e-05 | same gene group |
| [[TBC1D4]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ANTXR2]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[CDYL]] | +0.51 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[ITPR3]] | +0.51 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[LHX1-DT]] | +0.51 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[DTX4]] | +0.51 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFSP2]] | -0.53 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[C1R]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CEP350]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[NMT1]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RBSN]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[TMEM167B]] | -0.50 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SFSWAP]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[MRFAP1]] | -0.48 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[PAFAH1B1]] | -0.48 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[SPOP]] | -0.48 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[AZI2]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[RBM5]] | -0.47 | -0.54 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L2]] | B | EPB41L2 activity lowers RASSF3's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.49× higher at baseline in the lines without EPB41L2 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises RASSF3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[HTRA3]] | B | HTRA3 activity lowers RASSF3's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.31× higher at baseline in the lines without HTRA3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.8, 8.2); signed map (9.4, 46.4). **Vector** length 127, 37.4% of its response variance represented; |z| ≥ 3 in 1,366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +2.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.4 | +5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.3 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.9 | -5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.4 | -7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.2 | -7.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.2 | -5.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.8 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | Ras association domain family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.2 — chr12:64,507,001-64,697,564 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ras association domain family; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q86WH2](https://www.uniprot.org/uniprotkb/Q86WH2) carries no function annotation.

**Summary**, from NCBI Gene [283349](https://www.ncbi.nlm.nih.gov/gene/283349):

> The RAS oncogene (MIM 190020) is mutated in nearly one-third of all human cancers. Members of the RAS superfamily are plasma membrane GTP-binding proteins that modulate intracellular signal transduction pathways. A subfamily of RAS effectors, including RASSF3, share a RAS association (RA) domain.[supplied by OMIM, Jul 2003]

**Accessions** — [HGNC:14271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14271) · Entrez [283349](https://www.ncbi.nlm.nih.gov/gene/283349) · UniProt [Q86WH2](https://www.uniprot.org/uniprotkb/Q86WH2) · Ensembl [ENSG00000153179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153179)

## Data

Gene col 7698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7698); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7698]; `tensor/DDL_lfc|DDL_z.npy` [7698]; `embed/gene_vectors.npy` [7698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7698 or target_col == 7698). Every well: [[RASSF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASSF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
