---
symbol: "WDR59"
type: "gene"
col: 2319
ensembl_id: "ENSG00000103091"
name: "WD repeat domain 59"
location: "16q23.1"
module: 77
arm: "+"
pooled_cpm: 106.53
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# WDR59

*WD repeat domain 59* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.29× (z +6.1, q 5e-07, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.463× (z -26.0, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.531× (z -15.1, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUXAP10]] (+0.62, fdr 1e-05), [[SNRPD2]] (+0.61, fdr 3e-05), [[CCNB1IP1]] (+0.61, fdr 1e-05); moves opposite to [[MIER3]] (-0.63, fdr 1e-05), [[ATXN7]] (-0.59, fdr 1e-05), [[FAM111A]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LHFPL6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +6.1 | 5e-07 | 25/48 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +5.0 | 2e-04 | 32/49 (MIA PaCa-2, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.21×** | +4.4 | 0.002 | 19/47 (NCI-H23, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.21×** | +4.3 | 0.003 | 18/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.011 | 16/50 (SW 900, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.014 | 16/49 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.046 | 11/47 (NCI-H2030, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.054 | 13/49 (AsPC-1, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.2 | 0.093 | 12/48 (Hs 766T, A498, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.093 | 9/49 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.14× | +3.1 | 0.11 | 10/49 (A549, A-172, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.0 | 0.11 | 19/48 (NCI-H1573, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | 1.13× | +3.0 | 0.11 | 11/49 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.0 | 0.11 | 16/48 (NCI-H1573, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2319.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.463×** | -26.0 | 0e+00 | 47/48 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.415×** | -20.2 | 0e+00 | 46/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.531×** | -15.1 | 0e+00 | 46/48 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.559×** | -13.9 | 9e-42 | 42/48 (C32, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -12.2 | 3e-32 | 40/49 (CFPAC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.641×** | -10.6 | 2e-24 | 43/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.689×** | -8.9 | 5e-17 | 40/48 (KATO III, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.700×** | -8.5 | 1e-15 | 34/48 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.721×** | -7.2 | 3e-11 | 27/45 (RKO, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **0.741×** | -7.2 | 5e-11 | 29/49 (SNU-423, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **0.762×** | -6.2 | 2e-08 | 25/44 (RPMI-7951, SNU-1, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.788×** | -5.7 | 7e-07 | 27/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | **0.797×** | -5.4 | 3e-06 | 27/48 (HCT15, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.806×** | -5.1 | 1e-05 | 26/48 (SW480, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.670×** | -4.8 | 5e-05 | 20/49 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.6 | 2e-04 | 28/48 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.765×** | -3.2 | 0.040 | 17/49 (NCI-H1792, A549, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 197 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.404× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 109 | 2 (1 ⚠) | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.87× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.440× (z -12.1) |
| [[SW480 (line)]] | alt | 169 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -15.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.521× (z -9.4) |
| [[PANC-1 (line)]] | alt | 82.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -15.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.515× (z -10.9) |
| [[C32 (line)]] | wt | 68.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -14.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.268× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -21.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -13.1) |
| [[SNU-423 (line)]] | alt | 135 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -14.1) |
| [[A549 (line)]] | wt | 127 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -16.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.459× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 134 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -28.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -14.5) |
| [[KATO III (line)]] | alt | 91.5 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.322× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H1792 (line)]] | alt | 192 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -22.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -14.2) |
| [[SW 900 (line)]] | alt | 127 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.381× (z -9.9) |
| [[A498 (line)]] | wt | 83.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.9) ⚠ cell-cycle shift, explains ~47% of this change | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.519× (z -9.0) |
| [[HOP62 (line)]] | alt | 132 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -21.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.385× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -22.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -9.1) |
| [[LS 180 (line)]] | wt | 104 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.350× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.493× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 208 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 109 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.53× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | [[Homoharringtonine (drug)]] 5 µM 0.622× (z -9.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.529× (z -9.4) |
| [[RKO (line)]] | wt | 128 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -14.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.518× (z -8.6) |
| [[A-427 (line)]] | wt | 86.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -12.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.438× (z -10.0) |
| [[H4 (line)]] | wt | 136 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.357× (z -8.5) |
| [[HS-578T (line)]] | alt | 68.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 106 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 93.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[SK-MEL-2 (line)]] | alt | 90.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.395× (z -10.7) |
| [[SNU-1 (line)]] | wt | 80.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[A-172 (line)]] | wt | 89.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.361× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 75.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -14.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 73.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 82.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -19.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 143 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -13.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -9.6) |
| [[J82 (line)]] | alt | 65.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -12.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 80.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.413× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -11.2) |
| [[SW1417 (line)]] | alt | 68.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -16.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 157 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -11.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 78.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.387× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 65.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -17.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW 1088 (line)]] | alt | 140 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.115× (z -9.2) |
| [[AN3 CA (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUXAP10]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SNRPD2]] | +0.61 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[CCNB1IP1]] | +0.61 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[RPS24]] | +0.60 | +0.67 / +0.45 | both halves | 3e-05 | pathway: Cellular response to starvation |
| [[TMEM120B]] | +0.59 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[ERI3]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SHQ1]] | +0.58 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[PLD3]] | +0.58 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[CSNK2A1]] | +0.56 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[ADIPOR1]] | +0.56 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[RNF149]] | +0.56 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[ZCCHC7]] | +0.55 | +0.65 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIER3]] | -0.63 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ATXN7]] | -0.59 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[FAM111A]] | -0.59 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[TIA1]] | -0.59 | -0.70 / -0.36 | both halves | 1e-04 |  |
| [[ZNF689]] | -0.58 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[RBM26-AS1]] | -0.57 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[LEKR1]] | -0.57 | -0.64 / -0.37 | both halves | 9e-05 |  |
| [[ZNF827]] | -0.57 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[SIX5]] | -0.56 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[CYREN]] | -0.56 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[SEPTIN8]] | -0.56 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[CASC9]] | -0.55 | -0.60 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHFPL6]] | B | LHFPL6 activity raises WDR59's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without LHFPL6 | 0.068 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[MTOR]] | B | MTOR activity lowers WDR59's level | compounds that target MTOR: 3 of 8 raise it (Bimiralisib, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[DUXAP10]] | B | DUXAP10 activity raises WDR59's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.42× lower at baseline in the lines without DUXAP10 | 0.084 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-51.2, -28.0); signed map (-55.1, -4.7). **Vector** length 109, 32.8% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | +6.2 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -9.0 | -26.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -15.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.2 | -20.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -4.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.9 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 59 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:74,871,362-75,000,173 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12270 |
| Gene groups (HGNC) | WD repeat domain containing; GATOR2 subcomplex; RWD domain containing |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PJI9](https://www.uniprot.org/uniprotkb/Q6PJI9) (GATOR2 complex protein WDR59):

> As a component of the GATOR2 complex, functions as an activator of the amino acid-sensing branch of the mTORC1 signaling pathway. The GATOR2 complex indirectly activates mTORC1 through the inhibition of the GATOR1 subcomplex. GATOR2 probably acts as an E3 ubiquitin-protein ligase toward GATOR1. In the presence of abundant amino acids, the GATOR2 complex mediates ubiquitination of the NPRL2 core component of the GATOR1 complex, leading to GATOR1 inactivation. In the absence of amino acids, …

**Summary**, from NCBI Gene [79726](https://www.ncbi.nlm.nih.gov/gene/79726):

> Predicted to enable signaling adaptor activity. Involved in cellular response to amino acid starvation and positive regulation of TORC1 signaling. Acts upstream of or within protein localization to plasma membrane. Located in lysosomal membrane. Part of GATOR2 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25706) · Entrez [79726](https://www.ncbi.nlm.nih.gov/gene/79726) · UniProt [Q6PJI9](https://www.uniprot.org/uniprotkb/Q6PJI9) · Ensembl [ENSG00000103091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103091)

## Data

Gene col 2319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2319); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2319]; `tensor/DDL_lfc|DDL_z.npy` [2319]; `embed/gene_vectors.npy` [2319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2319 or target_col == 2319). Every well: [[WDR59 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR59.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
