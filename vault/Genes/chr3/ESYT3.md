---
symbol: "ESYT3"
type: "gene"
col: 8144
ensembl_id: "ENSG00000158220"
name: "extended synaptotagmin 3"
location: "3q22.3"
module: 82
arm: "+"
pooled_cpm: 2.45
n_lines_expressing: 35
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# ESYT3

*extended synaptotagmin 3* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.05× (z +14.7, q 0e+00, up in 12 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.634× (z -4.3, q 0.011, down in 8 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0697×, SW480 0.219×; ⚠ cell-cycle shift, explains ~59% of this change); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0589×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.162×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.132×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LPAR3]] (+0.67, fdr 1e-05), [[LHX6]] (+0.62, fdr 4e-05), [[LMX1B]] (+0.61, fdr 4e-05); moves opposite to [[TBCK]] (-0.52, fdr 5e-05), [[GET3]] (-0.49, fdr 5e-05), [[ALOX12-AS1]] (-0.49, fdr 5e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LHX6]] → it (grade B ⚠); 3 go from it, the strongest it → [[FHOD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +14.7 | 0e+00 | 12/18 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.04×** | +10.4 | 8e-23 | 23/26 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.94×** | +10.1 | 1e-21 | 24/28 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +9.8 | 1e-20 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +9.3 | 3e-18 | 21/27 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +8.8 | 2e-16 | 9/21 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.54×** | +8.7 | 3e-16 | 18/26 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +7.4 | 1e-11 | 15/21 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +7.1 | 9e-11 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +6.3 | 2e-08 | 0/9 | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.7 | 5e-07 | 1/12 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +5.2 | 7e-06 | 10/17 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +4.7 | 1e-04 | 18/28 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.41×** | +4.5 | 3e-04 | 5/29 (SW480, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.59×** | +4.3 | 7e-04 | 5/15 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.3 | 7e-04 | 2/16 (LS 180, NCI-H1792) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +3.8 | 0.004 | 6/22 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +3.5 | 0.014 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.014 | 5/20 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.014 | 2/19 (HOP62, SW1417) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8144.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0697×, SW480 0.219×; ⚠ cell-cycle shift, explains ~59% of this change); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0589×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.162×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.132×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -4.3 | 0.011 | 8/25 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.691× | -3.5 | 0.15 | 13/29 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.72 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 12.4× (z +9.6) | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0589× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 4.41 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0697× (z -11.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.132× (z -8.5) |
| [[SW480 (line)]] | alt | 8.33 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.871 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.682 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.885 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.757 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.666 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.696 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.801 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.431 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPAR3]] | +0.67 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[LHX6]] | +0.62 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[LMX1B]] | +0.61 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[MCOLN2]] | +0.59 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PAX9]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CACNG7]] | +0.58 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[PTPN20]] | +0.58 | +0.60 / +0.32 | both halves | 1e-04 |  |
| [[HEYL]] | +0.57 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[BMP8B]] | +0.57 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[SLC66A1L]] | +0.57 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[MAP6]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[SEMA4F]] | +0.55 | +0.31 / +0.57 | both halves | 2e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCK]] | -0.52 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[GET3]] | -0.49 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[ALOX12-AS1]] | -0.49 | -0.23 / -0.30 | both halves | 5e-04 |  |
| [[CLHC1]] | -0.49 | -0.12 / -0.40 | ⚠ not reproduced | 0.002 |  |
| [[FTX]] | -0.49 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[SUMF1]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TMEM199]] | -0.48 | -0.15 / -0.48 | ⚠ not reproduced | 0.001 |  |
| [[GGPS1]] | -0.47 | -0.21 / -0.36 | both halves | 7e-04 |  |
| [[VPS35L]] | -0.47 | -0.21 / -0.49 | both halves | 7e-04 |  |
| [[ZCWPW2]] | -0.47 | -0.27 / -0.26 | both halves | 4e-04 |  |
| [[DNAI4]] | -0.46 | -0.18 / -0.28 | ⚠ not reproduced | 9e-04 |  |
| [[ZRANB2-DT]] | -0.46 | -0.24 / -0.46 | both halves | 4e-04 |  |
| [[CFAP44]] | -0.46 | -0.38 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHX6]] | B | LHX6 activity raises ESYT3's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without LHX6 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[CSF2RA]] | B | CSF2RA activity raises ESYT3's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 1.60× lower at baseline in the lines without CSF2RA | 0.034 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A |
| [[MAP6]] | B | MAP6 activity raises ESYT3's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without MAP6 | 0.050 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91 |
| [[OCA2]] | B | OCA2 activity raises ESYT3's level | lines that do not express OCA2 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without OCA2 | 0.067 | ⚠ within organs, on part of the lines; also absent: BEX4, STAC, ATP10A; maybe low, not absent |
| [[VPS35L]] | B | VPS35L activity raises ESYT3's level | lines that do not express VPS35L (9) vs lines expressing it (41) | 1.69× lower at baseline in the lines without VPS35L | 0.077 | ⚠ within organs, on part of the lines; also absent: HDGFL3, CHST11, RNF150 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FHOD3]] | B | ESYT3 activity raises FHOD3's level | lines that do not express ESYT3 (15) vs lines expressing it (35) | 2.92× lower at baseline in the lines without ESYT3 | 0.015 | ⚠ within organs, on part of the lines; also absent: BEND6, ENSG00000224905, ZNF354C; maybe low, not absent |
| [[KIF5A]] | B | ESYT3 activity strengthens KIF5A's drug response | lines that do not express ESYT3 (13) vs lines expressing it (30) | the lines without ESYT3 respond 0.60× as strongly (z diff +1.06); strongest at Panobinostat 0.5 µM: 1.48x vs 3.11x (z diff +2.3) | 0.063 | ⚠ within organs, on part of the lines; also absent: BEND6, ENSG00000224905, ZNF354C; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SYT11]] | B | ESYT3 activity raises SYT11's level | lines that do not express ESYT3 (15) vs lines expressing it (35) | 2.00× lower at baseline in the lines without ESYT3 | 0.089 | ⚠ within organs, on part of the lines; also absent: BEND6, ENSG00000224905, ZNF354C; maybe low, not absent |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.8, 39.8); signed map (-24.7, 33.6). **Vector** length 37.0, 5.70% of its response variance represented; |z| ≥ 3 in 645 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -1.4 | -0.8 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | +1.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | extended synaptotagmin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:138,434,586-138,481,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CHR3SYT; previously FAM62C |
| Gene groups (HGNC) | Extended synaptotagmins |
| Reactome | 2 pathways, smallest: Glycosphingolipid transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [A0FGR9](https://www.uniprot.org/uniprotkb/A0FGR9) (Extended synaptotagmin-3):

> Binds glycerophospholipids in a barrel-like domain and may play a role in cellular lipid transport (By similarity). Tethers the endoplasmic reticulum to the cell membrane and promotes the formation of appositions between the endoplasmic reticulum and the cell membrane.

**Summary**, from NCBI Gene [83850](https://www.ncbi.nlm.nih.gov/gene/83850):

> Predicted to enable calcium ion binding activity; phosphatidylinositol binding activity; and phospholipid binding activity. Predicted to be involved in endoplasmic reticulum-plasma membrane tethering and lipid transport. Located in cytoplasmic side of plasma membrane; endoplasmic reticulum membrane; and endoplasmic reticulum-plasma membrane contact site. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24295) · Entrez [83850](https://www.ncbi.nlm.nih.gov/gene/83850) · UniProt [A0FGR9](https://www.uniprot.org/uniprotkb/A0FGR9) · Ensembl [ENSG00000158220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158220)

## Data

Gene col 8144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8144); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8144]; `tensor/DDL_lfc|DDL_z.npy` [8144]; `embed/gene_vectors.npy` [8144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8144 or target_col == 8144). Every well: [[ESYT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESYT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
