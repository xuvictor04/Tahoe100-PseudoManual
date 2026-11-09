---
symbol: "PHLDA1"
type: "gene"
col: 6287
ensembl_id: "ENSG00000139289"
name: "pleckstrin homology like domain family A member 1"
location: "12q21.2"
module: 158
arm: "+"
pooled_cpm: 288.94
n_lines_expressing: 45
n_dd_up: 7
n_dd_down: 69
n_dd_up_clean: 2
n_dd_down_clean: 61
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# PHLDA1

*pleckstrin homology like domain family A member 1* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.64× (z +10.5, q 6e-23, up in 38 of 43 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.16× (z +8.7, q 7e-16, up in 36 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 0.5 µM in 11 lines (SNU-1 7.82×, C32 5.33×, A549 6.93×, NCI-H460 4.19×, …); [[Homoharringtonine (drug)]] 5 µM in 8 lines (CFPAC-1 6.48×, AsPC-1 4.71×, C32 4.79×, Panc 03.27 4.59×, …; ⚠ cell-cycle shift, explains ~57% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (AsPC-1 6.33×, CFPAC-1 6.18×, C32 5.63×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 3 lines (NCI-H460 3.16×, A549 3.62×, C32 2.96×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 3.25×).
> Pooled over the cell lines (median), lowered significantly by 69 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.260× (z -21.3, q 0e+00, down in 44 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR1]] (+0.75, fdr 7e-06), [[SPRY2]] (+0.74, fdr 7e-06), [[FOSL1]] (+0.73, fdr 7e-06); moves opposite to [[NPEPPS]] (-0.57, fdr 1e-05), [[SOS1]] (-0.56, fdr 1e-05), [[FHIP2A]] (-0.55, fdr 1e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EGR3]] → it (grade B ⚠); 3 go from it, the strongest it → [[RABL6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6287.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 0.5 µM in 11 lines (SNU-1 7.82×, C32 5.33×, A549 6.93×, NCI-H460 4.19×, …); [[Homoharringtonine (drug)]] 5 µM in 8 lines (CFPAC-1 6.48×, AsPC-1 4.71×, C32 4.79×, Panc 03.27 4.59×, …; ⚠ cell-cycle shift, explains ~57% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (AsPC-1 6.33×, CFPAC-1 6.18×, C32 5.63×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 3 lines (NCI-H460 3.16×, A549 3.62×, C32 2.96×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 3.25×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.64×** | +10.5 | 6e-23 | 38/43 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.89×** | +10.2 | 9e-22 | 32/43 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.16×** | +8.7 | 7e-16 | 36/43 (SNU-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.12×** | +8.5 | 3e-15 | 35/43 (AsPC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.009 | 30/43 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.39×** | +3.8 | 0.017 | 34/44 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.33×** | +3.3 | 0.092 | 21/43 (SNU-1, AsPC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.35× | +3.2 | 0.10 | 24/42 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 70 in all, 8 with an alert ⚠; shown: the 15 strongest. 69 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6287.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.260×** | -21.3 | 0e+00 | 44/44 (SW48, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.297×** | -13.8 | 4e-41 | 44/45 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.377×** | -13.5 | 5e-39 | 43/43 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.322×** | -12.7 | 1e-34 | 39/43 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.320×** | -12.2 | 2e-32 | 43/43 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.342×** | -12.0 | 5e-31 | 43/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.334×** | -11.8 | 5e-30 | 41/42 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.351×** | -11.2 | 2e-27 | 40/45 (SW48, C32, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.391×** | -11.1 | 7e-27 | 41/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.359×** | -11.0 | 2e-26 | 40/43 (MIA PaCa-2, SW48, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.456×** | -10.7 | 3e-25 | 40/43 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.410×** | -9.9 | 1e-21 | 39/43 (SW48, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.452×** | -8.9 | 4e-17 | 39/43 (SW48, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.562×** | -8.7 | 2e-16 | 41/43 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.439×** | -8.5 | 8e-16 | 40/43 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 283 | 7 (4 ⚠) | 22 | [[Harringtonine (drug)]] 0.5 µM 4.19× (z +13.3) | [[Cobimetinib (drug)]] 5 µM 0.0937× (z -20.9) |
| [[AsPC-1 (line)]] | alt | 303 | 5 (4 ⚠) | 22 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +21.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.96× (z +13.3) | [[Trametinib (drug)]] 5 µM 0.126× (z -20.2) |
| [[A549 (line)]] | wt | 238 | 5 (3 ⚠) | 13 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +16.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.93× (z +14.8) | [[Trametinib (drug)]] 5 µM 0.156× (z -15.1) |
| [[HOP62 (line)]] | alt | 424 | 3 (2 ⚠) | 15 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.94× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -16.6) |
| [[LoVo (line)]] | wt | 360 | 0 | 18 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.277× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 766 | 3 (2 ⚠) | 15 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.17× (z +10.9) | [[Trametinib (drug)]] 5 µM 0.0432× (z -25.4) |
| [[NCI-H2030 (line)]] | alt | 193 | 3 (2 ⚠) | 15 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.45× (z +12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.64× (z +10.2) | [[Adagrasib (drug)]] 0.05 µM 0.458× (z -21.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.204× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 394 | 0 | 18 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -18.9) |
| [[SW48 (line)]] | wt | 922 | 0 | 18 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -26.2) |
| [[CFPAC-1 (line)]] | alt | 147 | 4 (4 ⚠) | 13 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +23.6) ⚠ cell-cycle shift, explains ~57% of this change | [[Binimetinib (drug)]] 0.5 µM 0.282× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 289 | 0 | 17 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.433× (z -22.3) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.0868× (z -19.8) |
| [[C32 (line)]] | wt | 310 | 6 (4 ⚠) | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +20.0) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.33× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -19.4) |
| [[LS 180 (line)]] | wt | 452 | 2 (1 ⚠) | 13 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.25× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -20.4) |
| [[MIA PaCa-2 (line)]] | alt | 430 | 0 | 14 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -24.8) |
| [[PANC-1 (line)]] | alt | 356 | 0 | 14 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -20.8) |
| [[NCI-H2347 (line)]] | alt | 167 | 3 (3 ⚠) | 10 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.1) ⚠ cell-cycle shift, explains ~57% of this change | [[Binimetinib (drug)]] 5 µM 0.265× (z -13.4) |
| [[A-172 (line)]] | wt | 294 | 0 | 12 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -18.3) |
| [[SNU-1 (line)]] | wt | 263 | 9 (7 ⚠) | 3 | [[Harringtonine (drug)]] 0.5 µM 7.82× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.7) |
| [[SW 900 (line)]] | alt | 501 | 0 | 12 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -21.8) |
| [[HCT15 (line)]] | alt | 275 | 0 | 11 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -16.6) |
| [[KATO III (line)]] | alt | 151 | 3 (3 ⚠) | 8 | [[Harringtonine (drug)]] 5 µM 3.95× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 5 µM 0.209× (z -13.2) |
| [[HS-578T (line)]] | alt | 239 | 2 (2 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +12.8) ⚠ cell-cycle shift, explains ~57% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -15.7) |
| [[J82 (line)]] | alt | 92.7 | 2 (2 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.7) ⚠ cell-cycle shift, explains ~57% of this change | [[Trametinib (drug)]] 5 µM 0.192× (z -14.9) |
| [[A498 (line)]] | wt | 266 | 1 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +12.3) ⚠ cell-cycle shift, explains ~57% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -15.6) |
| [[COLO 205 (line)]] | alt | 217 | 3 (2 ⚠) | 6 | [[Homoharringtonine (drug)]] 0.5 µM 9.11× (z +15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.21× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -17.7) |
| [[Hs 766T (line)]] | wt | 184 | 1 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +15.7) ⚠ cell-cycle shift, explains ~57% of this change | [[Trametinib (drug)]] 0.5 µM 0.326× (z -10.9) |
| [[H4 (line)]] | wt | 365 | 0 | 8 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.123× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 474 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -18.8) |
| [[Panc 03.27 (line)]] | alt | 124 | 4 (4 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +19.0) ⚠ cell-cycle shift, explains ~57% of this change | [[Panobinostat (drug)]] 5 µM 0.327× (z -9.8) |
| [[SW480 (line)]] | alt | 427 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -22.4) |
| [[A-427 (line)]] | wt | 413 | 3 (2 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.28× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 448 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -18.4) |
| [[CHP-212 (line)]] | wt | 272 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 237 | 3 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +16.6) ⚠ cell-cycle shift, explains ~57% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 231 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.8) ⚠ cell-cycle shift, explains ~57% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.0) |
| [[RKO (line)]] | wt | 363 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -24.5) |
| [[SW1417 (line)]] | alt | 82.5 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +15.8) ⚠ cell-cycle shift, explains ~57% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 258 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -18.7) |
| [[SNU-423 (line)]] | alt | 288 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -20.0) |
| [[SHP-77 (line)]] | alt | 119 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -12.2) |
| [[SW 1271 (line)]] | alt | 154 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.132× (z -9.0) |
| [[SW 1088 (line)]] | alt | 499 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -11.6) |
| [[AN3 CA (line)]] | alt | 164 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 27.5 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 42.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 60.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR1]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SPRY2]] | +0.74 | +0.72 / +0.74 | both halves | 7e-06 | STRING 691 |
| [[FOSL1]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EGR3]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NT5E]] | +0.72 | +0.73 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[DUSP6]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 | STRING 463 |
| [[IER2]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 503 |
| [[LIF]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[DCBLD2]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.70 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 559 |
| [[B4GALT6]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[PRDM8]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPEPPS]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SOS1]] | -0.56 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[FHIP2A]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EGR3]] | B | EGR3 activity raises PHLDA1's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 2.19× lower at baseline in the lines without EGR3 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |
| [[ENC1]] | B | ENC1 activity raises PHLDA1's level | lines that do not express ENC1 (5) vs lines expressing it (45) | 2.14× lower at baseline in the lines without ENC1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000285868, NMI, NABP1 |
| [[HAS2]] | B | HAS2 activity raises PHLDA1's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without HAS2 | 0.080 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[EGR2]] | B | EGR2 activity raises PHLDA1's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without EGR2 | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BCL2A1]] | B | BCL2A1 activity raises PHLDA1's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.72× lower at baseline in the lines without BCL2A1 | 0.087 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[SPRY4-AS1]] | C | SPRY4-AS1 activity raises PHLDA1's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RABL6]] | B | PHLDA1 activity lowers RABL6's level | lines that do not express PHLDA1 (5) vs lines expressing it (45) | 1.77× higher at baseline in the lines without PHLDA1 | 0.069 | ⚠ within organs, on part of the lines; also absent: DPYSL2, PARP3, C1RL; maybe low, not absent |
| [[EPHB2]] | B | PHLDA1 activity raises EPHB2's level | lines that do not express PHLDA1 (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without PHLDA1 | 0.071 | ⚠ within organs, on part of the lines; also absent: DPYSL2, PARP3, C1RL; maybe low, not absent |
| [[FAM43A]] | B | PHLDA1 activity raises FAM43A's level | lines that do not express PHLDA1 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without PHLDA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: DPYSL2, PARP3, C1RL; maybe low, not absent |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.8, 2.5); signed map (9.1, 45.5). **Vector** length 156, 61.8% of its response variance represented; |z| ≥ 3 in 2,405 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +11.8 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +11.2 | +8.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +11.1 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.2 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.9 | +1.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +4.5 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.3 | +3.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -13.8 | -13.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -13.1 | -13.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -11.6 | -12.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -11.2 | -11.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -10.7 | -12.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -9.7 | -8.7 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology like domain family A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2 — chr12:76,025,447-76,031,776 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TDAG51, DT1P1B11, PHRIP |
| Hallmark sets | IL2_STAT5_SIGNALING, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 9 pathways, smallest: Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes; Epigenetic regulation of gene expression by MLL3 and MLL4 complexes; MLL4 and MLL3 complexes regulate expression of PPARG target genes in adipogenesis and hepatic steatosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV24](https://www.uniprot.org/uniprotkb/Q8WV24) (Pleckstrin homology-like domain family A member 1):

> Seems to be involved in regulation of apoptosis. May be involved in detachment-mediated programmed cell death. May mediate apoptosis during neuronal development. May be involved in regulation of anti-apoptotic effects of IGF1. May be involved in translational regulation.

**Summary**, from NCBI Gene [22822](https://www.ncbi.nlm.nih.gov/gene/22822):

> This gene encodes an evolutionarily conserved proline-histidine rich nuclear protein. The encoded protein may play an important role in the anti-apoptotic effects of insulin-like growth factor-1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8933) · Entrez [22822](https://www.ncbi.nlm.nih.gov/gene/22822) · UniProt [Q8WV24](https://www.uniprot.org/uniprotkb/Q8WV24) · Ensembl [ENSG00000139289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139289)

## Data

Gene col 6287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6287); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6287]; `tensor/DDL_lfc|DDL_z.npy` [6287]; `embed/gene_vectors.npy` [6287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6287 or target_col == 6287). Every well: [[PHLDA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHLDA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
