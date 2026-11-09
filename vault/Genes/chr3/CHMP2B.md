---
symbol: "CHMP2B"
type: "gene"
col: 1388
ensembl_id: "ENSG00000083937"
name: "charged multivesicular body protein 2B"
location: "3p11.2"
module: 59
arm: "+"
pooled_cpm: 75.51
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# CHMP2B

*charged multivesicular body protein 2B* — 3p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +16.1, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.53× (z +11.1, q 4e-26, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.259×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB9A]] (+0.66, fdr 1e-05), [[PIGP]] (+0.64, fdr 7e-06), [[ABCA5]] (+0.63, fdr 1e-05); moves opposite to [[TOMM40]] (-0.66, fdr 7e-06), [[RNPS1]] (-0.64, fdr 7e-06), [[PCNX3]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CRB3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.59×** | +16.1 | 0e+00 | 45/48 (A-172, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.53×** | +11.1 | 4e-26 | 44/48 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +11.0 | 4e-26 | 47/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.28×** | +9.8 | 1e-20 | 44/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.14×** | +8.7 | 3e-16 | 42/48 (LoVo, COLO 205, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +7.7 | 9e-13 | 40/47 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.68×** | +6.2 | 4e-08 | 34/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.66×** | +6.1 | 9e-08 | 36/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +5.5 | 3e-06 | 36/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +5.1 | 2e-05 | 36/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +4.7 | 2e-04 | 33/49 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.5 | 4e-04 | 31/48 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.03×** | +4.4 | 5e-04 | 34/49 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.2 | 0.001 | 26/47 (NCI-H2030, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.37×** | +3.8 | 0.005 | 25/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.8 | 0.006 | 27/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.007 | 22/49 (J82, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.012 | 24/48 (J82, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.012 | 24/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.021 | 23/48 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.027 | 21/48 (NCI-H2347, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1388.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.259×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.762× | -3.2 | 0.68 | 22/48 (NCI-H1573, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.1 | 10 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +15.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.75× (z +13.2) | — |
| [[LoVo (line)]] | wt | 127 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +19.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.37× (z +16.8) | — |
| [[A549 (line)]] | wt | 66.7 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +15.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.73× (z +13.0) | — |
| [[NCI-H23 (line)]] | alt | 61.2 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +15.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.07× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 108 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1573 (line)]] | alt | 111 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +17.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.70× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 122 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +16.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 129 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 31.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 137 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +9.8) | — |
| [[A-172 (line)]] | wt | 51.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +22.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.66× (z +16.1) | — |
| [[A-427 (line)]] | wt | 31.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +13.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.15× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 63.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +13.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 65.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +15.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.52× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 62.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +16.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +8.7) | — |
| [[C32 (line)]] | wt | 60.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +12.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.47× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 79.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +13.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.29× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 42.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +12.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 157 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +12.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 49.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.52× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 191 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +9.1) | — |
| [[RKO (line)]] | wt | 78.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 68.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +16.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 60.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +8.6) | — |
| [[A498 (line)]] | wt | 79.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.3) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[CFPAC-1 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 42.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HS-578T (line)]] | alt | 81.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[J82 (line)]] | alt | 81.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +12.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 50.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.21× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 87.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SHP-77 (line)]] | alt | 40.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 80.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB9A]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[PIGP]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ABCA5]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[GPBP1]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[XPA]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[YTHDC1]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ZNF706]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MAP3K2-DT]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LINC01273]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[MIER1]] | +0.60 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[RPS27L]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 | pathway: SARS-CoV-1 Infection |
| [[BTG3]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM40]] | -0.66 | -0.61 / -0.59 | both halves | 7e-06 | pathway: Autophagy |
| [[RNPS1]] | -0.64 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[PCNX3]] | -0.64 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[RTEL1]] | -0.63 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.62 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[CHID1]] | -0.62 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[ATAD3A]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[TEX2]] | -0.61 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[POLE]] | -0.61 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ELAVL1]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SNRPA]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[CCAR2]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRB3]] | B | CRB3 activity raises CHMP2B's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 1.63× lower at baseline in the lines without CRB3 | 0.054 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1 |
| [[SNAP91]] | B | SNAP91 activity lowers CHMP2B's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 1.42× higher at baseline in the lines without SNAP91 | 0.092 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent |
| [[IL18]] | B | IL18 activity raises CHMP2B's level | lines that do not express IL18 (18) vs lines expressing it (32) | 1.41× lower at baseline in the lines without IL18 | 0.096 | ⚠ within organs, on part of the lines; also absent: LSR, SPINT2, LAMA3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.6, -29.1); signed map (-8.3, 2.7). **Vector** length 86.6, 27.6% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.7 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.8 | +16.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +1.9 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.0 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | +0.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.0 | +4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.7 | +6.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -2.6 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p11.2 — chr3:87,227,271-87,255,556 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564O123, CHMP2.5, VPS2B |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III |
| Reactome | 29 pathways, smallest: Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676; Pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQN3](https://www.uniprot.org/uniprotkb/Q9UQN3) (Charged multivesicular body protein 2b):

> Probable core component of the endosomal sorting required for transport complex III (ESCRT-III) which is involved in multivesicular bodies (MVBs) formation and sorting of endosomal cargo proteins into MVBs. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal enzymes and lipids. The …

**Summary**, from NCBI Gene [25978](https://www.ncbi.nlm.nih.gov/gene/25978):

> This gene encodes a component of the heteromeric ESCRT-III complex (Endosomal Sorting Complex Required for Transport III) that functions in the recycling or degradation of cell surface receptors. ESCRT-III functions in the concentration and invagination of ubiquitinated endosomal cargos into intralumenal vesicles. The protein encoded by this gene is found as a monomer in the cytosol or as an oligomer in ESCRT-III complexes on endosomal membranes. It is expressed in neurons of all major regions …

**Accessions** — [HGNC:24537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24537) · Entrez [25978](https://www.ncbi.nlm.nih.gov/gene/25978) · UniProt [Q9UQN3](https://www.uniprot.org/uniprotkb/Q9UQN3) · Ensembl [ENSG00000083937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083937)

## Data

Gene col 1388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1388); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1388]; `tensor/DDL_lfc|DDL_z.npy` [1388]; `embed/gene_vectors.npy` [1388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1388 or target_col == 1388). Every well: [[CHMP2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
