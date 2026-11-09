---
symbol: "IL31RA"
type: "gene"
col: 8957
ensembl_id: "ENSG00000164509"
name: "interleukin 31 receptor A"
location: "5q11.2"
module: 116
arm: "+"
pooled_cpm: 7.5
n_lines_expressing: 22
n_dd_up: 39
n_dd_down: 14
n_dd_up_clean: 22
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 8
direction_downstream: 14
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# IL31RA

*interleukin 31 receptor A* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (17 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.73× (z +16.0, q 0e+00, up in 17 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.876× (z -5.5, q 3e-05, down in 6 of 20 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.602× (z -5.3, q 3e-05, down in 8 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRMD6]] (+0.70, fdr 7e-06), [[NAV3]] (+0.69, fdr 7e-06), [[B4GALT6]] (+0.67, fdr 7e-06).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 14 go from it, the strongest it → [[ACTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.73×** | +16.0 | 0e+00 | 17/20 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.18×** | +12.5 | 2e-33 | 5/10 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +12.4 | 4e-33 | 12/20 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +11.4 | 5e-28 | 5/15 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.94×** | +11.2 | 3e-27 | 3/11 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +9.7 | 3e-20 | 15/20 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.17×** | +8.7 | 3e-16 | 14/19 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +8.6 | 5e-16 | 1/20 (SNU-423) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.3 | 2e-11 | 10/19 (NCI-H23, HS-578T, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.80×** | +6.6 | 2e-09 | 16/19 (NCI-H2030, SW 900, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +6.2 | 2e-08 | 10/18 (H4, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.70×** | +5.9 | 1e-07 | 5/20 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.40×** | +5.1 | 1e-05 | 1/10 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +5.1 | 2e-05 | 9/20 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.52×** | +4.7 | 1e-04 | 10/19 (NCI-H2030, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +4.3 | 6e-04 | 8/20 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.003 | 10/19 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +3.8 | 0.004 | 3/19 (LOX-IMVI, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.009 | 10/19 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.81×** | +3.5 | 0.011 | 2/17 (CFPAC-1, HS-578T) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.011 | 3/19 (NCI-H1792, A498, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +3.5 | 0.011 | 9/20 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.013 | 13/19 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.021 | 0/19 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8957.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.876× | -5.5 | 3e-05 | 6/20 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.602×** | -5.3 | 3e-05 | 8/19 (NCI-H2030, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.629×** | -5.2 | 3e-05 | 9/19 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.645×** | -4.8 | 3e-04 | 11/19 (A549, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.727×** | -4.3 | 0.002 | 12/20 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.785×** | -3.8 | 0.014 | 6/20 (SW480, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.790×** | -3.7 | 0.020 | 8/20 (CFPAC-1, PANC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.719×** | -3.5 | 0.031 | 7/20 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.815×** | -3.3 | 0.067 | 7/20 (A498, SW 1088, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.752×** | -3.2 | 0.068 | 4/19 (LOX-IMVI, A498, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.753×** | -3.2 | 0.068 | 4/19 (H4, A549, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.738×** | -3.2 | 0.070 | 8/19 (A549, SW 1271, …) | inconsistent across doses |  |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | **0.756×** | -3.2 | 0.070 | 1/20 (HS-578T) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.761×** | -3.1 | 0.084 | 5/19 (LOX-IMVI, NCI-H1792, …) | two highest doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.601×** | -3.0 | 0.100 | 2/20 (Panc 03.27, NCI-H1792) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 67.4 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +18.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 19.7 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +15.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 0.5 µM 0.196× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 51.6 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.606× (z -12.4) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -11.8) |
| [[H4 (line)]] | wt | 30.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -9.2) |
| [[HOP62 (line)]] | alt | 5.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 5.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 26.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -11.5) |
| [[SW 1271 (line)]] | alt | 86.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -10.4) |
| [[A-172 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.759 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRMD6]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[NAV3]] | +0.69 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[B4GALT6]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MARCHF4]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ADTRP]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LINC02930]] | +0.65 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[LTBP2]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[LINC00973]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[LCP1]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PHLDA1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SLC35F3]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CYB5R2]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers IL31RA's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[LINC02454]] | B | LINC02454 activity raises IL31RA's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 3.00× lower at baseline in the lines without LINC02454 | 0.059 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[GPR39]] | B | GPR39 activity raises IL31RA's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.55× lower at baseline in the lines without GPR39 | 0.087 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[TMEM156]] | C | TMEM156 activity raises IL31RA's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 3.87× lower at baseline in the lines without TMEM156 | 0.006 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises IL31RA's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.95× lower at baseline in the lines without FRMD4A | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[BCL2A1]] | C | BCL2A1 activity raises IL31RA's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 3.35× lower at baseline in the lines without BCL2A1 | 0.044 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1; co-absent with the target |
| [[HTR7]] | C | HTR7 activity raises IL31RA's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 3.01× lower at baseline in the lines without HTR7 | 0.056 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2; co-absent with the target |
| [[LINC02742]] | C | LINC02742 activity raises IL31RA's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 3.10× lower at baseline in the lines without LINC02742 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTN1]] | B | IL31RA activity raises ACTN1's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.56× lower at baseline in the lines without IL31RA | 0.004 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[GPR39]] | B | IL31RA activity raises GPR39's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without IL31RA | 0.010 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[SYNJ2]] | B | IL31RA activity raises SYNJ2's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without IL31RA | 0.019 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[EPHB2]] | B | IL31RA activity raises EPHB2's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.54× lower at baseline in the lines without IL31RA | 0.046 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[RUNX1]] | B | IL31RA activity raises RUNX1's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.71× lower at baseline in the lines without IL31RA | 0.049 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[MAST4]] | B | IL31RA activity raises MAST4's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without IL31RA | 0.058 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[FOSL1]] | B | IL31RA activity raises FOSL1's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.49× lower at baseline in the lines without IL31RA | 0.064 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[LRRC8C]] | B | IL31RA activity raises LRRC8C's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.89× lower at baseline in the lines without IL31RA | 0.097 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[HTR7]] | C | IL31RA activity raises HTR7's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 3.05× lower at baseline in the lines without IL31RA | 0.008 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1; co-absent with the target |
| [[TMEM156]] | C | IL31RA activity raises TMEM156's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 4.73× lower at baseline in the lines without IL31RA | 0.017 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1; co-absent with the target |
| [[PLAU]] | C | IL31RA activity raises PLAU's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 2.90× lower at baseline in the lines without IL31RA | 0.055 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1; co-absent with the target |
| [[LINC00707]] | C | IL31RA activity raises LINC00707's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 3.34× lower at baseline in the lines without IL31RA | 0.075 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1; co-absent with the target |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.8, 11.7); signed map (14.5, 44.0). **Vector** length 58.7, 15.5% of its response variance represented; |z| ≥ 3 in 557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +16.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.8 | +2.3 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 31 receptor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:55,851,357-55,922,854 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRL3, GLM-R, CRL, Glmr, IL-31RA |
| Gene groups (HGNC) | Fibronectin type III domain containing; Interleukin receptors |
| Reactome | 4 pathways, smallest: IL-6-type cytokine receptor ligand interactions; Interleukin-6 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI17](https://www.uniprot.org/uniprotkb/Q8NI17) (Interleukin-31 receptor subunit alpha):

> Functions as a membrane-bound signal-transducing subunit of the IL31 receptor complex (heterodimer composed of OSMR and IL31RA) which binds IL31. Functionally, IL31 signaling via OSMR/IL31RA is particularly important in skin immunity. Mechanistically, ligand binding induces heterodimerization with OSMR, activating JAK1 and JAK2 (and to a lesser extent TYK2) associated with the intracellular domains of IL31RA and OSMR. These kinases phosphorylate tyrosine residues on IL31RA and OSMR, creating …

**Summary**, from NCBI Gene [133396](https://www.ncbi.nlm.nih.gov/gene/133396):

> The protein encoded by this gene belongs to the type I cytokine receptor family. This receptor, with homology to gp130, is expressed on monocytes, and is involved in IL-31 signaling via activation of STAT-3 and STAT-5. It functions either as a monomer, or as part of a receptor complex with oncostatin M receptor (OSMR). Several alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:18969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18969) · Entrez [133396](https://www.ncbi.nlm.nih.gov/gene/133396) · UniProt [Q8NI17](https://www.uniprot.org/uniprotkb/Q8NI17) · Ensembl [ENSG00000164509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164509)

## Data

Gene col 8957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8957); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8957]; `tensor/DDL_lfc|DDL_z.npy` [8957]; `embed/gene_vectors.npy` [8957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8957 or target_col == 8957). Every well: [[IL31RA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL31RA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
