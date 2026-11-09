---
symbol: "HOXC10"
type: "gene"
col: 11135
ensembl_id: "ENSG00000180818"
name: "homeobox C10"
location: "12q13.13"
module: 130
arm: "+"
pooled_cpm: 13.71
n_lines_expressing: 24
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# HOXC10

*homeobox C10* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.53× (z +9.7, q 2e-19, up in 5 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +8.4, q 1e-14, up in 17 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (AN3 CA 0.212×, HS-578T 0.277×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.0902×; ⚠ cell-cycle shift, explains ~86% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (AN3 CA 0.115×; ⚠ toxic; transcription drop); [[Quinidine (15% dihydroquinidine) (drug)]] 5 µM in 1 line (A-172 0.138×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC115]] (+0.64, fdr 3e-05), [[HOXC9]] (+0.63, fdr 1e-05, ⚠ same locus), [[RCOR3]] (+0.60, fdr 2e-05), [[DNAJC27]] (+0.59, fdr 3e-05); moves opposite to [[HERC2P9-1]] (-0.54, fdr 4e-05), [[ASAP1]] (-0.53, fdr 4e-05), [[YWHAB]] (-0.51, fdr 4e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HOXC6]] → it (grade B ⚠); 5 go from it, the strongest it → [[HOXC9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +9.7 | 2e-19 | 5/13 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +8.8 | 3e-16 | 7/18 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +8.4 | 1e-14 | 17/22 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +7.3 | 5e-11 | 4/15 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +5.9 | 4e-07 | 11/19 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.9 | 0.011 | 6/19 (SW480, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.015 | 5/22 (A-172, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.031 | 9/22 (C32, KATO III, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (AN3 CA 0.212×, HS-578T 0.277×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.0902×; ⚠ cell-cycle shift, explains ~86% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (AN3 CA 0.115×; ⚠ toxic; transcription drop); [[Quinidine (15% dihydroquinidine) (drug)]] 5 µM in 1 line (A-172 0.138×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 247 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0902× (z -20.4) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -9.3) |
| [[KATO III (line)]] | alt | 59.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.1) | [[Ixazomib citrate (drug)]] 5 µM 0.338× (z -10.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 7.96 | 0 | 1 | — | [[Quinidine (15% dihydroquinidine) (drug)]] 5 µM 0.138× (z -9.2) |
| [[HS-578T (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -8.6) |
| [[A-427 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC115]] | +0.64 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[HOXC9]] | +0.63 | +0.54 / +0.69 | both halves | 1e-05 | same gene group; STRING 900; ⚠ same locus (4.6 kb, same strand: neighbours can correlate without regulation) |
| [[RCOR3]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[DNAJC27]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ZIC2]] | +0.59 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[GID8]] | +0.59 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ACBD5]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[HOXC6]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 | same gene group; STRING 754; ⚠ same locus (0.3 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA3]] | +0.57 | +0.36 / +0.62 | both halves | 9e-05 | same gene group |
| [[CDKN1B]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[LNX2]] | +0.56 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[HOXA9]] | +0.55 | +0.34 / +0.63 | both halves | 1e-04 | same gene group |
| [[ATP23]] | +0.55 | +0.29 / +0.55 | both halves | 2e-04 |  |
| [[PHF21A]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P9-1]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ASAP1]] | -0.53 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[YWHAB]] | -0.51 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[EIPR1]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[BICD1]] | -0.50 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[PSMD1]] | -0.49 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[EFTUD2]] | -0.49 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[SPATA5]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[GHRLOS]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PTPN11]] | -0.47 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[DCBLD2]] | -0.47 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC6]] | B | HOXC6 activity raises HOXC10's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 3.68× lower at baseline in the lines without HOXC6 | 0.048 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent |
| [[HOXC8]] | B | HOXC8 activity raises HOXC10's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 3.57× lower at baseline in the lines without HOXC8 | 0.054 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5 |
| [[HOXB2]] | B | HOXB2 activity raises HOXC10's level | lines that do not express HOXB2 (21) vs lines expressing it (29) | 2.32× lower at baseline in the lines without HOXB2 | 0.066 | ⚠ within organs, on part of the lines; also absent: HOXB-AS1, SOX2, JAKMIP2-AS1 |
| [[HOXC9]] | B | HOXC9 activity raises HOXC10's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 3.92× lower at baseline in the lines without HOXC9 | 0.081 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2 |
| [[HOXB4]] | B | HOXB4 activity raises HOXC10's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 1.59× lower at baseline in the lines without HOXB4 | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC9]] | B | HOXC10 activity raises HOXC9's level | lines that do not express HOXC10 (26) vs lines expressing it (24) | 3.16× lower at baseline in the lines without HOXC10 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: NTRK3, CES1, POTEE |
| [[HOXC6]] | B | HOXC10 activity raises HOXC6's level | lines that do not express HOXC10 (26) vs lines expressing it (24) | 3.13× lower at baseline in the lines without HOXC10 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: NTRK3, CES1, POTEE |
| [[HOXC8]] | B | HOXC10 activity raises HOXC8's level | lines that do not express HOXC10 (26) vs lines expressing it (24) | 2.65× lower at baseline in the lines without HOXC10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: NTRK3, CES1, POTEE |
| [[HOXB4]] | B | HOXC10 activity raises HOXB4's level | lines that do not express HOXC10 (26) vs lines expressing it (24) | 1.40× lower at baseline in the lines without HOXC10 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: NTRK3, CES1, POTEE |
| [[HOXB2]] | B | HOXC10 activity raises HOXB2's level | lines that do not express HOXC10 (26) vs lines expressing it (24) | 1.66× lower at baseline in the lines without HOXC10 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: NTRK3, CES1, POTEE |

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.8, -25.4); signed map (-6.3, 6.7). **Vector** length 43.3, 8.94% of its response variance represented; |z| ≥ 3 in 415 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +8.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.7 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +1.7 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +0.9 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +1.3 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.8 | -2.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | homeobox C10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,985,065-53,990,279 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX3I |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYD6](https://www.uniprot.org/uniprotkb/Q9NYD6) (Homeobox protein Hox-C10):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3226](https://www.ncbi.nlm.nih.gov/gene/3226):

> This gene belongs to the homeobox family of genes. The homeobox genes encode a highly conserved family of transcription factors that play an important role in morphogenesis in all multicellular organisms. Mammals possess four similar homeobox gene clusters, HOXA, HOXB, HOXC and HOXD, which are located on different chromosomes and consist of 9 to 11 genes arranged in tandem. This gene is one of several homeobox HOXC genes located in a cluster on chromosome 12. The protein level is controlled …

**Accessions** — [HGNC:5122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5122) · Entrez [3226](https://www.ncbi.nlm.nih.gov/gene/3226) · UniProt [Q9NYD6](https://www.uniprot.org/uniprotkb/Q9NYD6) · Ensembl [ENSG00000180818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180818)

## Data

Gene col 11135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11135); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11135]; `tensor/DDL_lfc|DDL_z.npy` [11135]; `embed/gene_vectors.npy` [11135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11135 or target_col == 11135). Every well: [[HOXC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
