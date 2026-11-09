---
symbol: "LRBA"
type: "gene"
col: 12623
ensembl_id: "ENSG00000198589"
name: "LPS responsive beige-like anchor protein"
location: "4q31.3"
module: 23
arm: "-"
pooled_cpm: 379.79
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# LRBA

*LPS responsive beige-like anchor protein* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.30× (z +5.0, q 4e-04, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.395× (z -24.5, q 0e+00, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMYD3]] (+0.63, fdr 3e-05), [[SPIDR]] (+0.61, fdr 2e-05), [[RABGAP1L]] (+0.61, fdr 2e-05); moves opposite to [[ZNF425]] (-0.60, fdr 1e-04), [[DDX59]] (-0.59, fdr 6e-05), [[SENP8]] (-0.59, fdr 2e-04).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MCTP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +5.0 | 4e-04 | 25/48 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.008 | 25/48 (AsPC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.008 | 30/48 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.0 | 0.008 | 19/48 (A-172, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.009 | 25/47 (C-33 A, Hs 766T, …) | rises with dose |  |
| [[Dapagliflozin (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.23 | 18/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12623.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.395×** | -24.5 | 0e+00 | 49/49 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.510×** | -17.7 | 0e+00 | 44/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.452×** | -14.8 | 0e+00 | 44/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.481×** | -13.1 | 4e-37 | 47/47 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.532×** | -11.3 | 1e-27 | 39/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.570×** | -10.5 | 1e-23 | 45/48 (MIA PaCa-2, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -10.3 | 4e-23 | 38/45 (CFPAC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.575×** | -10.3 | 4e-23 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.493×** | -9.6 | 4e-20 | 41/49 (COLO 205, HCT15, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -9.6 | 6e-20 | 43/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.589×** | -9.5 | 1e-19 | 36/44 (SW480, HCT15, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.613×** | -9.1 | 4e-18 | 44/48 (KATO III, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -8.5 | 7e-16 | 41/50 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.674×** | -7.4 | 7e-12 | 38/48 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **0.676×** | -7.3 | 1e-11 | 43/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.614×** | -6.6 | 1e-09 | 42/48 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.533×** | -6.1 | 3e-08 | 40/49 (HOP62, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.733×** | -5.8 | 2e-07 | 37/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.705×** | -4.8 | 5e-05 | 30/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -4.5 | 2e-04 | 22/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.717×** | -3.2 | 0.027 | 26/48 (HOP62, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.830×** | -3.2 | 0.030 | 22/47 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.891× | -3.0 | 0.050 | 5/49 (Hs 766T, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 246 | 2 (1 ⚠) | 14 (7 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.50× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -23.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -22.1) |
| [[PANC-1 (line)]] | alt | 290 | 1 (1 ⚠) | 15 (11 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.92× (z +9.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -28.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -25.2) |
| [[KATO III (line)]] | alt | 461 | 0 | 15 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -25.2) |
| [[NCI-H460 (line)]] | wt | 258 | 1 | 14 (9 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -22.6) |
| [[SW 900 (line)]] | alt | 396 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -23.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -23.7) |
| [[SW480 (line)]] | alt | 547 | 0 | 14 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -23.3) |
| [[MIA PaCa-2 (line)]] | alt | 337 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -23.4) |
| [[RKO (line)]] | wt | 438 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -19.0) |
| [[LoVo (line)]] | wt | 610 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -25.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -20.1) |
| [[LS 180 (line)]] | wt | 644 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -18.8) |
| [[NCI-H1573 (line)]] | alt | 758 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -33.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -26.0) |
| [[SNU-1 (line)]] | wt | 214 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.211× (z -15.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.245× (z -10.2) |
| [[A498 (line)]] | wt | 313 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -23.9) |
| [[A549 (line)]] | wt | 283 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -24.3) |
| [[BT-474 (line)]] | alt | 443 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -14.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.428× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 591 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -27.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -23.4) |
| [[HCT15 (line)]] | alt | 984 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -19.7) |
| [[HEC-1-A (line)]] | alt | 633 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -22.6) |
| [[NCI-H1792 (line)]] | alt | 358 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -26.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -21.3) |
| [[SNU-423 (line)]] | alt | 188 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -13.4) |
| [[C-33 A (line)]] | alt | 902 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -18.6) |
| [[A-172 (line)]] | wt | 174 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.44× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -10.2) |
| [[COLO 205 (line)]] | alt | 632 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -21.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -17.1) |
| [[HT-29 (line)]] | alt | 608 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -16.8) |
| [[NCI-H2030 (line)]] | alt | 269 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -19.5) |
| [[NCI-H2347 (line)]] | alt | 444 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -20.3) |
| [[SW48 (line)]] | wt | 567 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -20.5) |
| [[AsPC-1 (line)]] | alt | 247 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -16.3) |
| [[hTERT-HPNE (line)]] | wt | 238 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 229 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.333× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 267 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -20.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -16.7) |
| [[A-427 (line)]] | wt | 537 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.458× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.489× (z -10.6) |
| [[CHP-212 (line)]] | wt | 628 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 257 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 136 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -21.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -13.5) |
| [[SW1417 (line)]] | alt | 283 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -18.5) |
| [[C32 (line)]] | wt | 228 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -18.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -14.3) |
| [[H4 (line)]] | wt | 334 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.397× (z -10.2) |
| [[J82 (line)]] | alt | 156 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -13.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 356 | 1 (1 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 2.03× (z +9.3) ⚠ cell-cycle shift, explains ~35% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -19.1) |
| [[HepG2_C3A (line)]] | wt | 333 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -17.9) |
| [[Hs 766T (line)]] | wt | 163 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -15.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -13.8) |
| [[NCI-H661 (line)]] | alt | 228 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.2) |
| [[SHP-77 (line)]] | alt | 167 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -8.7) |
| [[SW 1088 (line)]] | alt | 226 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.165× (z -8.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[AN3 CA (line)]] | alt | 224 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 439 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 415 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 307 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD3]] | +0.63 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[SPIDR]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[RABGAP1L]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[EDA]] | +0.59 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[EXOC6B]] | +0.58 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[UBE3D]] | +0.57 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[CAMK2G]] | +0.57 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[STX8]] | +0.56 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[C20orf27]] | +0.56 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[LDHB]] | +0.55 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[TMEM241]] | +0.55 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[GMDS]] | +0.55 | +0.38 / +0.50 | both halves | 6e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF425]] | -0.60 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[DDX59]] | -0.59 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[SENP8]] | -0.59 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[NMNAT1]] | -0.57 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[TRAF3IP2-AS1]] | -0.57 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[CHTF8]] | -0.55 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[MTG2]] | -0.55 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[CSRNP2]] | -0.55 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[MFF-DT]] | -0.55 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[PBLD]] | -0.54 | -0.45 / -0.23 | both halves | 5e-04 |  |
| [[ATE1OSP]] | -0.54 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[PRANCR]] | -0.54 | -0.46 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCTP2]] | B | MCTP2 activity raises LRBA's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without MCTP2 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[HDAC6]] | B | HDAC6 activity lowers LRBA's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-4.6, 17.1); signed map (-12.9, -53.2). **Vector** length 114, 46.7% of its response variance represented; |z| ≥ 3 in 1,514 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.1 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.1 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.1 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | -0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.9 | -24.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.2 | -13.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -5.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.4 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | LPS responsive beige-like anchor protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:150,264,435-151,015,727 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BGL, LAB300, LBA, uc.147; previously CDC4L |
| Gene groups (HGNC) | WD repeat domain containing; BEACH domain containing ; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P50851](https://www.uniprot.org/uniprotkb/P50851) (Lipopolysaccharide-responsive and beige-like anchor protein):

> Involved in coupling signal transduction and vesicle trafficking to enable polarized secretion and/or membrane deposition of immune effector molecules (By similarity). Involved in phagophore growth during mitophagy by regulating ATG9A trafficking to mitochondria.

**Summary**, from NCBI Gene [987](https://www.ncbi.nlm.nih.gov/gene/987):

> The protein encoded by this gene is a member of the WDL-BEACH-WD (WBW) gene family. Its expression is induced in B cells and macrophages by bacterial lipopolysaccharides (LPS). The encoded protein associates with protein kinase A and may be involved in leading intracellular vesicles to activated receptor complexes, which aids in the secretion and/or membrane deposition of immune effector molecules. Defects in this gene are associated with the disorder common variable immunodeficiency-8 with …

**Accessions** — [HGNC:1742](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1742) · Entrez [987](https://www.ncbi.nlm.nih.gov/gene/987) · UniProt [P50851](https://www.uniprot.org/uniprotkb/P50851) · Ensembl [ENSG00000198589](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198589)

## Data

Gene col 12623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12623); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12623]; `tensor/DDL_lfc|DDL_z.npy` [12623]; `embed/gene_vectors.npy` [12623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12623 or target_col == 12623). Every well: [[LRBA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRBA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
