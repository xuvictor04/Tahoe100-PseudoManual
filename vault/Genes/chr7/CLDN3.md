---
symbol: "CLDN3"
type: "gene"
col: 9088
ensembl_id: "ENSG00000165215"
name: "claudin 3"
location: "7q11.23"
module: 44
arm: "+"
pooled_cpm: 10.94
n_lines_expressing: 22
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 117
direction_downstream: 142
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CLDN3

*claudin 3* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 2.08× (z +4.9, q 5e-04, up in 11 of 19 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Entrectinib (drug)]] 5 µM: 1.93× (z +4.4, q 0.003, up in 15 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.426× (z -5.7, q 6e-06, down in 15 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC3A]] (+0.78, fdr 7e-06), [[TJP3]] (+0.78, fdr 7e-06), [[LGALS4]] (+0.78, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 117 arrows point to it, the strongest [[SLC44A3]] → it (grade B ⚠); 142 go from it, the strongest it → [[SLC44A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9088.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **2.08×** | +4.9 | 5e-04 | 11/19 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.93×** | +4.4 | 0.003 | 15/20 (KATO III, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.010 | 8/20 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +3.9 | 0.015 | 1/8 (HEC-1-A) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.62× | +3.0 | 0.26 | 4/19 (LoVo, CFPAC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9088.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.426×** | -5.7 | 6e-06 | 15/20 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.458×** | -5.2 | 3e-05 | 18/20 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.576×** | -5.2 | 3e-05 | 15/18 (LS 180, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.500×** | -4.7 | 5e-04 | 16/20 (HT-29, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.494×** | -4.5 | 7e-04 | 16/19 (HT-29, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.514×** | -4.5 | 7e-04 | 13/20 (LS 180, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.319×** | -4.0 | 0.005 | 15/20 (LoVo, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.560×** | -3.9 | 0.007 | 11/20 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.561×** | -3.9 | 0.007 | 15/19 (HT-29, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.575×** | -3.7 | 0.012 | 12/20 (NCI-H2030, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.571×** | -3.6 | 0.014 | 10/20 (NCI-H2030, COLO 205, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.388×** | -3.3 | 0.043 | 15/20 (COLO 205, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.615×** | -3.1 | 0.065 | 10/19 (SW480, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.409×** | -3.1 | 0.065 | 11/19 (LS 180, HT-29, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.604×** | -3.1 | 0.065 | 8/20 (SW480, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -3.0 | 0.084 | 9/18 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 45.8 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0832× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.142× (z -14.0) |
| [[HT-29 (line)]] | alt | 82.3 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -16.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.9) |
| [[LoVo (line)]] | wt | 17.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.6) |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 6.63 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0391× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 6.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0725× (z -9.8) |
| [[SW480 (line)]] | alt | 5.39 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.480 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC3A]] | +0.78 | +0.74 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TJP3]] | +0.78 | +0.76 / +0.76 | both halves | 7e-06 | STRING 988 |
| [[LGALS4]] | +0.78 | +0.75 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[FXYD3]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PRR15]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[RAB25]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 | STRING 452 |
| [[PRR15L]] | +0.76 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PLEKHG6]] | +0.74 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TMC4]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.70 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[GPX2]] | +0.69 | +0.67 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*117 arrows, 117 of them with an alert ⚠; grade A 0, B 9, C 108. Shown: the 12 strongest; 105 more arrows (105 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | SLC44A3 activity raises CLDN3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.39× lower at baseline in the lines without SLC44A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[VWA1]] | B | VWA1 activity raises CLDN3's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 3.89× lower at baseline in the lines without VWA1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[MROH7]] | B | MROH7 activity raises CLDN3's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 2.93× lower at baseline in the lines without MROH7 | 0.032 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[FAM83E]] | B | FAM83E activity raises CLDN3's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 2.94× lower at baseline in the lines without FAM83E | 0.039 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity raises CLDN3's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.07× lower at baseline in the lines without ATP8B1 | 0.041 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[MANSC1]] | B | MANSC1 activity raises CLDN3's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 3.19× lower at baseline in the lines without MANSC1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[CRACR2B]] | B | CRACR2B activity raises CLDN3's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without CRACR2B | 0.045 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[PROM2]] | B | PROM2 activity raises CLDN3's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.66× lower at baseline in the lines without PROM2 | 0.046 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises CLDN3's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.95× lower at baseline in the lines without ELF3-AS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[ESRP1]] | C | ESRP1 activity raises CLDN3's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 7.61× lower at baseline in the lines without ESRP1 | 3e-05 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises CLDN3's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 7.31× lower at baseline in the lines without EPCAM | 4e-05 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[SPINT1-AS1]] | C | SPINT1-AS1 activity raises CLDN3's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 7.16× lower at baseline in the lines without SPINT1-AS1 | 5e-05 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3; co-absent with the target |

### Downstream of this gene

*142 arrows, 142 of them with an alert ⚠; grade A 0, B 48, C 94. Shown: the 12 strongest; 130 more arrows (130 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | CLDN3 activity raises SLC44A3's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 3.41× lower at baseline in the lines without CLDN3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[ELMO3]] | B | CLDN3 activity raises ELMO3's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.71× lower at baseline in the lines without CLDN3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[TMEM184A]] | B | CLDN3 activity raises TMEM184A's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without CLDN3 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[ABHD11]] | B | CLDN3 activity raises ABHD11's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.83× lower at baseline in the lines without CLDN3 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[MROH7]] | B | CLDN3 activity raises MROH7's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.57× lower at baseline in the lines without CLDN3 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[FAM83E]] | B | CLDN3 activity raises FAM83E's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 3.67× lower at baseline in the lines without CLDN3 | 0.002 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[RAB11FIP4]] | B | CLDN3 activity raises RAB11FIP4's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without CLDN3 | 0.003 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[DYRK3]] | B | CLDN3 activity lowers DYRK3's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.93× higher at baseline in the lines without CLDN3 | 0.004 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[ELF3-AS1]] | B | CLDN3 activity raises ELF3-AS1's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 3.37× lower at baseline in the lines without CLDN3 | 0.004 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[PIK3C2B]] | B | CLDN3 activity raises PIK3C2B's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without CLDN3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[FZD5]] | B | CLDN3 activity raises FZD5's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.11× lower at baseline in the lines without CLDN3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[RINL]] | B | CLDN3 activity weakens RINL's drug response | lines that do not express CLDN3 (24) vs lines expressing it (20) | the lines without CLDN3 respond 2.16× as strongly (z diff -1.21); strongest at Idarubicin (hydrochloride) 5 µM: 3.11x vs 0.87x (z diff -5.5) | 0.014 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; target measured in part of the lines; the reference differs; artifact flags |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 53.0); signed map (61.7, 5.6). **Vector** length 65.4, 23.8% of its response variance represented; |z| ≥ 3 in 414 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.58 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.58 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.58 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | -2.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | +2.1 | +4.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.8 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -5.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -3.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | claudin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,768,997-73,770,270 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RVP1, CPE-R2, HRVP1; previously C7orf1, CPETR2 |
| Gene groups (HGNC) | Claudins |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: Tight junction interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O15551](https://www.uniprot.org/uniprotkb/O15551) (Claudin-3):

> Barrier-forming claudin. Plays a major role in tight junction-specific obliteration of the intercellular space, through calcium-independent cell-adhesion activity.

**Summary**, from NCBI Gene [1365](https://www.ncbi.nlm.nih.gov/gene/1365):

> Tight junctions represent one mode of cell-to-cell adhesion in epithelial or endothelial cell sheets, forming continuous seals around cells and serving as a physical barrier to prevent solutes and water from passing freely through the paracellular space. These junctions are comprised of sets of continuous networking strands in the outwardly facing cytoplasmic leaflet, with complementary grooves in the inwardly facing extracytoplasmic leaflet. The protein encoded by this intronless gene, a …

**Accessions** — [HGNC:2045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2045) · Entrez [1365](https://www.ncbi.nlm.nih.gov/gene/1365) · UniProt [O15551](https://www.uniprot.org/uniprotkb/O15551) · Ensembl [ENSG00000165215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165215)

## Data

Gene col 9088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9088); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9088]; `tensor/DDL_lfc|DDL_z.npy` [9088]; `embed/gene_vectors.npy` [9088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9088 or target_col == 9088). Every well: [[CLDN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
