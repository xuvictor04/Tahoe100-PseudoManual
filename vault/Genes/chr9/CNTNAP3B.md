---
symbol: "CNTNAP3B"
type: "gene"
col: 7813
ensembl_id: "ENSG00000154529"
name: "contactin associated protein family member 3B"
location: "9p11.2"
module: 196
arm: "+"
pooled_cpm: 11.09
n_lines_expressing: 28
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# CNTNAP3B

*contactin associated protein family member 3B* — 9p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +5.0, q 4e-04, up in 5 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.520× (z -9.9, q 1e-20, down in 20 of 23 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.491× (z -7.7, q 5e-12, down in 17 of 25 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP3P2]] (+0.86, fdr 7e-06), [[CNTNAP3]] (+0.81, fdr 7e-06), [[CNTNAP3C]] (+0.68, fdr 7e-06); moves opposite to [[CDKL5]] (-0.44, fdr 4e-05), [[ICAM5]] (-0.40, fdr 1e-04), [[SNX33]] (-0.38, fdr 2e-04).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FAM78B]] → it (grade B ⚠); 6 go from it, the strongest it → [[FAM78B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.0 | 4e-04 | 5/25 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.3 | 0.004 | 1/14 (NCI-H1792) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.004 | 5/24 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.004 | 8/25 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.8 | 0.017 | 2/18 (HS-578T, SW480) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.058 | 10/24 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.13 | 8/26 (CFPAC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7813.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.520×** | -9.9 | 1e-20 | 20/23 (A549, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.491×** | -7.7 | 5e-12 | 17/25 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.539×** | -6.6 | 6e-09 | 18/23 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.544×** | -6.6 | 8e-09 | 17/24 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.548×** | -6.2 | 5e-08 | 16/24 (PANC-1, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.569×** | -6.1 | 1e-07 | 16/25 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -5.2 | 1e-05 | 19/22 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -5.0 | 5e-05 | 13/25 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.434×** | -4.7 | 1e-04 | 14/23 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.646×** | -4.7 | 1e-04 | 15/24 (SNU-423, C-33 A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -4.5 | 3e-04 | 15/24 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.659×** | -4.5 | 3e-04 | 15/24 (SW480, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.688×** | -4.0 | 0.003 | 17/25 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.701×** | -3.8 | 0.006 | 14/25 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.702×** | -3.8 | 0.006 | 11/25 (A-172, NCI-H2030, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.788×** | -3.6 | 0.011 | 8/24 (CFPAC-1, C32, …) | top dose only |  |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | **0.747×** | -3.1 | 0.055 | 1/25 (SK-MEL-2) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.749×** | -2.9 | 0.098 | 14/24 (NCI-H2030, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -14.8) |
| [[PANC-1 (line)]] | alt | 15.4 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -15.6) |
| [[SNU-1 (line)]] | wt | 57.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.164× (z -9.8) |
| [[A549 (line)]] | wt | 59.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0848× (z -22.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 63.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -14.2) |
| [[Hs 766T (line)]] | wt | 39.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -12.4) |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -10.1) |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.118× (z -8.7) |
| [[C32 (line)]] | wt | 29.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -15.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 9.04 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -10.4) |
| [[SW480 (line)]] | alt | 7.85 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 6.62 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0575× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 4.26 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 8.39 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0572× (z -11.9) |
| [[SHP-77 (line)]] | alt | 9.90 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -8.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -9.5) |
| [[A-172 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.972 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.861 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.984 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP3P2]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[CNTNAP3]] | +0.81 | +0.77 / +0.78 | both halves | 7e-06 | same gene group; STRING 605 |
| [[CNTNAP3C]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | same gene group |
| [[FBXO17]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD20A4P]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ANKRD29]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[STAMBPL1]] | +0.50 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[PTPRZ1]] | +0.47 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[FBXO27]] | +0.45 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[SDHAP3]] | +0.44 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[ANKRD18CP]] | +0.44 | +0.43 / +0.40 | both halves | 4e-05 |  |
| [[KCNQ5]] | +0.43 | +0.41 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL5]] | -0.44 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ICAM5]] | -0.40 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[SNX33]] | -0.38 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[TOX4]] | -0.37 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[GCC1]] | -0.36 | -0.36 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[MTFR1L]] | -0.36 | -0.29 / -0.30 | both halves | 3e-04 |  |
| [[TSPAN31]] | -0.36 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[MTMR4]] | -0.35 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[VPS39]] | -0.35 | -0.35 / -0.24 | both halves | 5e-04 |  |
| [[MAGED2]] | -0.35 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[CREB3L1]] | -0.34 | -0.30 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM78B]] | B | FAM78B activity raises CNTNAP3B's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.55× lower at baseline in the lines without FAM78B | 0.019 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[AKR1E2]] | B | AKR1E2 activity raises CNTNAP3B's level | lines that do not express AKR1E2 (19) vs lines expressing it (31) | 1.94× lower at baseline in the lines without AKR1E2 | 0.053 | ⚠ within organs, on part of the lines; also absent: FLNC, AFAP1L1, CACNA2D1 |
| [[CNTNAP3P2]] | C | CNTNAP3P2 activity raises CNTNAP3B's level | lines that do not express CNTNAP3P2 (19) vs lines expressing it (31) | 4.93× lower at baseline in the lines without CNTNAP3P2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: CNTNAP3B, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[CNTNAP3]] | C | CNTNAP3 activity raises CNTNAP3B's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 4.51× lower at baseline in the lines without CNTNAP3 | 0.002 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[CNTNAP3C]] | C | CNTNAP3C activity raises CNTNAP3B's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 3.46× lower at baseline in the lines without CNTNAP3C | 0.014 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[ANKRD20A4P]] | C | ANKRD20A4P activity raises CNTNAP3B's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 2.93× lower at baseline in the lines without ANKRD20A4P | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM78B]] | B | CNTNAP3B activity raises FAM78B's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without CNTNAP3B | 0.018 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C |
| [[TGFBRAP1]] | B | CNTNAP3B activity raises TGFBRAP1's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 1.06× lower at baseline in the lines without CNTNAP3B | 0.097 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C |
| [[CNTNAP3P2]] | C | CNTNAP3B activity raises CNTNAP3P2's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 3.97× lower at baseline in the lines without CNTNAP3B | 4e-04 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[CNTNAP3]] | C | CNTNAP3B activity raises CNTNAP3's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 3.98× lower at baseline in the lines without CNTNAP3B | 0.004 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[CNTNAP3C]] | C | CNTNAP3B activity raises CNTNAP3C's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without CNTNAP3B | 0.017 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[ANKRD20A4P]] | C | CNTNAP3B activity raises ANKRD20A4P's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 2.27× lower at baseline in the lines without CNTNAP3B | 0.027 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.8, 28.7); signed map (19.8, 58.6). **Vector** length 65.8, 17.3% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.7 | +1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +0.5 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | contactin associated protein family member 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p11.2 — chr9:41,890,314-42,129,510 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Contactin associated protein family |
| Matched by | ensembl_id |

UniProt [Q96NU0](https://www.uniprot.org/uniprotkb/Q96NU0) carries no function annotation.

**Summary**, from NCBI Gene [728577](https://www.ncbi.nlm.nih.gov/gene/728577):

> Predicted to be involved in nervous system development and signal transduction. Predicted to be located in membrane. Predicted to be active in plasma membrane and synapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32035) · Entrez [728577](https://www.ncbi.nlm.nih.gov/gene/728577) · UniProt [Q96NU0](https://www.uniprot.org/uniprotkb/Q96NU0) · Ensembl [ENSG00000154529](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154529)

## Data

Gene col 7813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7813); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7813]; `tensor/DDL_lfc|DDL_z.npy` [7813]; `embed/gene_vectors.npy` [7813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7813 or target_col == 7813). Every well: [[CNTNAP3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTNAP3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
