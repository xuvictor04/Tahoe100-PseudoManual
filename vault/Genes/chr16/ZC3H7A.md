---
symbol: "ZC3H7A"
type: "gene"
col: 4327
ensembl_id: "ENSG00000122299"
name: "zinc finger CCCH-type containing 7A"
location: "16p13.13"
module: 28
arm: "+"
pooled_cpm: 79.27
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ZC3H7A

*zinc finger CCCH-type containing 7A* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +25.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.467× (z -19.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OCIAD1]] (+0.64, fdr 1e-05), [[NDUFA5]] (+0.62, fdr 1e-05), [[EXOSC8]] (+0.61, fdr 1e-05); moves opposite to [[PRDX1]] (-0.61, fdr 1e-05), [[TSPAN17]] (-0.58, fdr 3e-05), [[ANKS1A]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4327.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +25.2 | 0e+00 | 47/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +14.8 | 0e+00 | 43/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +11.3 | 3e-27 | 36/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +8.4 | 6e-15 | 36/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +7.8 | 8e-13 | 34/48 (PANC-1, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +7.4 | 1e-11 | 35/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +6.1 | 8e-08 | 20/37 (NCI-H1792, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +5.7 | 6e-07 | 29/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +5.7 | 6e-07 | 32/49 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.003 | 19/45 (MIA PaCa-2, RKO, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.7 | 0.013 | 20/48 (KATO III, LoVo, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.31×** | +3.6 | 0.014 | 16/47 (PANC-1, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.014 | 18/48 (LoVo, PANC-1, …) | all doses, flat |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.047 | 7/48 (HOP62, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.050 | 17/43 (C-33 A, NCI-H460, …) | all doses, flat | composition shift |
| [[Tomivosertib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.050 | 8/48 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4327.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.467×** | -19.5 | 0e+00 | 48/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -16.5 | 0e+00 | 43/49 (AsPC-1, SHP-77, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.534×** | -16.1 | 0e+00 | 48/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.535×** | -16.0 | 0e+00 | 47/48 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.659×** | -10.7 | 1e-24 | 40/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.659×** | -10.3 | 6e-23 | 39/48 (SW480, H4, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -10.0 | 9e-22 | 36/50 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -7.8 | 5e-13 | 38/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -6.5 | 4e-09 | 24/48 (PANC-1, BT-474, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.847× | -6.1 | 8e-08 | 21/48 (HOP62, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.874× | -4.9 | 4e-05 | 18/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.722×** | -4.4 | 6e-04 | 20/49 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 0.885× | -3.2 | 0.068 | 10/48 (SW 1088, SW480, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.846× | -3.1 | 0.087 | 18/48 (C32, NCI-H661, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 253 | 1 | 16 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.145× (z -21.8) |
| [[PANC-1 (line)]] | alt | 91.4 | 5 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +21.5) | [[Panobinostat (drug)]] 5 µM 0.380× (z -16.3) |
| [[SW480 (line)]] | alt | 72.7 | 3 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +17.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -12.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -11.9) |
| [[A-172 (line)]] | wt | 110 | 1 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.283× (z -17.8) |
| [[H4 (line)]] | wt | 90.7 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +9.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.311× (z -11.2) |
| [[HOP62 (line)]] | alt | 69.7 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.440× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 69.9 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +17.4) | [[Panobinostat (drug)]] 5 µM 0.463× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 61.6 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.427× (z -12.4) |
| [[A498 (line)]] | wt | 108 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.391× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 132 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -13.7) |
| [[LoVo (line)]] | wt | 56.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 130 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -13.4) |
| [[A549 (line)]] | wt | 77.4 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +16.3) | [[Panobinostat (drug)]] 5 µM 0.385× (z -11.0) |
| [[Hs 766T (line)]] | wt | 88.1 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.7) | [[Selinexor (drug)]] 5 µM 0.549× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -9.7) |
| [[C-33 A (line)]] | alt | 53.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.5) | — |
| [[J82 (line)]] | alt | 75.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.2) | [[Selinexor (drug)]] 5 µM 0.619× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.526× (z -8.8) |
| [[A-427 (line)]] | wt | 45.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +13.3) | — |
| [[CFPAC-1 (line)]] | alt | 62.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -10.3) |
| [[CHP-212 (line)]] | wt | 132 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -8.8) |
| [[HCT15 (line)]] | alt | 105 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 75.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.406× (z -8.9) |
| [[KATO III (line)]] | alt | 82.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 61.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.6) | — |
| [[LS 180 (line)]] | wt | 73.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 57.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.479× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 51.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -8.7) |
| [[RKO (line)]] | wt | 75.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.7) | — |
| [[RPMI-7951 (line)]] | alt | 90.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.0) | [[Belinostat (drug)]] 5 µM 0.465× (z -8.8) |
| [[SNU-1 (line)]] | wt | 78.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -8.9) |
| [[SW 900 (line)]] | alt | 72.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.377× (z -10.2) |
| [[SW1417 (line)]] | alt | 72.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.464× (z -9.0) |
| [[BT-474 (line)]] | alt | 66.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.443× (z -8.5) |
| [[COLO 205 (line)]] | alt | 69.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 80.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 74.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 74.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.9) | — |
| [[NCI-H23 (line)]] | alt | 46.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 67.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.6) | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 1 | — | [[Finasteride (drug)]] 5 µM 0.0662× (z -11.4) |
| [[SW 1271 (line)]] | alt | 74.9 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0892× (z -8.9) |
| [[AN3 CA (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCIAD1]] | +0.64 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[NDUFA5]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[EXOSC8]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LSM14A]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SMARCE1]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SREK1]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ZNF280D]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[CLK4]] | +0.59 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[TYW5]] | +0.58 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[NDUFS1]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CCDC25]] | +0.58 | +0.61 / +0.33 | both halves | 1e-04 |  |
| [[SLC25A46]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX1]] | -0.61 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[TSPAN17]] | -0.58 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ANKS1A]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[DOCK9]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[TMEM41A]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TPST2]] | -0.54 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[PAQR4]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[CBL]] | -0.52 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[TUSC2]] | -0.52 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[CYTH1]] | -0.51 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SPSB1]] | -0.50 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[KATNB1]] | -0.50 | -0.45 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZC3H7A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises ZC3H7A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GFOD1]] | B | GFOD1 activity raises ZC3H7A's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.29× lower at baseline in the lines without GFOD1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.9, 4.5); signed map (7.8, -25.7). **Vector** length 104, 29.0% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +14.8 | +25.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.1 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.9 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.6 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.4 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | -0.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.5 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +5.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.7 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -7.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.5 | -16.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing 7A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:11,750,586-11,797,258 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC055, FLJ20318; previously ZC3HDC7, ZC3H7 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWR0](https://www.uniprot.org/uniprotkb/Q8IWR0) (Zinc finger CCCH domain-containing protein 7A):

> May be a specific regulator of miRNA biogenesis. Binds to microRNAs MIR7-1, MIR16-2 and MIR29A hairpins recognizing the 3'-ATA(A/T)-5' motif in the apical loop.

**Summary**, from NCBI Gene [29066](https://www.ncbi.nlm.nih.gov/gene/29066):

> Enables miRNA binding activity. Involved in miRNA processing. Acts upstream of with a positive effect on post-transcriptional regulation of gene expression. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30959) · Entrez [29066](https://www.ncbi.nlm.nih.gov/gene/29066) · UniProt [Q8IWR0](https://www.uniprot.org/uniprotkb/Q8IWR0) · Ensembl [ENSG00000122299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122299)

## Data

Gene col 4327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4327); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4327]; `tensor/DDL_lfc|DDL_z.npy` [4327]; `embed/gene_vectors.npy` [4327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4327 or target_col == 4327). Every well: [[ZC3H7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
