---
symbol: "IER2"
type: "gene"
col: 8392
ensembl_id: "ENSG00000160888"
name: "immediate early response 2"
location: "19p13.13"
module: 109
arm: "+"
pooled_cpm: 87.3
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# IER2

*immediate early response 2* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.07× (z +25.2, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 4.77× (z +13.5, q 2e-39, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.411× (z -10.0, q 9e-21, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR1]] (+0.90, fdr 7e-06), [[EGR2]] (+0.81, fdr 7e-06), [[EGR3]] (+0.79, fdr 7e-06); moves opposite to [[FHIP2A]] (-0.69, fdr 7e-06), [[CIAO2A]] (-0.66, fdr 1e-05), [[GAPVD1]] (-0.63, fdr 7e-06).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **9.07×** | +25.2 | 0e+00 | 48/48 (AsPC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **7.42×** | +16.7 | 0e+00 | 48/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.77×** | +13.5 | 2e-39 | 48/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.50×** | +13.0 | 1e-36 | 49/49 (NCI-H460, AsPC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.32×** | +11.7 | 9e-30 | 45/45 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.47×** | +10.4 | 3e-23 | 37/43 (NCI-H460, HS-578T, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.17×** | +6.7 | 1e-09 | 39/48 (NCI-H460, C32, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.95×** | +5.8 | 5e-07 | 34/48 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.005 | 34/48 (HS-578T, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.56×** | +3.9 | 0.006 | 30/48 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.006 | 29/48 (HS-578T, SW480, …) | two highest doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.049 | 31/48 (HS-578T, SW480, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.42×** | +3.1 | 0.092 | 27/48 (A-172, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.0 | 0.098 | 24/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8392.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.411×** | -10.0 | 9e-21 | 46/49 (AsPC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.347×** | -8.4 | 8e-15 | 46/48 (C32, SW480, …) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.401×** | -7.6 | 7e-12 | 45/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.431×** | -7.0 | 5e-10 | 45/50 (C32, SW48, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.567×** | -6.8 | 1e-09 | 46/48 (C32, SHP-77, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.482×** | -6.3 | 3e-08 | 42/49 (C32, SW48, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.471×** | -6.2 | 4e-08 | 36/50 (SNU-423, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.475×** | -6.2 | 5e-08 | 42/47 (C32, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.494×** | -5.8 | 3e-07 | 43/48 (C32, SW48, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.593×** | -5.2 | 1e-05 | 41/48 (SHP-77, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.552×** | -5.1 | 2e-05 | 39/48 (HT-29, SNU-423, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.603×** | -4.6 | 2e-04 | 40/49 (C32, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.599×** | -4.4 | 5e-04 | 37/47 (C32, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.614×** | -4.0 | 0.003 | 33/48 (HOP62, C32, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.631×** | -4.0 | 0.003 | 37/48 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.403×** | -3.7 | 0.007 | 37/50 (C32, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.688×** | -3.5 | 0.013 | 35/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.97 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 129 | 7 (6 ⚠) | 12 | [[Homoharringtonine (drug)]] 5 µM 43.1× (z +31.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 35.8× (z +22.5) | [[Cobimetinib (drug)]] 0.5 µM 0.135× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 74.6 | 15 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +27.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 19.4× (z +20.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 119 | 7 (6 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +19.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.75× (z +12.8) | [[Adagrasib (drug)]] 0.05 µM 0.537× (z -15.1) ⚠ position not correctable · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 124 | 10 (9 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +31.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.61× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -14.4) |
| [[SW48 (line)]] | wt | 176 | 6 (5 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +19.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.0× (z +15.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -11.7) |
| [[HS-578T (line)]] | alt | 118 | 7 (6 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +24.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.94× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -9.0) |
| [[SNU-1 (line)]] | wt | 44.8 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +18.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 19.8× (z +14.1) | — |
| [[A549 (line)]] | wt | 85.0 | 7 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.40× (z +19.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 95.9 | 7 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +23.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.81× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.2) |
| [[HOP62 (line)]] | alt | 77.8 | 6 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +20.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.37× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -8.5) |
| [[A-172 (line)]] | wt | 74.2 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +23.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 13.5× (z +16.4) | — |
| [[A-427 (line)]] | wt | 87.4 | 6 (5 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 4.95× (z +11.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.48× (z +9.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 116 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +23.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.54× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 81.6 | 6 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +24.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.82× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 72.9 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +22.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.45× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 53.1 | 5 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +13.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.42× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 98.2 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +16.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.48× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 48.0 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +18.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.38× (z +10.1) | — |
| [[A498 (line)]] | wt | 65.9 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +25.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.68× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -9.2) |
| [[AN3 CA (line)]] | alt | 59.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +15.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.4× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 57.7 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +21.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 100 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +13.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 145 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +22.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 136 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +23.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -11.6) |
| [[SW 900 (line)]] | alt | 65.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +21.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.14× (z +11.0) | — |
| [[SW480 (line)]] | alt | 75.0 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +15.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.50× (z +9.6) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.199× (z -9.5) |
| [[H4 (line)]] | wt | 75.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HCT15 (line)]] | alt | 110 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.252× (z -8.5) |
| [[J82 (line)]] | alt | 56.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +17.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 85.7 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +17.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.00× (z +11.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 71.5 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +17.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 133 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +18.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -12.0) |
| [[BT-474 (line)]] | alt | 87.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +19.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 112 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -11.7) |
| [[KATO III (line)]] | alt | 50.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +15.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 72.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +22.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.45× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 60.2 | 0 | 3 | — | [[Trametinib (drug)]] 0.05 µM 0.295× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 67.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +15.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 68.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +19.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 95.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +12.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 108 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -10.5) |
| [[CHP-212 (line)]] | wt | 66.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -10.6) |
| [[COLO 205 (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +14.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 95.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.85× (z +19.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW 1088 (line)]] | alt | 68.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW 1271 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +11.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[C-33 A (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR1]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 908 |
| [[EGR2]] | +0.81 | +0.85 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 582 |
| [[EGR3]] | +0.79 | +0.82 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 560 |
| [[JUNB]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 750 |
| [[CSRNP1]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 | STRING 567 |
| [[IER3]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 579 |
| [[ERCC1]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 503 |
| [[FOS]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 796 |
| [[MCL1]] | +0.70 | +0.73 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[HES1]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NR4A1]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 669 |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP2A]] | -0.69 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[CIAO2A]] | -0.66 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[GAPVD1]] | -0.63 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[MRPS15]] | -0.61 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SOS1]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[BMPR1A]] | -0.61 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[C8orf76]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[HINT1]] | -0.60 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[TIAL1]] | -0.60 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[SUPV3L1]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[NAPB]] | -0.59 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[DRAM2]] | -0.59 | -0.65 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises IER2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FOSL1]] | B | FOSL1 activity raises IER2's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[MAP2K1]] | B | MAP2K1 activity raises IER2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.886). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.8, -0.2); signed map (6.4, 29.0). **Vector** length 153, 63.2% of its response variance represented; |z| ≥ 3 in 1,512 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NGF-stimulated transcription* (reactome, mean cos +0.72 to 9); *Nuclear Events (kinase and transcription factor activation)* (reactome, mean cos +0.72 to 9); *Signaling by NTRK1 (TRKA)* (reactome, mean cos +0.72 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +9.2 | +25.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +8.4 | +16.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.6 | +0.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -13.7 | -7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.7 | -10.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -12.1 | -6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | -8.0 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -7.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.5 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.4 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.9 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.8 | -8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | immediate early response 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:13,150,411-13,154,911 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ETR101 |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTL4](https://www.uniprot.org/uniprotkb/Q9BTL4) (Immediate early response gene 2 protein):

> DNA-binding protein that seems to act as a transcription factor. Involved in the regulation of neuronal differentiation, acts upon JNK-signaling pathway activation and plays a role in neurite outgrowth in hippocampal cells (By similarity). May mediate with FIBP FGF-signaling in the establishment of laterality in the embryo (By similarity). Promotes cell motility, seems to stimulate tumor metastasis.

**Summary**, from NCBI Gene [9592](https://www.ncbi.nlm.nih.gov/gene/9592):

> Predicted to enable DNA binding activity. Involved in cell motility and positive regulation of transcription by RNA polymerase II. Located in cytoplasm and nucleoplasm. Implicated in colorectal cancer and hepatocellular carcinoma. Biomarker of childhood acute myeloid leukemia; colorectal adenocarcinoma; hepatocellular carcinoma; and melanoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28871) · Entrez [9592](https://www.ncbi.nlm.nih.gov/gene/9592) · UniProt [Q9BTL4](https://www.uniprot.org/uniprotkb/Q9BTL4) · Ensembl [ENSG00000160888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160888)

## Data

Gene col 8392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8392); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8392]; `tensor/DDL_lfc|DDL_z.npy` [8392]; `embed/gene_vectors.npy` [8392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8392 or target_col == 8392). Every well: [[IER2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IER2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
