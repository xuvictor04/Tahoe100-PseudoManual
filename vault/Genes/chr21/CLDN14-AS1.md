---
symbol: "CLDN14-AS1"
type: "gene"
col: 13925
ensembl_id: "ENSG00000233818"
name: ""
location: ""
module: 13
arm: "+"
pooled_cpm: 19.25
n_lines_expressing: 34
n_dd_up: 3
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 13
direction_downstream: 23
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CLDN14-AS1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +3.5, q 0.092, up in 13 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.310× (z -15.9, q 0e+00, down in 28 of 32 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.198× (z -11.9, q 2e-30, down in 29 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OR9Q1]] (+0.58, fdr 1e-05), [[LUCAT1]] (+0.57, fdr 1e-05), [[SPOCD1]] (+0.56, fdr 1e-05); moves opposite to [[PRR15L]] (-0.50, fdr 4e-05), [[KCNE3]] (-0.50, fdr 2e-04), [[PROM1]] (-0.50, fdr 7e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LINC00887]] → it (grade B ⚠); 23 go from it, the strongest it → [[MSANTD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.092 | 13/32 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.092 | 11/32 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.092 | 10/32 (A-172, Hs 766T, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.23 | 13/32 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.23 | 11/32 (A-172, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.37× | +3.0 | 0.23 | 11/32 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.310×** | -15.9 | 0e+00 | 28/32 (HEC-1-A, CFPAC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.205×** | -15.2 | 0e+00 | 29/32 (H4, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.249×** | -13.4 | 2e-38 | 27/31 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.198×** | -11.9 | 2e-30 | 29/32 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.296×** | -11.7 | 1e-29 | 25/32 (NCI-H1792, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.340×** | -10.4 | 3e-23 | 28/32 (J82, H4, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.346×** | -10.2 | 2e-22 | 25/32 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.375×** | -9.4 | 3e-19 | 25/32 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.296×** | -8.9 | 2e-17 | 27/31 (RPMI-7951, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.426×** | -8.2 | 1e-14 | 24/32 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.362×** | -7.5 | 4e-12 | 18/28 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.228×** | -7.4 | 5e-12 | 23/31 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.446×** | -7.3 | 1e-11 | 22/32 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.442×** | -7.3 | 2e-11 | 17/23 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.483×** | -7.0 | 1e-10 | 24/32 (HEC-1-A, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.263×** | -6.7 | 6e-10 | 21/32 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.610×** | -4.7 | 5e-05 | 18/32 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.647×** | -4.2 | 6e-04 | 20/32 (SW 1271, SNU-423, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.562×** | -2.9 | 0.075 | 12/31 (NCI-H1792, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.811×** | -2.8 | 0.083 | 12/32 (HS-578T, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 54.7 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0592× (z -26.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0760× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 85.0 | 0 | 14 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0976× (z -13.8) |
| [[J82 (line)]] | alt | 30.7 | 0 | 13 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0232× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.121× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 58.1 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0645× (z -25.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.169× (z -11.9) |
| [[H4 (line)]] | wt | 46.3 | 0 | 10 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0228× (z -19.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0634× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 50.3 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0725× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0928× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0424× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.191× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 36.0 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0318× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0946× (z -12.9) |
| [[SNU-423 (line)]] | alt | 43.6 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0961× (z -20.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -10.2) |
| [[HOP62 (line)]] | alt | 30.2 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0140× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.104× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 42.4 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0572× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 13.3 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.112× (z -12.8) ⚠ cell-cycle shift, explains ~74% of this change |
| [[NCI-H1573 (line)]] | alt | 21.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -17.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -8.7) |
| [[A-172 (line)]] | wt | 40.1 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.59× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -14.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 11.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -13.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0575× (z -9.6) |
| [[C32 (line)]] | wt | 17.4 | 0 | 3 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.0314× (z -13.6) |
| [[PANC-1 (line)]] | alt | 6.25 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0836× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 7.76 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0499× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.123× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 7.31 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -12.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0464× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0843× (z -11.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OR9Q1]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[LUCAT1]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SPOCD1]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ZNF439]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ADAM12]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[DIRC3-AS1]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[APCDD1L-DT]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CFAP20DC]] | +0.51 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.51 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[EFCAB13]] | +0.50 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ARL10]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[NIM1K]] | +0.50 | +0.40 / +0.55 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR15L]] | -0.50 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[KCNE3]] | -0.50 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[PROM1]] | -0.50 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[MBOAT1]] | -0.50 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[LRP4]] | -0.49 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[FGFR2]] | -0.48 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[TGFBR3]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ABO]] | -0.47 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[GPX2]] | -0.47 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[SYK]] | -0.47 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[RORC]] | -0.46 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[PLEKHG6]] | -0.46 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 5, C 8. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00887]] | B | LINC00887 activity raises CLDN14-AS1's level | lines that do not express LINC00887 (8) vs lines expressing it (42) | 3.05× lower at baseline in the lines without LINC00887 | 0.070 | ⚠ within organs, on part of the lines; also absent: LINC02036, STAMBPL1, CFAP45; maybe low, not absent |
| [[LINC02253]] | B | LINC02253 activity lowers CLDN14-AS1's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 2.73× higher at baseline in the lines without LINC02253 | 0.074 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349 |
| [[EFEMP2]] | B | EFEMP2 activity raises CLDN14-AS1's level | lines that do not express EFEMP2 (6) vs lines expressing it (44) | 3.35× lower at baseline in the lines without EFEMP2 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000198106, ZMIZ1-AS1; maybe low, not absent |
| [[CNRIP1]] | B | CNRIP1 activity raises CLDN14-AS1's level | lines that do not express CNRIP1 (25) vs lines expressing it (25) | 2.93× lower at baseline in the lines without CNRIP1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[APH1B]] | B | APH1B activity raises CLDN14-AS1's level | lines that do not express APH1B (6) vs lines expressing it (44) | 3.65× lower at baseline in the lines without APH1B | 0.095 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |
| [[HRH1]] | C | HRH1 activity raises CLDN14-AS1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 4.68× lower at baseline in the lines without HRH1 | 0.009 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent; co-absent with the target |
| [[OR9Q1]] | C | OR9Q1 activity raises CLDN14-AS1's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 4.12× lower at baseline in the lines without OR9Q1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L; co-absent with the target |
| [[STAC]] | C | STAC activity raises CLDN14-AS1's level | lines that do not express STAC (25) vs lines expressing it (25) | 3.18× lower at baseline in the lines without STAC | 0.032 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11; co-absent with the target |
| [[TM4SF19-DYNLT2B]] | C | TM4SF19-DYNLT2B activity raises CLDN14-AS1's level | lines that do not express TM4SF19-DYNLT2B (20) vs lines expressing it (30) | 3.17× lower at baseline in the lines without TM4SF19-DYNLT2B | 0.035 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3; co-absent with the target |
| [[SETBP1]] | C | SETBP1 activity raises CLDN14-AS1's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.39× lower at baseline in the lines without SETBP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises CLDN14-AS1's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 3.50× lower at baseline in the lines without ADAM12 | 0.046 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[EHD2]] | C | EHD2 activity raises CLDN14-AS1's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 3.52× lower at baseline in the lines without EHD2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 16, C 7. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSANTD3]] | B | CLDN14-AS1 activity raises MSANTD3's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without CLDN14-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[MEAK7]] | B | CLDN14-AS1 activity raises MEAK7's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 2.02× lower at baseline in the lines without CLDN14-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[APH1B]] | B | CLDN14-AS1 activity raises APH1B's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 2.76× lower at baseline in the lines without CLDN14-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[ARHGAP22]] | B | CLDN14-AS1 activity raises ARHGAP22's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 3.72× lower at baseline in the lines without CLDN14-AS1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[CLDN14]] | B | CLDN14-AS1 activity raises CLDN14's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without CLDN14-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[KCTD11]] | B | CLDN14-AS1 activity raises KCTD11's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.46× lower at baseline in the lines without CLDN14-AS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[GPATCH2L]] | B | CLDN14-AS1 activity raises GPATCH2L's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without CLDN14-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[LUCAT1]] | B | CLDN14-AS1 activity raises LUCAT1's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 3.11× lower at baseline in the lines without CLDN14-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[TEX21P]] | B | CLDN14-AS1 activity raises TEX21P's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without CLDN14-AS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[CAVIN4]] | B | CLDN14-AS1 activity raises CAVIN4's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without CLDN14-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[PDLIM7]] | B | CLDN14-AS1 activity raises PDLIM7's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without CLDN14-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[LINC00887]] | B | CLDN14-AS1 activity raises LINC00887's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 2.02× lower at baseline in the lines without CLDN14-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.459). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.3, 22.4); signed map (29.8, 49.1). **Vector** length 89.5, 25.8% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | -1.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +2.0 | +0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.5 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.3 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | -7.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.1 | -5.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.1 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -2.6 |

## What is on record

> [!warning] No registry record
> CLDN14-AS1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 13925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13925); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13925]; `tensor/DDL_lfc|DDL_z.npy` [13925]; `embed/gene_vectors.npy` [13925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13925 or target_col == 13925). Every well: [[CLDN14-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN14-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
