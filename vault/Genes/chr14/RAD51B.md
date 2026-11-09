---
symbol: "RAD51B"
type: "gene"
col: 11255
ensembl_id: "ENSG00000182185"
name: "RAD51 paralog B"
location: "14q24.1"
module: 200
arm: "+"
pooled_cpm: 519.56
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 49
n_dd_up_clean: 0
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# RAD51B

*RAD51 paralog B* — 14q24.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.46×; ⚠ cell-cycle shift, explains ~47% of this change).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (19 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.170× (z -22.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01473]] (+0.66, fdr 1e-05), [[FHIT]] (+0.62, fdr 1e-05), [[WWOX]] (+0.61, fdr 1e-05); moves opposite to [[TERB1]] (-0.53, fdr 5e-05), [[CDC20-DT]] (-0.52, fdr 1e-04), [[LGI4]] (-0.50, fdr 1e-04).
> It is in [[Module 200]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11255.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.46×; ⚠ cell-cycle shift, explains ~47% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.29× | +3.2 | 0.75 | 32/47 (HepG2/C3A, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.170×** | -22.9 | 0e+00 | 48/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.183×** | -22.0 | 0e+00 | 48/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.189×** | -20.7 | 0e+00 | 47/47 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.229×** | -19.1 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.268×** | -17.0 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.479×** | -13.4 | 5e-39 | 42/48 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.372×** | -12.8 | 2e-35 | 48/48 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.359×** | -12.7 | 4e-35 | 43/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.384×** | -11.9 | 1e-30 | 42/48 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.534×** | -11.4 | 2e-28 | 45/49 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.197×** | -11.0 | 3e-26 | 48/49 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.436×** | -10.7 | 4e-25 | 42/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.425×** | -10.6 | 1e-24 | 42/44 (LoVo, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.423×** | -10.3 | 5e-23 | 43/45 (NCI-H23, C-33 A, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.459×** | -10.0 | 4e-22 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.246×** | -9.5 | 1e-19 | 45/48 (Panc 03.27, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.481×** | -9.4 | 1e-19 | 47/48 (C-33 A, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.436×** | -9.2 | 1e-18 | 48/48 (C32, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.531×** | -8.2 | 9e-15 | 45/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.512×** | -8.1 | 1e-14 | 47/48 (HCT15, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.755×** | -5.1 | 8e-06 | 37/49 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -4.6 | 8e-05 | 34/48 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 759 | 0 | 23 (12 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -13.3) |
| [[SW480 (line)]] | alt | 659 | 0 | 23 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0811× (z -33.2) |
| [[PANC-1 (line)]] | alt | 415 | 0 | 22 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0981× (z -29.3) |
| [[CFPAC-1 (line)]] | alt | 716 | 0 | 20 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.144× (z -17.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -15.8) |
| [[KATO III (line)]] | alt | 440 | 0 | 19 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.121× (z -24.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -23.8) |
| [[LoVo (line)]] | wt | 655 | 0 | 19 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0929× (z -30.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -29.8) |
| [[NCI-H23 (line)]] | alt | 1,333 | 0 | 19 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0918× (z -27.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -26.2) |
| [[C32 (line)]] | wt | 534 | 0 | 18 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0926× (z -21.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -19.2) |
| [[NCI-H1792 (line)]] | alt | 734 | 0 | 18 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -19.6) |
| [[NCI-H460 (line)]] | wt | 489 | 0 | 18 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -20.6) |
| [[HCT15 (line)]] | alt | 788 | 0 | 17 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -22.8) |
| [[SNU-1 (line)]] | wt | 306 | 0 | 17 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.156× (z -18.5) |
| [[A-427 (line)]] | wt | 424 | 0 | 16 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -18.3) |
| [[Hs 766T (line)]] | wt | 451 | 0 | 16 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -19.5) |
| [[A549 (line)]] | wt | 489 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -14.4) |
| [[C-33 A (line)]] | alt | 2,166 | 0 | 15 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -21.6) |
| [[NCI-H1573 (line)]] | alt | 514 | 0 | 15 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.144× (z -22.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -22.4) |
| [[BT-474 (line)]] | alt | 349 | 0 | 14 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -20.5) |
| [[HEC-1-A (line)]] | alt | 797 | 0 | 14 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.148× (z -21.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 400 | 0 | 14 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -17.4) |
| [[LS 180 (line)]] | wt | 427 | 0 | 14 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -22.8) |
| [[Panc 03.27 (line)]] | alt | 592 | 0 | 14 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -17.8) |
| [[COLO 205 (line)]] | alt | 904 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -36.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0829× (z -31.5) |
| [[HT-29 (line)]] | alt | 326 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -22.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -21.2) |
| [[SNU-423 (line)]] | alt | 439 | 0 | 13 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -16.2) |
| [[SW 900 (line)]] | alt | 343 | 0 | 13 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -17.0) |
| [[AN3 CA (line)]] | alt | 593 | 0 | 12 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.157× (z -15.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -11.7) |
| [[J82 (line)]] | alt | 376 | 0 | 12 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -18.7) |
| [[SW48 (line)]] | wt | 1,107 | 0 | 12 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 376 | 0 | 11 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -16.5) |
| [[RKO (line)]] | wt | 591 | 0 | 11 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -18.5) |
| [[RPMI-7951 (line)]] | alt | 443 | 0 | 11 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -18.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -14.9) |
| [[SHP-77 (line)]] | alt | 469 | 0 | 11 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.131× (z -24.6) |
| [[SW1417 (line)]] | alt | 308 | 0 | 11 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -19.1) |
| [[HepG2_C3A (line)]] | wt | 363 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -19.3) |
| [[HOP62 (line)]] | alt | 385 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -18.4) |
| [[MIA PaCa-2 (line)]] | alt | 574 | 0 | 10 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.119× (z -18.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -17.9) |
| [[A-172 (line)]] | wt | 285 | 1 (1 ⚠) | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +14.1) ⚠ cell-cycle shift, explains ~47% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 594 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -14.7) |
| [[CHP-212 (line)]] | wt | 448 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0914× (z -18.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 190 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -12.7) |
| [[HS-578T (line)]] | alt | 258 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -15.7) |
| [[A498 (line)]] | wt | 362 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.235× (z -13.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -11.6) |
| [[H4 (line)]] | wt | 215 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -12.2) |
| [[SW 1271 (line)]] | alt | 585 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 260 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.327× (z -10.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -9.9) |
| [[SW 1088 (line)]] | alt | 410 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0407× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -10.5) |
| [[NCI-H2122 (line)]] | alt | 448 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 479 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 549 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01473]] | +0.66 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[FHIT]] | +0.62 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[WWOX]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[LINC01572]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SCAPER]] | +0.60 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[IMMP2L]] | +0.60 | +0.58 / +0.70 | both halves | 8e-06 |  |
| [[BABAM2]] | +0.60 | +0.64 / +0.56 | both halves | 1e-05 | pathway: DNA Double-Strand Break Repair |
| [[FGGY]] | +0.57 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[EXOC4]] | +0.55 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[HSD17B10]] ⚠ | +0.54 | +0.29 / +0.52 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[FAF1]] | +0.53 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[ZFHX3-AS1]] | +0.53 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[SLX4IP]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERB1]] | -0.53 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[CDC20-DT]] | -0.52 | -0.54 / -0.32 | both halves | 1e-04 |  |
| [[LGI4]] | -0.50 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[LSP1P5-1]] | -0.48 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[BORCS7-ASMT]] | -0.47 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[RETSAT]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[LYG1]] | -0.46 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[DGKA]] | -0.45 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[FAM229A]] | -0.45 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[BVES]] | -0.45 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[AGAP5]] | -0.44 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[BNIPL]] | -0.44 | -0.45 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-25.7, 31.0); signed map (9.8, -12.1). **Vector** length 86.1, 44.2% of its response variance represented; |z| ≥ 3 in 2,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.5 | -11.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.3 | -22.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.7 | -13.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.3 | -4.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.0 | +1.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -12.4 | -20.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -10.4 | -10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.8 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -8.5 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -7.1 | -9.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.8 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.5 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RAD51 paralog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:67,819,779-68,730,218 (+) |
| Ensembl biotype | protein_coding |
| Also known as | REC2, hREC2, R51H2; previously RAD51L1 |
| Gene groups (HGNC) | RAD51 paralogs |
| Reactome | 20 pathways, smallest: Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA2/RAD51/RAD51C binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [O15315](https://www.uniprot.org/uniprotkb/O15315) (DNA repair protein RAD51 homolog 2):

> Involved in the homologous recombination repair (HRR) pathway of double-stranded DNA breaks arising during DNA replication or induced by DNA-damaging agents. May promote the assembly of presynaptic RAD51 nucleoprotein filaments. Binds single-stranded DNA and double-stranded DNA and has DNA-dependent ATPase activity. Part of the RAD51 paralog protein complex BCDX2 which acts in the BRCA1-BRCA2-dependent HR pathway. Upon DNA damage, BCDX2 acts downstream of BRCA2 recruitment and upstream of RAD51 …

**Summary**, from NCBI Gene [5890](https://www.ncbi.nlm.nih.gov/gene/5890):

> The protein encoded by this gene is a member of the RAD51 protein family. RAD51 family members are evolutionarily conserved proteins essential for DNA repair by homologous recombination. This protein has been shown to form a stable heterodimer with the family member RAD51C, which further interacts with the other family members, such as RAD51, XRCC2, and XRCC3. Overexpression of this gene was found to cause cell cycle G1 delay and cell apoptosis, which suggested a role of this protein in sensing …

**Accessions** — [HGNC:9822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9822) · Entrez [5890](https://www.ncbi.nlm.nih.gov/gene/5890) · UniProt [O15315](https://www.uniprot.org/uniprotkb/O15315) · Ensembl [ENSG00000182185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182185)

## Data

Gene col 11255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11255); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11255]; `tensor/DDL_lfc|DDL_z.npy` [11255]; `embed/gene_vectors.npy` [11255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11255 or target_col == 11255). Every well: [[RAD51B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD51B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
