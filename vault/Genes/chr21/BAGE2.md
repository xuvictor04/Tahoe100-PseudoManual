---
symbol: "BAGE2"
type: "gene"
col: 11896
ensembl_id: "ENSG00000187172"
name: "BAGE family member 2 (pseudogene)"
location: "21p11.2"
module: 177
arm: "+"
pooled_cpm: 5.5
n_lines_expressing: 14
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 8
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# BAGE2

*BAGE family member 2 (pseudogene)* — 21p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.44× (z +13.1, q 2e-36, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +8.9, q 1e-16, up in 10 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.612× (z -5.3, q 7e-05, down in 2 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.239×, SNU-1 0.166×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (H4 0.0694×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0820×; ⚠ transcription drop).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPTE]] (+0.71, fdr 1e-05, ⚠ same locus), [[FAM230C]] (+0.68, fdr 4e-05), [[UTY]] (+0.66, fdr 4e-05), [[KDM5D]] (+0.61, fdr 9e-05); moves opposite to [[EXTL3]] (-0.49, fdr 9e-05), [[KLHL25]] (-0.49, fdr 1e-03, ⚠ not reproduced), [[TOR1B]] (-0.45, fdr 1e-04), [[FAM89B]] (-0.45, fdr 1e-04).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TPTE]] → it (grade C ⚠); 8 go from it, the strongest it → [[ZNF252P-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +13.1 | 2e-36 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +11.6 | 8e-29 | 1/6 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +8.9 | 1e-16 | 10/11 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +7.6 | 5e-12 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.85×** | +5.8 | 8e-07 | 0/6 | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.0 | 6e-05 | 1/9 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +4.9 | 8e-05 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +4.7 | 2e-04 | 2/10 (H4, HS-578T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +4.6 | 2e-04 | 6/11 (KATO III, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.2 | 0.002 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.1 | 0.002 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.003 | 5/11 (H4, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.8 | 0.008 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.034 | 0/11 | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.047 | 0/10 | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.047 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.047 | 1/10 (A-427) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.052 | 2/10 (HS-578T, NCI-H1573) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.052 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11896.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.239×, SNU-1 0.166×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (H4 0.0694×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0820×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.612×** | -5.3 | 7e-05 | 2/11 (SNU-1, A-427) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.732× | -3.2 | 0.34 | 1/11 (KATO III) | top dose only |  |
| [[Elagolix sodium (drug)]] 0.05 µM |  | 0.750× | -3.1 | 0.34 | 2/11 (A-172, A-427) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 40.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -10.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 72.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0694× (z -15.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 52.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -10.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0820× (z -14.9) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.906 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.559 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.742 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.571 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTE]] | +0.71 | +0.53 / +0.77 | both halves | 1e-05 | ⚠ same locus (5.1 kb, same strand: neighbours can correlate without regulation) |
| [[FAM230C]] | +0.68 | +0.42 / +0.74 | both halves | 4e-05 |  |
| [[UTY]] | +0.66 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[KDM5D]] | +0.61 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[USP24]] | +0.60 | +0.28 / +0.46 | both halves | 3e-04 |  |
| [[LINC02335]] | +0.57 | +0.32 / +0.63 | both halves | 2e-04 |  |
| [[CC2D2A]] | +0.56 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[NLGN4Y]] | +0.56 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[LINC01320]] | +0.56 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[DUS4L]] | +0.54 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[LINC00882]] | +0.54 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[PYDC2-AS1]] | +0.54 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[ITGBL1]] | +0.54 | +0.34 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXTL3]] | -0.49 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[KLHL25]] | -0.49 | -0.18 / -0.41 | ⚠ not reproduced | 1e-03 |  |
| [[TOR1B]] | -0.45 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[FAM89B]] | -0.45 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[ARID3B]] | -0.45 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[ZCCHC24]] | -0.44 | -0.40 / -0.23 | both halves | 5e-04 |  |
| [[OSTF1]] | -0.44 | -0.52 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPTE]] | C | TPTE activity raises BAGE2's level | lines that do not express TPTE (35) vs lines expressing it (15) | 6.93× lower at baseline in the lines without TPTE | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC02241]] | C | LINC02241 activity raises BAGE2's level | lines that do not express LINC02241 (34) vs lines expressing it (16) | 3.84× lower at baseline in the lines without LINC02241 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000259560, LINC02616, LINC02476; maybe low, not absent; co-absent with the target |
| [[FAM95A]] | C | FAM95A activity raises BAGE2's level | lines that do not express FAM95A (38) vs lines expressing it (12) | 5.13× lower at baseline in the lines without FAM95A | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |
| [[LINC02476]] | C | LINC02476 activity raises BAGE2's level | lines that do not express LINC02476 (40) vs lines expressing it (10) | 4.72× lower at baseline in the lines without LINC02476 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02335, ENSG00000234426, ENSG00000287598; co-absent with the target |
| [[LINC02335]] | C | LINC02335 activity raises BAGE2's level | lines that do not express LINC02335 (41) vs lines expressing it (9) | 4.09× lower at baseline in the lines without LINC02335 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02476, ENSG00000285751, ENSG00000234426; co-absent with the target |
| [[LINC00470]] | C | LINC00470 activity raises BAGE2's level | lines that do not express LINC00470 (38) vs lines expressing it (12) | 2.69× lower at baseline in the lines without LINC00470 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, ENSG00000287474, FCRLA; co-absent with the target |
| [[FAM230C]] | C | FAM230C activity raises BAGE2's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 3.44× lower at baseline in the lines without FAM230C | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[CPED1]] | C | CPED1 activity raises BAGE2's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 2.97× lower at baseline in the lines without CPED1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF252P-1]] | B | BAGE2 activity raises ZNF252P-1's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 1.29× lower at baseline in the lines without BAGE2 | 0.082 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029 |
| [[TPTE]] | C | BAGE2 activity raises TPTE's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 10.17× lower at baseline in the lines without BAGE2 | 0.009 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029; co-absent with the target |
| [[LINC00470]] | C | BAGE2 activity raises LINC00470's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 5.11× lower at baseline in the lines without BAGE2 | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029; co-absent with the target |
| [[LINC02476]] | C | BAGE2 activity raises LINC02476's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 7.33× lower at baseline in the lines without BAGE2 | 0.034 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029; co-absent with the target |
| [[AACSP1]] | C | BAGE2 activity raises AACSP1's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 2.09× lower at baseline in the lines without BAGE2 | 0.038 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029; co-absent with the target |
| [[THSD7A]] | C | BAGE2 activity raises THSD7A's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 1.95× lower at baseline in the lines without BAGE2 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029; co-absent with the target |
| [[LINC02241]] | C | BAGE2 activity raises LINC02241's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 3.66× lower at baseline in the lines without BAGE2 | 0.074 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029; co-absent with the target |
| [[LINC02335]] | C | BAGE2 activity raises LINC02335's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 3.18× lower at baseline in the lines without BAGE2 | 0.082 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.4, 27.3); signed map (34.9, 38.0). **Vector** length 19.6, 3.73% of its response variance represented; |z| ≥ 3 in 201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.3 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.7 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.5 | +0.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.5 | -3.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.5 | -1.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | BAGE family member 2 (pseudogene) |
| Locus type | pseudogene |
| Location | 21p11.2 — chr21:10,454,134-10,516,431 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | CT2.2 |
| Gene groups (HGNC) | BAGE family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y30](https://www.uniprot.org/uniprotkb/Q86Y30) (B melanoma antigen 2):

> Unknown. Candidate gene encoding tumor antigens.

**Summary**, from NCBI Gene [85319](https://www.ncbi.nlm.nih.gov/gene/85319):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15723) · Entrez [85319](https://www.ncbi.nlm.nih.gov/gene/85319) · UniProt [Q86Y30](https://www.uniprot.org/uniprotkb/Q86Y30) · Ensembl [ENSG00000187172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187172)

## Data

Gene col 11896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11896); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11896]; `tensor/DDL_lfc|DDL_z.npy` [11896]; `embed/gene_vectors.npy` [11896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11896 or target_col == 11896). Every well: [[BAGE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAGE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
