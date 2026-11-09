---
symbol: "DCT"
type: "gene"
col: 1274
ensembl_id: "ENSG00000080166"
name: "dopachrome tautomerase"
location: "13q32.1"
module: 9
arm: "+"
pooled_cpm: 12.85
n_lines_expressing: 8
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 20
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# DCT

*dopachrome tautomerase* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 10.7× (z +12.8, q 1e-34, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.35× (z +11.2, q 1e-26, up in 3 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (C32 0.155×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MLANA]] (+0.64, fdr 7e-06), [[GPNMB]] (+0.62, fdr 7e-06), [[CD36]] (+0.57, fdr 1e-05); moves opposite to [[MSRB3-AS1]] (-0.57, fdr 2e-05), [[LINC01812]] (-0.57, fdr 1e-05), [[RHBDF2]] (-0.51, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[COL19A1]] → it (grade C ⚠); 20 go from it, the strongest it → [[HAND2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1274.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **10.7×** | +12.8 | 1e-34 | 3/3 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.35×** | +11.2 | 1e-26 | 3/5 (A498, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.12×** | +10.2 | 4e-22 | 1/2 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.22×** | +8.2 | 2e-14 | 3/3 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.87×** | +7.0 | 3e-10 | 4/4 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.94×** | +5.0 | 5e-05 | 1/4 (SK-MEL-2) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +4.4 | 8e-04 | 2/3 (SK-MEL-2, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.08×** | +3.9 | 0.005 | 1/4 (SK-MEL-2) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.71×** | +3.9 | 0.005 | 3/5 (C32, A498, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.01×** | +3.9 | 0.005 | 2/3 (C32, SK-MEL-2) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.85×** | +3.9 | 0.006 | 2/4 (SK-MEL-2, C32) | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **2.70×** | +3.8 | 0.008 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.7 | 0.008 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.00×** | +3.7 | 0.008 | 0/3 | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +3.6 | 0.012 | 2/5 (SK-MEL-2, A498) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **2.00×** | +3.6 | 0.012 | 1/4 (C32) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.94×** | +3.6 | 0.012 | 3/4 (C32, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.51×** | +3.5 | 0.014 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.82×** | +3.3 | 0.028 | 3/6 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.89×** | +3.3 | 0.028 | 3/4 (SK-MEL-2, C32, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.36×** | +3.3 | 0.028 | 2/3 (C32, SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.65×** | +3.0 | 0.063 | 3/5 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1274.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (C32 0.155×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.535× | -3.1 | 0.58 | 0/5 | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.542× | -3.1 | 0.58 | 1/5 (AN3 CA) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 625 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.155× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2122 (line)]] | alt | 30.9 | 1 | 0 | [[Berbamine (drug)]] 5 µM 6.72× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 9.81× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLANA]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 | pathway: MITF-M-dependent gene expression; STRING 921 |
| [[GPNMB]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 | STRING 471 |
| [[CD36]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CCN3]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[P2RX7]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[SGCD]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[MGP]] | +0.52 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[PDZRN3]] | +0.51 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[COL24A1]] | +0.48 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[SEMA6A]] | +0.48 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[IRF4]] | +0.47 | +0.36 / +0.45 | both halves | 1e-04 | pathway: MITF-M-dependent gene expression |
| [[PRUNE2]] | +0.45 | +0.45 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSRB3-AS1]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 | **novel candidate** |
| [[LINC01812]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[RHBDF2]] | -0.51 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[LEF1-AS1]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[COL19A1]] | -0.46 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[HTR7]] | -0.44 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[RUBCNL]] | -0.44 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[PARVB]] | -0.42 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[ZFYVE28]] | -0.41 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[KCNC4]] | -0.41 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[SH2B3]] | -0.40 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[ITGB3]] | -0.40 | -0.38 / -0.35 | both halves | 1e-04 | pathway: HALLMARK_COAGULATION |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL19A1]] | C | COL19A1 activity raises DCT's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 3.19× lower at baseline in the lines without COL19A1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises DCT's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 2.46× lower at baseline in the lines without MMP2 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises DCT's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.56× lower at baseline in the lines without ITGA4 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises DCT's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 2.70× lower at baseline in the lines without LEF1-AS1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[PRUNE2]] | C | PRUNE2 activity raises DCT's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 2.06× lower at baseline in the lines without PRUNE2 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY; co-absent with the target |
| [[PDZRN3]] | C | PDZRN3 activity raises DCT's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 2.14× lower at baseline in the lines without PDZRN3 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098; co-absent with the target |
| [[NR1H4]] | C | NR1H4 activity raises DCT's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.66× lower at baseline in the lines without NR1H4 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[GASK1B]] | C | GASK1B activity raises DCT's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 1.89× lower at baseline in the lines without GASK1B | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[C10orf90]] | C | C10orf90 activity raises DCT's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 2.79× lower at baseline in the lines without C10orf90 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent; co-absent with the target |
| [[RUBCNL]] | C | RUBCNL activity raises DCT's level | lines that do not express RUBCNL (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without RUBCNL | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01967, LRRN1, CADPS; co-absent with the target |
| [[PHACTR1]] | C | PHACTR1 activity raises DCT's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 2.65× lower at baseline in the lines without PHACTR1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |
| [[CRYAB]] | C | CRYAB activity raises DCT's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without CRYAB | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 5, C 15. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HAND2-AS1]] | B | DCT activity raises HAND2-AS1's level | lines that do not express DCT (42) vs lines expressing it (8) | 2.37× lower at baseline in the lines without DCT | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1 |
| [[CAPN3]] | B | DCT activity raises CAPN3's level | lines that do not express DCT (42) vs lines expressing it (8) | 1.83× lower at baseline in the lines without DCT | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1 |
| [[MLANA]] | B | DCT activity raises MLANA's level | lines that do not express DCT (42) vs lines expressing it (8) | 2.55× lower at baseline in the lines without DCT | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1 |
| [[LDB2]] | B | DCT activity raises LDB2's level | lines that do not express DCT (42) vs lines expressing it (8) | 2.47× lower at baseline in the lines without DCT | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1 |
| [[LINC01170]] | B | DCT activity raises LINC01170's level | lines that do not express DCT (42) vs lines expressing it (8) | 2.23× lower at baseline in the lines without DCT | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1 |
| [[CD36]] | C | DCT activity raises CD36's level | lines that do not express DCT (42) vs lines expressing it (8) | 2.01× lower at baseline in the lines without DCT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[ENPP2]] | C | DCT activity raises ENPP2's level | lines that do not express DCT (42) vs lines expressing it (8) | 5.52× lower at baseline in the lines without DCT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[LEF1]] | C | DCT activity raises LEF1's level | lines that do not express DCT (42) vs lines expressing it (8) | 6.16× lower at baseline in the lines without DCT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[C10orf90]] | C | DCT activity raises C10orf90's level | lines that do not express DCT (42) vs lines expressing it (8) | 4.87× lower at baseline in the lines without DCT | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[COL19A1]] | C | DCT activity raises COL19A1's level | lines that do not express DCT (42) vs lines expressing it (8) | 5.37× lower at baseline in the lines without DCT | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[PDZRN3]] | C | DCT activity raises PDZRN3's level | lines that do not express DCT (42) vs lines expressing it (8) | 5.35× lower at baseline in the lines without DCT | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[LEF1-AS1]] | C | DCT activity raises LEF1-AS1's level | lines that do not express DCT (42) vs lines expressing it (8) | 3.69× lower at baseline in the lines without DCT | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.314). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (55.0, 28.2); signed map (46.3, 29.6). **Vector** length 22.1, 10.3% of its response variance represented; |z| ≥ 3 in 102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.1 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.0 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.7 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.6 | +3.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | -1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | +0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.4 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.4 | +0.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -0.4 | -1.0 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | -0.3 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.3 | -2.1 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.3 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | dopachrome tautomerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.1 — chr13:94,436,811-94,479,682 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRP-2, TRP2; previously TYRP2 |
| Gene groups (HGNC) | Tyrosinase family |
| Hallmark sets | COAGULATION |
| Reactome | 5 pathways, smallest: Melanin biosynthesis; Regulation of MITF-M-dependent genes involved in pigmentation; MITF-M-dependent gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P40126](https://www.uniprot.org/uniprotkb/P40126) (L-dopachrome tautomerase):

> Plays a role in melanin biosynthesis. Catalyzes the conversion of L-dopachrome into 5,6-dihydroxyindole-2-carboxylic acid (DHICA).

**Summary**, from NCBI Gene [1638](https://www.ncbi.nlm.nih.gov/gene/1638):

> Predicted to enable dopachrome isomerase activity. Involved in response to blue light. Located in plasma membrane. Implicated in oculocutaneous albinism. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2709) · Entrez [1638](https://www.ncbi.nlm.nih.gov/gene/1638) · UniProt [P40126](https://www.uniprot.org/uniprotkb/P40126) · Ensembl [ENSG00000080166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080166)

## Data

Gene col 1274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1274); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1274]; `tensor/DDL_lfc|DDL_z.npy` [1274]; `embed/gene_vectors.npy` [1274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1274 or target_col == 1274). Every well: [[DCT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
