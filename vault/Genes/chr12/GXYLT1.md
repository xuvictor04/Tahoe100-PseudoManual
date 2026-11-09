---
symbol: "GXYLT1"
type: "gene"
col: 7497
ensembl_id: "ENSG00000151233"
name: "glucoside xylosyltransferase 1"
location: "12q12"
module: 25
arm: "+"
pooled_cpm: 59.58
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# GXYLT1

*glucoside xylosyltransferase 1* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.59× (z +12.7, q 2e-34, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.828× (z -7.4, q 1e-10, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.211×, A-427 0.314×, NCI-H23 0.384×, AN3 CA 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 2 lines (HEC-1-A 0.237×, HS-578T 0.154×; ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.178×; ⚠ toxic; cell-cycle shift, explains ~26% of this change); [[Silodosin (drug)]] 5 µM in 1 line (AN3 CA 0.131×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC13B]] (+0.54, fdr 7e-05), [[MYO6]] (+0.52, fdr 4e-05), [[TMTC3]] (+0.48, fdr 3e-04); moves opposite to [[AGAP4]] (-0.44, fdr 6e-05), [[TM9SF4]] (-0.44, fdr 3e-05), [[UXT]] (-0.42, fdr 6e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CYFIP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +12.7 | 2e-34 | 39/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +12.4 | 5e-33 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +11.1 | 2e-26 | 27/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +8.9 | 6e-17 | 30/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.38×** | +8.9 | 9e-17 | 28/48 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +8.8 | 1e-16 | 28/44 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +7.3 | 3e-11 | 25/48 (J82, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +6.4 | 1e-08 | 27/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.27×** | +6.3 | 2e-08 | 28/47 (A-172, SNU-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +6.0 | 1e-07 | 24/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.52×** | +6.0 | 1e-07 | 21/48 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.21×** | +5.2 | 9e-06 | 21/47 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.20× | +5.0 | 3e-05 | 16/48 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | 1.20× | +4.9 | 4e-05 | 19/49 (A-172, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.9 | 4e-05 | 13/48 (C-33 A, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +4.5 | 2e-04 | 14/48 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.018 | 11/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.08× | +3.2 | 0.034 | 6/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.063 | 14/48 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.08× | +2.8 | 0.092 | 4/48 (A549, LS 180, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.07× | +2.8 | 0.099 | 3/49 (C32, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7497.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.211×, A-427 0.314×, NCI-H23 0.384×, AN3 CA 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 2 lines (HEC-1-A 0.237×, HS-578T 0.154×; ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.178×; ⚠ toxic; cell-cycle shift, explains ~26% of this change); [[Silodosin (drug)]] 5 µM in 1 line (AN3 CA 0.131×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.828×** | -7.4 | 1e-10 | 20/48 (Hs 766T, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.868× | -3.9 | 0.020 | 17/48 (NCI-H661, KATO III, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.905× | -3.9 | 0.020 | 19/48 (C-33 A, NCI-H1573, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.872× | -3.6 | 0.040 | 14/48 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Regorafenib (drug)]] 5 µM |  | **0.781×** | -3.6 | 0.042 | 9/48 (MIA PaCa-2, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 0.886× | -3.3 | 0.087 | 10/48 (NCI-H460, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Adenosine (drug)]] 5 µM |  | 0.925× | -3.0 | 0.19 | 4/48 (SW480, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 87.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 60.0 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +11.2) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[A-172 (line)]] | wt | 45.7 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.73× (z +10.3) ⚠ toxic; cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 68.2 | 0 | 2 (1 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.131× (z -11.0) |
| [[C-33 A (line)]] | alt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 41.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 85.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 90.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 68.7 | 1 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.65× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 76.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -15.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 67.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.237× (z -10.0) ⚠ toxic |
| [[HS-578T (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.154× (z -8.6) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 33.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.384× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 76.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.7) | — |
| [[SW480 (line)]] | alt | 47.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +15.7) | — |
| [[A549 (line)]] | wt | 78.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC13B]] | +0.54 | +0.37 / +0.62 | both halves | 7e-05 |  |
| [[MYO6]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[TMTC3]] | +0.48 | +0.28 / +0.62 | both halves | 3e-04 |  |
| [[FAM199X]] | +0.48 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[EI24]] | +0.48 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[GNPTAB]] | +0.48 | +0.31 / +0.52 | both halves | 2e-04 |  |
| [[BTBD3]] | +0.47 | +0.34 / +0.41 | both halves | 1e-04 |  |
| [[GK5]] | +0.47 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[PPM1A]] | +0.46 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[SNX7]] | +0.46 | +0.26 / +0.52 | both halves | 4e-04 |  |
| [[SVIP]] | +0.46 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[SPOPL]] | +0.46 | +0.33 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP4]] | -0.44 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[TM9SF4]] | -0.44 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[UXT]] | -0.42 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[CMYA5]] | -0.41 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[USP36]] | -0.40 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[TMEM79]] | -0.39 | -0.18 / -0.37 | ⚠ not reproduced | 0.001 |  |
| [[ANKHD1-EIF4EBP3]] | -0.39 | -0.18 / -0.48 | ⚠ not reproduced | 9e-04 |  |
| [[PYY]] | -0.39 | -0.21 / -0.38 | both halves | 6e-04 |  |
| [[LRRC41]] | -0.39 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[RPTOR]] | -0.39 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ECSIT]] | -0.39 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[C1S]] | -0.39 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[TTC41P]] | -0.38 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[DGLUCY]] | -0.38 | -0.35 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYFIP2]] | B | CYFIP2 activity raises GXYLT1's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without CYFIP2 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[TP53]] | C | TP53 activity strengthens GXYLT1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.96× as strongly (z diff +0.05); strongest at Topotecan (hydrochloride) 5 µM: 1.15x vs 1.65x (z diff +3.0) | 0.847 over the table, 0.066 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.295). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.2, 31.2); signed map (5.9, -60.1). **Vector** length 101, 23.6% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.4 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +2.5 | +6.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +6.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.1 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +6.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -7.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | glucoside xylosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:42,081,845-42,144,874 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43151; previously GLT8D3 |
| Gene groups (HGNC) | Glycosyltransferase family 8 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G148](https://www.uniprot.org/uniprotkb/Q4G148) (Glucoside xylosyltransferase 1):

> Glycosyltransferase which elongates the O-linked glucose attached to EGF-like repeats in the extracellular domain of Notch proteins by catalyzing the addition of xylose.

**Summary**, from NCBI Gene [283464](https://www.ncbi.nlm.nih.gov/gene/283464):

> GXYLT1 is a xylosyltransferase (EC 2.4.2.-) that adds the first xylose to O-glucose-modified residues in the epidermal growth factor (EGF; MIM 131530) repeats of proteins such as NOTCH1 (MIM 190198) (Sethi et al., 2010 [PubMed 19940119]).[supplied by OMIM, Mar 2010]

**Accessions** — [HGNC:27482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27482) · Entrez [283464](https://www.ncbi.nlm.nih.gov/gene/283464) · UniProt [Q4G148](https://www.uniprot.org/uniprotkb/Q4G148) · Ensembl [ENSG00000151233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151233)

## Data

Gene col 7497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7497); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7497]; `tensor/DDL_lfc|DDL_z.npy` [7497]; `embed/gene_vectors.npy` [7497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7497 or target_col == 7497). Every well: [[GXYLT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GXYLT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
