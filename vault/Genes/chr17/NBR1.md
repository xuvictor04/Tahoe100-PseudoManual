---
symbol: "NBR1"
type: "gene"
col: 12023
ensembl_id: "ENSG00000188554"
name: "NBR1 autophagy cargo receptor"
location: "17q21.31"
module: 74
arm: "+"
pooled_cpm: 119.95
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 27
n_dd_up_clean: 9
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# NBR1

*NBR1 autophagy cargo receptor* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +15.2, q 0e+00, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.90× (z +11.3, q 4e-27, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.275× (z -23.4, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.287× (z -11.8, q 7e-30, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLU7]] (+0.77, fdr 7e-06), [[RSF1]] (+0.75, fdr 7e-06), [[XRN1]] (+0.72, fdr 7e-06); moves opposite to [[FAM20B]] (-0.64, fdr 1e-05), [[GARNL3]] (-0.63, fdr 1e-05), [[FAR1]] (-0.61, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12023.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.80×** | +15.2 | 0e+00 | 41/48 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +11.3 | 4e-27 | 44/48 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.67×** | +9.4 | 9e-19 | 36/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +9.1 | 2e-17 | 42/48 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.3 | 3e-08 | 30/49 (A-172, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.6 | 2e-06 | 28/44 (A-172, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.6 | 4e-04 | 30/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.5 | 4e-04 | 20/49 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 0.001 | 30/47 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 30/49 (MIA PaCa-2, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.012 | 27/48 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.012 | 28/48 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.016 | 24/47 (AsPC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.049 | 23/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | 1.18× | +3.1 | 0.067 | 19/48 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12023.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.275×** | -23.4 | 0e+00 | 47/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.287×** | -11.8 | 7e-30 | 48/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.325×** | -10.7 | 3e-24 | 47/48 (A498, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.352×** | -9.9 | 6e-21 | 46/48 (A498, A549, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.358×** | -9.7 | 2e-20 | 46/48 (COLO 205, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.360×** | -9.7 | 3e-20 | 47/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.626×** | -8.5 | 2e-15 | 42/48 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.628×** | -8.4 | 3e-15 | 38/48 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.502×** | -8.3 | 6e-15 | 47/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.687×** | -6.8 | 7e-10 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.688×** | -6.7 | 8e-10 | 35/48 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.792×** | -5.9 | 1e-07 | 29/48 (SNU-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.727×** | -5.8 | 4e-07 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.716×** | -5.7 | 5e-07 | 36/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.749×** | -5.2 | 7e-06 | 34/48 (COLO 205, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.676×** | -4.7 | 9e-05 | 37/49 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.797×** | -4.1 | 0.001 | 23/48 (SW480, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.825×** | -3.5 | 0.016 | 25/49 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Volasertib (drug)]] 0.5 µM |  | **0.752×** | -3.4 | 0.018 | 26/48 (NCI-H460, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.825×** | -3.3 | 0.027 | 24/48 (SW48, NCI-H23, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.770×** | -3.1 | 0.041 | 17/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 117 | 7 (3 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +19.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.57× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.149× (z -24.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.186× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 98.7 | 3 (1 ⚠) | 9 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.12× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.204× (z -20.9) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.409× (z -11.7) |
| [[A549 (line)]] | wt | 145 | 4 (2 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +21.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.23× (z +14.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.225× (z -19.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.210× (z -10.8) |
| [[HT-29 (line)]] | alt | 129 | 1 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.5) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.195× (z -19.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.219× (z -9.6) |
| [[RKO (line)]] | wt | 139 | 4 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.04× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.236× (z -16.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.451× (z -8.6) |
| [[A498 (line)]] | wt | 184 | 2 (2 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.260× (z -18.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.179× (z -12.1) |
| [[A-172 (line)]] | wt | 120 | 6 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +19.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.19× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.446× (z -10.2) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 120 | 4 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.03× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.296× (z -15.0) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.252× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 178 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.8) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.219× (z -20.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.259× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 109 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.57× (z +11.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.372× (z -12.8) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 120 | 0 | 6 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.242× (z -19.4) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.469× (z -10.3) |
| [[COLO 205 (line)]] | alt | 231 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.259× (z -16.8) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.217× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 122 | 3 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.8) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.294× (z -16.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.255× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 173 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.309× (z -15.1) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 138 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +15.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.23× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.307× (z -13.9) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 97.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.55× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.340× (z -11.4) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 141 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +17.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.92× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.298× (z -14.1) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 95.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.2) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.268× (z -11.5) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 99.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.64× (z +10.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -16.0) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 104 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.7) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.344× (z -13.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.264× (z -8.8) |
| [[LoVo (line)]] | wt | 95.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.44× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -17.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 107 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.3) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.306× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 150 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.60× (z +10.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.431× (z -9.6) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 139 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.291× (z -14.2) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.227× (z -8.9) |
| [[SW48 (line)]] | wt | 80.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.5) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -12.7) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 73.9 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.188× (z -16.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.116× (z -11.1) |
| [[BT-474 (line)]] | alt | 77.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.8) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.377× (z -9.3) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 90.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.0) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.200× (z -14.8) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 92.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.350× (z -10.1) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 132 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -11.0) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 197 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.256× (z -10.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.123× (z -8.7) |
| [[HCT15 (line)]] | alt | 158 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.4) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.422× (z -8.8) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 160 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.346× (z -11.7) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 94.9 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.252× (z -14.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.193× (z -9.3) |
| [[KATO III (line)]] | alt | 210 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.1) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.236× (z -14.5) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 90.7 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.223× (z -15.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.163× (z -9.7) |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Brimonidine (drug)]] 0.5 µM 0.193× (z -9.3) |
| [[PANC-1 (line)]] | alt | 71.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.1) ⚠ cell-cycle shift, explains ~30% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -15.2) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 79.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.73× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 70.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.80× (z +9.9) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.298× (z -12.0) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -13.6) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.151× (z -9.2) |
| [[AN3 CA (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.265× (z -8.7) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.395× (z -9.0) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.288× (z -14.6) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 177 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.206× (z -9.0) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 94.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -11.6) ⚠ unreliable plate only |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLU7]] | +0.77 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[RSF1]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[XRN1]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.71 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[BOD1L1]] | +0.69 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[MAT2B]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[COQ5]] | +0.68 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[WDR48]] | +0.67 | +0.45 / +0.80 | both halves | 3e-05 |  |
| [[NIPBL]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[ATG2B]] | +0.67 | +0.65 / +0.57 | both halves | 9e-06 | STRING 543 |
| [[YIPF4]] | +0.67 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[UBN2]] | +0.66 | +0.46 / +0.72 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM20B]] | -0.64 | -0.75 / -0.52 | both halves | 1e-05 |  |
| [[GARNL3]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[FAR1]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[SMG1P2]] | -0.61 | -0.71 / -0.52 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.61 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[AP3M2]] | -0.61 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[BRI3BP]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[GLB1L2]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PPAT]] | -0.59 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[COLGALT1]] | -0.58 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[MAST2]] | -0.58 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[RNGTT]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.6, -46.4); signed map (3.9, -14.9). **Vector** length 157, 56.8% of its response variance represented; |z| ≥ 3 in 1,428 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +13.7 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +12.5 | +15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +11.4 | +9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.9 | +9.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.8 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +4.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.5 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +2.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +3.8 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.4 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -20.2 | -23.4 |
|  | [[EX229 (drug)]] 5 µM |  | -13.1 | -11.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -11.3 | -10.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -11.3 | -9.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -11.2 | -9.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -10.1 | -9.9 |

## What is on record

|  |  |
|---|---|
| Name | NBR1 autophagy cargo receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,170,481-43,211,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CA125, KIAA0049, 1A1-3B; previously M17S2 |
| Gene groups (HGNC) | Zinc fingers ZZ-type |
| Reactome | 4 pathways, smallest: Pexophagy; Selective autophagy; Macroautophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14596](https://www.uniprot.org/uniprotkb/Q14596) (Next to BRCA1 gene 1 protein):

> Ubiquitin-binding autophagy adapter that participates in different processes including host defense or intracellular homeostasis. Possesses a double function during the selective autophagy by acting as a shuttle bringing ubiquitinated proteins to autophagosomes and also by participating in the formation of protein aggregates. Plays a role in the regulation of the innate immune response by modulating type I interferon production and targeting ubiquitinated IRF3 for autophagic degradation. In …

**Summary**, from NCBI Gene [4077](https://www.ncbi.nlm.nih.gov/gene/4077):

> The protein encoded by this gene was originally identified as an ovarian tumor antigen monitored in ovarian cancer. The encoded protein contains a B-box/coiled-coil motif, which is present in many genes with transformation potential. It functions as a specific autophagy receptor for the selective autophagic degradation of peroxisomes by forming intracellular inclusions with ubiquitylated autophagic substrates. This gene is located on a region of chromosome 17q21.1 that is in close proximity to …

**Accessions** — [HGNC:6746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6746) · Entrez [4077](https://www.ncbi.nlm.nih.gov/gene/4077) · UniProt [Q14596](https://www.uniprot.org/uniprotkb/Q14596) · Ensembl [ENSG00000188554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188554)

## Data

Gene col 12023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12023); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12023]; `tensor/DDL_lfc|DDL_z.npy` [12023]; `embed/gene_vectors.npy` [12023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12023 or target_col == 12023). Every well: [[NBR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
