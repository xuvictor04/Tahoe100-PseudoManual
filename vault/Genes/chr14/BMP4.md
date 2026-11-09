---
symbol: "BMP4"
type: "gene"
col: 4608
ensembl_id: "ENSG00000125378"
name: "bone morphogenetic protein 4"
location: "14q22.2"
module: 55
arm: "+"
pooled_cpm: 24.41
n_lines_expressing: 19
n_dd_up: 3
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 103
direction_downstream: 95
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# BMP4

*bone morphogenetic protein 4* — 14q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +7.1, q 8e-10, up in 4 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.516× (z -4.7, q 0.001, down in 15 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (LoVo 0.0826×, LS 180 0.108×, COLO 205 0.0980×, SW48 0.126×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LS 180 0.0923×, LoVo 0.0841×, COLO 205 0.0696×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LS 180 0.204×, SW48 0.191×, COLO 205 0.206×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LoVo 0.0789×, COLO 205 0.0985×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL20RA]] (+0.84, fdr 7e-06), [[EDAR]] (+0.83, fdr 7e-06), [[C9orf152]] (+0.83, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 103 arrows point to it, the strongest [[TJP2]] → it (grade B ⚠); 95 go from it, the strongest it → [[CERCAM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4608.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +7.1 | 8e-10 | 4/17 (CFPAC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +5.5 | 8e-06 | 0/11 | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.92×** | +4.7 | 4e-04 | 8/15 (Panc 03.27, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | 1.57× | +3.3 | 0.15 | 1/17 (Panc 03.27) | rises with dose | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | 1.53× | +3.1 | 0.20 | 9/16 (SW480, SW1417, …) | two highest doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 1.53× | +3.1 | 0.20 | 11/17 (SW480, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4608.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (LoVo 0.0826×, LS 180 0.108×, COLO 205 0.0980×, SW48 0.126×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LS 180 0.0923×, LoVo 0.0841×, COLO 205 0.0696×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LS 180 0.204×, SW48 0.191×, COLO 205 0.206×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LoVo 0.0789×, COLO 205 0.0985×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.516×** | -4.7 | 0.001 | 15/17 (SW48, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.623× | -3.4 | 0.16 | 12/17 (HCT15, HT-29, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.626× | -3.3 | 0.16 | 12/17 (AsPC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.645× | -3.1 | 0.22 | 10/17 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.625× | -3.1 | 0.22 | 7/17 (COLO 205, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 149 | 0 | 22 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -18.0) |
| [[SW48 (line)]] | wt | 256 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -16.4) |
| [[LS 180 (line)]] | wt | 186 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -21.4) |
| [[LoVo (line)]] | wt | 143 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0826× (z -22.1) |
| [[SW480 (line)]] | alt | 57.3 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.5) |
| [[HT-29 (line)]] | alt | 76.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.4) |
| [[KATO III (line)]] | alt | 66.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 39.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.7) |
| [[HCT15 (line)]] | alt | 48.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0695× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 9.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -13.2) |
| [[SNU-1 (line)]] | wt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 41.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.4) |
| [[A-172 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL20RA]] | +0.84 | +0.85 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.83 | +0.83 / +0.75 | both halves | 7e-06 | STRING 627 |
| [[C9orf152]] | +0.83 | +0.75 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CLRN3]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.79 | +0.78 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.79 | +0.78 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[HNF4A]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | pathway: Kidney development; STRING 559 |
| [[LGR5]] | +0.77 | +0.76 / +0.72 | both halves | 7e-06 | STRING 475 |
| [[KCNE3]] | +0.76 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[RNF43]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LINC02331]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[GJB1]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*103 arrows, 103 of them with an alert ⚠; grade A 0, B 8, C 95. Shown: the 12 strongest; 91 more arrows (91 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TJP2]] | B | TJP2 activity raises BMP4's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 3.20× lower at baseline in the lines without TJP2 | 0.002 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[VILL]] | B | VILL activity raises BMP4's level | lines that do not express VILL (16) vs lines expressing it (34) | 2.57× lower at baseline in the lines without VILL | 0.021 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[PDE9A]] | B | PDE9A activity raises BMP4's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.47× lower at baseline in the lines without PDE9A | 0.021 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[MCF2L]] | B | MCF2L activity raises BMP4's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.88× lower at baseline in the lines without MCF2L | 0.049 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[MROH7]] | B | MROH7 activity raises BMP4's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 2.04× lower at baseline in the lines without MROH7 | 0.049 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises BMP4's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.13× lower at baseline in the lines without ZNF503-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[TNFRSF21]] | B | TNFRSF21 activity raises BMP4's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.58× lower at baseline in the lines without TNFRSF21 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[BAMBI]] | B | BAMBI activity raises BMP4's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without BAMBI | 0.065 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[LINC02331]] | C | LINC02331 activity raises BMP4's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 7.94× lower at baseline in the lines without LINC02331 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2; co-absent with the target |
| [[TNNT2]] | C | TNNT2 activity raises BMP4's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 6.25× lower at baseline in the lines without TNNT2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |
| [[EPS8L3]] | C | EPS8L3 activity raises BMP4's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 10.09× lower at baseline in the lines without EPS8L3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises BMP4's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 7.61× lower at baseline in the lines without TMEM45B | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |

### Downstream of this gene

*95 arrows, 95 of them with an alert ⚠; grade A 0, B 17, C 78. Shown: the 12 strongest; 83 more arrows (83 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERCAM]] | B | BMP4 activity lowers CERCAM's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 3.81× higher at baseline in the lines without BMP4 | 0.004 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[MROH7]] | B | BMP4 activity raises MROH7's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without BMP4 | 0.005 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[TJP2]] | B | BMP4 activity raises TJP2's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 3.04× lower at baseline in the lines without BMP4 | 0.008 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[ZNF703]] | B | BMP4 activity raises ZNF703's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.61× lower at baseline in the lines without BMP4 | 0.015 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[MAML2]] | B | BMP4 activity raises MAML2's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without BMP4 | 0.019 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[TNFRSF21]] | B | BMP4 activity raises TNFRSF21's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 3.69× lower at baseline in the lines without BMP4 | 0.019 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[SNTB1]] | B | BMP4 activity raises SNTB1's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 3.29× lower at baseline in the lines without BMP4 | 0.028 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[VILL]] | B | BMP4 activity raises VILL's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 1.99× lower at baseline in the lines without BMP4 | 0.031 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[BAMBI]] | B | BMP4 activity raises BAMBI's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.82× lower at baseline in the lines without BMP4 | 0.036 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[TOB1]] | B | BMP4 activity raises TOB1's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 1.81× lower at baseline in the lines without BMP4 | 0.037 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[LRP5]] | B | BMP4 activity raises LRP5's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.68× lower at baseline in the lines without BMP4 | 0.044 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[USP6NL]] | B | BMP4 activity raises USP6NL's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.09× lower at baseline in the lines without BMP4 | 0.045 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.867). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.4, 47.7); signed map (63.3, 11.2). **Vector** length 88.0, 38.0% of its response variance represented; |z| ≥ 3 in 498 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | -2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.2 — chr14:53,949,736-53,958,761 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BMP2B |
| Gene groups (HGNC) | Bone morphogenetic proteins |
| Reactome | 16 pathways, smallest: Formation of lateral plate mesoderm; Formation of intermediate mesoderm; Specification of primordial germ cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P12644](https://www.uniprot.org/uniprotkb/P12644) (Bone morphogenetic protein 4):

> Growth factor of the TGF-beta superfamily that plays essential roles in many developmental processes, including neurogenesis, vascular development, angiogenesis and osteogenesis. Acts in concert with PTHLH/PTHRP to stimulate ductal outgrowth during embryonic mammary development and to inhibit hair follicle induction (By similarity). Initiates the canonical BMP signaling cascade by associating with type I receptor BMPR1A and type II receptor BMPR2. Once all three components are bound together in …

**Summary**, from NCBI Gene [652](https://www.ncbi.nlm.nih.gov/gene/652):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer. This protein regulates heart development and adipogenesis. Mutations in this gene are associated with orofacial …

**Accessions** — [HGNC:1071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1071) · Entrez [652](https://www.ncbi.nlm.nih.gov/gene/652) · UniProt [P12644](https://www.uniprot.org/uniprotkb/P12644) · Ensembl [ENSG00000125378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125378)

## Data

Gene col 4608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4608); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4608]; `tensor/DDL_lfc|DDL_z.npy` [4608]; `embed/gene_vectors.npy` [4608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4608 or target_col == 4608). Every well: [[BMP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
