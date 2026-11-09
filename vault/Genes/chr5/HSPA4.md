---
symbol: "HSPA4"
type: "gene"
col: 9981
ensembl_id: "ENSG00000170606"
name: "heat shock protein family A (Hsp70) member 4"
location: "5q31.1"
module: 60
arm: "+"
pooled_cpm: 133.15
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSPA4

*heat shock protein family A (Hsp70) member 4* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (23 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.98× (z +26.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.825× (z -3.7, q 0.093, down in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.755×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LARP4]] (+0.72, fdr 7e-06), [[CCT5]] (+0.70, fdr 7e-06), [[IDE]] (+0.69, fdr 7e-06); moves opposite to [[SIRT2]] (-0.61, fdr 1e-05), [[WDR47]] (-0.58, fdr 3e-05), [[EFHC1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 25 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.98×** | +26.7 | 0e+00 | 48/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.39×** | +23.9 | 0e+00 | 45/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.31×** | +23.2 | 0e+00 | 48/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.92×** | +20.8 | 0e+00 | 48/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.11×** | +20.8 | 0e+00 | 48/48 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.90×** | +20.6 | 0e+00 | 48/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.90×** | +20.6 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.59×** | +18.5 | 0e+00 | 46/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.64×** | +18.1 | 0e+00 | 47/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.31×** | +16.2 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.70×** | +15.7 | 0e+00 | 45/45 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +14.9 | 0e+00 | 45/49 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.10×** | +14.3 | 6e-45 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **2.11×** | +13.9 | 4e-42 | 47/47 (COLO 205, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +12.3 | 4e-33 | 44/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.42×** | +12.2 | 8e-33 | 43/49 (HOP62, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.6 | 1e-09 | 29/48 (HOP62, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +6.2 | 1e-08 | 36/48 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.84×** | +6.2 | 1e-08 | 40/48 (HOP62, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.6 | 4e-07 | 29/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.60×** | +4.8 | 3e-05 | 32/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +4.7 | 3e-05 | 33/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9981.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.755×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.825×** | -3.7 | 0.093 | 23/47 (HS-578T, BT-474, …) | two highest doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.833× | -3.5 | 0.093 | 21/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | **0.830×** | -3.5 | 0.093 | 19/48 (AsPC-1, Panc 03.27, …) | top dose only | plate-row cell shift |
| [[Adenosine (drug)]] 5 µM |  | 0.885× | -3.4 | 0.11 | 8/48 (COLO 205, SHP-77, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.839× | -3.3 | 0.12 | 18/49 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Bimiralisib (drug)]] 5 µM |  | 0.730× | -3.2 | 0.13 | 19/50 (NCI-H1573, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.846× | -3.1 | 0.15 | 12/48 (KATO III, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 97.7 | 20 (12 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.59× (z +23.0) | — |
| [[NCI-H460 (line)]] | wt | 142 | 20 (10 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.85× (z +21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 3.81× (z +18.0) | — |
| [[SNU-423 (line)]] | alt | 86.0 | 20 (12 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.51× (z +19.4) | — |
| [[SW480 (line)]] | alt | 167 | 19 (12 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.99× (z +21.0) | — |
| [[Hs 766T (line)]] | wt | 111 | 18 (11 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.65× (z +17.8) | — |
| [[PANC-1 (line)]] | alt | 150 | 18 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +21.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.26× (z +18.5) | — |
| [[HEC-1-A (line)]] | alt | 153 | 17 (9 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.31× (z +25.7) | — |
| [[HS-578T (line)]] | alt | 109 | 17 (9 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.40× (z +18.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 199 | 17 (8 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.88× (z +19.2) | — |
| [[HOP62 (line)]] | alt | 89.1 | 16 (8 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.88× (z +24.1) | — |
| [[HT-29 (line)]] | alt | 116 | 16 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +18.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.99× (z +17.4) | — |
| [[LoVo (line)]] | wt | 180 | 15 (7 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.96× (z +19.0) | — |
| [[LS 180 (line)]] | wt | 117 | 15 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.49× (z +20.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 117 | 14 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +20.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.59× (z +13.2) | — |
| [[C32 (line)]] | wt | 84.1 | 14 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.53× (z +20.9) | — |
| [[COLO 205 (line)]] | alt | 60.6 | 14 (8 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 18.1× (z +21.3) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.85× (z +12.1) | — |
| [[H4 (line)]] | wt | 86.7 | 14 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.06× (z +14.8) | — |
| [[KATO III (line)]] | alt | 79.3 | 14 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.38× (z +18.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.40× (z +16.3) | — |
| [[SK-MEL-2 (line)]] | alt | 225 | 14 (8 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.34× (z +22.6) | — |
| [[A549 (line)]] | wt | 113 | 13 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +20.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.23× (z +14.5) | — |
| [[CFPAC-1 (line)]] | alt | 66.5 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +18.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 6.65× (z +16.4) | — |
| [[NCI-H1573 (line)]] | alt | 120 | 13 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.41× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.57× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 112 | 13 (7 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.00× (z +15.6) | — |
| [[LOX-IMVI (line)]] | wt | 112 | 12 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.36× (z +17.7) | — |
| [[RPMI-7951 (line)]] | alt | 68.6 | 11 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.80× (z +13.8) | — |
| [[SNU-1 (line)]] | wt | 143 | 11 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.81× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 80.2 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +15.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.37× (z +13.9) | — |
| [[A498 (line)]] | wt | 139 | 10 (4 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 4.73× (z +16.4) | — |
| [[hTERT-HPNE (line)]] | wt | 77.5 | 10 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.31× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 126 | 10 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.25× (z +16.6) | — |
| [[SW1417 (line)]] | alt | 101 | 10 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.32× (z +16.2) | — |
| [[J82 (line)]] | alt | 116 | 9 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.32× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 46.3 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +18.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.00× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 193 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.68× (z +11.8) | — |
| [[RKO (line)]] | wt | 202 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.39× (z +16.1) | — |
| [[A-427 (line)]] | wt | 326 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.78× (z +14.4) | — |
| [[BT-474 (line)]] | alt | 85.2 | 6 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.07× (z +15.9) | — |
| [[NCI-H2030 (line)]] | alt | 183 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.38× (z +10.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.29× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 98.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +13.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.15× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 143 | 4 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.31× (z +14.0) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.53× (z +11.3) | — |
| [[SW48 (line)]] | wt | 201 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +11.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.53× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 186 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 142 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +11.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 265 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.04× (z +13.2) | — |
| [[CHP-212 (line)]] | wt | 129 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW 1271 (line)]] | alt | 170 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.17× (z +9.2) | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP4]] | +0.72 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[CCT5]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 | STRING 799 |
| [[IDE]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[CCT6A]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 761 |
| [[NAA50]] | +0.64 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CCT3]] | +0.63 | +0.66 / +0.68 | both halves | 7e-06 | STRING 837 |
| [[PSMD11]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 | STRING 558 |
| [[FBXO30]] | +0.62 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[CHORDC1]] | +0.60 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[EPM2A]] | +0.60 | +0.64 / +0.35 | both halves | 1e-04 | STRING 488 |
| [[FKBP4]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 | pathway: Cellular response to heat stress; STRING 998 |
| [[HSPH1]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 | same gene group; pathway: Cellular response to heat stress; STRING 935 |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.61 | -0.54 / -0.55 | both halves | 1e-05 | STRING 427 |
| [[WDR47]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[EFHC1]] | -0.58 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[WIPF2]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[SEC22A]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.56 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ANG]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[MINDY2]] | -0.55 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[KMT5C]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CNNM4]] | -0.54 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[ZFYVE1]] | -0.53 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[TTC21A]] | -0.53 | -0.40 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HSPA4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.558). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.8, -30.9); signed map (-11.2, -43.8). **Vector** length 78.1, 30.2% of its response variance represented; |z| ≥ 3 in 1,820 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.56 to 4); *Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +26.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.2 | +20.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.4 | +15.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +23.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +5.8 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +20.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -4.1 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.7 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.3 | +7.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -3.2 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | +0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:133,052,013-133,106,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HS24/P52, HSPH2 |
| Gene groups (HGNC) | Heat shock 70kDa proteins |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

UniProt [P34932](https://www.uniprot.org/uniprotkb/P34932) carries no function annotation.

**Summary**, from NCBI Gene [3308](https://www.ncbi.nlm.nih.gov/gene/3308):

> Predicted to enable adenyl-nucleotide exchange factor activity. Involved in chaperone-mediated protein complex assembly and protein import into mitochondrial matrix. Located in cytosol and extracellular exosome. Implicated in Chagas disease. Biomarker of chronic obstructive pulmonary disease; rheumatoid arthritis; type 2 diabetes mellitus; and ulcerative colitis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5237) · Entrez [3308](https://www.ncbi.nlm.nih.gov/gene/3308) · UniProt [P34932](https://www.uniprot.org/uniprotkb/P34932) · Ensembl [ENSG00000170606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170606)

## Data

Gene col 9981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9981); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9981]; `tensor/DDL_lfc|DDL_z.npy` [9981]; `embed/gene_vectors.npy` [9981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9981 or target_col == 9981). Every well: [[HSPA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
