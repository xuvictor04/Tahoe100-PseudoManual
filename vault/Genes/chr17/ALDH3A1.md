---
symbol: "ALDH3A1"
type: "gene"
col: 2976
ensembl_id: "ENSG00000108602"
name: "aldehyde dehydrogenase 3 family member A1"
location: "17p11.2"
module: 44
arm: "+"
pooled_cpm: 11.99
n_lines_expressing: 14
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 17
direction_downstream: 20
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# ALDH3A1

*aldehyde dehydrogenase 3 family member A1* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 10.4× (z +13.0, q 6e-36, up in 7 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +5.3, q 2e-05, up in 2 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0379×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.0769×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKR1B10]] (+0.69, fdr 1e-05), [[TSPAN8]] (+0.64, fdr 1e-05), [[UGT1A1]] (+0.63, fdr 1e-05); moves opposite to [[CTSL]] (-0.41, fdr 3e-04), [[CEP104]] (-0.40, fdr 7e-05), [[DDN-AS1]] (-0.40, fdr 2e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[AKR1C3]] → it (grade B ⚠); 20 go from it, the strongest it → cells under [[Afatinib (drug)]] 0.05 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **10.4×** | +13.0 | 6e-36 | 7/8 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.87×** | +11.0 | 8e-26 | 4/4 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.18×** | +9.4 | 2e-18 | 6/7 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +5.3 | 2e-05 | 2/10 (A549, AsPC-1) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +4.6 | 6e-04 | 3/9 (NCI-H1573, LS 180, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **3.93×** | +3.9 | 0.007 | 6/9 (KATO III, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **3.89×** | +3.9 | 0.007 | 8/10 (NCI-H1573, KATO III, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.96×** | +3.7 | 0.013 | 0/11 | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **2.00×** | +3.7 | 0.013 | 5/10 (NCI-H1573, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.95×** | +3.7 | 0.013 | 2/9 (Hs 766T, A549) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **3.46×** | +3.6 | 0.018 | 0/6 | rises with dose | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.54×** | +3.3 | 0.040 | 9/12 (Hs 766T, KATO III, …) | top dose only | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.3 | 0.044 | 1/11 (AsPC-1) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.87×** | +3.3 | 0.044 | 5/12 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 5 µM |  | **2.14×** | +3.1 | 0.073 | 7/11 (LS 180, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **2.13×** | +3.0 | 0.099 | 6/12 (COLO 205, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2976.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0379×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.0769×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | 0.326× | -3.3 | 0.43 | 6/12 (Hs 766T, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | 0.558× | -3.1 | 0.43 | 8/12 (KATO III, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.351× | -3.0 | 0.43 | 6/12 (Hs 766T, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 8.70 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.1× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 69.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0379× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.726 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 171 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1B10]] | +0.69 | +0.75 / +0.54 | both halves | 1e-05 | STRING 717 |
| [[TSPAN8]] | +0.64 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[UGT1A1]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 | pathway: Biological oxidations; STRING 447 |
| [[LYZ]] | +0.62 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[FXYD3]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ST6GALNAC1]] | +0.60 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[TM4SF4]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PRR15]] | +0.59 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R1B]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[GPX2]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 | STRING 509 |
| [[MUC5B]] | +0.57 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[LGALS4]] | +0.55 | +0.58 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSL]] | -0.41 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[CEP104]] | -0.40 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[DDN-AS1]] | -0.40 | -0.43 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 1, C 16. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C3]] | B | AKR1C3 activity raises ALDH3A1's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without AKR1C3 | 0.057 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[CYP4F12]] | C | CYP4F12 activity raises ALDH3A1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.23× lower at baseline in the lines without CYP4F12 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises ALDH3A1's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 4.18× lower at baseline in the lines without PLA2G2A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[LINC00589]] | C | LINC00589 activity raises ALDH3A1's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 2.98× lower at baseline in the lines without LINC00589 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8; co-absent with the target |
| [[AKR1B10]] | C | AKR1B10 activity raises ALDH3A1's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 4.52× lower at baseline in the lines without AKR1B10 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[TSPAN8]] | C | TSPAN8 activity raises ALDH3A1's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 4.35× lower at baseline in the lines without TSPAN8 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17; co-absent with the target |
| [[AGR2]] | C | AGR2 activity raises ALDH3A1's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 4.08× lower at baseline in the lines without AGR2 | 0.048 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1; co-absent with the target |
| [[POF1B]] | C | POF1B activity raises ALDH3A1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 3.57× lower at baseline in the lines without POF1B | 0.049 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31; co-absent with the target |
| [[PRR15]] | C | PRR15 activity raises ALDH3A1's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.91× lower at baseline in the lines without PRR15 | 0.054 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C; co-absent with the target |
| [[ZBTB7C]] | C | ZBTB7C activity raises ALDH3A1's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 1.94× lower at baseline in the lines without ZBTB7C | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |
| [[SULF2]] | C | SULF2 activity raises ALDH3A1's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.26× lower at baseline in the lines without SULF2 | 0.057 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1; co-absent with the target |
| [[MUC5AC]] | C | MUC5AC activity raises ALDH3A1's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.43× lower at baseline in the lines without MUC5AC | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 6, C 14. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Afatinib (drug)]] 0.05 µM | B | ALDH3A1 activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express ALDH3A1 (36) vs lines expressing it (12) | the lines without ALDH3A1: 1.12× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1 |
| [[CD70]] | B | ALDH3A1 activity raises CD70's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 1.67× lower at baseline in the lines without ALDH3A1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1 |
| cells under [[Benproperine (phosphate) (drug)]] 0.05 µM | B | ALDH3A1 activity raises the cells' numbers under Benproperine (phosphate) 0.05 µM (protects the cells) | lines that do not express ALDH3A1 (36) vs lines expressing it (12) | the lines without ALDH3A1: 0.85× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1 |
| [[MGST2]] | B | ALDH3A1 activity raises MGST2's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 2.39× lower at baseline in the lines without ALDH3A1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1 |
| [[ABCG2]] | B | ALDH3A1 activity raises ABCG2's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 1.50× lower at baseline in the lines without ALDH3A1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1 |
| cells under [[BAY1125976 (drug)]] 0.5 µM | B | ALDH3A1 activity lowers the cells' numbers under BAY1125976 0.5 µM (makes them more sensitive) | lines that do not express ALDH3A1 (36) vs lines expressing it (12) | the lines without ALDH3A1: 1.30× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1 |
| [[AGR2]] | C | ALDH3A1 activity raises AGR2's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 6.76× lower at baseline in the lines without ALDH3A1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1; co-absent with the target |
| [[NPNT]] | C | ALDH3A1 activity raises NPNT's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 4.44× lower at baseline in the lines without ALDH3A1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1; co-absent with the target |
| [[LINC00589]] | C | ALDH3A1 activity raises LINC00589's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 3.53× lower at baseline in the lines without ALDH3A1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1; co-absent with the target |
| [[AKR1B10]] | C | ALDH3A1 activity raises AKR1B10's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 2.54× lower at baseline in the lines without ALDH3A1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1; co-absent with the target |
| [[MUC5B]] | C | ALDH3A1 activity raises MUC5B's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 2.84× lower at baseline in the lines without ALDH3A1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1; co-absent with the target |
| [[MUC5AC]] | C | ALDH3A1 activity raises MUC5AC's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 4.33× lower at baseline in the lines without ALDH3A1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.6, 51.1); signed map (64.4, 4.8). **Vector** length 42.4, 13.9% of its response variance represented; |z| ≥ 3 in 347 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.51 to 4); *Aspirin ADME* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +11.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | -0.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +2.6 |
|  | [[Arbutin (drug)]] 5 µM |  | +0.8 | +2.4 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.3 | -2.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.1 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -0.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 3 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:19,737,984-19,748,943 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ALDH3 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM |
| Reactome | 2 pathways, smallest: Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P30838](https://www.uniprot.org/uniprotkb/P30838) (Aldehyde dehydrogenase 3A1):

> Cytosolic aldehyde dehydrogenase that catalyzes the oxidation of aldehydes to their corresponding carboxylic acids, preferentially using NAD+ but also accepting NADP+ as cofactor, with a strong preference for medium- and long-chain saturated and unsaturated aliphatic aldehydes. In the corneal epithelium, contributes to protection against UV-induced oxidative damage by metabolizing toxic lipid peroxidation-derived aldehydes, including 4-hydroxy-2-nonenal (4-HNE) and malondialdehyde. In addition …

**Summary**, from NCBI Gene [218](https://www.ncbi.nlm.nih.gov/gene/218):

> Aldehyde dehydrogenases oxidize various aldehydes to the corresponding acids. They are involved in the detoxification of alcohol-derived acetaldehyde and in the metabolism of corticosteroids, biogenic amines, neurotransmitters, and lipid peroxidation. The enzyme encoded by this gene forms a cytoplasmic homodimer that preferentially oxidizes aromatic and medium-chain (6 carbons or more) saturated and unsaturated aldehyde substrates. It is thought to promote resistance to UV and …

**Accessions** — [HGNC:405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:405) · Entrez [218](https://www.ncbi.nlm.nih.gov/gene/218) · UniProt [P30838](https://www.uniprot.org/uniprotkb/P30838) · Ensembl [ENSG00000108602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108602)

## Data

Gene col 2976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2976); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2976]; `tensor/DDL_lfc|DDL_z.npy` [2976]; `embed/gene_vectors.npy` [2976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2976 or target_col == 2976). Every well: [[ALDH3A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH3A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
