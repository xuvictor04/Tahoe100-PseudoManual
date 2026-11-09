---
symbol: "NBEAP1"
type: "gene"
col: 15117
ensembl_id: "ENSG00000258590"
name: "neurobeachin pseudogene 1"
location: "15q11.2"
module: 62
arm: "+"
pooled_cpm: 4.89
n_lines_expressing: 23
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# NBEAP1

*neurobeachin pseudogene 1* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.64× (z +27.8, q 0e+00, up in 16 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.186×, RPMI-7951 0.168×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LOX-IMVI 0.0849×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.245×; ⚠ toxic; transcription drop); [[Acetohexamide (drug)]] 0.5 µM in 1 line (SHP-77 0.0918×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAI3]] (+0.62, fdr 1e-05), [[PINCR]] (+0.59, fdr 4e-05), [[CDKN1A]] (+0.59, fdr 3e-05); moves opposite to [[PPIP5K2]] (-0.47, fdr 5e-05), [[LIN52]] (-0.46, fdr 1e-04), [[PASK]] (-0.45, fdr 5e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CCDC144NL-1]] → it (grade B ⚠); 6 go from it, the strongest it → [[GPM6A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.64×** | +27.8 | 0e+00 | 16/17 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.64×** | +16.1 | 0e+00 | 14/17 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.67×** | +14.9 | 0e+00 | 8/17 (RPMI-7951, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **4.35×** | +14.2 | 1e-43 | 17/18 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.17×** | +13.8 | 3e-41 | 11/17 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.66×** | +13.4 | 7e-39 | 15/18 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.73×** | +12.7 | 3e-35 | 17/18 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.20×** | +10.4 | 2e-23 | 1/8 (A498) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +10.2 | 1e-22 | 1/7 (NCI-H460) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.72×** | +9.7 | 2e-20 | 11/18 (RPMI-7951, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.37×** | +8.3 | 4e-15 | 11/18 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.39×** | +8.1 | 2e-14 | 4/11 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.07×** | +7.1 | 7e-11 | 11/17 (RPMI-7951, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +6.8 | 5e-10 | 2/10 (NCI-H460, HOP62) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.78×** | +5.6 | 8e-07 | 3/17 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +5.4 | 2e-06 | 5/18 (LOX-IMVI, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +5.2 | 7e-06 | 7/18 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.0 | 2e-05 | 4/16 (A498, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.13×** | +3.8 | 0.003 | 6/17 (A498, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15117.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.186×, RPMI-7951 0.168×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LOX-IMVI 0.0849×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.245×; ⚠ toxic; transcription drop); [[Acetohexamide (drug)]] 0.5 µM in 1 line (SHP-77 0.0918×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -3.2 | 0.37 | 5/19 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.722× | -3.1 | 0.37 | 3/18 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.729× | -3.0 | 0.37 | 5/18 (NCI-H460, A549, …) | inconsistent across doses | position effect removed |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.718× | -3.0 | 0.37 | 9/17 (RPMI-7951, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.43 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 11.7× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 54.5 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.0849× (z -16.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 25.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.8× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -9.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 71.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.14× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 13.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +15.6) | — |
| [[A549 (line)]] | wt | 4.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +8.8) | — |
| [[KATO III (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 8.67 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0918× (z -8.8) |
| [[A-172 (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.929 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.906 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAI3]] | +0.62 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[PINCR]] | +0.59 | +0.43 / +0.68 | both halves | 4e-05 |  |
| [[CDKN1A]] | +0.59 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[PURPL]] | +0.58 | +0.38 / +0.71 | both halves | 6e-05 |  |
| [[ZNF423]] | +0.58 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[GAS6-AS1]] | +0.57 | +0.25 / +0.75 | both halves | 4e-04 |  |
| [[BTG2]] | +0.56 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[CDIP1]] | +0.55 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[PDE4C]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[PHLDA3]] | +0.54 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[ACHE]] | +0.54 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[CYFIP2]] | +0.54 | +0.29 / +0.66 | both halves | 2e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIP5K2]] | -0.47 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[LIN52]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[PASK]] | -0.45 | -0.23 / -0.43 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144NL-1]] | B | CCDC144NL-1 activity raises NBEAP1's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 2.23× lower at baseline in the lines without CCDC144NL-1 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |
| [[SNTG2]] | C | SNTG2 activity raises NBEAP1's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without SNTG2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent; co-absent with the target |
| [[OR4F15]] | C | OR4F15 activity raises NBEAP1's level | lines that do not express OR4F15 (32) vs lines expressing it (18) | 2.56× lower at baseline in the lines without OR4F15 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, PHACTR1, ITGA4; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPM6A]] | B | NBEAP1 activity lowers GPM6A's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 1.16× higher at baseline in the lines without NBEAP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B |
| [[KCNN3]] | B | NBEAP1 activity raises KCNN3's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without NBEAP1 | 0.041 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B |
| [[CDIP1]] | B | NBEAP1 activity lowers CDIP1's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 1.04× higher at baseline in the lines without NBEAP1 | 0.046 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B |
| [[HHAT]] | B | NBEAP1 activity lowers HHAT's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 1.10× higher at baseline in the lines without NBEAP1 | 0.096 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B |
| [[ARC]] | C | NBEAP1 activity raises ARC's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without NBEAP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B; co-absent with the target |
| [[CD163L1]] | C | NBEAP1 activity raises CD163L1's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 3.53× lower at baseline in the lines without NBEAP1 | 0.057 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.3, 37.9); signed map (44.0, -22.6). **Vector** length 38.7, 7.30% of its response variance represented; |z| ≥ 3 in 514 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +27.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +5.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | +1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.7 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.6 | -0.2 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -0.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | neurobeachin pseudogene 1 |
| Locus type | pseudogene |
| Location | 15q11.2 — chr15:20,657,638-20,688,408 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | BCL8A; previously BCL8 |
| Matched by | ensembl_id |

UniProt [P0C6P0](https://www.uniprot.org/uniprotkb/P0C6P0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:1007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1007) · Entrez [606](https://www.ncbi.nlm.nih.gov/gene/606) · UniProt [P0C6P0](https://www.uniprot.org/uniprotkb/P0C6P0) · Ensembl [ENSG00000258590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258590)

## Data

Gene col 15117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15117); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15117]; `tensor/DDL_lfc|DDL_z.npy` [15117]; `embed/gene_vectors.npy` [15117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15117 or target_col == 15117). Every well: [[NBEAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBEAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
