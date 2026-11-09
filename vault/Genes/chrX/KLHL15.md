---
symbol: "KLHL15"
type: "gene"
col: 10453
ensembl_id: "ENSG00000174010"
name: "kelch like family member 15"
location: "Xp22.11"
module: 93
arm: "+"
pooled_cpm: 46.97
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# KLHL15

*kelch like family member 15* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.20× (z +12.2, q 1e-31, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.645× (z -4.6, q 0.002, down in 32 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SK-MEL-2 0.104×, SNU-423 0.197×, A-172 0.218×, SW1417 0.308×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 0.243×, SW48 0.194×, A-427 0.353×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.327×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2A]] (+0.71, fdr 7e-06), [[LGMN]] (+0.66, fdr 7e-06), [[FOSB]] (+0.66, fdr 7e-06); moves opposite to [[AP3S2]] (-0.54, fdr 3e-05), [[LYPLAL1]] (-0.54, fdr 2e-05), [[RBM45]] (-0.54, fdr 5e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TLE4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +12.2 | 1e-31 | 39/47 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +11.7 | 6e-29 | 43/47 (Panc 03.27, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.35×** | +9.4 | 1e-18 | 44/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.12×** | +8.3 | 2e-14 | 43/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.21×** | +6.7 | 2e-09 | 41/48 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.81×** | +6.5 | 6e-09 | 38/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.64×** | +5.4 | 5e-06 | 34/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.66×** | +5.3 | 7e-06 | 32/46 (A-172, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.63×** | +5.2 | 2e-05 | 30/47 (NCI-H460, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 2e-04 | 28/47 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.50×** | +4.3 | 9e-04 | 29/45 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.002 | 27/47 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.45×** | +4.1 | 0.002 | 27/46 (NCI-H460, SW480, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +3.5 | 0.018 | 26/47 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +3.4 | 0.030 | 21/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.064 | 22/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.086 | 20/47 (J82, SNU-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10453.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SK-MEL-2 0.104×, SNU-423 0.197×, A-172 0.218×, SW1417 0.308×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 0.243×, SW48 0.194×, A-427 0.353×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.327×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.645×** | -4.6 | 0.002 | 32/47 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -4.5 | 0.002 | 21/38 (SNU-423, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.5 | 10 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.18× (z +16.9) | — |
| [[SW480 (line)]] | alt | 67.4 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 88.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -8.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 21.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 126 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -13.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 44.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -10.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 40.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +13.4) | — |
| [[C32 (line)]] | wt | 34.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 54.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 21.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 30.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 47.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +12.0) | — |
| [[J82 (line)]] | alt | 50.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 86.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 57.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 78.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 65.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -8.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +15.2) | — |
| [[A549 (line)]] | wt | 54.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 33.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +10.9) | — |
| [[LoVo (line)]] | wt | 37.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 46.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +8.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2347 (line)]] | alt | 59.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.8) | — |
| [[RKO (line)]] | wt | 35.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.3) | — |
| [[SW48 (line)]] | wt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -9.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2A]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[LGMN]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[FOSB]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[FAM222A]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[GTF2B]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[INTS6L]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[OAT]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[HEXIM1]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[VAMP1]] | +0.61 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[LINC00910]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[IVNS1ABP]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 | same gene group |
| [[TEX14]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3S2]] | -0.54 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[LYPLAL1]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[RBM45]] | -0.54 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[RRP36]] | -0.53 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TTC4]] | -0.52 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[RABEP1]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[NDUFAF5]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[UBE2K]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[METTL5]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[GLRX3]] | -0.50 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[TATDN1]] | -0.50 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[UBA3]] | -0.50 | -0.59 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLE4]] | B | TLE4 activity lowers KLHL15's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 1.50× higher at baseline in the lines without TLE4 | 0.073 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[CEMIP2]] | C | CEMIP2 activity lowers KLHL15's level | lines that do not express CEMIP2 (4) vs lines expressing it (46) | 2.17× higher at baseline in the lines without CEMIP2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIFC3, SMARCA2, PLSCR2; maybe low, not absent; its own permutation p |
| [[TRIM72]] | C | TRIM72 activity lowers KLHL15's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.75× higher at baseline in the lines without TRIM72 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.2, -27.5); signed map (2.4, 16.2). **Vector** length 98.0, 28.2% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +11.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.7 | -0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | +2.1 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.9 | +2.1 |
|  | [[Artemether (drug)]] 0.05 µM |  | +1.8 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.7 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.4 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:23,983,716-24,027,186 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1677 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M94](https://www.uniprot.org/uniprotkb/Q96M94) (Kelch-like protein 15):

> Substrate-specific adapter for CUL3 E3 ubiquitin-protein ligase complex. Acts as an adapter for CUL3 to target the serine/threonine-protein phosphatase 2A (PP2A) subunit PPP2R5B for ubiquitination and subsequent proteasomal degradation, thus promoting exchange with other regulatory subunits. Acts as an adapter for CUL3 to target the DNA-end resection factor RBBP8/CtIP for ubiquitination and subsequent proteasomal degradation. Through the regulation of RBBP8/CtIP protein turnover, plays a key …

**Summary**, from NCBI Gene [80311](https://www.ncbi.nlm.nih.gov/gene/80311):

> This gene encodes a member of the kelch-like family of proteins that share a common domain structure consisting of an N-terminal broad-complex, tramtrack, bric-a-brac/poxvirus and zinc finger domain and C-terminal kelch repeat motifs. The encoded protein may be involved in protein ubiquitination and cytoskeletal organization. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:29347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29347) · Entrez [80311](https://www.ncbi.nlm.nih.gov/gene/80311) · UniProt [Q96M94](https://www.uniprot.org/uniprotkb/Q96M94) · Ensembl [ENSG00000174010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174010)

## Data

Gene col 10453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10453); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10453]; `tensor/DDL_lfc|DDL_z.npy` [10453]; `embed/gene_vectors.npy` [10453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10453 or target_col == 10453). Every well: [[KLHL15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
