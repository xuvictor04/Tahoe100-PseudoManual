---
symbol: "HS3ST1"
type: "gene"
col: 22
ensembl_id: "ENSG00000002587"
name: "heparan sulfate-glucosamine 3-sulfotransferase 1"
location: "4p15.33"
module: 31
arm: "+"
pooled_cpm: 20.23
n_lines_expressing: 19
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 108
direction_downstream: 149
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# HS3ST1

*heparan sulfate-glucosamine 3-sulfotransferase 1* — 4p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.05× (z +8.8, q 7e-16, up in 0 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.60× (z +8.5, q 5e-15, up in 5 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.660× (z -7.5, q 3e-11, down in 15 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLK10]] (+0.78, fdr 7e-06), [[TMPRSS4]] (+0.78, fdr 7e-06), [[KIAA0040]] (+0.78, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 108 arrows point to it, the strongest [[LYPD3]] → it (grade B ⚠); 149 go from it, the strongest it → [[TNFRSF21]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 22.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.8 | 7e-16 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +8.5 | 5e-15 | 5/17 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +7.3 | 6e-11 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +7.0 | 5e-10 | 2/16 (NCI-H1573, SHP-77) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.1 | 1e-07 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.2 | 0.002 | 2/16 (SW 900, SW1417) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.19 | 2/17 (SW 900, AsPC-1) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 22.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.660×** | -7.5 | 3e-11 | 15/17 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.583×** | -6.2 | 1e-07 | 10/17 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.602×** | -6.0 | 3e-07 | 9/17 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.891× | -5.3 | 1e-05 | 2/18 (SHP-77, HCT15) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -4.7 | 3e-04 | 14/16 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.729×** | -4.5 | 7e-04 | 9/17 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.794×** | -4.1 | 0.003 | 5/17 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.703×** | -4.0 | 0.004 | 9/17 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.802×** | -3.9 | 0.005 | 8/17 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.744×** | -3.6 | 0.019 | 15/17 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.741×** | -3.4 | 0.032 | 10/17 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.769×** | -3.4 | 0.033 | 7/17 (Hs 766T, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.774×** | -3.3 | 0.043 | 6/17 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.767×** | -3.0 | 0.092 | 6/17 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.776×** | -3.0 | 0.092 | 0/17 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 5 µM |  | **0.639×** | -3.0 | 0.092 | 0/17 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.5 µM |  | **0.793×** | -3.0 | 0.092 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 22. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 85.2 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0546× (z -31.3) |
| [[Panc 03.27 (line)]] | alt | 192 | 0 | 12 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0906× (z -28.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.145× (z -23.0) |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 71.6 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 58.4 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.249× (z -10.4) |
| [[Hs 766T (line)]] | wt | 47.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0988× (z -20.7) |
| [[LS 180 (line)]] | wt | 48.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 22.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -16.0) |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -12.3) |
| [[HT-29 (line)]] | alt | 30.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 34.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -14.4) |
| [[LoVo (line)]] | wt | 25.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.1) |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.52 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.67 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 22), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLK10]] | +0.78 | +0.83 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.78 | +0.75 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[KIAA0040]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PRSS3]] | +0.78 | +0.73 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[GJB3]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB5]] | +0.76 | +0.75 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[DSG3]] | +0.76 | +0.72 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[FA2H]] | +0.76 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | pathway: Glycosaminoglycan metabolism |
| [[KLK11]] | +0.74 | +0.79 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[CRYBG2]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[PADI1]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*108 arrows, 108 of them with an alert ⚠; grade A 0, B 13, C 95. Shown: the 12 strongest; 96 more arrows (96 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPD3]] | B | LYPD3 activity raises HS3ST1's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.17× lower at baseline in the lines without LYPD3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises HS3ST1's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.04× lower at baseline in the lines without LMO7 | 0.033 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[PPARG]] | B | PPARG activity raises HS3ST1's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.79× lower at baseline in the lines without PPARG | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[GRHL3]] | B | GRHL3 activity raises HS3ST1's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.51× lower at baseline in the lines without GRHL3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[ABHD17C]] | B | ABHD17C activity raises HS3ST1's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.94× lower at baseline in the lines without ABHD17C | 0.050 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises HS3ST1's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.70× lower at baseline in the lines without TJP2 | 0.050 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises HS3ST1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.11× lower at baseline in the lines without GPRC5A | 0.051 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[MAP2K1]] | B | MAP2K1 activity raises HS3ST1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SEMA3B]] | B | SEMA3B activity raises HS3ST1's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.83× lower at baseline in the lines without SEMA3B | 0.079 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[INPP4B]] | B | INPP4B activity raises HS3ST1's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.26× lower at baseline in the lines without INPP4B | 0.081 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[B4GALNT3]] | B | B4GALNT3 activity raises HS3ST1's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.58× lower at baseline in the lines without B4GALNT3 | 0.089 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[PKP2]] | B | PKP2 activity raises HS3ST1's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 3.11× lower at baseline in the lines without PKP2 | 0.095 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |

### Downstream of this gene

*149 arrows, 149 of them with an alert ⚠; grade A 0, B 58, C 91. Shown: the 12 strongest; 137 more arrows (137 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF21]] | B | HS3ST1 activity raises TNFRSF21's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 4.77× lower at baseline in the lines without HS3ST1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[LMO7]] | B | HS3ST1 activity raises LMO7's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 5.03× lower at baseline in the lines without HS3ST1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[EPS8L1]] | B | HS3ST1 activity raises EPS8L1's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.93× lower at baseline in the lines without HS3ST1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[TJP2]] | B | HS3ST1 activity raises TJP2's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.29× lower at baseline in the lines without HS3ST1 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[PTK2B]] | B | HS3ST1 activity raises PTK2B's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.43× lower at baseline in the lines without HS3ST1 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[ABHD17C]] | B | HS3ST1 activity raises ABHD17C's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.04× lower at baseline in the lines without HS3ST1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[RDH13]] | B | HS3ST1 activity raises RDH13's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without HS3ST1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[DLG3]] | B | HS3ST1 activity raises DLG3's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.29× lower at baseline in the lines without HS3ST1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[MET]] | B | HS3ST1 activity raises MET's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.52× lower at baseline in the lines without HS3ST1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[PKP2]] | B | HS3ST1 activity raises PKP2's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 4.05× lower at baseline in the lines without HS3ST1 | 0.003 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[SLC25A25]] | B | HS3ST1 activity raises SLC25A25's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.04× lower at baseline in the lines without HS3ST1 | 0.003 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[FAM83E]] | B | HS3ST1 activity raises FAM83E's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.27× lower at baseline in the lines without HS3ST1 | 0.007 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.822). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.7, 54.0); signed map (1.6, 38.6). **Vector** length 85.7, 34.4% of its response variance represented; |z| ≥ 3 in 558 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -6.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.4 | -6.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | heparan sulfate-glucosamine 3-sulfotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.33 — chr4:11,393,150-11,429,564 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 3OST1 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Hallmark sets | HYPOXIA |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O14792](https://www.uniprot.org/uniprotkb/O14792) (Heparan sulfate glucosamine 3-O-sulfotransferase 1):

> Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) to catalyze the transfer of a sulfo group to position 3 of glucosamine residues in heparan. Catalyzes the rate limiting step in the biosynthesis of heparan sulfate (HSact). This modification is a crucial step in the biosynthesis of anticoagulant heparan sulfate as it completes the structure of the antithrombin pentasaccharide binding site.

**Summary**, from NCBI Gene [9957](https://www.ncbi.nlm.nih.gov/gene/9957):

> Heparan sulfate biosynthetic enzymes are key components in generating a myriad of distinct heparan sulfate fine structures that carry out multiple biologic activities. The enzyme encoded by this gene is a member of the heparan sulfate biosynthetic enzyme family. It possesses both heparan sulfate glucosaminyl 3-O-sulfotransferase activity, anticoagulant heparan sulfate conversion activity, and is a rate limiting enzyme for synthesis of anticoagulant heparan. This enzyme is an intraluminal Golgi …

**Accessions** — [HGNC:5194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5194) · Entrez [9957](https://www.ncbi.nlm.nih.gov/gene/9957) · UniProt [O14792](https://www.uniprot.org/uniprotkb/O14792) · Ensembl [ENSG00000002587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000002587)

## Data

Gene col 22: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 22); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 22, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 22]; `tensor/DDL_lfc|DDL_z.npy` [22]; `embed/gene_vectors.npy` [22]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 22 or target_col == 22). Every well: [[HS3ST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HS3ST1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
