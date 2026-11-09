---
symbol: "STX8"
type: "gene"
col: 9932
ensembl_id: "ENSG00000170310"
name: "syntaxin 8"
location: "17p13.1"
module: 230
arm: "+"
pooled_cpm: 112.96
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 24
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/230"]
generated_by: "tahoemap"
---

# STX8

*syntaxin 8* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.65× (z +11.3, q 1e-26, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.389× (z -30.3, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR70]] (+0.70, fdr 1e-05), [[PCCA]] (+0.68, fdr 3e-05), [[CSTPP1]] (+0.67, fdr 7e-06); moves opposite to [[NIPBL-DT]] (-0.67, fdr 1e-05), [[PTGR3]] (-0.57, fdr 7e-05), [[SIX4]] (-0.56, fdr 6e-05).
> It is in [[Module 230]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +11.3 | 1e-26 | 41/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +8.2 | 9e-14 | 36/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +6.1 | 2e-07 | 22/48 (NCI-H460, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.30×** | +5.9 | 4e-07 | 35/49 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +5.4 | 6e-06 | 28/48 (NCI-H460, SK-MEL-2, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +5.1 | 4e-05 | 11/48 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.7 | 2e-04 | 30/47 (LoVo, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 3e-04 | 22/48 (KATO III, A-172, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.4 | 6e-04 | 22/48 (A-172, HS-578T, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.25×** | +4.4 | 8e-04 | 27/50 (NCI-H596, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.002 | 24/48 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 21/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.20×** | +3.9 | 0.004 | 22/48 (HepG2/C3A, HS-578T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.8 | 0.005 | 19/48 (A-172, RKO, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.19× | +3.8 | 0.007 | 15/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.011 | 20/50 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.5 | 0.016 | 6/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +3.4 | 0.019 | 10/49 (LS 180, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.048 | 16/47 (SW48, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.051 | 13/48 (HS-578T, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9932.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.389×** | -30.3 | 0e+00 | 47/49 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.417×** | -19.8 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.430×** | -19.1 | 0e+00 | 43/48 (SNU-423, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.484×** | -16.5 | 0e+00 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.486×** | -16.4 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.624×** | -15.1 | 0e+00 | 31/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.548×** | -13.7 | 1e-40 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.587×** | -11.7 | 2e-29 | 34/44 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -10.9 | 5e-26 | 41/47 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -10.6 | 3e-24 | 39/50 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.629×** | -10.5 | 4e-24 | 38/49 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.633×** | -10.4 | 1e-23 | 39/48 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.626×** | -10.2 | 6e-23 | 33/48 (NCI-H23, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.640×** | -9.7 | 8e-21 | 39/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.677×** | -8.5 | 6e-16 | 31/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.757×** | -6.3 | 7e-09 | 30/48 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.574×** | -5.9 | 9e-08 | 30/48 (A-172, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.855× | -5.1 | 1e-05 | 22/48 (SNU-1, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.879× | -2.9 | 0.067 | 19/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 171 | 1 | 21 (14 ⚠) | [[Panobinostat (drug)]] 5 µM 1.88× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -30.5) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 0 | 15 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -18.4) |
| [[SNU-423 (line)]] | alt | 131 | 0 | 14 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -26.2) |
| [[SW480 (line)]] | alt | 156 | 0 | 14 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.247× (z -21.6) |
| [[LOX-IMVI (line)]] | wt | 123 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -19.0) |
| [[PANC-1 (line)]] | alt | 123 | 1 | 10 (9 ⚠) | [[Panobinostat (drug)]] 5 µM 1.83× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -19.0) |
| [[SNU-1 (line)]] | wt | 168 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -19.6) |
| [[KATO III (line)]] | alt | 155 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -23.8) |
| [[LoVo (line)]] | wt | 92.5 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -28.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -18.9) |
| [[HS-578T (line)]] | alt | 132 | 1 | 8 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -21.7) |
| [[COLO 205 (line)]] | alt | 138 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -20.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -14.3) |
| [[HT-29 (line)]] | alt | 76.3 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 231 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.315× (z -18.8) |
| [[RKO (line)]] | wt | 134 | 1 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.0) ⚠ cell-cycle shift, explains ~61% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -15.4) |
| [[A-172 (line)]] | wt | 92.2 | 1 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.4) ⚠ cell-cycle shift, explains ~61% of this change | [[Auranofin (drug)]] 5 µM 0.216× (z -19.2) |
| [[A498 (line)]] | wt | 103 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -18.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -16.0) |
| [[A549 (line)]] | wt | 187 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -23.8) |
| [[CFPAC-1 (line)]] | alt | 77.9 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -19.6) |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -19.1) |
| [[SW48 (line)]] | wt | 123 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -15.9) |
| [[A-427 (line)]] | wt | 153 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.347× (z -15.7) |
| [[C32 (line)]] | wt | 119 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -19.6) |
| [[HCT15 (line)]] | alt | 136 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.3) |
| [[J82 (line)]] | alt | 94.0 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.7) ⚠ cell-cycle shift, explains ~61% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -19.1) |
| [[NCI-H1573 (line)]] | alt | 57.3 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.268× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -17.2) |
| [[HEC-1-A (line)]] | alt | 116 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.25× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 54.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -17.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -17.7) |
| [[AsPC-1 (line)]] | alt | 55.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -17.1) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -10.3) |
| [[BT-474 (line)]] | alt | 98.9 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.1) |
| [[H4 (line)]] | wt | 93.7 | 0 | 4 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.243× (z -13.6) ⚠ transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.354× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -15.5) |
| [[HOP62 (line)]] | alt | 73.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -17.3) |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -15.3) |
| [[LS 180 (line)]] | wt | 85.8 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -16.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.4) |
| [[SHP-77 (line)]] | alt | 157 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.521× (z -8.9) |
| [[Hs 766T (line)]] | wt | 70.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0467× (z -27.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -17.8) |
| [[SK-MEL-2 (line)]] | alt | 63.6 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.115× (z -10.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.4) |
| [[SW1417 (line)]] | alt | 74.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.7) |
| [[AN3 CA (line)]] | alt | 115 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.182× (z -11.5) |
| [[C-33 A (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.323× (z -11.7) |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 2 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.119× (z -17.1) |
| [[SW 900 (line)]] | alt | 72.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 46.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -13.9) |
| [[SW 1088 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.110× (z -9.1) ⚠ transcription drop |
| [[SW 1271 (line)]] | alt | 193 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0956× (z -14.9) |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR70]] | +0.70 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[PCCA]] | +0.68 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[CSTPP1]] | +0.67 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NDUFB10]] | +0.66 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[MNAT1]] | +0.65 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NOL7]] ⚠ | +0.63 | +0.46 / +0.59 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[POLR2I]] | +0.63 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[TSR3]] | +0.62 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[DNAAF4]] | +0.61 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[WDR7]] | +0.60 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[TBC1D19]] | +0.60 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[MRPS34]] | +0.58 | +0.28 / +0.43 | both halves | 3e-04 |  |
| [[DTNBP1]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPBL-DT]] | -0.67 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PTGR3]] | -0.57 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[SIX4]] | -0.56 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[HNRNPLL]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ZBED5]] | -0.53 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[LINC01135]] | -0.53 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[MSANTD2]] | -0.52 | -0.39 / -0.26 | both halves | 3e-04 |  |
| [[PNISR-AS1]] | -0.52 | -0.28 / -0.25 | both halves | 4e-04 |  |
| [[TYMSOS]] | -0.52 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[SECISBP2]] | -0.51 | -0.24 / -0.41 | both halves | 5e-04 |  |
| [[LINC00938]] | -0.50 | -0.27 / -0.27 | both halves | 3e-04 |  |
| [[DYRK4]] | -0.50 | -0.40 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 230]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.852). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.9, -5.3); signed map (-21.1, -12.1). **Vector** length 106, 36.1% of its response variance represented; |z| ≥ 3 in 1,454 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.9 | +11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.3 | +8.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.1 | +5.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.0 | +4.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.2 | +5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +4.4 |
|  | [[EX229 (drug)]] 5 µM |  | +4.1 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | -1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.3 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.2 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.4 | -30.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -10.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -10.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -19.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -5.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:9,250,471-9,576,591 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CARB |
| Gene groups (HGNC) | Syntaxins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNK0](https://www.uniprot.org/uniprotkb/Q9UNK0) (Syntaxin-8):

> Vesicle trafficking protein that functions in the early secretory pathway, possibly by mediating retrograde transport from cis-Golgi membranes to the ER.

**Summary**, from NCBI Gene [9482](https://www.ncbi.nlm.nih.gov/gene/9482):

> The gene is a member of the syntaxin family. The encoded protein is involved in protein trafficking from early to late endosomes via vesicle fusion and exocytosis. A related pseudogene has been identified on chromosome 12. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:11443](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11443) · Entrez [9482](https://www.ncbi.nlm.nih.gov/gene/9482) · UniProt [Q9UNK0](https://www.uniprot.org/uniprotkb/Q9UNK0) · Ensembl [ENSG00000170310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170310)

## Data

Gene col 9932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9932); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9932]; `tensor/DDL_lfc|DDL_z.npy` [9932]; `embed/gene_vectors.npy` [9932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9932 or target_col == 9932). Every well: [[STX8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
