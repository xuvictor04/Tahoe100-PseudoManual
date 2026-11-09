---
symbol: "SMARCA4"
type: "gene"
col: 4827
ensembl_id: "ENSG00000127616"
name: "SWI/SNF related BAF chromatin remodeling complex subunit ATPase 4"
location: "19p13.2"
module: 4
arm: "+"
pooled_cpm: 134.57
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SMARCA4

*SWI/SNF related BAF chromatin remodeling complex subunit ATPase 4* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.79× (z +14.3, q 2e-43, up in 33 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.21× (z +4.6, q 3e-04, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.724× (z -11.6, q 2e-28, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC57]] (+0.65, fdr 1e-05), [[ANAPC7]] (+0.64, fdr 1e-05), [[SERBP1]] (+0.63, fdr 1e-05); moves opposite to [[MKRN1]] (-0.67, fdr 7e-06), [[SMPDL3A]] (-0.60, fdr 1e-05), [[TMEM59]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.79×** | +14.3 | 2e-43 | 33/43 (A498, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.73×** | +13.9 | 2e-41 | 39/48 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.36×** | +7.5 | 1e-11 | 34/47 (A498, A-172, …) | rises with dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +7.2 | 8e-11 | 35/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +6.5 | 1e-08 | 22/47 (A498, A-172, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.31×** | +6.3 | 2e-08 | 27/44 (SNU-423, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.27×** | +6.1 | 8e-08 | 28/47 (PANC-1, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.24×** | +5.4 | 4e-06 | 30/47 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.22×** | +5.0 | 4e-05 | 24/47 (PANC-1, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.21×** | +4.8 | 1e-04 | 25/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +4.6 | 3e-04 | 24/47 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.19× | +4.0 | 0.003 | 19/47 (BT-474, AN3 CA, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.004 | 19/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.014 | 18/47 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.025 | 20/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.025 | 18/47 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.4 | 0.025 | 11/47 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.028 | 20/47 (C32, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.030 | 9/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.030 | 14/46 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.062 | 5/47 (LoVo, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -11.6 | 2e-28 | 36/48 (SW48, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.726×** | -11.5 | 4e-28 | 36/47 (J82, RKO, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -7.1 | 3e-10 | 30/47 (HS-578T, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.781×** | -6.3 | 4e-08 | 29/47 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.800×** | -5.7 | 2e-06 | 30/47 (KATO III, SW48, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | **0.806×** | -5.3 | 1e-05 | 26/46 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.830×** | -4.7 | 2e-04 | 24/47 (C-33 A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.877× | -4.7 | 2e-04 | 10/47 (LOX-IMVI, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -4.5 | 4e-04 | 21/47 (C-33 A, BT-474, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.887× | -4.3 | 8e-04 | 20/47 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.854× | -4.0 | 0.003 | 19/48 (SW1417, BT-474, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.868× | -3.6 | 0.015 | 13/47 (KATO III, SW 1088, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.6 | 0.017 | 17/49 (C-33 A, LS 180, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.772×** | -3.4 | 0.024 | 18/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.897× | -3.4 | 0.025 | 10/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.874× | -3.2 | 0.050 | 11/47 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | 0.883× | -3.0 | 0.072 | 13/46 (BT-474, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 155 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +18.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 101 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 2.25× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 104 | 3 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.532× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.540× (z -9.6) |
| [[A-172 (line)]] | wt | 221 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +15.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 268 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 129 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Selinexor (drug)]] 5 µM 0.618× (z -10.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 124 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HCT15 (line)]] | alt | 236 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 100 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Selinexor (drug)]] 5 µM 0.572× (z -10.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 210 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.475× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 108 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Selinexor (drug)]] 5 µM 0.544× (z -9.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 36.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 97.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 159 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.570× (z -12.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -12.1) |
| [[HT-29 (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[J82 (line)]] | alt | 146 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Selinexor (drug)]] 5 µM 0.379× (z -20.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[KATO III (line)]] | alt | 83.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 161 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 134 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -8.9) |
| [[RKO (line)]] | wt | 233 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.482× (z -14.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -9.3) |
| [[SHP-77 (line)]] | alt | 166 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-1 (line)]] | wt | 182 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.592× (z -9.1) |
| [[SW480 (line)]] | alt | 198 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 67.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 298 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.512× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 53.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.630× (z -11.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HOP62 (line)]] | alt | 95.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 176 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.398× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 259 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -15.4) |
| [[AN3 CA (line)]] | alt | 286 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 133 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 148 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC57]] | +0.65 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ANAPC7]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SERBP1]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[DDX10]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[CEP83]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[NOP14]] | +0.61 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[NAA15]] | +0.61 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[NOM1]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TAF1B]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[PPRC1]] | +0.58 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[EIF4G3]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[NF2]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN1]] | -0.67 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[SMPDL3A]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PCMTD1]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[RTCA-AS1]] | -0.58 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[DUSP11]] | -0.57 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[MICA]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZNF836]] | -0.57 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[MRPS22]] | -0.56 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[NDUFAF7]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CPEB3]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[CLK1]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.458). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.4, -38.9); signed map (-6.0, -48.0). **Vector** length 109, 30.7% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | +6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.8 | +14.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -8.8 | -11.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -11.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -3.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -5.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.0 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.5 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | SWI/SNF related BAF chromatin remodeling complex subunit ATPase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,960,932-11,079,426 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hSNF2b, BRG1, BAF190, SNF2, SWI2, SNF2-BETA, SNF2LB, FLJ39786; previously SNF2L4 |
| Gene groups (HGNC) | SNF2 related family; Bromodomain containing; BAF complex subunits; PBAF complex subunits; GBAF complex subunits |
| Reactome | 41 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; Formation of the canonical BAF (cBAF) complex; Formation of the polybromo-BAF (pBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P51532](https://www.uniprot.org/uniprotkb/P51532) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A member 4):

> ATPase involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Component of the CREST-BRG1 complex, a multiprotein complex that regulates promoter activation by orchestrating the calcium-dependent release of a …

**Summary**, from NCBI Gene [6597](https://www.ncbi.nlm.nih.gov/gene/6597):

> The protein encoded by this gene is a member of the SWI/SNF family of proteins and is similar to the brahma protein of Drosophila. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI, which is required for transcriptional activation of genes normally repressed by chromatin. In …

**Accessions** — [HGNC:11100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11100) · Entrez [6597](https://www.ncbi.nlm.nih.gov/gene/6597) · UniProt [P51532](https://www.uniprot.org/uniprotkb/P51532) · Ensembl [ENSG00000127616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127616)

## Data

Gene col 4827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4827); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4827]; `tensor/DDL_lfc|DDL_z.npy` [4827]; `embed/gene_vectors.npy` [4827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4827 or target_col == 4827). Every well: [[SMARCA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
