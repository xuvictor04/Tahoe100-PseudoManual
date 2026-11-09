---
symbol: "SRP14-DT"
type: "gene"
col: 14545
ensembl_id: "ENSG00000248508"
name: "SRP14 divergent transcript"
location: "15q15.1"
module: 10
arm: "+"
pooled_cpm: 8.14
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 13
n_dd_up_clean: 22
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SRP14-DT

*SRP14 divergent transcript* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.52× (z +6.0, q 1e-06, up in 21 of 46 measured lines) ⚠ cell-cycle shift, explains ~75% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.78× (z +5.9, q 1e-06, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.343× (z -10.9, q 6e-25, down in 33 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.274× (z -6.9, q 5e-10, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPERE]] (+0.60, fdr 1e-05), [[LINC00412]] (+0.59, fdr 1e-05), [[RPAP3-DT]] (+0.58, fdr 7e-06); moves opposite to [[SRGAP2D]] (-0.56, fdr 3e-05), [[CD320]] (-0.54, fdr 4e-05), [[CMC2]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRIQ3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.52×** | +6.0 | 1e-06 | 21/46 (LoVo, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.78×** | +5.9 | 1e-06 | 26/46 (KATO III, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +5.3 | 2e-05 | 25/44 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.1 | 6e-05 | 9/15 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +4.7 | 3e-04 | 19/46 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.004 | 13/43 (KATO III, A498, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.004 | 19/45 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.0 | 0.004 | 8/30 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.006 | 14/44 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.015 | 8/46 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.015 | 11/46 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.47×** | +3.5 | 0.020 | 9/47 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +3.5 | 0.021 | 9/24 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **1.92×** | +3.5 | 0.022 | 2/45 (HEC-1-A, SW480) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.032 | 12/43 (SW480, NCI-H1792, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.032 | 7/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.86×** | +3.3 | 0.032 | 0/37 | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.032 | 8/46 (A498, CFPAC-1, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.035 | 7/46 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.050 | 13/45 (SW480, C32, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14545.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.343×** | -10.9 | 6e-25 | 33/43 (COLO 205, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.357×** | -10.5 | 2e-23 | 41/46 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.444×** | -8.3 | 2e-14 | 33/45 (COLO 205, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.497×** | -7.1 | 1e-10 | 31/44 (Panc 03.27, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.274×** | -6.9 | 5e-10 | 29/45 (NCI-H1792, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.328×** | -5.9 | 3e-07 | 25/42 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -5.3 | 8e-06 | 27/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.643×** | -4.3 | 1e-03 | 16/44 (A-427, NCI-H1792, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.650×** | -4.2 | 0.001 | 17/37 (COLO 205, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.639×** | -3.7 | 0.012 | 13/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.782×** | -3.6 | 0.018 | 22/41 (COLO 205, NCI-H460, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.675×** | -3.2 | 0.055 | 15/45 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.728×** | -3.1 | 0.075 | 9/46 (SW 1088, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0652× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 8.75 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0835× (z -14.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 15.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 9.02 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 8.63 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -10.4) ⚠ cell-cycle shift, explains ~91% of this change |
| [[A549 (line)]] | wt | 5.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0778× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 7.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -10.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.03 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0760× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 7.34 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0684× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 9.31 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 8.17 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0701× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 6.82 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0711× (z -9.2) |
| [[A-172 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERE]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[LINC00412]] | +0.59 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[RPAP3-DT]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 | same gene group |
| [[ZSCAN30]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[C22orf46]] | +0.57 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[CLIC2]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MYL5]] | +0.57 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[GPRASP1]] | +0.57 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[ACYP2]] | +0.57 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[IDNK]] | +0.57 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[DYNLT2]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[SH2B1]] | +0.56 | +0.54 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2D]] | -0.56 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[CD320]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CMC2]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[COX8A]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[RASA1]] | -0.51 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[NPAT]] | -0.51 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[GPN3]] | -0.49 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[HAUS8]] | -0.49 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[TXNDC17]] | -0.48 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[WDR44]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRIQ3]] | C | LRRIQ3 activity raises SRP14-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.42× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.7, 16.5); signed map (31.5, -12.6). **Vector** length 59.9, 9.59% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +3.8 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.5 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.3 | -7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.3 | +2.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | +0.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.1 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -5.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | SRP14 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q15.1 — chr15:40,039,242-40,080,614 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously SRP14-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48619) · Entrez [100131089](https://www.ncbi.nlm.nih.gov/gene/100131089) · Ensembl [ENSG00000248508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248508)

## Data

Gene col 14545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14545); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14545]; `tensor/DDL_lfc|DDL_z.npy` [14545]; `embed/gene_vectors.npy` [14545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14545 or target_col == 14545). Every well: [[SRP14-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRP14-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
