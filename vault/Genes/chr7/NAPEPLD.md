---
symbol: "NAPEPLD"
type: "gene"
col: 8414
ensembl_id: "ENSG00000161048"
name: "N-acyl phosphatidylethanolamine phospholipase D"
location: "7q22.1"
module: 136
arm: "+"
pooled_cpm: 13.82
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 24
n_dd_up_clean: 14
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# NAPEPLD

*N-acyl phosphatidylethanolamine phospholipase D* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.57× (z +6.3, q 2e-07, up in 24 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.51× (z +6.0, q 4e-07, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.446× (z -11.0, q 1e-25, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM26]] (+0.59, fdr 3e-05), [[PRPF4B]] (+0.58, fdr 1e-05), [[FIGN]] (+0.56, fdr 2e-05); moves opposite to [[FAM219A]] (-0.61, fdr 1e-05), [[MYO9B]] (-0.58, fdr 3e-05), [[TPD52L2]] (-0.58, fdr 1e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANKRD18A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.3 | 2e-07 | 24/41 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +6.0 | 4e-07 | 22/47 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +6.0 | 4e-07 | 24/48 (A498, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +4.5 | 7e-04 | 18/47 (HS-578T, J82, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.5 | 7e-04 | 11/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.4 | 9e-04 | 19/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.003 | 15/46 (C32, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +3.9 | 0.008 | 7/48 (A498, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.020 | 15/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.020 | 13/48 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.030 | 13/47 (C32, HEC-1-A, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.050 | 6/47 (PANC-1, SW1417, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.050 | 5/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.050 | 14/47 (LoVo, C32, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.050 | 9/48 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.087 | 10/45 (RKO, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8414.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.446×** | -11.0 | 1e-25 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.525×** | -9.4 | 2e-18 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.508×** | -9.3 | 4e-18 | 32/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.555×** | -8.6 | 1e-15 | 29/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.574×** | -7.6 | 4e-12 | 27/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.426×** | -6.5 | 7e-09 | 25/48 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.754×** | -5.8 | 5e-07 | 23/48 (LS 180, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.672×** | -5.8 | 5e-07 | 23/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.677×** | -5.7 | 7e-07 | 24/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.662×** | -5.7 | 7e-07 | 23/47 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -5.3 | 6e-06 | 21/47 (SK-MEL-2, AN3 CA, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.707×** | -5.1 | 2e-05 | 20/48 (NCI-H23, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.749×** | -4.2 | 0.001 | 17/45 (COLO 205, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.744×** | -4.0 | 0.003 | 12/29 (NCI-H2030, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.762×** | -4.0 | 0.003 | 14/47 (SNU-423, NCI-H2030, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.598×** | -3.9 | 0.003 | 14/44 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.774×** | -3.5 | 0.013 | 19/48 (COLO 205, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.785×** | -3.3 | 0.025 | 12/47 (SW480, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 30.3 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.330× (z -11.9) |
| [[PANC-1 (line)]] | alt | 20.5 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.245× (z -12.2) |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.280× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 7.56 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0730× (z -10.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.210× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -11.1) |
| [[H4 (line)]] | wt | 12.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0832× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -9.2) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -9.3) |
| [[A-172 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26]] | +0.59 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[PRPF4B]] | +0.58 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[FIGN]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[DIS3L]] | +0.55 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[RPRD2]] | +0.55 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[SLC25A12]] | +0.54 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[THUMPD2]] | +0.53 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[HMG20A]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[SCAF8]] | +0.53 | +0.34 / +0.35 | both halves | 1e-04 |  |
| [[ZNF608]] | +0.53 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[PUM2]] | +0.53 | +0.25 / +0.34 | both halves | 4e-04 |  |
| [[CACHD1]] | +0.52 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM219A]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.58 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[TPD52L2]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[IQGAP1]] | -0.57 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[LRRFIP1]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[MAP1LC3B]] | -0.53 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[DPP9]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[MXRA7]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MROH1]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ESYT1]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[FAM85B]] | -0.50 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[TESK1]] | -0.49 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD18A]] | B | ANKRD18A activity raises NAPEPLD's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.25× lower at baseline in the lines without ANKRD18A | 0.077 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction -0.518). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.5, 2.9); signed map (11.2, -37.1). **Vector** length 71.5, 12.6% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.8 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +6.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.5 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.0 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.8 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -8.6 |

## What is on record

|  |  |
|---|---|
| Name | N-acyl phosphatidylethanolamine phospholipase D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:103,099,776-103,149,560 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FMP30, C7orf18, NAPE-PLD |
| Gene groups (HGNC) | Metallo-beta-lactamase fold containing family |
| Reactome | 3 pathways, smallest: Diseases associated with visual transduction; Diseases of the neuronal system; Retinoid cycle disease events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IQ20](https://www.uniprot.org/uniprotkb/Q6IQ20) (N-acyl-phosphatidylethanolamine-hydrolyzing phospholipase D):

> D-type phospholipase that hydrolyzes N-acyl-phosphatidylethanolamines (NAPEs) to produce bioactive N-acylethanolamines/fatty acid ethanolamides (NAEs/FAEs) and phosphatidic acid. Cleaves the terminal phosphodiester bond of diacyl- and alkenylacyl-NAPEs, primarily playing a role in the generation of long-chain saturated and monounsaturated NAEs in the brain (By similarity). May control NAPE homeostasis in dopaminergic neuron membranes and regulate neuron survival, partly through RAC1 activation …

**Summary**, from NCBI Gene [222236](https://www.ncbi.nlm.nih.gov/gene/222236):

> NAPEPLD is a phospholipase D type enzyme that catalyzes the release of N-acylethanolamine (NAE) from N-acyl-phosphatidylethanolamine (NAPE) in the second step of the biosynthesis of N-acylethanolamine (Okamoto et al., 2004 [PubMed 14634025]).[supplied by OMIM, Oct 2008]

**Accessions** — [HGNC:21683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21683) · Entrez [222236](https://www.ncbi.nlm.nih.gov/gene/222236) · UniProt [Q6IQ20](https://www.uniprot.org/uniprotkb/Q6IQ20) · Ensembl [ENSG00000161048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161048)

## Data

Gene col 8414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8414); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8414]; `tensor/DDL_lfc|DDL_z.npy` [8414]; `embed/gene_vectors.npy` [8414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8414 or target_col == 8414). Every well: [[NAPEPLD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAPEPLD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
