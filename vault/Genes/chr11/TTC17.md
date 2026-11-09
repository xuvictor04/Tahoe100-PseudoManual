---
symbol: "TTC17"
type: "gene"
col: 589
ensembl_id: "ENSG00000052841"
name: "tetratricopeptide repeat domain 17"
location: "11p12-p11.2"
module: 213
arm: "+"
pooled_cpm: 299.4
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# TTC17

*tetratricopeptide repeat domain 17* — 11p12-p11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (COLO 205 2.38×, LoVo 1.60×, NCI-H1573 1.67×, NCI-H1792 1.58×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 1.55×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 1.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.465× (z -27.6, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.747× (z -14.9, q 0e+00, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP4]] (+0.67, fdr 7e-06), [[FAM120B]] (+0.61, fdr 1e-05), [[GIGYF2]] (+0.60, fdr 1e-05); moves opposite to [[MEX3B]] (-0.47, fdr 3e-05), [[UCP2]] (-0.45, fdr 2e-04), [[TSPYL4]] (-0.45, fdr 4e-05).
> It is in [[Module 213]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 589.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (COLO 205 2.38×, LoVo 1.60×, NCI-H1573 1.67×, NCI-H1792 1.58×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 1.55×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 1.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +4.3 | 0.009 | 16/48 (LoVo, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +4.0 | 0.016 | 18/48 (COLO 205, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.7 | 0.048 | 8/47 (SNU-1, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.0 | 0.35 | 13/48 (LoVo, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.465×** | -27.6 | 0e+00 | 47/49 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.449×** | -26.7 | 0e+00 | 44/45 (A549, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -23.3 | 0e+00 | 43/44 (NCI-H23, A549, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -14.9 | 0e+00 | 31/49 (A549, CHP-212, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -14.7 | 0e+00 | 36/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.755×** | -10.1 | 3e-22 | 37/48 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.757×** | -10.0 | 9e-22 | 31/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.769×** | -9.4 | 3e-19 | 32/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.792×** | -8.1 | 4e-14 | 32/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.801×** | -8.0 | 8e-14 | 31/48 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.806×** | -7.8 | 4e-13 | 28/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.811×** | -7.2 | 2e-11 | 28/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.813×** | -7.2 | 3e-11 | 25/50 (H4, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.827×** | -6.8 | 3e-10 | 26/48 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.830×** | -6.7 | 8e-10 | 25/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.815×** | -3.8 | 0.003 | 24/49 (MIA PaCa-2, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.941× | -3.1 | 0.049 | 2/48 (RKO, LOX-IMVI) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.912× | -3.1 | 0.050 | 5/47 (A-172, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.920× | -3.0 | 0.063 | 5/48 (Hs 766T, RKO, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.944× | -2.9 | 0.081 | 2/48 (NCI-H2030, CHP-212) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.920× | -2.9 | 0.081 | 1/49 (SW 900) | top dose only | plate-row cell shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.923× | -2.9 | 0.083 | 6/48 (A549, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 290 | 0 | 14 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.494× (z -13.9) |
| [[J82 (line)]] | alt | 306 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.488× (z -13.2) |
| [[A549 (line)]] | wt | 343 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -26.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -25.3) |
| [[PANC-1 (line)]] | alt | 382 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -24.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 257 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -19.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -14.5) |
| [[LoVo (line)]] | wt | 372 | 3 (3 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.60× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.608× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 265 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -24.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -13.9) |
| [[RKO (line)]] | wt | 408 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -15.6) |
| [[A-172 (line)]] | wt | 278 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.470× (z -14.0) |
| [[H4 (line)]] | wt | 437 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.577× (z -8.6) |
| [[SNU-423 (line)]] | alt | 307 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.412× (z -17.2) |
| [[SW1417 (line)]] | alt | 310 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -21.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 309 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -12.3) |
| [[SW480 (line)]] | alt | 432 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -29.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -17.6) |
| [[A-427 (line)]] | wt | 306 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -17.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 256 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -17.7) |
| [[HS-578T (line)]] | alt | 262 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -14.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 401 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.533× (z -11.2) |
| [[KATO III (line)]] | alt | 326 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -17.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 297 | 1 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.242× (z -24.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 286 | 1 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.58× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.377× (z -18.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 215 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -18.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.553× (z -9.5) |
| [[CHP-212 (line)]] | wt | 387 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -21.5) |
| [[HOP62 (line)]] | alt | 271 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.542× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 312 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -19.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 332 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -20.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 348 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.473× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 296 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -36.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.629× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 327 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -12.1) |
| [[SHP-77 (line)]] | alt | 301 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -18.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 296 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.407× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 341 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -20.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 245 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.518× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 276 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.421× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 207 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.583× (z -10.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 278 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.576× (z -9.4) |
| [[AN3 CA (line)]] | alt | 292 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 377 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -20.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 371 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -13.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 310 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -16.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 277 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -10.7) |
| [[SW 1271 (line)]] | alt | 378 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -11.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 220 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP4]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[FAM120B]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[GIGYF2]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SFSWAP]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ATR]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[LSM7]] | +0.56 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[UBE3C]] | +0.56 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[FBXO10]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[METTL2B]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[LRRC69]] | +0.53 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[VPS13B]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ACAD10]] | +0.53 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEX3B]] | -0.47 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[UCP2]] | -0.45 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[TSPYL4]] | -0.45 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[FRMPD3]] | -0.45 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[ZNF436]] | -0.45 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.44 | -0.44 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-13.8, 1.6); signed map (-19.0, -0.4). **Vector** length 112, 35.4% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.1 | +1.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +1.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.0 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -14.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -10.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.4 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | +0.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -3.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p12-p11.2 — chr11:43,358,920-43,494,933 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10890 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AE7](https://www.uniprot.org/uniprotkb/Q96AE7) (Tetratricopeptide repeat protein 17):

> Plays a role in primary ciliogenesis by modulating actin polymerization.

**Summary**, from NCBI Gene [55761](https://www.ncbi.nlm.nih.gov/gene/55761):

> Involved in actin filament polymerization and cilium organization. Located in actin cytoskeleton; cytoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25596) · Entrez [55761](https://www.ncbi.nlm.nih.gov/gene/55761) · UniProt [Q96AE7](https://www.uniprot.org/uniprotkb/Q96AE7) · Ensembl [ENSG00000052841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000052841)

## Data

Gene col 589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 589); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 589]; `tensor/DDL_lfc|DDL_z.npy` [589]; `embed/gene_vectors.npy` [589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 589 or target_col == 589). Every well: [[TTC17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
