---
symbol: "UBXN2A"
type: "gene"
col: 10449
ensembl_id: "ENSG00000173960"
name: "UBX domain protein 2A"
location: "2p23.3"
module: 46
arm: "+"
pooled_cpm: 66.5
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# UBXN2A

*UBX domain protein 2A* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +24.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.922× (z -6.2, q 3e-07, down in 2 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.700× (z -4.2, q 0.006, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (HT-29 0.114×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.449×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSTD3]] (+0.71, fdr 2e-05), [[LRRC57]] (+0.70, fdr 1e-05), [[WBP4]] (+0.68, fdr 1e-05); moves opposite to [[SND1]] (-0.67, fdr 2e-05), [[MATCAP1]] (-0.63, fdr 7e-05), [[AMPD2]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC2A1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +24.9 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +18.6 | 0e+00 | 47/49 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +10.9 | 2e-25 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +9.4 | 8e-19 | 36/49 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +9.2 | 5e-18 | 36/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.1 | 6e-18 | 31/44 (SHP-77, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +8.9 | 4e-17 | 32/45 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +7.8 | 4e-13 | 37/47 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +5.8 | 4e-07 | 25/48 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.5 | 2e-06 | 27/48 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +5.4 | 4e-06 | 21/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.2 | 8e-06 | 16/48 (A498, RKO, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 2e-05 | 26/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.9 | 4e-05 | 26/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 1e-04 | 20/48 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | 1.15× | +4.4 | 3e-04 | 15/48 (CFPAC-1, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.0 | 0.002 | 16/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.8 | 0.005 | 17/48 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.7 | 0.007 | 10/49 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.070 | 6/48 (MIA PaCa-2, C32, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.070 | 5/48 (SNU-423, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10449.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (HT-29 0.114×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.449×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -6.2 | 3e-07 | 2/49 (SW 1088, CHP-212) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.700×** | -4.2 | 0.006 | 23/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.823×** | -4.2 | 0.006 | 18/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.890× | -3.7 | 0.026 | 11/48 (Hs 766T, HEC-1-A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.848× | -3.5 | 0.050 | 14/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.762× | -3.2 | 0.12 | 18/49 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.870× | -3.1 | 0.18 | 9/49 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 56.4 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.2) | — |
| [[BT-474 (line)]] | alt | 59.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 65.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +21.5) | — |
| [[NCI-H460 (line)]] | wt | 59.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +25.3) | — |
| [[PANC-1 (line)]] | alt | 74.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +26.7) | — |
| [[SW480 (line)]] | alt | 91.9 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 43.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +16.1) | — |
| [[HT-29 (line)]] | alt | 44.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.1) | [[Lonafarnib (drug)]] 5 µM 0.114× (z -10.0) ⚠ toxic |
| [[KATO III (line)]] | alt | 61.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.7) | — |
| [[LS 180 (line)]] | wt | 45.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 89.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.5) | — |
| [[A-427 (line)]] | wt | 114 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.7) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.449× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 84.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.5) | — |
| [[C32 (line)]] | wt | 57.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 54.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +15.6) | — |
| [[HEC-1-A (line)]] | alt | 90.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +17.4) | — |
| [[HepG2_C3A (line)]] | wt | 80.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 66.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +16.9) | — |
| [[Hs 766T (line)]] | wt | 49.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.9) | — |
| [[LoVo (line)]] | wt | 58.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 59.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +13.7) | — |
| [[NCI-H23 (line)]] | alt | 67.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +10.5) | — |
| [[RKO (line)]] | wt | 63.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 58.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 48.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 105 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.6) | — |
| [[A-172 (line)]] | wt | 90.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 62.9 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 2.02× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 68.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 38.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.5) | — |
| [[J82 (line)]] | alt | 42.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 85.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 65.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 55.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.1) | — |
| [[SW48 (line)]] | wt | 52.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 15 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSTD3]] | +0.71 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[LRRC57]] | +0.70 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[WBP4]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[WAC-AS1]] | +0.68 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[TCEAL4]] | +0.67 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[HACD1]] | +0.66 | +0.71 / +0.34 | both halves | 1e-04 |  |
| [[DCUN1D1]] | +0.65 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.65 | +0.70 / +0.32 | both halves | 2e-04 |  |
| [[RDX]] | +0.64 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[RNF115]] | +0.64 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[FBXW4]] | +0.64 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[FAIM]] | +0.63 | +0.53 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SND1]] | -0.67 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[MATCAP1]] | -0.63 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[AMPD2]] | -0.62 | -0.74 / -0.41 | both halves | 4e-05 |  |
| [[GNB1L]] | -0.62 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[ST6GALNAC4]] | -0.62 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[SIPA1]] | -0.61 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[SLC2A1]] | -0.59 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[LPCAT1]] | -0.57 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[DCUN1D3]] | -0.57 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[DCAF13]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[NME7]] | -0.56 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[MRPL17]] | -0.56 | -0.43 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A1]] | C | SLC2A1 activity lowers UBXN2A's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 1.54× higher at baseline in the lines without SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.4, 10.9); signed map (22.5, -20.4). **Vector** length 111, 29.2% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +24.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +18.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +9.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.2 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +3.0 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.9 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.7 | -4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | UBX domain protein 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:23,927,285-24,004,909 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously UBXD4 |
| Gene groups (HGNC) | UBX domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P68543](https://www.uniprot.org/uniprotkb/P68543) (UBX domain-containing protein 2A):

> Acts to repress the ubiquitination and subsequent endoplasmic reticulum-associated degradation of CHRNA3 by the STUB1-VCP-UBXN2A complex in cortical neurons. Also acts to promote the translocation of CHRNA3 to the plasma membrane and subsequently increases plasma membrane acetylcholine-gated ion-channel activation (By similarity). Plays a role in the inhibition of STUB1-mediated TP53 degradation, via its interaction with HSPA9 which acts to inhibit TP53 binding to HSPA9. Positively mediates the …

**Summary**, from NCBI Gene [165324](https://www.ncbi.nlm.nih.gov/gene/165324):

> Predicted to enable ubiquitin binding activity. Involved in negative regulation of ERAD pathway; negative regulation of proteolysis; and positive regulation of protein catabolic process. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27265) · Entrez [165324](https://www.ncbi.nlm.nih.gov/gene/165324) · UniProt [P68543](https://www.uniprot.org/uniprotkb/P68543) · Ensembl [ENSG00000173960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173960)

## Data

Gene col 10449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10449); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10449]; `tensor/DDL_lfc|DDL_z.npy` [10449]; `embed/gene_vectors.npy` [10449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10449 or target_col == 10449). Every well: [[UBXN2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBXN2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
