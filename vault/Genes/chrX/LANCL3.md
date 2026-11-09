---
symbol: "LANCL3"
type: "gene"
col: 7140
ensembl_id: "ENSG00000147036"
name: "LanC like family member 3"
location: "Xp21.1"
module: 34
arm: "+"
pooled_cpm: 4.32
n_lines_expressing: 29
n_dd_up: 18
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 17
direction_downstream: 11
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# LANCL3

*LanC like family member 3* — Xp21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.20× (z +11.6, q 2e-28, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.04× (z +10.5, q 4e-23, up in 14 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.580× (z -8.0, q 9e-13, down in 17 of 22 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLNB]] (+0.68, fdr 1e-05), [[F3]] (+0.65, fdr 7e-06), [[PLEK2]] (+0.62, fdr 2e-05); moves opposite to [[GALNT7-DT]] (-0.58, fdr 3e-04), [[ATF5]] (-0.56, fdr 9e-05), [[FBXW4]] (-0.55, fdr 8e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[SERPINB5]] → it (grade B ⚠); 11 go from it, the strongest it → [[TINAGL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.20×** | +11.6 | 2e-28 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +10.5 | 4e-23 | 14/25 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +9.2 | 8e-18 | 1/8 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +7.6 | 5e-12 | 13/26 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +7.2 | 7e-11 | 15/26 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +6.6 | 4e-09 | 11/25 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +6.4 | 1e-08 | 9/21 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.81×** | +6.1 | 6e-08 | 0/14 | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +6.1 | 8e-08 | 4/16 (SW1417, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.45×** | +4.9 | 6e-05 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +4.6 | 2e-04 | 10/25 (SW1417, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.4 | 6e-04 | 7/22 (Panc 03.27, AsPC-1, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.77×** | +4.2 | 0.001 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.020 | 2/23 (NCI-H2030, NCI-H1792) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.4 | 0.022 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.090 | 1/15 (SW1417) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +3.0 | 0.099 | 5/22 (NCI-H460, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7140.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.580×** | -8.0 | 9e-13 | 17/22 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.555×** | -6.1 | 3e-07 | 16/26 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.567×** | -5.7 | 3e-06 | 13/25 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -5.2 | 3e-05 | 13/24 (J82, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -5.1 | 3e-05 | 12/21 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.615×** | -5.0 | 4e-05 | 6/26 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.626×** | -4.8 | 1e-04 | 7/25 (SNU-423, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.663×** | -4.3 | 0.001 | 11/22 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.715×** | -3.5 | 0.032 | 6/25 (SW48, H4, …) | inconsistent across doses |  |
| [[Cilostazol (drug)]] 5 µM |  | **0.708×** | -3.4 | 0.034 | 2/26 (SNU-423, NCI-H460) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.796×** | -3.3 | 0.045 | 2/25 (NCI-H2030, C32) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.728×** | -3.3 | 0.049 | 5/26 (AsPC-1, C32, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.714×** | -3.2 | 0.055 | 2/25 (AsPC-1, NCI-H2030) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.812×** | -3.0 | 0.096 | 9/24 (AsPC-1, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 25.0 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -22.2) |
| [[NCI-H1792 (line)]] | alt | 7.81 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0435× (z -13.1) |
| [[LS 180 (line)]] | wt | 29.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -20.5) |
| [[J82 (line)]] | alt | 11.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0531× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0998× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 6.64 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 23.5 | 0 | 2 (1 ⚠) | — | [[Alpelisib (drug)]] 5 µM 0.0209× (z -11.0) |
| [[H4 (line)]] | wt | 15.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -11.4) |
| [[Hs 766T (line)]] | wt | 4.84 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0381× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 2.48 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 8.24 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0550× (z -11.3) |
| [[A-172 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.548 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.895 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNB]] | +0.68 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[F3]] | +0.65 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.62 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[PRSS3]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[LYPD3]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[SERPINB5]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[MBOAT2]] | +0.60 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[FLNB-AS1]] | +0.58 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ATG16L1]] | +0.58 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[DGKD]] | +0.57 | +0.57 / +0.33 | both halves | 1e-04 |  |
| [[DENND2C]] | +0.57 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[IGSF9]] | +0.56 | +0.43 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT7-DT]] | -0.58 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[ATF5]] | -0.56 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[FBXW4]] | -0.55 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[RNF146]] | -0.54 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[TRAF3IP2-AS1]] | -0.54 | -0.40 / -0.26 | both halves | 3e-04 |  |
| [[N4BP2L2]] | -0.53 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[C1orf43]] | -0.53 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[DICER1-AS1]] | -0.52 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[MTUS1-DT]] | -0.52 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[DNAI4]] | -0.52 | -0.49 / -0.22 | both halves | 6e-04 |  |
| [[EPCAM-DT]] | -0.52 | -0.38 / -0.26 | both halves | 4e-04 |  |
| [[TSTD3]] | -0.51 | -0.44 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB5]] | B | SERPINB5 activity raises LANCL3's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.25× lower at baseline in the lines without SERPINB5 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[F3]] | B | F3 activity raises LANCL3's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.22× lower at baseline in the lines without F3 | 0.019 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[DHRS9]] | B | DHRS9 activity raises LANCL3's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.48× lower at baseline in the lines without DHRS9 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[FGFBP1]] | B | FGFBP1 activity raises LANCL3's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 2.32× lower at baseline in the lines without FGFBP1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[KLK10]] | B | KLK10 activity raises LANCL3's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.23× lower at baseline in the lines without KLK10 | 0.028 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[IL1R2]] | B | IL1R2 activity raises LANCL3's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 1.96× lower at baseline in the lines without IL1R2 | 0.034 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[LINC02725]] | B | LINC02725 activity raises LANCL3's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 1.80× lower at baseline in the lines without LINC02725 | 0.048 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425 |
| [[FA2H]] | B | FA2H activity raises LANCL3's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.73× lower at baseline in the lines without FA2H | 0.050 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[SCEL]] | B | SCEL activity raises LANCL3's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.78× lower at baseline in the lines without SCEL | 0.059 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[TINAGL1]] | B | TINAGL1 activity raises LANCL3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without TINAGL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[LINC02582]] | B | LINC02582 activity raises LANCL3's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.16× lower at baseline in the lines without LINC02582 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[KLK11]] | B | KLK11 activity raises LANCL3's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 2.48× lower at baseline in the lines without KLK11 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TINAGL1]] | B | LANCL3 activity raises TINAGL1's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 2.83× lower at baseline in the lines without LANCL3 | 0.011 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[KLK10]] | B | LANCL3 activity raises KLK10's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 2.60× lower at baseline in the lines without LANCL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[SERPINB5]] | B | LANCL3 activity raises SERPINB5's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 2.71× lower at baseline in the lines without LANCL3 | 0.025 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[TFAP2A-AS1]] | B | LANCL3 activity raises TFAP2A-AS1's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 1.29× lower at baseline in the lines without LANCL3 | 0.033 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[F3]] | B | LANCL3 activity raises F3's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 2.98× lower at baseline in the lines without LANCL3 | 0.040 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[PEAR1]] | B | LANCL3 activity raises PEAR1's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 1.64× lower at baseline in the lines without LANCL3 | 0.051 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[ITGA6]] | B | LANCL3 activity raises ITGA6's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 1.76× lower at baseline in the lines without LANCL3 | 0.054 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[GPRIN1]] | B | LANCL3 activity lowers GPRIN1's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 1.45× higher at baseline in the lines without LANCL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[LRRFIP1]] | B | LANCL3 activity raises LRRFIP1's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 1.40× lower at baseline in the lines without LANCL3 | 0.095 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[VSIR]] | B | LANCL3 activity raises VSIR's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 1.24× lower at baseline in the lines without LANCL3 | 0.097 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[PRSS3]] | C | LANCL3 activity raises PRSS3's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 2.62× lower at baseline in the lines without LANCL3 | 0.072 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.9, 6.3); signed map (-4.0, 44.2). **Vector** length 61.2, 13.8% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | +7.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.6 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -0.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +1.5 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | LanC like family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp21.1 — chrX:37,571,569-37,684,463 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ42925 |
| Gene groups (HGNC) | LanC like family |
| Matched by | ensembl_id |

UniProt [Q6ZV70](https://www.uniprot.org/uniprotkb/Q6ZV70) carries no function annotation.

**Summary**, from NCBI Gene [347404](https://www.ncbi.nlm.nih.gov/gene/347404):

> Predicted to be involved in carbohydrate metabolic process and peptide modification. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24767) · Entrez [347404](https://www.ncbi.nlm.nih.gov/gene/347404) · UniProt [Q6ZV70](https://www.uniprot.org/uniprotkb/Q6ZV70) · Ensembl [ENSG00000147036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147036)

## Data

Gene col 7140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7140); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7140]; `tensor/DDL_lfc|DDL_z.npy` [7140]; `embed/gene_vectors.npy` [7140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7140 or target_col == 7140). Every well: [[LANCL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LANCL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
