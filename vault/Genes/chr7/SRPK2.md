---
symbol: "SRPK2"
type: "gene"
col: 5671
ensembl_id: "ENSG00000135250"
name: "SRSF protein kinase 2"
location: "7q22.3"
module: 186
arm: "+"
pooled_cpm: 330.23
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# SRPK2

*SRSF protein kinase 2* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.59× (z +14.1, q 3e-42, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.491× (z -20.8, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H23 0.113×, SK-MEL-2 0.180×, NCI-H460 0.298×, C32 0.261×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 0.447×, LoVo 0.417×, SK-MEL-2 0.395×, C32 0.422×; ⚠ cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C32 0.328×, NCI-H2347 0.342×, NCI-H23 0.309×, SW1417 0.355×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2G1]] (+0.77, fdr 7e-06), [[PPP2R5E]] (+0.73, fdr 8e-06), [[STIM1]] (+0.71, fdr 7e-06); moves opposite to [[TRMT13]] (-0.64, fdr 2e-05), [[AIMP1]] (-0.63, fdr 3e-05), [[ARCN1]] (-0.63, fdr 1e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PARD6G]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +14.1 | 3e-42 | 46/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +11.9 | 4e-30 | 45/48 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +10.0 | 2e-21 | 37/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +9.4 | 6e-19 | 38/49 (NCI-H460, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +9.4 | 6e-19 | 37/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +8.9 | 6e-17 | 33/48 (A549, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +7.9 | 2e-13 | 37/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.20× | +7.8 | 3e-13 | 25/49 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +7.8 | 3e-13 | 48/49 (CFPAC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.30×** | +7.5 | 5e-12 | 32/48 (PANC-1, LS 180, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +7.4 | 6e-12 | 27/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +6.6 | 1e-09 | 19/48 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +6.6 | 2e-09 | 30/48 (A-172, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +6.3 | 1e-08 | 28/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +6.2 | 2e-08 | 27/48 (H4, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +5.8 | 2e-07 | 24/48 (H4, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +5.4 | 2e-06 | 29/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +5.0 | 1e-05 | 22/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.16× | +4.6 | 1e-04 | 13/48 (SW48, A-427, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +4.2 | 6e-04 | 13/49 (SHP-77, HepG2/C3A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.012 | 17/48 (CFPAC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.014 | 18/49 (PANC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5671.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H23 0.113×, SK-MEL-2 0.180×, NCI-H460 0.298×, C32 0.261×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 0.447×, LoVo 0.417×, SK-MEL-2 0.395×, C32 0.422×; ⚠ cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C32 0.328×, NCI-H2347 0.342×, NCI-H23 0.309×, SW1417 0.355×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.491×** | -20.8 | 0e+00 | 42/44 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.563×** | -17.5 | 0e+00 | 45/49 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.613×** | -13.7 | 1e-40 | 36/45 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.789×** | -10.2 | 4e-22 | 28/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.746×** | -8.9 | 6e-17 | 30/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.796×** | -6.9 | 5e-10 | 31/48 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.837× | -5.2 | 2e-05 | 23/47 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.869× | -4.3 | 0.001 | 20/48 (RKO, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.884× | -3.7 | 0.012 | 18/48 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.928× | -3.2 | 0.078 | 0/48 | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.084 | 17/48 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 1,051 | 4 | 6 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 7.30× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -23.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 347 | 5 (4 ⚠) | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +16.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.59× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -25.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LS 180 (line)]] | wt | 266 | 10 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +14.9) | — |
| [[A549 (line)]] | wt | 267 | 6 (3 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +14.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.74× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -16.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 239 | 8 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.41× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 253 | 3 (1 ⚠) | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -17.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[PANC-1 (line)]] | alt | 273 | 4 (3 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.57× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -25.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HS-578T (line)]] | alt | 290 | 3 (1 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -18.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H460 (line)]] | wt | 423 | 4 (3 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.77× (z +11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.76× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -23.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 598 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -19.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 247 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 2.67× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -18.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 432 | 2 (2 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.3) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -13.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 608 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -23.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 221 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -11.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[CFPAC-1 (line)]] | alt | 133 | 5 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.64× (z +14.7) | — |
| [[HT-29 (line)]] | alt | 241 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +12.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.91× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 160 | 3 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -13.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H23 (line)]] | alt | 332 | 1 (1 ⚠) | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +11.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.113× (z -35.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 367 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -20.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 432 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -31.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 444 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.65× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -18.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 353 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.60× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -16.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 334 | 1 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +13.6) ⚠ cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.476× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 316 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.55× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 265 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -14.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 456 | 1 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.4) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 5 µM 0.411× (z -12.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 212 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.08× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 302 | 2 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.88× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -15.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 365 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -16.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 110 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +11.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.46× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 284 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.69× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.539× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 239 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -16.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[Hs 766T (line)]] | wt | 339 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.19× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -18.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 233 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.458× (z -10.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 280 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -13.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 289 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.438× (z -13.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 635 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -18.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 364 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.561× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 398 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -13.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 247 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.16× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 174 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H661 (line)]] | alt | 484 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 376 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -9.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 402 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 237 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 337 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 332 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G1]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[PPP2R5E]] | +0.73 | +0.79 / +0.58 | both halves | 8e-06 |  |
| [[STIM1]] | +0.71 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[NFATC3]] | +0.69 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[EVI5]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[MAST2]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[XPR1]] | +0.68 | +0.70 / +0.57 | both halves | 8e-06 |  |
| [[SEC24B]] | +0.67 | +0.72 / +0.56 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[TSPAN17]] | +0.66 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[CYTH3]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PTK2]] | +0.65 | +0.79 / +0.44 | both halves | 3e-05 |  |
| [[TRIM33]] | +0.65 | +0.71 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT13]] | -0.64 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[AIMP1]] | -0.63 | -0.70 / -0.46 | both halves | 3e-05 |  |
| [[ARCN1]] | -0.63 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.63 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[SRRM2]] | -0.63 | -0.63 / -0.46 | both halves | 3e-05 | STRING 569 |
| [[PAN2]] | -0.62 | -0.67 / -0.46 | both halves | 2e-05 |  |
| [[CNOT3]] | -0.62 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[OCIAD1]] | -0.62 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[MYSM1]] | -0.61 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[METTL6]] | -0.61 | -0.72 / -0.47 | both halves | 2e-05 |  |
| [[THAP2]] | -0.61 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[THAP9]] | -0.61 | -0.66 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD6G]] | B | PARD6G activity raises SRPK2's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without PARD6G | 0.036 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[ARHGAP44]] | B | ARHGAP44 activity raises SRPK2's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without ARHGAP44 | 0.0996 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.3, -7.7); signed map (-44.7, -6.5). **Vector** length 127, 45.5% of its response variance represented; |z| ≥ 3 in 1,462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +6.1 | +6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +7.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.8 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.6 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.4 | +9.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.0 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -17.0 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -14.8 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.2 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -13.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | SRSF protein kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:105,110,704-105,399,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SFRSK2 |
| Gene groups (HGNC) | SRSF protein kinase family |
| Reactome | 6 pathways, smallest: Maturation of nucleoprotein_9694631; Translation of Structural Proteins_9694635; Late SARS-CoV-2 Infection Events |
| Matched by | ensembl_id |

**Function**, from UniProt [P78362](https://www.uniprot.org/uniprotkb/P78362) (SRSF protein kinase 2):

> Serine/arginine-rich protein-specific kinase which specifically phosphorylates its substrates at serine residues located in regions rich in arginine/serine dipeptides, known as RS domains and is involved in the phosphorylation of SR splicing factors and the regulation of splicing. Promotes neuronal apoptosis by up-regulating cyclin-D1 (CCND1) expression. This is done by the phosphorylation of SRSF2, leading to the suppression of p53/TP53 phosphorylation thereby relieving the repressive effect …

**Summary**, from NCBI Gene [6733](https://www.ncbi.nlm.nih.gov/gene/6733):

> Enables ATP binding activity; magnesium ion binding activity; and protein serine/threonine kinase activity. Involved in several processes, including R-loop processing; peptidyl-serine phosphorylation; and regulation of viral genome replication. Located in chromatin; cytosol; and nuclear lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11306) · Entrez [6733](https://www.ncbi.nlm.nih.gov/gene/6733) · UniProt [P78362](https://www.uniprot.org/uniprotkb/P78362) · Ensembl [ENSG00000135250](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135250)

## Data

Gene col 5671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5671); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5671]; `tensor/DDL_lfc|DDL_z.npy` [5671]; `embed/gene_vectors.npy` [5671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5671 or target_col == 5671). Every well: [[SRPK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRPK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
