---
symbol: "INPP5F"
type: "gene"
col: 12693
ensembl_id: "ENSG00000198825"
name: "inositol polyphosphate-5-phosphatase F"
location: "10q26.11"
module: 88
arm: "-"
pooled_cpm: 69.91
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# INPP5F

*inositol polyphosphate-5-phosphatase F* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.47× (z +24.8, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.699× (z -7.2, q 2e-10, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTLC2]] (+0.66, fdr 7e-05), [[TNK2]] (+0.66, fdr 3e-05), [[FAM102B]] (+0.65, fdr 1e-05); moves opposite to [[LINC00571]] (-0.70, fdr 2e-05), [[MCPH1]] (-0.68, fdr 2e-05), [[LINC01134]] (-0.65, fdr 3e-05).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NOS1AP]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RGS14]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.47×** | +24.8 | 0e+00 | 45/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.24×** | +23.5 | 0e+00 | 45/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.97×** | +21.7 | 0e+00 | 44/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +11.4 | 7e-28 | 42/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +9.4 | 7e-19 | 38/47 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.38×** | +9.1 | 1e-17 | 40/48 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +8.3 | 1e-14 | 37/47 (RKO, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 1e-05 | 24/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.9 | 6e-05 | 26/46 (NCI-H1792, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.002 | 20/47 (RKO, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.2 | 0.070 | 15/42 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12693.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.699×** | -7.2 | 2e-10 | 29/47 (SK-MEL-2, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -7.2 | 2e-10 | 36/48 (A-172, NCI-H1792, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.680×** | -7.1 | 2e-10 | 25/42 (NCI-H661, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -6.3 | 4e-08 | 29/47 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.764×** | -5.2 | 2e-05 | 22/40 (SHP-77, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.778×** | -5.0 | 4e-05 | 22/47 (C32, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.779×** | -5.0 | 5e-05 | 26/47 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -4.7 | 2e-04 | 23/47 (SK-MEL-2, C32, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -4.5 | 3e-04 | 15/47 (SK-MEL-2, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -4.3 | 0.001 | 20/47 (SK-MEL-2, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.9 | 0.005 | 19/47 (SK-MEL-2, HT-29, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.869× | -3.8 | 0.006 | 15/48 (CFPAC-1, C32, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.768×** | -3.8 | 0.007 | 18/47 (C32, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.826×** | -3.7 | 0.007 | 15/48 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.878× | -3.7 | 0.008 | 13/47 (SK-MEL-2, NCI-H1792, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.781×** | -3.5 | 0.014 | 12/46 (LS 180, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.727×** | -3.3 | 0.025 | 15/47 (SK-MEL-2, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.848× | -3.2 | 0.042 | 17/46 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.881× | -3.1 | 0.048 | 16/47 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 458 | 0 | 24 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -21.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -16.5) |
| [[C32 (line)]] | wt | 309 | 0 | 16 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -20.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.266× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 38.7 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -10.0) |
| [[RKO (line)]] | wt | 42.2 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +12.7) | — |
| [[SW1417 (line)]] | alt | 69.2 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 44.1 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.05× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 68.3 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.534× (z -9.0) |
| [[LoVo (line)]] | wt | 31.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.34× (z +17.2) | — |
| [[LS 180 (line)]] | wt | 30.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.96× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 58.9 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 105 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +14.3) | — |
| [[SW48 (line)]] | wt | 39.4 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 5.00× (z +10.6) | [[Cobimetinib (drug)]] 0.05 µM 0.180× (z -10.4) |
| [[A-172 (line)]] | wt | 83.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 52.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +10.2) | — |
| [[A498 (line)]] | wt | 43.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.09× (z +10.9) | — |
| [[A549 (line)]] | wt | 66.0 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 60.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +13.1) | — |
| [[H4 (line)]] | wt | 39.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.29× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 48.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 48.8 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.82× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 64.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.63× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 36.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 47.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.36× (z +15.5) | — |
| [[hTERT-HPNE (line)]] | wt | 37.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.31× (z +11.8) | — |
| [[J82 (line)]] | alt | 28.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +12.4) | — |
| [[KATO III (line)]] | alt | 39.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.26× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 23.2 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.33× (z +9.8) | [[Harringtonine (drug)]] 0.5 µM 0.352× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 43.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.55× (z +16.5) | — |
| [[Panc 03.27 (line)]] | alt | 95.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.00× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -11.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 39.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.99× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 65.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +13.5) | — |
| [[SW 900 (line)]] | alt | 87.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 90.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 111 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 94.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -11.5) |
| [[C-33 A (line)]] | alt | 60.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 56.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.111× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 63.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0465× (z -12.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -14.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 35.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTLC2]] | +0.66 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[TNK2]] | +0.66 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[FAM102B]] | +0.65 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CYTH3]] | +0.65 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[SLC27A1]] | +0.65 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[STRN]] | +0.64 | +0.62 / +0.43 | both halves | 4e-05 |  |
| [[RGS14]] | +0.63 | +0.58 / +0.25 | both halves | 4e-04 |  |
| [[GNAI2]] | +0.63 | +0.51 / +0.30 | both halves | 2e-04 |  |
| [[CEP131]] | +0.63 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[AFDN]] | +0.63 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[NOS1AP]] | +0.63 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[AFAP1]] | +0.63 | +0.56 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00571]] | -0.70 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[MCPH1]] | -0.68 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LINC01134]] | -0.65 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | -0.65 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[FAM200A]] | -0.65 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[C1S]] | -0.64 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[AEBP2]] | -0.64 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[WDR33]] | -0.64 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[RAB30-DT]] | -0.64 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[GTF2H1]] | -0.64 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[PBLD]] | -0.64 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[MR1]] | -0.63 | -0.58 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOS1AP]] | B | NOS1AP activity raises INPP5F's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without NOS1AP | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[ABCC2]] | B | ABCC2 activity lowers INPP5F's level | lines that do not express ABCC2 (22) vs lines expressing it (28) | 1.33× higher at baseline in the lines without ABCC2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers INPP5F's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers INPP5F's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DNMT3B]] | C | DNMT3B activity raises INPP5F's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without DNMT3B | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS14]] | C | INPP5F's natural level strengthens RGS14's drug response | INPP5F's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.39; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (6.8, 5.4); signed map (-21.2, 20.7). **Vector** length 127, 38.0% of its response variance represented; |z| ≥ 3 in 1,341 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.9 | +21.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.9 | +11.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | +23.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +24.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +8.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.3 | +9.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.0 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.5 | -7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.6 | -6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.5 | -7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate-5-phosphatase F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:119,726,042-119,829,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAC2, KIAA0966, hSac2 |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the early endosome membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2H2](https://www.uniprot.org/uniprotkb/Q9Y2H2) (Phosphatidylinositide 4-phosphatase SAC2):

> Phosphoinositide phosphatase which catalyzes the hydrolysis of phosphatidylinositol 4-phosphate (1,2-diacyl-sn-glycero-3-phospho-(1D-myo-inositol 4-phosphate), PtdIns(4)P). May be functionally linked to OCRL, which converts phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2) to PtdIns, for a sequential dephosphorylation of (PtdIns(4,5)P2) at the 5 and 4 position of inositol, thus playing an important role in the endocytic recycling. Regulator of TF:TFRC and integrins recycling pathway, is …

**Summary**, from NCBI Gene [22876](https://www.ncbi.nlm.nih.gov/gene/22876):

> The protein encoded by this gene is an inositol 1,4,5-trisphosphate (InsP3) 5-phosphatase and contains a Sac domain. The activity of this protein is specific for phosphatidylinositol 4,5-bisphosphate and phosphatidylinositol 3,4,5-trisphosphate. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:17054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17054) · Entrez [22876](https://www.ncbi.nlm.nih.gov/gene/22876) · UniProt [Q9Y2H2](https://www.uniprot.org/uniprotkb/Q9Y2H2) · Ensembl [ENSG00000198825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198825)

## Data

Gene col 12693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12693); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12693]; `tensor/DDL_lfc|DDL_z.npy` [12693]; `embed/gene_vectors.npy` [12693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12693 or target_col == 12693). Every well: [[INPP5F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INPP5F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
