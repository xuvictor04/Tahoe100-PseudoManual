---
symbol: "NT5M"
type: "gene"
col: 12966
ensembl_id: "ENSG00000205309"
name: "5',3'-nucleotidase, mitochondrial"
location: "17p11.2"
module: 18
arm: "+"
pooled_cpm: 6.31
n_lines_expressing: 43
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 8
direction_downstream: 54
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# NT5M

*5',3'-nucleotidase, mitochondrial* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.41× (z +4.5, q 0.002, up in 4 of 22 measured lines) ⚠ toxic; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.37× (z +4.2, q 0.004, up in 8 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.346× (z -20.2, q 0e+00, down in 27 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY3]] (+0.64, fdr 7e-06), [[FAM86DP]] (+0.64, fdr 7e-06), [[MCOLN2]] (+0.62, fdr 1e-05); moves opposite to [[FMO4]] (-0.55, fdr 3e-05), [[LYRM2]] (-0.54, fdr 3e-05), [[STX4]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); 54 go from it, the strongest it → [[PRELID3A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.41×** | +4.5 | 0.002 | 4/22 (SW480, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.39×** | +4.5 | 0.002 | 5/40 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +4.2 | 0.004 | 8/36 (LOX-IMVI, HS-578T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.011 | 9/37 (HEC-1-A, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.080 | 8/36 (HS-578T, A-172, …) | all doses, flat |  |
| [[Everolimus (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.080 | 4/39 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.17 | 3/39 (MIA PaCa-2, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12966.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.346×** | -20.2 | 0e+00 | 27/32 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.219×** | -19.7 | 0e+00 | 32/38 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.337×** | -14.6 | 0e+00 | 27/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.374×** | -13.2 | 1e-37 | 19/30 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.298×** | -8.5 | 2e-15 | 20/36 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.540×** | -8.3 | 1e-14 | 19/37 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.555×** | -7.9 | 2e-13 | 17/39 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.597×** | -6.9 | 3e-10 | 21/40 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.619×** | -6.4 | 7e-09 | 15/39 (PANC-1, A-172, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.627×** | -6.3 | 2e-08 | 18/38 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.642×** | -5.9 | 2e-07 | 15/38 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.445×** | -5.7 | 6e-07 | 18/30 (C-33 A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.644×** | -5.6 | 1e-06 | 15/35 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -5.3 | 5e-06 | 13/24 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.692×** | -4.9 | 3e-05 | 16/31 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -4.8 | 7e-05 | 16/40 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.773×** | -3.4 | 0.020 | 7/39 (HOP62, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -16.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.144× (z -14.7) |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -19.4) |
| [[NCI-H460 (line)]] | wt | 9.38 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.1) |
| [[A-172 (line)]] | wt | 8.87 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0584× (z -20.5) |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 3 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0822× (z -11.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.9) |
| [[J82 (line)]] | alt | 8.43 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -12.5) |
| [[SW48 (line)]] | wt | 10.6 | 0 | 3 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.0380× (z -11.7) |
| [[A498 (line)]] | wt | 11.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0590× (z -27.6) |
| [[A549 (line)]] | wt | 10.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -14.8) |
| [[C32 (line)]] | wt | 7.83 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 5.23 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0721× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0917× (z -19.6) |
| [[A-427 (line)]] | wt | 14.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0719× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 6.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -15.5) |
| [[HOP62 (line)]] | alt | 5.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -9.0) |
| [[LoVo (line)]] | wt | 4.52 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.145× (z -8.5) |
| [[LS 180 (line)]] | wt | 2.31 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0479× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.8) |
| [[SW480 (line)]] | alt | 5.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.1) |
| [[AN3 CA (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY3]] | +0.64 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[FAM86DP]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MCOLN2]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SLC25A15]] | +0.62 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[ANKS6]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PUS7]] | +0.61 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[GLMN]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PXYLP1]] | +0.58 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[UCK2]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 | pathway: Metabolism of nucleotides |
| [[PMS1]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CAMKK2]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PEMT]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FMO4]] | -0.55 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[LYRM2]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[STX4]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[BROX]] | -0.52 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[SMARCA1]] | -0.51 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | -0.51 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[AFF4]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ATP6V1G1]] | -0.50 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[MVP-DT]] | -0.50 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[ARHGAP42]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[GDAP1]] | -0.50 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[LRGUK]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises NT5M's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.48× lower at baseline in the lines without GNAZ | 0.002 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[RNF220]] | B | RNF220 activity raises NT5M's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 2.56× lower at baseline in the lines without RNF220 | 0.005 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[TERT]] | B | TERT activity raises NT5M's level | lines that do not express TERT (13) vs lines expressing it (37) | 2.05× lower at baseline in the lines without TERT | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[ANKRD20A1]] | B | ANKRD20A1 activity raises NT5M's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without ANKRD20A1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A |
| [[MCOLN2]] | B | MCOLN2 activity raises NT5M's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.08× lower at baseline in the lines without MCOLN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[LDLRAD3]] | B | LDLRAD3 activity raises NT5M's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 2.62× lower at baseline in the lines without LDLRAD3 | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANKRD20A4P]] | B | ANKRD20A4P activity raises NT5M's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.53× lower at baseline in the lines without ANKRD20A4P | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5 |
| [[ADCY3]] | B | ADCY3 activity raises NT5M's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 2.06× lower at baseline in the lines without ADCY3 | 0.099 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |

### Downstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 54, C 0. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRELID3A]] | B | NT5M activity raises PRELID3A's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.70× lower at baseline in the lines without NT5M | 0.003 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[PRMT7]] | B | NT5M activity raises PRMT7's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without NT5M | 0.003 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[PUS7]] | B | NT5M activity raises PUS7's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.31× lower at baseline in the lines without NT5M | 0.006 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[PEMT]] | B | NT5M activity raises PEMT's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.03× lower at baseline in the lines without NT5M | 0.007 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[ANKRD13B]] | B | NT5M activity raises ANKRD13B's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without NT5M | 0.011 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[XYLB]] | B | NT5M activity raises XYLB's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.22× lower at baseline in the lines without NT5M | 0.011 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[NTAQ1]] | B | NT5M activity weakens NTAQ1's drug response | lines that do not express NT5M (7) vs lines expressing it (41) | the lines without NT5M respond 1.22× as strongly (z diff -0.65); strongest at Belinostat 5 µM: 2.71x vs 1.84x (z diff -2.8) | 0.013 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG; target measured in part of the lines; artifact flags |
| [[FANCC]] | B | NT5M activity raises FANCC's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without NT5M | 0.013 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[TRAP1]] | B | NT5M activity raises TRAP1's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without NT5M | 0.013 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[TMEM231]] | B | NT5M activity raises TMEM231's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.44× lower at baseline in the lines without NT5M | 0.014 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[TRIM65]] | B | NT5M activity raises TRIM65's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.70× lower at baseline in the lines without NT5M | 0.015 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[RILPL1]] | B | NT5M activity raises RILPL1's level | lines that do not express NT5M (7) vs lines expressing it (43) | 3.24× lower at baseline in the lines without NT5M | 0.016 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.2, -18.1); signed map (-40.7, -20.9). **Vector** length 72.8, 13.8% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.4 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +1.9 | +4.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.1 | +1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.0 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -19.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -20.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | 5',3'-nucleotidase, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,303,335-17,347,663 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dNT-2, dNT2, mdN |
| Gene groups (HGNC) | 5'-nucleotidases |
| Reactome | 3 pathways, smallest: Pyrimidine catabolism; Nucleotide catabolism; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPB1](https://www.uniprot.org/uniprotkb/Q9NPB1) (5'(3')-deoxyribonucleotidase, mitochondrial):

> Dephosphorylates preferentially the 5'- and 2'(3')-phosphates of uracil and thymine (deoxy)ribonucleotide monophosphates. Shows low activity toward dGMP and marginal activity toward dIMP.

**Summary**, from NCBI Gene [56953](https://www.ncbi.nlm.nih.gov/gene/56953):

> This gene encodes a 5' nucleotidase that localizes to the mitochondrial matrix. This enzyme dephosphorylates the 5'- and 2'(3')-phosphates of uracil and thymine deoxyribonucleotides. The gene is located within the Smith-Magenis syndrome region on chromosome 17. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15769) · Entrez [56953](https://www.ncbi.nlm.nih.gov/gene/56953) · UniProt [Q9NPB1](https://www.uniprot.org/uniprotkb/Q9NPB1) · Ensembl [ENSG00000205309](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205309)

## Data

Gene col 12966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12966); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12966]; `tensor/DDL_lfc|DDL_z.npy` [12966]; `embed/gene_vectors.npy` [12966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12966 or target_col == 12966). Every well: [[NT5M — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NT5M.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
