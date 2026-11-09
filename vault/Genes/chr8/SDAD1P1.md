---
symbol: "SDAD1P1"
type: "gene"
col: 13646
ensembl_id: "ENSG00000228451"
name: "SDA1 domain containing 1 pseudogene 1"
location: "8p21.2"
module: 79
arm: "+"
pooled_cpm: 7.95
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# SDAD1P1

*SDA1 domain containing 1 pseudogene 1* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.13× (z +9.2, q 1e-17, up in 16 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.02× (z +8.7, q 6e-16, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.442× (z -7.1, q 6e-10, down in 36 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.557× (z -5.1, q 7e-05, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASL-DT]] (+0.59, fdr 1e-05), [[RYBP]] (+0.58, fdr 3e-05), [[BNIP3L]] (+0.56, fdr 5e-05, ⚠ same locus), [[CHMP1B]] (+0.53, fdr 2e-05); moves opposite to [[XPO4]] (-0.51, fdr 3e-05), [[MAPKAPK5]] (-0.51, fdr 5e-05), [[ATP6V0A2]] (-0.50, fdr 4e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FBXO32]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13646.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.13×** | +9.2 | 1e-17 | 16/18 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +8.7 | 6e-16 | 39/47 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.70×** | +8.7 | 6e-16 | 39/46 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +7.3 | 5e-11 | 24/29 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +6.8 | 1e-09 | 32/47 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +6.6 | 3e-09 | 31/46 (HS-578T, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +6.5 | 5e-09 | 32/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +6.1 | 1e-07 | 31/47 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +5.1 | 2e-05 | 25/46 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.5 | 3e-04 | 19/44 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.003 | 18/45 (KATO III, LoVo, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.005 | 17/47 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.008 | 15/47 (HT-29, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +3.6 | 0.016 | 13/45 (NCI-H460, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +3.4 | 0.028 | 6/14 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.057 | 21/45 (A-172, HOP62, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.94×** | +3.0 | 0.073 | 11/40 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.442×** | -7.1 | 6e-10 | 36/46 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.557×** | -5.1 | 7e-05 | 23/45 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.558×** | -5.1 | 7e-05 | 22/46 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -4.8 | 2e-04 | 22/41 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.681×** | -4.7 | 3e-04 | 22/42 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.599×** | -4.2 | 0.002 | 17/43 (SK-MEL-2, J82, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.873× | -4.0 | 0.005 | 15/48 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.629×** | -3.9 | 0.007 | 20/46 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.433×** | -3.8 | 0.008 | 17/36 (NCI-H460, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.649×** | -3.8 | 0.009 | 19/45 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.484×** | -3.7 | 0.012 | 10/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.660×** | -3.6 | 0.014 | 20/47 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.685×** | -3.3 | 0.041 | 16/45 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.487×** | -3.3 | 0.041 | 14/44 (A498, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.501×** | -3.2 | 0.061 | 14/41 (NCI-H1573, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 24.0 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0937× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 21.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0481× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0782× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 8.86 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -10.1) |
| [[SW480 (line)]] | alt | 5.84 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 9.43 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.101× (z -11.0) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 6.03 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 9.51× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 6.55 | 1 | 0 | [[Selinexor (drug)]] 5 µM 4.67× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 6.04 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -8.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 7.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -8.6) |
| [[A-172 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASL-DT]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[RYBP]] | +0.58 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[BNIP3L]] | +0.56 | +0.39 / +0.54 | both halves | 5e-05 | ⚠ same locus (1.5 kb: neighbours can correlate without regulation) |
| [[CHMP1B]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LINC02175]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SERINC1]] | +0.52 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[MYOM1]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[RORA]] | +0.51 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[PAIP2]] | +0.51 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[PPM1N]] | +0.51 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[BTG1]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[USP9X]] | +0.51 | +0.50 / +0.37 | both halves | 7e-05 |  |
| [[BNIP3]] | +0.51 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPO4]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | -0.51 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[ATP6V0A2]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PDSS1]] | -0.49 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[CAMKK2]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SELENOI]] | -0.48 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[SNAPC4]] | -0.48 | -0.21 / -0.51 | both halves | 6e-04 |  |
| [[NEURL4]] | -0.47 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[CTU2]] | -0.47 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[DHX35]] | -0.44 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[DCPS]] | -0.44 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[TREX2]] | -0.44 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO32]] | B | FBXO32 activity lowers SDAD1P1's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.40× higher at baseline in the lines without FBXO32 | 0.048 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, -12.9); signed map (-8.8, 16.2). **Vector** length 75.4, 14.7% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | SDA1 domain containing 1 pseudogene 1 |
| Locus type | pseudogene |
| Location | 8p21.2 — chr8:26,379,392-26,381,519 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31403) · Entrez [157489](https://www.ncbi.nlm.nih.gov/gene/157489) · Ensembl [ENSG00000228451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228451)

## Data

Gene col 13646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13646); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13646]; `tensor/DDL_lfc|DDL_z.npy` [13646]; `embed/gene_vectors.npy` [13646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13646 or target_col == 13646). Every well: [[SDAD1P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDAD1P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
