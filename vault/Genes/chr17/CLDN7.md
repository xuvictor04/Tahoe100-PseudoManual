---
symbol: "CLDN7"
type: "gene"
col: 11221
ensembl_id: "ENSG00000181885"
name: "claudin 7"
location: "17p13.1"
module: 31
arm: "+"
pooled_cpm: 43.17
n_lines_expressing: 20
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 86
direction_downstream: 113
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# CLDN7

*claudin 7* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.24× (z +9.0, q 1e-16, up in 9 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +5.6, q 4e-06, up in 6 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 3.16×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.665× (z -6.4, q 7e-08, down in 15 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMPRSS4]] (+0.70, fdr 7e-06), [[TACSTD2]] (+0.67, fdr 7e-06), [[RAB25]] (+0.67, fdr 8e-06); moves opposite to [[TMEM80]] (-0.46, fdr 3e-04), [[PSTK]] (-0.46, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 86 arrows point to it, the strongest [[EPS8L1]] → it (grade B ⚠); 113 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11221.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 3.16×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +9.0 | 1e-16 | 9/19 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +7.7 | 4e-12 | 3/16 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.6 | 4e-06 | 6/19 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +5.2 | 2e-05 | 9/18 (SW1417, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +4.3 | 0.002 | 2/16 (SW480, SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.019 | 2/19 (A-427, LS 180) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | 1.33× | +3.2 | 0.11 | 13/18 (HCT15, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.17 | 9/18 (LS 180, COLO 205, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11221.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.665×** | -6.4 | 7e-08 | 15/18 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.557×** | -6.3 | 9e-08 | 13/18 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -6.2 | 1e-07 | 15/18 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.353×** | -6.1 | 2e-07 | 18/18 (A-427, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.649×** | -4.8 | 2e-04 | 12/18 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.501×** | -4.0 | 0.005 | 13/19 (NCI-H2347, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.708×** | -3.9 | 0.009 | 16/18 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.699×** | -3.8 | 0.012 | 14/18 (BT-474, LS 180, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.028 | 17/18 (PANC-1, Panc 03.27, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.738×** | -3.4 | 0.040 | 0/18 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.746×** | -3.3 | 0.056 | 6/18 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.753×** | -3.2 | 0.074 | 10/18 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.758×** | -3.1 | 0.086 | 10/18 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | **0.759×** | -3.1 | 0.087 | 0/18 | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.745×** | -3.0 | 0.091 | 0/18 | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.751×** | -3.0 | 0.091 | 0/18 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 267 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.0) |
| [[PANC-1 (line)]] | alt | 48.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -21.8) |
| [[CFPAC-1 (line)]] | alt | 69.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.3) |
| [[COLO 205 (line)]] | alt | 115 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.6) |
| [[HT-29 (line)]] | alt | 98.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.5) |
| [[LS 180 (line)]] | wt | 200 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 77.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 86.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.5) |
| [[BT-474 (line)]] | alt | 87.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 86.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.3) |
| [[A-427 (line)]] | wt | 27.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0623× (z -9.8) |
| [[HCT15 (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.7) |
| [[LoVo (line)]] | wt | 122 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 62.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0973× (z -9.2) ⚠ toxic |
| [[SW1417 (line)]] | alt | 118 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.381× (z -8.7) |
| [[SW480 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.30 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.44 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.90 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 78.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS4]] | +0.70 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[TACSTD2]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | STRING 966 |
| [[RAB25]] | +0.67 | +0.66 / +0.57 | both halves | 8e-06 | STRING 679 |
| [[CLDN3]] | +0.67 | +0.64 / +0.56 | both halves | 1e-05 | same gene group; pathway: Cell junction organization; STRING 864 |
| [[CEACAM5]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[NECTIN4]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[CLDN4]] | +0.67 | +0.68 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_APICAL_JUNCTION; STRING 953 |
| [[PRSS8]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 | STRING 586 |
| [[SLC44A4]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[GALNT3]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45B]] | +0.66 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[BICDL2]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM80]] | -0.46 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[PSTK]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*86 arrows, 86 of them with an alert ⚠; grade A 0, B 5, C 81. Shown: the 12 strongest; 74 more arrows (74 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | EPS8L1 activity raises CLDN7's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.92× lower at baseline in the lines without EPS8L1 | 0.015 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[TMEM51-AS1]] | B | TMEM51-AS1 activity raises CLDN7's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 3.14× lower at baseline in the lines without TMEM51-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises CLDN7's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.69× lower at baseline in the lines without GPRC5A | 0.055 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[SEMA3B]] | B | SEMA3B activity raises CLDN7's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without SEMA3B | 0.077 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[MYO1D]] | B | MYO1D activity raises CLDN7's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 2.85× lower at baseline in the lines without MYO1D | 0.079 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[TMPRSS4]] | C | TMPRSS4 activity raises CLDN7's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 14.93× lower at baseline in the lines without TMPRSS4 | 5e-06 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[ESRP1]] | C | ESRP1 activity raises CLDN7's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 14.39× lower at baseline in the lines without ESRP1 | 5e-06 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7; co-absent with the target |
| [[ST14]] | C | ST14 activity raises CLDN7's level | lines that do not express ST14 (32) vs lines expressing it (18) | 14.56× lower at baseline in the lines without ST14 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises CLDN7's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 12.35× lower at baseline in the lines without CDH1 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises CLDN7's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 14.24× lower at baseline in the lines without TMEM125 | 4e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[CLDN3]] | C | CLDN3 activity raises CLDN7's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 10.68× lower at baseline in the lines without CLDN3 | 6e-05 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises CLDN7's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 11.83× lower at baseline in the lines without LCN2 | 8e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |

### Downstream of this gene

*113 arrows, 113 of them with an alert ⚠; grade A 0, B 35, C 78. Shown: the 12 strongest; 101 more arrows (101 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | CLDN7 activity raises EPS8L1's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 4.92× lower at baseline in the lines without CLDN7 | 6e-05 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[RASSF7]] | B | CLDN7 activity raises RASSF7's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 2.79× lower at baseline in the lines without CLDN7 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[TMC6]] | B | CLDN7 activity raises TMC6's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 4.49× lower at baseline in the lines without CLDN7 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[FAM83E]] | B | CLDN7 activity raises FAM83E's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 4.31× lower at baseline in the lines without CLDN7 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[ABHD11]] | B | CLDN7 activity raises ABHD11's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 3.10× lower at baseline in the lines without CLDN7 | 0.001 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[MYO1D]] | B | CLDN7 activity raises MYO1D's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 3.67× lower at baseline in the lines without CLDN7 | 0.002 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[RDH13]] | B | CLDN7 activity raises RDH13's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without CLDN7 | 0.002 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[BAIAP2L1]] | B | CLDN7 activity raises BAIAP2L1's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 3.01× lower at baseline in the lines without CLDN7 | 0.004 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[ELMO3]] | B | CLDN7 activity raises ELMO3's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 2.57× lower at baseline in the lines without CLDN7 | 0.004 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[SDCBP2]] | B | CLDN7 activity raises SDCBP2's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 3.97× lower at baseline in the lines without CLDN7 | 0.008 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[SEMA3B]] | B | CLDN7 activity raises SEMA3B's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 3.26× lower at baseline in the lines without CLDN7 | 0.009 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[TMEM51-AS1]] | B | CLDN7 activity raises TMEM51-AS1's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 2.10× lower at baseline in the lines without CLDN7 | 0.020 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.9, 56.8); signed map (58.5, 7.3). **Vector** length 81.8, 34.7% of its response variance represented; |z| ≥ 3 in 477 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.7 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +2.5 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | -0.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.9 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.0 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -6.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | claudin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,259,903-7,263,983 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hs.84359; previously CEPTRL2, CPETRL2 |
| Gene groups (HGNC) | Claudins |
| Hallmark sets | APICAL_JUNCTION, ESTROGEN_RESPONSE_EARLY |
| Reactome | 6 pathways, smallest: Epithelial-Mesenchymal Transition (EMT) during gastrulation; Tight junction interactions; Gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95471](https://www.uniprot.org/uniprotkb/O95471) (Claudin-7):

> Plays a major role in tight junction-specific obliteration of the intercellular space.

**Summary**, from NCBI Gene [1366](https://www.ncbi.nlm.nih.gov/gene/1366):

> This gene encodes a member of the claudin family. Claudins are integral membrane proteins and components of tight junction strands. Tight junction strands serve as a physical barrier to prevent solutes and water from passing freely through the paracellular space between epithelial or endothelial cell sheets, and also play critical roles in maintaining cell polarity and signal transductions. Differential expression of this gene has been observed in different types of malignancies, including …

**Accessions** — [HGNC:2049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2049) · Entrez [1366](https://www.ncbi.nlm.nih.gov/gene/1366) · UniProt [O95471](https://www.uniprot.org/uniprotkb/O95471) · Ensembl [ENSG00000181885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181885)

## Data

Gene col 11221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11221); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11221]; `tensor/DDL_lfc|DDL_z.npy` [11221]; `embed/gene_vectors.npy` [11221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11221 or target_col == 11221). Every well: [[CLDN7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
