---
symbol: "TPTE"
type: "gene"
col: 15818
ensembl_id: "ENSG00000274391"
name: "transmembrane phosphatase with tensin homology"
location: "21p11.2"
module: 177
arm: "+"
pooled_cpm: 15.99
n_lines_expressing: 15
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 16
direction_downstream: 17
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# TPTE

*transmembrane phosphatase with tensin homology* — 21p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.42× (z +11.6, q 2e-28, up in 0 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +7.9, q 8e-13, up in 0 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.686× (z -5.0, q 4e-04, down in 2 of 12 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAGE2]] (+0.71, fdr 1e-05, ⚠ same locus), [[LINC02476]] (+0.69, fdr 7e-06), [[FAM230C]] (+0.67, fdr 1e-05), [[LINC00470]] (+0.67, fdr 7e-06); moves opposite to [[RNPEP]] (-0.42, fdr 3e-04), [[SEMA4F]] (-0.42, fdr 1e-04), [[LINC03009]] (-0.40, fdr 1e-04).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[ANKRD20A8P]], [[FAM95A]] → it (grade C ⚠); 17 go from it, the strongest it → [[LDB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +11.6 | 2e-28 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +11.3 | 3e-27 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.9 | 8e-13 | 0/13 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +7.6 | 4e-12 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.009 | 0/12 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.8 | 0.011 | 1/12 (A-172) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.8 | 0.011 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.32×** | +3.6 | 0.020 | 1/12 (A-427) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.4 | 0.043 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.089 | 7/12 (KATO III, RPMI-7951, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.089 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.27× | +3.0 | 0.11 | 1/12 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15818.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.686×** | -5.0 | 4e-04 | 2/12 (A-427, Hs 766T) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.659×** | -3.9 | 0.013 | 0/13 | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.743×** | -3.9 | 0.013 | 6/12 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.735×** | -3.9 | 0.013 | 3/12 (A-427, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.760×** | -3.6 | 0.033 | 0/12 | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.761×** | -3.5 | 0.050 | 4/13 (SW 1088, RPMI-7951, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.778×** | -3.3 | 0.069 | 0/13 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.779×** | -3.3 | 0.069 | 5/12 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.790× | -3.1 | 0.11 | 5/12 (KATO III, H4, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 129 | 2 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.9) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0750× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.9) |
| [[KATO III (line)]] | alt | 113 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.8) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -18.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 248 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.1) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0158× (z -33.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.345× (z -8.6) |
| [[A-172 (line)]] | wt | 116 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.8) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -17.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 81.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -15.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 39.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -11.9) |
| [[HS-578T (line)]] | alt | 69.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -15.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 48.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0518× (z -18.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 89.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0908× (z -9.5) |
| [[A498 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 9 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAGE2]] | +0.71 | +0.53 / +0.77 | both halves | 1e-05 | ⚠ same locus (5.1 kb, same strand: neighbours can correlate without regulation) |
| [[LINC02476]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[FAM230C]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[LINC00470]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[UTY]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LINC02335]] | +0.60 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[ANKRD20A8P]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CCDC144NL-AS1]] | +0.56 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[AK6]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[FAM95A]] | +0.54 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MSR1]] | +0.54 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[LINC02506]] | +0.53 | +0.30 / +0.54 | both halves | 2e-04 |  |
| [[LINC01446]] | +0.53 | +0.28 / +0.69 | both halves | 3e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNPEP]] | -0.42 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[SEMA4F]] | -0.42 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[LINC03009]] | -0.40 | -0.35 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A8P]], [[FAM95A]] | C | ANKRD20A8P, FAM95A activity raises TPTE's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 9.26× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[PHF2P2]] | C | PHF2P2 activity raises TPTE's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 8.81× lower at baseline in the lines without PHF2P2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[LINC02476]] | C | LINC02476 activity raises TPTE's level | lines that do not express LINC02476 (40) vs lines expressing it (10) | 7.96× lower at baseline in the lines without LINC02476 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02335, ENSG00000234426, ENSG00000287598; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises TPTE's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 6.24× lower at baseline in the lines without LINC01446 | 0.006 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[GABRA3]] | C | GABRA3 activity raises TPTE's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 3.77× lower at baseline in the lines without GABRA3 | 0.008 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[BAGE2]] | C | BAGE2 activity raises TPTE's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 10.17× lower at baseline in the lines without BAGE2 | 0.009 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029; co-absent with the target |
| [[LINC00470]] | C | LINC00470 activity raises TPTE's level | lines that do not express LINC00470 (38) vs lines expressing it (12) | 4.53× lower at baseline in the lines without LINC00470 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, ENSG00000287474, FCRLA; co-absent with the target |
| [[MAGEA3-DT]] | C | MAGEA3-DT activity raises TPTE's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 4.16× lower at baseline in the lines without MAGEA3-DT | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises TPTE's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 3.86× lower at baseline in the lines without CCDC144NL-AS1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[LINC01518]] | C | LINC01518 activity raises TPTE's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 4.36× lower at baseline in the lines without LINC01518 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[FAM230C]] | C | FAM230C activity raises TPTE's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 4.58× lower at baseline in the lines without FAM230C | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[MIR548XHG]] | C | MIR548XHG activity raises TPTE's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 4.68× lower at baseline in the lines without MIR548XHG | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 2, C 15. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDB2]] | B | TPTE activity raises LDB2's level | lines that do not express TPTE (35) vs lines expressing it (15) | 2.30× lower at baseline in the lines without TPTE | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P |
| [[BDP1]] | B | TPTE activity lowers BDP1's level | lines that do not express TPTE (35) vs lines expressing it (15) | 1.13× higher at baseline in the lines without TPTE | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P |
| [[BAGE2]] | C | TPTE activity raises BAGE2's level | lines that do not express TPTE (35) vs lines expressing it (15) | 6.93× lower at baseline in the lines without TPTE | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC00470]] | C | TPTE activity raises LINC00470's level | lines that do not express TPTE (35) vs lines expressing it (15) | 6.01× lower at baseline in the lines without TPTE | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[PHF2P2]] | C | TPTE activity raises PHF2P2's level | lines that do not express TPTE (35) vs lines expressing it (15) | 4.64× lower at baseline in the lines without TPTE | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC02616]] | C | TPTE activity raises LINC02616's level | lines that do not express TPTE (35) vs lines expressing it (15) | 3.88× lower at baseline in the lines without TPTE | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC02476]] | C | TPTE activity raises LINC02476's level | lines that do not express TPTE (35) vs lines expressing it (15) | 7.38× lower at baseline in the lines without TPTE | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[CCDC144NL-AS1]] | C | TPTE activity raises CCDC144NL-AS1's level | lines that do not express TPTE (35) vs lines expressing it (15) | 2.74× lower at baseline in the lines without TPTE | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[GABRA3]] | C | TPTE activity raises GABRA3's level | lines that do not express TPTE (35) vs lines expressing it (15) | 4.09× lower at baseline in the lines without TPTE | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC01446]] | C | TPTE activity raises LINC01446's level | lines that do not express TPTE (35) vs lines expressing it (15) | 5.61× lower at baseline in the lines without TPTE | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[ANKRD20A8P]] | C | TPTE activity raises ANKRD20A8P's level | lines that do not express TPTE (35) vs lines expressing it (15) | 4.64× lower at baseline in the lines without TPTE | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC02335]] | C | TPTE activity raises LINC02335's level | lines that do not express TPTE (35) vs lines expressing it (15) | 2.97× lower at baseline in the lines without TPTE | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.794). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.1, 27.5); signed map (34.8, 37.7). **Vector** length 34.0, 8.82% of its response variance represented; |z| ≥ 3 in 266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.2 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.9 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane phosphatase with tensin homology |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21p11.2 — chr21:10,521,553-10,606,140 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTEN2, CT44, TPTE1 |
| Gene groups (HGNC) | C2 tensin-type domain containing; PTEN protein phosphatases |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the Golgi membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P56180](https://www.uniprot.org/uniprotkb/P56180) (Putative tyrosine-protein phosphatase TPTE):

> Could be involved in signal transduction.

**Summary**, from NCBI Gene [7179](https://www.ncbi.nlm.nih.gov/gene/7179):

> This gene encodes a PTEN-related tyrosine phosphatase which may play a role in the signal transduction pathways of the endocrine or spermatogenic function of the testis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:12023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12023) · Entrez [7179](https://www.ncbi.nlm.nih.gov/gene/7179) · UniProt [P56180](https://www.uniprot.org/uniprotkb/P56180) · Ensembl [ENSG00000274391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274391)

## Data

Gene col 15818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15818); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15818]; `tensor/DDL_lfc|DDL_z.npy` [15818]; `embed/gene_vectors.npy` [15818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15818 or target_col == 15818). Every well: [[TPTE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPTE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
