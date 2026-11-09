---
symbol: "DNAI1"
type: "gene"
col: 4372
ensembl_id: "ENSG00000122735"
name: "dynein axonemal intermediate chain 1"
location: "9p13.3"
module: 100
arm: "+"
pooled_cpm: 4.22
n_lines_expressing: 45
n_dd_up: 32
n_dd_down: 9
n_dd_up_clean: 28
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# DNAI1

*dynein axonemal intermediate chain 1* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.43× (z +27.5, q 0e+00, up in 25 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.428× (z -8.2, q 9e-14, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTBN4]] (+0.61, fdr 2e-05), [[HESX1]] (+0.58, fdr 7e-06), [[MAST1]] (+0.56, fdr 7e-05); moves opposite to [[NR2C2AP]] (-0.45, fdr 1e-04), [[ATR]] (-0.44, fdr 1e-03, ⚠ not reproduced), [[WDR77]] (-0.44, fdr 8e-04, ⚠ not reproduced), [[PA2G4]] (-0.44, fdr 2e-04), [[SPECC1L]] (-0.43, fdr 3e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[SPTBN4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.43×** | +27.5 | 0e+00 | 25/30 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **11.1×** | +23.4 | 0e+00 | 38/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **10.0×** | +22.4 | 0e+00 | 40/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **8.07×** | +20.2 | 0e+00 | 38/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.27×** | +19.9 | 0e+00 | 27/31 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.39×** | +14.3 | 1e-44 | 33/41 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.37×** | +11.8 | 2e-30 | 27/42 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.84×** | +10.1 | 3e-22 | 19/33 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **6.14×** | +9.2 | 2e-18 | 25/35 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.39×** | +8.4 | 2e-15 | 18/36 (A-172, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.18×** | +7.5 | 3e-12 | 17/30 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +6.6 | 2e-09 | 14/27 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +6.1 | 6e-08 | 10/26 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.0 | 6e-08 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.7 | 5e-07 | 10/32 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.68×** | +4.8 | 5e-05 | 12/34 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.428×** | -8.2 | 9e-14 | 23/38 (BT-474, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.516×** | -6.4 | 3e-08 | 18/35 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.554×** | -5.7 | 2e-06 | 17/36 (BT-474, SW 900, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.557×** | -5.7 | 2e-06 | 15/42 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.605×** | -4.9 | 1e-04 | 19/42 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -4.4 | 0.001 | 12/27 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.648×** | -4.2 | 0.002 | 12/41 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.461×** | -3.9 | 0.006 | 7/25 (BT-474, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.676×** | -3.8 | 0.009 | 8/40 (COLO 205, RPMI-7951, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.720× | -3.1 | 0.12 | 7/36 (H4, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.8 | 3 | 9 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 5.16× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -14.8) |
| [[SW480 (line)]] | alt | 2.70 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +11.1) | — |
| [[A498 (line)]] | wt | 4.72 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 2.23 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 10.2 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 12.8× (z +9.1) | [[Digitoxin (drug)]] 0.5 µM 0.0358× (z -11.9) |
| [[A549 (line)]] | wt | 3.25 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 15.9× (z +8.8) | [[Digitoxin (drug)]] 0.5 µM 0.0400× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 2.22 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.0× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 1.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +10.3) | — |
| [[A-172 (line)]] | wt | 3.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.63× (z +10.6) | — |
| [[C32 (line)]] | wt | 2.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.2× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 1.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 3.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 3.64 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0666× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 4.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 2.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +9.1) | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTBN4]] | +0.61 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[HESX1]] | +0.58 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[MAST1]] | +0.56 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[CCDC144NL-1]] | +0.55 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CCDC88B]] | +0.55 | +0.34 / +0.66 | both halves | 1e-04 |  |
| [[LRRC36]] | +0.54 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[HOOK2]] | +0.54 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[CEACAM22P-1]] | +0.51 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[COL26A1]] | +0.51 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LHX4]] | +0.49 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[CELF5]] | +0.49 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SYNM-AS1]] | +0.49 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2C2AP]] | -0.45 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ATR]] | -0.44 | -0.18 / -0.37 | ⚠ not reproduced | 1e-03 |  |
| [[WDR77]] | -0.44 | -0.20 / -0.48 | ⚠ not reproduced | 8e-04 | same gene group |
| [[PA2G4]] | -0.44 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[TMEM250]] | -0.43 | -0.19 / -0.41 | ⚠ not reproduced | 8e-04 |  |
| [[SPECC1L]] | -0.43 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[SLC35B4]] | -0.42 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[METTL8]] | -0.41 | -0.12 / -0.37 | ⚠ not reproduced | 0.002 |  |
| [[UTP4]] | -0.41 | -0.29 / -0.39 | both halves | 2e-04 | same gene group |
| [[ALG8]] | -0.41 | -0.22 / -0.39 | both halves | 6e-04 |  |
| [[WDR27]] | -0.40 | -0.25 / -0.38 | both halves | 4e-04 | same gene group |
| [[ARMC6]] | -0.40 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[PCNA]] | -0.40 | -0.24 / -0.32 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DNAI1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CACNA1B]] | B | CACNA1B activity raises DNAI1's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.68× lower at baseline in the lines without CACNA1B | 0.050 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[NOVA2]] | B | NOVA2 activity raises DNAI1's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without NOVA2 | 0.055 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[KCNN3]] | B | KCNN3 activity raises DNAI1's level | lines that do not express KCNN3 (8) vs lines expressing it (42) | 2.22× lower at baseline in the lines without KCNN3 | 0.056 | ⚠ within organs, on part of the lines; also absent: VLDLR-AS1, ADGRG2, SLC17A7; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPTBN4]] | B | DNAI1 activity raises SPTBN4's level | lines that do not express DNAI1 (5) vs lines expressing it (45) | 2.27× lower at baseline in the lines without DNAI1 | 0.059 | ⚠ within organs, on part of the lines; also absent: FBXO15, KCNK15-AS1, CRB1; maybe low, not absent |
| [[DCDC1]] | B | DNAI1 activity raises DCDC1's level | lines that do not express DNAI1 (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without DNAI1 | 0.065 | ⚠ within organs, on part of the lines; also absent: FBXO15, KCNK15-AS1, CRB1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.456). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.1, 31.7); signed map (24.8, 16.2). **Vector** length 51.9, 7.24% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +19.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | +2.3 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.9 | -0.2 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal intermediate chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,457,414-34,520,988 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DIC1, PCD, CILD1, oda6 |
| Gene groups (HGNC) | WD repeat domain containing; Dyneins, axonemal outer arm complex subunits; Dynein intermediate chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI46](https://www.uniprot.org/uniprotkb/Q9UI46) (Dynein axonemal intermediate chain 1):

> Component of dynein, a family of motor proteins essential for movement along microtubules (By similarity). Required for structural and functional integrity of cilia (By similarity). Part of the dynein complex of respiratory cilia.

**Summary**, from NCBI Gene [27019](https://www.ncbi.nlm.nih.gov/gene/27019):

> This gene encodes a member of the dynein intermediate chain family. The encoded protein is part of the dynein complex in respiratory cilia. The inner- and outer-arm dyneins, which bridge between the doublet microtubules in axonemes, are the force-generating proteins responsible for the sliding movement in axonemes. The intermediate and light chains, thought to form the base of the dynein arm, help mediate attachment and may also participate in regulating dynein activity. Mutations in this gene …

**Accessions** — [HGNC:2954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2954) · Entrez [27019](https://www.ncbi.nlm.nih.gov/gene/27019) · UniProt [Q9UI46](https://www.uniprot.org/uniprotkb/Q9UI46) · Ensembl [ENSG00000122735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122735)

## Data

Gene col 4372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4372); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4372]; `tensor/DDL_lfc|DDL_z.npy` [4372]; `embed/gene_vectors.npy` [4372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4372 or target_col == 4372). Every well: [[DNAI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
