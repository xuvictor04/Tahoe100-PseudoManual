---
symbol: "TFDP2"
type: "gene"
col: 3528
ensembl_id: "ENSG00000114126"
name: "transcription factor Dp-2"
location: "3q23"
module: 76
arm: "+"
pooled_cpm: 164.6
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 28
n_dd_up_clean: 14
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# TFDP2

*transcription factor Dp-2* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.40× (z +27.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.329× (z -34.3, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.532× (z -27.6, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACL1]] (+0.75, fdr 7e-06), [[PLEKHM3]] (+0.71, fdr 1e-05), [[RALBP1]] (+0.64, fdr 1e-05); moves opposite to [[ARCN1]] (-0.53, fdr 3e-05), [[CYREN]] (-0.53, fdr 3e-05), [[CYCS]] (-0.52, fdr 2e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARHGAP44]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.40×** | +27.1 | 0e+00 | 48/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.12×** | +22.0 | 0e+00 | 47/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.96×** | +20.8 | 0e+00 | 46/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +16.0 | 0e+00 | 40/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +15.2 | 0e+00 | 39/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +13.9 | 9e-42 | 35/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.32×** | +12.3 | 1e-32 | 35/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +12.0 | 4e-31 | 44/45 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.68×** | +11.4 | 3e-28 | 45/49 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +9.8 | 1e-20 | 36/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +8.9 | 2e-17 | 32/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +6.9 | 3e-10 | 31/49 (NCI-H2347, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.23×** | +6.3 | 1e-08 | 24/48 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +5.4 | 3e-06 | 11/48 (H4, NCI-H23, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 19/47 (C32, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.002 | 21/49 (NCI-H460, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.14× | +4.0 | 0.002 | 8/48 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.13× | +3.9 | 0.003 | 17/48 (A498, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.329×** | -34.3 | 0e+00 | 48/48 (HEC-1-A, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.532×** | -27.6 | 0e+00 | 38/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.494×** | -21.0 | 0e+00 | 44/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.510×** | -20.8 | 0e+00 | 45/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.300×** | -19.3 | 0e+00 | 47/48 (HEC-1-A, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.466×** | -16.8 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.587×** | -16.5 | 0e+00 | 42/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.372×** | -15.9 | 0e+00 | 46/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.586×** | -15.6 | 0e+00 | 47/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.384×** | -15.4 | 0e+00 | 44/48 (Panc 03.27, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.397×** | -14.9 | 0e+00 | 47/48 (Panc 03.27, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.412×** | -14.3 | 2e-44 | 44/49 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.414×** | -14.2 | 5e-44 | 45/48 (Panc 03.27, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.684×** | -11.3 | 7e-28 | 28/44 (NCI-H23, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.680×** | -11.0 | 1e-26 | 32/45 (MIA PaCa-2, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -10.5 | 3e-24 | 34/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.713×** | -9.9 | 2e-21 | 38/48 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.645×** | -9.7 | 1e-20 | 44/49 (LOX-IMVI, HEC-1-A, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 271 | 3 | 18 (6 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +11.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.213× (z -26.8) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.182× (z -15.4) |
| [[HOP62 (line)]] | alt | 157 | 6 | 13 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.31× (z +17.9) | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -26.4) |
| [[SW480 (line)]] | alt | 171 | 4 | 15 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +17.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.230× (z -27.0) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.307× (z -21.7) |
| [[A-172 (line)]] | wt | 164 | 5 | 13 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +14.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.184× (z -25.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.361× (z -22.0) |
| [[A549 (line)]] | wt | 173 | 4 | 13 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.40× (z +18.0) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -22.4) |
| [[MIA PaCa-2 (line)]] | alt | 389 | 5 (1 ⚠) | 12 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.61× (z +20.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -34.2) |
| [[PANC-1 (line)]] | alt | 217 | 5 | 11 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.83× (z +18.2) | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -25.6) |
| [[SK-MEL-2 (line)]] | alt | 312 | 3 | 13 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -34.5) |
| [[HEC-1-A (line)]] | alt | 293 | 3 | 12 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.96× (z +11.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.205× (z -27.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -13.9) |
| [[SNU-423 (line)]] | alt | 150 | 4 (1 ⚠) | 11 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.22× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -29.4) |
| [[HS-578T (line)]] | alt | 132 | 7 (1 ⚠) | 7 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.16× (z +19.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.272× (z -17.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.448× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 154 | 3 | 11 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +10.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.276× (z -18.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.483× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 86.7 | 5 | 9 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.25× (z +13.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.289× (z -14.2) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.294× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 315 | 1 | 13 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.68× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.0442× (z -53.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.239× (z -36.1) |
| [[RKO (line)]] | wt | 217 | 3 | 11 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.26× (z +12.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.283× (z -18.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.441× (z -12.6) |
| [[A498 (line)]] | wt | 120 | 6 | 6 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.29× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -19.0) |
| [[SW1417 (line)]] | alt | 226 | 2 | 10 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.88× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -24.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.460× (z -14.0) |
| [[A-427 (line)]] | wt | 295 | 1 | 10 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.63× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -22.0) |
| [[J82 (line)]] | alt | 169 | 5 | 5 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.31× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -21.3) |
| [[NCI-H2347 (line)]] | alt | 109 | 7 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.05 µM 2.53× (z +13.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.387× (z -13.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.302× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 103 | 5 (1 ⚠) | 5 | [[Ixazomib citrate (drug)]] 5 µM 4.95× (z +25.4) | [[Harringtonine (drug)]] 5 µM 0.315× (z -17.6) |
| [[SNU-1 (line)]] | wt | 207 | 3 | 7 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.64× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -15.7) |
| [[AsPC-1 (line)]] | alt | 80.5 | 3 | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.231× (z -16.2) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -11.9) |
| [[KATO III (line)]] | alt | 124 | 4 | 5 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.26× (z +14.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -16.5) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.206× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 149 | 3 | 6 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.40× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.531× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 99.6 | 5 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.87× (z +12.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.191× (z -15.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0831× (z -12.1) |
| [[LoVo (line)]] | wt | 116 | 2 | 6 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.14× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.407× (z -13.2) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -10.9) |
| [[SW48 (line)]] | wt | 189 | 1 | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.41× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -15.9) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.297× (z -13.6) |
| [[C32 (line)]] | wt | 97.0 | 3 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.90× (z +14.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -14.1) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.283× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 109 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +12.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -14.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.432× (z -10.1) |
| [[HT-29 (line)]] | alt | 71.2 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.252× (z -15.2) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 157 | 3 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.52× (z +15.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.222× (z -18.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.524× (z -11.0) |
| [[AN3 CA (line)]] | alt | 316 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -16.4) |
| [[H4 (line)]] | wt | 129 | 4 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 8.22× (z +20.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.322× (z -10.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -10.7) |
| [[HCT15 (line)]] | alt | 162 | 2 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.53× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.424× (z -9.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -8.6) |
| [[SW 900 (line)]] | alt | 81.3 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.90× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -10.8) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 178 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.82× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.457× (z -9.6) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 69.2 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.46× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.348× (z -9.0) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 56.1 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.75× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.309× (z -10.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 96.5 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.89× (z +14.3) | [[EX229 (drug)]] 0.05 µM 0.368× (z -9.8) |
| [[SHP-77 (line)]] | alt | 206 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -13.8) |
| [[C-33 A (line)]] | alt | 226 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.07× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.331× (z -12.8) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 203 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -15.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 88.9 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.53× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.328× (z -10.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.4) |
| [[LS 180 (line)]] | wt | 146 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.416× (z -12.3) |
| [[NCI-H661 (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 96.9 | 0 | 1 | — | [[Omeprazole (sodium) (drug)]] 5 µM 0.0555× (z -10.1) |
| [[SW 1271 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACL1]] | +0.75 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[PLEKHM3]] | +0.71 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[RALBP1]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[COQ8A]] | +0.62 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[NIPAL3]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ERI3]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[WIPI2]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[DPY30]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[MBTPS1]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CCDC28A]] | +0.59 | +0.37 / +0.60 | both halves | 8e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[FBXL20]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ACTR6]] | +0.59 | +0.39 / +0.62 | both halves | 6e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARCN1]] | -0.53 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[CYREN]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[CYCS]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 | pathway: Apoptosis |
| [[TUG1]] | -0.52 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[SCAF1]] | -0.52 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[SLC30A1]] | -0.51 | -0.65 / -0.29 | both halves | 2e-04 | pathway: HALLMARK_HEME_METABOLISM |
| [[SEC23B]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MCTS1]] | -0.51 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[LIG4]] | -0.50 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[SECISBP2]] | -0.50 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[ZNF34]] | -0.50 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | -0.50 | -0.52 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP44]] | B | ARHGAP44 activity raises TFDP2's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.44× lower at baseline in the lines without ARHGAP44 | 0.053 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.2, -46.8); signed map (-19.6, 8.6). **Vector** length 158, 58.1% of its response variance represented; |z| ≥ 3 in 2,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +17.5 | +27.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +15.7 | +22.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +14.1 | +20.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +9.4 | +12.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +8.5 | +11.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Resveratrol (drug)]] 5 µM |  | +3.1 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -17.4 | -34.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -13.3 | -19.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -13.3 | -20.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -11.4 | -15.9 |
|  | [[EX229 (drug)]] 5 µM |  | -11.2 | -15.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.7 | -14.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -10.3 | -14.9 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor Dp-2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:141,944,428-142,149,544 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Dp-2 |
| Gene groups (HGNC) | Transcription factor Dp family; DREAM complex subunits |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 42 pathways, smallest: Activation of NOXA and translocation to mitochondria; Activation of PUMA and translocation to mitochondria; Inhibition of replication initiation of damaged DNA by RB1/E2F1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14188](https://www.uniprot.org/uniprotkb/Q14188) (Transcription factor Dp-2):

> Can stimulate E2F-dependent transcription. Binds DNA cooperatively with E2F family members through the E2 recognition site, 5'-TTTC[CG]CGC-3', found in the promoter region of a number of genes whose products are involved in cell cycle regulation or in DNA replication. The TFDP2:E2F complex functions in the control of cell-cycle progression from G1 to S phase. The E2F1:DP complex appears to mediate both cell proliferation and apoptosis. Blocks adipocyte differentiation by repressing CEBPA …

**Summary**, from NCBI Gene [7029](https://www.ncbi.nlm.nih.gov/gene/7029):

> The gene is a member of the transcription factor DP family. The encoded protein forms heterodimers with the E2F transcription factors resulting in transcriptional activation of cell cycle regulated genes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:11751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11751) · Entrez [7029](https://www.ncbi.nlm.nih.gov/gene/7029) · UniProt [Q14188](https://www.uniprot.org/uniprotkb/Q14188) · Ensembl [ENSG00000114126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114126)

## Data

Gene col 3528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3528); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3528]; `tensor/DDL_lfc|DDL_z.npy` [3528]; `embed/gene_vectors.npy` [3528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3528 or target_col == 3528). Every well: [[TFDP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFDP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
