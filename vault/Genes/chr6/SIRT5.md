---
symbol: "SIRT5"
type: "gene"
col: 4536
ensembl_id: "ENSG00000124523"
name: "sirtuin 5"
location: "6p23"
module: 10
arm: "+"
pooled_cpm: 16.58
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SIRT5

*sirtuin 5* — 6p23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.75× (z +7.3, q 1e-10, up in 18 of 28 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.73×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.279× (z -24.5, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF514]] (+0.65, fdr 1e-05), [[CARF]] (+0.61, fdr 4e-05), [[TXNRD3]] (+0.60, fdr 1e-05); moves opposite to [[ENO2]] (-0.56, fdr 4e-05), [[MAP3K9]] (-0.54, fdr 5e-05), [[NOSIP]] (-0.51, fdr 7e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC00886]] → it (grade B ⚠); 7 go from it, the strongest it → [[GABPB2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4536.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.73×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +7.3 | 1e-10 | 18/28 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.3 | 3e-05 | 22/40 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.5 | 0.001 | 17/34 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.26 | 10/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Omeprazole (drug)]] 5 µM |  | 1.25× | +3.0 | 0.26 | 6/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4536.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.279×** | -24.5 | 0e+00 | 45/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.243×** | -19.2 | 0e+00 | 47/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.301×** | -16.3 | 0e+00 | 39/46 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.325×** | -15.3 | 0e+00 | 43/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.373×** | -13.4 | 6e-39 | 41/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.378×** | -13.2 | 5e-38 | 35/45 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.365×** | -13.2 | 1e-37 | 41/46 (J82, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.427×** | -11.6 | 5e-29 | 38/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.440×** | -11.2 | 4e-27 | 39/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.474×** | -10.1 | 2e-22 | 37/47 (J82, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.505×** | -9.3 | 9e-19 | 34/48 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.508×** | -9.2 | 2e-18 | 29/47 (PANC-1, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.278×** | -9.1 | 5e-18 | 38/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.305×** | -8.4 | 1e-15 | 34/43 (LOX-IMVI, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.548×** | -8.2 | 1e-14 | 34/47 (BT-474, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.611×** | -6.3 | 9e-09 | 28/47 (KATO III, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.638×** | -6.1 | 4e-08 | 26/45 (SNU-423, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.649×** | -4.9 | 3e-05 | 17/48 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.745×** | -4.0 | 0.002 | 14/48 (NCI-H2030, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.663×** | -4.0 | 0.002 | 16/48 (SW 1271, J82, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 24.5 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0227× (z -28.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.217× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -17.4) |
| [[PANC-1 (line)]] | alt | 26.2 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -21.3) |
| [[SW480 (line)]] | alt | 17.7 | 0 | 9 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0823× (z -19.8) |
| [[NCI-H23 (line)]] | alt | 30.4 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0238× (z -26.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0990× (z -16.4) |
| [[A-427 (line)]] | wt | 22.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.4) |
| [[KATO III (line)]] | alt | 29.9 | 0 | 7 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.192× (z -12.3) |
| [[LoVo (line)]] | wt | 16.5 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0879× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0600× (z -16.9) |
| [[MIA PaCa-2 (line)]] | alt | 30.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -23.1) |
| [[HEC-1-A (line)]] | alt | 20.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.6) |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -14.0) |
| [[A-172 (line)]] | wt | 15.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.1) |
| [[H4 (line)]] | wt | 17.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0559× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -12.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.1) |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -15.1) |
| [[A549 (line)]] | wt | 13.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 9.84 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0690× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.275× (z -8.5) |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0676× (z -13.9) |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.226× (z -9.2) |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0895× (z -11.8) |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 9.94 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -14.0) |
| [[A498 (line)]] | wt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.1) |
| [[C-33 A (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0782× (z -12.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.8) |
| [[HCT15 (line)]] | alt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -10.1) |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -9.5) |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.122× (z -10.3) |
| [[RKO (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 6.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -9.8) |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -9.6) |
| [[SW48 (line)]] | wt | 9.68 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0463× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF514]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CARF]] | +0.61 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[TXNRD3]] | +0.60 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ARPIN]] | +0.58 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TMEM9B-AS1]] | +0.58 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ARSD]] | +0.58 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[HENMT1]] | +0.57 | +0.47 / +0.31 | both halves | 2e-04 |  |
| [[HDHD2]] | +0.57 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[CYP4V2]] | +0.56 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[BICRAL]] | +0.56 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[TRIM66]] | +0.56 | +0.60 / +0.36 | both halves | 9e-05 |  |
| [[SP2-AS1]] | +0.56 | +0.59 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENO2]] | -0.56 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[MAP3K9]] | -0.54 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[NOSIP]] | -0.51 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[ALDOC]] | -0.51 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[RAB3A]] | -0.51 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[ABCB9]] | -0.50 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[ZNF511]] | -0.50 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[CIB1]] | -0.50 | -0.47 / -0.22 | both halves | 6e-04 |  |
| [[POLR2J]] ⚠ | -0.50 | -0.42 / -0.30 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC26A6]] | -0.49 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[RRBP1]] | -0.48 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.48 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[GRIN2D]] | -0.47 | -0.36 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00886]] | B | LINC00886 activity raises SIRT5's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 1.25× lower at baseline in the lines without LINC00886 | 0.093 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |
| [[RAB3A]] | C | RAB3A's natural level weakens SIRT5's drug response | RAB3A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.74, reverse -0.07; direction clear | 0.003 | ⚠ tissue can mimic it; precision caveat |
| [[GABPB2]] | C | GABPB2's natural level strengthens SIRT5's drug response | GABPB2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.66; direction not clear | 0.047 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TASOR]] | C | TASOR's natural level strengthens SIRT5's drug response | TASOR's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.52; direction not clear | 0.047 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABPB2]] | C | SIRT5's natural level strengthens GABPB2's drug response | SIRT5's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.66; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[WDR31]] | C | SIRT5's natural level strengthens WDR31's drug response | SIRT5's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.49; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | SIRT5's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | SIRT5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.019 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Nimesulide (drug)]] 5 µM | C | SIRT5's natural level raises the cells' numbers under Nimesulide 5 µM (protects the cells) | SIRT5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.323 over the table, 0.074 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Futibatinib (drug)]] 0.05 µM | C | SIRT5's natural level lowers the cells' numbers under Futibatinib 0.05 µM (makes them more sensitive) | SIRT5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.339 over the table, 0.058 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | SIRT5's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | SIRT5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.457 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | SIRT5's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | SIRT5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.465 over the table, 0.072 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.1, 21.0); signed map (29.2, -30.3). **Vector** length 52.8, 9.11% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.0 | -0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.8 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -24.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.4 | -11.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.3 | -10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -4.0 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | sirtuin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p23 — chr6:13,574,227-13,615,158 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sirtuins |
| Reactome | 5 pathways, smallest: Urea cycle; Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXA8](https://www.uniprot.org/uniprotkb/Q9NXA8) (NAD-dependent protein deacylase sirtuin-5, mitochondrial):

> NAD-dependent lysine demalonylase, desuccinylase and deglutarylase that specifically removes malonyl, succinyl and glutaryl groups on target proteins. Activates CPS1 and contributes to the regulation of blood ammonia levels during prolonged fasting: acts by mediating desuccinylation and deglutarylation of CPS1, thereby increasing CPS1 activity in response to elevated NAD levels during fasting. Activates SOD1 by mediating its desuccinylation, leading to reduced reactive oxygen species. Activates …

**Summary**, from NCBI Gene [23408](https://www.ncbi.nlm.nih.gov/gene/23408):

> This gene encodes a member of the sirtuin family of proteins, homologs to the yeast Sir2 protein. Members of the sirtuin family are characterized by a sirtuin core domain and grouped into four classes. The functions of human sirtuins have not yet been determined; however, yeast sirtuin proteins are known to regulate epigenetic gene silencing and suppress recombination of rDNA. Studies suggest that the human sirtuins may function as intracellular regulatory proteins with …

**Accessions** — [HGNC:14933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14933) · Entrez [23408](https://www.ncbi.nlm.nih.gov/gene/23408) · UniProt [Q9NXA8](https://www.uniprot.org/uniprotkb/Q9NXA8) · Ensembl [ENSG00000124523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124523)

## Data

Gene col 4536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4536); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4536]; `tensor/DDL_lfc|DDL_z.npy` [4536]; `embed/gene_vectors.npy` [4536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4536 or target_col == 4536). Every well: [[SIRT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIRT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
