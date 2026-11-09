---
symbol: "HNMT"
type: "gene"
col: 7442
ensembl_id: "ENSG00000150540"
name: "histamine N-methyltransferase"
location: "2q22.1"
module: 8
arm: "+"
pooled_cpm: 11.86
n_lines_expressing: 33
n_dd_up: 12
n_dd_down: 45
n_dd_up_clean: 10
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 13
direction_downstream: 15
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# HNMT

*histamine N-methyltransferase* — 2q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.83× (z +7.9, q 2e-12, up in 24 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.225× (z -19.3, q 0e+00, down in 29 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARSL]] (+0.61, fdr 1e-05), [[HOXA3]] (+0.59, fdr 1e-05), [[MGST2]] (+0.57, fdr 1e-05); moves opposite to [[MPP3]] (-0.57, fdr 1e-05), [[PLSCR3]] (-0.56, fdr 3e-05), [[SFN]] (-0.55, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SLC40A1]] → it (grade B ⚠); 15 go from it, the strongest it → [[LNX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.83×** | +7.9 | 2e-12 | 24/30 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **2.53×** | +6.3 | 8e-08 | 17/27 (LS 180, AsPC-1, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.9 | 7e-07 | 17/27 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.50×** | +5.3 | 2e-05 | 12/30 (A-172, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +5.3 | 2e-05 | 14/29 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.9 | 7e-05 | 14/30 (COLO 205, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.5 | 4e-04 | 8/16 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib (drug)]] 5 µM |  | **1.75×** | +3.8 | 0.010 | 6/28 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.012 | 10/29 (LS 180, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.026 | 6/30 (HepG2/C3A, Panc 03.27, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.029 | 7/28 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.069 | 7/31 (SW480, A-172, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.085 | 5/29 (LS 180, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7442.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.225×** | -19.3 | 0e+00 | 29/30 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.240×** | -18.5 | 0e+00 | 30/30 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.317×** | -14.9 | 0e+00 | 27/30 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.530×** | -11.6 | 5e-29 | 22/28 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.413×** | -11.4 | 3e-28 | 26/30 (HepG2/C3A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -10.4 | 2e-23 | 23/29 (HepG2/C3A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.458×** | -10.1 | 5e-22 | 23/30 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.477×** | -9.6 | 7e-20 | 20/30 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.492×** | -9.2 | 3e-18 | 24/30 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.530×** | -7.7 | 5e-13 | 20/29 (COLO 205, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -7.7 | 6e-13 | 17/26 (COLO 205, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.582×** | -7.0 | 1e-10 | 16/29 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.605×** | -6.5 | 4e-09 | 19/30 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.713×** | -6.2 | 3e-08 | 19/30 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.616×** | -6.0 | 7e-08 | 19/30 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.626×** | -5.8 | 2e-07 | 15/29 (COLO 205, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 40.6 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0636× (z -22.1) |
| [[HepG2_C3A (line)]] | wt | 136 | 0 | 9 | — | [[Panobinostat (drug)]] 0.5 µM 0.0665× (z -18.4) |
| [[Panc 03.27 (line)]] | alt | 36.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -16.8) |
| [[A498 (line)]] | wt | 23.1 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 27.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0809× (z -13.6) |
| [[KATO III (line)]] | alt | 11.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0628× (z -13.8) |
| [[LS 180 (line)]] | wt | 26.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -13.8) |
| [[PANC-1 (line)]] | alt | 5.92 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.1) |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -11.8) |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 22.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -10.4) |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -10.6) |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -8.5) |
| [[H4 (line)]] | wt | 13.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0908× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 6.97 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0368× (z -12.6) |
| [[A-172 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.898 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARSL]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 | STRING 431 |
| [[HOXA3]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MGST2]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SLC2A12]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[RAMP1]] | +0.57 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[FMO5]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[P4HTM]] | +0.55 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[MANSC1]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[HNF1A-AS1]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[DEPTOR]] | +0.52 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[DLEU1]] | +0.52 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[ABCC6]] | +0.51 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP3]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PLSCR3]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SFN]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NLN]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ZBED4]] | -0.53 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[ELOVL1]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PPP2R2C]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[LRRFIP1]] | -0.50 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[MAP4]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[PARVB]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ADCY7]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ABCC10]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC40A1]] | B | SLC40A1 activity raises HNMT's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without SLC40A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[AGR3]] | B | AGR3 activity raises HNMT's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 2.63× lower at baseline in the lines without AGR3 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[TCN1]] | B | TCN1 activity raises HNMT's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.81× lower at baseline in the lines without TCN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[LNX1]] | B | LNX1 activity raises HNMT's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.36× lower at baseline in the lines without LNX1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[FRK]] | B | FRK activity raises HNMT's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.30× lower at baseline in the lines without FRK | 0.021 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[BCAS1]] | B | BCAS1 activity raises HNMT's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.12× lower at baseline in the lines without BCAS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[SLC16A4]] | B | SLC16A4 activity raises HNMT's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without SLC16A4 | 0.050 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[CRYZL2P]] | B | CRYZL2P activity raises HNMT's level | lines that do not express CRYZL2P (14) vs lines expressing it (36) | 2.34× lower at baseline in the lines without CRYZL2P | 0.065 | ⚠ within organs, on part of the lines; also absent: SEC16B |
| [[TMPRSS3]] | B | TMPRSS3 activity raises HNMT's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.03× lower at baseline in the lines without TMPRSS3 | 0.078 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[SEC16B]] | B | SEC16B activity raises HNMT's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.58× lower at baseline in the lines without SEC16B | 0.088 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[GABRP]] | B | GABRP activity raises HNMT's level | lines that do not express GABRP (44) vs lines expressing it (6) | 2.70× lower at baseline in the lines without GABRP | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[RNF128]] | B | RNF128 activity raises HNMT's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without RNF128 | 0.096 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LNX1]] | B | HNMT activity raises LNX1's level | lines that do not express HNMT (17) vs lines expressing it (33) | 2.81× lower at baseline in the lines without HNMT | 0.022 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[BMF]] | B | HNMT activity raises BMF's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without HNMT | 0.023 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[MGST2]] | B | HNMT activity raises MGST2's level | lines that do not express HNMT (17) vs lines expressing it (33) | 2.07× lower at baseline in the lines without HNMT | 0.028 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[FRK]] | B | HNMT activity raises FRK's level | lines that do not express HNMT (17) vs lines expressing it (33) | 2.63× lower at baseline in the lines without HNMT | 0.032 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[USP54]] | B | HNMT activity raises USP54's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.45× lower at baseline in the lines without HNMT | 0.042 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[ABCC10]] | B | HNMT activity lowers ABCC10's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.42× higher at baseline in the lines without HNMT | 0.055 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[SLC40A1]] | B | HNMT activity raises SLC40A1's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.98× lower at baseline in the lines without HNMT | 0.059 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[TSPAN8]] | B | HNMT activity raises TSPAN8's level | lines that do not express HNMT (17) vs lines expressing it (33) | 2.17× lower at baseline in the lines without HNMT | 0.059 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[TMPRSS3]] | B | HNMT activity raises TMPRSS3's level | lines that do not express HNMT (17) vs lines expressing it (33) | 2.23× lower at baseline in the lines without HNMT | 0.060 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[MINDY1]] | B | HNMT activity raises MINDY1's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without HNMT | 0.078 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[SLC2A12]] | B | HNMT activity raises SLC2A12's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without HNMT | 0.089 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[YWHAEP7-1]] | B | HNMT activity raises YWHAEP7-1's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.36× lower at baseline in the lines without HNMT | 0.090 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.430). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.6, 50.4); signed map (64.7, -1.5). **Vector** length 82.1, 20.9% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +7.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -10.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -6.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | histamine N-methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q22.1 — chr2:137,964,020-138,016,364 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HMT |
| Gene groups (HGNC) | 7BS small molecule methyltransferases; Small molecule methyltransferases |
| Reactome | 4 pathways, smallest: Histidine catabolism; Metabolism of ingested SeMet, Sec, MeSec into H2Se; Selenoamino acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P50135](https://www.uniprot.org/uniprotkb/P50135) (Histamine N-methyltransferase):

> Inactivates histamine by N-methylation. Plays an important role in degrading histamine and in regulating the airway response to histamine.

**Summary**, from NCBI Gene [3176](https://www.ncbi.nlm.nih.gov/gene/3176):

> In mammals, histamine is metabolized by two major pathways: N(tau)-methylation via histamine N-methyltransferase and oxidative deamination via diamine oxidase. This gene encodes the first enzyme which is found in the cytosol and uses S-adenosyl-L-methionine as the methyl donor. In the mammalian brain, the neurotransmitter activity of histamine is controlled by N(tau)-methylation as diamine oxidase is not found in the central nervous system. A common genetic polymorphism affects the activity …

**Accessions** — [HGNC:5028](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5028) · Entrez [3176](https://www.ncbi.nlm.nih.gov/gene/3176) · UniProt [P50135](https://www.uniprot.org/uniprotkb/P50135) · Ensembl [ENSG00000150540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150540)

## Data

Gene col 7442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7442); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7442]; `tensor/DDL_lfc|DDL_z.npy` [7442]; `embed/gene_vectors.npy` [7442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7442 or target_col == 7442). Every well: [[HNMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
