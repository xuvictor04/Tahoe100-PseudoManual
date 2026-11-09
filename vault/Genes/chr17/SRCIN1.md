---
symbol: "SRCIN1"
type: "gene"
col: 15891
ensembl_id: "ENSG00000277363"
name: "SRC kinase signaling inhibitor 1"
location: "17q12"
module: 128
arm: "+"
pooled_cpm: 20.3
n_lines_expressing: 41
n_dd_up: 13
n_dd_down: 21
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# SRCIN1

*SRC kinase signaling inhibitor 1* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.82× (z +11.0, q 3e-25, up in 28 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.394× (z -11.9, q 4e-30, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBFA2T3]] (+0.64, fdr 7e-06), [[SLC6A11]] (+0.55, fdr 5e-04), [[KCNQ2]] (+0.53, fdr 2e-05); moves opposite to [[NUP133]] (-0.50, fdr 3e-05), [[OXNAD1]] (-0.46, fdr 5e-05), [[GPX8]] (-0.43, fdr 2e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 8 go from it, the strongest it → [[SSPOP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +11.0 | 3e-25 | 28/39 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.17×** | +9.8 | 4e-20 | 25/37 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.56×** | +5.8 | 2e-06 | 16/39 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.5 | 7e-06 | 15/39 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.36×** | +3.8 | 0.019 | 10/39 (BT-474, A498, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.6 | 0.027 | 10/31 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.031 | 8/38 (BT-474, NCI-H460, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.038 | 10/38 (NCI-H460, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.038 | 6/35 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.038 | 14/36 (NCI-H460, A498, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.4 | 0.038 | 6/39 (BT-474, H4, …) | all doses, stronger at high dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.038 | 5/38 (BT-474, SW 900, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +3.2 | 0.052 | 8/23 (LOX-IMVI, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.078 | 3/38 (BT-474, SW480, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.090 | 5/38 (A549, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.394×** | -11.9 | 4e-30 | 23/38 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.400×** | -11.7 | 2e-29 | 32/38 (BT-474, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.431×** | -10.8 | 6e-25 | 30/39 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.549×** | -7.2 | 1e-10 | 20/32 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.584×** | -6.9 | 7e-10 | 22/38 (BT-474, MIA PaCa-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.592×** | -6.7 | 2e-09 | 24/39 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.626×** | -6.0 | 2e-07 | 21/38 (BT-474, H4, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.415×** | -5.9 | 3e-07 | 20/35 (BT-474, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.456×** | -5.3 | 9e-06 | 21/38 (BT-474, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -5.1 | 2e-05 | 20/38 (BT-474, C-33 A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.688×** | -4.8 | 1e-04 | 16/39 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -4.4 | 5e-04 | 15/32 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.717×** | -4.2 | 0.001 | 14/36 (BT-474, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.794×** | -4.1 | 0.001 | 17/39 (SNU-1, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **0.727×** | -4.1 | 0.002 | 10/38 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.574×** | -3.7 | 0.007 | 13/36 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.021 | 7/39 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.705×** | -3.2 | 0.044 | 6/39 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.790×** | -3.0 | 0.076 | 11/38 (SHP-77, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 678 | 0 | 24 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0989× (z -19.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 47.3 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.150× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.167× (z -9.8) |
| [[KATO III (line)]] | alt | 9.68 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.144× (z -10.4) |
| [[A-427 (line)]] | wt | 21.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.142× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 9.09 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.36× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.147× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -9.1) |
| [[HS-578T (line)]] | alt | 5.24 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0874× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.229× (z -9.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 9.52 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0741× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 9.04 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -10.3) |
| [[HT-29 (line)]] | alt | 9.52 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.96× (z +9.3) | — |
| [[RKO (line)]] | wt | 8.84 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0698× (z -14.3) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.0330× (z -11.0) |
| [[SW480 (line)]] | alt | 9.09 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.203× (z -9.7) |
| [[A498 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T3]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[SLC6A11]] | +0.55 | +0.70 / +0.24 | both halves | 5e-04 |  |
| [[KCNQ2]] | +0.53 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[ELFN1]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ZSWIM4]] | +0.52 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[ZBTB46]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[CHD5]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[FSD1]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[CELF2]] | +0.50 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[PTCHD1]] | +0.50 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[LINC01440]] | +0.50 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[NFATC1]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP133]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[OXNAD1]] | -0.46 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[GPX8]] | -0.43 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[TCTN3]] | -0.43 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises SRCIN1's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.19× lower at baseline in the lines without MSI1 | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[SSPOP]] | B | SSPOP activity raises SRCIN1's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 2.17× lower at baseline in the lines without SSPOP | 0.056 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[RASGEF1A]] | B | RASGEF1A activity raises SRCIN1's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 2.00× lower at baseline in the lines without RASGEF1A | 0.080 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[KIF1A]] | B | KIF1A activity raises SRCIN1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.31× lower at baseline in the lines without KIF1A | 0.086 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[KCNQ2]] | B | KCNQ2 activity raises SRCIN1's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without KCNQ2 | 0.091 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSPOP]] | B | SRCIN1 activity raises SSPOP's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 2.07× lower at baseline in the lines without SRCIN1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[EPOP]] | B | SRCIN1 activity raises EPOP's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 1.98× lower at baseline in the lines without SRCIN1 | 0.038 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[PAQR6]] | B | SRCIN1 activity raises PAQR6's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 1.56× lower at baseline in the lines without SRCIN1 | 0.048 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[ZFHX2]] | B | SRCIN1 activity raises ZFHX2's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 2.17× lower at baseline in the lines without SRCIN1 | 0.058 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[MMP25-AS1]] | B | SRCIN1 activity raises MMP25-AS1's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 1.39× lower at baseline in the lines without SRCIN1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[ABCA3]] | B | SRCIN1 activity raises ABCA3's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 2.35× lower at baseline in the lines without SRCIN1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[TCTN3]] | B | SRCIN1 activity raises TCTN3's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without SRCIN1 | 0.094 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[GABBR1]] | B | SRCIN1 activity raises GABBR1's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without SRCIN1 | 0.097 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.3, 37.2); signed map (25.2, 23.5). **Vector** length 84.9, 18.2% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | +2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.9 | +0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.3 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -11.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.5 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -11.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.6 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | SRC kinase signaling inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,530,031-38,605,952 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SNIP, p140Cap, KIAA1684 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0H9](https://www.uniprot.org/uniprotkb/Q9C0H9) (SRC kinase signaling inhibitor 1):

> Acts as a negative regulator of SRC by activating CSK which inhibits SRC activity and downstream signaling, leading to impaired cell spreading and migration. Regulates dendritic spine morphology. Involved in calcium-dependent exocytosis. May play a role in neurotransmitter release or synapse maintenance.

**Summary**, from NCBI Gene [80725](https://www.ncbi.nlm.nih.gov/gene/80725):

> Enables protein kinase binding activity. Involved in several processes, including postsynaptic actin cytoskeleton organization; regulation of protein tyrosine kinase activity; and substrate adhesion-dependent cell spreading. Located in actin cytoskeleton and cytoplasm. Is active in glutamatergic synapse. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29506) · Entrez [80725](https://www.ncbi.nlm.nih.gov/gene/80725) · UniProt [Q9C0H9](https://www.uniprot.org/uniprotkb/Q9C0H9) · Ensembl [ENSG00000277363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277363)

## Data

Gene col 15891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15891); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15891]; `tensor/DDL_lfc|DDL_z.npy` [15891]; `embed/gene_vectors.npy` [15891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15891 or target_col == 15891). Every well: [[SRCIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRCIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
