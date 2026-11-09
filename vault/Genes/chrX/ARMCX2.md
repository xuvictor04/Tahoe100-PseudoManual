---
symbol: "ARMCX2"
type: "gene"
col: 11584
ensembl_id: "ENSG00000184867"
name: "armadillo repeat containing X-linked 2"
location: "Xq22.1"
module: 13
arm: "+"
pooled_cpm: 3.31
n_lines_expressing: 22
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 16
direction_downstream: 15
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ARMCX2

*armadillo repeat containing X-linked 2* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.98× (z +12.2, q 2e-31, up in 2 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.65× (z +5.0, q 8e-05, up in 8 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.457× (z -5.6, q 1e-05, down in 17 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01615]] (+0.71, fdr 1e-05), [[CARMN]] (+0.63, fdr 1e-05), [[GPR173]] (+0.63, fdr 2e-05); moves opposite to [[MYO5C]] (-0.58, fdr 2e-05), [[DENND1A]] (-0.49, fdr 3e-05), [[TMTC4]] (-0.48, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[SPEG]] → it (grade B ⚠); 15 go from it, the strongest it → [[TUBB2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.98×** | +12.2 | 2e-31 | 2/11 (LOX-IMVI, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +8.3 | 3e-14 | 1/14 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +6.6 | 6e-09 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.25×** | +5.4 | 1e-05 | 14/20 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +5.0 | 8e-05 | 8/19 (SHP-77, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.2 | 0.003 | 3/16 (SHP-77, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.32×** | +3.6 | 0.023 | 0/12 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +3.4 | 0.055 | 4/15 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.457×** | -5.6 | 1e-05 | 17/20 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.509×** | -4.8 | 4e-04 | 16/19 (HOP62, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.573×** | -4.0 | 0.013 | 15/19 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.599×** | -3.7 | 0.035 | 14/19 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -3.4 | 0.074 | 0/19 | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.424× | -3.2 | 0.13 | 13/15 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 11.7 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0714× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0978× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0630× (z -12.0) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0470× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 7.34 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0743× (z -9.2) |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.178 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.203 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.260 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.944 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.247 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.389 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01615]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[CARMN]] | +0.63 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[GPR173]] | +0.63 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[APCDD1L]] | +0.59 | +0.67 / +0.37 | both halves | 8e-05 |  |
| [[NAGK]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[VSTM4]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[EVC2]] | +0.57 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[PGF]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SYNDIG1]] | +0.57 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[HCFC1R1]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PDGFRB]] | +0.56 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[CA12]] | +0.56 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO5C]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[DENND1A]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[TMTC4]] | -0.48 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[IRAK1]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[VSIG10]] | -0.46 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[TSPAN3]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[UBE2G2]] | -0.46 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[NUP210]] | -0.45 | -0.36 / -0.48 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 3, C 13. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPEG]] | B | SPEG activity raises ARMCX2's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without SPEG | 0.076 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[MSX2]] | B | MSX2 activity lowers ARMCX2's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 2.69× higher at baseline in the lines without MSX2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[DENND2A]] | B | DENND2A activity raises ARMCX2's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without DENND2A | 0.089 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[SPOCD1]] | C | SPOCD1 activity raises ARMCX2's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 3.72× lower at baseline in the lines without SPOCD1 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; co-absent with the target |
| [[ARMCX1]] | C | ARMCX1 activity raises ARMCX2's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 3.95× lower at baseline in the lines without ARMCX1 | 0.009 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1; co-absent with the target |
| [[GPR173]] | C | GPR173 activity raises ARMCX2's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 3.74× lower at baseline in the lines without GPR173 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[COL6A2]] | C | COL6A2 activity raises ARMCX2's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 3.38× lower at baseline in the lines without COL6A2 | 0.016 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2; co-absent with the target |
| [[EDNRA]] | C | EDNRA activity raises ARMCX2's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 3.63× lower at baseline in the lines without EDNRA | 0.023 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[SARDH]] | C | SARDH activity raises ARMCX2's level | lines that do not express SARDH (21) vs lines expressing it (29) | 2.48× lower at baseline in the lines without SARDH | 0.038 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent; co-absent with the target |
| [[PTPRN]] | C | PTPRN activity raises ARMCX2's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.68× lower at baseline in the lines without PTPRN | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[LINC02377]] | C | LINC02377 activity raises ARMCX2's level | lines that do not express LINC02377 (35) vs lines expressing it (15) | 2.41× lower at baseline in the lines without LINC02377 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, GRIA2; co-absent with the target |
| [[LAYN]] | C | LAYN activity raises ARMCX2's level | lines that do not express LAYN (31) vs lines expressing it (19) | 3.27× lower at baseline in the lines without LAYN | 0.059 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 1, C 14. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TUBB2A]] | B | ARMCX2 activity raises TUBB2A's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 1.48× lower at baseline in the lines without ARMCX2 | 0.095 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173 |
| [[SPOCD1]] | C | ARMCX2 activity raises SPOCD1's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 3.95× lower at baseline in the lines without ARMCX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[GPR173]] | C | ARMCX2 activity raises GPR173's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 6.36× lower at baseline in the lines without ARMCX2 | 0.013 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[SARDH]] | C | ARMCX2 activity raises SARDH's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without ARMCX2 | 0.013 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[THEMIS2]] | C | ARMCX2 activity raises THEMIS2's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 3.03× lower at baseline in the lines without ARMCX2 | 0.016 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[LOX]] | C | ARMCX2 activity raises LOX's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 6.38× lower at baseline in the lines without ARMCX2 | 0.022 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[EDNRA]] | C | ARMCX2 activity raises EDNRA's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 3.68× lower at baseline in the lines without ARMCX2 | 0.022 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[ARMCX1]] | C | ARMCX2 activity raises ARMCX1's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 3.31× lower at baseline in the lines without ARMCX2 | 0.025 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[LINC02377]] | C | ARMCX2 activity raises LINC02377's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 2.83× lower at baseline in the lines without ARMCX2 | 0.048 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[COL6A2]] | C | ARMCX2 activity raises COL6A2's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 5.19× lower at baseline in the lines without ARMCX2 | 0.052 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[PRICKLE2]] | C | ARMCX2 activity raises PRICKLE2's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 2.76× lower at baseline in the lines without ARMCX2 | 0.066 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |
| [[LAYN]] | C | ARMCX2 activity raises LAYN's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 3.67× lower at baseline in the lines without ARMCX2 | 0.069 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.576). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.6, 18.6); signed map (25.8, 46.7). **Vector** length 40.4, 9.16% of its response variance represented; |z| ≥ 3 in 414 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.5 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | -2.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.2 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.7 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.7 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.6 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.1 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -1.0 | +6.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | +0.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.7 | -1.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.6 | -1.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing X-linked 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,655,281-101,659,850 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ALEX2, KIAA0512, GASP9 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L311](https://www.uniprot.org/uniprotkb/Q7L311) (Armadillo repeat-containing X-linked protein 2):

> May regulate the dynamics and distribution of mitochondria in neural cells.

**Summary**, from NCBI Gene [9823](https://www.ncbi.nlm.nih.gov/gene/9823):

> This gene encodes a protein containing a potential N-terminal transmembrane domain and multiple armadillo (arm) repeats. Proteins containing arm repeats are involved in development, maintenance of tissue integrity, and tumorigenesis. This gene is located in a cluster of related genes on chromosome X. There is a pseudogene for this gene on chromosome 7. Alternative splicing in the 5' UTR results in multiple transcript variants encoding the same protein. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:16869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16869) · Entrez [9823](https://www.ncbi.nlm.nih.gov/gene/9823) · UniProt [Q7L311](https://www.uniprot.org/uniprotkb/Q7L311) · Ensembl [ENSG00000184867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184867)

## Data

Gene col 11584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11584); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11584]; `tensor/DDL_lfc|DDL_z.npy` [11584]; `embed/gene_vectors.npy` [11584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11584 or target_col == 11584). Every well: [[ARMCX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMCX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
