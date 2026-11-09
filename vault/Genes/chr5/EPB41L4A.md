---
symbol: "EPB41L4A"
type: "gene"
col: 4990
ensembl_id: "ENSG00000129595"
name: "erythrocyte membrane protein band 4.1 like 4A"
location: "5q22.1-q22.2"
module: 115
arm: "+"
pooled_cpm: 28.49
n_lines_expressing: 24
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# EPB41L4A

*erythrocyte membrane protein band 4.1 like 4A* — 5q22.1-q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +19.5, q 0e+00, up in 9 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.782× (z -5.9, q 1e-06, down in 17 of 22 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.683× (z -5.9, q 1e-06, down in 13 of 22 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANO4]] (+0.56, fdr 2e-05), [[ENTREP2]] (+0.52, fdr 2e-05), [[CCDC85A]] (+0.51, fdr 3e-05); moves opposite to [[PRPF38A]] (-0.38, fdr 4e-04), [[TUBGCP2]] (-0.37, fdr 7e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[KCNS3]] → it (grade B ⚠); 7 go from it, the strongest it → [[KCNK13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +19.5 | 0e+00 | 9/22 (H4, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.07×** | +17.6 | 0e+00 | 11/22 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.35×** | +13.2 | 1e-37 | 15/22 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +11.9 | 2e-30 | 4/20 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +11.0 | 4e-26 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +9.0 | 2e-17 | 7/22 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +8.1 | 6e-14 | 10/22 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.3 | 9e-06 | 10/22 (PANC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +4.8 | 9e-05 | 3/17 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.7 | 2e-04 | 3/20 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.001 | 1/22 (A498) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.002 | 0/22 | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 8/22 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 7/22 (PANC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.006 | 7/22 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.007 | 2/22 (NCI-H1573, Panc 03.27) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.14× | +3.2 | 0.054 | 6/22 (HEC-1-A, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.782×** | -5.9 | 1e-06 | 17/22 (LoVo, A-172, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.683×** | -5.9 | 1e-06 | 13/22 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.721×** | -5.6 | 5e-06 | 18/22 (J82, LoVo, …) | top dose only | composition shift |
| [[Larotrectinib (drug)]] 5 µM |  | **0.813×** | -5.0 | 8e-05 | 18/22 (NCI-H23, A-427, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.755×** | -4.8 | 2e-04 | 7/22 (H4, SNU-1, …) | all doses, flat |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | **0.779×** | -3.9 | 0.008 | 1/22 (PANC-1) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.803×** | -3.7 | 0.014 | 16/22 (BT-474, NCI-H23, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.804×** | -3.7 | 0.014 | 15/22 (J82, BT-474, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.672×** | -3.5 | 0.025 | 12/23 (A549, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.867× | -3.4 | 0.034 | 4/22 (A549, SNU-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.683×** | -3.4 | 0.034 | 10/22 (SW1417, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.051 | 9/22 (A-172, BT-474, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.822×** | -3.2 | 0.069 | 2/22 (LoVo, NCI-H1573) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 123 | 0 | 12 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.154× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -11.8) |
| [[J82 (line)]] | alt | 75.5 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 66.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.352× (z -9.7) |
| [[Hs 766T (line)]] | wt | 98.3 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.312× (z -8.7) |
| [[PANC-1 (line)]] | alt | 7.50 | 5 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.33× (z +13.1) | — |
| [[LoVo (line)]] | wt | 93.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -16.8) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A-172 (line)]] | wt | 31.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0927× (z -15.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 83.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H1573 (line)]] | alt | 14.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.64× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 57.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.299× (z -8.6) |
| [[SW1417 (line)]] | alt | 81.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 82.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -17.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 55.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -16.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 93.1 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0612× (z -10.9) |
| [[A498 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANO4]] | +0.56 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ENTREP2]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[CCDC85A]] | +0.51 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[ROR2]] | +0.50 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[COL4A4]] | +0.49 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PHACTR3]] | +0.48 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[SNAP91]] | +0.48 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[NELL2]] | +0.48 | +0.41 / +0.39 | both halves | 6e-05 |  |
| [[PRSS12]] | +0.47 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[KCNS3]] | +0.46 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[ZNF385B]] | +0.46 | +0.40 / +0.38 | both halves | 6e-05 |  |
| [[ZDHHC2]] | +0.45 | +0.42 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF38A]] | -0.38 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[TUBGCP2]] | -0.37 | -0.21 / -0.29 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNS3]] | B | KCNS3 activity raises EPB41L4A's level | lines that do not express KCNS3 (16) vs lines expressing it (34) | 3.04× lower at baseline in the lines without KCNS3 | 0.025 | ⚠ within organs, on part of the lines; also absent: EFCAB13, JHY, SAA1; maybe low, not absent |
| [[SYTL4]] | B | SYTL4 activity raises EPB41L4A's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 3.19× lower at baseline in the lines without SYTL4 | 0.051 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[RIMKLB]] | B | RIMKLB activity raises EPB41L4A's level | lines that do not express RIMKLB (13) vs lines expressing it (37) | 2.15× lower at baseline in the lines without RIMKLB | 0.058 | ⚠ within organs, on part of the lines; also absent: DNAAF9, GJC1, ANKRD6 |
| [[ENTREP1]] | C | ENTREP1 activity raises EPB41L4A's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 3.90× lower at baseline in the lines without ENTREP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4; co-absent with the target |
| [[COL4A4]] | C | COL4A4 activity raises EPB41L4A's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 3.25× lower at baseline in the lines without COL4A4 | 0.008 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[COL4A3]] | C | COL4A3 activity raises EPB41L4A's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 3.24× lower at baseline in the lines without COL4A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[ANO4]] | C | ANO4 activity raises EPB41L4A's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 2.36× lower at baseline in the lines without ANO4 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK13]] | B | EPB41L4A activity raises KCNK13's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 1.26× lower at baseline in the lines without EPB41L4A | 0.035 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P |
| [[ENTREP2]] | B | EPB41L4A activity raises ENTREP2's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 2.00× lower at baseline in the lines without EPB41L4A | 0.052 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P |
| [[RIMKLB]] | B | EPB41L4A activity raises RIMKLB's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without EPB41L4A | 0.059 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P |
| [[TJP1]] | B | EPB41L4A activity raises TJP1's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 1.34× lower at baseline in the lines without EPB41L4A | 0.099 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P |
| [[STOX2]] | C | EPB41L4A activity raises STOX2's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 2.59× lower at baseline in the lines without EPB41L4A | 0.035 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P; co-absent with the target |
| [[ANO4]] | C | EPB41L4A activity raises ANO4's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 1.53× lower at baseline in the lines without EPB41L4A | 0.067 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P; co-absent with the target |
| [[ENTREP1]] | C | EPB41L4A activity raises ENTREP1's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 1.99× lower at baseline in the lines without EPB41L4A | 0.095 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.369). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.2, 41.0); signed map (54.1, 16.1). **Vector** length 63.0, 15.5% of its response variance represented; |z| ≥ 3 in 635 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +17.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +19.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.0 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.2 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.8 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | +2.5 |

## What is on record

|  |  |
|---|---|
| Name | erythrocyte membrane protein band 4.1 like 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.1-q22.2 — chr5:112,142,441-112,419,313 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NBL4 |
| Gene groups (HGNC) | FERM domain containing |
| Matched by | ensembl_id |

UniProt [Q9HCS5](https://www.uniprot.org/uniprotkb/Q9HCS5) carries no function annotation.

**Summary**, from NCBI Gene [64097](https://www.ncbi.nlm.nih.gov/gene/64097):

> The protein encoded by this gene is a member of the band 4.1 protein superfamily. Members of this superfamily are thought to play an important role in regulating interactions between the cytoskeleton and plasma membrane, and contain an amino terminal conserved domain that binds glycophorin C. This gene product is thought to be involved in the beta-catenin signaling pathway. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:13278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13278) · Entrez [64097](https://www.ncbi.nlm.nih.gov/gene/64097) · UniProt [Q9HCS5](https://www.uniprot.org/uniprotkb/Q9HCS5) · Ensembl [ENSG00000129595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129595)

## Data

Gene col 4990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4990); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4990]; `tensor/DDL_lfc|DDL_z.npy` [4990]; `embed/gene_vectors.npy` [4990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4990 or target_col == 4990). Every well: [[EPB41L4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPB41L4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
