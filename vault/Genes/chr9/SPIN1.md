---
symbol: "SPIN1"
type: "gene"
col: 2800
ensembl_id: "ENSG00000106723"
name: "spindlin 1"
location: "9q22.1"
module: 17
arm: "+"
pooled_cpm: 112.5
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SPIN1

*spindlin 1* — 9q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.41× (z +4.6, q 0.003, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 0.05 µM in 3 lines (SW48 2.73×, C32 2.32×, BT-474 2.13×); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 2.44×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 5.73×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.399× (z -32.6, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGPS]] (+0.66, fdr 7e-06), [[DLD]] (+0.65, fdr 7e-06), [[EHMT2]] (+0.64, fdr 1e-05); moves opposite to [[TTLL3]] (-0.55, fdr 3e-05), [[DHX32]] (-0.53, fdr 3e-05), [[C16orf46]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF618]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2800.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 0.05 µM in 3 lines (SW48 2.73×, C32 2.32×, BT-474 2.13×); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 2.44×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 5.73×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +4.6 | 0.003 | 26/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +4.0 | 0.012 | 21/47 (SK-MEL-2, SNU-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.012 | 26/50 (H4, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 1.12× | +3.9 | 0.014 | 1/48 (SNU-423) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.16× | +3.5 | 0.054 | 14/50 (HEC-1-A, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.054 | 15/48 (SK-MEL-2, RKO, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.4 | 0.057 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.064 | 6/48 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.076 | 14/48 (HEC-1-A, RKO, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.399×** | -32.6 | 0e+00 | 46/49 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.525×** | -22.8 | 0e+00 | 40/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.535×** | -15.1 | 0e+00 | 42/48 (C32, H4, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.601×** | -12.3 | 2e-32 | 41/50 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.646×** | -11.0 | 7e-26 | 45/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.649×** | -10.8 | 2e-25 | 46/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.652×** | -10.7 | 6e-25 | 43/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.665×** | -10.2 | 1e-22 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.666×** | -10.2 | 1e-22 | 43/48 (BT-474, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.678×** | -9.4 | 4e-19 | 37/47 (SW1417, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.699×** | -9.0 | 1e-17 | 37/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.744×** | -7.4 | 6e-12 | 36/48 (BT-474, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.750×** | -7.2 | 3e-11 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -6.4 | 8e-09 | 22/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.782×** | -6.1 | 3e-08 | 29/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.755×** | -3.7 | 0.006 | 19/48 (HOP62, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.873× | -3.4 | 0.018 | 16/48 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.886× | -3.0 | 0.063 | 16/48 (SW 1271, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 103 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -28.0) |
| [[PANC-1 (line)]] | alt | 106 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -23.4) |
| [[C32 (line)]] | wt | 94.3 | 3 | 5 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.73× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -19.2) |
| [[HOP62 (line)]] | alt | 104 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -20.2) |
| [[LOX-IMVI (line)]] | wt | 123 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -25.6) |
| [[MIA PaCa-2 (line)]] | alt | 133 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -19.0) |
| [[RKO (line)]] | wt | 138 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -17.9) |
| [[A-172 (line)]] | wt | 171 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -21.2) |
| [[J82 (line)]] | alt | 168 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -18.2) |
| [[A498 (line)]] | wt | 159 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -19.9) |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -25.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -20.0) |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -18.9) |
| [[SW1417 (line)]] | alt | 155 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -19.2) |
| [[AsPC-1 (line)]] | alt | 104 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -20.2) |
| [[Hs 766T (line)]] | wt | 94.7 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -21.0) |
| [[SNU-1 (line)]] | wt | 95.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.8) |
| [[SW 900 (line)]] | alt | 98.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -21.1) |
| [[SW48 (line)]] | wt | 130 | 1 | 3 | [[TAK-901 (drug)]] 0.05 µM 2.73× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -14.6) |
| [[A-427 (line)]] | wt | 94.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 112 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.13× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -14.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 68.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -15.9) |
| [[NCI-H1792 (line)]] | alt | 89.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -21.6) |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -16.6) |
| [[RPMI-7951 (line)]] | alt | 92.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.7) |
| [[SNU-423 (line)]] | alt | 127 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -18.5) |
| [[SW480 (line)]] | alt | 110 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -18.1) |
| [[C-33 A (line)]] | alt | 180 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 67.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -15.0) |
| [[H4 (line)]] | wt | 115 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -17.0) |
| [[HS-578T (line)]] | alt | 93.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -23.0) |
| [[HT-29 (line)]] | alt | 80.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -12.8) |
| [[LoVo (line)]] | wt | 93.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -16.9) |
| [[LS 180 (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -21.6) |
| [[SK-MEL-2 (line)]] | alt | 93.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.44× (z +10.3) | — |
| [[A549 (line)]] | wt | 99.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -16.7) |
| [[AN3 CA (line)]] | alt | 168 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -13.0) |
| [[COLO 205 (line)]] | alt | 75.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -14.6) |
| [[HCT15 (line)]] | alt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 94.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 83.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -12.3) |
| [[KATO III (line)]] | alt | 81.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -9.3) |
| [[SHP-77 (line)]] | alt | 99.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -10.9) |
| [[CHP-212 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 189 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPS]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[DLD]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[EHMT2]] | +0.64 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[FAM98B]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[DHX9]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[QDPR]] | +0.61 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[FECH]] | +0.61 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ZDHHC21]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[RAD23B]] | +0.59 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SMG7]] | +0.59 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SSX2IP]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[CDC73]] | +0.58 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL3]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[DHX32]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[C16orf46]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[SPRED3]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[INTS6L]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[FAM120B]] | -0.52 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[TUT7]] | -0.52 | -0.61 / -0.40 | both halves | 4e-05 |  |
| [[SLC30A7]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[POLR2J4]] | -0.51 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[GAN]] | -0.51 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[HIC2]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | ZNF618 activity raises SPIN1's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without ZNF618 | 0.008 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[TOP2A]] | B | TOP2A activity raises SPIN1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.8, -15.9); signed map (-16.8, -43.0). **Vector** length 110, 33.1% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +5.5 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.9 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.9 | +3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.7 | +3.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.3 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.0 | -10.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -7.0 | -10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -32.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.0 | -12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -6.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | spindlin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.1 — chr9:88,388,430-88,478,694 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TDRD24; previously SPIN |
| Gene groups (HGNC) | Tudor domain containing; Spindlin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y657](https://www.uniprot.org/uniprotkb/Q9Y657) (Spindlin-1):

> Chromatin reader that specifically recognizes and binds histone H3 both trimethylated at 'Lys-4' and 'Lys-9' (H3K4me3K9me3) and is involved in piRNA-mediated retrotransposon silencing during spermatogenesis. Plays a key role in the initiation of the PIWIL4-piRNA pathway, a pathway that directs transposon DNA methylation and silencing in the male embryonic germ cells, by promoting recruitment of DNA methylation machinery to transposons: binds young, but not old, LINE1 transposons, which are …

**Summary**, from NCBI Gene [10927](https://www.ncbi.nlm.nih.gov/gene/10927):

> Enables histone H3K4me3 reader activity. Involved in positive regulation of DNA-templated transcription; positive regulation of Wnt signaling pathway; and rRNA transcription. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11243) · Entrez [10927](https://www.ncbi.nlm.nih.gov/gene/10927) · UniProt [Q9Y657](https://www.uniprot.org/uniprotkb/Q9Y657) · Ensembl [ENSG00000106723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106723)

## Data

Gene col 2800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2800); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2800]; `tensor/DDL_lfc|DDL_z.npy` [2800]; `embed/gene_vectors.npy` [2800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2800 or target_col == 2800). Every well: [[SPIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
