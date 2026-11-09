---
symbol: "ERGIC2"
type: "gene"
col: 1509
ensembl_id: "ENSG00000087502"
name: "ERGIC and golgi 2"
location: "12p11.22"
module: 233
arm: "+"
pooled_cpm: 85.73
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/233"]
generated_by: "tahoemap"
---

# ERGIC2

*ERGIC and golgi 2* — 12p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.40× (z +20.0, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.75× (z +6.7, q 4e-09, up in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H1792 4.08×, SNU-423 4.83×, A498 2.90×, CFPAC-1 3.28×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-423 4.96×, NCI-H1792 3.53×, HOP62 3.09×, CFPAC-1 3.41×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 3.97×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.924× (z -6.0, q 1e-06, down in 1 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.788× (z -5.4, q 1e-05, down in 25 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (SHP-77 0.512×, LoVo 0.560×, RKO 0.584×, C32 0.538×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.508×, A-427 0.531×, HOP62 0.618×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.368×; ⚠ cell-cycle shift, explains ~95% of this change); [[Rosiglitazone (drug)]] 0.5 µM in 1 line (SW 1088 0.0748×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF2]] (+0.56, fdr 1e-05), [[JPX]] (+0.56, fdr 1e-05), [[API5]] (+0.56, fdr 4e-05); moves opposite to [[SNHG1]] (-0.63, fdr 1e-05), [[TRIM36]] (-0.60, fdr 2e-05), [[RBM38]] (-0.57, fdr 2e-05).
> It is in [[Module 233]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1509.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H1792 4.08×, SNU-423 4.83×, A498 2.90×, CFPAC-1 3.28×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-423 4.96×, NCI-H1792 3.53×, HOP62 3.09×, CFPAC-1 3.41×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 3.97×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +20.0 | 0e+00 | 47/49 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +19.4 | 0e+00 | 41/44 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +12.0 | 4e-31 | 39/45 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +6.7 | 4e-09 | 36/49 (LoVo, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.048 | 19/48 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.048 | 15/48 (HOP62, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.11× | +3.3 | 0.059 | 2/48 (Panc 03.27, CHP-212) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.3 | 0.059 | 7/48 (PANC-1, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.059 | 23/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1509.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (SHP-77 0.512×, LoVo 0.560×, RKO 0.584×, C32 0.538×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.508×, A-427 0.531×, HOP62 0.618×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.368×; ⚠ cell-cycle shift, explains ~95% of this change); [[Rosiglitazone (drug)]] 0.5 µM in 1 line (SW 1088 0.0748×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -6.0 | 1e-06 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -5.6 | 7e-06 | 24/49 (SHP-77, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.788×** | -5.4 | 1e-05 | 25/49 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -5.4 | 1e-05 | 22/48 (SW1417, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.809×** | -4.8 | 2e-04 | 25/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.844× | -3.7 | 0.020 | 18/47 (J82, NCI-H460, …) | rises with dose |  |
| [[Ivermectin (drug)]] 5 µM |  | 0.870× | -3.2 | 0.13 | 5/48 (A498, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 88.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 153 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.09× (z +14.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.618× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 63.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +13.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 96.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 78.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +15.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 63.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +11.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 75.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +14.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 60.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +12.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 84.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +13.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 86.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -12.0) ⚠ cell-cycle shift, explains ~95% of this change |
| [[NCI-H1792 (line)]] | alt | 101 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +17.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 76.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +12.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 96.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +12.5) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.582× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 127 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.24× (z +10.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 65.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +17.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 92.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.76× (z +10.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.601× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 69.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 80.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +10.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 64.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 74.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 41.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 56.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 98.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +13.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 85.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 76.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +10.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 75.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +10.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 96.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.443× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 88.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.04× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 77.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 76.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 66.1 | 0 | 1 | — | [[Rosiglitazone (drug)]] 0.5 µM 0.0748× (z -8.7) |
| [[AN3 CA (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | +0.56 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[JPX]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[API5]] | +0.56 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[VPS50]] | +0.55 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[DPP8]] | +0.55 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[SNX19]] | +0.55 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[GFM1]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[FAF2]] | +0.53 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[C12orf4]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CWC27]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SDHC]] | +0.53 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NUP155]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG1]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[TRIM36]] | -0.60 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[RBM38]] | -0.57 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[LONRF1]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[FAM53C]] | -0.54 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[SNHG7]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[EPB41L5]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CNNM4]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[IFRD1]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PIM2]] | -0.50 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[SNHG12]] | -0.50 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ZFAS1]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 233]]; 6 genes; every member is in the + arm (projection on the module's main direction -0.644). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.2, -24.7); signed map (-16.7, -27.3). **Vector** length 97.4, 24.0% of its response variance represented; |z| ≥ 3 in 715 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +20.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +19.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +3.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.1 | +2.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +1.8 | +2.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.7 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.5 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.3 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ERGIC and golgi 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.22 — chr12:29,337,352-29,381,189 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTX1, Erv41 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RQ1](https://www.uniprot.org/uniprotkb/Q96RQ1) (Endoplasmic reticulum-Golgi intermediate compartment protein 2):

> Possible role in transport between endoplasmic reticulum and Golgi.

**Summary**, from NCBI Gene [51290](https://www.ncbi.nlm.nih.gov/gene/51290):

> ERGIC2, or PTX1, is a ubiquitously expressed nuclear protein that is downregulated in prostate carcinoma (Kwok et al., 2001 [PubMed 11445006]).[supplied by OMIM, Aug 2008]

**Accessions** — [HGNC:30208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30208) · Entrez [51290](https://www.ncbi.nlm.nih.gov/gene/51290) · UniProt [Q96RQ1](https://www.uniprot.org/uniprotkb/Q96RQ1) · Ensembl [ENSG00000087502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087502)

## Data

Gene col 1509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1509); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1509]; `tensor/DDL_lfc|DDL_z.npy` [1509]; `embed/gene_vectors.npy` [1509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1509 or target_col == 1509). Every well: [[ERGIC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERGIC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
