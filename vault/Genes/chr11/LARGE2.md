---
symbol: "LARGE2"
type: "gene"
col: 9203
ensembl_id: "ENSG00000165905"
name: "LARGE xylosyl- and glucuronyltransferase 2"
location: "11p11.2"
module: 27
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 29
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 15
direction_downstream: 11
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# LARGE2

*LARGE xylosyl- and glucuronyltransferase 2* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.15× (z +11.9, q 5e-30, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.09× (z +7.9, q 4e-13, up in 2 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.605× (z -3.8, q 0.081, down in 8 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.350×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.0792×; ⚠ cell-cycle shift, explains ~47% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTPA]] (+0.65, fdr 1e-05), [[SLC27A2]] (+0.65, fdr 7e-06), [[APCDD1]] (+0.64, fdr 1e-05); moves opposite to [[CSNK1A1]] (-0.46, fdr 3e-05), [[BCL10-AS1]] (-0.45, fdr 1e-04), [[MED29]] (-0.45, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[MEST]] → it (grade B ⚠); 11 go from it, the strongest it → [[NMNAT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.15×** | +11.9 | 5e-30 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.74×** | +10.0 | 6e-21 | 2/7 (LS 180, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.86×** | +9.5 | 6e-19 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +7.9 | 4e-13 | 2/15 (HOP62, NCI-H2347) | top dose only | cell-cycle shift (explains ~5% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.97×** | +5.9 | 5e-07 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +5.2 | 2e-05 | 0/23 | top dose only | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +4.9 | 7e-05 | 4/11 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +4.9 | 7e-05 | 10/22 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.8 | 1e-04 | 1/8 (SHP-77) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +4.7 | 2e-04 | 5/23 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.002 | 0/14 | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.67×** | +3.9 | 0.005 | 0/9 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.008 | 0/15 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +3.6 | 0.011 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.48×** | +3.6 | 0.013 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.027 | 1/9 (LS 180) | inconsistent across doses | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.027 | 0/21 | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.55×** | +3.2 | 0.033 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.58×** | +3.2 | 0.036 | 0/10 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.045 | 0/14 | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +3.0 | 0.060 | 5/23 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9203.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.350×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.0792×; ⚠ cell-cycle shift, explains ~47% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.605×** | -3.8 | 0.081 | 8/24 (BT-474, RKO, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.5 µM |  | 0.656× | -3.2 | 0.39 | 3/20 (NCI-H1792, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Artesunate (drug)]] 5 µM |  | 0.754× | -3.0 | 0.47 | 10/23 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0792× (z -8.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW480 (line)]] | alt | 14.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -9.1) |
| [[A-172 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.915 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.159 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.653 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.865 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.886 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.571 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.316 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.163 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.768 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.569 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.693 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.202 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.549 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.692 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTPA]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SLC27A2]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[APCDD1]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[KLK7]] | +0.60 | +0.63 / +0.26 | both halves | 4e-04 |  |
| [[VWA2]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SEMA4G]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MEST]] | +0.58 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[KCNE3]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SMPDL3B]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[FGF20]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[NMNAT3]] | +0.56 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[EMID1]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 | pathway: O-linked glycosylation |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK1A1]] | -0.46 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[BCL10-AS1]] | -0.45 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[MED29]] | -0.45 | -0.32 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 6, C 9. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEST]] | B | MEST activity raises LARGE2's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.86× lower at baseline in the lines without MEST | 0.011 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[KLK7]] | B | KLK7 activity raises LARGE2's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 2.23× lower at baseline in the lines without KLK7 | 0.027 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3 |
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises LARGE2's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 1.79× lower at baseline in the lines without ZNF503-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[NOTUM]] | B | NOTUM activity raises LARGE2's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without NOTUM | 0.041 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7 |
| [[JAKMIP2-AS1]] | B | JAKMIP2-AS1 activity raises LARGE2's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 1.46× lower at baseline in the lines without JAKMIP2-AS1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[NMNAT3]] | B | NMNAT3 activity raises LARGE2's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.80× lower at baseline in the lines without NMNAT3 | 0.097 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[SMPDL3B]] | C | SMPDL3B activity raises LARGE2's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.38× lower at baseline in the lines without SMPDL3B | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises LARGE2's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without SKAP1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[PRR36]] | C | PRR36 activity raises LARGE2's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without PRR36 | 0.023 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises LARGE2's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 2.36× lower at baseline in the lines without VWA2 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[CKMT1A]] | C | CKMT1A activity raises LARGE2's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without CKMT1A | 0.037 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |
| [[CKMT1B]] | C | CKMT1B activity raises LARGE2's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without CKMT1B | 0.043 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMNAT3]] | B | LARGE2 activity raises NMNAT3's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 2.68× lower at baseline in the lines without LARGE2 | 0.057 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[COPG2IT1]] | B | LARGE2 activity raises COPG2IT1's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without LARGE2 | 0.068 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[SEMA4G]] | B | LARGE2 activity raises SEMA4G's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 2.13× lower at baseline in the lines without LARGE2 | 0.069 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[GPR143]] | B | LARGE2 activity raises GPR143's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 1.62× lower at baseline in the lines without LARGE2 | 0.070 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[MEST]] | B | LARGE2 activity raises MEST's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 1.51× lower at baseline in the lines without LARGE2 | 0.071 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[FGFR4]] | B | LARGE2 activity raises FGFR4's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 1.69× lower at baseline in the lines without LARGE2 | 0.074 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[LINC01819]] | B | LARGE2 activity raises LINC01819's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 1.28× lower at baseline in the lines without LARGE2 | 0.097 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[SMPDL3B]] | C | LARGE2 activity raises SMPDL3B's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 2.33× lower at baseline in the lines without LARGE2 | 0.016 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2; co-absent with the target |
| [[SKAP1]] | C | LARGE2 activity raises SKAP1's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 2.84× lower at baseline in the lines without LARGE2 | 0.054 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2; co-absent with the target |
| [[PROM1]] | C | LARGE2 activity raises PROM1's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without LARGE2 | 0.068 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2; co-absent with the target |
| [[SLC29A2]] | C | LARGE2 activity raises SLC29A2's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 2.51× lower at baseline in the lines without LARGE2 | 0.077 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.2, 44.2); signed map (60.2, 14.1). **Vector** length 32.8, 5.54% of its response variance represented; |z| ≥ 3 in 494 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.1 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.9 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -1.2 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -0.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | LARGE xylosyl- and glucuronyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:45,921,621-45,929,096 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP5656, FLJ35207; previously GYLTL1B |
| Gene groups (HGNC) | Glycosyltransferase family 8 |
| Reactome | 3 pathways, smallest: Matriglycan biosynthesis on DAG1; DAG1 glycosylations; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3Y3](https://www.uniprot.org/uniprotkb/Q8N3Y3) (Xylosyl- and glucuronyltransferase LARGE2):

> Bifunctional glycosyltransferase with both alpha-1,3-xylosyltransferase and beta-1,3-glucuronyltransferase activities involved in the maturation of alpha-dystroglycan (DAG1) by glycosylation leading to DAG1 binding to laminin G-like domain-containing extracellular proteins with high affinity and in a phosphorylated-O-mannosyl trisaccharide dependent manner. Elongates the glucuronyl-beta-1,4-xylose-beta disaccharide primer structure by adding repeating units [-3-Xylose-alpha-1,3-GlcA-beta-1-] to …

**Summary**, from NCBI Gene [120071](https://www.ncbi.nlm.nih.gov/gene/120071):

> Predicted to enable dystroglycan binding activity; glucuronosyltransferase activity; and xylosyltransferase activity. Involved in protein O-linked glycosylation via mannose. Predicted to be located in Golgi membrane. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16522) · Entrez [120071](https://www.ncbi.nlm.nih.gov/gene/120071) · UniProt [Q8N3Y3](https://www.uniprot.org/uniprotkb/Q8N3Y3) · Ensembl [ENSG00000165905](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165905)

## Data

Gene col 9203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9203); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9203]; `tensor/DDL_lfc|DDL_z.npy` [9203]; `embed/gene_vectors.npy` [9203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9203 or target_col == 9203). Every well: [[LARGE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LARGE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
