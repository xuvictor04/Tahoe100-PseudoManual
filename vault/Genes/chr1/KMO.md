---
symbol: "KMO"
type: "gene"
col: 3865
ensembl_id: "ENSG00000117009"
name: "kynurenine 3-monooxygenase"
location: "1q43"
module: 14
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 32
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 26
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# KMO

*kynurenine 3-monooxygenase* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.54× (z +12.8, q 2e-34, up in 17 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.527× (z -4.2, q 0.013, down in 4 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC2A6]] (+0.72, fdr 7e-06), [[PATL2]] (+0.70, fdr 1e-05), [[DUSP16]] (+0.70, fdr 1e-05); moves opposite to [[FBXW2]] (-0.65, fdr 2e-05), [[PYGB]] (-0.62, fdr 1e-05), [[LPCAT4]] (-0.60, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 26 go from it, the strongest it → [[CTSS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.54×** | +12.8 | 2e-34 | 17/20 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.52×** | +12.7 | 2e-34 | 11/18 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.27×** | +10.4 | 7e-23 | 2/8 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.48×** | +10.3 | 1e-22 | 2/6 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.53×** | +9.0 | 2e-17 | 14/18 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.75×** | +8.7 | 3e-16 | 1/6 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.79×** | +5.9 | 3e-07 | 10/28 (PANC-1, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +5.5 | 3e-06 | 3/10 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +5.0 | 4e-05 | 13/22 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.00×** | +4.9 | 5e-05 | 10/25 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +4.3 | 7e-04 | 4/12 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +4.3 | 7e-04 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.82×** | +4.1 | 0.002 | 12/18 (NCI-H2030, NCI-H460, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +3.9 | 0.005 | 4/19 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.006 | 11/29 (A498, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +3.7 | 0.008 | 4/21 (NCI-H460, RPMI-7951, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.015 | 11/29 (NCI-H2030, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.018 | 10/20 (A498, NCI-H2030, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.024 | 2/26 (NCI-H2030, A-172) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +3.3 | 0.025 | 6/10 (NCI-H2030, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.527×** | -4.2 | 0.013 | 4/26 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.598×** | -3.7 | 0.071 | 5/21 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.618× | -3.4 | 0.11 | 6/27 (NCI-H2030, A498, …) | rises with dose |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.640× | -3.2 | 0.21 | 5/28 (A-172, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 27.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 30.5× (z +14.7) | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +9.4) | — |
| [[A-172 (line)]] | wt | 0.904 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.834 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.758 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.716 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.948 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.750 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.704 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.761 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.930 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.644 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.626 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC2A6]] | +0.72 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[PATL2]] | +0.70 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[DUSP16]] | +0.70 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[LITAF]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ZHX2]] | +0.69 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[IL32]] | +0.68 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.68 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[TAPBPL]] | +0.67 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[MYPN]] | +0.67 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.67 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[ARHGAP42]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SYNPO2]] | +0.67 | +0.68 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.65 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[PYGB]] | -0.62 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.60 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[MLX]] | -0.59 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[TBC1D24]] | -0.59 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[LYPLA1]] | -0.59 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[IMPDH1]] | -0.58 | -0.60 / -0.36 | both halves | 9e-05 |  |
| [[BCR]] | -0.58 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[NTAQ1]] | -0.58 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ACTR5]] | -0.58 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[PPM1F]] | -0.58 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[WDR5]] | -0.57 | -0.60 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KMO's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CASC9]] | B | CASC9 activity lowers KMO's level | lines that do not express CASC9 (22) vs lines expressing it (28) | 1.37× higher at baseline in the lines without CASC9 | 0.054 | ⚠ within organs, on part of the lines; also absent: MSLN, LINC00857, SLC38A5 |
| [[RARRES1]] | B | RARRES1 activity raises KMO's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without RARRES1 | 0.092 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[TIMD4]] | B | TIMD4 activity raises KMO's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 1.66× lower at baseline in the lines without TIMD4 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 21, C 5. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | KMO activity raises CTSS's level | lines that do not express KMO (18) vs lines expressing it (32) | 3.11× lower at baseline in the lines without KMO | 0.005 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[HLA-F]] | B | KMO activity raises HLA-F's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.45× lower at baseline in the lines without KMO | 0.006 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[TBC1D24]] | B | KMO activity lowers TBC1D24's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.46× higher at baseline in the lines without KMO | 0.007 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[RBPMS]] | B | KMO activity raises RBPMS's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.77× lower at baseline in the lines without KMO | 0.007 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[STAT6]] | B | KMO activity raises STAT6's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without KMO | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[KIAA1217]] | B | KMO activity raises KIAA1217's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.41× lower at baseline in the lines without KMO | 0.015 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[CXCL3]] | B | KMO activity raises CXCL3's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.56× lower at baseline in the lines without KMO | 0.030 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[ZHX2]] | B | KMO activity raises ZHX2's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.14× lower at baseline in the lines without KMO | 0.037 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[WDR5]] | B | KMO activity lowers WDR5's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.36× higher at baseline in the lines without KMO | 0.038 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[LGALS3]] | B | KMO activity raises LGALS3's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without KMO | 0.038 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[SLC41A2]] | B | KMO activity raises SLC41A2's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without KMO | 0.041 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[FOSL2]] | B | KMO activity raises FOSL2's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without KMO | 0.043 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.4, 19.1); signed map (45.3, 14.6). **Vector** length 49.2, 10.1% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +9.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | kynurenine 3-monooxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:241,532,134-241,595,642 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavoproteins; Oxygenases |
| Reactome | 2 pathways, smallest: Tryptophan catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [O15229](https://www.uniprot.org/uniprotkb/O15229) (Kynurenine 3-monooxygenase):

> Catalyzes the hydroxylation of L-kynurenine (L-Kyn) to form 3-hydroxy-L-kynurenine (L-3OHKyn). Required for synthesis of quinolinic acid, a neurotoxic NMDA receptor antagonist and potential endogenous inhibitor of NMDA receptor signaling in axonal targeting, synaptogenesis and apoptosis during brain development. Quinolinic acid may also affect NMDA receptor signaling in pancreatic beta cells, osteoblasts, myocardial cells, and the gastrointestinal tract (Probable).

**Summary**, from NCBI Gene [8564](https://www.ncbi.nlm.nih.gov/gene/8564):

> This gene encodes a mitochondrion outer membrane protein that catalyzes the hydroxylation of L-tryptophan metabolite, L-kynurenine, to form L-3-hydroxykynurenine. Studies in yeast identified this gene as a therapeutic target for Huntington disease. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:6381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6381) · Entrez [8564](https://www.ncbi.nlm.nih.gov/gene/8564) · UniProt [O15229](https://www.uniprot.org/uniprotkb/O15229) · Ensembl [ENSG00000117009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117009)

## Data

Gene col 3865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3865); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3865]; `tensor/DDL_lfc|DDL_z.npy` [3865]; `embed/gene_vectors.npy` [3865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3865 or target_col == 3865). Every well: [[KMO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KMO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
