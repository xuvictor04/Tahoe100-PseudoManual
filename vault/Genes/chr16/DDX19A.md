---
symbol: "DDX19A"
type: "gene"
col: 9711
ensembl_id: "ENSG00000168872"
name: "DEAD-box helicase 19A"
location: "16q22.1"
module: 52
arm: "+"
pooled_cpm: 38.2
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# DDX19A

*DEAD-box helicase 19A* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.92× (z +15.3, q 0e+00, up in 42 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.86× (z +14.6, q 1e-45, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.802× (z -5.2, q 1e-04, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.875× (z -4.5, q 0.002, down in 16 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GON4L]] (+0.67, fdr 7e-06), [[CTU2]] (+0.63, fdr 1e-05), [[ATAD3B]] (+0.63, fdr 1e-05); moves opposite to [[RAB21]] (-0.65, fdr 8e-06), [[NCKAP1]] (-0.55, fdr 1e-05), [[CHASERR]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ATXN1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +15.3 | 0e+00 | 42/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +14.6 | 1e-45 | 42/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.83×** | +14.2 | 2e-43 | 43/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.82×** | +14.0 | 1e-42 | 43/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +12.6 | 3e-34 | 42/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.67×** | +12.0 | 3e-31 | 36/48 (SW480, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +11.2 | 2e-27 | 41/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +10.7 | 5e-25 | 33/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.07×** | +9.0 | 2e-17 | 37/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +7.4 | 8e-12 | 32/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +6.8 | 6e-10 | 25/48 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +6.6 | 2e-09 | 28/48 (A-172, NCI-H460, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +6.4 | 7e-09 | 23/47 (A-172, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +5.5 | 2e-06 | 23/48 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.27×** | +5.4 | 3e-06 | 23/47 (SW480, HT-29, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +4.5 | 2e-04 | 18/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.003 | 11/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.005 | 8/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.007 | 7/48 (MIA PaCa-2, Hs 766T, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.009 | 9/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.011 | 9/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.016 | 4/48 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9711.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.802×** | -5.2 | 1e-04 | 24/48 (LS 180, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.875× | -4.5 | 0.002 | 16/48 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.827×** | -4.3 | 0.003 | 19/47 (CFPAC-1, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.840× | -4.1 | 0.004 | 16/48 (SNU-423, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.836× | -4.1 | 0.004 | 16/47 (C-33 A, A-427, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.836× | -4.1 | 0.004 | 14/47 (A498, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.874× | -3.9 | 0.008 | 14/48 (H4, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.861× | -3.5 | 0.028 | 15/47 (LoVo, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.853× | -3.5 | 0.030 | 12/48 (NCI-H460, HEC-1-A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.904× | -3.4 | 0.037 | 15/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.821×** | -3.3 | 0.044 | 14/47 (CHP-212, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.873× | -3.2 | 0.059 | 13/48 (A-427, NCI-H2030, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.875× | -3.2 | 0.064 | 8/48 (LoVo, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.910× | -3.1 | 0.068 | 10/48 (A-427, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.895× | -3.1 | 0.068 | 7/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.878× | -3.1 | 0.068 | 11/47 (AsPC-1, HS-578T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.886× | -3.1 | 0.068 | 9/48 (COLO 205, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **0.785×** | -3.0 | 0.083 | 5/48 (SHP-77, C-33 A, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 63.1 | 7 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +14.0) | [[Lonafarnib (drug)]] 5 µM 0.324× (z -8.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 39.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 35.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 25.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +11.2) | — |
| [[LoVo (line)]] | wt | 36.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.31× (z +8.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 30.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.1) | — |
| [[A-172 (line)]] | wt | 34.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.0) | — |
| [[A-427 (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 64.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 36.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.334× (z -9.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 40.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.65× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.2) | — |
| [[RKO (line)]] | wt | 61.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 82.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 44.0 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0681× (z -8.9) |
| [[SW 900 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GON4L]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CTU2]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ATAD3B]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[DIABLO]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MECR]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[DDX18]] | +0.59 | +0.52 / +0.70 | both halves | 1e-05 | same gene group; STRING 444 |
| [[SLC25A32]] | +0.59 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[SCFD2]] | +0.59 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[NUP214]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 | STRING 970 |
| [[OPA3]] | +0.58 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ISG20L2]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[METTL2B]] | +0.58 | +0.49 / +0.62 | both halves | 1e-05 | STRING 480 |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB21]] | -0.65 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[NCKAP1]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[CHASERR]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ABI1]] | -0.53 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[FMR1]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[KDM6A]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[VPS26A]] | -0.52 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[YPEL5]] | -0.52 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[PCMTD1]] | -0.52 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[CLK1]] | -0.52 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[RNF11]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[FBXO7]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN1-AS1]] | B | ATXN1-AS1 activity lowers DDX19A's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 1.51× higher at baseline in the lines without ATXN1-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-4.4, -27.6); signed map (-46.9, -17.3). **Vector** length 83.2, 17.8% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.9 | +12.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.7 | +14.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +7.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.0 | +11.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.0 | +14.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.1 | +3.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -4.1 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.0 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.3 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 19A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:70,346,861-70,373,383 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11126; previously DDX19L |
| Gene groups (HGNC) | DEAD-box helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUU7](https://www.uniprot.org/uniprotkb/Q9NUU7) (ATP-dependent RNA helicase DDX19A):

> ATP-dependent RNA helicase involved in mRNA export from the nucleus. Rather than unwinding RNA duplexes, DDX19 functions as a remodeler of ribonucleoprotein particles, whereby proteins bound to nuclear mRNA are dissociated and replaced by cytoplasmic mRNA binding proteins.

**Summary**, from NCBI Gene [55308](https://www.ncbi.nlm.nih.gov/gene/55308):

> Predicted to enable RNA helicase activity and mRNA binding activity. Predicted to be involved in poly(A)+ mRNA export from nucleus. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25628) · Entrez [55308](https://www.ncbi.nlm.nih.gov/gene/55308) · UniProt [Q9NUU7](https://www.uniprot.org/uniprotkb/Q9NUU7) · Ensembl [ENSG00000168872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168872)

## Data

Gene col 9711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9711); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9711]; `tensor/DDL_lfc|DDL_z.npy` [9711]; `embed/gene_vectors.npy` [9711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9711 or target_col == 9711). Every well: [[DDX19A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX19A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
