---
symbol: "ZWILCH"
type: "gene"
col: 10492
ensembl_id: "ENSG00000174442"
name: "zwilch kinetochore protein"
location: "15q22.31"
module: 6
arm: "+"
pooled_cpm: 26.17
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ZWILCH

*zwilch kinetochore protein* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.35× (z +25.1, q 0e+00, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.21× (z +5.7, q 5e-07, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.765× (z -5.5, q 2e-05, down in 22 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.639× (z -4.9, q 3e-04, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.368×, A-427 0.404×; ⚠ cell-cycle shift, explains ~25% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (A498 0.395×, A-172 0.433×; ⚠ cell-cycle shift, explains ~74% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (H4 0.0413×; ⚠ cell-cycle shift, would explain all of this change); [[Capivasertib (drug)]] 5 µM in 1 line (RPMI-7951 0.0651×); [[Amsacrine (drug)]] 5 µM in 1 line (A498 0.507×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPH]] (+0.80, fdr 7e-06), [[CIP2A]] (+0.78, fdr 7e-06), [[VRK1]] (+0.77, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 27 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.35×** | +25.1 | 0e+00 | 42/43 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.08×** | +22.5 | 0e+00 | 31/34 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.51×** | +17.7 | 0e+00 | 34/39 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **2.07×** | +15.2 | 0e+00 | 43/48 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.91×** | +13.4 | 4e-39 | 43/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.85×** | +12.8 | 2e-35 | 41/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.52×** | +12.3 | 8e-33 | 31/47 (HS-578T, Panc 03.27, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.62×** | +9.6 | 5e-20 | 34/48 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.52×** | +8.4 | 3e-15 | 28/47 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.50×** | +8.1 | 2e-14 | 26/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +7.8 | 2e-13 | 24/47 (CFPAC-1, J82, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.42×** | +7.1 | 7e-11 | 28/48 (AsPC-1, SW480, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.33×** | +5.9 | 1e-07 | 24/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.7 | 5e-07 | 19/48 (HOP62, J82, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +5.2 | 7e-06 | 21/47 (LoVo, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 5e-05 | 15/47 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.2 | 7e-04 | 7/48 (C32, NCI-H1792, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.005 | 10/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.18× | +3.3 | 0.017 | 5/48 (A549, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.038 | 12/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.039 | 10/47 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.11× | +3.0 | 0.052 | 7/48 (SW480, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +2.9 | 0.064 | 6/48 (A549, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.15× | +2.7 | 0.094 | 8/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10492.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.368×, A-427 0.404×; ⚠ cell-cycle shift, explains ~25% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (A498 0.395×, A-172 0.433×; ⚠ cell-cycle shift, explains ~74% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (H4 0.0413×; ⚠ cell-cycle shift, would explain all of this change); [[Capivasertib (drug)]] 5 µM in 1 line (RPMI-7951 0.0651×); [[Amsacrine (drug)]] 5 µM in 1 line (A498 0.507×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.765×** | -5.5 | 2e-05 | 22/47 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.639×** | -4.9 | 3e-04 | 16/48 (SW480, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.773×** | -4.8 | 3e-04 | 21/48 (A498, A-172, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -4.8 | 3e-04 | 2/48 (CHP-212, SW 1088) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.783×** | -4.7 | 3e-04 | 20/48 (SNU-1, KATO III, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.800×** | -4.6 | 4e-04 | 18/48 (A498, LoVo, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.675×** | -4.3 | 0.002 | 14/47 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.869× | -4.1 | 0.003 | 17/48 (A498, A-172, …) | all doses, flat | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.873× | -4.0 | 0.005 | 13/48 (HepG2/C3A, LOX-IMVI, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.818×** | -3.9 | 0.006 | 11/48 (HCT15, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.7 | 0.009 | 14/48 (SHP-77, SNU-1, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.803×** | -3.2 | 0.056 | 8/48 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.843× | -3.2 | 0.062 | 9/46 (Hs 766T, COLO 205, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 33.3 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.97× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.507× (z -8.8) |
| [[A549 (line)]] | wt | 31.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 17.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.32× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 39.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 28.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HS-578T (line)]] | alt | 19.6 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[LoVo (line)]] | wt | 41.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 25.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2347 (line)]] | alt | 24.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 30.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.22× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.433× (z -9.0) ⚠ cell-cycle shift, explains ~74% of this change |
| [[HOP62 (line)]] | alt | 22.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.90× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[Panc 03.27 (line)]] | alt | 23.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[RPMI-7951 (line)]] | alt | 27.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Capivasertib (drug)]] 5 µM 0.0651× (z -8.9) |
| [[SHP-77 (line)]] | alt | 38.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.290× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 14.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW1417 (line)]] | alt | 25.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[H4 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0413× (z -13.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HT-29 (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[J82 (line)]] | alt | 39.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1573 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.25× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 31.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[AN3 CA (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPH]] | +0.80 | +0.76 / +0.80 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 713 |
| [[CIP2A]] | +0.78 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[VRK1]] | +0.77 | +0.74 / +0.80 | both halves | 7e-06 | pathway: Mitotic Anaphase |
| [[FANCD2]] | +0.77 | +0.67 / +0.82 | both halves | 7e-06 | STRING 647 |
| [[XRCC2]] | +0.77 | +0.64 / +0.85 | both halves | 7e-06 |  |
| [[TRIP13]] | +0.76 | +0.67 / +0.76 | both halves | 7e-06 | STRING 625 |
| [[MYBL2]] | +0.76 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 | same gene group; pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 999 |
| [[C18orf54]] | +0.75 | +0.73 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CENPK]] | +0.75 | +0.61 / +0.84 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 791 |
| [[MCM8]] | +0.73 | +0.60 / +0.81 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 574 |
| [[RAD51AP1]] | +0.73 | +0.64 / +0.79 | both halves | 7e-06 | STRING 644 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZWILCH's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises ZWILCH's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without E2F8 | 0.030 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises ZWILCH's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without DSCC1 | 0.030 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-39.6, -45.6); signed map (-40.2, -48.8). **Vector** length 97.7, 24.1% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.55 to 65); *DNA strand elongation* (reactome, mean cos +0.56 to 28); *DNA Replication* (reactome, mean cos +0.55 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +6.7 | +25.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +6.4 | +22.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +5.0 | +17.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.6 | +9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.4 | +8.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.9 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -4.4 | -4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.9 | -4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.9 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.9 | -1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | zwilch kinetochore protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:66,504,959-66,550,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10036, KNTC1AP |
| Gene groups (HGNC) | RZZ complex |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H900](https://www.uniprot.org/uniprotkb/Q9H900) (Protein zwilch homolog):

> Essential component of the mitotic checkpoint, which prevents cells from prematurely exiting mitosis. Required for the assembly of the dynein-dynactin and MAD1-MAD2 complexes onto kinetochores. Its function related to the spindle assembly machinery is proposed to depend on its association in the mitotic RZZ complex.

**Summary**, from NCBI Gene [55055](https://www.ncbi.nlm.nih.gov/gene/55055):

> Involved in mitotic spindle assembly checkpoint signaling and protein localization to kinetochore. Located in kinetochore. Part of RZZ complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25468) · Entrez [55055](https://www.ncbi.nlm.nih.gov/gene/55055) · UniProt [Q9H900](https://www.uniprot.org/uniprotkb/Q9H900) · Ensembl [ENSG00000174442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174442)

## Data

Gene col 10492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10492); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10492]; `tensor/DDL_lfc|DDL_z.npy` [10492]; `embed/gene_vectors.npy` [10492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10492 or target_col == 10492). Every well: [[ZWILCH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZWILCH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
