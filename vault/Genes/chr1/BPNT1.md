---
symbol: "BPNT1"
type: "gene"
col: 8582
ensembl_id: "ENSG00000162813"
name: "3'(2'), 5'-bisphosphate nucleotidase 1"
location: "1q41"
module: 17
arm: "+"
pooled_cpm: 13.07
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 16
n_dd_up_clean: 18
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# BPNT1

*3'(2'), 5'-bisphosphate nucleotidase 1* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.99× (z +12.1, q 6e-31, up in 28 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.61× (z +11.8, q 1e-29, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.614× (z -8.6, q 6e-15, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA5]] (+0.62, fdr 7e-06), [[FRG1BP]] (+0.62, fdr 7e-06), [[PRCP]] (+0.60, fdr 1e-05); moves opposite to [[RANBP17]] (-0.66, fdr 1e-05), [[PAQR4]] (-0.58, fdr 1e-05), [[UGGT2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CCL28]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +12.1 | 6e-31 | 28/36 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +12.0 | 6e-31 | 19/28 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +11.8 | 1e-29 | 35/48 (A-172, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +8.9 | 8e-17 | 27/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +8.5 | 2e-15 | 25/40 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.3 | 1e-14 | 31/45 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +8.0 | 8e-14 | 17/32 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +7.2 | 5e-11 | 20/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +7.1 | 7e-11 | 24/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.44×** | +6.4 | 9e-09 | 22/46 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +5.6 | 1e-06 | 21/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +5.6 | 1e-06 | 21/46 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.3 | 4e-06 | 17/48 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +5.2 | 8e-06 | 16/44 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.9 | 3e-05 | 18/45 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +4.3 | 5e-04 | 13/46 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 7e-04 | 15/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.003 | 11/46 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.003 | 12/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8582.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.614×** | -8.6 | 6e-15 | 29/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.617×** | -8.5 | 7e-15 | 35/46 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -8.3 | 2e-14 | 26/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.638×** | -7.9 | 4e-13 | 28/46 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.663×** | -7.2 | 6e-11 | 23/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -6.0 | 2e-07 | 23/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.748×** | -5.1 | 3e-05 | 14/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.747×** | -4.9 | 6e-05 | 17/46 (CFPAC-1, A498, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.759×** | -4.8 | 9e-05 | 17/47 (A-172, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.768×** | -4.6 | 2e-04 | 16/47 (NCI-H460, AN3 CA, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.779×** | -4.4 | 6e-04 | 16/46 (MIA PaCa-2, BT-474, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.654×** | -3.9 | 0.005 | 13/44 (AsPC-1, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.808×** | -3.7 | 0.008 | 18/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.679×** | -3.6 | 0.015 | 12/46 (SW 900, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.867× | -3.5 | 0.015 | 9/48 (CFPAC-1, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.831×** | -3.1 | 0.073 | 13/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 4.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0858× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -12.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 9.78 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0909× (z -9.2) |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0972× (z -11.7) |
| [[A-172 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[FRG1BP]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[PRCP]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PREPL]] | +0.60 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[COPS5]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MINDY1]] | +0.58 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[FBXO8]] | +0.57 | +0.71 / +0.40 | both halves | 5e-05 |  |
| [[MBIP]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[RIDA]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TRAPPC6B]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[IFT46]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[MAGED2]] | +0.56 | +0.48 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP17]] | -0.66 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[PAQR4]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[UGGT2]] | -0.58 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MTHFD1L]] | -0.58 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[PWP2]] | -0.55 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[PPM1G]] | -0.55 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[MAD1L1]] | -0.54 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[LYRM4]] | -0.54 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.53 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[DOCK1]] | -0.53 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TRAPPC9]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[EHMT1]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL28]] | B | CCL28 activity raises BPNT1's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.29× lower at baseline in the lines without CCL28 | 0.071 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[MTHFD1L]] | C | MTHFD1L activity lowers BPNT1's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.80× higher at baseline in the lines without MTHFD1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.413). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-23.3, 2.5); signed map (-24.5, -10.2). **Vector** length 70.1, 11.7% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.1 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +12.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.1 | +6.4 |
|  | [[NG25 (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +5.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +4.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -8.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -7.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -4.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | 3'(2'), 5'-bisphosphate nucleotidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:220,057,482-220,090,462 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 3 pathways, smallest: Cytosolic sulfonation of small molecules; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [O95861](https://www.uniprot.org/uniprotkb/O95861) (3'(2'),5'-bisphosphate nucleotidase 1):

> Phosphatase that converts 3'(2')-phosphoadenosine 5'-phosphate (PAP) to AMP and inositol 1,4-bisphosphate (Ins(1,4)P2) to inositol 4-phosphate. Is also able to hydrolyze adenosine 3'-phosphate 5'-phosphosulfate (PAPS) to adenosine 5'-phosphosulfate (APS) (By similarity). Probably prevents the toxic accumulation of PAP, a compound which inhibits a variety of proteins, including PAPS-utilizing enzymes such as sulfotransferases, and RNA processing enzymes. Could also play a role in inositol …

**Summary**, from NCBI Gene [10380](https://www.ncbi.nlm.nih.gov/gene/10380):

> BPNT1, also called bisphosphate 3-prime-nucleotidase, or BPntase, is a member of a magnesium-dependent phosphomonoesterase family. Lithium, a major drug used to treat manic depression, acts as an uncompetitive inhibitor of BPntase. The predicted human protein is 92% identical to mouse BPntase. BPntase's physiologic role in nucleotide metabolism may be regulated by inositol signaling pathways. The inhibition of human BPntase may account for lithium-induced nephrotoxicity. [provided by RefSeq, …

**Accessions** — [HGNC:1096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1096) · Entrez [10380](https://www.ncbi.nlm.nih.gov/gene/10380) · UniProt [O95861](https://www.uniprot.org/uniprotkb/O95861) · Ensembl [ENSG00000162813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162813)

## Data

Gene col 8582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8582); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8582]; `tensor/DDL_lfc|DDL_z.npy` [8582]; `embed/gene_vectors.npy` [8582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8582 or target_col == 8582). Every well: [[BPNT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BPNT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
