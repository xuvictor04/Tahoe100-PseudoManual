---
symbol: "PANX2"
type: "gene"
col: 1044
ensembl_id: "ENSG00000073150"
name: "pannexin 2"
location: "22q13.33"
module: 145
arm: "+"
pooled_cpm: 4.97
n_lines_expressing: 41
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# PANX2

*pannexin 2* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +6.2, q 4e-07, up in 10 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.76× (z +5.6, q 6e-06, up in 16 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.413× (z -12.3, q 4e-32, down in 26 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRELD1]] (+0.65, fdr 7e-06), [[PHF1]] (+0.63, fdr 7e-06), [[ULK1]] (+0.63, fdr 1e-05); moves opposite to [[ATIC]] (-0.55, fdr 1e-05), [[SRFBP1]] (-0.55, fdr 3e-05), [[UTP15]] (-0.54, fdr 3e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ERFL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.2 | 4e-07 | 10/18 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +5.6 | 6e-06 | 16/31 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +4.7 | 5e-04 | 6/12 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.91×** | +4.6 | 7e-04 | 6/28 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **1.55×** | +4.3 | 0.002 | 12/33 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.84×** | +4.3 | 0.002 | 6/32 (MIA PaCa-2, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +4.2 | 0.002 | 5/10 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.80×** | +4.2 | 0.002 | 14/32 (A498, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.77×** | +4.0 | 0.004 | 8/22 (A-427, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +4.0 | 0.004 | 8/24 (NCI-H2347, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.005 | 7/30 (HT-29, HCT15, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.63×** | +3.5 | 0.026 | 4/33 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.4 | 0.034 | 2/29 (SNU-423, A549) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.045 | 6/28 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.067 | 5/34 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.413×** | -12.3 | 4e-32 | 26/30 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.300×** | -11.4 | 1e-27 | 25/33 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.351×** | -10.3 | 9e-23 | 26/31 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.419×** | -8.6 | 1e-15 | 27/37 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.425×** | -8.4 | 4e-15 | 30/36 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.500×** | -6.8 | 8e-10 | 22/35 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.528×** | -6.3 | 2e-08 | 17/36 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.546×** | -6.0 | 2e-07 | 18/36 (HEC-1-A, A-427, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.533×** | -6.0 | 2e-07 | 16/28 (HCT15, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.553×** | -5.8 | 3e-07 | 16/36 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.681×** | -5.3 | 5e-06 | 14/32 (HCT15, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.586×** | -5.3 | 7e-06 | 20/37 (HT-29, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.654×** | -4.2 | 0.001 | 14/30 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.420×** | -4.0 | 0.002 | 11/31 (HT-29, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.671×** | -3.9 | 0.003 | 15/35 (HT-29, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.675×** | -3.9 | 0.004 | 13/34 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.468×** | -3.5 | 0.015 | 8/33 (HS-578T, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -3.3 | 0.029 | 9/33 (HCT15, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.729×** | -3.1 | 0.054 | 1/36 (HEC-1-A) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.722×** | -3.1 | 0.055 | 13/30 (A498, Panc 03.27, …) | top dose only |  |
| [[venetoclax (drug)]] 0.5 µM |  | **0.647×** | -3.1 | 0.056 | 2/37 (HEC-1-A, NCI-H2347) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.60 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0463× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 4.43 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -10.2) |
| [[HCT15 (line)]] | alt | 7.51 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0469× (z -9.1) |
| [[HT-29 (line)]] | alt | 3.68 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0605× (z -9.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.144× (z -9.2) |
| [[LoVo (line)]] | wt | 5.45 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0167× (z -17.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 8.21 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0559× (z -21.7) |
| [[A-427 (line)]] | wt | 6.25 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.120× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 1.97 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 7.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -15.4) |
| [[H4 (line)]] | wt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -8.6) |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -12.4) |
| [[J82 (line)]] | alt | 4.86 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0770× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 5.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0361× (z -16.4) |
| [[SW 900 (line)]] | alt | 5.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -10.5) |
| [[A-172 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.989 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRELD1]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PHF1]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ULK1]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[DEDD2]] | +0.62 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[MXD4]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PTOV1]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[BSDC1]] | +0.61 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SARAF]] | +0.60 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MARK4]] | +0.59 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[L3MBTL1]] | +0.58 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[SEMA6C]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[SRFBP1]] | -0.55 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[UTP15]] | -0.54 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TRMT5]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[SF3B3]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[NOC3L]] | -0.52 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TMA16]] | -0.51 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[FARSB]] | -0.51 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[GUF1]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[RUVBL1]] | -0.51 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[NOP14]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[MCCC2]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERFL]] | B | PANX2 activity raises ERFL's level | lines that do not express PANX2 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without PANX2 | 0.078 | ⚠ within organs, on part of the lines; also absent: APBA2, CABYR; maybe low, not absent |

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.9, -41.9); signed map (-22.8, 10.9). **Vector** length 47.1, 7.15% of its response variance represented; |z| ≥ 3 in 735 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.7 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +4.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +4.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -6.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -11.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -10.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | pannexin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,170,731-50,180,295 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hPANX2, PX2 |
| Gene groups (HGNC) | Pannexins |
| Reactome | 3 pathways, smallest: Electric Transmission Across Gap Junctions; Transmission across Electrical Synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RD6](https://www.uniprot.org/uniprotkb/Q96RD6) (Pannexin-2):

> Ion channel with a slight anion preference. Also able to release ATP. Plays a role in regulating neurogenesis and apoptosis in keratinocytes (By similarity).

**Summary**, from NCBI Gene [56666](https://www.ncbi.nlm.nih.gov/gene/56666):

> The protein encoded by this gene belongs to the innexin family. Innexin family members are the structural components of gap junctions. This protein and pannexin 1 are abundantly expressed in central nervous system (CNS) and are coexpressed in various neuronal populations. Studies in Xenopus oocytes suggest that this protein alone and in combination with pannexin 1 may form cell type-specific gap junctions with distinct properties. Multiple transcript variants encoding different isoforms have …

**Accessions** — [HGNC:8600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8600) · Entrez [56666](https://www.ncbi.nlm.nih.gov/gene/56666) · UniProt [Q96RD6](https://www.uniprot.org/uniprotkb/Q96RD6) · Ensembl [ENSG00000073150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073150)

## Data

Gene col 1044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1044); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1044]; `tensor/DDL_lfc|DDL_z.npy` [1044]; `embed/gene_vectors.npy` [1044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1044 or target_col == 1044). Every well: [[PANX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PANX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
