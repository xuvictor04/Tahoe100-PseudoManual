---
symbol: "LRP11"
type: "gene"
col: 4171
ensembl_id: "ENSG00000120256"
name: "LDL receptor related protein 11"
location: "6q25.1"
module: 29
arm: "+"
pooled_cpm: 52.92
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# LRP11

*LDL receptor related protein 11* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.31× (z +15.5, q 0e+00, up in 36 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +8.8, q 1e-16, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.562× (z -11.0, q 1e-25, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGK]] (+0.64, fdr 1e-05), [[LAMP2]] (+0.61, fdr 1e-05), [[SCARB2]] (+0.57, fdr 1e-05); moves opposite to [[ZNF593]] (-0.57, fdr 2e-04), [[NDUFB9]] (-0.56, fdr 1e-05), [[MRPL46]] (-0.56, fdr 3e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[MRPL32]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +15.5 | 0e+00 | 36/40 (CFPAC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +13.6 | 2e-39 | 42/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +9.9 | 1e-20 | 33/42 (CFPAC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +8.8 | 1e-16 | 32/47 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +6.4 | 1e-08 | 34/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.30×** | +5.1 | 3e-05 | 28/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.5 | 4e-04 | 22/49 (NCI-H23, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.5 | 4e-04 | 20/48 (SW480, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.004 | 17/48 (NCI-H1573, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +3.8 | 0.008 | 22/48 (A-172, SW480, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.009 | 13/48 (SW 900, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.009 | 19/49 (NCI-H1573, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.011 | 16/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.012 | 17/49 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.20×** | +3.6 | 0.014 | 17/48 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.016 | 17/48 (NCI-H1573, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.022 | 13/47 (NCI-H1573, A549, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.4 | 0.023 | 11/48 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.027 | 14/49 (NCI-H1573, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.028 | 9/48 (NCI-H1792, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.052 | 19/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.067 | 13/48 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4171.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.562×** | -11.0 | 1e-25 | 36/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.693×** | -9.9 | 1e-20 | 31/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.649×** | -8.3 | 3e-14 | 28/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -7.6 | 4e-12 | 28/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.666×** | -7.5 | 9e-12 | 29/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.675×** | -7.1 | 1e-10 | 29/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -6.7 | 1e-09 | 33/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.523×** | -6.5 | 6e-09 | 32/45 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.561×** | -5.8 | 4e-07 | 25/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.700×** | -5.6 | 1e-06 | 30/48 (PANC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.612×** | -4.9 | 4e-05 | 23/48 (H4, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.780×** | -4.7 | 1e-04 | 24/48 (A-172, SNU-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.656×** | -4.2 | 0.001 | 23/48 (C32, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.660×** | -4.2 | 0.001 | 18/48 (NCI-H1792, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.662×** | -4.1 | 0.001 | 18/46 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.807×** | -3.9 | 0.003 | 21/49 (PANC-1, SW 1088, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.750×** | -3.9 | 0.003 | 18/48 (PANC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.692×** | -3.7 | 0.007 | 18/48 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 157 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -15.9) |
| [[A-427 (line)]] | wt | 68.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -20.4) |
| [[A-172 (line)]] | wt | 65.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -18.6) |
| [[NCI-H23 (line)]] | alt | 95.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -12.2) |
| [[SW480 (line)]] | alt | 39.4 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +10.2) | [[TAK-901 (drug)]] 5 µM 0.210× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 27.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.33× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 33.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +10.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 46.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.5) |
| [[C32 (line)]] | wt | 51.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -9.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.373× (z -8.5) |
| [[HS-578T (line)]] | alt | 55.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 44.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 30.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 16.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -8.5) |
| [[SNU-423 (line)]] | alt | 61.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.7) |
| [[SW1417 (line)]] | alt | 63.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 40.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +11.1) | — |
| [[H4 (line)]] | wt | 75.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 35.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 54.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -8.5) |
| [[HT-29 (line)]] | alt | 50.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.364× (z -9.3) |
| [[J82 (line)]] | alt | 41.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.351× (z -11.0) |
| [[KATO III (line)]] | alt | 84.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.448× (z -9.0) |
| [[LoVo (line)]] | wt | 40.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 46.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 73.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 46.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 37.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.140× (z -11.1) |
| [[A498 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGK]] | +0.64 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[LAMP2]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SCARB2]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ADAM9]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[CLSTN1]] | +0.56 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[GALNT2]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[AIDA]] | +0.55 | +0.36 / +0.63 | both halves | 9e-05 |  |
| [[CRTAP]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[IL13RA1]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TMEM123]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[HADHA]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[TMEM30A]] | +0.54 | +0.39 / +0.53 | both halves | 5e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF593]] | -0.57 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[NDUFB9]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[MRPL46]] | -0.56 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[LPAR5]] | -0.54 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[MRPS18C]] | -0.53 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[COMMD5]] | -0.53 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[ZNF579]] | -0.53 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[PAQR6]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[HSD17B2-AS1]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[PEX16]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[MRPL27]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[DAXX]] | -0.52 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRPL32]] | C | LRP11's natural level strengthens MRPL32's drug response | LRP11's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.09; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[LLPH]] | C | LRP11's natural level strengthens LLPH's drug response | LRP11's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.13; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.1, -20.2); signed map (-23.7, -37.2). **Vector** length 102, 26.3% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.7 | +2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +4.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.4 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.5 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -11.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -5.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -1.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:149,818,757-149,864,359 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA350J20.3, MANSC3 |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Matched by | ensembl_id |

UniProt [Q86VZ4](https://www.uniprot.org/uniprotkb/Q86VZ4) carries no function annotation.

**Summary**, from NCBI Gene [84918](https://www.ncbi.nlm.nih.gov/gene/84918):

> Enables phosphoprotein binding activity. Predicted to be involved in several processes, including response to cold; response to heat; and response to water deprivation. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16936](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16936) · Entrez [84918](https://www.ncbi.nlm.nih.gov/gene/84918) · UniProt [Q86VZ4](https://www.uniprot.org/uniprotkb/Q86VZ4) · Ensembl [ENSG00000120256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120256)

## Data

Gene col 4171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4171); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4171]; `tensor/DDL_lfc|DDL_z.npy` [4171]; `embed/gene_vectors.npy` [4171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4171 or target_col == 4171). Every well: [[LRP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
