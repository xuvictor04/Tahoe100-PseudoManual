---
symbol: "SCAT1"
type: "gene"
col: 15524
ensembl_id: "ENSG00000267123"
name: "S-phase cancer associated transcript 1"
location: "17q25.3"
module: 34
arm: "+"
pooled_cpm: 4.24
n_lines_expressing: 34
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 17
direction_downstream: 23
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SCAT1

*S-phase cancer associated transcript 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +9.2, q 3e-17, up in 7 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.516× (z -5.7, q 5e-06, down in 17 of 25 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Trametinib (drug)]] 5 µM: 0.617× (z -4.9, q 3e-04, down in 10 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH17]] (+0.70, fdr 7e-06, ⚠ same locus), [[PDE2A]] (+0.67, fdr 7e-06), [[VSIG1]] (+0.63, fdr 1e-05), [[IL19]] (+0.63, fdr 7e-06); moves opposite to [[AKAP7]] (-0.51, fdr 3e-05), [[EEF2K]] (-0.50, fdr 3e-05), [[CHPT1]] (-0.49, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[DNAH17]] → it (grade B ⚠); 23 go from it, the strongest it → [[SPTBN5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +9.2 | 3e-17 | 7/25 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +7.0 | 1e-09 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +6.6 | 9e-09 | 10/25 (HEC-1-A, H4, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.5 | 1e-08 | 2/23 (HEC-1-A, SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +5.5 | 5e-06 | 1/11 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.50×** | +5.1 | 4e-05 | 8/28 (NCI-H2030, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.6 | 4e-04 | 7/27 (SW480, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.002 | 4/25 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.54×** | +3.6 | 0.017 | 2/26 (NCI-H460, SW 900) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.4 | 0.035 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.46×** | +3.4 | 0.035 | 7/24 (COLO 205, HCT15, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.053 | 9/25 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.2 | 0.062 | 2/25 (NCI-H1792, NCI-H2030) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.90× | +3.0 | 0.11 | 6/19 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15524.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.516×** | -5.7 | 5e-06 | 17/25 (NCI-H460, CFPAC-1, …) | rises with dose | composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.617×** | -4.9 | 3e-04 | 10/29 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.589×** | -4.8 | 3e-04 | 14/27 (SW480, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.698×** | -4.6 | 6e-04 | 7/26 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -4.5 | 8e-04 | 15/28 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.638×** | -4.1 | 0.005 | 14/26 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.659×** | -3.8 | 0.013 | 16/27 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.467×** | -3.6 | 0.024 | 10/21 (HepG2/C3A, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.681×** | -3.5 | 0.032 | 13/28 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.692×** | -3.3 | 0.041 | 17/30 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.771×** | -3.3 | 0.041 | 6/29 (RPMI-7951, SNU-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.692×** | -3.3 | 0.041 | 8/28 (COLO 205, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.677×** | -3.3 | 0.048 | 6/28 (CFPAC-1, SNU-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.732×** | -3.2 | 0.058 | 10/29 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.707×** | -3.1 | 0.064 | 9/28 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.696×** | -3.1 | 0.065 | 12/25 (NCI-H1792, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.712×** | -3.1 | 0.066 | 6/28 (HepG2/C3A, NCI-H1573, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.747×** | -3.1 | 0.067 | 10/27 (LS 180, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.766×** | -3.0 | 0.084 | 9/27 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.143× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 7.52 | 0 | 3 (1 ⚠) | — | [[Trametinib (drug)]] 0.05 µM 0.120× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 3 (2 ⚠) | — | [[Clofarabine (drug)]] 0.05 µM 0.0699× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 5.03 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0590× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 8.10 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +13.8) | [[Harringtonine (drug)]] 5 µM 0.155× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 5.72 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.0707× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[HCT15 (line)]] | alt | 9.03 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0683× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0938× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 7.04 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0891× (z -9.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-172 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.977 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.739 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.940 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.768 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH17]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 | ⚠ same locus (27.8 kb, same strand: neighbours can correlate without regulation) |
| [[PDE2A]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[VSIG1]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[IL19]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[CFAP251]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[GPSM3]] | +0.60 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[LAT2]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ADAM8]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TNFRSF6B]] | +0.58 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[SPTBN5]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[LINC02725]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[MEI1]] | +0.56 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[BCAN-AS1]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP7]] | -0.51 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[EEF2K]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[CHPT1]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[GNAQ]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[PLBD1]] | -0.47 | -0.45 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAH17]] | B | DNAH17 activity raises SCAT1's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without DNAH17 | 0.004 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[TMEM154]] | B | TMEM154 activity raises SCAT1's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.76× lower at baseline in the lines without TMEM154 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[LYPD3]] | B | LYPD3 activity raises SCAT1's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.35× lower at baseline in the lines without LYPD3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[ADAM28]] | B | ADAM28 activity raises SCAT1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.74× lower at baseline in the lines without ADAM28 | 0.017 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[LINC00659]] | B | LINC00659 activity raises SCAT1's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 1.87× lower at baseline in the lines without LINC00659 | 0.028 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |
| [[GOLT1A]] | B | GOLT1A activity raises SCAT1's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.78× lower at baseline in the lines without GOLT1A | 0.055 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[TNFRSF6B]] | B | TNFRSF6B activity raises SCAT1's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 2.11× lower at baseline in the lines without TNFRSF6B | 0.058 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[WFDC3]] | B | WFDC3 activity raises SCAT1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without WFDC3 | 0.059 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[FAM110C]] | B | FAM110C activity raises SCAT1's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without FAM110C | 0.064 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[LINC01426]] | B | LINC01426 activity raises SCAT1's level | lines that do not express LINC01426 (22) vs lines expressing it (28) | 1.62× lower at baseline in the lines without LINC01426 | 0.065 | ⚠ within organs, on part of the lines; also absent: MIR3142HG, ADAMTS3, CTHRC1; maybe low, not absent |
| [[ITGA2]] | B | ITGA2 activity raises SCAT1's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.74× lower at baseline in the lines without ITGA2 | 0.073 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[FES]] | B | FES activity raises SCAT1's level | lines that do not express FES (11) vs lines expressing it (39) | 2.00× lower at baseline in the lines without FES | 0.076 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 22, C 1. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPTBN5]] | B | SCAT1 activity raises SPTBN5's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.45× lower at baseline in the lines without SCAT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[DNAH17]] | B | SCAT1 activity raises DNAH17's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without SCAT1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[LINC02320]] | B | SCAT1 activity raises LINC02320's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without SCAT1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[SSUH2]] | B | SCAT1 activity raises SSUH2's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without SCAT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[PLEK2]] | B | SCAT1 activity raises PLEK2's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 2.62× lower at baseline in the lines without SCAT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[CEMIP]] | B | SCAT1 activity raises CEMIP's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 3.43× lower at baseline in the lines without SCAT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[PDE2A]] | B | SCAT1 activity raises PDE2A's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.44× lower at baseline in the lines without SCAT1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[LINC02405]] | B | SCAT1 activity raises LINC02405's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 2.92× lower at baseline in the lines without SCAT1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[LYPD3]] | B | SCAT1 activity raises LYPD3's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without SCAT1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[EPHB6]] | B | SCAT1 activity raises EPHB6's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without SCAT1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[ADAM28]] | B | SCAT1 activity raises ADAM28's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 2.92× lower at baseline in the lines without SCAT1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[TLDC2]] | B | SCAT1 activity raises TLDC2's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.48× lower at baseline in the lines without SCAT1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.3, -2.5); signed map (10.2, 53.2). **Vector** length 65.6, 14.1% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.7 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -4.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | S-phase cancer associated transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q25.3 — chr17:78,605,233-78,632,155 (-) |
| Ensembl biotype | lncRNA |
| Also known as | CTD-2357A8.3, XLOC_012582; previously LINC02081 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52930](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52930) · Entrez [101928710](https://www.ncbi.nlm.nih.gov/gene/101928710) · Ensembl [ENSG00000267123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267123)

## Data

Gene col 15524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15524); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15524]; `tensor/DDL_lfc|DDL_z.npy` [15524]; `embed/gene_vectors.npy` [15524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15524 or target_col == 15524). Every well: [[SCAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
