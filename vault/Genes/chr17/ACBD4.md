---
symbol: "ACBD4"
type: "gene"
col: 11193
ensembl_id: "ENSG00000181513"
name: "acyl-CoA binding domain containing 4"
location: "17q21.31"
module: 45
arm: "+"
pooled_cpm: 5.2
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 23
n_dd_up_clean: 18
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ACBD4

*acyl-CoA binding domain containing 4* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.57× (z +7.7, q 9e-12, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.308× (z -14.2, q 4e-43, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCRN2]] (+0.65, fdr 1e-05), [[CCDC88B]] (+0.64, fdr 1e-05), [[SLC25A23]] (+0.61, fdr 1e-05); moves opposite to [[GEN1]] (-0.53, fdr 2e-04), [[AVEN]] (-0.52, fdr 9e-05), [[MSANTD2]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SSPOP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +7.7 | 9e-12 | 23/46 (A498, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +6.9 | 1e-09 | 19/42 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +6.7 | 4e-09 | 5/8 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 2e-05 | 15/45 (CFPAC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.9 | 1e-04 | 14/46 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.32×** | +4.8 | 2e-04 | 9/45 (A-427, A-172, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.011 | 18/46 (A498, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.017 | 5/26 (MIA PaCa-2, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.018 | 11/42 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.018 | 5/40 (SK-MEL-2, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.028 | 9/43 (NCI-H23, SW480, …) | all doses, flat |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.3 | 0.037 | 1/17 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.3 | 0.037 | 6/25 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.037 | 6/43 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.039 | 8/42 (SW 900, NCI-H23, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.044 | 4/35 (LS 180, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.050 | 3/46 (NCI-H2347, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.056 | 11/40 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Procainamide (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.060 | 2/42 (NCI-H2030, SW48) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.308×** | -14.2 | 4e-43 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.334×** | -13.2 | 1e-37 | 40/45 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.348×** | -12.8 | 5e-35 | 30/36 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.430×** | -10.2 | 3e-22 | 33/44 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.459×** | -9.4 | 6e-19 | 29/44 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.521×** | -7.9 | 3e-13 | 21/38 (A549, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.532×** | -7.6 | 2e-12 | 23/44 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.542×** | -7.4 | 9e-12 | 21/46 (SW48, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.526×** | -7.3 | 1e-11 | 23/44 (NCI-H23, NCI-H1792, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.658×** | -7.1 | 5e-11 | 24/40 (NCI-H2030, SNU-423, …) | two highest doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.571×** | -6.8 | 7e-10 | 21/46 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.614×** | -5.9 | 2e-07 | 18/44 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.607×** | -5.7 | 5e-07 | 20/41 (LS 180, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -5.6 | 1e-06 | 18/37 (SW480, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.463×** | -4.6 | 2e-04 | 14/42 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -4.0 | 0.002 | 15/44 (SNU-423, A-172, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.545×** | -3.6 | 0.010 | 4/40 (SK-MEL-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.731×** | -3.6 | 0.010 | 9/39 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.745×** | -3.4 | 0.020 | 9/45 (NCI-H2030, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 14.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0874× (z -14.1) ⚠ toxic; cell-cycle shift, explains ~36% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -12.1) |
| [[HCT15 (line)]] | alt | 7.26 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0398× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 5.14 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 7.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -10.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H23 (line)]] | alt | 6.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0951× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 4.89 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.0) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW48 (line)]] | wt | 7.08 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0385× (z -9.9) |
| [[SW480 (line)]] | alt | 5.08 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.190× (z -8.7) |
| [[A-172 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCRN2]] | +0.65 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CCDC88B]] | +0.64 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[REEP2]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[BCAM]] | +0.59 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[NOXA1]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ANO8]] | +0.58 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[DBP]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PRSS16]] | +0.57 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[CFD]] | +0.57 | +0.43 / +0.60 | both halves | 4e-05 |  |
| [[KBTBD3]] | +0.57 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[MAPK3]] | +0.57 | +0.42 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEN1]] | -0.53 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[AVEN]] | -0.52 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[MSANTD2]] | -0.51 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[DNAJC9]] | -0.49 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[SUV39H2]] | -0.49 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[ORC6]] | -0.49 | -0.52 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSPOP]] | B | SSPOP activity raises ACBD4's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without SSPOP | 0.069 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-1.3, 32.7); signed map (-5.6, 16.5). **Vector** length 44.9, 5.08% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +1.7 | +4.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.6 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.1 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -13.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -14.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -10.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA binding domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:45,132,600-45,144,181 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13322 |
| Reactome | 3 pathways, smallest: Peroxisomal lipid metabolism; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NC06](https://www.uniprot.org/uniprotkb/Q8NC06) (Acyl-CoA-binding domain-containing protein 4):

> Binds medium- and long-chain acyl-CoA esters and may function as an intracellular carrier of acyl-CoA esters.

**Summary**, from NCBI Gene [79777](https://www.ncbi.nlm.nih.gov/gene/79777):

> This gene encodes a member of the acyl-coenzyme A binding domain containing protein family. All family members contain the conserved acyl-Coenzyme A binding domain, which binds acyl-CoA thiol esters. They are thought to play roles in acyl-CoA dependent lipid metabolism. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:23337](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23337) · Entrez [79777](https://www.ncbi.nlm.nih.gov/gene/79777) · UniProt [Q8NC06](https://www.uniprot.org/uniprotkb/Q8NC06) · Ensembl [ENSG00000181513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181513)

## Data

Gene col 11193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11193); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11193]; `tensor/DDL_lfc|DDL_z.npy` [11193]; `embed/gene_vectors.npy` [11193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11193 or target_col == 11193). Every well: [[ACBD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACBD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
