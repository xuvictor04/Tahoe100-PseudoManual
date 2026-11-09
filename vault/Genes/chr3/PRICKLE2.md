---
symbol: "PRICKLE2"
type: "gene"
col: 8742
ensembl_id: "ENSG00000163637"
name: "prickle planar cell polarity protein 2"
location: "3p14.1"
module: 13
arm: "+"
pooled_cpm: 32.23
n_lines_expressing: 30
n_dd_up: 2
n_dd_down: 42
n_dd_up_clean: 2
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 19
direction_downstream: 6
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PRICKLE2

*prickle planar cell polarity protein 2* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.85× (z +10.2, q 1e-21, up in 24 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (SW480 3.06×, HEC-1-A 2.08×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (A549 5.04×; ⚠ unreliable plate only).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.460× (z -12.7, q 3e-34, down in 22 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNG2]] (+0.59, fdr 1e-05), [[EDNRA]] (+0.59, fdr 2e-05), [[CARMN]] (+0.58, fdr 1e-05); moves opposite to [[PATJ]] (-0.50, fdr 4e-05), [[PDCD6P1]] (-0.46, fdr 5e-05), [[MYO16-AS1]] (-0.44, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[LINC02882]] → it (grade B ⚠); 6 go from it, the strongest it → [[CDC42EP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8742.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (SW480 3.06×, HEC-1-A 2.08×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (A549 5.04×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +10.2 | 1e-21 | 24/28 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +5.6 | 8e-06 | 18/28 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.32× | +3.2 | 0.23 | 9/28 (NCI-H2347, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8742.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.460×** | -12.7 | 3e-34 | 22/27 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.453×** | -9.2 | 1e-17 | 24/28 (H4, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -8.1 | 1e-13 | 23/28 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.433×** | -7.9 | 2e-13 | 21/26 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.615×** | -7.9 | 2e-13 | 22/28 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.486×** | -7.7 | 1e-12 | 20/25 (SNU-423, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.508×** | -7.5 | 4e-12 | 18/26 (LOX-IMVI, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.532×** | -7.0 | 2e-10 | 18/27 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.578×** | -6.3 | 2e-08 | 15/28 (HEC-1-A, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.586×** | -6.2 | 4e-08 | 18/28 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -5.6 | 9e-07 | 21/28 (SHP-77, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.607×** | -5.5 | 1e-06 | 17/27 (J82, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.730×** | -5.1 | 1e-05 | 17/28 (A-172, RPMI-7951, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.650×** | -5.0 | 3e-05 | 15/28 (HS-578T, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -4.9 | 3e-05 | 14/28 (SNU-423, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -4.9 | 4e-05 | 15/28 (LOX-IMVI, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.660×** | -4.8 | 5e-05 | 16/28 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -4.6 | 1e-04 | 15/28 (SHP-77, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.673×** | -4.6 | 1e-04 | 20/28 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -4.3 | 4e-04 | 15/28 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.659×** | -3.9 | 0.002 | 15/27 (C32, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 163 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -15.8) |
| [[A-172 (line)]] | wt | 130 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -16.3) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -13.6) |
| [[SHP-77 (line)]] | alt | 75.8 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -12.5) |
| [[HS-578T (line)]] | alt | 103 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.4) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -11.5) |
| [[A498 (line)]] | wt | 82.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -8.8) |
| [[HOP62 (line)]] | alt | 64.9 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -10.6) |
| [[C32 (line)]] | wt | 46.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0600× (z -13.2) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.188× (z -9.5) |
| [[H4 (line)]] | wt | 40.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0377× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.131× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 44.6 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0907× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 139 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0749× (z -14.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 31.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 43.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.04× (z +9.7) ⚠ unreliable plate only | — |
| [[HEC-1-A (line)]] | alt | 68.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.08× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 86.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -9.9) |
| [[J82 (line)]] | alt | 9.70 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 28.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 37.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -10.0) |
| [[SW480 (line)]] | alt | 10.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.06× (z +9.8) | — |
| [[A-427 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.19 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG2]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[EDNRA]] | +0.59 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CARMN]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PRRX1]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[NAV1]] | +0.55 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[LINC01242]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[GLIS3]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ADAMTS12]] | +0.54 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ARMCX2]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[PTGFR]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ZNF521]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[KC6]] | +0.52 | +0.43 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATJ]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PDCD6P1]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[MYO16-AS1]] | -0.44 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[DUSP22]] | -0.43 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[DPY19L2P3]] | -0.41 | -0.27 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02882]] | B | LINC02882 activity raises PRICKLE2's level | lines that do not express LINC02882 (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without LINC02882 | 0.069 | ⚠ within organs, on part of the lines; also absent: VGLL3, ANXA10, DDX43 |
| [[EDNRA]] | C | EDNRA activity raises PRICKLE2's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 4.43× lower at baseline in the lines without EDNRA | 0.002 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises PRICKLE2's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 5.28× lower at baseline in the lines without ADAMTS12 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[SNAI2]] | C | SNAI2 activity raises PRICKLE2's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 4.72× lower at baseline in the lines without SNAI2 | 0.009 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT; co-absent with the target |
| [[ZNF521]] | C | ZNF521 activity raises PRICKLE2's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 3.16× lower at baseline in the lines without ZNF521 | 0.020 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4; co-absent with the target |
| [[APBB1IP]] | C | APBB1IP activity raises PRICKLE2's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 4.73× lower at baseline in the lines without APBB1IP | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[COL7A1]] | C | COL7A1 activity raises PRICKLE2's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 3.91× lower at baseline in the lines without COL7A1 | 0.027 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |
| [[ARHGAP24]] | C | ARHGAP24 activity raises PRICKLE2's level | lines that do not express ARHGAP24 (17) vs lines expressing it (33) | 4.30× lower at baseline in the lines without ARHGAP24 | 0.032 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176; co-absent with the target |
| [[SETBP1]] | C | SETBP1 activity raises PRICKLE2's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 4.80× lower at baseline in the lines without SETBP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[TNS1]] | C | TNS1 activity raises PRICKLE2's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 3.73× lower at baseline in the lines without TNS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises PRICKLE2's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 3.69× lower at baseline in the lines without WNT5A | 0.038 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[GNG2]] | C | GNG2 activity raises PRICKLE2's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 3.71× lower at baseline in the lines without GNG2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42EP3]] | B | PRICKLE2 activity raises CDC42EP3's level | lines that do not express PRICKLE2 (20) vs lines expressing it (30) | 3.08× lower at baseline in the lines without PRICKLE2 | 0.033 | ⚠ within organs, on part of the lines; also absent: SNAI2, STK32A, LINC00973 |
| [[SETBP1]] | C | PRICKLE2 activity raises SETBP1's level | lines that do not express PRICKLE2 (20) vs lines expressing it (30) | 4.78× lower at baseline in the lines without PRICKLE2 | 0.020 | ⚠ within organs, on part of the lines; also absent: SNAI2, STK32A, LINC00973; co-absent with the target |
| [[SNAI2]] | C | PRICKLE2 activity raises SNAI2's level | lines that do not express PRICKLE2 (20) vs lines expressing it (30) | 4.25× lower at baseline in the lines without PRICKLE2 | 0.044 | ⚠ within organs, on part of the lines; also absent: SNAI2, STK32A, LINC00973; co-absent with the target |
| [[TENM4]] | C | PRICKLE2 activity raises TENM4's level | lines that do not express PRICKLE2 (20) vs lines expressing it (30) | 3.60× lower at baseline in the lines without PRICKLE2 | 0.052 | ⚠ within organs, on part of the lines; also absent: SNAI2, STK32A, LINC00973; co-absent with the target |
| [[IGFBP5]] | C | PRICKLE2 activity raises IGFBP5's level | lines that do not express PRICKLE2 (20) vs lines expressing it (30) | 4.39× lower at baseline in the lines without PRICKLE2 | 0.094 | ⚠ within organs, on part of the lines; also absent: SNAI2, STK32A, LINC00973; co-absent with the target |
| [[COL4A1]] | C | PRICKLE2 activity raises COL4A1's level | lines that do not express PRICKLE2 (20) vs lines expressing it (30) | 5.15× lower at baseline in the lines without PRICKLE2 | 0.098 | ⚠ within organs, on part of the lines; also absent: SNAI2, STK32A, LINC00973; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.0, 18.5); signed map (26.1, 47.1). **Vector** length 86.1, 24.2% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.4 | +2.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -7.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -6.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | prickle planar cell polarity protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:64,092,236-64,445,476 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686D143 |
| Gene groups (HGNC) | Prickle planar cell polarity proteins; LIM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3G6](https://www.uniprot.org/uniprotkb/Q7Z3G6) (Prickle-like protein 2):

> Is involved in the organization and maintenance of axon initial segment (AIS) architecture, likely cooperating with IGSF9B to regulate ANK3/ANKG localization to AIS (By similarity). By binding to and regulating ANK3/ANKG, it modulates its ability to bundle microtubules, a crucial mechanism for establishing neuronal polarity and AIS formation (By similarity). During early embryonic development, has a role in blastocyst formation, likely controlling the redistribution of the microtubule network …

**Summary**, from NCBI Gene [166336](https://www.ncbi.nlm.nih.gov/gene/166336):

> This gene encodes a homolog of Drosophila prickle. The exact function of this gene is not known, however, studies in mice suggest that it may be involved in seizure prevention. Mutations in this gene are associated with progressive myoclonic epilepsy type 5. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:20340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20340) · Entrez [166336](https://www.ncbi.nlm.nih.gov/gene/166336) · UniProt [Q7Z3G6](https://www.uniprot.org/uniprotkb/Q7Z3G6) · Ensembl [ENSG00000163637](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163637)

## Data

Gene col 8742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8742); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8742]; `tensor/DDL_lfc|DDL_z.npy` [8742]; `embed/gene_vectors.npy` [8742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8742 or target_col == 8742). Every well: [[PRICKLE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRICKLE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
