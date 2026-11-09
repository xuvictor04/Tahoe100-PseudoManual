---
symbol: "POFUT1"
type: "gene"
col: 2120
ensembl_id: "ENSG00000101346"
name: "protein O-fucosyltransferase 1"
location: "20q11.21"
module: 18
arm: "+"
pooled_cpm: 35.83
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# POFUT1

*protein O-fucosyltransferase 1* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.08× (z +15.7, q 0e+00, up in 38 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 1.46× (z +4.3, q 0.001, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.514× (z -20.1, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFT1]] (+0.76, fdr 7e-06), [[CAD]] (+0.75, fdr 7e-06), [[MTG1]] (+0.74, fdr 7e-06); moves opposite to [[ARID4B]] (-0.63, fdr 1e-05), [[NPHS1]] (-0.62, fdr 3e-05), [[LINC02362]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SATB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2120.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +15.7 | 0e+00 | 38/46 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +13.6 | 2e-39 | 26/35 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +10.0 | 2e-21 | 29/41 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +6.9 | 6e-10 | 31/48 (A498, LOX-IMVI, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.9 | 5e-07 | 26/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.32×** | +5.6 | 2e-06 | 23/48 (A549, A498, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.25×** | +4.8 | 1e-04 | 18/48 (A498, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.24×** | +4.5 | 4e-04 | 21/47 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.46×** | +4.3 | 0.001 | 16/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.003 | 16/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.008 | 12/48 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.008 | 16/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.010 | 12/48 (Panc 03.27, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.010 | 15/47 (A498, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.032 | 11/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.061 | 12/48 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.063 | 13/48 (HCT15, SNU-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.063 | 11/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.092 | 7/48 (NCI-H1573, SNU-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2120.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.514×** | -20.1 | 0e+00 | 44/47 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -13.6 | 1e-39 | 38/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -8.9 | 7e-17 | 36/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -8.0 | 2e-13 | 30/47 (Hs 766T, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.706×** | -7.4 | 1e-11 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -7.3 | 2e-11 | 28/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.712×** | -7.2 | 4e-11 | 29/48 (SK-MEL-2, KATO III, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.554×** | -6.6 | 3e-09 | 28/47 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.756×** | -6.0 | 1e-07 | 23/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.759×** | -5.9 | 2e-07 | 25/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.755×** | -5.8 | 4e-07 | 23/47 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.792×** | -5.0 | 3e-05 | 19/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.793×** | -4.7 | 1e-04 | 24/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.819×** | -4.0 | 0.002 | 21/48 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.833×** | -3.7 | 0.008 | 17/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.797×** | -3.5 | 0.018 | 12/48 (PANC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.868× | -2.9 | 0.095 | 11/48 (BT-474, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 75.7 | 2 (2 ⚠) | 11 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.80× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -17.8) |
| [[A-172 (line)]] | wt | 34.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -15.4) |
| [[HOP62 (line)]] | alt | 61.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -16.8) |
| [[MIA PaCa-2 (line)]] | alt | 42.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 31.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -19.4) |
| [[SNU-423 (line)]] | alt | 29.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.5) |
| [[SW480 (line)]] | alt | 38.7 | 0 | 4 | — | [[TAK-901 (drug)]] 5 µM 0.259× (z -9.2) |
| [[Hs 766T (line)]] | wt | 54.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.7) |
| [[KATO III (line)]] | alt | 42.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.426× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 32.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -8.6) |
| [[A-427 (line)]] | wt | 40.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +13.4) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.408× (z -9.3) |
| [[A498 (line)]] | wt | 38.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -13.5) |
| [[C32 (line)]] | wt | 22.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.6) |
| [[H4 (line)]] | wt | 37.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.79× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -16.6) |
| [[HEC-1-A (line)]] | alt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -9.9) |
| [[HS-578T (line)]] | alt | 40.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -19.6) |
| [[A549 (line)]] | wt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -15.2) |
| [[J82 (line)]] | alt | 58.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.3) |
| [[LoVo (line)]] | wt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -17.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 36.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -8.5) |
| [[SNU-1 (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -8.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 58.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -17.7) |
| [[SW48 (line)]] | wt | 28.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -10.8) |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFT1]] | +0.76 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[CAD]] | +0.75 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[MTG1]] | +0.74 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[QSOX2]] | +0.72 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[WDR5]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.66 | +0.51 / +0.78 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MRPS27]] | +0.65 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[CHID1]] | +0.65 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[PRPF19]] | +0.64 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[MRPL42]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4B]] | -0.63 | -0.49 / -0.55 | both halves | 1e-05 | same gene group |
| [[NPHS1]] | -0.62 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[LINC02362]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[SPATC1]] | -0.59 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SLU7]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[PLA2G12B]] | -0.58 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[KDM5B]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[BOLA1]] | -0.57 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[MSX1]] | -0.57 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[UBB]] | -0.57 | -0.45 / -0.53 | both halves | 3e-05 | pathway: Signaling by NOTCH |
| [[GPRC5C]] | -0.57 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[SATB1]] | -0.56 | -0.37 / -0.61 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SATB1]] | B | SATB1 activity lowers POFUT1's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.34× higher at baseline in the lines without SATB1 | 0.045 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[BMP2]] | B | BMP2 activity lowers POFUT1's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.35× higher at baseline in the lines without BMP2 | 0.070 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.8, -36.6); signed map (-8.1, -47.5). **Vector** length 86.1, 18.8% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.7 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.6 | +6.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.6 | +4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | -20.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -13.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | protein O-fucosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:32,207,855-32,238,658 (+) |
| Ensembl biotype | protein_coding |
| Also known as | O-FUT, O-Fuc-T, KIAA0180, FUT12 |
| Gene groups (HGNC) | Fucosyltransferases; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Pre-NOTCH Processing in the Endoplasmic Reticulum; Pre-NOTCH Expression and Processing; Signaling by NOTCH |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H488](https://www.uniprot.org/uniprotkb/Q9H488) (GDP-fucose protein O-fucosyltransferase 1):

> Catalyzes the reaction that attaches fucose through an O-glycosidic linkage to a conserved serine or threonine residue found in the consensus sequence C2-X(4,5)-[S/T]-C3 of EGF domains, where C2 and C3 are the second and third conserved cysteines. Specifically uses GDP-fucose as donor substrate and proper disulfide pairing of the substrate EGF domains is required for fucose transfer. Plays a crucial role in NOTCH signaling. Initial fucosylation of NOTCH by POFUT1 generates a substrate for …

**Summary**, from NCBI Gene [23509](https://www.ncbi.nlm.nih.gov/gene/23509):

> This gene encodes a member of the glycosyltransferase O-Fuc family. This enzyme adds O-fucose through an O-glycosidic linkage to conserved serine or threonine residues in the epidermal growth factor-like repeats of a number of cell surface and secreted proteins. O-fucose glycans are involved in ligand-induced receptor signaling. Alternative splicing of this gene results in two transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14988) · Entrez [23509](https://www.ncbi.nlm.nih.gov/gene/23509) · UniProt [Q9H488](https://www.uniprot.org/uniprotkb/Q9H488) · Ensembl [ENSG00000101346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101346)

## Data

Gene col 2120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2120); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2120]; `tensor/DDL_lfc|DDL_z.npy` [2120]; `embed/gene_vectors.npy` [2120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2120 or target_col == 2120). Every well: [[POFUT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POFUT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
