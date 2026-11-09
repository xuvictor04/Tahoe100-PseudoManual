---
symbol: "ZNF280C"
type: "gene"
col: 635
ensembl_id: "ENSG00000056277"
name: "zinc finger protein 280C"
location: "Xq26.1"
module: 107
arm: "+"
pooled_cpm: 34.59
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 6
n_dd_up_clean: 24
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# ZNF280C

*zinc finger protein 280C* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.09× (z +25.3, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.483× (z -11.6, q 4e-28, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.377× (z -8.1, q 1e-13, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 0.0697×, NCI-H460 0.154×, SW480 0.188×, PANC-1 0.266×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.104×, PANC-1 0.241×, SNU-423 0.148×, SW480 0.317×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.144×, NCI-H2347 0.145×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.171×); [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 0.207×).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRCH3]] (+0.51, fdr 2e-04), [[DMTF1]] (+0.51, fdr 2e-04), [[THEM4]] (+0.49, fdr 2e-05); moves opposite to [[CDK11B]] (-0.48, fdr 4e-05), [[INTS3]] (-0.48, fdr 5e-05), [[FTO]] (-0.47, fdr 1e-04).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.09×** | +25.3 | 0e+00 | 44/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.79×** | +16.2 | 0e+00 | 45/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.68×** | +15.6 | 0e+00 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +14.6 | 1e-45 | 45/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.21×** | +12.5 | 5e-34 | 41/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +12.1 | 1e-31 | 40/47 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +11.6 | 5e-29 | 40/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +11.1 | 7e-27 | 40/47 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +11.1 | 7e-27 | 39/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +10.8 | 2e-25 | 35/48 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +10.3 | 3e-23 | 39/48 (AsPC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +10.0 | 5e-22 | 40/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.86×** | +9.8 | 5e-21 | 40/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +8.6 | 5e-16 | 38/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.9 | 1e-13 | 35/48 (SNU-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.7 | 3e-07 | 29/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 635.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 0.0697×, NCI-H460 0.154×, SW480 0.188×, PANC-1 0.266×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.104×, PANC-1 0.241×, SNU-423 0.148×, SW480 0.317×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.144×, NCI-H2347 0.145×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.171×); [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 0.207×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.483×** | -11.6 | 4e-28 | 35/44 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -11.3 | 2e-27 | 30/37 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -8.1 | 1e-13 | 32/48 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.658×** | -6.2 | 1e-07 | 27/42 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.626×** | -3.9 | 0.011 | 18/47 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.807×** | -3.4 | 0.058 | 19/46 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 66.3 | 13 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.95× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -18.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 54.5 | 10 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -17.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 40.3 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 28.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +17.8) | — |
| [[KATO III (line)]] | alt | 25.7 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.31× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -13.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 78.7 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.207× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 34.9 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -14.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 25.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +16.4) | — |
| [[LOX-IMVI (line)]] | wt | 49.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 30.4 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.02× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -13.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 40.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -16.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 27.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +11.1) | — |
| [[A549 (line)]] | wt | 45.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.0697× (z -21.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 20.8 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.50× (z +9.7) | [[Canagliflozin (drug)]] 0.05 µM 0.171× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 16.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +17.6) | — |
| [[HEC-1-A (line)]] | alt | 28.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 23.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +14.1) | — |
| [[LoVo (line)]] | wt | 14.7 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 20.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -10.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 38.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -10.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 52.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -10.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 23.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -11.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 20.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 17.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 47.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -9.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 21.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +16.6) | — |
| [[A-172 (line)]] | wt | 10.2 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +9.1) | — |
| [[C32 (line)]] | wt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +17.3) | — |
| [[NCI-H1573 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -14.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -10.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 42.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 10 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRCH3]] | +0.51 | +0.49 / +0.31 | both halves | 2e-04 |  |
| [[DMTF1]] | +0.51 | +0.58 / +0.29 | both halves | 2e-04 |  |
| [[THEM4]] | +0.49 | +0.49 / +0.59 | both halves | 2e-05 |  |
| [[SDHAF4]] | +0.48 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[FBXW4]] | +0.47 | +0.68 / -0.00 | ⚠ one half (not replicated) | 1.00 |  |
| [[TBPL1]] | +0.47 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[KATNBL1]] | +0.46 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[ENY2]] | +0.45 | +0.45 / +0.39 | both halves | 6e-05 |  |
| [[POLE4]] ⚠ | +0.45 | +0.35 / +0.47 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[KRBOX5]] | +0.45 | +0.56 / +0.28 | both halves | 3e-04 |  |
| [[WDR75]] | +0.44 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[UNK]] | +0.44 | +0.52 / +0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[HMGCL]] | +0.43 | +0.44 / +0.31 | both halves | 2e-04 |  |
| [[HNRNPLL]] | +0.43 | +0.44 / +0.33 | both halves | 1e-04 |  |
| [[ZNF330]] | +0.43 | +0.41 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK11B]] | -0.48 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[INTS3]] | -0.48 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[FTO]] | -0.47 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[SF3A2]] | -0.47 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[GAK]] | -0.47 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[ELAVL1]] | -0.46 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ERP44]] | -0.46 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[COASY]] | -0.46 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[SPON2]] | -0.46 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[DCAF12]] | -0.45 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[DDX23]] | -0.45 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[RAB5C]] | -0.45 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF280C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction -0.270). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.7, 19.8); signed map (10.1, -14.9). **Vector** length 81.7, 20.7% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | +3.7 | +5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.4 | +15.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +4.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +7.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +4.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -11.5 | -8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -8.8 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -11.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +2.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.2 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +3.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 280C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:130,202,707-130,268,899 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20095, ZNF633, ZPET; previously SUHW3 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8ND82](https://www.uniprot.org/uniprotkb/Q8ND82) (Zinc finger protein 280C):

> May function as a transcription factor.

**Summary**, from NCBI Gene [55609](https://www.ncbi.nlm.nih.gov/gene/55609):

> This gene encodes a member of the zinc finger domain-containing protein family. This family member contains multiple Cys2-His2(C2H2)-type zinc finger domains, the most common type of zinc finger domain that self-folds to form a beta-beta-alpha structure that binds a zinc ion. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:25955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25955) · Entrez [55609](https://www.ncbi.nlm.nih.gov/gene/55609) · UniProt [Q8ND82](https://www.uniprot.org/uniprotkb/Q8ND82) · Ensembl [ENSG00000056277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000056277)

## Data

Gene col 635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 635); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 635]; `tensor/DDL_lfc|DDL_z.npy` [635]; `embed/gene_vectors.npy` [635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 635 or target_col == 635). Every well: [[ZNF280C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF280C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
