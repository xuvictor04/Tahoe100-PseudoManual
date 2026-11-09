---
symbol: "CYB5R4"
type: "gene"
col: 798
ensembl_id: "ENSG00000065615"
name: "cytochrome b5 reductase 4"
location: "6q14.2"
module: 57
arm: "+"
pooled_cpm: 57.36
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# CYB5R4

*cytochrome b5 reductase 4* — 6q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.86× (z +10.4, q 1e-22, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.743× (z -7.0, q 1e-09, down in 31 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 0.324×, NCI-H1792 0.340×, NCI-H2347 0.410×, NCI-H1573 0.380×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.421×, LS 180 0.470×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.400×, NCI-H1792 0.384×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX7]] (+0.67, fdr 7e-06), [[PLA2G12A]] (+0.66, fdr 1e-05), [[RPP30]] (+0.65, fdr 7e-06); moves opposite to [[ZNF689]] (-0.61, fdr 1e-05), [[TLNRD1]] (-0.60, fdr 1e-05), [[HIVEP1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WNK4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +10.4 | 1e-22 | 43/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.26×** | +10.2 | 3e-22 | 41/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +9.4 | 7e-19 | 43/48 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +9.1 | 1e-17 | 42/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +8.7 | 5e-16 | 41/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +7.9 | 2e-13 | 43/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +7.4 | 9e-12 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +6.9 | 4e-10 | 37/48 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.25×** | +5.4 | 5e-06 | 27/48 (Hs 766T, LoVo, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 3e-05 | 27/48 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +4.5 | 3e-04 | 28/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.004 | 24/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.26×** | +3.8 | 0.005 | 19/48 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.011 | 23/49 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.012 | 24/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.023 | 20/48 (HOP62, SW 1271, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.091 | 8/48 (PANC-1, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 798.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 0.324×, NCI-H1792 0.340×, NCI-H2347 0.410×, NCI-H1573 0.380×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.421×, LS 180 0.470×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.400×, NCI-H1792 0.384×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -7.0 | 1e-09 | 31/49 (A549, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.706×** | -5.6 | 7e-06 | 24/41 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -4.6 | 8e-04 | 22/47 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.767×** | -4.4 | 0.001 | 27/49 (NCI-H2347, NCI-H1792, …) | rises with dose | composition shift |
| [[OTS514 (drug)]] 5 µM |  | **0.648×** | -3.7 | 0.021 | 23/46 (H4, SW48, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.871× | -3.2 | 0.10 | 11/48 (A498, SK-MEL-2, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.760× | -3.2 | 0.10 | 18/48 (HCT15, Hs 766T, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.822× | -3.1 | 0.10 | 21/50 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | 0.829× | -3.1 | 0.10 | 21/48 (NCI-H661, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.876× | -3.1 | 0.10 | 10/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.769× | -3.1 | 0.10 | 15/47 (SW 1271, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 0.701× | -3.1 | 0.10 | 20/45 (MIA PaCa-2, SNU-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.8 | 10 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.39× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 72.6 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +16.0) | — |
| [[NCI-H1792 (line)]] | alt | 83.9 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 57.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 51.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 47.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 55.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.99× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 51.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[AN3 CA (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.213× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 57.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 88.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.11× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 47.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.362× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 49.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.89× (z +9.3) | — |
| [[NCI-H661 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0957× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 58.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.40× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 86.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +9.4) | — |
| [[SW480 (line)]] | alt | 63.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.13× (z +11.1) | — |
| [[A-172 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX7]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PLA2G12A]] | +0.66 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[RPP30]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[FXR1]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[STAM]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[SNX3]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TMEM9]] | +0.63 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[VAMP7]] | +0.62 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[SCPEP1]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[OSBPL9]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ABRAXAS1]] | +0.61 | +0.43 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF689]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.59 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ZCCHC3]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SIX5]] | -0.59 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[KDSR]] | -0.59 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[PPRC1]] | -0.58 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.58 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[ZBED5]] | -0.58 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CYREN]] | -0.57 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[SATB2]] | -0.56 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[BRD1]] | -0.56 | -0.49 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK4]] | B | WNK4 activity lowers CYB5R4's level | lines that do not express WNK4 (5) vs lines expressing it (45) | 1.38× higher at baseline in the lines without WNK4 | 0.060 | ⚠ within organs, on part of the lines; also absent: TEX14, TMEM144, NEO1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.2, -6.9); signed map (-34.0, -14.8). **Vector** length 92.1, 24.2% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +8.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.2 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +9.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | -0.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.1 | +1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.6 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b5 reductase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.2 — chr6:83,859,656-83,967,423 (+) |
| Ensembl biotype | protein_coding |
| Also known as | b5+b5R, dJ676J13.1; previously NCB5OR |
| Gene groups (HGNC) | Cytochrome b5 reductases; Flavoproteins; Cytochrome b5 domain containing |
| Reactome | 3 pathways, smallest: Erythrocytes take up carbon dioxide and release oxygen; O2/CO2 exchange in erythrocytes; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L1T6](https://www.uniprot.org/uniprotkb/Q7L1T6) (Cytochrome b5 reductase 4):

> NADH-cytochrome b5 reductase involved in endoplasmic reticulum stress response pathway. Plays a critical role in protecting pancreatic beta-cells against oxidant stress, possibly by protecting the cell from excess buildup of reactive oxygen species (ROS). Reduces a variety of substrates in vitro, such as cytochrome c, feericyanide and methemoglobin.

**Summary**, from NCBI Gene [51167](https://www.ncbi.nlm.nih.gov/gene/51167):

> NCB5OR is a flavohemoprotein that contains functional domains found in both cytochrome b5 (CYB5A; MIM 613218) and CYB5 reductase (CYB5R3; MIM 613213) (Zhu et al., 1999 [PubMed 10611283]).[supplied by OMIM, Jan 2010]

**Accessions** — [HGNC:20147](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20147) · Entrez [51167](https://www.ncbi.nlm.nih.gov/gene/51167) · UniProt [Q7L1T6](https://www.uniprot.org/uniprotkb/Q7L1T6) · Ensembl [ENSG00000065615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065615)

## Data

Gene col 798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 798); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 798]; `tensor/DDL_lfc|DDL_z.npy` [798]; `embed/gene_vectors.npy` [798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 798 or target_col == 798). Every well: [[CYB5R4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYB5R4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
