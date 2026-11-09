---
symbol: "CHMP5"
type: "gene"
col: 1453
ensembl_id: "ENSG00000086065"
name: "charged multivesicular body protein 5"
location: "9p13.3"
module: 74
arm: "+"
pooled_cpm: 88.82
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# CHMP5

*charged multivesicular body protein 5* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.98× (z +8.1, q 4e-13, up in 45 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.42× (z +4.1, q 0.005, up in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (J82 3.94×, SHP-77 4.65×, HOP62 3.83×, HEC-1-A 3.51×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 4.09×, SHP-77 3.40×, HOP62 3.07×, HEC-1-A 3.00×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.543× (z -7.2, q 4e-10, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.746× (z -4.4, q 0.003, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 3 lines (AsPC-1 0.320×, LoVo 0.386×, NCI-H460 0.389×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.367×, KATO III 0.510×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.334×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAT2]] (+0.68, fdr 7e-06), [[SELENOK]] (+0.62, fdr 7e-06), [[RNF181]] (+0.60, fdr 1e-05); moves opposite to [[CAD]] (-0.61, fdr 7e-06), [[SLC25A15]] (-0.59, fdr 3e-05), [[LMNB2]] (-0.53, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[IFI6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[POLD4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1453.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (J82 3.94×, SHP-77 4.65×, HOP62 3.83×, HEC-1-A 3.51×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 4.09×, SHP-77 3.40×, HOP62 3.07×, HEC-1-A 3.00×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.98×** | +8.1 | 4e-13 | 45/49 (J82, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.95×** | +7.6 | 1e-11 | 40/44 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.43×** | +4.2 | 0.005 | 31/48 (SW1417, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.005 | 35/48 (HOP62, LOX-IMVI, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.45×** | +3.9 | 0.011 | 27/45 (HEC-1-A, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.082 | 25/48 (LOX-IMVI, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | 1.33× | +3.2 | 0.13 | 27/48 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.30× | +3.1 | 0.16 | 25/48 (C32, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.22× | +3.0 | 0.17 | 24/49 (SW480, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1453.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 3 lines (AsPC-1 0.320×, LoVo 0.386×, NCI-H460 0.389×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.367×, KATO III 0.510×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.334×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.543×** | -7.2 | 4e-10 | 46/48 (AsPC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.746×** | -4.4 | 0.003 | 34/48 (AsPC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 60.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Digitoxin (drug)]] 5 µM 0.334× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 134 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 71.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 58.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 77.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 57.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.389× (z -8.6) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 88.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.7) |
| [[LoVo (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.386× (z -9.1) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 92.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 71.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 87.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 123 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 89.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 79.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 62.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAT2]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SELENOK]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[RNF181]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SLU7]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[CIR1]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MVB12A]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 | pathway: Budding and maturation of HIV virion; STRING 720 |
| [[BSDC1]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SYF2]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PRKD2]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[OTUD5]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[GCC2]] | +0.57 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[PABIR3]] | +0.57 | +0.45 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAD]] | -0.61 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[SLC25A15]] | -0.59 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[LMNB2]] | -0.53 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.53 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[CDKN2AIPNL]] | -0.53 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[VARS1]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[IPO5]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[FAM120A]] | -0.52 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[PDE3B]] | -0.51 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[CDCA7]] | -0.51 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ATIC]] | -0.51 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[SNX5]] | -0.51 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI6]] | B | IFI6 activity raises CHMP5's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without IFI6 | 0.008 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises CHMP5's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.23× lower at baseline in the lines without IFI44 | 0.018 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[OAS1]] | B | OAS1 activity weakens CHMP5's drug response | lines that do not express OAS1 (13) vs lines expressing it (36) | the lines without OAS1 respond 1.24× as strongly (z diff -0.73); strongest at Bortezomib 0.05 µM: 1.72x vs 1.23x (z diff -2.3) | 0.039 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[OASL]] | B | OASL activity raises CHMP5's level | lines that do not express OASL (10) vs lines expressing it (40) | 1.30× lower at baseline in the lines without OASL | 0.049 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[GBP3]] | B | GBP3 activity raises CHMP5's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 1.28× lower at baseline in the lines without GBP3 | 0.063 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[IFI16]] | B | IFI16 activity raises CHMP5's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 1.19× lower at baseline in the lines without IFI16 | 0.067 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[ODF3B]] | B | ODF3B activity raises CHMP5's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.13× lower at baseline in the lines without ODF3B | 0.080 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[IFI27]] | B | IFI27 activity raises CHMP5's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.25× lower at baseline in the lines without IFI27 | 0.089 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[BST2]] | B | BST2 activity weakens CHMP5's drug response | lines that do not express BST2 (18) vs lines expressing it (31) | the lines without BST2 respond 1.28× as strongly (z diff -0.61); strongest at Bortezomib 0.05 µM: 1.54x vs 1.24x (z diff -1.8) | 0.093 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLD4]] | C | CHMP5's natural level strengthens POLD4's drug response | CHMP5's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.70, reverse -0.17; direction not clear | 0.025 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.7, -45.9); signed map (-13.4, 6.8). **Vector** length 88.4, 31.5% of its response variance represented; |z| ≥ 3 in 495 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +0.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.6 | -7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -3.7 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:33,264,879-33,282,070 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Spike, Vps60, CGI-34, HSPC177; previously C9orf83, SNF7DC2 |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III associated factors |
| Reactome | 8 pathways, smallest: Budding and maturation of HIV virion; Endosomal Sorting Complex Required For Transport (ESCRT); Late Phase of HIV Life Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZZ3](https://www.uniprot.org/uniprotkb/Q9NZZ3) (Charged multivesicular body protein 5):

> Probable peripherally associated component of the endosomal sorting required for transport complex III (ESCRT-III) which is involved in multivesicular bodies (MVBs) formation and sorting of endosomal cargo proteins into MVBs. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal …

**Summary**, from NCBI Gene [51510](https://www.ncbi.nlm.nih.gov/gene/51510):

> CHMP5 belongs to the chromatin-modifying protein/charged multivesicular body protein (CHMP) family. These proteins are components of ESCRT-III (endosomal sorting complex required for transport III), a complex involved in degradation of surface receptor proteins and formation of endocytic multivesicular bodies (MVBs). Some CHMPs have both nuclear and cytoplasmic/vesicular distributions, and one such CHMP, CHMP1A (MIM 164010), is required for both MVB formation and regulation of cell cycle …

**Accessions** — [HGNC:26942](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26942) · Entrez [51510](https://www.ncbi.nlm.nih.gov/gene/51510) · UniProt [Q9NZZ3](https://www.uniprot.org/uniprotkb/Q9NZZ3) · Ensembl [ENSG00000086065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086065)

## Data

Gene col 1453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1453); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1453]; `tensor/DDL_lfc|DDL_z.npy` [1453]; `embed/gene_vectors.npy` [1453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1453 or target_col == 1453). Every well: [[CHMP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
