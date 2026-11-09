---
symbol: "SHANK1"
type: "gene"
col: 8449
ensembl_id: "ENSG00000161681"
name: "SH3 and multiple ankyrin repeat domains 1"
location: "19q13.33"
module: 13
arm: "+"
pooled_cpm: 15.72
n_lines_expressing: 28
n_dd_up: 7
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 26
direction_downstream: 13
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SHANK1

*SH3 and multiple ankyrin repeat domains 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.20× (z +7.0, q 2e-09, up in 12 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.481× (z -6.4, q 8e-08, down in 14 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD3]] (+0.78, fdr 7e-06), [[RFX8]] (+0.76, fdr 7e-06), [[ARHGAP22]] (+0.74, fdr 7e-06); moves opposite to [[TNS3]] (-0.52, fdr 2e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[TNS3]] → it (grade B ⚠); 13 go from it, the strongest it → [[PGF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +7.0 | 2e-09 | 12/23 (SW480, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +6.7 | 7e-09 | 1/9 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +5.3 | 2e-05 | 11/24 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +5.3 | 2e-05 | 9/24 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.22×** | +5.0 | 5e-05 | 10/20 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.5 | 8e-04 | 5/22 (A549, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +3.5 | 0.045 | 1/16 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.65× | +3.2 | 0.11 | 3/24 (RKO, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.5 µM |  | 1.42× | +3.1 | 0.13 | 6/22 (A-172, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, none with an alert; shown: the 15 strongest. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8449.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.481×** | -6.4 | 8e-08 | 14/25 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.536×** | -5.5 | 9e-06 | 17/25 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.529×** | -5.4 | 9e-06 | 14/24 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.518×** | -5.4 | 9e-06 | 12/25 (RKO, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.559×** | -5.2 | 3e-05 | 14/25 (RKO, CFPAC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.562×** | -5.1 | 3e-05 | 13/24 (HOP62, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.626×** | -4.2 | 0.002 | 8/25 (NCI-H23, H4, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -3.9 | 0.008 | 11/22 (H4, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.657×** | -3.6 | 0.018 | 14/26 (RKO, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.658×** | -3.6 | 0.019 | 14/25 (RKO, LOX-IMVI, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.717×** | -3.5 | 0.021 | 11/26 (RKO, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.748×** | -3.5 | 0.022 | 13/25 (RKO, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.760×** | -3.4 | 0.027 | 10/25 (RKO, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.684×** | -3.4 | 0.029 | 10/25 (HOP62, H4, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.436×** | -3.3 | 0.036 | 10/25 (RKO, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 335 | 0 | 20 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.195× (z -17.4) |
| [[H4 (line)]] | wt | 60.8 | 0 | 10 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0135× (z -17.1) |
| [[HOP62 (line)]] | alt | 28.3 | 0 | 10 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.413× (z -15.6) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 121 | 0 | 6 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.258× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 68.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.8) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 23.5 | 0 | 2 | — | [[Belumosudil (drug)]] 5 µM 0.122× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0887× (z -10.6) ⚠ toxic · without an alert: [[Cobimetinib (drug)]] 5 µM 0.130× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -9.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.160× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0568× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 5.89 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.09× (z +8.8) | — |
| [[A-172 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD3]] | +0.78 | +0.66 / +0.75 | both halves | 7e-06 | same gene group |
| [[RFX8]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP22]] | +0.74 | +0.75 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[GPR68]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SPOCD1]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[NLRP3]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS18]] | +0.69 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[PAEP]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[COL6A2]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[CORO2B]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[VEPH1]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[BCL2A1]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS3]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 14, C 12. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS3]] | B | TNS3 activity lowers SHANK1's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 4.37× higher at baseline in the lines without TNS3 | 0.009 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[STC1]] | B | STC1 activity raises SHANK1's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without STC1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[SGIP1]] | B | SGIP1 activity raises SHANK1's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.36× lower at baseline in the lines without SGIP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[IL11]] | B | IL11 activity raises SHANK1's level | lines that do not express IL11 (27) vs lines expressing it (23) | 2.31× lower at baseline in the lines without IL11 | 0.032 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[ROBO4]] | B | ROBO4 activity raises SHANK1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.74× lower at baseline in the lines without ROBO4 | 0.033 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[NETO1]] | B | NETO1 activity raises SHANK1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 3.25× lower at baseline in the lines without NETO1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises SHANK1's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 1.98× lower at baseline in the lines without APCDD1L-DT | 0.050 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[BCL2A1]] | B | BCL2A1 activity raises SHANK1's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.56× lower at baseline in the lines without BCL2A1 | 0.082 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[MAP2K1]] | B | MAP2K1 activity raises SHANK1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ENKUR]] | B | ENKUR activity strengthens SHANK1's drug response | lines that do not express ENKUR (9) vs lines expressing it (16) | the lines without ENKUR respond 0.61× as strongly (z diff +1.02); strongest at Trametinib (DMSO_TF solvate) 0.5 µM: 0.95x vs 0.41x (z diff +3.7) | 0.086 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[MEG8]] | B | MEG8 activity raises SHANK1's level | lines that do not express MEG8 (32) vs lines expressing it (18) | 1.35× lower at baseline in the lines without MEG8 | 0.089 | ⚠ within organs, on part of the lines; also absent: MEG3, MIR493HG, MXRA8 |
| [[LINC01812]] | B | LINC01812 activity strengthens SHANK1's drug response | lines that do not express LINC01812 (16) vs lines expressing it (9) | the lines without LINC01812 respond 0.64× as strongly (z diff +1.04); strongest at Trametinib 5 µM: 0.69x vs 0.32x (z diff +4.5) | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 8, C 5. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGF]] | B | SHANK1 activity raises PGF's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 1.47× lower at baseline in the lines without SHANK1 | 0.045 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[SNCAIP]] | B | SHANK1 activity raises SNCAIP's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 2.19× lower at baseline in the lines without SHANK1 | 0.048 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[CLEC11A]] | B | SHANK1 activity weakens CLEC11A's drug response | lines that do not express SHANK1 (6) vs lines expressing it (19) | the lines without SHANK1 respond 1.26× as strongly (z diff -0.20); rises at some drug-doses, falls at others (70% from rises): Topotecan (hydrochloride) 5 µM: 2.65x vs 0.97x (z diff -3.2); Panobinostat 0.5 µM: 2.96x vs 1.43x (z diff -2.4); Rutin (trihydrate) 0.05 µM: 0.46x vs 0.77x (z diff -1.5) | 0.054 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[PLEKHG4B]] | B | SHANK1 activity raises PLEKHG4B's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 2.59× lower at baseline in the lines without SHANK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[FHAD1]] | B | SHANK1 activity raises FHAD1's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 1.31× lower at baseline in the lines without SHANK1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[MBNL1]] | B | SHANK1 activity lowers MBNL1's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 1.28× higher at baseline in the lines without SHANK1 | 0.064 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[STC1]] | B | SHANK1 activity raises STC1's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 3.22× lower at baseline in the lines without SHANK1 | 0.065 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[FAM167A]] | B | SHANK1 activity raises FAM167A's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without SHANK1 | 0.080 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[CRMP1]] | C | SHANK1 activity raises CRMP1's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 2.70× lower at baseline in the lines without SHANK1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880; co-absent with the target |
| [[CLEC11A]] | C | SHANK1 activity raises CLEC11A's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 2.91× lower at baseline in the lines without SHANK1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880; co-absent with the target |
| [[MME]] | C | SHANK1 activity raises MME's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 4.72× lower at baseline in the lines without SHANK1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880; co-absent with the target |
| [[MEG3]] | C | SHANK1 activity raises MEG3's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without SHANK1 | 0.077 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.7, 12.9); signed map (19.1, 47.8). **Vector** length 90.6, 26.8% of its response variance represented; |z| ≥ 3 in 776 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NCAM1 interactions* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +5.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +2.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -5.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.4 | -6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.6 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | SH3 and multiple ankyrin repeat domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:50,659,255-50,719,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SSTRIP, SPANK-1, synamon |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Sterile alpha motif domain containing; PDZ domain containing; SH3 domain containing |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y566](https://www.uniprot.org/uniprotkb/Q9Y566) (SH3 and multiple ankyrin repeat domains protein 1):

> Seems to be an adapter protein in the postsynaptic density (PSD) of excitatory synapses that interconnects receptors of the postsynaptic membrane including NMDA-type and metabotropic glutamate receptors via complexes with GKAP/PSD-95 and Homer, respectively, and the actin-based cytoskeleton. Plays a role in the structural and functional organization of the dendritic spine and synaptic junction.

**Summary**, from NCBI Gene [50944](https://www.ncbi.nlm.nih.gov/gene/50944):

> This gene encodes a member of the SHANK (SH3 domain and ankyrin repeat containing) family of proteins. Members of this family act as scaffold proteins that are required for the development and function of neuronal synapses. Deletions in this gene may be associated with autism spectrum disorder in males. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:15474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15474) · Entrez [50944](https://www.ncbi.nlm.nih.gov/gene/50944) · UniProt [Q9Y566](https://www.uniprot.org/uniprotkb/Q9Y566) · Ensembl [ENSG00000161681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161681)

## Data

Gene col 8449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8449); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8449]; `tensor/DDL_lfc|DDL_z.npy` [8449]; `embed/gene_vectors.npy` [8449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8449 or target_col == 8449). Every well: [[SHANK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHANK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
