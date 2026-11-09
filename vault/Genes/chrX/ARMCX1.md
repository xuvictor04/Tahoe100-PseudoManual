---
symbol: "ARMCX1"
type: "gene"
col: 4781
ensembl_id: "ENSG00000126947"
name: "armadillo repeat containing X-linked 1"
location: "Xq22.1"
module: 122
arm: "+"
pooled_cpm: 3.74
n_lines_expressing: 27
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 12
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# ARMCX1

*armadillo repeat containing X-linked 1* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.15× (z +12.1, q 4e-31, up in 19 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.401× (z -10.3, q 5e-22, down in 18 of 24 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.555× (z -6.6, q 5e-09, down in 13 of 24 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPART]] (+0.69, fdr 1e-05), [[GPRASP3]] (+0.63, fdr 1e-05), [[DTX3]] (+0.62, fdr 7e-06); moves opposite to [[STK39]] (-0.56, fdr 3e-05), [[TTC13]] (-0.55, fdr 3e-05), [[GMDS]] (-0.54, fdr 4e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[GLMP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.15×** | +12.1 | 4e-31 | 19/24 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +6.9 | 2e-09 | 12/22 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +5.3 | 2e-05 | 4/13 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +5.1 | 5e-05 | 11/19 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.7 | 0.023 | 5/17 (LOX-IMVI, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.023 | 5/23 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.023 | 5/22 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.6 | 0.023 | 3/24 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.45×** | +3.6 | 0.023 | 6/24 (J82, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +3.4 | 0.032 | 5/24 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.063 | 6/24 (NCI-H23, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.097 | 4/22 (J82, A498, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.68×** | +3.1 | 0.097 | 2/18 (NCI-H2030, Panc 03.27) | top dose only | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4781.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.401×** | -10.3 | 5e-22 | 18/24 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.409×** | -10.1 | 2e-21 | 17/23 (SNU-423, RPMI-7951, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.428×** | -9.6 | 2e-19 | 16/24 (RPMI-7951, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.555×** | -6.6 | 5e-09 | 13/24 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.571×** | -6.1 | 1e-07 | 12/21 (H4, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.725×** | -5.1 | 3e-05 | 11/24 (SNU-423, RPMI-7951, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.646×** | -4.9 | 7e-05 | 8/23 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.747×** | -4.7 | 2e-04 | 10/22 (RPMI-7951, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.668×** | -4.5 | 4e-04 | 10/24 (NCI-H2030, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.673×** | -4.5 | 5e-04 | 5/23 (NCI-H2030, A-172, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.693×** | -4.0 | 0.004 | 7/22 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.709×** | -3.9 | 0.005 | 7/23 (NCI-H2030, SW 900, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.713×** | -3.8 | 0.006 | 10/23 (A-172, NCI-H2347, …) | rises with dose | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **0.683×** | -3.7 | 0.009 | 4/20 (A498, A-172, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.728×** | -3.4 | 0.022 | 7/23 (A-172, SNU-423, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.767×** | -3.0 | 0.092 | 4/23 (C32, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.69 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.80 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +9.2) | [[Panobinostat (drug)]] 0.05 µM 0.0936× (z -9.1) |
| [[HS-578T (line)]] | alt | 7.75 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.143× (z -9.2) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.209× (z -10.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[J82 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -10.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.340 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.313 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPART]] | +0.69 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[GPRASP3]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 | same gene group |
| [[DTX3]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[TCEAL1]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 | STRING 485 |
| [[RAB29]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[LINC02335]] | +0.57 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[UAP1L1]] | +0.57 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[WASHC2A]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[TSC1]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[BTN3A1]] | +0.56 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[ZNF737]] | +0.55 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[BTN2A2]] | +0.55 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK39]] | -0.56 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[TTC13]] | -0.55 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[GMDS]] | -0.54 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SRPK1]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[SPCS3]] | -0.53 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[UBE2G2]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[HDAC4]] | -0.51 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[DIAPH1]] | -0.51 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[TRAPPC9]] | -0.51 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[YWHAB]] | -0.51 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[SEPTIN10]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CHID1]] | -0.50 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARMCX1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF737]] | B | ZNF737 activity raises ARMCX1's level | lines that do not express ZNF737 (18) vs lines expressing it (32) | 2.09× lower at baseline in the lines without ZNF737 | 0.045 | ⚠ within organs, on part of the lines; also absent: ZNF85, ZNF66, ZNF90 |
| [[ARMCX2]] | C | ARMCX2 activity raises ARMCX1's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 3.31× lower at baseline in the lines without ARMCX2 | 0.025 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[GNG2]] | C | GNG2 activity raises ARMCX1's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 2.93× lower at baseline in the lines without GNG2 | 0.057 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 7, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLMP]] | B | ARMCX1 activity raises GLMP's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without ARMCX1 | 0.023 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[TCEAL3]] | B | ARMCX1 activity raises TCEAL3's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 2.74× lower at baseline in the lines without ARMCX1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[ZSCAN12]] | B | ARMCX1 activity raises ZSCAN12's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 2.60× lower at baseline in the lines without ARMCX1 | 0.039 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[SHISA4]] | B | ARMCX1 activity raises SHISA4's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 1.82× lower at baseline in the lines without ARMCX1 | 0.062 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[TP53BP1]] | B | ARMCX1 activity raises TP53BP1's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without ARMCX1 | 0.064 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[CLIP3]] | B | ARMCX1 activity raises CLIP3's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without ARMCX1 | 0.072 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[BRI3BP]] | B | ARMCX1 activity lowers BRI3BP's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 2.14× higher at baseline in the lines without ARMCX1 | 0.073 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[ARMCX2]] | C | ARMCX1 activity raises ARMCX2's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 3.95× lower at baseline in the lines without ARMCX1 | 0.009 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1; co-absent with the target |
| [[GNG2]] | C | ARMCX1 activity raises GNG2's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 4.41× lower at baseline in the lines without ARMCX1 | 0.025 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1; co-absent with the target |
| [[MAGI2]] | C | ARMCX1 activity raises MAGI2's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 5.70× lower at baseline in the lines without ARMCX1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1; co-absent with the target |
| [[ZNF625]] | C | ARMCX1 activity raises ZNF625's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 3.41× lower at baseline in the lines without ARMCX1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1; co-absent with the target |
| [[ATP6V0D2]] | C | ARMCX1 activity raises ATP6V0D2's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 3.07× lower at baseline in the lines without ARMCX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.1, 17.0); signed map (15.8, -13.9). **Vector** length 45.9, 9.05% of its response variance represented; |z| ≥ 3 in 522 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.4 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +6.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.7 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.1 | +3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.7 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.5 | -10.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -1.5 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.2 | -4.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing X-linked 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,550,547-101,554,700 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALEX1, GASP7 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P291](https://www.uniprot.org/uniprotkb/Q9P291) (Armadillo repeat-containing X-linked protein 1):

> Regulates mitochondrial transport during axon regeneration. Increases the proportion of motile mitochondria by recruiting stationary mitochondria into the motile pool. Enhances mitochondria movement and neurite growth in both adult axons and embryonic neurons. Promotes neuronal survival and axon regeneration after nerve injury. May link mitochondria to the Trak1-kinesin motor complex via its interaction with MIRO1.

**Summary**, from NCBI Gene [51309](https://www.ncbi.nlm.nih.gov/gene/51309):

> This gene encodes a member of the ALEX family of proteins and may play a role in tumor suppression. The encoded protein contains a potential N-terminal transmembrane domain and two Armadillo (arm) repeats. Other proteins containing the arm repeat are involved in development, maintenance of tissue integrity, and tumorigenesis. This gene is closely localized with other family members, including ALEX2 and ALEX3, on the X chromosome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18073) · Entrez [51309](https://www.ncbi.nlm.nih.gov/gene/51309) · UniProt [Q9P291](https://www.uniprot.org/uniprotkb/Q9P291) · Ensembl [ENSG00000126947](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126947)

## Data

Gene col 4781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4781); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4781]; `tensor/DDL_lfc|DDL_z.npy` [4781]; `embed/gene_vectors.npy` [4781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4781 or target_col == 4781). Every well: [[ARMCX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMCX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
