---
symbol: "TMEM87B"
type: "gene"
col: 7703
ensembl_id: "ENSG00000153214"
name: "transmembrane protein 87B"
location: "2q13"
module: 51
arm: "-"
pooled_cpm: 78.37
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# TMEM87B

*transmembrane protein 87B* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[HI-TOPK-032 (drug)]] 0.05 µM: 1.21× (z +3.7, q 0.073, up in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 2.25×, NCI-H460 1.77×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -24.5, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMC10]] (+0.57, fdr 1e-05), [[METTL21A]] (+0.50, fdr 3e-05), [[SLC35F5]] (+0.49, fdr 3e-05); moves opposite to [[KAT5]] (-0.55, fdr 2e-05), [[MCRS1]] (-0.55, fdr 1e-05), [[ZNF583]] (-0.51, fdr 4e-05).
> It sits in the **-** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ITGA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7703.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 2.25×, NCI-H460 1.77×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.073 | 15/47 (A-427, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.13× | +3.6 | 0.073 | 5/48 (RKO, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.073 | 14/47 (HepG2/C3A, A-172, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.081 | 18/48 (SW48, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | 1.33× | +3.0 | 0.26 | 8/48 (RPMI-7951, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.430×** | -24.5 | 0e+00 | 43/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.432×** | -16.6 | 0e+00 | 40/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -10.5 | 2e-23 | 40/49 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.608×** | -10.2 | 2e-22 | 33/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.608×** | -10.2 | 2e-22 | 40/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -9.5 | 2e-19 | 41/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.633×** | -9.4 | 5e-19 | 35/48 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.641×** | -9.2 | 4e-18 | 36/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.683×** | -7.8 | 3e-13 | 33/48 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.689×** | -7.7 | 1e-12 | 30/48 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.494×** | -7.6 | 2e-12 | 33/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.714×** | -6.9 | 2e-10 | 33/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.719×** | -6.8 | 5e-10 | 28/48 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.720×** | -6.8 | 5e-10 | 34/48 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.749×** | -5.9 | 1e-07 | 27/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.741×** | -5.8 | 2e-07 | 30/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.776×** | -5.2 | 6e-06 | 29/48 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.678×** | -4.2 | 9e-04 | 23/48 (PANC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.714×** | -3.6 | 0.008 | 18/48 (MIA PaCa-2, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.719×** | -3.6 | 0.010 | 20/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.725×** | -3.5 | 0.013 | 14/48 (SW1417, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.727×** | -3.4 | 0.014 | 17/48 (PANC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.0 | 1 (1 ⚠) | 14 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 0.5 µM 0.243× (z -15.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.297× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 133 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -23.8) |
| [[HOP62 (line)]] | alt | 109 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.5) |
| [[PANC-1 (line)]] | alt | 66.9 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -32.2) |
| [[MIA PaCa-2 (line)]] | alt | 82.8 | 0 | 6 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.106× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 68.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -16.6) |
| [[SW480 (line)]] | alt | 89.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -11.5) |
| [[A498 (line)]] | wt | 131 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -20.7) |
| [[BT-474 (line)]] | alt | 97.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -12.8) |
| [[LS 180 (line)]] | wt | 87.9 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -10.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.417× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -14.9) |
| [[A549 (line)]] | wt | 88.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -19.2) |
| [[AsPC-1 (line)]] | alt | 88.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -25.5) |
| [[HS-578T (line)]] | alt | 82.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -22.3) |
| [[NCI-H1573 (line)]] | alt | 100 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 67.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -18.1) |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -19.1) |
| [[SW 900 (line)]] | alt | 78.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 68.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -13.4) |
| [[H4 (line)]] | wt | 105 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -9.4) |
| [[HCT15 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -11.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.440× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 80.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.356× (z -8.9) |
| [[HT-29 (line)]] | alt | 73.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.6) |
| [[LoVo (line)]] | wt | 54.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.387× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 54.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -11.6) |
| [[RKO (line)]] | wt | 50.7 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.321× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 68.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -20.5) |
| [[SNU-1 (line)]] | wt | 42.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[SNU-423 (line)]] | alt | 45.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.9) |
| [[A-172 (line)]] | wt | 92.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -14.7) |
| [[A-427 (line)]] | wt | 55.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.432× (z -8.9) |
| [[COLO 205 (line)]] | alt | 85.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -11.6) |
| [[Hs 766T (line)]] | wt | 75.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 74.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.3) |
| [[KATO III (line)]] | alt | 57.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 62.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 85.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -13.7) |
| [[SW 1088 (line)]] | alt | 85.3 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0844× (z -9.2) |
| [[SW1417 (line)]] | alt | 93.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -8.9) |
| [[AN3 CA (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC10]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[METTL21A]] | +0.50 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[SLC35F5]] | +0.49 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[PIGF]] | +0.47 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[SETD3]] | +0.47 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[RASSF3]] | +0.46 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[CD46]] | +0.46 | +0.43 / +0.49 | both halves | 4e-05 |  |
| [[TPCN1]] | +0.46 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[TMEM50B]] | +0.45 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[SRD5A1]] | +0.45 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[CTNNBIP1]] | +0.45 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[AIDA]] | +0.44 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT5]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[MCRS1]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ZNF583]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ASXL1]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[INO80]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[YJU2]] | -0.51 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[PALLD]] | -0.50 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ZNF644]] | -0.49 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TRMO]] | -0.49 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[EPC2]] | -0.49 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[TMEM18]] | -0.49 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[LURAP1L-AS1]] | -0.48 | -0.54 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA3]] | B | ITGA3 activity raises TMEM87B's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 1.52× lower at baseline in the lines without ITGA3 | 0.035 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[ITGA3]] | B | ITGA3 activity strengthens TMEM87B's drug response | lines that do not express ITGA3 (10) vs lines expressing it (39) | the lines without ITGA3 respond 0.55× as strongly (z diff +1.58); strongest at Homoharringtonine 5 µM: 0.74x vs 0.38x (z diff +4.7) | 0.068 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-35.6, 9.0); signed map (-52.1, 23.7). **Vector** length 94.3, 25.7% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.1 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -24.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.3 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -10.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -16.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -10.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 87B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:112,055,269-112,119,318 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14681 |
| Gene groups (HGNC) | 7TM uncharacterized proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96K49](https://www.uniprot.org/uniprotkb/Q96K49) (Transmembrane protein 87B):

> May be involved in retrograde transport from endosomes to the trans-Golgi network (TGN).

**Summary**, from NCBI Gene [84910](https://www.ncbi.nlm.nih.gov/gene/84910):

> This gene encodes a protein that may interact with human papillomavirus type 18 E6 oncogene. The protein is also likely to be involved in endosome-to-trans-Golgi network retrograde transport. The gene is expressed in adult and fetal tissues, including brain and heart. This gene is a component of the 2q13 deletion syndrome. Mutations in this gene may be associated with congenital heart defects. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:25913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25913) · Entrez [84910](https://www.ncbi.nlm.nih.gov/gene/84910) · UniProt [Q96K49](https://www.uniprot.org/uniprotkb/Q96K49) · Ensembl [ENSG00000153214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153214)

## Data

Gene col 7703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7703); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7703]; `tensor/DDL_lfc|DDL_z.npy` [7703]; `embed/gene_vectors.npy` [7703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7703 or target_col == 7703). Every well: [[TMEM87B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM87B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
