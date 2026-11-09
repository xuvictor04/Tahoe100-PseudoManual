---
symbol: "ALDH1A1"
type: "gene"
col: 9065
ensembl_id: "ENSG00000165092"
name: "aldehyde dehydrogenase 1 family member A1"
location: "9q21.13"
module: 19
arm: "+"
pooled_cpm: 56.15
n_lines_expressing: 14
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ALDH1A1

*aldehyde dehydrogenase 1 family member A1* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.37× (z +22.7, q 0e+00, up in 12 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.89× (z +16.0, q 0e+00, up in 7 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Larotrectinib (drug)]] 5 µM: 0.740× (z -4.6, q 0.003, down in 10 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.230×, A-427 0.458×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.320×; ⚠ cell-cycle shift, explains ~99% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.167×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFEMP1]] (+0.63, fdr 1e-05), [[AKR1B10]] (+0.56, fdr 3e-05), [[GASK1B]] (+0.55, fdr 3e-05); moves opposite to [[LAT]] (-0.52, fdr 1e-05), [[TNFRSF10A]] (-0.50, fdr 5e-05), [[PLEKHN1]] (-0.49, fdr 3e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EFEMP1]] → it (grade B ⚠); 10 go from it, the strongest it → [[TOP2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.37×** | +22.7 | 0e+00 | 12/12 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.73×** | +19.6 | 0e+00 | 10/11 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.89×** | +16.0 | 0e+00 | 7/12 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.92×** | +15.7 | 0e+00 | 11/11 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +7.6 | 2e-12 | 8/12 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.4 | 1e-08 | 3/12 (MIA PaCa-2, KATO III, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.2 | 4e-08 | 7/12 (MIA PaCa-2, A549, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.63×** | +5.4 | 5e-06 | 5/9 (A549, A498, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 4e-04 | 8/12 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 5e-04 | 9/12 (MIA PaCa-2, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.49×** | +4.2 | 0.001 | 2/12 (CFPAC-1, MIA PaCa-2) | inconsistent across doses | low cells (technical?); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **2.04×** | +4.0 | 0.003 | 8/12 (HT-29, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.004 | 8/12 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.004 | 9/12 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.013 | 9/12 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.014 | 2/12 (A549, NCI-H460) | inconsistent across doses | position effect removed |
| [[AZD-7648 (drug)]] 5 µM |  | **1.88×** | +3.5 | 0.014 | 6/12 (MIA PaCa-2, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.024 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.024 | 4/12 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.027 | 9/12 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[Posaconazole (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.028 | 0/12 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9065.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.230×, A-427 0.458×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.320×; ⚠ cell-cycle shift, explains ~99% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.167×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Larotrectinib (drug)]] 5 µM |  | **0.740×** | -4.6 | 0.003 | 10/12 (C32, A-427, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -3.6 | 0.086 | 7/12 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.746× | -3.1 | 0.25 | 5/12 (A-427, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.577× | -3.1 | 0.25 | 1/12 (HT-29) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.734× | -3.1 | 0.25 | 0/12 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 81.4 | 9 (6 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.83× (z +18.5) ⚠ position not correctable · without an alert: [[TAK-901 (drug)]] 5 µM 30.7× (z +9.1) | — |
| [[A498 (line)]] | wt | 240 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.24× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +10.8) | — |
| [[A549 (line)]] | wt | 317 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.6× (z +14.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 1,184 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -9.8) ⚠ cell-cycle shift, explains ~99% of this change |
| [[KATO III (line)]] | alt | 26.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -9.4) |
| [[C32 (line)]] | wt | 49.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +10.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 34.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.35 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.16 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.74 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFEMP1]] | +0.63 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[AKR1B10]] | +0.56 | +0.44 / +0.47 | both halves | 3e-05 | STRING 437 |
| [[GASK1B]] | +0.55 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[SH3BGRL]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[MAP2K6]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[OLFML2A]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PBX1]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[AKR1C2]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MORF4L1]] | +0.52 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[DDIT4L]] | +0.51 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TSPAN6]] | +0.51 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[PAX7]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAT]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TNFRSF10A]] | -0.50 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[PLEKHN1]] | -0.49 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[WNT9A]] | -0.49 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[C19orf25]] | -0.49 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[PLEKHM1]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ZNF696]] | -0.47 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[CLCF1]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SLC10A3]] | -0.46 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[AXIN1]] | -0.45 | -0.39 / -0.47 | both halves | 6e-05 | pathway: Signaling by Nuclear Receptors |
| [[ZNF765]] | -0.44 | -0.22 / -0.42 | both halves | 6e-04 |  |
| [[RABIF]] | -0.44 | -0.32 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFEMP1]] | B | EFEMP1 activity lowers ALDH1A1's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.57× higher at baseline in the lines without EFEMP1 | 0.092 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[GASK1B]] | C | GASK1B activity raises ALDH1A1's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 3.80× lower at baseline in the lines without GASK1B | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[LIN7A]] | C | LIN7A activity raises ALDH1A1's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 1.99× lower at baseline in the lines without LIN7A | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[COL5A2]] | C | COL5A2 activity raises ALDH1A1's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without COL5A2 | 0.097 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2B]] | B | ALDH1A1 activity lowers TOP2B's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 1.41× higher at baseline in the lines without ALDH1A1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG |
| [[AKR1C3]] | B | ALDH1A1 activity raises AKR1C3's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 2.75× lower at baseline in the lines without ALDH1A1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG |
| [[TMEM123]] | B | ALDH1A1 activity raises TMEM123's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 1.43× lower at baseline in the lines without ALDH1A1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG |
| [[GASK1B]] | C | ALDH1A1 activity raises GASK1B's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 3.58× lower at baseline in the lines without ALDH1A1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |
| [[AKR1B10]] | C | ALDH1A1 activity raises AKR1B10's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 3.94× lower at baseline in the lines without ALDH1A1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |
| [[SLC40A1]] | C | ALDH1A1 activity raises SLC40A1's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 3.48× lower at baseline in the lines without ALDH1A1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |
| [[MAP2K6]] | C | ALDH1A1 activity raises MAP2K6's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 2.12× lower at baseline in the lines without ALDH1A1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |
| [[CHL1]] | C | ALDH1A1 activity raises CHL1's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 2.15× lower at baseline in the lines without ALDH1A1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |
| [[COL5A2]] | C | ALDH1A1 activity raises COL5A2's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 1.96× lower at baseline in the lines without ALDH1A1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |
| [[AKR1C2]] | C | ALDH1A1 activity raises AKR1C2's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 2.88× lower at baseline in the lines without ALDH1A1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.4, 40.6); signed map (47.7, 44.8). **Vector** length 47.6, 14.8% of its response variance represented; |z| ≥ 3 in 400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +22.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +19.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +15.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 1 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:72,900,671-73,080,442 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RALDH1; previously PUMB1, ALDH1 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, FATTY_ACID_METABOLISM |
| Reactome | 8 pathways, smallest: Fructose metabolism; Ethanol oxidation; RA biosynthesis pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P00352](https://www.uniprot.org/uniprotkb/P00352) (Aldehyde dehydrogenase 1A1):

> Cytosolic dehydrogenase that catalyzes the NAD(+)-dependent irreversible oxidation of a wide range of aldehydes to their corresponding carboxylic acid. Functions downstream of retinol dehydrogenases and catalyzes the oxidation of retinaldehyde into retinoic acid, the second step in the oxidation of retinol/vitamin A into retinoic acid. This pathway is crucial to control the levels of retinol and retinoic acid, two important molecules which excess can be teratogenic and cytotoxic. Also oxidizes …

**Summary**, from NCBI Gene [216](https://www.ncbi.nlm.nih.gov/gene/216):

> The protein encoded by this gene belongs to the aldehyde dehydrogenase family. Aldehyde dehydrogenase is the next enzyme after alcohol dehydrogenase in the major pathway of alcohol metabolism. There are two major aldehyde dehydrogenase isozymes in the liver, cytosolic and mitochondrial, which are encoded by distinct genes, and can be distinguished by their electrophoretic mobility, kinetic properties, and subcellular localization. This gene encodes the cytosolic isozyme. Studies in mice show …

**Accessions** — [HGNC:402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:402) · Entrez [216](https://www.ncbi.nlm.nih.gov/gene/216) · UniProt [P00352](https://www.uniprot.org/uniprotkb/P00352) · Ensembl [ENSG00000165092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165092)

## Data

Gene col 9065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9065); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9065]; `tensor/DDL_lfc|DDL_z.npy` [9065]; `embed/gene_vectors.npy` [9065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9065 or target_col == 9065). Every well: [[ALDH1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
