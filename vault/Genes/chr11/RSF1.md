---
symbol: "RSF1"
type: "gene"
col: 538
ensembl_id: "ENSG00000048649"
name: "remodeling and spacing factor 1"
location: "11q14.1"
module: 74
arm: "+"
pooled_cpm: 335.15
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# RSF1

*remodeling and spacing factor 1* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.43× (z +18.7, q 0e+00, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.66× (z +18.6, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.404× (z -33.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAF11]] (+0.78, fdr 7e-06), [[REST]] (+0.76, fdr 7e-06), [[KMT2A]] (+0.76, fdr 7e-06); moves opposite to [[COLGALT1]] (-0.66, fdr 1e-05), [[TXNDC5]] (-0.65, fdr 7e-06), [[NUTF2]] (-0.65, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.43×** | +18.7 | 0e+00 | 37/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +18.6 | 0e+00 | 45/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +14.8 | 0e+00 | 39/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +13.8 | 2e-41 | 41/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +13.4 | 6e-39 | 42/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +11.2 | 6e-27 | 39/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +7.6 | 2e-12 | 29/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +6.2 | 5e-08 | 20/48 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.5 | 3e-06 | 20/48 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.08× | +4.2 | 0.001 | 1/48 (KATO III) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.18× | +3.2 | 0.081 | 15/49 (AsPC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.1 | 0.092 | 4/48 (HCT15, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.404×** | -33.1 | 0e+00 | 48/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.442×** | -29.8 | 0e+00 | 48/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.448×** | -29.3 | 0e+00 | 48/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.531×** | -22.3 | 0e+00 | 41/44 (KATO III, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.559×** | -20.4 | 0e+00 | 44/47 (CFPAC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.577×** | -20.1 | 0e+00 | 47/49 (PANC-1, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.574×** | -18.8 | 0e+00 | 43/45 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.659×** | -15.2 | 0e+00 | 47/48 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.688×** | -13.7 | 1e-40 | 44/48 (HT-29, AsPC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.730×** | -11.5 | 1e-28 | 45/48 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.763×** | -9.9 | 3e-21 | 42/48 (C32, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.598×** | -9.8 | 4e-21 | 45/49 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.633×** | -8.7 | 1e-16 | 30/38 (Panc 03.27, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.853× | -8.2 | 1e-14 | 19/48 (SW 900, SNU-423, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.702×** | -6.7 | 6e-10 | 39/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.833×** | -6.7 | 9e-10 | 24/48 (AsPC-1, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.706×** | -6.6 | 1e-09 | 40/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.729×** | -6.0 | 5e-08 | 39/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.804×** | -5.7 | 4e-07 | 32/48 (AsPC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.760×** | -5.2 | 5e-06 | 29/48 (HT-29, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.864× | -5.0 | 1e-05 | 14/48 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.776×** | -4.8 | 3e-05 | 33/48 (MIA PaCa-2, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.796×** | -4.3 | 3e-04 | 25/47 (A549, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.897× | -3.9 | 0.002 | 15/48 (AsPC-1, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 673 | 6 (2 ⚠) | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +18.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -26.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.374× (z -20.8) |
| [[HT-29 (line)]] | alt | 436 | 3 (1 ⚠) | 11 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +17.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.86× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -22.0) |
| [[LOX-IMVI (line)]] | wt | 362 | 5 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.71× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.379× (z -22.5) |
| [[A549 (line)]] | wt | 324 | 5 (1 ⚠) | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +19.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.10× (z +16.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -22.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.390× (z -20.7) |
| [[MIA PaCa-2 (line)]] | alt | 379 | 4 | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.02× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -20.6) |
| [[SW 900 (line)]] | alt | 415 | 4 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.64× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -19.7) |
| [[HEC-1-A (line)]] | alt | 331 | 3 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.68× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.390× (z -22.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.390× (z -22.8) |
| [[KATO III (line)]] | alt | 439 | 3 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.75× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -29.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.374× (z -19.1) |
| [[PANC-1 (line)]] | alt | 464 | 5 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +38.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +28.5) | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -31.6) |
| [[A-172 (line)]] | wt | 409 | 2 | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 1.71× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.398× (z -19.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.411× (z -18.3) |
| [[BT-474 (line)]] | alt | 213 | 7 (4 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -15.4) |
| [[HOP62 (line)]] | alt | 226 | 4 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -17.1) |
| [[NCI-H2030 (line)]] | alt | 304 | 3 (1 ⚠) | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +16.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.85× (z +11.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.439× (z -14.5) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.524× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 218 | 4 | 7 (5 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.58× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.454× (z -16.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.463× (z -16.4) |
| [[SNU-423 (line)]] | alt | 341 | 2 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.85× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.350× (z -23.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.365× (z -22.1) |
| [[A498 (line)]] | wt | 242 | 3 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 1.86× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -19.1) |
| [[AsPC-1 (line)]] | alt | 349 | 2 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.454× (z -17.3) |
| [[C32 (line)]] | wt | 307 | 2 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 1.83× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -21.2) |
| [[J82 (line)]] | alt | 382 | 2 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.66× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.473× (z -16.3) |
| [[LoVo (line)]] | wt | 235 | 4 (2 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.434× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 274 | 4 | 6 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.13× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.521× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 283 | 5 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +15.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.495× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.501× (z -12.3) |
| [[RKO (line)]] | wt | 304 | 5 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.369× (z -15.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.445× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 356 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -20.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.402× (z -17.0) |
| [[H4 (line)]] | wt | 335 | 1 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.7) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -19.3) |
| [[Hs 766T (line)]] | wt | 370 | 2 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -20.1) |
| [[hTERT-HPNE (line)]] | wt | 326 | 2 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 1.88× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -17.6) |
| [[SW1417 (line)]] | alt | 401 | 1 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.53× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -16.6) |
| [[C-33 A (line)]] | alt | 353 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.96× (z +11.2) | [[Belinostat (drug)]] 5 µM 0.346× (z -17.5) |
| [[HS-578T (line)]] | alt | 268 | 4 | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.83× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -19.2) |
| [[LS 180 (line)]] | wt | 276 | 2 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +12.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.64× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.476× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 373 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 426 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.439× (z -19.0) |
| [[SW480 (line)]] | alt | 351 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -21.0) |
| [[SHP-77 (line)]] | alt | 334 | 2 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +14.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.73× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.466× (z -15.0) |
| [[A-427 (line)]] | wt | 342 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 1.76× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -27.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.452× (z -16.0) |
| [[COLO 205 (line)]] | alt | 298 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.403× (z -14.5) |
| [[HCT15 (line)]] | alt | 433 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -22.6) |
| [[RPMI-7951 (line)]] | alt | 301 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.83× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -15.5) |
| [[SK-MEL-2 (line)]] | alt | 165 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Belinostat (drug)]] 5 µM 0.402× (z -13.2) |
| [[HepG2_C3A (line)]] | wt | 239 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.268× (z -18.1) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.359× (z -14.6) |
| [[CHP-212 (line)]] | wt | 427 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.297× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.413× (z -10.5) |
| [[SNU-1 (line)]] | wt | 254 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.97× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -13.8) |
| [[SW 1271 (line)]] | alt | 588 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.404× (z -9.7) |
| [[AN3 CA (line)]] | alt | 344 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.464× (z -9.2) |
| [[SW48 (line)]] | wt | 201 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.1) ⚠ cell-cycle shift, explains ~31% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.410× (z -11.0) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.490× (z -8.8) |
| [[NCI-H2122 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 274 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAF11]] | +0.78 | +0.74 / +0.75 | both halves | 7e-06 | STRING 485 |
| [[REST]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[KMT2A]] | +0.76 | +0.68 / +0.79 | both halves | 7e-06 | same gene group |
| [[NIPBL]] | +0.75 | +0.63 / +0.73 | both halves | 7e-06 | STRING 720 |
| [[NBR1]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[ANKRD12]] | +0.74 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[CEP350]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[PPIG]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 | STRING 542 |
| [[ZC3H6]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.73 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[PPP1R12A]] | +0.73 | +0.60 / +0.72 | both halves | 7e-06 | STRING 486 |
| [[TERF2IP]] | +0.73 | +0.80 / +0.60 | both halves | 7e-06 | pathway: Chromosome Maintenance |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLGALT1]] | -0.66 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.65 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[NUTF2]] | -0.65 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[RPSA]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[NIPA2]] | -0.64 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[CS]] | -0.64 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[FAM20B]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.63 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[ATP13A2]] | -0.62 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[CHID1]] | -0.61 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | -0.61 | -0.59 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.3, -45.8); signed map (4.0, -15.2). **Vector** length 149, 56.3% of its response variance represented; |z| ≥ 3 in 1,645 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +12.1 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.4 | +18.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.1 | +13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +9.2 | +18.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.2 | +14.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.1 | +7.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +4.2 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.9 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.0 | -13.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -10.6 | -20.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.4 | -18.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -7.2 | -22.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.1 | -6.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.7 | -6.7 |
|  | [[EX229 (drug)]] 5 µM |  | -6.7 | -5.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.5 | -6.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -6.5 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | remodeling and spacing factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:77,660,009-77,820,869 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XAP8, RSF-1, p325; previously HBXAP |
| Gene groups (HGNC) | PHD finger proteins; RSF complex |
| Reactome | 4 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Chromosome Maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T23](https://www.uniprot.org/uniprotkb/Q96T23) (Remodeling and spacing factor 1):

> Regulatory subunit of the ATP-dependent RSF-1 and RSF-5 ISWI chromatin-remodeling complexes, which form ordered nucleosome arrays on chromatin and facilitate access to DNA during DNA-templated processes such as DNA replication, transcription, and repair. Binds to core histones together with SMARCA5, and is required for the assembly of regular nucleosome arrays by the RSF-5 ISWI chromatin-remodeling complex. Directly stimulates the ATPase activity of SMARCA1 and SMARCA5 in the RSF-1 and RSF-5 …

**Summary**, from NCBI Gene [51773](https://www.ncbi.nlm.nih.gov/gene/51773):

> This gene encodes a nuclear protein that interacts with hepatitis B virus X protein (HBX) and facilitates transcription of hepatitis B virus genes by the HBX transcription activator, suggesting a role for this interaction in the virus life cycle. This protein also interacts with SNF2H protein to form the RSF chromatin-remodeling complex, where the SNF2H subunit functions as the nucleosome-dependent ATPase, and this protein as the histone chaperone. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:18118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18118) · Entrez [51773](https://www.ncbi.nlm.nih.gov/gene/51773) · UniProt [Q96T23](https://www.uniprot.org/uniprotkb/Q96T23) · Ensembl [ENSG00000048649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048649)

## Data

Gene col 538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 538); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 538]; `tensor/DDL_lfc|DDL_z.npy` [538]; `embed/gene_vectors.npy` [538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 538 or target_col == 538). Every well: [[RSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
