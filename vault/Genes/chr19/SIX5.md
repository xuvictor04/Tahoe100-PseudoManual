---
symbol: "SIX5"
type: "gene"
col: 10783
ensembl_id: "ENSG00000177045"
name: "SIX homeobox 5"
location: "19q13.32"
module: 80
arm: "+"
pooled_cpm: 6.91
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 10
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# SIX5

*SIX homeobox 5* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.58× (z +13.4, q 3e-38, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.400× (z -9.2, q 2e-17, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENO3]] (+0.76, fdr 7e-06), [[PIGV]] (+0.72, fdr 1e-05), [[MEPCE]] (+0.71, fdr 1e-05); moves opposite to [[OPA1]] (-0.65, fdr 7e-06), [[GTF2E2]] (-0.64, fdr 4e-05), [[WASF3]] (-0.62, fdr 3e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SOCS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.58×** | +13.4 | 3e-38 | 33/41 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +9.2 | 7e-18 | 31/40 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.20×** | +7.6 | 6e-12 | 28/44 (HOP62, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.7 | 3e-04 | 4/12 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.3 | 0.002 | 17/40 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +4.2 | 0.002 | 13/35 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.8 | 0.010 | 4/47 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.69×** | +3.8 | 0.012 | 9/42 (LS 180, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.080 | 7/42 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.096 | 7/37 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.1 | 0.097 | 7/28 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.097 | 4/42 (A498, RPMI-7951, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.097 | 6/40 (HS-578T, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.400×** | -9.2 | 2e-17 | 37/46 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.403×** | -9.1 | 2e-17 | 35/46 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.413×** | -8.9 | 2e-16 | 35/46 (HS-578T, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.478×** | -7.4 | 2e-11 | 31/46 (hTERT-HPNE, NCI-H23, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.510×** | -6.7 | 2e-09 | 27/46 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.535×** | -5.9 | 3e-07 | 24/42 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.557×** | -5.9 | 4e-07 | 24/45 (HT-29, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -5.7 | 7e-07 | 24/45 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.614×** | -4.9 | 6e-05 | 19/46 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.540×** | -4.4 | 6e-04 | 13/46 (Hs 766T, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.467×** | -3.9 | 0.006 | 12/45 (J82, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.685×** | -3.8 | 0.007 | 21/41 (NCI-H460, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.697×** | -3.6 | 0.013 | 16/45 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -3.2 | 0.060 | 16/46 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.732×** | -3.1 | 0.066 | 7/46 (AN3 CA, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -3.0 | 0.086 | 12/45 (HOP62, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.744×** | -3.0 | 0.097 | 13/42 (CFPAC-1, NCI-H460, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.557×** | -3.0 | 0.097 | 12/39 (MIA PaCa-2, BT-474, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 8.51 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 13.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +17.2) | — |
| [[HS-578T (line)]] | alt | 7.69 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.125× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 4.77 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0602× (z -8.8) |
| [[A498 (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -8.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 7.95 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 6.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 4.88 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0903× (z -8.6) |
| [[LS 180 (line)]] | wt | 3.20 | 0 | 1 | — | [[Lopinavir (drug)]] 0.05 µM 0.0497× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 7.84 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 4.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -10.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 4.02 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0623× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 5.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +9.8) | — |
| [[A-172 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENO3]] | +0.76 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[PIGV]] | +0.72 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[MEPCE]] | +0.71 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[RGL2]] | +0.70 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[NEK8]] | +0.70 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[CREB3L4]] | +0.69 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ZCCHC3]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ZBED5]] | +0.68 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ZNF689]] | +0.68 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[GPR137]] | +0.67 | +0.80 / +0.36 | both halves | 9e-05 |  |
| [[BOLA1]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.67 | +0.71 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPA1]] | -0.65 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[GTF2E2]] | -0.64 | -0.63 / -0.40 | both halves | 4e-05 |  |
| [[WASF3]] | -0.62 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[GARNL3]] | -0.62 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[NUTF2]] | -0.62 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[PLA2G12A]] | -0.62 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ST6GALNAC4]] | -0.61 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[ARPC1A]] | -0.60 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[NME2]] | -0.60 | -0.70 / -0.28 | both halves | 3e-04 |  |
| [[PACC1]] | -0.60 | -0.48 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOCS2]] | B | SOCS2 activity raises SIX5's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without SOCS2 | 0.050 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[CCDC102A]] | B | CCDC102A activity raises SIX5's level | lines that do not express CCDC102A (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without CCDC102A | 0.053 | ⚠ within organs, on part of the lines; also absent: CYP46A1, TMOD2, DPF1; maybe low, not absent |
| [[FZD7]] | C | FZD7 activity raises SIX5's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without FZD7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2; its own permutation p |
| [[ARHGEF17]] | C | ARHGEF17 activity raises SIX5's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 10.1); signed map (18.6, -11.8). **Vector** length 86.9, 17.9% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +13.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.1 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +4.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.6 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -9.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | SIX homeobox 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,764,785-45,769,252 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DMAHP |
| Gene groups (HGNC) | SINE class homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N196](https://www.uniprot.org/uniprotkb/Q8N196) (Homeobox protein SIX5):

> Transcription factor that is thought to be involved in regulation of organogenesis. May be involved in determination and maintenance of retina formation. Binds a 5'-GGTGTCAG-3' motif present in the ARE regulatory element of ATP1A1. Binds a 5'-TCA[AG][AG]TTNC-3' motif present in the MEF3 element in the myogenin promoter, and in the IGFBP5 promoter (By similarity). Thought to be regulated by association with Dach and Eya proteins, and seems to be coactivated by EYA1, EYA2 and EYA3 (By similarity).

**Summary**, from NCBI Gene [147912](https://www.ncbi.nlm.nih.gov/gene/147912):

> The protein encoded by this gene is a homeodomain-containing transcription factor that appears to function in the regulation of organogenesis. This gene is located downstream of the dystrophia myotonica-protein kinase gene. Mutations in this gene are a cause of branchiootorenal syndrome type 2. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:10891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10891) · Entrez [147912](https://www.ncbi.nlm.nih.gov/gene/147912) · UniProt [Q8N196](https://www.uniprot.org/uniprotkb/Q8N196) · Ensembl [ENSG00000177045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177045)

## Data

Gene col 10783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10783); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10783]; `tensor/DDL_lfc|DDL_z.npy` [10783]; `embed/gene_vectors.npy` [10783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10783 or target_col == 10783). Every well: [[SIX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
