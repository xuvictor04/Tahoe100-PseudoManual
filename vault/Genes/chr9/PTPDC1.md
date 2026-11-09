---
symbol: "PTPDC1"
type: "gene"
col: 8129
ensembl_id: "ENSG00000158079"
name: "protein tyrosine phosphatase domain containing 1"
location: "9q22.32"
module: 18
arm: "+"
pooled_cpm: 32.09
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PTPDC1

*protein tyrosine phosphatase domain containing 1* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.51× (z +5.8, q 4e-06, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.481× (z -14.5, q 6e-45, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.293× (z -9.0, q 3e-17, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANP32B]] (+0.57, fdr 4e-05), [[SLC38A1]] (+0.53, fdr 2e-05), [[NBPF15]] (+0.52, fdr 2e-05); moves opposite to [[IFFO2]] (-0.52, fdr 3e-05), [[EXT1]] (-0.52, fdr 5e-05), [[LIMA1]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SYTL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +5.8 | 4e-06 | 31/48 (RKO, C-33 A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.081 | 23/47 (HS-578T, Hs 766T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.26× | +3.3 | 0.21 | 17/47 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.32 | 8/47 (NCI-H460, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 16 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8129.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.481×** | -14.5 | 6e-45 | 37/47 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.462×** | -10.8 | 1e-24 | 39/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.465×** | -10.7 | 1e-24 | 39/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.293×** | -9.0 | 3e-17 | 45/48 (PANC-1, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.524×** | -8.7 | 4e-16 | 34/47 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.369×** | -7.3 | 3e-11 | 35/47 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.597×** | -7.2 | 5e-11 | 32/47 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.607×** | -7.0 | 2e-10 | 34/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.616×** | -6.8 | 9e-10 | 29/47 (H4, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.625×** | -6.6 | 3e-09 | 29/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.636×** | -6.3 | 1e-08 | 31/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.699×** | -4.8 | 7e-05 | 25/47 (LS 180, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.709×** | -4.8 | 7e-05 | 24/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.712×** | -4.7 | 9e-05 | 25/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.717×** | -4.4 | 4e-04 | 22/48 (HT-29, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.654×** | -3.1 | 0.054 | 17/47 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 60.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -20.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HOP62 (line)]] | alt | 34.5 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -18.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.343× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 31.7 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 41.1 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.143× (z -10.5) |
| [[SW480 (line)]] | alt | 30.8 | 0 | 5 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0946× (z -12.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.429× (z -8.5) |
| [[A-427 (line)]] | wt | 40.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[H4 (line)]] | wt | 26.2 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.148× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 67.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -19.6) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.423× (z -9.2) |
| [[HS-578T (line)]] | alt | 24.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -12.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 18.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[A549 (line)]] | wt | 32.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -12.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H1792 (line)]] | alt | 27.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -14.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[C32 (line)]] | wt | 25.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -8.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HCT15 (line)]] | alt | 38.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 43.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.203× (z -9.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H23 (line)]] | alt | 40.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SHP-77 (line)]] | alt | 43.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[SNU-423 (line)]] | alt | 46.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -20.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A498 (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -19.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0514× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.329× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.127× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.307× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LOX-IMVI (line)]] | wt | 25.6 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0628× (z -10.0) |
| [[LS 180 (line)]] | wt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[RKO (line)]] | wt | 36.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0263× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.4) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SK-MEL-2 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.4) ⚠ cell-cycle shift, explains ~55% of this change |
| [[AN3 CA (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANP32B]] | +0.57 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[SLC38A1]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[NBPF15]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TYRO3]] | +0.51 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SLC25A15]] | +0.51 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[CHPT1]] | +0.51 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PDS5A]] | +0.51 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[TUBGCP4]] | +0.50 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TXNRD3]] | +0.50 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[METTL3]] | +0.49 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[STARD9]] | +0.49 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[PRIMPOL]] | +0.48 | +0.51 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFFO2]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[EXT1]] | -0.52 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[LIMA1]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[MEIS1]] | -0.48 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[IKZF2]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[AP1G1]] | -0.47 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[NR4A3]] | -0.47 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[CTNND1]] | -0.45 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ATP1B1]] | -0.45 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[ATP8B1]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[KCNN3]] | -0.45 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[ABCA7]] | -0.45 | -0.43 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYTL2]] | B | SYTL2 activity lowers PTPDC1's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 1.51× higher at baseline in the lines without SYTL2 | 0.076 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-14.7, 42.8); signed map (-22.8, -52.0). **Vector** length 67.6, 14.0% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | -0.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.4 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -4.3 | -14.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -9.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -7.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32 — chr9:94,030,794-94,109,856 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTP9Q22, FLJ37312 |
| Gene groups (HGNC) | CDC14 phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [A2A3K4](https://www.uniprot.org/uniprotkb/A2A3K4) (Protein tyrosine phosphatase domain-containing protein 1):

> May play roles in cilia formation and/or maintenance.

**Summary**, from NCBI Gene [138639](https://www.ncbi.nlm.nih.gov/gene/138639):

> The protein encoded by this gene contains a characteristic motif of protein tyrosine phosphatases (PTPs). PTPs regulate activities of phosphoproteins through dephosphorylation. They are signaling molecules involved in the regulation of a wide variety of biological processes. The specific function of this protein has not yet been determined. Alternatively spliced transcript variants encoding distinct isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30184) · Entrez [138639](https://www.ncbi.nlm.nih.gov/gene/138639) · UniProt [A2A3K4](https://www.uniprot.org/uniprotkb/A2A3K4) · Ensembl [ENSG00000158079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158079)

## Data

Gene col 8129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8129); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8129]; `tensor/DDL_lfc|DDL_z.npy` [8129]; `embed/gene_vectors.npy` [8129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8129 or target_col == 8129). Every well: [[PTPDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
