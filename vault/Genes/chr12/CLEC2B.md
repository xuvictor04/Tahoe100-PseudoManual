---
symbol: "CLEC2B"
type: "gene"
col: 3171
ensembl_id: "ENSG00000110852"
name: "C-type lectin domain family 2 member B"
location: "12p13.31"
module: 79
arm: "+"
pooled_cpm: 49.91
n_lines_expressing: 28
n_dd_up: 1
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# CLEC2B

*C-type lectin domain family 2 member B* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.60× (z +4.4, q 0.005, up in 13 of 25 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change.
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.323× (z -10.6, q 1e-23, down in 26 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC03047]] (+0.60, fdr 1e-05), [[ANG]] (+0.58, fdr 1e-05), [[RNASE4]] (+0.57, fdr 1e-05); moves opposite to [[PTPN11]] (-0.56, fdr 3e-05), [[GNL3L]] (-0.52, fdr 2e-05), [[PIGO]] (-0.50, fdr 1e-04).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TMEM158]] → it (grade C ⚠); 5 go from it, the strongest it → [[RAB8B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.60×** | +4.4 | 0.005 | 13/25 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.46× | +3.3 | 0.19 | 3/21 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.41× | +3.3 | 0.19 | 4/23 (Hs 766T, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.59× | +3.1 | 0.23 | 10/26 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3171.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.323×** | -10.6 | 1e-23 | 26/26 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.556×** | -7.8 | 2e-12 | 22/26 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.472×** | -7.1 | 3e-10 | 23/26 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.488×** | -6.7 | 2e-09 | 26/26 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.504×** | -6.4 | 1e-08 | 23/26 (A498, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.515×** | -6.0 | 2e-07 | 21/26 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.552×** | -5.6 | 2e-06 | 21/26 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.604×** | -4.5 | 5e-04 | 16/26 (A-172, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.716×** | -4.4 | 6e-04 | 20/26 (CFPAC-1, C32, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.715×** | -4.3 | 8e-04 | 15/26 (NCI-H2030, A-172, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.637×** | -4.1 | 0.002 | 18/24 (CFPAC-1, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.666×** | -3.8 | 0.007 | 17/26 (AsPC-1, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.647×** | -3.8 | 0.007 | 13/26 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -3.7 | 0.009 | 3/27 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.689×** | -3.5 | 0.018 | 11/25 (NCI-H2030, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.538×** | -3.1 | 0.081 | 18/26 (NCI-H1792, C32, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.543×** | -3.0 | 0.088 | 18/26 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 170 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0885× (z -21.7) |
| [[CFPAC-1 (line)]] | alt | 93.7 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -23.6) |
| [[HOP62 (line)]] | alt | 281 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0602× (z -20.3) |
| [[A-172 (line)]] | wt | 99.1 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0704× (z -19.7) |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 6 | — | [[Harringtonine (drug)]] 5 µM 0.0937× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 75.8 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0786× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 225 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 78.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -13.9) |
| [[Hs 766T (line)]] | wt | 137 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -13.8) |
| [[PANC-1 (line)]] | alt | 25.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.9) |
| [[SW 900 (line)]] | alt | 83.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 36.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.9) |
| [[H4 (line)]] | wt | 265 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.4) |
| [[J82 (line)]] | alt | 71.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -14.1) |
| [[A498 (line)]] | wt | 67.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.212× (z -10.4) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.189× (z -8.7) |
| [[SW 1088 (line)]] | alt | 226 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0287× (z -18.6) |
| [[A-427 (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.89 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.47 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.61 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03047]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ANG]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RNASE4]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.56 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RHEBL1]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[UHRF2]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ZNF8-DT]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[USP37]] | +0.54 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[RSBN1]] | +0.54 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[PEX3]] | +0.54 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[WDR54]] | +0.54 | +0.59 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN11]] | -0.56 | -0.46 / -0.61 | both halves | 3e-05 | STRING 410 |
| [[GNL3L]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PIGO]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[CDC42BPA]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[POGK]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SLC35F6]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ANAPC7]] | -0.48 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[VARS1]] | -0.48 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[OCRL]] | -0.47 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[SLC12A8]] | -0.47 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[ARMC6]] | -0.46 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[INTS7]] | -0.46 | -0.38 / -0.50 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM158]] | C | TMEM158 activity raises CLEC2B's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 6.24× lower at baseline in the lines without TMEM158 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises CLEC2B's level | lines that do not express GYPC (35) vs lines expressing it (15) | 4.91× lower at baseline in the lines without GYPC | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB8B]] | B | CLEC2B activity raises RAB8B's level | lines that do not express CLEC2B (22) vs lines expressing it (28) | 2.03× lower at baseline in the lines without CLEC2B | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, TMEM158, FRMD4A |
| [[CHSY1]] | B | CLEC2B activity raises CHSY1's level | lines that do not express CLEC2B (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without CLEC2B | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, TMEM158, FRMD4A |
| [[VKORC1]] | B | CLEC2B activity raises VKORC1's level | lines that do not express CLEC2B (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without CLEC2B | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, TMEM158, FRMD4A |
| [[TMEM158]] | C | CLEC2B activity raises TMEM158's level | lines that do not express CLEC2B (22) vs lines expressing it (28) | 4.40× lower at baseline in the lines without CLEC2B | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, TMEM158, FRMD4A; co-absent with the target |
| [[LINC03047]] | C | CLEC2B activity raises LINC03047's level | lines that do not express CLEC2B (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without CLEC2B | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, TMEM158, FRMD4A; co-absent with the target |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.5, -20.7); signed map (-33.5, 22.7). **Vector** length 89.4, 27.3% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -6.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.9 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | C-type lectin domain family 2 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:9,852,369-9,869,386 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AICL, HP10085; previously CLECSF2 |
| Gene groups (HGNC) | C-type lectin domain containing |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92478](https://www.uniprot.org/uniprotkb/Q92478) (C-type lectin domain family 2 member B):

> Membrane-bound protein expressed on myeloid cells which acts as a ligand to stimulate the activating receptor NKp80/KLRF1, expressed on the surface of natural killer (NK) cells. In turn, stimulates NK-cell cytotoxicity and cytokine production leading to the cytolysis of malignant CLEC2B-expressing myeloid cells.

**Summary**, from NCBI Gene [9976](https://www.ncbi.nlm.nih.gov/gene/9976):

> This gene encodes a member of the C-type lectin/C-type lectin-like domain (CTL/CTLD) superfamily. Members of this family share a common protein fold and have diverse functions, such as cell adhesion, cell-cell signalling, glycoprotein turnover, and roles in inflammation and immune response. The encoded type 2 transmembrane protein may function as a cell activation antigen. An alternative splice variant has been described but its full-length sequence has not been determined. This gene is closely …

**Accessions** — [HGNC:2053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2053) · Entrez [9976](https://www.ncbi.nlm.nih.gov/gene/9976) · UniProt [Q92478](https://www.uniprot.org/uniprotkb/Q92478) · Ensembl [ENSG00000110852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110852)

## Data

Gene col 3171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3171); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3171]; `tensor/DDL_lfc|DDL_z.npy` [3171]; `embed/gene_vectors.npy` [3171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3171 or target_col == 3171). Every well: [[CLEC2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLEC2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
