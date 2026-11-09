---
symbol: "TYMP"
type: "gene"
col: 363
ensembl_id: "ENSG00000025708"
name: "thymidine phosphorylase"
location: "22q13.33"
module: 32
arm: "+"
pooled_cpm: 22.11
n_lines_expressing: 30
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 36
direction_downstream: 42
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TYMP

*thymidine phosphorylase* — 22q13.33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.575× (z -6.0, q 8e-07, down in 23 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ODF3B]] (+0.85, fdr 7e-06, ⚠ same locus), [[IRF7]] (+0.76, fdr 7e-06), [[HELZ2]] (+0.70, fdr 1e-05), [[CFB]] (+0.69, fdr 7e-06); moves opposite to [[CRTAP]] (-0.53, fdr 2e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[GBP4]] → it (grade B ⚠); 42 go from it, the strongest it → [[IFIH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.58× | +3.4 | 0.21 | 16/27 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 2.11× | +3.4 | 0.21 | 15/27 (NCI-H1573, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.55× | +3.2 | 0.23 | 17/27 (RKO, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.575×** | -6.0 | 8e-07 | 23/28 (KATO III, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.461×** | -5.9 | 8e-07 | 24/28 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.449×** | -5.8 | 1e-06 | 22/27 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -5.6 | 3e-06 | 23/28 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.615×** | -5.3 | 2e-05 | 21/26 (CFPAC-1, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.633×** | -5.0 | 7e-05 | 16/27 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.634×** | -4.9 | 7e-05 | 20/27 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.535×** | -4.8 | 1e-04 | 23/27 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.551×** | -4.6 | 3e-04 | 16/28 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.327×** | -4.3 | 0.001 | 19/28 (NCI-H1792, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.575×** | -4.2 | 0.001 | 18/27 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.337×** | -4.2 | 0.001 | 21/27 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.587×** | -4.1 | 0.002 | 21/28 (Panc 03.27, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.348×** | -4.0 | 0.002 | 18/25 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.591×** | -4.0 | 0.002 | 17/28 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.632×** | -3.5 | 0.014 | 13/27 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.724×** | -3.5 | 0.014 | 17/28 (COLO 205, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.644×** | -3.4 | 0.020 | 16/28 (NCI-H1573, RPMI-7951, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.415×** | -3.4 | 0.020 | 16/27 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 109 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0676× (z -25.0) |
| [[NCI-H1792 (line)]] | alt | 86.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0555× (z -25.5) |
| [[A549 (line)]] | wt | 30.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 91.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -13.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 25.8 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.171× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 32.6 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -10.6) |
| [[A498 (line)]] | wt | 76.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 5.54 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0472× (z -9.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[COLO 205 (line)]] | alt | 30.2 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.192× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -11.0) |
| [[A-172 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.85 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ODF3B]] | +0.85 | +0.77 / +0.87 | both halves | 7e-06 | STRING 497; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[IRF7]] | +0.76 | +0.67 / +0.80 | both halves | 7e-06 | STRING 504 |
| [[HELZ2]] | +0.70 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[CFB]] | +0.69 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[SP110]] | +0.68 | +0.56 / +0.75 | both halves | 1e-05 | same gene group |
| [[IFI16]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[IFI44L]] | +0.68 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[OAS1]] | +0.67 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[SCO2]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 | STRING 743; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ISG15]] | +0.66 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[IRF9]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MX1]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[BATF2]] | +0.65 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[OASL]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAP]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 32, C 4. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP4]] | B | GBP4 activity raises TYMP's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.55× lower at baseline in the lines without GBP4 | 0.009 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[CP]] | B | CP activity raises TYMP's level | lines that do not express CP (39) vs lines expressing it (11) | 3.91× lower at baseline in the lines without CP | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[IFI44L]] | B | IFI44L activity raises TYMP's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without IFI44L | 0.017 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[ADAM28]] | B | ADAM28 activity raises TYMP's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without ADAM28 | 0.025 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[ETV7]] | B | ETV7 activity raises TYMP's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without ETV7 | 0.027 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[SOX4]] | B | SOX4 activity raises TYMP's level | lines that do not express SOX4 (6) vs lines expressing it (44) | 3.48× lower at baseline in the lines without SOX4 | 0.028 | ⚠ within organs, on part of the lines; also absent: B3GNT5, PLCXD2, PMEPA1; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises TYMP's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.70× lower at baseline in the lines without OAS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI27]] | B | IFI27 activity raises TYMP's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without IFI27 | 0.029 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[GBP4]] | B | GBP4 activity strengthens TYMP's drug response | lines that do not express GBP4 (8) vs lines expressing it (21) | the lines without GBP4 respond 0.45× as strongly (z diff +2.19); strongest at Idarubicin (hydrochloride) 5 µM: 0.77x vs 0.41x (z diff +4.5) | 0.033 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1; target measured in part of the lines; artifact flags |
| [[GBP1]] | B | GBP1 activity raises TYMP's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.25× lower at baseline in the lines without GBP1 | 0.038 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[RSAD2]] | B | RSAD2 activity raises TYMP's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without RSAD2 | 0.043 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[KYNU]] | B | KYNU activity raises TYMP's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.79× lower at baseline in the lines without KYNU | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 38, C 4. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIH1]] | B | TYMP activity raises IFIH1's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.01× lower at baseline in the lines without TYMP | 0.008 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[USP15]] | B | TYMP activity raises USP15's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.24× lower at baseline in the lines without TYMP | 0.012 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[HLA-F]] | B | TYMP activity raises HLA-F's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without TYMP | 0.012 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[UBAP1]] | B | TYMP activity raises UBAP1's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.29× lower at baseline in the lines without TYMP | 0.013 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[PARP12]] | B | TYMP activity raises PARP12's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.78× lower at baseline in the lines without TYMP | 0.014 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[IRF7]] | B | TYMP activity raises IRF7's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.45× lower at baseline in the lines without TYMP | 0.015 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[SP110]] | B | TYMP activity raises SP110's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.86× lower at baseline in the lines without TYMP | 0.016 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[STAT2]] | B | TYMP activity strengthens STAT2's drug response | lines that do not express TYMP (20) vs lines expressing it (29) | the lines without TYMP respond 0.63× as strongly (z diff +1.99); strongest at Homoharringtonine 0.5 µM: 0.74x vs 0.46x (z diff +3.6) | 0.020 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20; target measured in part of the lines; artifact flags |
| [[PARP14]] | B | TYMP activity raises PARP14's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without TYMP | 0.020 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[SAMD9]] | B | TYMP activity raises SAMD9's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.18× lower at baseline in the lines without TYMP | 0.021 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[CMPK2]] | B | TYMP activity raises CMPK2's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without TYMP | 0.022 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[OAS1]] | B | TYMP activity raises OAS1's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without TYMP | 0.028 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.2, 51.8); signed map (65.1, 29.5). **Vector** length 95.7, 34.0% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.53 to 56); *interferon gamma response* (hallmark, mean cos +0.54 to 60); *interferon* (control, mean cos +0.60 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +3.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.9 | -4.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.8 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.4 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | thymidine phosphorylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,525,752-50,530,032 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MNGIE, ECGF1 |
| Gene groups (HGNC) | Minor histocompatibility antigens |
| Reactome | 5 pathways, smallest: Pyrimidine catabolism; Pyrimidine salvage; Nucleotide salvage |
| Matched by | ensembl_id |

**Function**, from UniProt [P19971](https://www.uniprot.org/uniprotkb/P19971) (Thymidine phosphorylase):

> May have a role in maintaining the integrity of the blood vessels. Has growth promoting activity on endothelial cells, angiogenic activity in vivo and chemotactic activity on endothelial cells in vitro.; Catalyzes the reversible phosphorolysis of thymidine. The produced molecules are then utilized as carbon and energy sources or in the rescue of pyrimidine bases for nucleotide synthesis.

**Summary**, from NCBI Gene [1890](https://www.ncbi.nlm.nih.gov/gene/1890):

> This gene encodes an angiogenic factor which promotes angiogenesis in vivo and stimulates the in vitro growth of a variety of endothelial cells. It has a highly restricted target cell specificity acting only on endothelial cells. Mutations in this gene have been associated with mitochondrial neurogastrointestinal encephalomyopathy. Multiple alternatively spliced transcript variants have been identified. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:3148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3148) · Entrez [1890](https://www.ncbi.nlm.nih.gov/gene/1890) · UniProt [P19971](https://www.uniprot.org/uniprotkb/P19971) · Ensembl [ENSG00000025708](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000025708)

## Data

Gene col 363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 363); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 363]; `tensor/DDL_lfc|DDL_z.npy` [363]; `embed/gene_vectors.npy` [363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 363 or target_col == 363). Every well: [[TYMP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYMP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
