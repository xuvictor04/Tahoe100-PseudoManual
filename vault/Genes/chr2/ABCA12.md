---
symbol: "ABCA12"
type: "gene"
col: 6881
ensembl_id: "ENSG00000144452"
name: "ATP binding cassette subfamily A member 12"
location: "2q35"
module: 62
arm: "+"
pooled_cpm: 4.38
n_lines_expressing: 40
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# ABCA12

*ATP binding cassette subfamily A member 12* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.65× (z +16.7, q 0e+00, up in 17 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.0550×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.262×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.182×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA18]] (+0.78, fdr 7e-06), [[ACTA2]] (+0.73, fdr 7e-06), [[MDM2]] (+0.73, fdr 7e-06); moves opposite to [[KIAA1328]] (-0.56, fdr 1e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC02967]] → it (grade B ⚠); 7 go from it, the strongest it → [[ETS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.65×** | +16.7 | 0e+00 | 17/22 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.47×** | +11.6 | 1e-28 | 19/25 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.55×** | +11.5 | 2e-28 | 2/9 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.85×** | +11.1 | 1e-26 | 3/5 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +9.2 | 5e-18 | 3/6 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.64×** | +8.8 | 1e-16 | 20/30 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.72×** | +7.0 | 3e-10 | 8/33 (A498, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +5.9 | 2e-07 | 9/27 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +5.9 | 3e-07 | 11/33 (LS 180, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +5.8 | 3e-07 | 6/13 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +5.5 | 2e-06 | 16/24 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.81×** | +5.4 | 3e-06 | 13/30 (SW48, A498, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.52×** | +5.4 | 4e-06 | 12/32 (A498, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.2 | 9e-06 | 13/33 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +5.1 | 2e-05 | 12/32 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +5.0 | 2e-05 | 11/26 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +4.6 | 1e-04 | 15/33 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.4 | 3e-04 | 6/18 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +4.3 | 4e-04 | 9/28 (A498, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6881.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.0550×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.262×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.182×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.714× | -3.1 | 0.81 | 2/31 (C-33 A, C32) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.5 | 10 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 10.3× (z +14.6) | — |
| [[COLO 205 (line)]] | alt | 63.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0550× (z -21.7) |
| [[BT-474 (line)]] | alt | 14.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +13.6) | — |
| [[LS 180 (line)]] | wt | 29.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 1.24 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.26× (z +8.6) | [[Vandetanib (drug)]] 5 µM 0.0497× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 3.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +10.1) | — |
| [[LoVo (line)]] | wt | 2.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.64× (z +9.1) | — |
| [[A-172 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.922 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA18]] | +0.78 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ACTA2]] | +0.73 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[MDM2]] | +0.73 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[PINCR]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[TP53I3]] | +0.69 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LACC1]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PHLDA3]] | +0.66 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[DOCK8]] | +0.66 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[PSTPIP2]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DRAM1]] | +0.65 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[FAS]] | +0.65 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[BTG2]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1328]] | -0.56 | -0.52 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02967]] | B | LINC02967 activity raises ABCA12's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 2.80× lower at baseline in the lines without LINC02967 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[TOP2A]] | B | TOP2A activity lowers ABCA12's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PURPL]] | B | PURPL activity strengthens ABCA12's drug response | lines that do not express PURPL (18) vs lines expressing it (15) | the lines without PURPL respond 0.47× as strongly (z diff +1.34); strongest at Idarubicin (hydrochloride) 5 µM: 1.82x vs 6.28x (z diff +5.7) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1; target measured in part of the lines; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens ABCA12's drug response | lines that do not express PINCR (19) vs lines expressing it (14) | the lines without PINCR respond 0.44× as strongly (z diff +1.56); strongest at Idarubicin (hydrochloride) 5 µM: 1.91x vs 5.84x (z diff +5.3) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[FLG-AS1]] | B | FLG-AS1 activity raises ABCA12's level | lines that do not express FLG-AS1 (22) vs lines expressing it (28) | 1.49× lower at baseline in the lines without FLG-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: FLRT2, CNRIP1, MARCHF4 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETS2]] | B | ABCA12 activity raises ETS2's level | lines that do not express ABCA12 (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without ABCA12 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |
| [[MGST2]] | B | ABCA12 activity raises MGST2's level | lines that do not express ABCA12 (10) vs lines expressing it (40) | 1.16× lower at baseline in the lines without ABCA12 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |
| [[GREB1]] | B | ABCA12 activity raises GREB1's level | lines that do not express ABCA12 (10) vs lines expressing it (40) | 1.07× lower at baseline in the lines without ABCA12 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |
| [[CXCL3]] | B | ABCA12 activity raises CXCL3's level | lines that do not express ABCA12 (10) vs lines expressing it (40) | 1.97× lower at baseline in the lines without ABCA12 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |
| [[KITLG]] | B | ABCA12 activity raises KITLG's level | lines that do not express ABCA12 (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without ABCA12 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |
| [[MIR34AHG]] | B | ABCA12 activity raises MIR34AHG's level | lines that do not express ABCA12 (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without ABCA12 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM | B | ABCA12 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ABCA12 (10) vs lines expressing it (38) | the lines without ABCA12: 0.57× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.3, 36.4); signed map (42.4, -23.0). **Vector** length 67.4, 13.8% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.53 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.54 to 6); *apoptosis* (hallmark, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +16.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.4 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +7.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | +0.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:214,931,542-215,138,626 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434G232, LI2; previously ICR2B |
| Gene groups (HGNC) | ATP binding cassette subfamily A; ATPase phospholipid transporting |
| Reactome | 5 pathways, smallest: ABC transporters in lipid homeostasis; ABC transporter disorders; ABC-family protein mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UK0](https://www.uniprot.org/uniprotkb/Q86UK0) (Glucosylceramide transporter ABCA12):

> Transports lipids such as glucosylceramides from the outer to the inner leaflet of lamellar granules (LGs) membrane, whereby the lipids are finally transported to the keratinocyte periphery via the trans-Golgi network and LGs and released to the apical surface of the granular keratinocytes to form lipid lamellae in the stratum corneum of the epidermis, which is essential for skin barrier function. In the meantime, participates in the transport of the lamellar granules-associated proteolytic …

**Summary**, from NCBI Gene [26154](https://www.ncbi.nlm.nih.gov/gene/26154):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intracellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, and White). This encoded protein is a member of the ABC1 subfamily, which is the only major ABC subfamily found exclusively in multicellular eukaryotes. Alternative splicing of this gene results …

**Accessions** — [HGNC:14637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14637) · Entrez [26154](https://www.ncbi.nlm.nih.gov/gene/26154) · UniProt [Q86UK0](https://www.uniprot.org/uniprotkb/Q86UK0) · Ensembl [ENSG00000144452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144452)

## Data

Gene col 6881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6881); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6881]; `tensor/DDL_lfc|DDL_z.npy` [6881]; `embed/gene_vectors.npy` [6881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6881 or target_col == 6881). Every well: [[ABCA12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
