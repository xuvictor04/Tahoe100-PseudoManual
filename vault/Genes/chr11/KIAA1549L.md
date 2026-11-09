---
symbol: "KIAA1549L"
type: "gene"
col: 3137
ensembl_id: "ENSG00000110427"
name: "KIAA1549 like"
location: "11p13"
module: 110
arm: "+"
pooled_cpm: 68.48
n_lines_expressing: 30
n_dd_up: 0
n_dd_down: 66
n_dd_up_clean: 0
n_dd_down_clean: 54
in_vector_space: true
direction_upstream: 19
direction_downstream: 10
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# KIAA1549L

*KIAA1549 like* — 11p13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 66 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.212× (z -26.5, q 0e+00, down in 28 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC8C]] (+0.77, fdr 7e-06), [[NLRP3]] (+0.71, fdr 7e-06), [[ARHGAP22]] (+0.68, fdr 7e-06); moves opposite to [[ALDH3B1]] (-0.59, fdr 1e-05), [[MBNL2]] (-0.57, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[LINC01812]] → it (grade B ⚠); 10 go from it, the strongest it → [[EVC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | 1.36× | +3.7 | 0.10 | 13/28 (SK-MEL-2, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.21× | +3.4 | 0.15 | 8/28 (BT-474, A-427, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.74× | +3.4 | 0.15 | 12/27 (LS 180, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 5 µM |  | 1.68× | +3.1 | 0.24 | 11/28 (AsPC-1, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.25 | 9/28 (SK-MEL-2, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 68 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 66 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3137.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.212×** | -26.5 | 0e+00 | 28/28 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.262×** | -15.6 | 0e+00 | 28/28 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.358×** | -12.4 | 4e-33 | 26/28 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.360×** | -12.3 | 7e-33 | 24/28 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.366×** | -12.2 | 5e-32 | 25/28 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.397×** | -11.2 | 6e-27 | 26/28 (C-33 A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.443×** | -9.8 | 6e-21 | 20/28 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.463×** | -9.3 | 1e-18 | 21/28 (SK-MEL-2, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.509×** | -8.1 | 2e-14 | 20/28 (HOP62, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.593×** | -7.7 | 6e-13 | 22/28 (AsPC-1, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.528×** | -7.7 | 7e-13 | 18/27 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.516×** | -7.7 | 7e-13 | 24/27 (C-33 A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -7.6 | 1e-12 | 23/27 (C-33 A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.526×** | -7.5 | 4e-12 | 21/27 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.568×** | -7.2 | 2e-11 | 23/30 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.567×** | -6.6 | 2e-09 | 17/27 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.575×** | -6.2 | 2e-08 | 20/28 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 703 | 0 | 30 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0513× (z -36.6) |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 21 (4 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0725× (z -20.4) |
| [[HOP62 (line)]] | alt | 197 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0592× (z -28.0) |
| [[hTERT-HPNE (line)]] | wt | 320 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0477× (z -20.4) |
| [[PANC-1 (line)]] | alt | 149 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0694× (z -33.8) |
| [[J82 (line)]] | alt | 45.0 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -20.3) |
| [[A549 (line)]] | wt | 80.4 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0876× (z -27.8) |
| [[C-33 A (line)]] | alt | 71.9 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0190× (z -30.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -15.8) |
| [[C32 (line)]] | wt | 206 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -23.1) |
| [[RKO (line)]] | wt | 60.2 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -19.9) |
| [[SK-MEL-2 (line)]] | alt | 171 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -26.0) |
| [[A-172 (line)]] | wt | 157 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -25.2) |
| [[H4 (line)]] | wt | 98.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0498× (z -21.8) |
| [[LS 180 (line)]] | wt | 51.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.159× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 32.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -12.1) |
| [[Hs 766T (line)]] | wt | 115 | 0 | 5 (2 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0189× (z -12.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.185× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 29.3 | 0 | 5 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.479× (z -14.8) ⚠ position not correctable · without an alert: [[Harringtonine (drug)]] 5 µM 0.109× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 61.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -15.2) |
| [[HS-578T (line)]] | alt | 70.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -16.4) |
| [[SNU-423 (line)]] | alt | 63.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 38.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -17.8) |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.5) |
| [[SW 1271 (line)]] | alt | 84.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -11.3) |
| [[SW1417 (line)]] | alt | 22.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -9.9) |
| [[A-427 (line)]] | wt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.2) |
| [[A498 (line)]] | wt | 4.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.95 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.65 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8C]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[NLRP3]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP22]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[CD59]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 | STRING 668; ⚠ same locus (28.9 kb: neighbours can correlate without regulation) |
| [[RPSAP52]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[FLT1]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[NT5E]] | +0.66 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[MAP4K4]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[MIR100HG]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH3B1]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[MBNL2]] | -0.57 | -0.60 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 12, C 7. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01812]] | B | LINC01812 activity raises KIAA1549L's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 3.98× lower at baseline in the lines without LINC01812 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |
| [[FRMD4A]] | B | FRMD4A activity raises KIAA1549L's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.69× lower at baseline in the lines without FRMD4A | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[AP1G2]] | B | AP1G2 activity lowers KIAA1549L's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 3.40× higher at baseline in the lines without AP1G2 | 0.041 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[FRMD6]] | B | FRMD6 activity raises KIAA1549L's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 3.47× lower at baseline in the lines without FRMD6 | 0.043 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[CLMP]] | B | CLMP activity raises KIAA1549L's level | lines that do not express CLMP (25) vs lines expressing it (25) | 2.57× lower at baseline in the lines without CLMP | 0.058 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[HHIP]] | B | HHIP activity raises KIAA1549L's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.39× lower at baseline in the lines without HHIP | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[LINC01812]] | B | LINC01812 activity strengthens KIAA1549L's drug response | lines that do not express LINC01812 (17) vs lines expressing it (11) | the lines without LINC01812 respond 0.76× as strongly (z diff +2.18); strongest at Homoharringtonine 0.5 µM: 0.63x vs 0.14x (z diff +5.4) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; target measured in part of the lines; artifact flags |
| [[MIR100HG]] | B | MIR100HG activity raises KIAA1549L's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 3.18× lower at baseline in the lines without MIR100HG | 0.068 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises KIAA1549L's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 3.30× lower at baseline in the lines without HS3ST3A1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[COL13A1]] | B | COL13A1 activity raises KIAA1549L's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 3.16× lower at baseline in the lines without COL13A1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[HMGA2]] | B | HMGA2 activity raises KIAA1549L's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 2.69× lower at baseline in the lines without HMGA2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[MAP2K1]] | B | MAP2K1 activity raises KIAA1549L's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 12.3% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVC]] | B | KIAA1549L activity raises EVC's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 2.85× lower at baseline in the lines without KIAA1549L | 0.014 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[CD59]] | B | KIAA1549L activity raises CD59's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without KIAA1549L | 0.023 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[C11orf91]] | B | KIAA1549L activity raises C11orf91's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 2.25× lower at baseline in the lines without KIAA1549L | 0.054 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[GCNT2]] | B | KIAA1549L activity lowers GCNT2's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 1.38× higher at baseline in the lines without KIAA1549L | 0.056 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[ATP13A3]] | B | KIAA1549L activity raises ATP13A3's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without KIAA1549L | 0.070 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[FRMD6]] | B | KIAA1549L activity raises FRMD6's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without KIAA1549L | 0.078 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[EPB41]] | B | KIAA1549L activity lowers EPB41's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 1.70× higher at baseline in the lines without KIAA1549L | 0.085 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[FXYD5]] | B | KIAA1549L activity raises FXYD5's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 1.77× lower at baseline in the lines without KIAA1549L | 0.091 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[MICAL2]] | B | KIAA1549L activity raises MICAL2's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 2.07× lower at baseline in the lines without KIAA1549L | 0.093 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[NLRP3]] | C | KIAA1549L activity raises NLRP3's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 2.77× lower at baseline in the lines without KIAA1549L | 0.034 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1; co-absent with the target |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.7, 8.2); signed map (12.1, 47.8). **Vector** length 131, 43.7% of its response variance represented; |z| ≥ 3 in 1,281 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.7 | +0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.1 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.4 | -7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.3 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.2 | -7.5 |
|  | [[Binimetinib (drug)]] 0.5 µM | ⚠ position correction uncertain | -5.1 | -6.1 |
|  | [[Binimetinib (drug)]] 5 µM | ⚠ position correction uncertain | -5.0 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | KIAA1549 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:33,376,108-33,674,102 (+) |
| Ensembl biotype | protein_coding |
| Also known as | G2, MGC34830; previously C11orf69, C11orf41 |
| Matched by | ensembl_id |

UniProt [Q6ZVL6](https://www.uniprot.org/uniprotkb/Q6ZVL6) carries no function annotation.

**Summary**, from NCBI Gene [25758](https://www.ncbi.nlm.nih.gov/gene/25758):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24836) · Entrez [25758](https://www.ncbi.nlm.nih.gov/gene/25758) · UniProt [Q6ZVL6](https://www.uniprot.org/uniprotkb/Q6ZVL6) · Ensembl [ENSG00000110427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110427)

## Data

Gene col 3137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3137); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3137]; `tensor/DDL_lfc|DDL_z.npy` [3137]; `embed/gene_vectors.npy` [3137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3137 or target_col == 3137). Every well: [[KIAA1549L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIAA1549L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
