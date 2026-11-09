---
symbol: "BSPRY"
type: "gene"
col: 4065
ensembl_id: "ENSG00000119411"
name: "B-box and SPRY domain containing"
location: "9q32"
module: 8
arm: "+"
pooled_cpm: 8.98
n_lines_expressing: 21
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 60
direction_downstream: 77
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# BSPRY

*B-box and SPRY domain containing* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.14× (z +7.6, q 2e-11, up in 4 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +6.0, q 2e-07, up in 8 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.580× (z -5.7, q 9e-06, down in 18 of 19 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENPP5]] (+0.71, fdr 1e-05), [[LINC03040]] (+0.63, fdr 1e-05), [[TMEM125]] (+0.61, fdr 1e-05); moves opposite to [[SPRY3]] (-0.52, fdr 1e-04), [[UBTF]] (-0.51, fdr 2e-04), [[GTF3C2-AS2]] (-0.49, fdr 4e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 60 arrows point to it, the strongest [[VAV1]] → it (grade B ⚠); 77 go from it, the strongest it → [[ARHGEF16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +7.6 | 2e-11 | 4/11 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +7.2 | 2e-10 | 5/16 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +6.3 | 6e-08 | 3/13 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +6.0 | 2e-07 | 8/19 (SW480, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.0 | 6e-05 | 11/19 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +4.2 | 0.003 | 5/18 (SHP-77, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.029 | 4/19 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.033 | 7/19 (COLO 205, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.061 | 4/18 (LoVo, LS 180, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.061 | 4/19 (COLO 205, NCI-H1573, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.082 | 3/19 (NCI-H23, Panc 03.27, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.1 | 0.086 | 4/18 (SW48, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.092 | 4/19 (LoVo, COLO 205, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.72×** | +3.1 | 0.092 | 3/17 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4065.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.580×** | -5.7 | 9e-06 | 18/19 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.405×** | -4.8 | 4e-04 | 14/19 (LS 180, HCT15, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.635×** | -4.7 | 5e-04 | 18/19 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.033 | 2/19 (CFPAC-1, HEC-1-A) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.717×** | -3.5 | 0.060 | 16/18 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.527×** | -3.4 | 0.060 | 15/18 (HCT15, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.746× | -3.0 | 0.19 | 14/19 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 43.2 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -12.9) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -9.7) |
| [[SW480 (line)]] | alt | 8.23 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0861× (z -14.4) |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0866× (z -11.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 43.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -15.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HT-29 (line)]] | alt | 21.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -12.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[LoVo (line)]] | wt | 15.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 20.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.288× (z -10.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -10.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -11.1) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -14.9) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A-172 (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.715 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.849 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.997 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.989 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENPP5]] | +0.71 | +0.75 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[LINC03040]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[TMEM125]] | +0.61 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CLDN3]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[USH1C]] | +0.59 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[ILDR1]] | +0.58 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ADCY4]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TJP3]] | +0.58 | +0.57 / +0.43 | both halves | 4e-05 |  |
| [[CLDN4]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD22]] | +0.57 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[TMEM45B]] | +0.56 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[CLDN7]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY3]] | -0.52 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[UBTF]] | -0.51 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[GTF3C2-AS2]] | -0.49 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[PHF2]] | -0.48 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[ANTXR1]] | -0.47 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[EFCAB2]] | -0.47 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[PIPOX]] | -0.46 | -0.29 / -0.32 | both halves | 2e-04 |  |
| [[TMEM80]] | -0.44 | -0.40 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[FAM20C]] | -0.44 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[PHF8]] | -0.43 | -0.32 / -0.09 | ⚠ not reproduced | 0.003 |  |
| [[TGFB3]] | -0.43 | -0.17 / -0.30 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 3, C 57. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAV1]] | B | VAV1 activity raises BSPRY's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 2.01× lower at baseline in the lines without VAV1 | 0.083 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[PROM2]] | B | PROM2 activity raises BSPRY's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.55× lower at baseline in the lines without PROM2 | 0.085 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[FAM20C]] | B | FAM20C activity lowers BSPRY's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 3.20× higher at baseline in the lines without FAM20C | 0.089 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[TMEM125]] | C | TMEM125 activity raises BSPRY's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 9.14× lower at baseline in the lines without TMEM125 | 9e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises BSPRY's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 8.14× lower at baseline in the lines without ATP2C2 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises BSPRY's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 8.92× lower at baseline in the lines without RAB25 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises BSPRY's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 7.79× lower at baseline in the lines without MAL2 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises BSPRY's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 7.90× lower at baseline in the lines without CDH1 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises BSPRY's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 7.99× lower at baseline in the lines without TMPRSS4 | 3e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[ST14]] | C | ST14 activity raises BSPRY's level | lines that do not express ST14 (32) vs lines expressing it (18) | 8.01× lower at baseline in the lines without ST14 | 4e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[CLDN3]] | C | CLDN3 activity raises BSPRY's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 6.67× lower at baseline in the lines without CLDN3 | 8e-05 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises BSPRY's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 6.32× lower at baseline in the lines without MPZL2 | 9e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |

### Downstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 21, C 56. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF16]] | B | BSPRY activity raises ARHGEF16's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 3.79× lower at baseline in the lines without BSPRY | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[EDA]] | B | BSPRY activity raises EDA's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 3.06× lower at baseline in the lines without BSPRY | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[ABHD11]] | B | BSPRY activity raises ABHD11's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.63× lower at baseline in the lines without BSPRY | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[PROM2]] | B | BSPRY activity raises PROM2's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.54× lower at baseline in the lines without BSPRY | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[CDK18]] | B | BSPRY activity raises CDK18's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without BSPRY | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[GPR160]] | B | BSPRY activity raises GPR160's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.55× lower at baseline in the lines without BSPRY | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[NSUN7]] | B | BSPRY activity raises NSUN7's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.68× lower at baseline in the lines without BSPRY | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[CATSPER2]] | B | BSPRY activity raises CATSPER2's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 1.68× lower at baseline in the lines without BSPRY | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | BSPRY activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express BSPRY (29) vs lines expressing it (19) | the lines without BSPRY: 1.16× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[VAV1]] | B | BSPRY activity raises VAV1's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 1.94× lower at baseline in the lines without BSPRY | 0.047 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[FUT2]] | B | BSPRY activity raises FUT2's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.04× lower at baseline in the lines without BSPRY | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[CHST9]] | B | BSPRY activity raises CHST9's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 1.33× lower at baseline in the lines without BSPRY | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.0, 54.3); signed map (60.7, 8.6). **Vector** length 53.1, 15.4% of its response variance represented; |z| ≥ 3 in 359 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | B-box and SPRY domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,349,541-113,371,233 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20150 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5W0U4](https://www.uniprot.org/uniprotkb/Q5W0U4) (B box and SPRY domain-containing protein):

> May regulate epithelial calcium transport by inhibiting TRPV5 activity.

**Summary**, from NCBI Gene [54836](https://www.ncbi.nlm.nih.gov/gene/54836):

> Predicted to enable ubiquitin protein ligase activity. Predicted to be involved in innate immune response. Predicted to act upstream of or within cellular response to leukemia inhibitory factor. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18232) · Entrez [54836](https://www.ncbi.nlm.nih.gov/gene/54836) · UniProt [Q5W0U4](https://www.uniprot.org/uniprotkb/Q5W0U4) · Ensembl [ENSG00000119411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119411)

## Data

Gene col 4065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4065); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4065]; `tensor/DDL_lfc|DDL_z.npy` [4065]; `embed/gene_vectors.npy` [4065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4065 or target_col == 4065). Every well: [[BSPRY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BSPRY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
