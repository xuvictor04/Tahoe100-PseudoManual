---
symbol: "GSTM4"
type: "gene"
col: 9693
ensembl_id: "ENSG00000168765"
name: "glutathione S-transferase mu 4"
location: "1p13.3"
module: 45
arm: "+"
pooled_cpm: 3.97
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# GSTM4

*glutathione S-transferase mu 4* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.23× (z +15.1, q 0e+00, up in 7 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.49× (z +4.3, q 0.001, up in 12 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.451× (z -8.7, q 2e-15, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THYN1]] (+0.68, fdr 7e-06), [[GAMT]] (+0.68, fdr 7e-06), [[CYB5A]] (+0.65, fdr 1e-05); moves opposite to [[CDR2]] (-0.56, fdr 4e-05), [[PIGL]] (-0.54, fdr 3e-05), [[NUP50-DT]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FKBP7]] → it (grade B ⚠); 7 go from it, the strongest it → [[SCPEP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.23×** | +15.1 | 0e+00 | 7/8 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +14.4 | 2e-44 | 14/18 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +9.0 | 3e-17 | 9/9 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.77×** | +6.2 | 9e-08 | 15/42 (PANC-1, A498, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.63×** | +5.3 | 2e-05 | 19/42 (PANC-1, NCI-H23, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +4.3 | 0.001 | 12/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.3 | 0.001 | 11/41 (LS 180, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.029 | 6/41 (SK-MEL-2, NCI-H23, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.4 | 0.037 | 1/9 (J82) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.3 | 0.058 | 4/21 (A498, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.3 | 0.058 | 6/44 (NCI-H23, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9693.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.451×** | -8.7 | 2e-15 | 25/41 (SW48, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.527×** | -7.0 | 8e-10 | 23/42 (NCI-H23, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -6.1 | 2e-07 | 17/41 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.593×** | -5.7 | 2e-06 | 15/40 (A-172, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.601×** | -5.6 | 3e-06 | 16/31 (NCI-H2030, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.716×** | -5.2 | 2e-05 | 14/33 (NCI-H2030, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.673×** | -4.3 | 0.001 | 13/30 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.682×** | -4.2 | 0.002 | 11/41 (J82, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.707×** | -3.7 | 0.016 | 11/39 (NCI-H23, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.724×** | -3.5 | 0.022 | 8/42 (H4, HS-578T, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.716×** | -3.5 | 0.022 | 13/37 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.750× | -3.0 | 0.11 | 10/39 (RKO, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.85 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.03× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 4.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0707× (z -9.2) |
| [[LoVo (line)]] | wt | 5.16 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.54× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 6.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 8.20 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -9.5) |
| [[PANC-1 (line)]] | alt | 4.11 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.66× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 8.20 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.108× (z -8.6) |
| [[SW1417 (line)]] | alt | 2.96 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0483× (z -9.4) |
| [[A-172 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THYN1]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[GAMT]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CYB5A]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[CDK5]] | +0.65 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ATP6V0E2]] | +0.65 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[LMBRD1]] | +0.64 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MPP1]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[GSTM2]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 | same gene group; pathway: Biological oxidations; STRING 973; ⚠ same locus (2.5 kb, same strand: neighbours can correlate without regulation) |
| [[ALAD]] | +0.62 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[QPRT]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[EHMT2]] | +0.61 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.59 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PECR]] | +0.59 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDR2]] | -0.56 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PIGL]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NUP50-DT]] | -0.53 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TLNRD1]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[KCNJ14]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[MIRLET7IHG]] | -0.51 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[TAF12]] | -0.50 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[ST3GAL3]] | -0.50 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP7]] | B | FKBP7 activity raises GSTM4's level | lines that do not express FKBP7 (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without FKBP7 | 0.073 | ⚠ within organs, on part of the lines; also absent: C12orf75, KCNC4, MXRA7; maybe low, not absent |
| [[GSTM2]] | C | GSTM2 activity raises GSTM4's level | lines that do not express GSTM2 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without GSTM2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLEC2D, IMPG2, ENSG00000286952; maybe low, not absent; its own permutation p |
| [[SMARCD3]] | C | SMARCD3 activity raises GSTM4's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without SMARCD3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCPEP1]] | C | GSTM4 activity raises SCPEP1's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without GSTM4 | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |
| [[CDR2]] | C | GSTM4 activity lowers CDR2's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.72× higher at baseline in the lines without GSTM4 | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |
| [[ATP5F1C]] | C | GSTM4 activity raises ATP5F1C's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.26× lower at baseline in the lines without GSTM4 | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |
| [[SCRN2]] | C | GSTM4 activity raises SCRN2's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without GSTM4 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |
| [[RBBP9]] | C | GSTM4 activity raises RBBP9's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without GSTM4 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |
| [[LRRC45]] | C | GSTM4 activity raises LRRC45's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without GSTM4 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |
| [[SKP2]] | C | GSTM4 activity raises SKP2's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without GSTM4 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.1, -7.7); signed map (-27.3, -3.5). **Vector** length 46.0, 5.53% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +9.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.6 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | glutathione S-transferase mu 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,656,099-109,665,496 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Soluble glutathione S-transferases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 6 pathways, smallest: Biosynthesis of DHA-derived SPMs; Biosynthesis of specialized proresolving mediators (SPMs); Glutathione conjugation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03013](https://www.uniprot.org/uniprotkb/Q03013) (Glutathione S-transferase Mu 4):

> Conjugation of reduced glutathione to a wide number of exogenous and endogenous hydrophobic electrophiles. Catalyzes the conjugation of leukotriene A4 with reduced glutathione (GSH) to form leukotriene C4. Can also catalyze the transfer of a glutathionyl group from glutathione (GSH) to 13(S),14(S)-epoxy-docosahexaenoic acid to form maresin conjugate in tissue regeneration 1 (MCTR1), a bioactive lipid mediator that possess potent anti-inflammatory and proresolving actions.

**Summary**, from NCBI Gene [2948](https://www.ncbi.nlm.nih.gov/gene/2948):

> Cytosolic and membrane-bound forms of glutathione S-transferase are encoded by two distinct supergene families. At present, eight distinct classes of the soluble cytoplasmic mammalian glutathione S-transferases have been identified: alpha, kappa, mu, omega, pi, sigma, theta and zeta. This gene encodes a glutathione S-transferase that belongs to the mu class. The mu class of enzymes functions in the detoxification of electrophilic compounds, including carcinogens, therapeutic drugs, …

**Accessions** — [HGNC:4636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4636) · Entrez [2948](https://www.ncbi.nlm.nih.gov/gene/2948) · UniProt [Q03013](https://www.uniprot.org/uniprotkb/Q03013) · Ensembl [ENSG00000168765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168765)

## Data

Gene col 9693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9693); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9693]; `tensor/DDL_lfc|DDL_z.npy` [9693]; `embed/gene_vectors.npy` [9693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9693 or target_col == 9693). Every well: [[GSTM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSTM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
