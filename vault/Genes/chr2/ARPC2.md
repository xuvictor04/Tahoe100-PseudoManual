---
symbol: "ARPC2"
type: "gene"
col: 8694
ensembl_id: "ENSG00000163466"
name: "actin related protein 2/3 complex subunit 2"
location: "2q35"
module: 78
arm: "+"
pooled_cpm: 302.93
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ARPC2

*actin related protein 2/3 complex subunit 2* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.20× (z +15.7, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.27× (z +4.8, q 2e-04, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A498 2.70×, SNU-423 2.94×, PANC-1 3.02×, HS-578T 2.92×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 7 lines (A498 2.44×, HT-29 2.68×, MIA PaCa-2 3.07×, NCI-H1792 3.23×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (AsPC-1 2.24×; ⚠ cell-cycle shift, explains ~66% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SW480 1.79×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.740× (z -8.5, q 1e-14, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAP1]] (+0.77, fdr 7e-06), [[ACTN1]] (+0.74, fdr 7e-06), [[SEPTIN10]] (+0.72, fdr 7e-06); moves opposite to [[SETD2]] (-0.60, fdr 1e-05), [[SREK1]] (-0.56, fdr 1e-05), [[SLC3A2]] (-0.55, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[C11orf91]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8694.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A498 2.70×, SNU-423 2.94×, PANC-1 3.02×, HS-578T 2.92×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 7 lines (A498 2.44×, HT-29 2.68×, MIA PaCa-2 3.07×, NCI-H1792 3.23×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (AsPC-1 2.24×; ⚠ cell-cycle shift, explains ~66% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SW480 1.79×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.20×** | +15.7 | 0e+00 | 47/49 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +14.1 | 1e-42 | 40/44 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +9.6 | 2e-19 | 39/45 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.31×** | +5.3 | 1e-05 | 26/48 (AsPC-1, SW480, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.8 | 2e-04 | 31/48 (SW480, SNU-1, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.19× | +3.5 | 0.050 | 19/47 (HT-29, CFPAC-1, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.43× | +3.2 | 0.11 | 24/49 (RPMI-7951, A498, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.17× | +3.0 | 0.18 | 21/50 (MIA PaCa-2, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8694.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.740×** | -8.5 | 1e-14 | 35/48 (LOX-IMVI, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.659×** | -7.5 | 2e-11 | 46/50 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.743×** | -5.9 | 6e-07 | 38/48 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.736×** | -5.6 | 2e-06 | 42/48 (NCI-H23, C32, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.748×** | -5.6 | 3e-06 | 36/47 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.806×** | -5.5 | 3e-06 | 33/48 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.752×** | -5.5 | 4e-06 | 38/48 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.767×** | -5.3 | 9e-06 | 37/47 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.787×** | -5.2 | 1e-05 | 31/49 (NCI-H23, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.833×** | -5.1 | 2e-05 | 23/48 (C32, RKO, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.813×** | -4.8 | 9e-05 | 26/48 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.790×** | -4.7 | 1e-04 | 34/49 (NCI-H23, C32, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.591×** | -4.7 | 1e-04 | 44/50 (NCI-H23, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.827×** | -4.6 | 2e-04 | 22/48 (C32, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.844× | -4.4 | 4e-04 | 22/49 (C32, SW480, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **0.742×** | -4.2 | 8e-04 | 32/49 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 491 | 1 (1 ⚠) | 12 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Trametinib (drug)]] 5 µM 0.368× (z -15.8) |
| [[C32 (line)]] | wt | 504 | 1 (1 ⚠) | 11 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 667 | 1 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +13.7) ⚠ cell-cycle shift, explains ~66% of this change | [[Panobinostat (drug)]] 5 µM 0.454× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 227 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SW480 (line)]] | alt | 253 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.79× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 290 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -10.6) |
| [[HT-29 (line)]] | alt | 287 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.659× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 459 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -21.2) |
| [[NCI-H2030 (line)]] | alt | 326 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -12.0) |
| [[PANC-1 (line)]] | alt | 259 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[RPMI-7951 (line)]] | alt | 415 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.646× (z -10.0) |
| [[A498 (line)]] | wt | 371 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[C-33 A (line)]] | alt | 152 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 390 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -9.6) |
| [[J82 (line)]] | alt | 299 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -11.7) |
| [[LoVo (line)]] | wt | 198 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -13.0) |
| [[LS 180 (line)]] | wt | 239 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 245 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H1573 (line)]] | alt | 320 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 297 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.621× (z -10.0) |
| [[SNU-1 (line)]] | wt | 186 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 366 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 372 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +11.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 225 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A549 (line)]] | wt | 319 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[AN3 CA (line)]] | alt | 179 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +10.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 384 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[HCT15 (line)]] | alt | 214 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[HOP62 (line)]] | alt | 432 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -9.6) |
| [[Hs 766T (line)]] | wt | 342 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[KATO III (line)]] | alt | 196 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 194 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H2347 (line)]] | alt | 256 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -12.8) |
| [[H4 (line)]] | wt | 285 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[HEC-1-A (line)]] | alt | 291 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[HepG2_C3A (line)]] | wt | 319 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -15.4) |
| [[RKO (line)]] | wt | 313 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.632× (z -8.5) ⚠ cell-cycle shift, explains ~84% of this change |
| [[SHP-77 (line)]] | alt | 189 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SW 900 (line)]] | alt | 314 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.84× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SW1417 (line)]] | alt | 258 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.69× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[BT-474 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 240 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 333 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 233 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAP1]] | +0.77 | +0.79 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 665 |
| [[ACTN1]] | +0.74 | +0.77 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 547 |
| [[SEPTIN10]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[STK4]] | +0.69 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[BZW1]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[RECQL]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ITGA3]] | +0.66 | +0.70 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[CD59]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[COL13A1]] | +0.64 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[ITGB1]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[SPRED2]] | +0.64 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[EHBP1L1]] | +0.64 | +0.69 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD2]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[SREK1]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[SLC3A2]] | -0.55 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[WDSUB1]] | -0.54 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[KIF13A]] | -0.54 | -0.37 / -0.50 | both halves | 7e-05 |  |
| [[THAP3]] | -0.54 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[ZNF428]] | -0.53 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ZBED3]] | -0.53 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[PAIP1]] | -0.53 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[DIS3L]] | -0.53 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[JADE1]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[STAT5B]] | -0.53 | -0.54 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf91]] | B | C11orf91 activity raises ARPC2's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.43× lower at baseline in the lines without C11orf91 | 0.056 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[NIBAN2]] | B | NIBAN2 activity raises ARPC2's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 1.62× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CD59]] | B | CD59 activity raises ARPC2's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.47× lower at baseline in the lines without CD59 | 0.067 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ARPC2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[IL1RAP]] | B | IL1RAP activity raises ARPC2's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without IL1RAP | 0.072 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[ZBED3]] | C | ZBED3 activity lowers ARPC2's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 1.76× higher at baseline in the lines without ZBED3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.6, 5.9); signed map (6.3, 45.3). **Vector** length 128, 50.7% of its response variance represented; |z| ≥ 3 in 1,320 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.7 | +15.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.1 | +1.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.6 | -7.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.4 | -4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.9 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.9 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.8 | -5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.7 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 2/3 complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,217,141-218,254,356 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p34-Arc, ARC34 |
| Gene groups (HGNC) | Actin related protein 2/3 complex subunits |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; EPHB-mediated forward signaling; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O15144](https://www.uniprot.org/uniprotkb/O15144) (Actin-related protein 2/3 complex subunit 2):

> Actin-binding component of the Arp2/3 complex, a multiprotein complex that mediates actin polymerization upon stimulation by nucleation-promoting factor (NPF). The Arp2/3 complex mediates the formation of branched actin networks in the cytoplasm, providing the force for cell motility. Seems to contact the mother actin filament. In addition to its role in the cytoplasmic cytoskeleton, the Arp2/3 complex also promotes actin polymerization in the nucleus, thereby regulating gene transcription and …

**Summary**, from NCBI Gene [10109](https://www.ncbi.nlm.nih.gov/gene/10109):

> This gene encodes one of seven subunits of the human Arp2/3 protein complex. The Arp2/3 protein complex has been implicated in the control of actin polymerization in cells and has been conserved through evolution. The exact role of the protein encoded by this gene, the p34 subunit, has yet to be determined. Two alternatively spliced variants have been characterized to date. Additional alternatively spliced variants have been described but their full length nature has not been determined. …

**Accessions** — [HGNC:705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:705) · Entrez [10109](https://www.ncbi.nlm.nih.gov/gene/10109) · UniProt [O15144](https://www.uniprot.org/uniprotkb/O15144) · Ensembl [ENSG00000163466](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163466)

## Data

Gene col 8694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8694); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8694]; `tensor/DDL_lfc|DDL_z.npy` [8694]; `embed/gene_vectors.npy` [8694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8694 or target_col == 8694). Every well: [[ARPC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARPC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
