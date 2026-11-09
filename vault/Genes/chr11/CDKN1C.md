---
symbol: "CDKN1C"
type: "gene"
col: 5002
ensembl_id: "ENSG00000129757"
name: "cyclin dependent kinase inhibitor 1C"
location: "11p15.4"
module: 74
arm: "+"
pooled_cpm: 6.08
n_lines_expressing: 42
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# CDKN1C

*cyclin dependent kinase inhibitor 1C* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.36× (z +12.0, q 1e-30, up in 26 of 33 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 4.61× (z +8.8, q 3e-16, up in 30 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.293× (z -7.1, q 7e-10, down in 31 of 39 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0707×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CHP-212 0.0323×; ⚠ cell-cycle shift, explains ~60% of this change); [[Nafamostat (mesylate) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0523×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (SW48 0.0323×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID3A]] (+0.69, fdr 1e-05), [[INAFM1]] (+0.68, fdr 7e-06), [[EIF1B]] (+0.67, fdr 7e-06); moves opposite to [[NUP205]] (-0.67, fdr 7e-06), [[XRCC6]] (-0.67, fdr 7e-06), [[NUP155]] (-0.66, fdr 7e-06).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[OVOL1]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Omeprazole (drug)]] 0.05 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **4.36×** | +12.0 | 1e-30 | 26/33 (A498, C32, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.61×** | +8.8 | 3e-16 | 30/37 (SK-MEL-2, SNU-423, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.24×** | +6.8 | 2e-09 | 27/37 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.05×** | +6.5 | 2e-08 | 16/23 (LoVo, HOP62, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.69×** | +5.7 | 1e-06 | 30/39 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.64×** | +5.6 | 2e-06 | 22/34 (SW48, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +5.6 | 2e-06 | 20/34 (A549, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +5.5 | 2e-06 | 5/11 (NCI-H1792, HOP62, …) | two highest doses | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.006 | 19/40 (SW480, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.8 | 0.009 | 12/29 (SW1417, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +3.7 | 0.011 | 19/38 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.92×** | +3.6 | 0.013 | 16/35 (HOP62, A498, …) | rises with dose | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5002.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0707×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CHP-212 0.0323×; ⚠ cell-cycle shift, explains ~60% of this change); [[Nafamostat (mesylate) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0523×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (SW48 0.0323×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.293×** | -7.1 | 7e-10 | 31/39 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.315× | -3.4 | 0.13 | 17/34 (LS 180, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 0.661× | -3.4 | 0.13 | 12/40 (SW1417, A498, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.572× | -3.1 | 0.30 | 13/37 (BT-474, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.89 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.64 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 12.7× (z +10.1) | — |
| [[C32 (line)]] | wt | 2.85 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 39.8× (z +12.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 32.9× (z +8.5) | — |
| [[SW48 (line)]] | wt | 10.2 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 47.0× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0323× (z -8.5) |
| [[A498 (line)]] | wt | 9.24 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +13.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 4.74 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 0.05 µM 0.0523× (z -8.8) |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0323× (z -10.0) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HOP62 (line)]] | alt | 6.80 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +10.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 7.83 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.47× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0766× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 6.81 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +8.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2347 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0707× (z -11.8) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 5.90 | 1 | 0 | [[Auranofin (drug)]] 5 µM 20.6× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 3.90 | 1 | 0 | [[Auranofin (drug)]] 5 µM 26.3× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID3A]] | +0.69 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[EIF1B]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[HDAC5]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.66 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[ZFAND2B]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[GABARAPL2]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[PNRC1]] | +0.62 | +0.64 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[ANKRD12]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[AKAP13-AS1]] | +0.62 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[CDKN2D]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 | pathway: Cyclin D associated events in G1; STRING 878 |
| [[GPX4]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP205]] | -0.67 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[XRCC6]] | -0.67 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[NUP155]] | -0.66 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[MTHFD1]] | -0.65 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[XRCC5]] | -0.64 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[TMX3]] | -0.64 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[RPE]] | -0.63 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.61 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[GOT2]] | -0.61 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[PSME3]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[MRPS27]] | -0.60 | -0.57 / -0.62 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OVOL1]] | B | OVOL1 activity raises CDKN1C's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.66× lower at baseline in the lines without OVOL1 | 0.066 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Omeprazole (drug)]] 0.05 µM | B | CDKN1C activity lowers the cells' numbers under Omeprazole 0.05 µM (makes them more sensitive) | lines that do not express CDKN1C (8) vs lines expressing it (40) | the lines without CDKN1C: 1.24× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: MAP3K9, CARD10, TESMIN; maybe low, not absent |
| [[FOXO3]] | B | CDKN1C activity raises FOXO3's level | lines that do not express CDKN1C (8) vs lines expressing it (42) | 1.11× lower at baseline in the lines without CDKN1C | 0.084 | ⚠ within organs, on part of the lines; also absent: MAP3K9, CARD10, TESMIN; maybe low, not absent |
| [[IPO5]] | B | CDKN1C activity lowers IPO5's level | lines that do not express CDKN1C (8) vs lines expressing it (42) | 1.21× higher at baseline in the lines without CDKN1C | 0.097 | ⚠ within organs, on part of the lines; also absent: MAP3K9, CARD10, TESMIN; maybe low, not absent |
| cells under [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM | B | CDKN1C activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express CDKN1C (8) vs lines expressing it (40) | the lines without CDKN1C: 1.15× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: MAP3K9, CARD10, TESMIN; maybe low, not absent |
| cells under [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM | B | CDKN1C activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CDKN1C (8) vs lines expressing it (40) | the lines without CDKN1C: 1.12× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: MAP3K9, CARD10, TESMIN; maybe low, not absent |

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-31.9, -31.9); signed map (-15.9, 5.0). **Vector** length 84.2, 21.4% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.4 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +3.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.0 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase inhibitor 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:2,883,213-2,885,775 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P57, KIP2; previously BWCR, BWS |
| Gene groups (HGNC) | Cyclin dependent kinase inhibitor 1 family |
| Hallmark sets | TGF_BETA_SIGNALING, UV_RESPONSE_UP, IL2_STAT5_SIGNALING, HYPOXIA |
| Reactome | 9 pathways, smallest: Aberrant regulation of mitotic G1/S transition in cancer due to RB1 defects; Defective binding of RB1 mutants to E2F1,(E2F2, E2F3); Aberrant regulation of mitotic cell cycle due to RB1 defects |
| Matched by | ensembl_id |

**Function**, from UniProt [P49918](https://www.uniprot.org/uniprotkb/P49918) (Cyclin-dependent kinase inhibitor 1C):

> Potent tight-binding inhibitor of several G1 cyclin/CDK complexes (cyclin E-CDK2, cyclin D2-CDK4, and cyclin A-CDK2) and, to lesser extent, of the mitotic cyclin B-CDC2. Negative regulator of cell proliferation. May play a role in maintenance of the non-proliferative state throughout life.

**Summary**, from NCBI Gene [1028](https://www.ncbi.nlm.nih.gov/gene/1028):

> This gene is imprinted, with preferential expression of the maternal allele. The encoded protein is a tight-binding, strong inhibitor of several G1 cyclin/Cdk complexes and a negative regulator of cell proliferation. Mutations in this gene are implicated in sporadic cancers and Beckwith-Wiedemann syndorome, suggesting that this gene is a tumor suppressor candidate. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:1786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1786) · Entrez [1028](https://www.ncbi.nlm.nih.gov/gene/1028) · UniProt [P49918](https://www.uniprot.org/uniprotkb/P49918) · Ensembl [ENSG00000129757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129757)

## Data

Gene col 5002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5002); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5002]; `tensor/DDL_lfc|DDL_z.npy` [5002]; `embed/gene_vectors.npy` [5002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5002 or target_col == 5002). Every well: [[CDKN1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKN1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
