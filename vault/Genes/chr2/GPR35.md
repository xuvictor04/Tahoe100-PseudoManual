---
symbol: "GPR35"
type: "gene"
col: 10943
ensembl_id: "ENSG00000178623"
name: "G protein-coupled receptor 35"
location: "2q37.3"
module: 31
arm: "+"
pooled_cpm: 5.22
n_lines_expressing: 21
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 97
direction_downstream: 103
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# GPR35

*G protein-coupled receptor 35* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.11× (z +11.0, q 3e-25, up in 5 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.257×, SW1417 0.389×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.371×, KATO III 0.290×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LS 180 0.170×; ⚠ cell-cycle shift, explains ~55% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GNT3]] (+0.84, fdr 7e-06), [[MST1R]] (+0.79, fdr 7e-06), [[EPS8L3]] (+0.73, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 97 arrows point to it, the strongest [[BNC2]] → it (grade B ⚠); 103 go from it, the strongest it → [[MROH7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.11×** | +11.0 | 3e-25 | 5/18 (NCI-H23, BT-474, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.97×** | +10.1 | 1e-21 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +9.2 | 5e-18 | 1/11 (SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +9.0 | 5e-17 | 0/15 | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +7.5 | 5e-12 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +5.9 | 4e-07 | 2/16 (AsPC-1, COLO 205) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.4 | 6e-06 | 1/13 (NCI-H1573) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.49×** | +3.9 | 0.008 | 4/16 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.008 | 1/17 (AsPC-1) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.009 | 1/14 (SW48) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.7 | 0.010 | 1/14 (COLO 205) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.017 | 2/16 (HT-29, HCT15) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +3.6 | 0.017 | 3/18 (AsPC-1, LoVo, …) | top dose only | low cells (technical?) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.45×** | +3.4 | 0.032 | 2/14 (KATO III, NCI-H1573) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.2 | 0.058 | 2/14 (CFPAC-1, HT-29) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10943.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.257×, SW1417 0.389×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.371×, KATO III 0.290×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LS 180 0.170×; ⚠ cell-cycle shift, explains ~55% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.732× | -3.1 | 0.90 | 4/17 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 13.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -9.7) |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -12.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 25.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -9.2) |
| [[A-172 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.825 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.931 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GNT3]] | +0.84 | +0.78 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[MST1R]] | +0.79 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[LINC03040]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ITGB4]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[INPP5D]] | +0.71 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[PADI1]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[ONECUT3]] | +0.70 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SLC5A1]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[HNF4A]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*97 arrows, 97 of them with an alert ⚠; grade A 0, B 16, C 81. Shown: the 12 strongest; 85 more arrows (85 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BNC2]] | B | BNC2 activity lowers GPR35's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 3.84× higher at baseline in the lines without BNC2 | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[PLEKHG1]] | B | PLEKHG1 activity raises GPR35's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.24× lower at baseline in the lines without PLEKHG1 | 0.012 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[TGFA]] | B | TGFA activity raises GPR35's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.57× lower at baseline in the lines without TGFA | 0.013 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[ZNF860]] | B | ZNF860 activity raises GPR35's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.57× lower at baseline in the lines without ZNF860 | 0.013 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[PRAG1]] | B | PRAG1 activity raises GPR35's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without PRAG1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[TTC28]] | B | TTC28 activity lowers GPR35's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 4.87× higher at baseline in the lines without TTC28 | 0.015 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[TJP2]] | B | TJP2 activity raises GPR35's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.24× lower at baseline in the lines without TJP2 | 0.027 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity raises GPR35's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.59× lower at baseline in the lines without MCF2L | 0.044 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[MROH7]] | B | MROH7 activity raises GPR35's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without MROH7 | 0.049 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[DCLK2]] | B | DCLK2 activity lowers GPR35's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 4.08× higher at baseline in the lines without DCLK2 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[VILL]] | B | VILL activity raises GPR35's level | lines that do not express VILL (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without VILL | 0.052 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[MYEOV]] | B | MYEOV activity raises GPR35's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 1.83× lower at baseline in the lines without MYEOV | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |

### Downstream of this gene

*103 arrows, 103 of them with an alert ⚠; grade A 0, B 30, C 73. Shown: the 12 strongest; 91 more arrows (91 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MROH7]] | B | GPR35 activity raises MROH7's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 2.89× lower at baseline in the lines without GPR35 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[TLDC2]] | B | GPR35 activity raises TLDC2's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 2.26× lower at baseline in the lines without GPR35 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[BNC2]] | B | GPR35 activity lowers BNC2's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 7.03× higher at baseline in the lines without GPR35 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[ACOT11]] | B | GPR35 activity raises ACOT11's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 3.03× lower at baseline in the lines without GPR35 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[BAIAP2L2]] | B | GPR35 activity raises BAIAP2L2's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 2.71× lower at baseline in the lines without GPR35 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[ARHGAP27]] | B | GPR35 activity raises ARHGAP27's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 2.40× lower at baseline in the lines without GPR35 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[NUDT4]] | B | GPR35 activity raises NUDT4's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 1.80× lower at baseline in the lines without GPR35 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[EPS8L1]] | B | GPR35 activity raises EPS8L1's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 3.45× lower at baseline in the lines without GPR35 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[TGFA]] | B | GPR35 activity raises TGFA's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 3.37× lower at baseline in the lines without GPR35 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[SDCBP2]] | B | GPR35 activity raises SDCBP2's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 3.55× lower at baseline in the lines without GPR35 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[PTK6]] | B | GPR35 activity raises PTK6's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 2.70× lower at baseline in the lines without GPR35 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[DCLK2]] | B | GPR35 activity lowers DCLK2's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 3.58× higher at baseline in the lines without GPR35 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, 51.6); signed map (61.0, 9.8). **Vector** length 45.7, 12.3% of its response variance represented; |z| ≥ 3 in 380 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +9.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +7.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +1.8 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:240,605,430-240,633,159 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Reactome | 3 pathways, smallest: Class A/1 (Rhodopsin-like receptors); GPCR ligand binding; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC97](https://www.uniprot.org/uniprotkb/Q9HC97) (G protein-coupled receptor 35):

> G protein-coupled receptor that binds to several ligands including the tryptophan metabolite kynurenic acid (KYNA), lysophosphatidic acid (LPA) or 5-hydroxyindoleacetic acid (5-HIAA) with high affinity, leading to rapid and transient activation of numerous intracellular signaling pathways. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase. GPR35 …

**Summary**, from NCBI Gene [2859](https://www.ncbi.nlm.nih.gov/gene/2859):

> Enables C-X-C chemokine receptor activity. Involved in several processes, including leukocyte chemotaxis; negative regulation of cardiac muscle cell apoptotic process; and response to ischemia. Acts upstream of or within chemokine-mediated signaling pathway. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4492) · Entrez [2859](https://www.ncbi.nlm.nih.gov/gene/2859) · UniProt [Q9HC97](https://www.uniprot.org/uniprotkb/Q9HC97) · Ensembl [ENSG00000178623](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178623)

## Data

Gene col 10943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10943); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10943]; `tensor/DDL_lfc|DDL_z.npy` [10943]; `embed/gene_vectors.npy` [10943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10943 or target_col == 10943). Every well: [[GPR35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
