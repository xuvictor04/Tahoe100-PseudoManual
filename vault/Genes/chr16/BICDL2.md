---
symbol: "BICDL2"
type: "gene"
col: 8476
ensembl_id: "ENSG00000162069"
name: "BICD family like cargo adaptor 2"
location: "16p13.3"
module: 31
arm: "+"
pooled_cpm: 7.17
n_lines_expressing: 28
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 75
direction_downstream: 75
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# BICDL2

*BICD family like cargo adaptor 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +9.4, q 4e-18, up in 9 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (COLO 205 0.0540×, LoVo 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (SW48 0.0555×); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 0.291×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLDN4]] (+0.66, fdr 9e-06), [[MYH14]] (+0.66, fdr 7e-06), [[CLDN7]] (+0.65, fdr 7e-06); moves opposite to [[TAS2R30]] (-0.57, fdr 2e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 75 arrows point to it, the strongest [[CYP4F12]] → it (grade B ⚠); 75 go from it, the strongest it → [[JUP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +9.4 | 4e-18 | 9/22 (RPMI-7951, SW480, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +9.2 | 7e-18 | 6/20 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +9.1 | 2e-17 | 6/14 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +9.0 | 2e-17 | 4/9 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +6.5 | 1e-08 | 3/12 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.3 | 0.002 | 1/16 (BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +4.2 | 0.002 | 9/20 (LS 180, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.005 | 6/24 (COLO 205, NCI-H2347, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.1 | 0.12 | 3/19 (SW480, KATO III, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.39× | +3.1 | 0.12 | 3/20 (SW1417, BT-474, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.37× | +3.0 | 0.14 | 6/22 (LS 180, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8476.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (COLO 205 0.0540×, LoVo 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (SW48 0.0555×); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 0.291×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.720× | -3.2 | 0.49 | 9/22 (LoVo, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.724× | -3.1 | 0.49 | 5/24 (RPMI-7951, LoVo, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0540× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 6.11 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.291× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 8.64 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0555× (z -9.0) |
| [[A-172 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.818 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.981 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLDN4]] | +0.66 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[MYH14]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CLDN7]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TMEM45B]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CLDN3]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TMEM125]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ADCY4]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CLIC5]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[MUC12]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CEACAM5]] | +0.61 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[TMPRSS4]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAS2R30]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 18, C 57. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP4F12]] | B | CYP4F12 activity raises BICDL2's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.40× lower at baseline in the lines without CYP4F12 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[ARHGAP30]] | B | ARHGAP30 activity raises BICDL2's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.66× lower at baseline in the lines without ARHGAP30 | 0.006 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[VIPR1]] | B | VIPR1 activity raises BICDL2's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 3.29× lower at baseline in the lines without VIPR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[MUC3A]] | B | MUC3A activity raises BICDL2's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.51× lower at baseline in the lines without MUC3A | 0.013 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[ALOX5]] | B | ALOX5 activity raises BICDL2's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.89× lower at baseline in the lines without ALOX5 | 0.014 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[LIPH]] | B | LIPH activity raises BICDL2's level | lines that do not express LIPH (27) vs lines expressing it (23) | 3.34× lower at baseline in the lines without LIPH | 0.015 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[MISP]] | B | MISP activity raises BICDL2's level | lines that do not express MISP (23) vs lines expressing it (27) | 3.06× lower at baseline in the lines without MISP | 0.016 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[EPS8L1]] | B | EPS8L1 activity raises BICDL2's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without EPS8L1 | 0.023 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[LGALS4]] | B | LGALS4 activity raises BICDL2's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 4.38× lower at baseline in the lines without LGALS4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[JUP]] | B | JUP activity raises BICDL2's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.56× lower at baseline in the lines without JUP | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises BICDL2's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.58× lower at baseline in the lines without ELF3-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[NPSR1]] | B | NPSR1 activity raises BICDL2's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 5.07× lower at baseline in the lines without NPSR1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |

### Downstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 25, C 50. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | BICDL2 activity raises JUP's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 3.25× lower at baseline in the lines without BICDL2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[EPS8L1]] | B | BICDL2 activity raises EPS8L1's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 3.05× lower at baseline in the lines without BICDL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[TMC6]] | B | BICDL2 activity raises TMC6's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 2.78× lower at baseline in the lines without BICDL2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[FAM83E]] | B | BICDL2 activity raises FAM83E's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 3.24× lower at baseline in the lines without BICDL2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[MISP]] | B | BICDL2 activity raises MISP's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 3.07× lower at baseline in the lines without BICDL2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[ABHD11]] | B | BICDL2 activity raises ABHD11's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without BICDL2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[ELF3-AS1]] | B | BICDL2 activity raises ELF3-AS1's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 2.51× lower at baseline in the lines without BICDL2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[ARHGAP30]] | B | BICDL2 activity raises ARHGAP30's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 2.15× lower at baseline in the lines without BICDL2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[EPS8L1]] | B | BICDL2 activity strengthens EPS8L1's drug response | lines that do not express BICDL2 (11) vs lines expressing it (23) | the lines without BICDL2 respond 0.61× as strongly (z diff +1.25); strongest at Belinostat 5 µM: 0.65x vs 0.33x (z diff +3.9) | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | BICDL2 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express BICDL2 (22) vs lines expressing it (26) | the lines without BICDL2: 1.12× the cells of the other lines | 0.030 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[AMN]] | B | BICDL2 activity raises AMN's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without BICDL2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[TAS2R30]] | B | BICDL2 activity lowers TAS2R30's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 1.18× higher at baseline in the lines without BICDL2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.0, 54.9); signed map (60.5, 6.2). **Vector** length 44.6, 9.52% of its response variance represented; |z| ≥ 3 in 432 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.5 | -0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | BICD family like cargo adaptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,027,682-3,036,944 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CCDC64B |
| Gene groups (HGNC) | BICD family cargo adaptors |
| Matched by | ensembl_id |

UniProt [A1A5D9](https://www.uniprot.org/uniprotkb/A1A5D9) carries no function annotation.

**Summary**, from NCBI Gene [146439](https://www.ncbi.nlm.nih.gov/gene/146439):

> Predicted to enable small GTPase binding activity. Predicted to be involved in Golgi to secretory granule transport and vesicle transport along microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33584) · Entrez [146439](https://www.ncbi.nlm.nih.gov/gene/146439) · UniProt [A1A5D9](https://www.uniprot.org/uniprotkb/A1A5D9) · Ensembl [ENSG00000162069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162069)

## Data

Gene col 8476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8476); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8476]; `tensor/DDL_lfc|DDL_z.npy` [8476]; `embed/gene_vectors.npy` [8476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8476 or target_col == 8476). Every well: [[BICDL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BICDL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
