---
symbol: "CCDC146"
type: "gene"
col: 5664
ensembl_id: "ENSG00000135205"
name: "coiled-coil domain containing 146"
location: "7q11.23"
module: 37
arm: "+"
pooled_cpm: 76.72
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 38
n_dd_up_clean: 3
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CCDC146

*coiled-coil domain containing 146* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.42× (z +5.1, q 2e-04, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.364× (z -21.6, q 0e+00, down in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.316× (z -16.8, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02937]] (+0.69, fdr 7e-06), [[IQCJ]] (+0.56, fdr 3e-05), [[BCO2]] (+0.56, fdr 1e-05); moves opposite to [[ZNF708]] (-0.54, fdr 1e-05), [[SAAL1]] (-0.53, fdr 1e-05), [[TRIM32]] (-0.49, fdr 6e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SYCP2L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +5.1 | 2e-04 | 32/46 (SW480, AsPC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.019 | 20/47 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.059 | 16/47 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.36× | +3.3 | 0.12 | 13/47 (HEC-1-A, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.17 | 21/46 (Hs 766T, A549, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 5 µM |  | 1.22× | +3.1 | 0.21 | 9/49 (NCI-H1792, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5664.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.364×** | -21.6 | 0e+00 | 45/47 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.300×** | -17.5 | 0e+00 | 42/46 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.316×** | -16.8 | 0e+00 | 44/47 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.386×** | -14.4 | 1e-44 | 44/47 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.395×** | -14.0 | 9e-43 | 41/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.415×** | -13.3 | 2e-38 | 38/47 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.196×** | -12.9 | 4e-36 | 42/47 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.207×** | -12.5 | 9e-34 | 45/48 (KATO III, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.470×** | -10.5 | 5e-24 | 35/47 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.521×** | -9.8 | 4e-21 | 40/47 (KATO III, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.538×** | -9.4 | 4e-19 | 34/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.594×** | -7.9 | 2e-13 | 35/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.570×** | -7.8 | 2e-13 | 36/47 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.647×** | -6.6 | 2e-09 | 32/47 (KATO III, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.670×** | -6.0 | 6e-08 | 32/47 (HT-29, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.511×** | -5.3 | 4e-06 | 30/47 (A498, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.661×** | -4.5 | 2e-04 | 24/47 (NCI-H460, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.756×** | -4.2 | 6e-04 | 23/47 (HT-29, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.832×** | -3.9 | 0.002 | 18/48 (HT-29, C32, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.627×** | -3.7 | 0.005 | 23/47 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.780×** | -3.4 | 0.011 | 21/47 (SW1417, A549, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.649×** | -3.4 | 0.012 | 20/47 (KATO III, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.817×** | -2.9 | 0.058 | 10/48 (NCI-H460, SNU-423, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 157 | 0 | 21 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -31.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.250× (z -16.9) |
| [[KATO III (line)]] | alt | 273 | 0 | 17 (11 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0541× (z -30.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.0465× (z -17.7) |
| [[LS 180 (line)]] | wt | 192 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -19.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.162× (z -18.1) |
| [[SW480 (line)]] | alt | 76.8 | 0 | 13 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.175× (z -19.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.294× (z -13.8) |
| [[COLO 205 (line)]] | alt | 309 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -29.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 66.4 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.193× (z -13.7) |
| [[A549 (line)]] | wt | 89.9 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -21.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.167× (z -13.7) |
| [[C32 (line)]] | wt | 98.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.191× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 59.3 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 86.6 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.347× (z -10.8) |
| [[A498 (line)]] | wt | 201 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -14.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.251× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 390 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.306× (z -13.5) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.373× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 72.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -21.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.230× (z -10.6) |
| [[H4 (line)]] | wt | 53.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0789× (z -16.7) |
| [[HCT15 (line)]] | alt | 105 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0895× (z -19.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.282× (z -10.3) |
| [[HT-29 (line)]] | alt | 47.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -19.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.246× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 33.8 | 1 (1 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.88× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.301× (z -10.0) |
| [[BT-474 (line)]] | alt | 41.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 69.7 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.208× (z -14.9) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.133× (z -10.4) |
| [[HS-578T (line)]] | alt | 49.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -15.8) |
| [[PANC-1 (line)]] | alt | 26.8 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 65.8 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0922× (z -19.0) |
| [[A-427 (line)]] | wt | 25.6 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.261× (z -9.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0791× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 55.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -16.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -10.5) |
| [[Hs 766T (line)]] | wt | 60.4 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.201× (z -11.0) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 68.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.249× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 48.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -15.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -14.6) |
| [[SW 900 (line)]] | alt | 39.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -15.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0992× (z -14.6) |
| [[A-172 (line)]] | wt | 81.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.133× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 62.8 | 0 | 3 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0690× (z -10.2) |
| [[SNU-1 (line)]] | wt | 63.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -19.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0654× (z -9.4) |
| [[SNU-423 (line)]] | alt | 44.8 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -13.4) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.0533× (z -11.4) |
| [[SW48 (line)]] | wt | 71.2 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0344× (z -11.7) |
| [[C-33 A (line)]] | alt | 87.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 45.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 49.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.225× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0846× (z -8.8) |
| [[SW 1271 (line)]] | alt | 68.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0670× (z -10.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.400× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 86.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02937]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[IQCJ]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[BCO2]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TNNI3K]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[GRK3]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[FTX]] | +0.54 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[RAPGEF4]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[DNHD1]] | +0.53 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[FRZB]] | +0.53 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MGAM]] | +0.53 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[KAZN]] | +0.53 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[LINC02649]] | +0.53 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF708]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SAAL1]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[TRIM32]] | -0.49 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[ZNF16]] | -0.48 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ZNF18]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CHAMP1]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[AADAT]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[OSGEP]] | -0.47 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[C12orf4]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PDSS1]] | -0.46 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[AGK]] | -0.45 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[ZNF180]] | -0.45 | -0.35 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYCP2L]] | B | SYCP2L activity raises CCDC146's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 2.36× lower at baseline in the lines without SYCP2L | 0.010 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[RAPGEF4]] | B | RAPGEF4 activity raises CCDC146's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without RAPGEF4 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[CORIN]] | B | CORIN activity raises CCDC146's level | lines that do not express CORIN (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without CORIN | 0.093 | ⚠ within organs, on part of the lines; also absent: TNNI3K, WDR49, ENSG00000229195; maybe low, not absent |
| [[LINC02656]] | C | LINC02656 activity raises CCDC146's level | lines that do not express LINC02656 (4) vs lines expressing it (46) | 2.82× lower at baseline in the lines without LINC02656 | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, MAP3K8, ENSG00000250842; maybe low, not absent |
| [[WDR49]] | C | WDR49 activity raises CCDC146's level | lines that do not express WDR49 (3) vs lines expressing it (47) | 2.18× lower at baseline in the lines without WDR49 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FOXP1, ENSG00000286952, CORIN; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.3, -18.2); signed map (8.2, 7.5). **Vector** length 92.3, 29.0% of its response variance represented; |z| ≥ 3 in 1,303 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | +2.9 | -5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | -0.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | -1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.4 | -17.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.1 | -7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -12.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -12.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 146 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:77,122,434-77,329,533 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1505, MBO2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYE0](https://www.uniprot.org/uniprotkb/Q8IYE0) (Coiled-coil domain-containing protein 146):

> Essential for sperm flagellum biogenesis and male fertility.

**Summary**, from NCBI Gene [57639](https://www.ncbi.nlm.nih.gov/gene/57639):

> Involved in spermatid development. Located in several cellular components, including microtubule organizing center; midbody; and sperm flagellum. Implicated in spermatogenic failure 94. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29296) · Entrez [57639](https://www.ncbi.nlm.nih.gov/gene/57639) · UniProt [Q8IYE0](https://www.uniprot.org/uniprotkb/Q8IYE0) · Ensembl [ENSG00000135205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135205)

## Data

Gene col 5664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5664); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5664]; `tensor/DDL_lfc|DDL_z.npy` [5664]; `embed/gene_vectors.npy` [5664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5664 or target_col == 5664). Every well: [[CCDC146 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC146.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
