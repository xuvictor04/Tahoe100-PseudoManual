---
symbol: "PRR36"
type: "gene"
col: 11384
ensembl_id: "ENSG00000183248"
name: "proline rich 36"
location: "19p13.2"
module: 2
arm: "+"
pooled_cpm: 2.94
n_lines_expressing: 31
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 35
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PRR36

*proline rich 36* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.29× (z +9.3, q 1e-17, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pyridoxine (drug)]] 0.5 µM: 1.57× (z +3.7, q 0.029, up in 5 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -6.9, q 3e-09, down in 13 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP1G2]] (+0.64, fdr 7e-06), [[BCAM]] (+0.56, fdr 1e-05), [[SLC25A23]] (+0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NOXA1]] → it (grade B ⚠); 35 go from it, the strongest it → [[MPP7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11384.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +9.3 | 1e-17 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +7.3 | 1e-10 | 7/13 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +5.5 | 9e-06 | 1/3 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +4.5 | 9e-04 | 4/28 (NCI-H23, COLO 205, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.029 | 5/18 (SHP-77, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.4 | 0.058 | 4/13 (HEC-1-A, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11384.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -6.9 | 3e-09 | 13/22 (HEC-1-A, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.482×** | -5.9 | 1e-06 | 16/23 (NCI-H2347, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.491×** | -5.8 | 2e-06 | 18/26 (C-33 A, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.545×** | -4.7 | 3e-04 | 8/22 (SW 900, SW480, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.558×** | -4.7 | 3e-04 | 14/28 (SW480, COLO 205, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.593×** | -4.2 | 0.002 | 8/24 (LS 180, SW 900, …) | all doses, flat | cell-cycle shift (explains ~17% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.600×** | -4.1 | 0.003 | 7/26 (SW1417, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.592×** | -4.1 | 0.003 | 11/26 (Panc 03.27, HCT15, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.641×** | -3.6 | 0.021 | 9/27 (NCI-H2347, BT-474, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -3.5 | 0.024 | 6/27 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.747×** | -3.3 | 0.049 | 15/25 (SW 900, NCI-H2347, …) | two highest doses | composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.665×** | -3.1 | 0.087 | 9/24 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.684×** | -3.1 | 0.087 | 1/28 (RKO) | rises with dose | position effect removed |
| [[Sulfisoxazole (drug)]] 5 µM |  | **0.759×** | -3.1 | 0.087 | 4/27 (NCI-H661, HT-29, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0801× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H2347 (line)]] | alt | 9.03 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -8.9) |
| [[RKO (line)]] | wt | 6.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0837× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SW 900 (line)]] | alt | 3.87 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0440× (z -8.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 3.23 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0934× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.992 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.974 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.159 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.995 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.945 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1G2]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[BCAM]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TRAF7]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[SSH3]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ABCA2]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ACBD4]] | +0.52 | +0.51 / +0.37 | both halves | 9e-05 |  |
| [[RAP1GAP]] | +0.52 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[NSMF]] | +0.52 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[ELMO3]] | +0.52 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[PRSS16]] | +0.52 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[EPS8L2]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOXA1]] | B | NOXA1 activity raises PRR36's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 2.68× lower at baseline in the lines without NOXA1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[ERBB3]] | B | ERBB3 activity raises PRR36's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without ERBB3 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[BSPRY]] | C | BSPRY activity raises PRR36's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 1.95× lower at baseline in the lines without BSPRY | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[ENPP5]] | C | ENPP5 activity raises PRR36's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.97× lower at baseline in the lines without ENPP5 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises PRR36's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.24× lower at baseline in the lines without KIF1A | 0.092 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 28, C 7. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP7]] | B | PRR36 activity raises MPP7's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 3.60× lower at baseline in the lines without PRR36 | 0.005 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[CACFD1]] | B | PRR36 activity raises CACFD1's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.39× lower at baseline in the lines without PRR36 | 0.006 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[ROGDI]] | B | PRR36 activity raises ROGDI's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without PRR36 | 0.007 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[ERBB3]] | B | PRR36 activity raises ERBB3's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 2.82× lower at baseline in the lines without PRR36 | 0.039 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[PROM2]] | B | PRR36 activity raises PROM2's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without PRR36 | 0.048 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| cells under [[Balsalazide (sodium hydrate) (drug)]] 5 µM | B | PRR36 activity lowers the cells' numbers under Balsalazide (sodium hydrate) 5 µM (makes them more sensitive) | lines that do not express PRR36 (19) vs lines expressing it (29) | the lines without PRR36: 1.10× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[SPINT2]] | B | PRR36 activity raises SPINT2's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 3.16× lower at baseline in the lines without PRR36 | 0.054 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[PRXL2B]] | B | PRR36 activity raises PRXL2B's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without PRR36 | 0.055 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| cells under [[Malotilate (drug)]] 0.05 µM | B | PRR36 activity lowers the cells' numbers under Malotilate 0.05 µM (makes them more sensitive) | lines that do not express PRR36 (19) vs lines expressing it (29) | the lines without PRR36: 1.20× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[CARD10]] | B | PRR36 activity raises CARD10's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without PRR36 | 0.065 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[SPINT1]] | B | PRR36 activity raises SPINT1's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 3.63× lower at baseline in the lines without PRR36 | 0.074 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[TMEM184A]] | B | PRR36 activity raises TMEM184A's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.66× lower at baseline in the lines without PRR36 | 0.074 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-1.6, 31.6); signed map (-5.2, 17.7). **Vector** length 41.7, 7.22% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +5.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +0.7 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.4 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -3.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -0.9 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,868,719-7,874,390 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q9H6K5](https://www.uniprot.org/uniprotkb/Q9H6K5) carries no function annotation.

**Summary**, from NCBI Gene [80164](https://www.ncbi.nlm.nih.gov/gene/80164):

> This gene encodes a large protein of unknown function that contains internal regions of low complexity sequence. Alternative splicing results in multiple transcript variants. The transcript structure of the protein-coding variant at this locus is conserved between human and mouse. [provided by RefSeq, Oct 2013]

**Accessions** — [HGNC:26172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26172) · Entrez [80164](https://www.ncbi.nlm.nih.gov/gene/80164) · UniProt [Q9H6K5](https://www.uniprot.org/uniprotkb/Q9H6K5) · Ensembl [ENSG00000183248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183248)

## Data

Gene col 11384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11384); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11384]; `tensor/DDL_lfc|DDL_z.npy` [11384]; `embed/gene_vectors.npy` [11384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11384 or target_col == 11384). Every well: [[PRR36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
