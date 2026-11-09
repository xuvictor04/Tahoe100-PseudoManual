---
symbol: "SMIM2-AS1"
type: "gene"
col: 13581
ensembl_id: "ENSG00000227258"
name: "SMIM2 antisense RNA 1"
location: "13q14.11"
module: 8
arm: "+"
pooled_cpm: 21.51
n_lines_expressing: 13
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 40
direction_downstream: 69
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SMIM2-AS1

*SMIM2 antisense RNA 1* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.77× (z +8.0, q 5e-13, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +7.9, q 9e-13, up in 2 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.451× (z -6.2, q 2e-07, down in 7 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF183]] (+0.80, fdr 7e-06), [[ATP10B]] (+0.72, fdr 9e-06), [[BCL2L15]] (+0.72, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[DIRC3]] → it (grade B ⚠); 69 go from it, the strongest it → [[RSPH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13581.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +8.0 | 5e-13 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +7.9 | 9e-13 | 2/11 (LoVo, KATO III) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +5.8 | 1e-06 | 1/9 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +4.7 | 3e-04 | 4/11 (A549, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +4.5 | 6e-04 | 7/10 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +4.2 | 0.003 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.69× | +3.1 | 0.17 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.451×** | -6.2 | 2e-07 | 7/10 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.467×** | -6.2 | 2e-07 | 7/10 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.600×** | -4.1 | 0.006 | 8/10 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.729×** | -3.6 | 0.041 | 6/10 (C32, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.655× | -3.2 | 0.13 | 0/10 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.687× | -3.0 | 0.18 | 1/10 (HT-29) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.690× | -3.0 | 0.18 | 1/10 (CFPAC-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 1,410 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0195× (z -40.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0697× (z -19.1) |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0675× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0501× (z -9.9) |
| [[A-172 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF183]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ATP10B]] | +0.72 | +0.82 / +0.57 | both halves | 9e-06 |  |
| [[BCL2L15]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[HNF1A-AS1]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 | same gene group |
| [[ARSL]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[BCAS1]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[TMEM51-AS1]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | same gene group |
| [[UNC5CL]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[FMO5]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TRIM31]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SPATA6L]] | +0.62 | +0.51 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 1, C 39. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIRC3]] | B | DIRC3 activity raises SMIM2-AS1's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without DIRC3 | 0.054 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[TCN1]] | C | TCN1 activity raises SMIM2-AS1's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 3.25× lower at baseline in the lines without TCN1 | 0.004 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises SMIM2-AS1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 5.82× lower at baseline in the lines without AGR3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises SMIM2-AS1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.22× lower at baseline in the lines without MUC5B | 0.005 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[MMP7]] | C | MMP7 activity raises SMIM2-AS1's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.98× lower at baseline in the lines without MMP7 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises SMIM2-AS1's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 3.70× lower at baseline in the lines without PLA2G2A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises SMIM2-AS1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.45× lower at baseline in the lines without IGFBP1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises SMIM2-AS1's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.08× lower at baseline in the lines without TNFRSF14-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |
| [[RNF183]] | C | RNF183 activity raises SMIM2-AS1's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 3.08× lower at baseline in the lines without RNF183 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1; co-absent with the target |
| [[SERPINA3]] | C | SERPINA3 activity raises SMIM2-AS1's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 1.43× lower at baseline in the lines without SERPINA3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |
| [[SLC28A3]] | C | SLC28A3 activity raises SMIM2-AS1's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.41× lower at baseline in the lines without SLC28A3 | 0.013 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14; co-absent with the target |
| [[ATP10B]] | C | ATP10B activity raises SMIM2-AS1's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 5.10× lower at baseline in the lines without ATP10B | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 15, C 54. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSPH1]] | B | SMIM2-AS1 activity raises RSPH1's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.11× lower at baseline in the lines without SMIM2-AS1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[PPP1R3B-DT]] | B | SMIM2-AS1 activity raises PPP1R3B-DT's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 3.17× lower at baseline in the lines without SMIM2-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[PLCH1]] | B | SMIM2-AS1 activity raises PLCH1's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.70× lower at baseline in the lines without SMIM2-AS1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[LINC01504]] | B | SMIM2-AS1 activity raises LINC01504's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 1.64× lower at baseline in the lines without SMIM2-AS1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[CARD14]] | B | SMIM2-AS1 activity raises CARD14's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 1.96× lower at baseline in the lines without SMIM2-AS1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[MUC12]] | B | SMIM2-AS1 activity raises MUC12's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.23× lower at baseline in the lines without SMIM2-AS1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[C4orf19]] | B | SMIM2-AS1 activity raises C4orf19's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.78× lower at baseline in the lines without SMIM2-AS1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[FZD5]] | B | SMIM2-AS1 activity raises FZD5's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 1.65× lower at baseline in the lines without SMIM2-AS1 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[TMEM51-AS1]] | B | SMIM2-AS1 activity raises TMEM51-AS1's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.20× lower at baseline in the lines without SMIM2-AS1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[UNC5CL]] | B | SMIM2-AS1 activity raises UNC5CL's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 1.79× lower at baseline in the lines without SMIM2-AS1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[BCL2L15]] | B | SMIM2-AS1 activity raises BCL2L15's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.37× lower at baseline in the lines without SMIM2-AS1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[PROM2]] | B | SMIM2-AS1 activity raises PROM2's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 1.97× lower at baseline in the lines without SMIM2-AS1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.3, 53.1); signed map (60.6, -0.2). **Vector** length 47.6, 19.6% of its response variance represented; |z| ≥ 3 in 274 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +1.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -1.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -0.9 | -2.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | SMIM2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q14.11 — chr13:44,110,451-44,240,517 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C13orf44-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42674) · Entrez [101929212](https://www.ncbi.nlm.nih.gov/gene/101929212) · Ensembl [ENSG00000227258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227258)

## Data

Gene col 13581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13581); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13581]; `tensor/DDL_lfc|DDL_z.npy` [13581]; `embed/gene_vectors.npy` [13581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13581 or target_col == 13581). Every well: [[SMIM2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
