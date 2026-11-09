---
symbol: "NRARP"
type: "gene"
col: 12591
ensembl_id: "ENSG00000198435"
name: "NOTCH regulated ankyrin repeat protein"
location: "9q34.3"
module: 162
arm: "+"
pooled_cpm: 6.2
n_lines_expressing: 36
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 12
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# NRARP

*NOTCH regulated ankyrin repeat protein* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.05× (z +15.8, q 0e+00, up in 22 of 29 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 4.05× (z +11.2, q 1e-26, up in 24 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (PANC-1 0.248×, SW480 0.329×, LS 180 0.308×; ⚠ cell-cycle shift, explains ~15% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP2]] (+0.72, fdr 7e-06), [[MIR23AHG]] (+0.64, fdr 2e-05), [[NKD2]] (+0.61, fdr 1e-05); moves opposite to [[LNPK]] (-0.50, fdr 2e-05), [[VPS37A]] (-0.50, fdr 2e-04), [[EXD2]] (-0.46, fdr 2e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CPLX1]] → it (grade B ⚠); 12 go from it, the strongest it → [[APCDD1L-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **4.05×** | +15.8 | 0e+00 | 22/29 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.05×** | +11.2 | 1e-26 | 24/31 (SW480, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.21×** | +11.0 | 5e-26 | 3/10 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.89×** | +10.4 | 2e-23 | 19/22 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.62×** | +10.3 | 1e-22 | 14/16 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.60×** | +9.8 | 7e-21 | 14/19 (KATO III, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.15×** | +9.2 | 5e-18 | 17/26 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.22×** | +9.0 | 2e-17 | 21/31 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.65×** | +7.8 | 4e-13 | 19/33 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.74×** | +7.2 | 3e-11 | 10/12 (SW1417, AsPC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +6.8 | 8e-10 | 18/27 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +6.7 | 1e-09 | 20/31 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +6.6 | 2e-09 | 14/31 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.80×** | +4.7 | 1e-04 | 12/33 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.77×** | +4.5 | 2e-04 | 16/32 (NCI-H460, A549, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +4.5 | 2e-04 | 10/30 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12591.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (PANC-1 0.248×, SW480 0.329×, LS 180 0.308×; ⚠ cell-cycle shift, explains ~15% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.618× | -3.5 | 0.28 | 8/32 (SW480, A549, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.662× | -3.3 | 0.28 | 9/33 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.09 | 11 (10 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 75.3× (z +13.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 28.7× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.97 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 49.4× (z +17.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 22.5× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 6.18 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +9.8) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -10.0) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW480 (line)]] | alt | 16.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.61× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.0) ⚠ cell-cycle shift, explains ~15% of this change |
| [[AsPC-1 (line)]] | alt | 6.59 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.4× (z +14.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 31.7 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.81× (z +9.5) ⚠ toxic | — |
| [[CFPAC-1 (line)]] | alt | 3.87 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +10.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 12.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -8.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW48 (line)]] | wt | 34.8 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.87× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 0.981 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP2]] | +0.72 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[MIR23AHG]] | +0.64 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[NKD2]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[LINC02968]] | +0.58 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[IER3]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[JUNB]] | +0.53 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[CPLX1]] | +0.53 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ASTL]] | +0.53 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ARL14]] | +0.53 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[OLFM2]] | +0.52 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[IER2]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | +0.52 | +0.59 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNPK]] | -0.50 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[VPS37A]] | -0.50 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[EXD2]] | -0.46 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MIGA1]] | -0.46 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ALG5]] | -0.45 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[CLCC1]] | -0.45 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[JKAMP]] | -0.45 | -0.54 / -0.37 | both halves | 7e-05 |  |
| [[MFSD8]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[SELENOF]] | -0.44 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[MRPL13]] | -0.44 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ZDHHC7]] | -0.43 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[RTCA]] | -0.43 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPLX1]] | B | CPLX1 activity raises NRARP's level | lines that do not express CPLX1 (9) vs lines expressing it (41) | 2.52× lower at baseline in the lines without CPLX1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LLGL2, CASZ1, MNX1; maybe low, not absent |
| [[TRIM15]] | B | TRIM15 activity raises NRARP's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 3.38× lower at baseline in the lines without TRIM15 | 0.048 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[ABHD11]] | B | ABHD11 activity raises NRARP's level | lines that do not express ABHD11 (8) vs lines expressing it (42) | 2.23× lower at baseline in the lines without ABHD11 | 0.064 | ⚠ within organs, on part of the lines; also absent: E2F2, CXCL16, ABLIM2; maybe low, not absent |
| [[SHH]] | B | SHH activity raises NRARP's level | lines that do not express SHH (29) vs lines expressing it (21) | 2.55× lower at baseline in the lines without SHH | 0.072 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity lowers NRARP's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.37× higher at baseline in the lines without APCDD1L-DT | 0.075 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[EPPK1]] | C | EPPK1 activity raises NRARP's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 2.68× lower at baseline in the lines without EPPK1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3; co-absent with the target |
| [[PRSS22]] | C | PRSS22 activity raises NRARP's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 3.20× lower at baseline in the lines without PRSS22 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14; co-absent with the target |
| [[KRT18]] | C | KRT18 activity raises NRARP's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 2.61× lower at baseline in the lines without KRT18 | 0.048 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent; co-absent with the target |
| [[SYP]] | C | SYP activity raises NRARP's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APCDD1L-DT]] | B | NRARP activity lowers APCDD1L-DT's level | lines that do not express NRARP (14) vs lines expressing it (36) | 6.13× higher at baseline in the lines without NRARP | 0.001 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[TGFB1]] | B | NRARP activity lowers TGFB1's level | lines that do not express NRARP (14) vs lines expressing it (36) | 2.36× higher at baseline in the lines without NRARP | 0.011 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[C11orf96]] | B | NRARP activity lowers C11orf96's level | lines that do not express NRARP (14) vs lines expressing it (36) | 1.96× higher at baseline in the lines without NRARP | 0.012 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[DOT1L]] | B | NRARP activity lowers DOT1L's level | lines that do not express NRARP (14) vs lines expressing it (36) | 1.39× higher at baseline in the lines without NRARP | 0.022 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[CPLX1]] | B | NRARP activity raises CPLX1's level | lines that do not express NRARP (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without NRARP | 0.029 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[ABHD11]] | B | NRARP activity raises ABHD11's level | lines that do not express NRARP (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without NRARP | 0.040 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[ANKDD1A]] | B | NRARP activity lowers ANKDD1A's level | lines that do not express NRARP (14) vs lines expressing it (36) | 1.54× higher at baseline in the lines without NRARP | 0.051 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[LINC02901]] | B | NRARP activity raises LINC02901's level | lines that do not express NRARP (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without NRARP | 0.062 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[TGFB1]] | B | NRARP activity weakens TGFB1's drug response | lines that do not express NRARP (12) vs lines expressing it (28) | the lines without NRARP respond 1.29× as strongly (z diff -0.79); strongest at Topotecan (hydrochloride) 5 µM: 0.51x vs 0.87x (z diff -5.2) | 0.073 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A; target measured in part of the lines; both ways; artifact flags |
| [[ANKDD1A]] | B | NRARP activity weakens ANKDD1A's drug response | lines that do not express NRARP (14) vs lines expressing it (33) | the lines without NRARP respond 1.18× as strongly (z diff -0.43); strongest at Homoharringtonine 5 µM: 5.17x vs 1.10x (z diff -8.3) | 0.075 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A; target measured in part of the lines; both ways; artifact flags |
| [[KRT18]] | C | NRARP activity raises KRT18's level | lines that do not express NRARP (14) vs lines expressing it (36) | 4.45× lower at baseline in the lines without NRARP | 0.013 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A; co-absent with the target |
| [[EPPK1]] | C | NRARP activity raises EPPK1's level | lines that do not express NRARP (14) vs lines expressing it (36) | 3.60× lower at baseline in the lines without NRARP | 0.045 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A; co-absent with the target |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.5, -1.1); signed map (6.1, 27.7). **Vector** length 71.7, 17.0% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.6 | +15.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.1 | +9.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +0.8 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -2.1 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | NOTCH regulated ankyrin repeat protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,299,631-137,302,271 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC61598 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6K4](https://www.uniprot.org/uniprotkb/Q7Z6K4) (Notch-regulated ankyrin repeat-containing protein):

> Downstream effector of Notch signaling. Involved in the regulation of liver cancer cells self-renewal. Involved in angiogenesis acting downstream of Notch at branch points to regulate vascular density. Proposed to integrate endothelial Notch and Wnt signaling to control stalk cell proliferation and to stablilize new endothelial connections during angiogenesis. During somitogenesis involved in maintenance of proper somite segmentation and proper numbers of somites and vertebrae. Required for …

**Summary**, from NCBI Gene [441478](https://www.ncbi.nlm.nih.gov/gene/441478):

> Involved in Notch signaling pathway. Acts upstream of or within negative regulation of Notch signaling pathway and positive regulation of canonical Wnt signaling pathway. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33843) · Entrez [441478](https://www.ncbi.nlm.nih.gov/gene/441478) · UniProt [Q7Z6K4](https://www.uniprot.org/uniprotkb/Q7Z6K4) · Ensembl [ENSG00000198435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198435)

## Data

Gene col 12591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12591); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12591]; `tensor/DDL_lfc|DDL_z.npy` [12591]; `embed/gene_vectors.npy` [12591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12591 or target_col == 12591). Every well: [[NRARP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRARP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
