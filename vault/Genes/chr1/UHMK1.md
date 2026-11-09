---
symbol: "UHMK1"
type: "gene"
col: 7615
ensembl_id: "ENSG00000152332"
name: "U2AF homology motif kinase 1"
location: "1q23.3"
module: 25
arm: "+"
pooled_cpm: 167.6
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# UHMK1

*U2AF homology motif kinase 1* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.19× (z +18.8, q 0e+00, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.54× (z +10.8, q 7e-25, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.859× (z -5.4, q 4e-05, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.562×, LoVo 0.676×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.553×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1573 0.539×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOB1A]] (+0.70, fdr 1e-05), [[DPY19L4]] (+0.68, fdr 1e-05), [[ARPP19]] (+0.67, fdr 3e-05); moves opposite to [[PAXX]] (-0.58, fdr 2e-04, ⚠ PAXX in the vector space only through flagged drug-doses), [[ING2]] (-0.57, fdr 8e-05), [[INAFM1]] (-0.56, fdr 5e-05), [[MRPL36]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +18.8 | 0e+00 | 41/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +18.6 | 0e+00 | 45/49 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +10.8 | 7e-25 | 43/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +10.4 | 3e-23 | 37/45 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +10.4 | 4e-23 | 37/48 (SK-MEL-2, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +9.3 | 1e-18 | 35/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +6.3 | 3e-08 | 31/48 (C32, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.27×** | +6.0 | 2e-07 | 28/48 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +5.8 | 6e-07 | 31/48 (H4, BT-474, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +5.0 | 3e-05 | 24/48 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.21×** | +4.8 | 1e-04 | 24/48 (SK-MEL-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.7 | 1e-04 | 0/50 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.7 | 1e-04 | 14/48 (BT-474, SW1417, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +4.4 | 4e-04 | 27/49 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.3 | 8e-04 | 23/38 (HOP62, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.004 | 26/47 (SW48, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.006 | 21/48 (A-172, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.010 | 8/48 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.057 | 16/47 (C32, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.059 | 6/48 (J82, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7615.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.562×, LoVo 0.676×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.553×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1573 0.539×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -5.4 | 4e-05 | 14/48 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.841× | -4.4 | 0.004 | 19/48 (H4, HEC-1-A, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.5 µM |  | 0.857× | -3.9 | 0.020 | 21/48 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.818×** | -3.6 | 0.038 | 25/49 (PANC-1, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.6 | 0.038 | 18/48 (NCI-H1573, SW1417, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.869× | -3.5 | 0.038 | 12/48 (Hs 766T, C-33 A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.879× | -3.3 | 0.093 | 9/49 (A-172, LS 180, …) | rises with dose |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | 0.881× | -3.2 | 0.10 | 9/49 (SW 900, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -3.1 | 0.11 | 11/48 (SW480, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 112 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +11.1) | — |
| [[A-427 (line)]] | wt | 272 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.53× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 1.54× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 176 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 192 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 1.81× (z +12.1) | — |
| [[SW480 (line)]] | alt | 114 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +11.8) | — |
| [[A-172 (line)]] | wt | 227 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +16.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 181 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +13.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 168 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +10.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 141 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.97× (z +9.3) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.7) | — |
| [[C32 (line)]] | wt | 415 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 1.65× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 135 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +19.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 130 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +13.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 167 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 200 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +14.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 150 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +15.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 145 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 1.53× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 122 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 100 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +14.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 150 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 162 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +9.7) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 131 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +14.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 81.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +12.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 132 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +11.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 157 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +11.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 144 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +11.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 167 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 165 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +12.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 132 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +14.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +9.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 131 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 89.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 187 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.539× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 201 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 221 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.63× (z +8.9) | — |
| [[RKO (line)]] | wt | 235 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 216 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 212 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | +0.70 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[DPY19L4]] | +0.68 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[ARPP19]] | +0.67 | +0.44 / +0.74 | both halves | 3e-05 |  |
| [[MMGT1]] | +0.64 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.62 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[TMX1]] | +0.62 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[TWF1]] | +0.61 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[DR1]] | +0.61 | +0.37 / +0.62 | both halves | 7e-05 |  |
| [[FAM136A]] | +0.61 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[EIF2D]] | +0.60 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[ALG10B]] | +0.60 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[STRADB]] | +0.59 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAXX]] ⚠ | -0.58 | -0.29 / -0.62 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ING2]] | -0.57 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[INAFM1]] | -0.56 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[MRPL36]] | -0.55 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[PPP1R35]] ⚠ | -0.55 | -0.31 / -0.58 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LENG1]] | -0.55 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[ZBTB7A]] | -0.54 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[CLIP2]] | -0.54 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[NTHL1]] | -0.53 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[PILRB]] | -0.53 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[MED19]] | -0.53 | -0.37 / -0.56 | both halves | 7e-05 |  |
| [[CHD1]] | -0.53 | -0.24 / -0.48 | both halves | 5e-04 | pathway: ESR-mediated signaling |
| [[CAMKK1]] | -0.53 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[POLD4]] | -0.53 | -0.25 / -0.51 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.6, -20.1); signed map (-17.5, -38.1). **Vector** length 114, 33.1% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +11.9 | +10.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.5 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +18.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +18.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +3.0 | +1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.9 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.8 | +0.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.5 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.9 | -3.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.7 | -4.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | U2AF homology motif kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:162,497,251-162,529,631 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIS, Kist |
| Gene groups (HGNC) | RNA binding motif containing; U2AF homology motif kinase family |
| Reactome | 4 pathways, smallest: Estrogen-dependent nuclear events downstream of ESR-membrane signaling; Extra-nuclear estrogen signaling; ESR-mediated signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAS1](https://www.uniprot.org/uniprotkb/Q8TAS1) (Serine/threonine-protein kinase Kist):

> Upon serum stimulation, phosphorylates CDKN1B/p27Kip1, thus controlling CDKN1B subcellular location and cell cycle progression in G1 phase. May be involved in trafficking and/or processing of RNA (By similarity).

**Summary**, from NCBI Gene [127933](https://www.ncbi.nlm.nih.gov/gene/127933):

> The gene encodes a serine/threonine protein kinase that promotes cell cycle progression through G1 by phosphorylation of the cyclin-dependent kinase inhibitor 1B (p27Kip1), which causes nuclear export and degradation. The encoded protein is also thought to function in the adult nervous system and the gene has been associated with schizophrenia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:19683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19683) · Entrez [127933](https://www.ncbi.nlm.nih.gov/gene/127933) · UniProt [Q8TAS1](https://www.uniprot.org/uniprotkb/Q8TAS1) · Ensembl [ENSG00000152332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152332)

## Data

Gene col 7615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7615); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7615]; `tensor/DDL_lfc|DDL_z.npy` [7615]; `embed/gene_vectors.npy` [7615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7615 or target_col == 7615). Every well: [[UHMK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UHMK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
