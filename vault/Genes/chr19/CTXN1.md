---
symbol: "CTXN1"
type: "gene"
col: 10934
ensembl_id: "ENSG00000178531"
name: "cortexin 1"
location: "19p13.2"
module: 135
arm: "-"
pooled_cpm: 2.35
n_lines_expressing: 42
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 19
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# CTXN1

*cortexin 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.37× (z +12.3, q 8e-32, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Erythromycin (drug)]] 5 µM: 1.52× (z +3.2, q 0.061, up in 2 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 7.74×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 5.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.460× (z -8.4, q 3e-14, down in 21 of 25 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METRN]] (+0.64, fdr 2e-05), [[PODXL2]] (+0.60, fdr 5e-05), [[ARSA]] (+0.60, fdr 2e-05); moves opposite to [[ZXDA]] (-0.65, fdr 5e-05), [[AIMP1]] (-0.62, fdr 6e-05), [[TDP2]] (-0.62, fdr 5e-04).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LACC1]] → it (grade B ⚠); 19 go from it, the strongest it → [[SAMD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 14 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10934.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 7.74×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 5.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.37×** | +12.3 | 8e-32 | 4/5 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.28×** | +11.0 | 8e-26 | 6/8 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.37×** | +8.5 | 3e-15 | 7/7 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.99×** | +5.2 | 3e-05 | 6/13 (A-172, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.82×** | +4.4 | 0.001 | 3/13 (A-427, A-172, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +4.3 | 0.002 | 9/38 (J82, A-427, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.75×** | +4.2 | 0.002 | 11/34 (SW480, A498, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.71×** | +4.1 | 0.003 | 11/36 (SW480, HOP62, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.70×** | +4.0 | 0.004 | 7/35 (SW480, Hs 766T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.69×** | +4.0 | 0.004 | 2/16 (PANC-1, A-172) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.53×** | +3.7 | 0.013 | 1/6 (A-172) | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.5 | 0.024 | 3/18 (SW48, NCI-H23, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.85×** | +3.3 | 0.041 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +3.2 | 0.050 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.061 | 2/36 (C-33 A, HCT15) | top dose only |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.081 | 1/31 (A-172) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10934.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.460×** | -8.4 | 3e-14 | 21/25 (HS-578T, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.448×** | -6.1 | 2e-07 | 16/22 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.529×** | -4.6 | 8e-04 | 12/30 (C-33 A, SW48, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.536×** | -4.5 | 9e-04 | 13/23 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.619×** | -3.5 | 0.047 | 11/31 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cinacalcet (drug)]] 5 µM |  | 0.674× | -3.0 | 0.23 | 3/37 (LS 180, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.74× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 4.09 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 3.03 | 0 | 2 | — | [[Vismodegib (drug)]] 0.05 µM 0.0399× (z -11.7) |
| [[BT-474 (line)]] | alt | 2.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0779× (z -9.3) |
| [[PANC-1 (line)]] | alt | 3.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0672× (z -11.4) |
| [[SW48 (line)]] | wt | 5.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0773× (z -9.3) |
| [[A-427 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.621 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.910 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.855 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.600 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.676 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.723 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.787 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.655 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.729 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.702 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.728 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.801 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METRN]] | +0.64 | +0.57 / +0.49 | both halves | 2e-05 |  |
| [[PODXL2]] | +0.60 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[ARSA]] | +0.60 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PDXP]] | +0.60 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[SNRNP25]] | +0.60 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[PGP]] | +0.59 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[PAQR4]] | +0.59 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[RAP2A]] | +0.59 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[MICOS13]] | +0.59 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[GRK6]] | +0.58 | +0.56 / +0.31 | both halves | 2e-04 |  |
| [[NUDT1]] | +0.58 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.57 | +0.63 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDA]] | -0.65 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[AIMP1]] | -0.62 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[TDP2]] | -0.62 | -0.58 / -0.23 | both halves | 5e-04 |  |
| [[BTN2A3P-1]] | -0.61 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[METTL6]] | -0.61 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[CARD8]] | -0.61 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[ZNF286B]] | -0.60 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[OCIAD1]] | -0.60 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[MTX3]] | -0.60 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[BTN2A3P]] | -0.60 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[RNF6]] | -0.59 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[POLR2M]] | -0.57 | -0.53 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LACC1]] | B | LACC1 activity lowers CTXN1's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 2.34× higher at baseline in the lines without LACC1 | 0.039 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[PODXL2]] | B | PODXL2 activity raises CTXN1's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without PODXL2 | 0.079 | ⚠ within organs, on part of the lines |
| [[GNAZ]] | C | GNAZ activity raises CTXN1's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.99× lower at baseline in the lines without GNAZ | 0.051 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent; co-absent with the target |
| [[SLC29A4]] | C | SLC29A4 activity raises CTXN1's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without SLC29A4 | 0.093 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 17, C 2. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD1]] | B | CTXN1 activity raises SAMD1's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without CTXN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[ZFR]] | B | CTXN1 activity raises ZFR's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without CTXN1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[C20orf27]] | B | CTXN1 activity raises C20orf27's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without CTXN1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[SLC66A2]] | B | CTXN1 activity raises SLC66A2's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without CTXN1 | 0.024 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[PDXP]] | B | CTXN1 activity raises PDXP's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without CTXN1 | 0.026 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[PGP]] | B | CTXN1 activity raises PGP's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without CTXN1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[ATRN]] | B | CTXN1 activity raises ATRN's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without CTXN1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[KIAA2013]] | B | CTXN1 activity raises KIAA2013's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without CTXN1 | 0.035 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[SHANK3]] | B | CTXN1 activity raises SHANK3's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 2.13× lower at baseline in the lines without CTXN1 | 0.045 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[TSPAN17]] | B | CTXN1 activity raises TSPAN17's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without CTXN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[KIAA1958]] | B | CTXN1 activity raises KIAA1958's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without CTXN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[TYW3]] | B | CTXN1 activity raises TYW3's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without CTXN1 | 0.079 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-17.8, 8.8); signed map (-37.2, 15.5). **Vector** length 36.1, 4.42% of its response variance represented; |z| ≥ 3 in 753 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.2 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.2 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +1.9 | +4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +1.3 | +4.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +1.2 | +4.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +2.9 |
|  | [[vincristine (drug)]] 5 µM |  | +0.6 | +2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.6 | +2.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +0.6 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.6 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | cortexin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,924,491-7,926,135 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25968 |
| Matched by | ensembl_id |

**Function**, from UniProt [P60606](https://www.uniprot.org/uniprotkb/P60606) (Cortexin-1):

> May mediate extracellular or intracellular signaling of cortical neurons during forebrain development.

**Summary**, from NCBI Gene [404217](https://www.ncbi.nlm.nih.gov/gene/404217):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31108) · Entrez [404217](https://www.ncbi.nlm.nih.gov/gene/404217) · UniProt [P60606](https://www.uniprot.org/uniprotkb/P60606) · Ensembl [ENSG00000178531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178531)

## Data

Gene col 10934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10934); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10934]; `tensor/DDL_lfc|DDL_z.npy` [10934]; `embed/gene_vectors.npy` [10934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10934 or target_col == 10934). Every well: [[CTXN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTXN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
