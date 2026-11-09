---
symbol: "RBM20"
type: "gene"
col: 12796
ensembl_id: "ENSG00000203867"
name: "RNA binding motif protein 20"
location: "10q25.2"
module: 9
arm: "+"
pooled_cpm: 30.2
n_lines_expressing: 25
n_dd_up: 24
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 13
direction_downstream: 5
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# RBM20

*RNA binding motif protein 20* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +22.0, q 0e+00, up in 4 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.704× (z -5.8, q 5e-06, down in 13 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASXL3]] (+0.74, fdr 7e-06), [[SNCA]] (+0.67, fdr 7e-06), [[NELL2]] (+0.65, fdr 7e-06); moves opposite to [[RIN2]] (-0.44, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CSMD3]] → it (grade B ⚠); 5 go from it, the strongest it → [[BMP5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +22.0 | 0e+00 | 4/23 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.20×** | +18.3 | 0e+00 | 13/23 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +11.8 | 7e-30 | 16/22 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +9.2 | 4e-18 | 1/19 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +8.3 | 1e-14 | 12/23 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.8 | 1e-09 | 0/18 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +6.4 | 1e-08 | 11/23 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.45×** | +6.1 | 8e-08 | 13/23 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +5.8 | 3e-07 | 7/23 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +5.5 | 2e-06 | 9/22 (NCI-H460, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.37×** | +4.9 | 4e-05 | 0/21 | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +4.7 | 1e-04 | 7/22 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 1e-04 | 12/20 (NCI-H460, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 1e-04 | 1/22 (SNU-423) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +4.6 | 1e-04 | 0/19 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 2e-04 | 1/20 (A-172) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 5e-04 | 8/23 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.001 | 5/22 (SW480, A549, …) | rises with dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.002 | 4/23 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.003 | 9/22 (A549, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12796.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -5.8 | 5e-06 | 13/22 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.718×** | -5.4 | 1e-05 | 13/21 (NCI-H460, A-427, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -5.2 | 3e-05 | 9/22 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.742×** | -4.9 | 1e-04 | 14/21 (NCI-H460, A-427, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.620×** | -4.1 | 0.005 | 8/22 (SW480, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.790×** | -3.9 | 0.010 | 17/23 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.780×** | -3.8 | 0.010 | 2/23 (NCI-H23, A-427) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.812×** | -3.4 | 0.042 | 12/23 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.823× | -3.1 | 0.13 | 2/23 (SK-MEL-2, NCI-H2030) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.832× | -3.0 | 0.13 | 11/22 (NCI-H460, A-427, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.833× | -3.0 | 0.13 | 15/22 (NCI-H1792, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 134 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 30.9 | 3 | 9 (7 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.47× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.245× (z -12.1) |
| [[A-427 (line)]] | wt | 51.2 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0988× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.377× (z -8.5) |
| [[CHP-212 (line)]] | wt | 332 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0861× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -17.9) |
| [[SW480 (line)]] | alt | 153 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -22.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.189× (z -20.9) |
| [[A549 (line)]] | wt | 65.3 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -16.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 104 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0444× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.246× (z -11.7) |
| [[SHP-77 (line)]] | alt | 211 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.252× (z -16.3) |
| [[SK-MEL-2 (line)]] | alt | 65.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 472 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 41.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 91.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -15.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 39.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 10.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.77× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 8.23 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.38× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 9.31 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.18 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASXL3]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SNCA]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[NELL2]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[CDH10]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TMEM108]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[GALNT13]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[SLITRK5]] | +0.60 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[ERBB4]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CRISPLD1]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[BCL11A]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[KCTD8]] | +0.57 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[KCNH7]] | +0.55 | +0.44 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIN2]] | -0.44 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 2, C 11. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSMD3]] | B | CSMD3 activity weakens RBM20's drug response | lines that do not express CSMD3 (13) vs lines expressing it (10) | (z diff -2.87); strongest at Tucidinostat 5 µM: 2.17x vs 1.08x (z diff -5.7) | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; target measured in part of the lines; artifact flags |
| [[RIN2]] | B | RIN2 activity lowers RBM20's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 4.58× higher at baseline in the lines without RIN2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises RBM20's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 5.86× lower at baseline in the lines without SLC25A24P1 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises RBM20's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 5.07× lower at baseline in the lines without CSMD3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises RBM20's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 4.79× lower at baseline in the lines without RUNX1T1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises RBM20's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 5.17× lower at baseline in the lines without GABRG2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises RBM20's level | lines that do not express BCHE (35) vs lines expressing it (15) | 4.85× lower at baseline in the lines without BCHE | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises RBM20's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 6.22× lower at baseline in the lines without CDH18 | 0.033 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[POU6F2]] | C | POU6F2 activity raises RBM20's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 4.96× lower at baseline in the lines without POU6F2 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent; co-absent with the target |
| [[FRG1FP]] | C | FRG1FP activity raises RBM20's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 3.29× lower at baseline in the lines without FRG1FP | 0.067 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |
| [[ADGRL3]] | C | ADGRL3 activity raises RBM20's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 3.22× lower at baseline in the lines without ADGRL3 | 0.068 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent; co-absent with the target |
| [[LINC02864]] | C | LINC02864 activity raises RBM20's level | lines that do not express LINC02864 (36) vs lines expressing it (14) | 4.06× lower at baseline in the lines without LINC02864 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC00824, LINC01205; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP5]] | C | RBM20 activity raises BMP5's level | lines that do not express RBM20 (25) vs lines expressing it (25) | 3.17× lower at baseline in the lines without RBM20 | 0.044 | ⚠ within organs, on part of the lines; also absent: NOVA2, VAT1L, CDH18; co-absent with the target |
| [[SLC25A24P1]] | C | RBM20 activity raises SLC25A24P1's level | lines that do not express RBM20 (25) vs lines expressing it (25) | 2.12× lower at baseline in the lines without RBM20 | 0.051 | ⚠ within organs, on part of the lines; also absent: NOVA2, VAT1L, CDH18; co-absent with the target |
| [[JPH3]] | C | RBM20 activity raises JPH3's level | lines that do not express RBM20 (25) vs lines expressing it (25) | 3.17× lower at baseline in the lines without RBM20 | 0.059 | ⚠ within organs, on part of the lines; also absent: NOVA2, VAT1L, CDH18; co-absent with the target |
| [[CSMD3]] | C | RBM20 activity raises CSMD3's level | lines that do not express RBM20 (25) vs lines expressing it (25) | 2.74× lower at baseline in the lines without RBM20 | 0.072 | ⚠ within organs, on part of the lines; also absent: NOVA2, VAT1L, CDH18; co-absent with the target |
| [[ROBO2]] | C | RBM20 activity raises ROBO2's level | lines that do not express RBM20 (25) vs lines expressing it (25) | 2.64× lower at baseline in the lines without RBM20 | 0.094 | ⚠ within organs, on part of the lines; also absent: NOVA2, VAT1L, CDH18; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, 35.3); signed map (40.3, 37.7). **Vector** length 74.8, 20.2% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.4 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +18.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.8 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +22.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +4.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.1 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +4.3 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.9 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -5.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.5 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -2.2 | -2.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:110,644,336-110,839,468 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers matrin-type; RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T481](https://www.uniprot.org/uniprotkb/Q5T481) (RNA-binding protein 20):

> RNA-binding protein that acts as a regulator of mRNA splicing of a subset of genes encoding key structural proteins involved in cardiac development, such as TTN (Titin), CACNA1C, CAMK2D or PDLIM5/ENH. Acts as a repressor of mRNA splicing: specifically binds the 5'UCUU-3' motif that is predominantly found within intronic sequences of pre-mRNAs, leading to the exclusion of specific exons in target transcripts. RBM20-mediated exon skipping is hormone-dependent and is essential for TTN isoform …

**Summary**, from NCBI Gene [282996](https://www.ncbi.nlm.nih.gov/gene/282996):

> This gene encodes a protein that binds RNA and regulates splicing. Mutations in this gene have been associated with familial dilated cardiomyopathy. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:27424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27424) · Entrez [282996](https://www.ncbi.nlm.nih.gov/gene/282996) · UniProt [Q5T481](https://www.uniprot.org/uniprotkb/Q5T481) · Ensembl [ENSG00000203867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203867)

## Data

Gene col 12796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12796); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12796]; `tensor/DDL_lfc|DDL_z.npy` [12796]; `embed/gene_vectors.npy` [12796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12796 or target_col == 12796). Every well: [[RBM20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
