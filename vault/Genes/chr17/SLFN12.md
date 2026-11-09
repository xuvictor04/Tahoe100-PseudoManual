---
symbol: "SLFN12"
type: "gene"
col: 10213
ensembl_id: "ENSG00000172123"
name: "schlafen family member 12"
location: "17q12"
module: 70
arm: "+"
pooled_cpm: 4.85
n_lines_expressing: 28
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# SLFN12

*schlafen family member 12* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.75× (z +17.0, q 0e+00, up in 18 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.509× (z -7.7, q 6e-12, down in 14 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNIP3]] (+0.66, fdr 1e-05), [[CFH]] (+0.65, fdr 7e-06), [[IL7R]] (+0.65, fdr 1e-05); moves opposite to [[INPP5F]] (-0.57, fdr 1e-04), [[GET1]] (-0.55, fdr 3e-05), [[CAMSAP1]] (-0.54, fdr 6e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GPR176]] → it (grade C ⚠); 10 go from it, the strongest it → [[NEXN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.75×** | +17.0 | 0e+00 | 18/23 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.18×** | +13.7 | 3e-40 | 20/22 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.66×** | +11.2 | 1e-26 | 18/25 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.55×** | +11.1 | 2e-26 | 17/25 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +10.1 | 6e-22 | 16/24 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.26×** | +7.3 | 2e-11 | 15/25 (PANC-1, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +6.6 | 3e-09 | 9/25 (HOP62, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +6.5 | 8e-09 | 10/22 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.7 | 6e-07 | 11/25 (HOP62, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.4 | 3e-06 | 10/20 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 3e-05 | 13/25 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.50×** | +4.8 | 8e-05 | 9/25 (PANC-1, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +4.5 | 3e-04 | 5/25 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +4.4 | 4e-04 | 8/24 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +4.3 | 5e-04 | 10/23 (PANC-1, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.015 | 5/23 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.036 | 3/24 (AsPC-1, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10213.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.509×** | -7.7 | 6e-12 | 14/23 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -4.4 | 0.003 | 5/25 (A498, J82, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.784×** | -4.1 | 0.007 | 9/24 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **0.716×** | -3.8 | 0.018 | 4/24 (A498, HOP62, …) | top dose only |  |
| [[Malotilate (drug)]] 0.5 µM |  | **0.737×** | -3.7 | 0.029 | 4/24 (SNU-423, C32, …) | inconsistent across doses | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.740×** | -3.6 | 0.030 | 4/24 (LoVo, PANC-1, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.757×** | -3.3 | 0.069 | 6/25 (A-172, A498, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | 0.753× | -3.1 | 0.12 | 8/24 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 10.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +14.3) | — |
| [[A-172 (line)]] | wt | 17.5 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.06× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 10.6× (z +11.0) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0912× (z -11.2) |
| [[H4 (line)]] | wt | 10.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +9.2) | [[Furosemide (drug)]] 0.05 µM 0.0641× (z -9.9) |
| [[HOP62 (line)]] | alt | 9.20 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +15.4) | — |
| [[PANC-1 (line)]] | alt | 13.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 2.92 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.101× (z -8.8) ⚠ toxic; unreliable plate only |
| [[Hs 766T (line)]] | wt | 6.46 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0913× (z -8.7) |
| [[HS-578T (line)]] | alt | 8.16 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.72× (z +8.5) | — |
| [[J82 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.78× (z +11.8) | — |
| [[A-427 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.350 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNIP3]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[CFH]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[IL7R]] | +0.65 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[GBP1]] | +0.64 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[KCNT2]] | +0.62 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[ZNF462]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TRIM21]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[AMOTL2]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.60 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[ADAMTS3]] | +0.60 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[NEXN]] | +0.59 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[CASP8]] | +0.59 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5F]] | -0.57 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[GET1]] | -0.55 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[CAMSAP1]] | -0.54 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[CARD19]] | -0.54 | -0.56 / -0.37 | both halves | 7e-05 |  |
| [[SRD5A1]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[STXBP1]] | -0.53 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[PSMD9]] | -0.53 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[NPDC1]] | -0.53 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[CBFA2T2]] | -0.53 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[SNTA1]] | -0.53 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TMEM65]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[DIP2A]] | -0.52 | -0.56 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR176]] | C | GPR176 activity raises SLFN12's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 3.66× lower at baseline in the lines without GPR176 | 0.010 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1; co-absent with the target |
| [[IL7R]] | C | IL7R activity raises SLFN12's level | lines that do not express IL7R (30) vs lines expressing it (20) | 3.19× lower at baseline in the lines without IL7R | 0.063 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |
| [[CSF1]] | C | CSF1 activity raises SLFN12's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without CSF1 | 0.072 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1; co-absent with the target |
| [[CCBE1]] | C | CCBE1 activity raises SLFN12's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.73× lower at baseline in the lines without CCBE1 | 0.099 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEXN]] | B | SLFN12 activity raises NEXN's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 2.25× lower at baseline in the lines without SLFN12 | 0.005 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1 |
| [[IL7]] | B | SLFN12 activity raises IL7's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without SLFN12 | 0.007 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1 |
| [[MAML2]] | B | SLFN12 activity raises MAML2's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without SLFN12 | 0.024 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1 |
| [[LINC02605]] | B | SLFN12 activity raises LINC02605's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 2.28× lower at baseline in the lines without SLFN12 | 0.028 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1 |
| [[GBP1]] | B | SLFN12 activity raises GBP1's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 3.49× lower at baseline in the lines without SLFN12 | 0.048 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1 |
| [[GBP3]] | B | SLFN12 activity raises GBP3's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 2.26× lower at baseline in the lines without SLFN12 | 0.057 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1 |
| [[GPR176]] | C | SLFN12 activity raises GPR176's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 5.93× lower at baseline in the lines without SLFN12 | 0.007 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1; co-absent with the target |
| [[EPSTI1]] | C | SLFN12 activity raises EPSTI1's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 2.79× lower at baseline in the lines without SLFN12 | 0.036 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1; co-absent with the target |
| [[IL7R]] | C | SLFN12 activity raises IL7R's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 3.57× lower at baseline in the lines without SLFN12 | 0.084 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1; co-absent with the target |
| [[IFI16]] | C | SLFN12 activity raises IFI16's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 3.92× lower at baseline in the lines without SLFN12 | 0.096 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.2, 24.0); signed map (46.1, 24.6). **Vector** length 56.1, 12.2% of its response variance represented; |z| ≥ 3 in 591 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +17.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +4.4 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.3 | -7.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -1.9 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | schlafen family member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,409,465-35,433,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10260 |
| Gene groups (HGNC) | Schlafen family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYM2](https://www.uniprot.org/uniprotkb/Q8IYM2) (Ribonuclease SLFN12):

> Ribonuclease which is part of an E2/17beta-estradiol-induced pro-apoptotic signaling pathway. E2 stabilizes the PDE3A/SLFN12 complex in the cytosol, promoting the dephosphorylation of SLFN12 and activating its pro-apoptotic ribosomal RNA/rRNA ribonuclease activity. This apoptotic pathway might be relevant in tissues with high concentration of E2 and be for instance involved in placenta remodeling. May play a role in cell differentiation.

**Summary**, from NCBI Gene [55106](https://www.ncbi.nlm.nih.gov/gene/55106):

> Enables RNA nuclease activity and ribosome binding activity. Involved in apoptotic signaling pathway and rRNA catabolic process. Part of cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25500) · Entrez [55106](https://www.ncbi.nlm.nih.gov/gene/55106) · UniProt [Q8IYM2](https://www.uniprot.org/uniprotkb/Q8IYM2) · Ensembl [ENSG00000172123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172123)

## Data

Gene col 10213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10213); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10213]; `tensor/DDL_lfc|DDL_z.npy` [10213]; `embed/gene_vectors.npy` [10213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10213 or target_col == 10213). Every well: [[SLFN12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLFN12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
