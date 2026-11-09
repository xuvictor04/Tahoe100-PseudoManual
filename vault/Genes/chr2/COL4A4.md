---
symbol: "COL4A4"
type: "gene"
col: 1305
ensembl_id: "ENSG00000081052"
name: "collagen type IV alpha 4 chain"
location: "2q36.3"
module: 19
arm: "+"
pooled_cpm: 17.29
n_lines_expressing: 22
n_dd_up: 16
n_dd_down: 22
n_dd_up_clean: 12
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 12
direction_downstream: 13
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# COL4A4

*collagen type IV alpha 4 chain* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.14× (z +21.4, q 0e+00, up in 19 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.494× (z -9.3, q 7e-18, down in 17 of 19 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL4A3]] (+0.90, fdr 7e-06, ⚠ same locus), [[RADIL]] (+0.64, fdr 1e-05), [[EBF2]] (+0.63, fdr 7e-06), [[FAM124A]] (+0.61, fdr 1e-05); moves opposite to [[ARMCX4]] (-0.50, fdr 5e-05), [[COQ7]] (-0.44, fdr 4e-04), [[ZNF532]] (-0.43, fdr 5e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[EBF2]] → it (grade B ⚠); 13 go from it, the strongest it → [[GALNT16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.14×** | +21.4 | 0e+00 | 19/20 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.95×** | +14.3 | 5e-44 | 19/19 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +13.6 | 1e-39 | 3/14 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +8.9 | 6e-17 | 3/18 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.6 | 8e-16 | 1/9 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +8.5 | 1e-15 | 13/19 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +8.3 | 8e-15 | 11/19 (NCI-H1573, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +7.7 | 7e-13 | 10/19 (A-427, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +7.4 | 1e-11 | 11/19 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.15×** | +5.3 | 7e-06 | 11/20 (NCI-H23, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +4.6 | 2e-04 | 1/12 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +4.0 | 0.003 | 9/19 (BT-474, A498, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.003 | 1/18 (A-427) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.015 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.1 | 0.078 | 3/19 (A549, A-172, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.078 | 6/19 (NCI-H1573, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.494×** | -9.3 | 7e-18 | 17/19 (NCI-H460, A549, …) | two highest doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.531×** | -8.4 | 2e-14 | 17/19 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.523×** | -8.2 | 3e-14 | 16/18 (NCI-H460, A549, …) | two highest doses | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.551×** | -7.9 | 4e-13 | 14/19 (NCI-H460, A549, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -6.0 | 2e-07 | 13/19 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.430×** | -5.8 | 5e-07 | 12/18 (HEC-1-A, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.735×** | -5.8 | 7e-07 | 11/19 (SK-MEL-2, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -5.5 | 2e-06 | 16/18 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.660×** | -5.5 | 3e-06 | 13/17 (A549, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -4.2 | 0.001 | 10/19 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -3.9 | 0.004 | 11/19 (NCI-H460, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.728×** | -3.9 | 0.005 | 2/19 (SW 900, HEC-1-A) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.574×** | -3.8 | 0.005 | 10/20 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.751×** | -3.8 | 0.007 | 8/19 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.761×** | -3.6 | 0.012 | 6/19 (A-427, C-33 A, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.764×** | -3.6 | 0.013 | 12/19 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.828×** | -3.5 | 0.014 | 8/20 (NCI-H460, H4, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 85.5 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -25.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0607× (z -23.6) |
| [[A549 (line)]] | wt | 83.1 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0748× (z -30.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0573× (z -23.4) |
| [[HEC-1-A (line)]] | alt | 95.2 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -16.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.230× (z -13.3) |
| [[LoVo (line)]] | wt | 20.5 | 1 | 7 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.34× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -15.2) |
| [[J82 (line)]] | alt | 26.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 90.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0572× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.126× (z -9.6) |
| [[A-172 (line)]] | wt | 26.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0906× (z -15.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 7.28 | 0 | 2 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0474× (z -12.4) |
| [[A498 (line)]] | wt | 5.19 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.06× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -10.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.269× (z -9.4) |
| [[SW480 (line)]] | alt | 6.77 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.33× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.203× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 17.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.96× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 7.04 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0543× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 9.82 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0781× (z -9.4) |
| [[AN3 CA (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL4A3]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | same gene group; pathway: Anchoring fibril formation; STRING 995; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[RADIL]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[EBF2]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[FAM124A]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[TMEM170B]] | +0.60 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[RAB3C]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SCN9A]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LRRC63]] | +0.56 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[KIF26A]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[MAPT]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[GALNT16]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[UNC5D]] | +0.54 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[JAKMIP1]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX4]] | -0.50 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[COQ7]] | -0.44 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[ZNF532]] | -0.43 | -0.24 / -0.42 | both halves | 5e-04 | STRING 463 |
| [[TMEM199]] | -0.43 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[PGBD4]] | -0.43 | -0.33 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF2]] | B | EBF2 activity raises COL4A4's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.18× lower at baseline in the lines without EBF2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[NR2E3]] | B | NR2E3 activity raises COL4A4's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 1.89× lower at baseline in the lines without NR2E3 | 0.078 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[CSF2RA]] | B | CSF2RA activity raises COL4A4's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 2.33× lower at baseline in the lines without CSF2RA | 0.085 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A |
| [[GALNT12]] | B | GALNT12 activity raises COL4A4's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 2.48× lower at baseline in the lines without GALNT12 | 0.087 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[COL4A3]] | C | COL4A3 activity raises COL4A4's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 5.32× lower at baseline in the lines without COL4A3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[RADIL]] | C | RADIL activity raises COL4A4's level | lines that do not express RADIL (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without RADIL | 0.008 | ⚠ within organs, on part of the lines; also absent: ZYG11A, OLFM1, JAKMIP1; maybe low, not absent; co-absent with the target |
| [[FAM124A]] | C | FAM124A activity raises COL4A4's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 2.99× lower at baseline in the lines without FAM124A | 0.042 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |
| [[ANKRD6]] | C | ANKRD6 activity raises COL4A4's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.86× lower at baseline in the lines without ANKRD6 | 0.055 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |
| [[SLAIN1]] | C | SLAIN1 activity raises COL4A4's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without SLAIN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2; co-absent with the target |
| [[STOX2]] | C | STOX2 activity raises COL4A4's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without STOX2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[KCNS3]] | C | KCNS3 activity raises COL4A4's level | lines that do not express KCNS3 (16) vs lines expressing it (34) | 2.73× lower at baseline in the lines without KCNS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: EFCAB13, JHY, SAA1; maybe low, not absent; co-absent with the target |
| [[MAPK4]] | C | MAPK4 activity raises COL4A4's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 3.18× lower at baseline in the lines without MAPK4 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT16]] | B | COL4A4 activity raises GALNT16's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without COL4A4 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A |
| [[EBF2]] | B | COL4A4 activity raises EBF2's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without COL4A4 | 0.041 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A |
| [[SGSM1]] | B | COL4A4 activity raises SGSM1's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 1.45× lower at baseline in the lines without COL4A4 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A |
| [[GALNT12]] | B | COL4A4 activity raises GALNT12's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 1.66× lower at baseline in the lines without COL4A4 | 0.093 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A |
| [[COL4A3]] | C | COL4A4 activity raises COL4A3's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 5.04× lower at baseline in the lines without COL4A4 | 1e-04 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[EPB41L4A]] | C | COL4A4 activity raises EPB41L4A's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 3.25× lower at baseline in the lines without COL4A4 | 0.008 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[WASF3]] | C | COL4A4 activity raises WASF3's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 2.89× lower at baseline in the lines without COL4A4 | 0.040 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[FAM124A]] | C | COL4A4 activity raises FAM124A's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without COL4A4 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[LRRC63]] | C | COL4A4 activity raises LRRC63's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without COL4A4 | 0.059 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[NRXN3]] | C | COL4A4 activity raises NRXN3's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 3.39× lower at baseline in the lines without COL4A4 | 0.061 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[ST6GAL2]] | C | COL4A4 activity raises ST6GAL2's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 2.06× lower at baseline in the lines without COL4A4 | 0.061 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[KCNS3]] | C | COL4A4 activity raises KCNS3's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 2.31× lower at baseline in the lines without COL4A4 | 0.062 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.457). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.2, 39.7); signed map (40.1, 47.9). **Vector** length 70.9, 21.2% of its response variance represented; |z| ≥ 3 in 628 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +21.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +5.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -9.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | collagen type IV alpha 4 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:227,002,714-227,164,453 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CA44 |
| Gene groups (HGNC) | Network forming collagens |
| Reactome | 24 pathways, smallest: Anchoring fibril formation; Crosslinking of collagen fibrils; Fibronectin matrix formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P53420](https://www.uniprot.org/uniprotkb/P53420) (Collagen alpha-4(IV) chain):

> Type IV collagen is the major structural component of glomerular basement membranes (GBM), forming a 'chicken-wire' meshwork together with laminins, proteoglycans and entactin/nidogen.

**Summary**, from NCBI Gene [1286](https://www.ncbi.nlm.nih.gov/gene/1286):

> This gene encodes one of the six subunits of type IV collagen, the major structural component of basement membranes. This particular collagen IV subunit, however, is only found in a subset of basement membranes. Like the other members of the type IV collagen gene family, this gene is organized in a head-to-head conformation with another type IV collagen gene so that each gene pair shares a common promoter. Mutations in this gene are associated with type II autosomal recessive Alport syndrome …

**Accessions** — [HGNC:2206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2206) · Entrez [1286](https://www.ncbi.nlm.nih.gov/gene/1286) · UniProt [P53420](https://www.uniprot.org/uniprotkb/P53420) · Ensembl [ENSG00000081052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081052)

## Data

Gene col 1305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1305); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1305]; `tensor/DDL_lfc|DDL_z.npy` [1305]; `embed/gene_vectors.npy` [1305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1305 or target_col == 1305). Every well: [[COL4A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL4A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
