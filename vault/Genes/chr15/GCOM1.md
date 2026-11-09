---
symbol: "GCOM1"
type: "gene"
col: 6091
ensembl_id: "ENSG00000137878"
name: "GCOM1, MYZAP-POLR2M combined locus"
location: "15q21.3"
module: 57
arm: "+"
pooled_cpm: 22.85
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# GCOM1

*GCOM1, MYZAP-POLR2M combined locus* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.09× (z +13.3, q 1e-37, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.717× (z -8.5, q 8e-15, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLD]] (+0.65, fdr 1e-05), [[ENPP4]] (+0.61, fdr 3e-05), [[MAPRE3]] (+0.60, fdr 3e-05); moves opposite to [[RAB11FIP3]] (-0.56, fdr 2e-05), [[ZNF785]] (-0.55, fdr 5e-05), [[TRPV1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CDH17]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.09×** | +13.3 | 1e-37 | 41/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +9.6 | 3e-19 | 28/47 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +8.8 | 3e-16 | 29/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +7.3 | 3e-11 | 25/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +7.3 | 3e-11 | 26/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +7.2 | 4e-11 | 27/47 (A498, CFPAC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +7.2 | 4e-11 | 20/33 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +7.1 | 8e-11 | 25/47 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +7.0 | 1e-10 | 29/47 (A498, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +6.6 | 3e-09 | 24/48 (AsPC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +5.3 | 8e-06 | 19/47 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +5.1 | 1e-05 | 20/46 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +5.1 | 1e-05 | 19/48 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +4.4 | 4e-04 | 14/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 9e-04 | 16/47 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.004 | 16/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -8.5 | 8e-15 | 26/45 (COLO 205, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -4.7 | 7e-04 | 21/47 (LS 180, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -3.8 | 0.033 | 16/48 (Panc 03.27, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | 0.766× | -3.3 | 0.12 | 15/46 (NCI-H23, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.782× | -3.1 | 0.17 | 7/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tranilast (drug)]] 0.05 µM |  | 0.834× | -3.0 | 0.17 | 11/47 (hTERT-HPNE, SK-MEL-2, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 0.5 µM |  | 0.846× | -3.0 | 0.17 | 8/46 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.847× | -3.0 | 0.17 | 9/47 (HOP62, BT-474, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.848× | -3.0 | 0.17 | 12/47 (AN3 CA, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 21.2 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.183× (z -8.8) |
| [[A498 (line)]] | wt | 15.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.47× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 59.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 56.5 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0802× (z -13.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 91.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -15.8) |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.113× (z -9.4) |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.121× (z -10.8) |
| [[HT-29 (line)]] | alt | 75.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -15.0) |
| [[KATO III (line)]] | alt | 80.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -14.0) |
| [[LoVo (line)]] | wt | 35.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.4) |
| [[LS 180 (line)]] | wt | 46.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.67× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 19.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.77× (z +8.9) | — |
| [[RKO (line)]] | wt | 15.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 24.0× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.104× (z -9.3) |
| [[SW480 (line)]] | alt | 27.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +12.2) | — |
| [[A-172 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | +0.65 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ENPP4]] | +0.61 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[MAPRE3]] | +0.60 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[PLS1]] | +0.59 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[COMMD8]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[PLRG1]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CYP4F12]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PRELID3B]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CYB5R4]] | +0.55 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[MOCS2]] | +0.55 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[OAZ2]] | +0.55 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[GDE1]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB11FIP3]] | -0.56 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[ZNF785]] | -0.55 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[TRPV1]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[CDR2]] | -0.54 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ZNF131]] | -0.53 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[TOP3A]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[RBX1]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SYCE2]] | -0.52 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[ANXA2R-OT1]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[KCNJ14]] | -0.52 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[ING2-DT]] | -0.51 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[ENDOG]] | -0.51 | -0.36 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH17]] | B | CDH17 activity raises GCOM1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 2.55× lower at baseline in the lines without CDH17 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[SLC40A1]] | B | SLC40A1 activity raises GCOM1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without SLC40A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[TOP2A]] | B | TOP2A activity raises GCOM1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 0.8% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC03040]] | B | LINC03040 activity raises GCOM1's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without LINC03040 | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[CYP4F12]] | B | CYP4F12 activity raises GCOM1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 1.73× lower at baseline in the lines without CYP4F12 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[SLC5A1]] | B | SLC5A1 activity raises GCOM1's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 2.09× lower at baseline in the lines without SLC5A1 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[ANKRD22]] | B | ANKRD22 activity raises GCOM1's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 1.83× lower at baseline in the lines without ANKRD22 | 0.062 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[ANKEF1]] | B | ANKEF1 activity raises GCOM1's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without ANKEF1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[PCK1]] | B | PCK1 activity raises GCOM1's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 1.71× lower at baseline in the lines without PCK1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.2, 36.4); signed map (-3.4, 17.5). **Vector** length 82.4, 15.2% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.4 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.2 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +0.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | +1.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | GCOM1, MYZAP-POLR2M combined locus |
| Locus type | readthrough (other) |
| Location | 15q21.3 — chr15:57,591,908-57,714,745 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30973, GRINL1A, MYZAP-POLR2M |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [145781](https://www.ncbi.nlm.nih.gov/gene/145781):

> This locus represents naturally occurring readthrough transcription between the neighboring MYZAP (myocardial zonula adherens protein) and POLR2M (polymerase (RNA) II (DNA directed) polypeptide M) genes on chromosome 15. Alternative splicing results in multiple readthrough transcript variants. Readthrough variants may encode proteins that share sequence identity with the upstream gene product or with both the upstream and downstream gene products. Some readthrough transcript variants are also …

**Accessions** — [HGNC:26424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26424) · Entrez [145781](https://www.ncbi.nlm.nih.gov/gene/145781) · Ensembl [ENSG00000137878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137878)

## Data

Gene col 6091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6091); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6091]; `tensor/DDL_lfc|DDL_z.npy` [6091]; `embed/gene_vectors.npy` [6091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6091 or target_col == 6091). Every well: [[GCOM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCOM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
