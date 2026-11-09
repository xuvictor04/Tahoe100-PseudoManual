---
symbol: "IPO7"
type: "gene"
col: 12969
ensembl_id: "ENSG00000205339"
name: "importin 7"
location: "11p15.4"
module: 4
arm: "+"
pooled_cpm: 286.06
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# IPO7

*importin 7* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (20 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 2.10× (z +13.9, q 6e-41, up in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.63× (z +11.1, q 1e-26, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.735× (z -5.8, q 5e-06, down in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.747×, MIA PaCa-2 0.741×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.561×; ⚠ cell-cycle shift, explains ~42% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (A-427 0.626×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKDC]] (+0.75, fdr 7e-06), [[IPO5]] (+0.71, fdr 7e-06), [[LRPPRC]] (+0.70, fdr 7e-06); moves opposite to [[TTI2]] (-0.73, fdr 7e-06), [[THAP3]] (-0.67, fdr 1e-05), [[PI4KB]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 26 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +13.9 | 6e-41 | 45/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.68×** | +11.9 | 5e-30 | 41/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.43×** | +11.5 | 2e-28 | 30/48 (NCI-H1573, AsPC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.63×** | +11.1 | 1e-26 | 39/49 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +11.1 | 1e-26 | 37/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.53×** | +9.7 | 2e-20 | 37/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +9.7 | 3e-20 | 39/48 (Hs 766T, HT-29, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.59×** | +9.2 | 3e-18 | 41/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +8.7 | 2e-16 | 37/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +8.4 | 2e-15 | 44/49 (SNU-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.55×** | +8.2 | 1e-14 | 33/44 (NCI-H1792, HCT15, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +8.1 | 2e-14 | 40/48 (RKO, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.49×** | +8.0 | 8e-14 | 38/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.39×** | +7.5 | 3e-12 | 34/48 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.37×** | +7.1 | 4e-11 | 34/48 (A-172, SNU-423, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +5.9 | 9e-08 | 29/48 (AN3 CA, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 4e-06 | 31/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.30×** | +4.9 | 2e-05 | 34/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 9e-05 | 28/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +4.6 | 9e-05 | 31/48 (HEC-1-A, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +4.6 | 9e-05 | 31/48 (A498, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +4.5 | 2e-04 | 30/48 (HT-29, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.3 | 3e-04 | 14/49 (AN3 CA, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 4e-04 | 28/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.20× | +4.1 | 7e-04 | 21/47 (NCI-H23, MIA PaCa-2, …) | two highest doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.006 | 15/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12969.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.747×, MIA PaCa-2 0.741×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.561×; ⚠ cell-cycle shift, explains ~42% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (A-427 0.626×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.735×** | -5.8 | 5e-06 | 34/47 (A-427, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.811×** | -4.9 | 3e-04 | 25/50 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.828×** | -4.3 | 0.003 | 23/48 (A-427, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.875× | -4.2 | 0.003 | 14/48 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.836× | -4.1 | 0.005 | 20/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.849× | -3.7 | 0.017 | 18/47 (SK-MEL-2, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.867× | -3.7 | 0.018 | 14/48 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.895× | -3.6 | 0.018 | 17/48 (LS 180, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.834× | -3.6 | 0.018 | 22/48 (KATO III, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.868× | -3.6 | 0.018 | 16/48 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.848× | -3.6 | 0.018 | 19/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.849× | -3.5 | 0.026 | 17/49 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.865× | -3.3 | 0.037 | 9/48 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.840× | -3.3 | 0.044 | 18/48 (HepG2/C3A, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.851× | -3.2 | 0.048 | 14/48 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.904× | -3.2 | 0.058 | 7/49 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.848× | -3.1 | 0.070 | 13/49 (CFPAC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 256 | 11 (9 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.55× (z +14.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.84× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 248 | 11 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 175 | 9 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.56× (z +17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.33× (z +17.0) | — |
| [[NCI-H1792 (line)]] | alt | 183 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.56× (z +10.2) | — |
| [[SW480 (line)]] | alt | 401 | 8 (8 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.21× (z +11.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 105 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 116 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +16.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.91× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 218 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[AsPC-1 (line)]] | alt | 302 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +17.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 248 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 324 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 383 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.1) ⚠ cell-cycle shift, explains ~42% of this change | [[Trametinib (drug)]] 5 µM 0.597× (z -8.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[Panc 03.27 (line)]] | alt | 154 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.1) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SNU-1 (line)]] | wt | 258 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.29× (z +9.5) | — |
| [[A-172 (line)]] | wt | 173 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.22× (z +10.4) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[A549 (line)]] | wt | 312 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +15.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.13× (z +9.6) | — |
| [[C32 (line)]] | wt | 176 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 173 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.59× (z +9.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +9.1) | — |
| [[LoVo (line)]] | wt | 299 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.55× (z +13.9) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 360 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[RKO (line)]] | wt | 287 | 3 (2 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.72× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 190 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +11.0) | — |
| [[A498 (line)]] | wt | 308 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.76× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 411 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.90× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -11.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[LS 180 (line)]] | wt | 207 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.53× (z +11.8) ⚠ toxic | — |
| [[A-427 (line)]] | wt | 583 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.626× (z -9.0) |
| [[AN3 CA (line)]] | alt | 345 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.66× (z +9.5) | — |
| [[H4 (line)]] | wt | 210 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.45× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 254 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[HepG2_C3A (line)]] | wt | 268 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.25× (z +8.8) ⚠ toxic | — |
| [[hTERT-HPNE (line)]] | wt | 198 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +9.9) | — |
| [[KATO III (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +9.4) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2347 (line)]] | alt | 203 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.8) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[PANC-1 (line)]] | alt | 560 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.63× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.40× (z +9.6) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 304 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.16× (z +9.1) ⚠ toxic | — |
| [[BT-474 (line)]] | alt | 390 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 322 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 394 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 338 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 369 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 356 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | +0.75 | +0.72 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[IPO5]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 | same gene group; STRING 884 |
| [[LRPPRC]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[AHCY]] | +0.68 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[XRN2]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[SERBP1]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CCT5]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[GSPT1]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ATIC]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CCT2]] | +0.63 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[NSUN2]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[GART]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTI2]] | -0.73 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[THAP3]] | -0.67 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[PI4KB]] | -0.66 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.65 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.65 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[SAT2]] | -0.64 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[ZNF44]] | -0.63 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ZNF226]] | -0.62 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[APBA3]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[NAA38]] | -0.62 | -0.57 / -0.60 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[MRPS18C]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[TIMM29]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises IPO7's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.5, -30.9); signed map (-20.3, -45.1). **Vector** length 106, 41.4% of its response variance represented; |z| ≥ 3 in 1,665 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +9.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.5 | +13.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.2 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.9 | +6.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.5 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.8 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.0 | +2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -4.6 | +9.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.3 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.1 | +11.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.6 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | importin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:9,384,652-9,448,127 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Imp7; previously RANBP7 |
| Gene groups (HGNC) | Importins; Small nucleolar RNA protein coding host genes |
| Hallmark sets | E2F_TARGETS |
| Reactome | 4 pathways, smallest: Maturation of DENV proteins; Dengue Virus Genome Translation and Replication; Dengue Virus Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [O95373](https://www.uniprot.org/uniprotkb/O95373) (Importin-7):

> Functions in nuclear protein import, either by acting as autonomous nuclear transport receptor or as an adapter-like protein in association with the importin-beta subunit KPNB1. Acting autonomously, is thought to serve itself as receptor for nuclear localization signals (NLS) and to promote translocation of import substrates through the nuclear pore complex (NPC) by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to importin, the importin/substrate …

**Summary**, from NCBI Gene [10527](https://www.ncbi.nlm.nih.gov/gene/10527):

> The importin-alpha/beta complex and the GTPase Ran mediate nuclear import of proteins with a classical nuclear localization signal. The protein encoded by this gene is a member of a class of approximately 20 potential Ran targets that share a sequence motif related to the Ran-binding site of importin-beta. Similar to importin-beta, this protein prevents the activation of Ran's GTPase by RanGAP1 and inhibits nucleotide exchange on RanGTP, and also binds directly to nuclear pore complexes where …

**Accessions** — [HGNC:9852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9852) · Entrez [10527](https://www.ncbi.nlm.nih.gov/gene/10527) · UniProt [O95373](https://www.uniprot.org/uniprotkb/O95373) · Ensembl [ENSG00000205339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205339)

## Data

Gene col 12969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12969); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12969]; `tensor/DDL_lfc|DDL_z.npy` [12969]; `embed/gene_vectors.npy` [12969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12969 or target_col == 12969). Every well: [[IPO7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPO7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
