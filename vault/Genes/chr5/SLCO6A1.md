---
symbol: "SLCO6A1"
type: "gene"
col: 12972
ensembl_id: "ENSG00000205359"
name: "solute carrier organic anion transporter family member 6A1"
location: "5q21.1"
module: 27
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 30
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 17
direction_downstream: 7
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SLCO6A1

*solute carrier organic anion transporter family member 6A1* — 5q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.48× (z +16.7, q 0e+00, up in 7 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW480 0.0791×, LOX-IMVI 0.0501×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.0294×; ⚠ cell-cycle shift, explains ~44% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.0402×; ⚠ toxic); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0419×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00491]] (+0.86, fdr 7e-06), [[LINC01905]] (+0.79, fdr 7e-06), [[LINC01980]] (+0.73, fdr 7e-06); moves opposite to [[PASD1]] (-0.48, fdr 3e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[LINC01967]] → it (grade B ⚠); 7 go from it, the strongest it → [[LINC01170]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.48×** | +16.7 | 0e+00 | 7/12 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +7.9 | 7e-13 | 1/7 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +7.4 | 2e-11 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.05×** | +6.4 | 2e-08 | 3/19 (LoVo, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +6.3 | 3e-08 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +5.7 | 1e-06 | 2/14 (C32, HT-29) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +5.6 | 2e-06 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.23×** | +5.1 | 3e-05 | 5/16 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +4.7 | 1e-04 | 4/15 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +4.3 | 1e-03 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +4.1 | 0.002 | 8/19 (LOX-IMVI, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.75×** | +3.4 | 0.032 | 6/10 (SW480, SNU-423, …) | rises with dose | position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.65×** | +3.2 | 0.071 | 3/10 (SW480, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.078 | 1/10 (RPMI-7951) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12972.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW480 0.0791×, LOX-IMVI 0.0501×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.0294×; ⚠ cell-cycle shift, explains ~44% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.0402×; ⚠ toxic); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0419×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.837× | -4.1 | 0.028 | 8/24 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.609× | -3.2 | 0.46 | 12/21 (SW480, LOX-IMVI, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.4 | 0 | 6 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0294× (z -14.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[LOX-IMVI (line)]] | wt | 6.47 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0501× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0419× (z -9.7) |
| [[A-172 (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.702 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.762 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.741 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.757 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.724 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.715 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.739 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.821 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.715 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.728 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.759 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00491]] | +0.86 | +0.89 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LINC01905]] | +0.79 | +0.78 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[LINC01980]] | +0.73 | +0.68 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MIR2052HG]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SLC25A24P1]] | +0.68 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[GABRG2]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[HTR2C]] | +0.66 | +0.77 / +0.40 | both halves | 5e-05 |  |
| [[JAKMIP2-AS1]] | +0.65 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ARHGAP25]] | +0.64 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[ST18]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[FBXO38-DT]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[F10]] | +0.63 | +0.60 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PASD1]] | -0.48 | -0.51 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 13, C 4. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01967]] | B | LINC01967 activity raises SLCO6A1's level | lines that do not express LINC01967 (38) vs lines expressing it (12) | 2.84× lower at baseline in the lines without LINC01967 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, SLC15A5, PCSK1 |
| [[LINC02405]] | B | LINC02405 activity raises SLCO6A1's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 1.86× lower at baseline in the lines without LINC02405 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360 |
| [[TOP2A]] | B | TOP2A activity lowers SLCO6A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PASD1]] | B | PASD1 activity raises SLCO6A1's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 2.28× lower at baseline in the lines without PASD1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent |
| [[GABRG2]] | B | GABRG2 activity raises SLCO6A1's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 1.94× lower at baseline in the lines without GABRG2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent |
| [[ADGRG7]] | B | ADGRG7 activity raises SLCO6A1's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.95× lower at baseline in the lines without ADGRG7 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[LINC01551]] | B | LINC01551 activity raises SLCO6A1's level | lines that do not express LINC01551 (36) vs lines expressing it (14) | 1.75× lower at baseline in the lines without LINC01551 | 0.034 | ⚠ within organs, on part of the lines; co-absent genes; also absent: LINC02566, MMRN1, GCG |
| [[SLC24A3]] | B | SLC24A3 activity raises SLCO6A1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.78× lower at baseline in the lines without SLC24A3 | 0.040 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[POU6F2]] | B | POU6F2 activity raises SLCO6A1's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.86× lower at baseline in the lines without POU6F2 | 0.041 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[LINC02315]] | B | LINC02315 activity raises SLCO6A1's level | lines that do not express LINC02315 (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without LINC02315 | 0.050 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1 |
| [[LINC01611]] | B | LINC01611 activity raises SLCO6A1's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 1.80× lower at baseline in the lines without LINC01611 | 0.060 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377 |
| [[HS3ST5]] | B | HS3ST5 activity raises SLCO6A1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.36× lower at baseline in the lines without HS3ST5 | 0.091 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01170]] | B | SLCO6A1 activity raises LINC01170's level | lines that do not express SLCO6A1 (20) vs lines expressing it (30) | 1.77× lower at baseline in the lines without SLCO6A1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF883, SOX5, KCNK2; maybe low, not absent |
| [[LINC02405]] | B | SLCO6A1 activity raises LINC02405's level | lines that do not express SLCO6A1 (20) vs lines expressing it (30) | 2.43× lower at baseline in the lines without SLCO6A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ZNF883, SOX5, KCNK2; maybe low, not absent |
| [[PROX1-AS1]] | B | SLCO6A1 activity raises PROX1-AS1's level | lines that do not express SLCO6A1 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without SLCO6A1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ZNF883, SOX5, KCNK2; maybe low, not absent |
| [[G2E3-AS1]] | B | SLCO6A1 activity raises G2E3-AS1's level | lines that do not express SLCO6A1 (20) vs lines expressing it (30) | 1.46× lower at baseline in the lines without SLCO6A1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ZNF883, SOX5, KCNK2; maybe low, not absent |
| [[FAM13C]] | B | SLCO6A1 activity raises FAM13C's level | lines that do not express SLCO6A1 (20) vs lines expressing it (30) | 1.86× lower at baseline in the lines without SLCO6A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF883, SOX5, KCNK2; maybe low, not absent |
| [[LINC01807]] | B | SLCO6A1 activity raises LINC01807's level | lines that do not express SLCO6A1 (20) vs lines expressing it (30) | 1.60× lower at baseline in the lines without SLCO6A1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF883, SOX5, KCNK2; maybe low, not absent |
| [[LINC00491]] | C | SLCO6A1 activity raises LINC00491's level | lines that do not express SLCO6A1 (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without SLCO6A1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF883, SOX5, KCNK2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.6, 40.6); signed map (48.6, 34.3). **Vector** length 35.9, 8.03% of its response variance represented; |z| ≥ 3 in 407 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +6.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.5 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -1.3 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -0.9 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -2.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -2.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -0.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier organic anion transporter family member 6A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.1 — chr5:102,371,774-102,499,016 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OATP6A1, OATPY, MGC26949, CT48 |
| Gene groups (HGNC) | Solute carrier organic anion transporter family |
| Matched by | ensembl_id |

UniProt [Q86UG4](https://www.uniprot.org/uniprotkb/Q86UG4) carries no function annotation.

**Summary**, from NCBI Gene [133482](https://www.ncbi.nlm.nih.gov/gene/133482):

> Predicted to be involved in sodium-independent organic anion transport. Predicted to be located in sperm principal piece. Predicted to be part of CatSper complex. Predicted to be active in basolateral plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23613) · Entrez [133482](https://www.ncbi.nlm.nih.gov/gene/133482) · UniProt [Q86UG4](https://www.uniprot.org/uniprotkb/Q86UG4) · Ensembl [ENSG00000205359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205359)

## Data

Gene col 12972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12972); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12972]; `tensor/DDL_lfc|DDL_z.npy` [12972]; `embed/gene_vectors.npy` [12972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12972 or target_col == 12972). Every well: [[SLCO6A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLCO6A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
