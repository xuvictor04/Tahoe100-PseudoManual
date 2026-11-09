---
symbol: "DEF6"
type: "gene"
col: 352
ensembl_id: "ENSG00000023892"
name: "DEF6 guanine nucleotide exchange factor"
location: "6p21.31"
module: 31
arm: "+"
pooled_cpm: 6.95
n_lines_expressing: 45
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# DEF6

*DEF6 guanine nucleotide exchange factor* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.90× (z +8.9, q 3e-16, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 1.43× (z +4.8, q 5e-04, up in 10 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.405× (z -13.0, q 4e-36, down in 34 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LPAR5]] (+0.60, fdr 1e-05), [[TLDC2]] (+0.60, fdr 1e-05), [[INAVA]] (+0.56, fdr 2e-05); moves opposite to [[LRP11]] (-0.48, fdr 3e-05), [[DPYD]] (-0.45, fdr 7e-05), [[DCLK2]] (-0.43, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ANO1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +8.9 | 3e-16 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.8 | 5e-04 | 10/31 (NCI-H2347, LS 180, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.4 | 0.002 | 3/13 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.1 | 0.007 | 2/21 (LS 180, SNU-423) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.20×** | +3.8 | 0.018 | 8/39 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.023 | 3/30 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.6 | 0.023 | 2/24 (LS 180, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 1.24× | +3.1 | 0.14 | 2/41 (PANC-1, NCI-H460) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.405×** | -13.0 | 4e-36 | 34/41 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.431×** | -12.1 | 2e-31 | 27/33 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.451×** | -11.5 | 2e-28 | 26/38 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.537×** | -9.0 | 4e-17 | 24/37 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.717×** | -6.8 | 1e-09 | 19/33 (MIA PaCa-2, CFPAC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -6.3 | 2e-08 | 16/34 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.644×** | -6.1 | 8e-08 | 17/36 (Panc 03.27, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.450×** | -6.0 | 1e-07 | 19/34 (KATO III, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.471×** | -5.7 | 8e-07 | 14/34 (Panc 03.27, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -5.3 | 7e-06 | 17/38 (NCI-H2030, HOP62, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.702×** | -5.1 | 2e-05 | 16/39 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.716×** | -4.8 | 6e-05 | 14/37 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -4.8 | 7e-05 | 12/39 (hTERT-HPNE, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.733×** | -4.5 | 3e-04 | 12/40 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.729×** | -4.3 | 6e-04 | 11/36 (SHP-77, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.794×** | -3.1 | 0.061 | 4/40 (HOP62, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 11.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 10.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0807× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[Hs 766T (line)]] | wt | 7.66 | 0 | 2 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.109× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 32.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -21.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 5.10 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 9.31 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0610× (z -10.6) |
| [[LoVo (line)]] | wt | 8.47 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.241× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 5.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 4.10 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0652× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0443× (z -8.7) |
| [[SW48 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -9.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 13.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.268× (z -10.8) |
| [[A-172 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPAR5]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TLDC2]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[INAVA]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[TMCC3]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[LASTR]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ARHGAP27]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 | same gene group; pathway: CDC42 GTPase cycle |
| [[FBLIM1]] | +0.51 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[GNA15]] | +0.51 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[NECTIN4]] | +0.51 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ARHGAP30]] | +0.51 | +0.42 / +0.46 | both halves | 4e-05 | pathway: CDC42 GTPase cycle |
| [[NET1]] | +0.51 | +0.54 / +0.42 | both halves | 4e-05 | same gene group; pathway: RHOA GTPase cycle |
| [[IL17RE]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP11]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[DPYD]] | -0.45 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[DCLK2]] | -0.43 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[SLC39A8]] | -0.42 | -0.32 / -0.40 | both halves | 1e-04 |  |
| [[SLC22A23]] | -0.41 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[PRKN]] | -0.41 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[USP25]] | -0.41 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[CUX1]] | -0.40 | -0.38 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO1]] | B | ANO1 activity raises DEF6's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.53× lower at baseline in the lines without ANO1 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[SEMA3B]] | B | SEMA3B activity raises DEF6's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.66× lower at baseline in the lines without SEMA3B | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[BLACAT1]] | B | BLACAT1 activity raises DEF6's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without BLACAT1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[LCK]] | B | LCK activity raises DEF6's level | lines that do not express LCK (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without LCK | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[LEMD1]] | B | LEMD1 activity raises DEF6's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without LEMD1 | 0.031 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[TTC22]] | B | TTC22 activity raises DEF6's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.46× lower at baseline in the lines without TTC22 | 0.058 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[PTK6]] | B | PTK6 activity raises DEF6's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 2.13× lower at baseline in the lines without PTK6 | 0.060 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[LCK]] | B | LCK activity strengthens DEF6's drug response | lines that do not express LCK (25) vs lines expressing it (16) | the lines without LCK respond 0.68× as strongly (z diff +1.31); strongest at Homoharringtonine 5 µM: 0.60x vs 0.51x (z diff +2.5) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CDH1]] | B | CDH1 activity raises DEF6's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without CDH1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[SYTL1]] | B | SYTL1 activity raises DEF6's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 2.07× lower at baseline in the lines without SYTL1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[WNT7A]] | B | WNT7A activity raises DEF6's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without WNT7A | 0.087 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.505). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 58.3); signed map (58.2, 11.7). **Vector** length 51.4, 6.78% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +2.3 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | -0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | -0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -11.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -13.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.7 | -4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.6 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.0 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | DEF6 guanine nucleotide exchange factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:35,297,818-35,321,771 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IBP, SLAT, SWAP70L |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Hallmark sets | P53_PATHWAY |
| Reactome | 7 pathways, smallest: RAC2 GTPase cycle; RHOA GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4E7](https://www.uniprot.org/uniprotkb/Q9H4E7) (Differentially expressed in FDCP 6 homolog):

> Phosphatidylinositol 3,4,5-trisphosphate-dependent guanine nucleotide exchange factor (GEF) which plays a role in the activation of Rho GTPases RAC1, RhoA and CDC42. Can regulate cell morphology in cooperation with activated RAC1 (By similarity). Involved in immune homeostasis by ensuring proper trafficking and availability of T-cell regulator CTLA-4 at T-cell surface. Plays a role in Th2 (T helper cells) development and/or activation, perhaps by interfering with ZAP70 signaling (By similarity).

**Summary**, from NCBI Gene [50619](https://www.ncbi.nlm.nih.gov/gene/50619):

> DEF6, or IBP, is a guanine nucleotide exchange factor (GEF) for RAC (MIM 602048) and CDC42 (MIM 116952) that is highly expressed in B and T cells (Gupta et al., 2003 [PubMed 12923183]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:2760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2760) · Entrez [50619](https://www.ncbi.nlm.nih.gov/gene/50619) · UniProt [Q9H4E7](https://www.uniprot.org/uniprotkb/Q9H4E7) · Ensembl [ENSG00000023892](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023892)

## Data

Gene col 352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 352); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 352]; `tensor/DDL_lfc|DDL_z.npy` [352]; `embed/gene_vectors.npy` [352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 352 or target_col == 352). Every well: [[DEF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
