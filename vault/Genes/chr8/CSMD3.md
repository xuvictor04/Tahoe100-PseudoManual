---
symbol: "CSMD3"
type: "gene"
col: 9007
ensembl_id: "ENSG00000164796"
name: "CUB and Sushi multiple domains 3"
location: "8q23.3"
module: 9
arm: "+"
pooled_cpm: 33.71
n_lines_expressing: 14
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 28
direction_downstream: 46
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CSMD3

*CUB and Sushi multiple domains 3* — 8q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.31× (z +20.5, q 0e+00, up in 0 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.693× (z -4.1, q 0.020, down in 2 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 20 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.150×, SHP-77 0.225×, SW480 0.353×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.0659×, SK-MEL-2 0.0392×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.233×, A-427 0.218×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.116×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCSK1]] (+0.75, fdr 7e-06), [[ARHGAP25]] (+0.69, fdr 7e-06), [[RMST]] (+0.66, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 46 go from it, the strongest it → [[RBM20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.31×** | +20.5 | 0e+00 | 0/12 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +11.5 | 6e-28 | 1/10 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.37×** | +10.5 | 2e-23 | 3/12 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +10.1 | 8e-22 | 1/10 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +10.0 | 2e-21 | 4/12 (NCI-H23, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +9.3 | 1e-18 | 6/12 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +8.9 | 6e-17 | 1/10 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +7.6 | 2e-12 | 1/11 (NCI-H23) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.2 | 5e-11 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +6.9 | 3e-10 | 5/11 (NCI-H23, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.5 | 5e-09 | 4/12 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.005 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.8 | 0.007 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.7 | 0.010 | 0/11 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.011 | 0/11 | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.018 | 8/12 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9007.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 20 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.150×, SHP-77 0.225×, SW480 0.353×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.0659×, SK-MEL-2 0.0392×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.233×, A-427 0.218×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.693×** | -4.1 | 0.020 | 2/12 (SW480, SW1417) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.751× | -3.2 | 0.36 | 0/12 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 74.6 | 0 | 21 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 454 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0659× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -21.6) |
| [[A-427 (line)]] | wt | 165 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +14.1) | [[Auranofin (drug)]] 5 µM 0.218× (z -9.9) |
| [[SHP-77 (line)]] | alt | 156 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 120 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0392× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 155 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 9.09 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.51× (z +9.4) | — |
| [[A-172 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.31 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.90 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 415 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCSK1]] | +0.75 | +0.77 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP25]] | +0.69 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[RMST]] | +0.66 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[KCNB2]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CDH10]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 | STRING 432 |
| [[NELL2]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[GABRG2]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ST18]] | +0.64 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[GRIA2]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[LINC02197]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[RUNX1T1]] | +0.61 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[ASCL1]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 1, C 27. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CSMD3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ASCL1]] | C | ASCL1 activity raises CSMD3's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 7.46× lower at baseline in the lines without ASCL1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[ROBO2]] | C | ROBO2 activity raises CSMD3's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 6.72× lower at baseline in the lines without ROBO2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises CSMD3's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 3.62× lower at baseline in the lines without FUT9 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises CSMD3's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 4.48× lower at baseline in the lines without KCNH5 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[COLGALT2]] | C | COLGALT2 activity raises CSMD3's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 2.99× lower at baseline in the lines without COLGALT2 | 0.025 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises CSMD3's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 3.27× lower at baseline in the lines without GABRG2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises CSMD3's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.31× lower at baseline in the lines without KCNH7 | 0.027 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises CSMD3's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 3.97× lower at baseline in the lines without CDH10 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises CSMD3's level | lines that do not express BCHE (35) vs lines expressing it (15) | 4.77× lower at baseline in the lines without BCHE | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises CSMD3's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.53× lower at baseline in the lines without RUNX1T1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[MIR2052HG]] | C | MIR2052HG activity raises CSMD3's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without MIR2052HG | 0.039 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 9, C 37. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM20]] | B | CSMD3 activity weakens RBM20's drug response | lines that do not express CSMD3 (13) vs lines expressing it (10) | (z diff -2.87); strongest at Tucidinostat 5 µM: 2.17x vs 1.08x (z diff -5.7) | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; target measured in part of the lines; artifact flags |
| [[DKK2]] | B | CSMD3 activity raises DKK2's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.26× lower at baseline in the lines without CSMD3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| [[NPAS3]] | B | CSMD3 activity raises NPAS3's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.24× lower at baseline in the lines without CSMD3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| [[GLI3]] | B | CSMD3 activity raises GLI3's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.36× lower at baseline in the lines without CSMD3 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| cells under [[Tolcapone (drug)]] 5 µM | B | CSMD3 activity lowers the cells' numbers under Tolcapone 5 µM (makes them more sensitive) | lines that do not express CSMD3 (36) vs lines expressing it (12) | the lines without CSMD3: 1.15× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| [[LINC01695]] | B | CSMD3 activity raises LINC01695's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.83× lower at baseline in the lines without CSMD3 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| [[EGFEM1P]] | B | CSMD3 activity raises EGFEM1P's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.21× lower at baseline in the lines without CSMD3 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| [[ADAMTS19]] | B | CSMD3 activity raises ADAMTS19's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without CSMD3 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| [[GLI3]] | B | CSMD3 activity strengthens GLI3's drug response | lines that do not express CSMD3 (20) vs lines expressing it (9) | the lines without CSMD3 respond 0.90× as strongly (z diff +0.73); strongest at Belinostat 5 µM: 0.77x vs 0.49x (z diff +3.2) | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; target measured in part of the lines; both ways; artifact flags |
| [[DACH1]] | C | CSMD3 activity raises DACH1's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 5.13× lower at baseline in the lines without CSMD3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[LINC02428]] | C | CSMD3 activity raises LINC02428's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.15× lower at baseline in the lines without CSMD3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[NELL2]] | C | CSMD3 activity raises NELL2's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 3.27× lower at baseline in the lines without CSMD3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.4, 35.9); signed map (46.1, 34.8). **Vector** length 59.3, 22.6% of its response variance represented; |z| ≥ 3 in 382 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +20.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | -1.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -1.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CUB and Sushi multiple domains 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.3 — chr8:112,222,928-113,436,939 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sushi domain containing; Complement system regulators and receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z407](https://www.uniprot.org/uniprotkb/Q7Z407) (CUB and sushi domain-containing protein 3):

> Involved in dendrite development.

**Summary**, from NCBI Gene [114788](https://www.ncbi.nlm.nih.gov/gene/114788):

> Predicted to be involved in regulation of dendrite development. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19291) · Entrez [114788](https://www.ncbi.nlm.nih.gov/gene/114788) · UniProt [Q7Z407](https://www.uniprot.org/uniprotkb/Q7Z407) · Ensembl [ENSG00000164796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164796)

## Data

Gene col 9007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9007); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9007]; `tensor/DDL_lfc|DDL_z.npy` [9007]; `embed/gene_vectors.npy` [9007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9007 or target_col == 9007). Every well: [[CSMD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSMD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
