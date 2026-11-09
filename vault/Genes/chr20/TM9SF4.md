---
symbol: "TM9SF4"
type: "gene"
col: 2117
ensembl_id: "ENSG00000101337"
name: "transmembrane 9 superfamily member 4"
location: "20q11.21"
module: 156
arm: "+"
pooled_cpm: 145.76
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# TM9SF4

*transmembrane 9 superfamily member 4* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.24× (z +6.4, q 7e-08, up in 28 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.50× (z +6.3, q 1e-07, up in 31 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.497× (z -20.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFX1]] (+0.66, fdr 7e-06), [[LRRC41]] (+0.65, fdr 7e-06), [[ECSIT]] (+0.64, fdr 7e-06); moves opposite to [[SPOPL]] (-0.55, fdr 2e-05), [[TMOD2]] (-0.54, fdr 1e-05), [[CMTM6]] (-0.54, fdr 3e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +6.4 | 7e-08 | 28/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +6.3 | 1e-07 | 31/49 (Hs 766T, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.26×** | +5.0 | 1e-04 | 32/48 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.37×** | +4.9 | 2e-04 | 24/48 (PANC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +4.7 | 4e-04 | 28/48 (SW480, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.16× | +4.4 | 0.001 | 16/49 (RPMI-7951, SW1417, …) | top dose only | plate-row cell shift |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.14× | +3.8 | 0.011 | 8/48 (C32, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[TAK-733 (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.017 | 21/48 (A498, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.017 | 14/49 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.024 | 15/48 (SW480, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.048 | 5/47 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.052 | 16/48 (PANC-1, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.11× | +3.1 | 0.073 | 5/48 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.076 | 8/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.097 | 18/48 (PANC-1, Hs 766T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2117.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.497×** | -20.8 | 0e+00 | 47/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.530×** | -18.9 | 0e+00 | 48/48 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.538×** | -18.5 | 0e+00 | 48/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -11.7 | 2e-29 | 39/47 (J82, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.681×** | -11.0 | 5e-26 | 37/48 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.699×** | -10.7 | 1e-24 | 45/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.780×** | -10.5 | 1e-23 | 33/48 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.727×** | -9.1 | 4e-18 | 33/48 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.745×** | -8.8 | 1e-16 | 37/48 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.583×** | -8.4 | 2e-15 | 43/49 (SK-MEL-2, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.833×** | -7.7 | 8e-13 | 25/49 (RKO, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.767×** | -7.6 | 1e-12 | 24/44 (LS 180, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.783×** | -7.3 | 1e-11 | 32/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.784×** | -7.3 | 2e-11 | 27/49 (NCI-H23, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -7.1 | 3e-11 | 28/50 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Verteporfin (drug)]] 5 µM |  | 0.836× | -5.1 | 9e-06 | 23/49 (SW1417, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.850× | -4.8 | 4e-05 | 19/48 (A549, HOP62, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.903× | -3.0 | 0.056 | 8/48 (C32, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.886× | -2.9 | 0.071 | 10/47 (A549, C32, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 200 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.431× (z -12.7) |
| [[KATO III (line)]] | alt | 184 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -13.7) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.445× (z -12.8) |
| [[SW480 (line)]] | alt | 154 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.496× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.525× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 133 | 1 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +13.3) ⚠ cell-cycle shift, explains ~11% of this change | [[Panobinostat (drug)]] 5 µM 0.374× (z -17.9) |
| [[SK-MEL-2 (line)]] | alt | 148 | 1 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.3) ⚠ cell-cycle shift, explains ~11% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -15.6) |
| [[A-427 (line)]] | wt | 148 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.418× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -10.7) |
| [[SW1417 (line)]] | alt | 207 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.360× (z -17.1) |
| [[A498 (line)]] | wt | 153 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.507× (z -10.5) |
| [[HOP62 (line)]] | alt | 174 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.433× (z -13.4) |
| [[Hs 766T (line)]] | wt | 232 | 2 (1 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.94× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.546× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.594× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 152 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.388× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 207 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.419× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.473× (z -10.4) |
| [[SW 900 (line)]] | alt | 135 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.461× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 114 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.464× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 94.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -13.1) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.435× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 99.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.479× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 123 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.408× (z -10.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.450× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 96.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 142 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.432× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 148 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.1) ⚠ cell-cycle shift, explains ~11% of this change | [[Panobinostat (drug)]] 5 µM 0.406× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.485× (z -9.6) |
| [[PANC-1 (line)]] | alt | 286 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.547× (z -13.4) |
| [[RKO (line)]] | wt | 173 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -12.8) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.460× (z -11.2) |
| [[SNU-1 (line)]] | wt | 193 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.468× (z -9.6) |
| [[A-172 (line)]] | wt | 123 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.3) ⚠ cell-cycle shift, explains ~11% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -9.8) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.530× (z -9.6) |
| [[COLO 205 (line)]] | alt | 197 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.561× (z -9.1) |
| [[H4 (line)]] | wt | 152 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -13.4) |
| [[LoVo (line)]] | wt | 100 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.502× (z -10.3) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.543× (z -9.5) |
| [[LS 180 (line)]] | wt | 101 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -27.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 129 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -16.0) |
| [[SNU-423 (line)]] | alt | 165 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -12.4) |
| [[C-33 A (line)]] | alt | 133 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.414× (z -10.3) |
| [[A549 (line)]] | wt | 94.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.495× (z -8.9) |
| [[CHP-212 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[HCT15 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 128 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.48× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.551× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H2347 (line)]] | alt | 77.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.472× (z -9.8) |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.136× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 212 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.170× (z -9.7) |
| [[SW48 (line)]] | wt | 120 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.451× (z -8.8) |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 150 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 200 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFX1]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[LRRC41]] | +0.65 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[ECSIT]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[FAF2]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[AP1G1]] | +0.63 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[PMM2]] | +0.63 | +0.52 / +0.77 | both halves | 1e-05 |  |
| [[METTL16]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[NUP214]] | +0.63 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ACOX3]] | +0.62 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[UBE2J2]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TRMT44]] | +0.61 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[GOSR1]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOPL]] | -0.55 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[TMOD2]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[CMTM6]] | -0.54 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[PPP4R1]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PTBP3]] | -0.53 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[BTBD3]] | -0.52 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ZDHHC2]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[FAM199X]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SSX2IP]] | -0.51 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SPAST]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TM9SF4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.9, -2.6); signed map (-6.3, -13.5). **Vector** length 122, 38.7% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.8 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.6 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +5.9 | -3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.7 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.6 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +5.5 | +4.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +4.7 | +5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.3 | +2.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.8 | -11.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -10.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -8.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -5.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 9 superfamily member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:32,109,714-32,167,258 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0255, dJ836N17.2 |
| Gene groups (HGNC) | Transmembrane 9 superfamily members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92544](https://www.uniprot.org/uniprotkb/Q92544) (Transmembrane 9 superfamily member 4):

> Associates with proteins harboring glycine-rich transmembrane domains and ensures their efficient localization to the cell surface. Regulates the assembly and activity of V-ATPase in colon cancer cells via its interaction with V-type proton ATPase subunit H (ATP6V1H) and contributes to V-ATPase-mediated pH alterations in cancer cells which play an important role in drug resistance and invasiveness of colon cancer cells. Plays an important role in an atypical phagocytic activity of metastatic …

**Summary**, from NCBI Gene [9777](https://www.ncbi.nlm.nih.gov/gene/9777):

> Involved in several processes, including positive regulation of protein localization; response to hypoxia; and vacuolar proton-transporting V-type ATPase complex assembly. Located in Golgi apparatus and early endosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30797) · Entrez [9777](https://www.ncbi.nlm.nih.gov/gene/9777) · UniProt [Q92544](https://www.uniprot.org/uniprotkb/Q92544) · Ensembl [ENSG00000101337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101337)

## Data

Gene col 2117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2117); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2117]; `tensor/DDL_lfc|DDL_z.npy` [2117]; `embed/gene_vectors.npy` [2117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2117 or target_col == 2117). Every well: [[TM9SF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM9SF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
