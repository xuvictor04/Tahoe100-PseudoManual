---
symbol: "CCDC162P"
type: "gene"
col: 12790
ensembl_id: "ENSG00000203799"
name: "coiled-coil domain containing 162, pseudogene"
location: "6q21"
module: 39
arm: "+"
pooled_cpm: 12.77
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 24
n_dd_up_clean: 13
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# CCDC162P

*coiled-coil domain containing 162, pseudogene* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +12.0, q 3e-30, up in 31 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.405× (z -10.7, q 7e-24, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTBD16]] (+0.65, fdr 2e-05), [[CAPN3]] (+0.65, fdr 1e-05), [[BCAR3-AS1]] (+0.64, fdr 7e-06); moves opposite to [[SH3PXD2B]] (-0.59, fdr 1e-04), [[CAMKK1]] (-0.56, fdr 3e-04), [[PLA2G12A]] (-0.52, fdr 4e-04).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC01250]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +12.0 | 3e-30 | 31/41 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.80×** | +6.9 | 1e-09 | 29/46 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +5.7 | 2e-06 | 21/45 (BT-474, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +5.2 | 3e-05 | 14/40 (C-33 A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.9 | 1e-04 | 7/18 (HCT15, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.6 | 3e-04 | 15/46 (LS 180, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.6 | 3e-04 | 19/41 (SNU-423, RKO, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.6 | 3e-04 | 14/46 (BT-474, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.5 | 5e-04 | 13/40 (HT-29, H4, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.2 | 0.001 | 11/34 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.013 | 11/43 (SW480, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.35×** | +3.6 | 0.015 | 9/45 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.015 | 11/44 (SW480, A549, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.015 | 9/46 (COLO 205, BT-474, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.015 | 11/45 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.060 | 6/44 (A-172, J82, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.405×** | -10.7 | 7e-24 | 32/45 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.466×** | -9.0 | 5e-17 | 31/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.468×** | -9.0 | 5e-17 | 28/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -8.2 | 3e-14 | 29/42 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.612×** | -5.8 | 7e-07 | 21/45 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.708×** | -5.8 | 8e-07 | 21/46 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.592×** | -5.7 | 9e-07 | 23/43 (COLO 205, RKO, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.415×** | -5.4 | 4e-06 | 17/39 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.635×** | -5.4 | 5e-06 | 22/45 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.455×** | -4.9 | 7e-05 | 23/43 (NCI-H1573, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.668×** | -4.8 | 1e-04 | 20/45 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.696×** | -4.3 | 9e-04 | 17/40 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -4.0 | 0.002 | 17/44 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.704×** | -3.9 | 0.004 | 18/42 (NCI-H1573, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.695×** | -3.9 | 0.004 | 15/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.735×** | -3.6 | 0.010 | 16/41 (COLO 205, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.582×** | -3.3 | 0.027 | 7/42 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.680×** | -3.3 | 0.032 | 5/46 (LoVo, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 80.2 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.3) |
| [[LoVo (line)]] | wt | 27.1 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.169× (z -13.0) |
| [[SW480 (line)]] | alt | 21.5 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.153× (z -13.9) |
| [[A549 (line)]] | wt | 19.2 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.121× (z -10.3) |
| [[BT-474 (line)]] | alt | 18.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.06× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 18.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +9.1) | [[Belumosudil (drug)]] 5 µM 0.0638× (z -10.8) |
| [[HCT15 (line)]] | alt | 25.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.113× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 6.03 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.113× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.186× (z -9.9) |
| [[PANC-1 (line)]] | alt | 9.01 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.207× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.20 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0874× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 33.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.142× (z -10.2) |
| [[HOP62 (line)]] | alt | 4.87 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0772× (z -9.8) |
| [[HT-29 (line)]] | alt | 5.44 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0978× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 8.70 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0627× (z -8.9) |
| [[J82 (line)]] | alt | 6.20 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0997× (z -8.8) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 4.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 37.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.285× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0933× (z -10.1) |
| [[A-172 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD16]] | +0.65 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[CAPN3]] | +0.65 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[BCAR3-AS1]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[BTG3-AS1]] | +0.61 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[FAM151B]] | +0.61 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[HSD17B3]] | +0.61 | +0.65 / +0.38 | both halves | 7e-05 |  |
| [[ANKDD1B]] | +0.61 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[LINC01191]] | +0.60 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[CD226]] | +0.60 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CCT6B]] | +0.59 | +0.66 / +0.38 | both halves | 7e-05 |  |
| [[HCLS1]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[SLC6A13]] | +0.59 | +0.65 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.59 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[CAMKK1]] | -0.56 | -0.58 / -0.29 | both halves | 3e-04 |  |
| [[PLA2G12A]] | -0.52 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[RMND1]] | -0.52 | -0.37 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01250]] | B | LINC01250 activity raises CCDC162P's level | lines that do not express LINC01250 (10) vs lines expressing it (40) | 2.20× lower at baseline in the lines without LINC01250 | 0.009 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CCDC162P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CD226]] | B | CD226 activity raises CCDC162P's level | lines that do not express CD226 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without CD226 | 0.032 | ⚠ within organs, on part of the lines; also absent: FRZB, GALNT16, KLRG1; maybe low, not absent |
| [[DSCAML1]] | B | DSCAML1 activity raises CCDC162P's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.01× lower at baseline in the lines without DSCAML1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[NDUFA4L2]] | B | NDUFA4L2 activity raises CCDC162P's level | lines that do not express NDUFA4L2 (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without NDUFA4L2 | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ASB4]] | B | ASB4 activity raises CCDC162P's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without ASB4 | 0.098 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises CCDC162P's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.79× lower at baseline in the lines without ITPR2-AS1 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.9, -8.9); signed map (20.0, 5.6). **Vector** length 74.4, 13.8% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.2 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +6.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +0.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.0 | -4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | +0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 162, pseudogene |
| Locus type | pseudogene |
| Location | 6q21 — chr6:109,183,955-109,355,046 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | bA425D10.7, bA425D10.3, bA487F23.3; previously C6orf184, C6orf185, CCDC162, C6orf183 |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [221262](https://www.ncbi.nlm.nih.gov/gene/221262):

> This gene is the ortholog of the mouse coiled-coil domain containing 162 gene. This locus is transcribed, but is represented as a unitary pseudogene because there are multiple changes in the coding sequence, including multiple changes that result in premature stop codons, relative to the mouse coding sequence. Transcripts from this locus are expected to encode truncated proteins, and may be candidates for nonsense-mediated decay (NMD). [provided by RefSeq, Sep 2018]

**Accessions** — [HGNC:21565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21565) · Entrez [221262](https://www.ncbi.nlm.nih.gov/gene/221262) · Ensembl [ENSG00000203799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203799)

## Data

Gene col 12790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12790); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12790]; `tensor/DDL_lfc|DDL_z.npy` [12790]; `embed/gene_vectors.npy` [12790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12790 or target_col == 12790). Every well: [[CCDC162P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC162P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
