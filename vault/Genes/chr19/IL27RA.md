---
symbol: "IL27RA"
type: "gene"
col: 2539
ensembl_id: "ENSG00000104998"
name: "interleukin 27 receptor subunit alpha"
location: "19p13.12"
module: 111
arm: "+"
pooled_cpm: 10.49
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# IL27RA

*interleukin 27 receptor subunit alpha* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +8.6, q 3e-15, up in 24 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 4.11×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.452× (z -7.1, q 8e-10, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INSYN2A]] (+0.52, fdr 1e-04), [[TMEM35B]] (+0.49, fdr 6e-05), [[ERVK3-1]] (+0.49, fdr 9e-05); moves opposite to [[RHOA]] (-0.54, fdr 8e-05), [[EIF3L]] (-0.51, fdr 3e-05), [[ACP1]] (-0.46, fdr 2e-04).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARHGAP31]] → it (grade B ⚠); 4 go from it, the strongest it → [[PHLDA2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2539.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 4.11×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.63×** | +8.6 | 3e-15 | 24/27 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.38×** | +7.5 | 2e-11 | 14/14 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.19×** | +7.0 | 4e-10 | 29/40 (HOP62, NCI-H460, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +5.6 | 4e-06 | 21/37 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.85×** | +5.1 | 4e-05 | 12/19 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.66×** | +4.5 | 6e-04 | 19/44 (SW480, HOP62, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.59×** | +4.1 | 0.003 | 16/44 (BT-474, SW480, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.1 | 0.003 | 16/37 (A498, RKO, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.30×** | +3.4 | 0.045 | 16/45 (NCI-H2347, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **1.45×** | +3.4 | 0.045 | 14/34 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2539.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.452×** | -7.1 | 8e-10 | 26/44 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.492×** | -6.3 | 7e-08 | 29/40 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.498×** | -6.2 | 9e-08 | 29/44 (RKO, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.522×** | -5.8 | 9e-07 | 23/44 (RKO, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.352×** | -4.9 | 1e-04 | 23/43 (RKO, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.592×** | -4.2 | 0.002 | 19/44 (RKO, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.651×** | -3.8 | 0.011 | 24/44 (MIA PaCa-2, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.466×** | -3.6 | 0.025 | 17/43 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.652×** | -3.5 | 0.025 | 15/44 (SK-MEL-2, RKO, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.471×** | -3.5 | 0.025 | 13/44 (HOP62, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.678×** | -3.5 | 0.028 | 15/44 (H4, NCI-H2030, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.677×** | -3.3 | 0.039 | 15/42 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.499×** | -3.2 | 0.052 | 13/43 (RKO, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.704×** | -3.1 | 0.073 | 14/44 (A-172, LS 180, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 34.0 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0879× (z -13.3) |
| [[KATO III (line)]] | alt | 4.51 | 0 | 3 | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0597× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -12.2) |
| [[A498 (line)]] | wt | 17.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.86 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.138× (z -9.1) |
| [[A-427 (line)]] | wt | 17.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -10.5) |
| [[LoVo (line)]] | wt | 4.77 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0900× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 41.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 4.87 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 3.68 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0518× (z -9.3) |
| [[SW48 (line)]] | wt | 23.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.147× (z -8.9) |
| [[SW480 (line)]] | alt | 13.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -8.5) |
| [[A549 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INSYN2A]] | +0.52 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[TMEM35B]] | +0.49 | +0.38 / +0.44 | both halves | 6e-05 |  |
| [[ERVK3-1]] | +0.49 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[ABRACL]] | +0.48 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[KDSR]] | +0.48 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[FAM169A]] | +0.47 | +0.44 / +0.28 | both halves | 3e-04 |  |
| [[LRCH3]] | +0.47 | +0.39 / +0.32 | both halves | 2e-04 |  |
| [[S100A13]] | +0.46 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[SYT12]] | +0.46 | +0.47 / +0.38 | both halves | 7e-05 |  |
| [[CACHD1]] | +0.46 | +0.30 / +0.32 | both halves | 2e-04 |  |
| [[PHLDA2]] | +0.46 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[MCOLN3]] | +0.46 | +0.40 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOA]] | -0.54 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[EIF3L]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ACP1]] | -0.46 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[INTS11]] | -0.45 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[VDAC2]] | -0.45 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[BAP1]] | -0.44 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[SH3YL1]] | -0.44 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[HNRNPA1]] | -0.44 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[SUDS3]] | -0.44 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[ZC3H10]] | -0.43 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[VTI1B]] | -0.43 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[TBCB]] | -0.43 | -0.38 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[PDHA1]] | -0.42 | -0.22 / -0.38 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP31]] | B | ARHGAP31 activity raises IL27RA's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 2.02× lower at baseline in the lines without ARHGAP31 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[MCOLN3]] | B | MCOLN3 activity raises IL27RA's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without MCOLN3 | 0.043 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHLDA2]] | C | IL27RA activity lowers PHLDA2's level | lines that do not express IL27RA (3) vs lines expressing it (47) | 2.85× higher at baseline in the lines without IL27RA | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ITGA2B, TMEM132A, CLEC2D; maybe low, not absent; its own permutation p |
| [[DCTN1]] | C | IL27RA activity raises DCTN1's level | lines that do not express IL27RA (3) vs lines expressing it (47) | 1.46× lower at baseline in the lines without IL27RA | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ITGA2B, TMEM132A, CLEC2D; maybe low, not absent; its own permutation p |
| [[NDUFA13]] | C | IL27RA activity raises NDUFA13's level | lines that do not express IL27RA (3) vs lines expressing it (47) | 1.34× lower at baseline in the lines without IL27RA | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ITGA2B, TMEM132A, CLEC2D; maybe low, not absent |
| [[CACHD1]] | C | IL27RA activity raises CACHD1's level | lines that do not express IL27RA (3) vs lines expressing it (47) | 3.40× lower at baseline in the lines without IL27RA | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ITGA2B, TMEM132A, CLEC2D; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction -0.301). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.7, 37.0); signed map (39.7, -18.2). **Vector** length 69.7, 13.8% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +4.5 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +3.7 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +1.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.9 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 27 receptor subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,031,762-14,053,218 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WSX-1, TCCR, CRL1, WSX1, zcytor1, IL-27R |
| Gene groups (HGNC) | Fibronectin type III domain containing; Interleukin receptors |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 5 pathways, smallest: Interleukin-27 signaling; Interleukin-35 Signalling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWB1](https://www.uniprot.org/uniprotkb/Q6UWB1) (Interleukin-27 receptor subunit alpha):

> Signal-transducing subunit for an heterodimeric cytokine composed of IL27/p28 and a soluble receptor EBI3. Heterodimerizes with IL6ST/GP130 to mediate signal transduction in response to the heterodimeric cytokine IL27/p28-EBI3. This signaling system acts through STAT3 and STAT1. Also acts as a signaling receptor as part of the humanin receptor complex; binding of MT-RNR2/humanin (HN) activates the intracellular JAK-STAT3 signaling pathway leading to neuroprotection. Involved in the regulation …

**Summary**, from NCBI Gene [9466](https://www.ncbi.nlm.nih.gov/gene/9466):

> In mice, CD4+ helper T-cells differentiate into type 1 (Th1) cells, which are critical for cell-mediated immunity, predominantly under the influence of IL12. Also, IL4 influences their differentiation into type 2 (Th2) cells, which are critical for most antibody responses. Mice deficient in these cytokines, their receptors, or associated transcription factors have impaired, but are not absent of, Th1 or Th2 immune responses. This gene encodes a protein which is similar to the mouse T-cell …

**Accessions** — [HGNC:17290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17290) · Entrez [9466](https://www.ncbi.nlm.nih.gov/gene/9466) · UniProt [Q6UWB1](https://www.uniprot.org/uniprotkb/Q6UWB1) · Ensembl [ENSG00000104998](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104998)

## Data

Gene col 2539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2539); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2539]; `tensor/DDL_lfc|DDL_z.npy` [2539]; `embed/gene_vectors.npy` [2539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2539 or target_col == 2539). Every well: [[IL27RA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL27RA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
