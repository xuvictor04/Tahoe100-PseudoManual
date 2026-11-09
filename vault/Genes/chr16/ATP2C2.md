---
symbol: "ATP2C2"
type: "gene"
col: 741
ensembl_id: "ENSG00000064270"
name: "ATPase secretory pathway Ca2+ transporting 2"
location: "16q24.1"
module: 31
arm: "+"
pooled_cpm: 26.2
n_lines_expressing: 18
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 50
direction_downstream: 90
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ATP2C2

*ATPase secretory pathway Ca2+ transporting 2* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.66× (z +13.6, q 1e-39, up in 1 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.61× (z +9.5, q 6e-19, up in 12 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.616× (z -6.2, q 2e-07, down in 4 of 15 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTGS1]] (+0.63, fdr 1e-05), [[SLC5A1]] (+0.63, fdr 1e-05), [[ACOT11]] (+0.60, fdr 1e-05); moves opposite to [[PLBD1-AS1]] (-0.45, fdr 2e-04), [[TMEM80]] (-0.45, fdr 4e-04), [[FOXA1]] (-0.45, fdr 5e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 50 arrows point to it, the strongest [[LMTK3]] → it (grade B ⚠); 90 go from it, the strongest it → [[ARHGEF16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +13.6 | 1e-39 | 1/16 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +9.5 | 6e-19 | 12/16 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +9.5 | 6e-19 | 2/17 (BT-474, HCT15) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +7.3 | 6e-11 | 11/15 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +5.9 | 4e-07 | 10/16 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +5.5 | 4e-06 | 3/16 (BT-474, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +5.0 | 4e-05 | 0/15 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.43×** | +5.0 | 4e-05 | 11/15 (SW1417, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 5e-04 | 0/15 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.35×** | +4.1 | 0.003 | 1/13 (NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.9 | 0.004 | 2/15 (NCI-H2347, SW480) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +3.9 | 0.005 | 1/16 (BT-474) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.011 | 11/15 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.030 | 0/16 | all doses, flat | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.27×** | +3.3 | 0.042 | 1/15 (NCI-H2347) | rises with dose |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.059 | 0/15 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.067 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.085 | 0/15 | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.090 | 0/16 | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 741.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.616×** | -6.2 | 2e-07 | 4/15 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.682×** | -5.3 | 3e-05 | 6/15 (HEC-1-A, NCI-H1573, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.734×** | -4.3 | 0.003 | 10/15 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.753×** | -4.0 | 0.009 | 6/15 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.754×** | -3.9 | 0.009 | 10/15 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.756×** | -3.9 | 0.009 | 10/15 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.818×** | -3.9 | 0.009 | 3/16 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.825×** | -3.8 | 0.010 | 10/16 (KATO III, HT-29, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.772×** | -3.6 | 0.020 | 10/15 (NCI-H1573, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.768×** | -3.4 | 0.035 | 0/15 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.784×** | -3.4 | 0.035 | 4/15 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.771×** | -3.4 | 0.038 | 3/17 (CFPAC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.849× | -3.2 | 0.056 | 13/16 (COLO 205, LS 180, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.799×** | -3.1 | 0.070 | 0/16 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0561× (z -24.2) |
| [[COLO 205 (line)]] | alt | 388 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 57.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -11.0) |
| [[KATO III (line)]] | alt | 81.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -13.3) |
| [[SW1417 (line)]] | alt | 24.3 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.01× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.77× (z +9.3) | — |
| [[LoVo (line)]] | wt | 14.4 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.29× (z +10.6) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.13× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 84.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +16.1) | — |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -11.7) |
| [[HT-29 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.321× (z -8.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 27.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -8.6) |
| [[SW480 (line)]] | alt | 9.10 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.98× (z +10.1) | — |
| [[A-172 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.73 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 716 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGS1]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SLC5A1]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ACOT11]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TLDC2]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[MCF2L]] | +0.59 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[FA2H]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TMEM125]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LASTR]] | +0.57 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[TMEM92]] | +0.57 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[LMTK3]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[LINC00659]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[CDH1]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLBD1-AS1]] | -0.45 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[TMEM80]] | -0.45 | -0.37 / -0.25 | both halves | 4e-04 |  |
| [[FOXA1]] | -0.45 | -0.48 / -0.23 | both halves | 5e-04 |  |
| [[CXCL16]] | -0.43 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[MIER3]] | -0.42 | -0.41 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 2, C 48. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | LMTK3 activity raises ATP2C2's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.54× lower at baseline in the lines without LMTK3 | 0.027 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[LYPD3]] | B | LYPD3 activity raises ATP2C2's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.64× lower at baseline in the lines without LYPD3 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[TMPRSS4]] | C | TMPRSS4 activity raises ATP2C2's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 11.81× lower at baseline in the lines without TMPRSS4 | 2e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises ATP2C2's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 12.56× lower at baseline in the lines without TMEM125 | 4e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[ANKRD22]] | C | ANKRD22 activity raises ATP2C2's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 10.19× lower at baseline in the lines without ANKRD22 | 6e-05 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises ATP2C2's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 9.62× lower at baseline in the lines without CDH1 | 9e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[FUT3]] | C | FUT3 activity raises ATP2C2's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 7.48× lower at baseline in the lines without FUT3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004; co-absent with the target |
| [[PRSS8]] | C | PRSS8 activity raises ATP2C2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 10.52× lower at baseline in the lines without PRSS8 | 1e-04 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2; co-absent with the target |
| [[ESRP1]] | C | ESRP1 activity raises ATP2C2's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 9.73× lower at baseline in the lines without ESRP1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7; co-absent with the target |
| [[B3GNT3]] | C | B3GNT3 activity raises ATP2C2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 6.84× lower at baseline in the lines without B3GNT3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises ATP2C2's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 7.67× lower at baseline in the lines without BSPRY | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[SLC5A1]] | C | SLC5A1 activity raises ATP2C2's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 10.36× lower at baseline in the lines without SLC5A1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125; co-absent with the target |

### Downstream of this gene

*90 arrows, 90 of them with an alert ⚠; grade A 0, B 42, C 48. Shown: the 12 strongest; 78 more arrows (78 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF16]] | B | ATP2C2 activity raises ARHGEF16's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.54× lower at baseline in the lines without ATP2C2 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[TMC6]] | B | ATP2C2 activity raises TMC6's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 4.36× lower at baseline in the lines without ATP2C2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[SYTL1]] | B | ATP2C2 activity raises SYTL1's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.19× lower at baseline in the lines without ATP2C2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[PTK2B]] | B | ATP2C2 activity raises PTK2B's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.24× lower at baseline in the lines without ATP2C2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[RDH13]] | B | ATP2C2 activity raises RDH13's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.61× lower at baseline in the lines without ATP2C2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[MROH7]] | B | ATP2C2 activity raises MROH7's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.80× lower at baseline in the lines without ATP2C2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[ACOT11]] | B | ATP2C2 activity raises ACOT11's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.15× lower at baseline in the lines without ATP2C2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[PTK6]] | B | ATP2C2 activity raises PTK6's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.13× lower at baseline in the lines without ATP2C2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | ATP2C2 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.19× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[TLDC2]] | B | ATP2C2 activity raises TLDC2's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without ATP2C2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[PKP2]] | B | ATP2C2 activity raises PKP2's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 4.14× lower at baseline in the lines without ATP2C2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[SLC25A25]] | B | ATP2C2 activity raises SLC25A25's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.12× lower at baseline in the lines without ATP2C2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.7, 52.8); signed map (60.7, 10.7). **Vector** length 78.0, 28.9% of its response variance represented; |z| ≥ 3 in 554 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +2.9 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +4.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.9 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -6.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -2.4 | -3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ATPase secretory pathway Ca2+ transporting 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:84,368,527-84,464,187 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0703, SPCA2 |
| Gene groups (HGNC) | ATPases Ca2+ transporting |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O75185](https://www.uniprot.org/uniprotkb/O75185) (Calcium-transporting ATPase type 2C member 2):

> ATP-driven pump that supplies the Golgi apparatus with Ca(2+) and Mn(2+) ions, both essential cofactors for processing and trafficking of newly synthesized proteins in the secretory pathway. Within a catalytic cycle, acquires Ca(2+) or Mn(2+) ions on the cytoplasmic side of the membrane and delivers them to the lumenal side. The transfer of ions across the membrane is coupled to ATP hydrolysis and is associated with a transient phosphorylation that shifts the pump conformation from …

**Summary**, from NCBI Gene [9914](https://www.ncbi.nlm.nih.gov/gene/9914):

> Enables P-type calcium transporter activity and P-type manganese transporter activity. Predicted to be involved in calcium ion transmembrane transport; intracellular calcium ion homeostasis; and manganese ion transport. Predicted to act upstream of or within mammary gland epithelium development; positive regulation of calcium ion import; and protein localization to plasma membrane. Predicted to be located in trans-Golgi network membrane. Predicted to be active in Golgi membrane; endoplasmic …

**Accessions** — [HGNC:29103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29103) · Entrez [9914](https://www.ncbi.nlm.nih.gov/gene/9914) · UniProt [O75185](https://www.uniprot.org/uniprotkb/O75185) · Ensembl [ENSG00000064270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064270)

## Data

Gene col 741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 741); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 741]; `tensor/DDL_lfc|DDL_z.npy` [741]; `embed/gene_vectors.npy` [741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 741 or target_col == 741). Every well: [[ATP2C2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP2C2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
