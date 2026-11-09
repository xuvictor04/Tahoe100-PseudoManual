---
symbol: "GATAD2B"
type: "gene"
col: 6779
ensembl_id: "ENSG00000143614"
name: "GATA zinc finger domain containing 2B"
location: "1q21.3"
module: 145
arm: "+"
pooled_cpm: 178.46
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 18
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# GATAD2B

*GATA zinc finger domain containing 2B* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.27× (z +22.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.481× (z -19.4, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.507× (z -9.8, q 2e-20, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX8]] (+0.70, fdr 3e-05), [[ZER1]] (+0.64, fdr 4e-05), [[HAGH]] (+0.62, fdr 1e-05); moves opposite to [[MRPL30]] (-0.57, fdr 6e-05), [[ACAD11]] (-0.56, fdr 1e-05), [[AFAP1-AS1]] (-0.51, fdr 5e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.27×** | +22.5 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +19.1 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.86×** | +17.1 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.83×** | +16.6 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +16.0 | 0e+00 | 45/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +14.7 | 0e+00 | 38/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +14.5 | 1e-45 | 45/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.73×** | +14.4 | 3e-45 | 47/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +13.1 | 2e-37 | 44/48 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +9.3 | 6e-19 | 39/48 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +8.6 | 4e-16 | 38/48 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +8.6 | 5e-16 | 39/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +7.5 | 3e-12 | 35/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +6.7 | 9e-10 | 30/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +6.7 | 1e-09 | 26/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +6.3 | 9e-09 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +5.9 | 1e-07 | 26/48 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6779.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -19.4 | 0e+00 | 39/44 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.501×** | -19.0 | 0e+00 | 47/49 (NCI-H23, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.540×** | -16.9 | 0e+00 | 46/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.651×** | -10.9 | 2e-25 | 33/45 (C32, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.507×** | -9.8 | 2e-20 | 44/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.543×** | -8.8 | 2e-16 | 42/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.547×** | -8.7 | 3e-16 | 43/48 (NCI-H2347, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.572×** | -8.0 | 6e-14 | 40/48 (NCI-H2347, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.637×** | -6.5 | 5e-09 | 41/48 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.830×** | -4.9 | 6e-05 | 23/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.744×** | -4.4 | 5e-04 | 27/48 (LoVo, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.898× | -4.2 | 0.001 | 15/48 (C32, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[EX229 (drug)]] 0.5 µM |  | **0.764×** | -4.0 | 0.002 | 25/49 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | 0.868× | -3.9 | 0.004 | 19/48 (NCI-H460, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **0.762×** | -3.9 | 0.004 | 20/47 (PANC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.869× | -3.7 | 0.007 | 15/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.813×** | -3.0 | 0.087 | 16/49 (NCI-H2347, A498, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.822×** | -2.9 | 0.099 | 18/48 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 209 | 17 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -19.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 210 | 5 (1 ⚠) | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +13.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.373× (z -18.6) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.382× (z -9.5) |
| [[SW480 (line)]] | alt | 168 | 11 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +22.3) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -14.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 114 | 10 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +17.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.408× (z -13.0) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 125 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +20.6) | — |
| [[LoVo (line)]] | wt | 135 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +18.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.479× (z -12.5) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 138 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +17.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.461× (z -13.7) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 111 | 7 (1 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.47× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.503× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 154 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.429× (z -9.5) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 128 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +18.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.534× (z -8.6) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 100 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +16.4) | — |
| [[NCI-H1792 (line)]] | alt | 222 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -20.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 458 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -32.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 271 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -18.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 179 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -11.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 201 | 5 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +13.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.365× (z -15.1) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 165 | 4 | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 4.27× (z +12.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.534× (z -10.2) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 127 | 5 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.23× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.12× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 236 | 1 | 6 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 3.75× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.642× (z -9.2) |
| [[HT-29 (line)]] | alt | 202 | 3 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.98× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -17.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 202 | 2 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 1.84× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -17.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 133 | 5 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -14.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 210 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -18.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 297 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -16.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 196 | 4 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.90× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.86× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -12.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 96.2 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.56× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.50× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 135 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 120 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 165 | 2 (1 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 1.76× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -14.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 191 | 4 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -22.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 189 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -16.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 202 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -17.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 283 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -13.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 129 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 192 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -14.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 297 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -16.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 152 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.32× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -11.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 183 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.492× (z -12.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 125 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 195 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -24.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 165 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.439× (z -8.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 210 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -13.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 159 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -16.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 206 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 186 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.267× (z -8.7) |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 11 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX8]] | +0.70 | +0.44 / +0.71 | both halves | 3e-05 | **novel candidate** |
| [[ZER1]] | +0.64 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[HAGH]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PIP5K1C]] | +0.59 | +0.52 / +0.45 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers |
| [[TMEM50A]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[FBXL20]] | +0.56 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[MAP3K3]] | +0.56 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[UBALD1]] | +0.56 | +0.20 / +0.67 | ⚠ one half (not replicated) | 8e-04 |  |
| [[UBE2W]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[MARK2]] | +0.55 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MOB2]] | +0.55 | +0.20 / +0.60 | ⚠ one half (not replicated) | 8e-04 |  |
| [[UBALD2]] | +0.55 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[FOXK1]] | +0.54 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[SPSB3]] | +0.53 | +0.26 / +0.57 | both halves | 4e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL30]] | -0.57 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[ACAD11]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[AFAP1-AS1]] | -0.51 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[UCHL5]] | -0.50 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[SRP72]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[UBA5]] | -0.48 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[SNX5]] | -0.46 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[DDX39B]] | -0.46 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[STEAP2]] | -0.46 | -0.19 / -0.49 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.0, -43.1); signed map (-18.7, 12.5). **Vector** length 110, 39.7% of its response variance represented; |z| ≥ 3 in 1,588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.4 | +7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +19.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +14.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.8 | +17.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +13.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.2 | +1.6 |
|  | [[Sodium Salicylate (drug)]] 5 µM |  | +2.8 | +0.7 |
|  | [[Resveratrol (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.5 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.5 | -16.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -9.4 | -9.8 |
|  | [[EX229 (drug)]] 5 µM |  | -9.0 | -6.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.7 | -8.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.6 | -8.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -7.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | GATA zinc finger domain containing 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,789,030-153,923,360 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P66beta |
| Gene groups (HGNC) | GATA zinc finger domain containing; NuRD complex subunits |
| Reactome | 31 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; ERCC6 (CSB) and EHMT2 (G9a) positively regulate rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXI9](https://www.uniprot.org/uniprotkb/Q8WXI9) (Transcriptional repressor p66-beta):

> Transcriptional repressor. Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. Enhances MBD2-mediated repression. Efficient repression requires the presence of GATAD2A. Targets MBD3 to discrete loci in the nucleus. May play a role in synapse development.

**Summary**, from NCBI Gene [57459](https://www.ncbi.nlm.nih.gov/gene/57459):

> This gene encodes a zinc finger protein transcriptional repressor. The encoded protein is part of the methyl-CpG-binding protein-1 complex, which represses gene expression by deacetylating methylated nucleosomes. Mutations in this gene are linked to intellectual disability and dysmorphic features associated with cognitive disability. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:30778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30778) · Entrez [57459](https://www.ncbi.nlm.nih.gov/gene/57459) · UniProt [Q8WXI9](https://www.uniprot.org/uniprotkb/Q8WXI9) · Ensembl [ENSG00000143614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143614)

## Data

Gene col 6779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6779); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6779]; `tensor/DDL_lfc|DDL_z.npy` [6779]; `embed/gene_vectors.npy` [6779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6779 or target_col == 6779). Every well: [[GATAD2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATAD2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
