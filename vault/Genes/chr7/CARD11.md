---
symbol: "CARD11"
type: "gene"
col: 12566
ensembl_id: "ENSG00000198286"
name: "caspase recruitment domain family member 11"
location: "7p22.2"
module: 34
arm: "+"
pooled_cpm: 37.93
n_lines_expressing: 17
n_dd_up: 22
n_dd_down: 26
n_dd_up_clean: 16
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 24
direction_downstream: 39
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CARD11

*caspase recruitment domain family member 11* — 7p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.26× (z +14.2, q 3e-43, up in 4 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.77× (z +7.1, q 1e-10, up in 9 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.635× (z -8.1, q 5e-13, down in 15 of 15 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WNT7A]] (+0.59, fdr 1e-05), [[SCN5A]] (+0.55, fdr 1e-05), [[TTC9]] (+0.55, fdr 1e-05); moves opposite to [[CNTNAP1]] (-0.44, fdr 1e-04), [[TLL1]] (-0.42, fdr 2e-04), [[HOXC6]] (-0.42, fdr 0.002, ⚠ not reproduced), [[PHF21A]] (-0.41, fdr 2e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[PTPRE]] → it (grade B ⚠); 39 go from it, the strongest it → [[MANCR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +14.2 | 3e-43 | 4/14 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.02×** | +13.9 | 3e-41 | 6/16 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +9.2 | 1e-17 | 5/14 (HS-578T, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +7.1 | 1e-10 | 9/15 (HOP62, HS-578T, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +6.3 | 3e-08 | 9/15 (SW1417, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 8e-04 | 5/15 (HOP62, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.1 | 0.003 | 1/15 (HS-578T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.004 | 1/16 (SW1417) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.004 | 2/15 (SW480, J82) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.004 | 0/16 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.006 | 4/15 (SNU-423, HS-578T, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.8 | 0.008 | 2/15 (SW1417, J82) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.7 | 0.008 | 3/15 (SW1417, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.020 | 2/15 (NCI-H1792, A498) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.020 | 0/16 | top dose only |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.032 | 2/15 (NCI-H1792, Panc 03.27) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.036 | 0/15 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.036 | 6/15 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.047 | 6/15 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.064 | 10/15 (NCI-H1792, COLO 205, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.068 | 0/15 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 1 with an alert ⚠; shown: the 15 strongest. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12566.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.635×** | -8.1 | 5e-13 | 15/15 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.531×** | -7.9 | 6e-13 | 14/15 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.572×** | -7.0 | 3e-10 | 14/15 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.572×** | -7.0 | 3e-10 | 14/15 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.602×** | -6.1 | 1e-07 | 14/15 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.421×** | -5.7 | 1e-06 | 14/16 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.613×** | -5.7 | 1e-06 | 9/15 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.656×** | -5.3 | 9e-06 | 13/15 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.718×** | -4.2 | 0.002 | 9/16 (CFPAC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.533×** | -4.1 | 0.002 | 10/15 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.727×** | -4.0 | 0.003 | 10/16 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.720×** | -3.8 | 0.007 | 0/15 | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.788×** | -3.6 | 0.015 | 8/15 (CFPAC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -3.5 | 0.017 | 14/15 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.748×** | -3.5 | 0.017 | 11/15 (SW480, J82, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 159 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -24.2) |
| [[COLO 205 (line)]] | alt | 61.9 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0389× (z -26.3) |
| [[A-172 (line)]] | wt | 177 | 0 | 11 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -21.0) |
| [[CFPAC-1 (line)]] | alt | 141 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -26.5) |
| [[J82 (line)]] | alt | 72.8 | 0 | 11 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -22.8) |
| [[Panc 03.27 (line)]] | alt | 185 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -26.7) |
| [[A498 (line)]] | wt | 163 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -21.9) |
| [[NCI-H1792 (line)]] | alt | 107 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -14.5) |
| [[SW480 (line)]] | alt | 23.8 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -16.3) |
| [[NCI-H2347 (line)]] | alt | 62.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -20.3) |
| [[SW1417 (line)]] | alt | 51.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -17.1) |
| [[SW 900 (line)]] | alt | 71.2 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -15.3) |
| [[HS-578T (line)]] | alt | 11.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.47× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.41 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.02 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.55 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT7A]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[SCN5A]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TTC9]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TMEM171]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[PPARD]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PADI1]] | +0.53 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ATG9B]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[BLACAT1]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[LASTR]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[MYH16]] | +0.51 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[MANCR]] | +0.51 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[DYNC1I1]] | +0.50 | +0.47 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP1]] | -0.44 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[TLL1]] | -0.42 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[HOXC6]] | -0.42 | -0.47 / -0.12 | ⚠ not reproduced | 0.002 |  |
| [[PHF21A]] | -0.41 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[UBR5]] | -0.41 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[REV3L]] | -0.39 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[SLC35A5]] | -0.39 | -0.32 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 9, C 15. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRE]] | B | PTPRE activity raises CARD11's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 3.71× lower at baseline in the lines without PTPRE | 0.017 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[LEMD1]] | B | LEMD1 activity raises CARD11's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.37× lower at baseline in the lines without LEMD1 | 0.056 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[PROSER2]] | B | PROSER2 activity raises CARD11's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.93× lower at baseline in the lines without PROSER2 | 0.058 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[ZNF185]] | B | ZNF185 activity raises CARD11's level | lines that do not express ZNF185 (15) vs lines expressing it (35) | 2.35× lower at baseline in the lines without ZNF185 | 0.062 | ⚠ within organs, on part of the lines; also absent: HTR1D, KLF5, IL18 |
| [[SORCS2]] | B | SORCS2 activity lowers CARD11's level | lines that do not express SORCS2 (22) vs lines expressing it (28) | 1.71× higher at baseline in the lines without SORCS2 | 0.068 | ⚠ within organs, on part of the lines; also absent: ELFN1, CECR2, NTRK3; maybe low, not absent |
| [[MANCR]] | B | MANCR activity raises CARD11's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.16× lower at baseline in the lines without MANCR | 0.078 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises CARD11's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.57× lower at baseline in the lines without EVA1A-AS | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[ADAM19]] | B | ADAM19 activity raises CARD11's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without ADAM19 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[MAP2K1]] | B | MAP2K1 activity raises CARD11's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[TINAGL1]] | C | TINAGL1 activity raises CARD11's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 4.29× lower at baseline in the lines without TINAGL1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; co-absent with the target |
| [[ST6GALNAC5]] | C | ST6GALNAC5 activity raises CARD11's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 2.66× lower at baseline in the lines without ST6GALNAC5 | 0.005 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8; co-absent with the target |
| [[MIR4280HG]] | C | MIR4280HG activity raises CARD11's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 2.86× lower at baseline in the lines without MIR4280HG | 0.012 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 25, C 14. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MANCR]] | B | CARD11 activity raises MANCR's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 3.44× lower at baseline in the lines without CARD11 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[PTPRE]] | B | CARD11 activity raises PTPRE's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.48× lower at baseline in the lines without CARD11 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[EVA1A-AS]] | B | CARD11 activity raises EVA1A-AS's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.23× lower at baseline in the lines without CARD11 | 0.006 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[ADAM19]] | B | CARD11 activity raises ADAM19's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.56× lower at baseline in the lines without CARD11 | 0.009 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[TMEM171]] | B | CARD11 activity raises TMEM171's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.93× lower at baseline in the lines without CARD11 | 0.010 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[ATG9B]] | B | CARD11 activity raises ATG9B's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.04× lower at baseline in the lines without CARD11 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[CCNJL]] | B | CARD11 activity strengthens CCNJL's drug response | lines that do not express CARD11 (27) vs lines expressing it (12) | the lines without CARD11 respond 0.47× as strongly (z diff +2.90); strongest at Idarubicin (hydrochloride) 5 µM: 0.66x vs 0.27x (z diff +5.7) | 0.012 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; target measured in part of the lines; artifact flags |
| [[BLACAT1]] | B | CARD11 activity raises BLACAT1's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.72× lower at baseline in the lines without CARD11 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[PPARD]] | B | CARD11 activity raises PPARD's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.94× lower at baseline in the lines without CARD11 | 0.015 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[LEMD1]] | B | CARD11 activity raises LEMD1's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.05× lower at baseline in the lines without CARD11 | 0.016 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[KIF21B]] | B | CARD11 activity raises KIF21B's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.81× lower at baseline in the lines without CARD11 | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[MAP3K9-DT]] | B | CARD11 activity raises MAP3K9-DT's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.06× lower at baseline in the lines without CARD11 | 0.026 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, 59.3); signed map (3.7, 56.8). **Vector** length 77.8, 28.1% of its response variance represented; |z| ≥ 3 in 598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +13.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +7.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -6.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -5.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | caspase recruitment domain family member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.2 — chr7:2,906,142-3,044,228 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CARMA1, BIMP3 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; Caspase recruitment domain containing; PDZ domain containing; CBM complex |
| Reactome | 11 pathways, smallest: Activation of NF-kappaB in B cells; FCERI mediated NF-kB activation; Downstream signaling events of B Cell Receptor (BCR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXL7](https://www.uniprot.org/uniprotkb/Q9BXL7) (Caspase recruitment domain-containing protein 11):

> Adapter protein that plays a key role in adaptive immune response by transducing the activation of NF-kappa-B downstream of T-cell receptor (TCR) and B-cell receptor (BCR) engagement. Transduces signals downstream TCR or BCR activation via the formation of a multiprotein complex together with BCL10 and MALT1 that induces NF-kappa-B and MAP kinase p38 (MAPK11, MAPK12, MAPK13 and/or MAPK14) pathways. Upon activation in response to TCR or BCR triggering, CARD11 homooligomerizes to form a …

**Summary**, from NCBI Gene [84433](https://www.ncbi.nlm.nih.gov/gene/84433):

> The protein encoded by this gene belongs to the membrane-associated guanylate kinase (MAGUK) family, a class of proteins that functions as molecular scaffolds for the assembly of multiprotein complexes at specialized regions of the plasma membrane. This protein is also a member of the CARD protein family, which is defined by carrying a characteristic caspase-associated recruitment domain (CARD). This protein has a domain structure similar to that of CARD14 protein. The CARD domains of both …

**Accessions** — [HGNC:16393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16393) · Entrez [84433](https://www.ncbi.nlm.nih.gov/gene/84433) · UniProt [Q9BXL7](https://www.uniprot.org/uniprotkb/Q9BXL7) · Ensembl [ENSG00000198286](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198286)

## Data

Gene col 12566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12566); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12566]; `tensor/DDL_lfc|DDL_z.npy` [12566]; `embed/gene_vectors.npy` [12566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12566 or target_col == 12566). Every well: [[CARD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
