---
symbol: "POLG2"
type: "gene"
col: 14994
ensembl_id: "ENSG00000256525"
name: "DNA polymerase gamma 2, accessory subunit"
location: "17q23.3"
module: 38
arm: "+"
pooled_cpm: 45.32
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# POLG2

*DNA polymerase gamma 2, accessory subunit* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.34× (z +36.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.742× (z -4.6, q 0.002, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.144×, NCI-H23 0.216×, SK-MEL-2 0.220×, HCT15 0.169×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (SW480 0.510×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGF18]] (+0.69, fdr 7e-06), [[TRIM72]] (+0.68, fdr 7e-06), [[LDHC]] (+0.67, fdr 7e-06); moves opposite to [[TMTC3]] (-0.60, fdr 2e-05), [[DLD]] (-0.55, fdr 2e-05), [[FAHD2CP]] (-0.52, fdr 4e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PRKCG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.34×** | +36.5 | 0e+00 | 48/48 (CFPAC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.14×** | +25.0 | 0e+00 | 43/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.01×** | +10.8 | 7e-25 | 44/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +9.8 | 2e-20 | 35/49 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +9.5 | 2e-19 | 37/48 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.78×** | +8.9 | 4e-17 | 40/48 (A498, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +8.2 | 2e-14 | 30/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.66×** | +7.9 | 3e-13 | 35/48 (A498, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.4 | 9e-12 | 33/48 (A-172, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.6 | 2e-09 | 33/47 (CFPAC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +6.5 | 4e-09 | 30/48 (SNU-423, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +6.1 | 5e-08 | 29/48 (A498, HS-578T, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +5.5 | 1e-06 | 29/48 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.38×** | +5.0 | 2e-05 | 26/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +4.8 | 7e-05 | 25/47 (A-172, Panc 03.27, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +4.6 | 2e-04 | 25/48 (A498, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.007 | 19/48 (A-427, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.021 | 15/48 (NCI-H2347, NCI-H23, …) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.021 | 13/49 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.021 | 19/48 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.033 | 17/47 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.045 | 16/47 (PANC-1, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14994.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.144×, NCI-H23 0.216×, SK-MEL-2 0.220×, HCT15 0.169×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (SW480 0.510×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.742×** | -4.6 | 0.002 | 25/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.790× | -3.4 | 0.17 | 19/48 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.812× | -3.2 | 0.25 | 17/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.806× | -3.1 | 0.30 | 12/48 (A-427, NCI-H460, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 34.4 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +31.4) | — |
| [[HS-578T (line)]] | alt | 23.7 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.91× (z +20.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 56.1 | 5 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.95× (z +23.9) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 61.7 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +27.2) | [[Ixazomib citrate (drug)]] 5 µM 0.510× (z -9.1) |
| [[A-172 (line)]] | wt | 27.1 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.71× (z +25.0) | — |
| [[C32 (line)]] | wt | 60.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +16.5) | — |
| [[HEC-1-A (line)]] | alt | 56.1 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.99× (z +24.3) | — |
| [[HOP62 (line)]] | alt | 51.2 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.77× (z +27.0) | — |
| [[CFPAC-1 (line)]] | alt | 40.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.62× (z +29.6) | — |
| [[HCT15 (line)]] | alt | 56.2 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 65.8 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 22.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +26.8) | — |
| [[SK-MEL-2 (line)]] | alt | 59.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 23.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.9× (z +28.5) | — |
| [[BT-474 (line)]] | alt | 24.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.8× (z +26.4) | — |
| [[COLO 205 (line)]] | alt | 26.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +19.5) | — |
| [[H4 (line)]] | wt | 53.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +15.4) | — |
| [[LoVo (line)]] | wt | 41.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +17.2) | — |
| [[LS 180 (line)]] | wt | 25.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +15.6) | — |
| [[NCI-H460 (line)]] | wt | 44.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +27.6) | — |
| [[Panc 03.27 (line)]] | alt | 42.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +29.0) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 36.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +23.0) | — |
| [[SW 900 (line)]] | alt | 43.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +21.9) | — |
| [[CHP-212 (line)]] | wt | 126 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +11.3) | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0903× (z -8.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 39.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.40× (z +14.2) | — |
| [[hTERT-HPNE (line)]] | wt | 60.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.81× (z +17.1) | — |
| [[KATO III (line)]] | alt | 37.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +20.0) | — |
| [[LOX-IMVI (line)]] | wt | 67.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.58× (z +20.1) | — |
| [[NCI-H1792 (line)]] | alt | 38.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +21.5) | — |
| [[NCI-H2030 (line)]] | alt | 49.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +15.5) | — |
| [[RPMI-7951 (line)]] | alt | 34.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +15.1) | — |
| [[SNU-1 (line)]] | wt | 34.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.58× (z +14.9) | — |
| [[SW1417 (line)]] | alt | 27.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.28× (z +23.6) | — |
| [[SW48 (line)]] | wt | 36.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.13× (z +16.8) | — |
| [[A549 (line)]] | wt | 42.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +26.6) | — |
| [[C-33 A (line)]] | alt | 83.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +12.8) | — |
| [[HepG2_C3A (line)]] | wt | 53.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.21× (z +14.5) | — |
| [[Hs 766T (line)]] | wt | 54.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +13.1) | — |
| [[J82 (line)]] | alt | 29.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +20.6) | — |
| [[NCI-H1573 (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 51.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +19.8) | — |
| [[RKO (line)]] | wt | 33.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +17.1) | — |
| [[SHP-77 (line)]] | alt | 42.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +13.0) | — |
| [[A-427 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGF18]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[TRIM72]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[LDHC]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[LRRC23]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[PRX]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[PPIEL-1]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[INTS6]] | +0.62 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[AZU1]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PPIEL]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[PYY]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PPP1R36]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC3]] | -0.60 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[DLD]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[FAHD2CP]] | -0.52 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[ANXA7]] | -0.52 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[USP14]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[BLMH]] | -0.50 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[OCRL]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[COMMD2]] | -0.48 | -0.48 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCG]] | B | PRKCG activity raises POLG2's level | lines that do not express PRKCG (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without PRKCG | 0.044 | ⚠ within organs, on part of the lines; also absent: SLC36A4, DBN1, CEP41; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers POLG2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ROPN1L]] | C | ROPN1L activity raises POLG2's level | lines that do not express ROPN1L (3) vs lines expressing it (47) | 1.69× lower at baseline in the lines without ROPN1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NBEAP2, FAM229B, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.2, -17.3); signed map (15.4, 11.9). **Vector** length 103, 27.3% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +36.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +25.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.6 | +6.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.9 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.2 | +7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -3.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.8 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase gamma 2, accessory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:64,477,785-64,497,054 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MTPOLB, HP55 |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 5 pathways, smallest: Strand-asynchronous mitochondrial DNA replication; Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHN1](https://www.uniprot.org/uniprotkb/Q9UHN1) (DNA polymerase subunit gamma-2):

> Accessory subunit of DNA polymerase gamma solely responsible for replication of mitochondrial DNA (mtDNA). Acts as an allosteric regulator of the holoenzyme activities. Enhances the polymerase activity and the processivity of POLG by increasing its interactions with the DNA template. Suppresses POLG exonucleolytic proofreading especially toward homopolymeric templates bearing mismatched termini. Binds to single-stranded DNA.

**Summary**, from NCBI Gene [11232](https://www.ncbi.nlm.nih.gov/gene/11232):

> This gene encodes the processivity subunit of the mitochondrial DNA polymerase gamma. The encoded protein forms a heterotrimer containing one catalytic subunit and two processivity subunits. This protein enhances DNA binding and promotes processive DNA synthesis. Mutations in this gene result in autosomal dominant progressive external ophthalmoplegia with mitochondrial DNA deletions.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:9180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9180) · Entrez [11232](https://www.ncbi.nlm.nih.gov/gene/11232) · UniProt [Q9UHN1](https://www.uniprot.org/uniprotkb/Q9UHN1) · Ensembl [ENSG00000256525](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256525)

## Data

Gene col 14994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14994); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14994]; `tensor/DDL_lfc|DDL_z.npy` [14994]; `embed/gene_vectors.npy` [14994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14994 or target_col == 14994). Every well: [[POLG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
