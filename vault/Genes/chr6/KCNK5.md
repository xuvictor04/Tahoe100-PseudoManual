---
symbol: "KCNK5"
type: "gene"
col: 8975
ensembl_id: "ENSG00000164626"
name: "potassium two pore domain channel subfamily K member 5"
location: "6p21.2"
module: 162
arm: "+"
pooled_cpm: 10.01
n_lines_expressing: 28
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 11
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# KCNK5

*potassium two pore domain channel subfamily K member 5* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.12× (z +13.4, q 6e-38, up in 13 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.690× (z -4.5, q 0.005, down in 12 of 23 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCL20]] (+0.53, fdr 1e-05), [[DGAT2]] (+0.53, fdr 3e-05), [[DUSP2]] (+0.51, fdr 2e-05); moves opposite to [[GPALPP1]] (-0.49, fdr 4e-05), [[ITCH]] (-0.48, fdr 4e-05), [[GLYR1]] (-0.43, fdr 1e-04).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2B]] → it (grade B ⚠); 11 go from it, the strongest it → [[TIPARP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +13.4 | 6e-38 | 13/22 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +11.4 | 8e-28 | 16/25 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +8.7 | 9e-16 | 12/25 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +7.2 | 1e-10 | 12/25 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +7.0 | 4e-10 | 12/24 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.71×** | +6.8 | 1e-09 | 10/25 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +6.2 | 4e-08 | 10/22 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +6.2 | 4e-08 | 7/19 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +5.9 | 2e-07 | 8/25 (KATO III, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +5.0 | 3e-05 | 9/24 (LoVo, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +4.7 | 1e-04 | 9/25 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +4.6 | 2e-04 | 3/16 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.44×** | +4.6 | 2e-04 | 9/25 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.43×** | +4.5 | 3e-04 | 7/25 (NCI-H2030, LoVo, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.42×** | +4.4 | 4e-04 | 5/23 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.033 | 4/25 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.033 | 2/25 (LoVo, SW1417) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.034 | 0/25 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Isocorydine (drug)]] 5 µM |  | 1.19× | +3.1 | 0.046 | 3/25 (Panc 03.27, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +2.9 | 0.091 | 4/25 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -4.5 | 0.005 | 12/23 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -4.0 | 0.015 | 13/25 (SW1417, MIA PaCa-2, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.730×** | -3.6 | 0.053 | 3/26 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.747×** | -3.5 | 0.061 | 3/25 (LoVo, COLO 205, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.758×** | -3.5 | 0.061 | 2/25 (Panc 03.27, NCI-H23) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.786× | -3.0 | 0.18 | 4/25 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 130 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0429× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0543× (z -21.7) |
| [[A498 (line)]] | wt | 3.90 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 10.8× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.380× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +14.3) | — |
| [[BT-474 (line)]] | alt | 8.00 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0612× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +13.6) | — |
| [[HT-29 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -9.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -10.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 17.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0718× (z -13.8) |
| [[SW48 (line)]] | wt | 8.44 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 5 µM 0.0420× (z -9.7) |
| [[A-172 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.851 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.785 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCL20]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[DGAT2]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[DUSP2]] | +0.51 | +0.47 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[TNFRSF1B]] | +0.50 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[EPHB3]] | +0.50 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TRIB1]] | +0.50 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[TRIM15]] | +0.48 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[KCNQ4]] | +0.48 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[DOC2B]] | +0.47 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[PLEKHO2]] | +0.47 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ADGRE5]] | +0.47 | +0.32 / +0.50 | both halves | 2e-04 |  |
| [[LRRC8B]] | +0.46 | +0.36 / +0.44 | both halves | 9e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPALPP1]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ITCH]] | -0.48 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[GLYR1]] | -0.43 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[SPAG16]] | -0.42 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[DNAJC13]] | -0.42 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[EIF3F]] | -0.42 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[SFTPA2]] | -0.42 | -0.41 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[DCDC1]] | -0.41 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[NDUFS1]] | -0.40 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[ATP6V1E1]] | -0.38 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[ANXA2R-OT1]] | -0.38 | -0.26 / -0.45 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2B]] | B | TOP2B activity raises KCNK5's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[HSPA2]] | B | HSPA2 activity lowers KCNK5's level | lines that do not express HSPA2 (12) vs lines expressing it (38) | 4.05× higher at baseline in the lines without HSPA2 | 0.077 | ⚠ within organs, on part of the lines; also absent: SGCE, MICU3, TUSC3; maybe low, not absent |
| [[SFTPA2]] | C | SFTPA2 activity raises KCNK5's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 2.91× lower at baseline in the lines without SFTPA2 | 0.010 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |
| [[EEPD1]] | C | EEPD1 activity raises KCNK5's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 3.66× lower at baseline in the lines without EEPD1 | 0.026 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent; co-absent with the target |
| [[MLXIPL]] | C | MLXIPL activity raises KCNK5's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 3.84× lower at baseline in the lines without MLXIPL | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIPARP]] | B | KCNK5 activity raises TIPARP's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without KCNK5 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |
| [[BIK]] | B | KCNK5 activity raises BIK's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 2.89× lower at baseline in the lines without KCNK5 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |
| [[SLC45A4]] | B | KCNK5 activity raises SLC45A4's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 2.82× lower at baseline in the lines without KCNK5 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |
| [[ARHGAP40]] | B | KCNK5 activity raises ARHGAP40's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 1.43× lower at baseline in the lines without KCNK5 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |
| [[KCNQ4]] | B | KCNK5 activity raises KCNQ4's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without KCNK5 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |
| [[EPHB3]] | B | KCNK5 activity raises EPHB3's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without KCNK5 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |
| [[SOX13]] | B | KCNK5 activity raises SOX13's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without KCNK5 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |
| [[EPPK1]] | C | KCNK5 activity raises EPPK1's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 3.15× lower at baseline in the lines without KCNK5 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2; co-absent with the target |
| [[MLXIPL]] | C | KCNK5 activity raises MLXIPL's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 3.09× lower at baseline in the lines without KCNK5 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2; co-absent with the target |
| [[IKZF3]] | C | KCNK5 activity raises IKZF3's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 2.64× lower at baseline in the lines without KCNK5 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2; co-absent with the target |
| [[SLC52A3]] | C | KCNK5 activity raises SLC52A3's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 3.17× lower at baseline in the lines without KCNK5 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2; co-absent with the target |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.3, 6.7); signed map (-0.9, 25.8). **Vector** length 62.0, 14.2% of its response variance represented; |z| ≥ 3 in 603 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +6.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.3 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +13.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +4.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | +0.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | potassium two pore domain channel subfamily K member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:39,188,971-39,229,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | K2p5.1, TASK-2, TASK2 |
| Gene groups (HGNC) | Potassium two pore domain channel subfamily K |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Phase 4 - resting membrane potential; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [O95279](https://www.uniprot.org/uniprotkb/O95279) (Potassium channel subfamily K member 5):

> K(+) channel that conducts voltage-dependent outward rectifying currents upon membrane depolarization. Voltage sensing is coupled to K(+) electrochemical gradient in an 'ion flux gating' mode where outward but not inward ion flow opens the gate. Homo- and heterodimerizes to form functional channels with distinct regulatory and gating properties.

**Summary**, from NCBI Gene [8645](https://www.ncbi.nlm.nih.gov/gene/8645):

> This gene encodes one of the members of the superfamily of potassium channel proteins containing two pore-forming P domains. The message for this gene is mainly expressed in the cortical distal tubules and collecting ducts of the kidney. The protein is highly sensitive to external pH and this, in combination with its expression pattern, suggests it may play an important role in renal potassium transport. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6280) · Entrez [8645](https://www.ncbi.nlm.nih.gov/gene/8645) · UniProt [O95279](https://www.uniprot.org/uniprotkb/O95279) · Ensembl [ENSG00000164626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164626)

## Data

Gene col 8975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8975); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8975]; `tensor/DDL_lfc|DDL_z.npy` [8975]; `embed/gene_vectors.npy` [8975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8975 or target_col == 8975). Every well: [[KCNK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
