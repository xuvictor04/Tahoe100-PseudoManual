---
symbol: "DIS3L2"
type: "gene"
col: 6890
ensembl_id: "ENSG00000144535"
name: "DIS3 like 3'-5' exoribonuclease 2"
location: "2q37.1"
module: 4
arm: "+"
pooled_cpm: 99.76
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DIS3L2

*DIS3 like 3'-5' exoribonuclease 2* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.25× (z +6.5, q 3e-08, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.608× (z -10.9, q 7e-25, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHCHD6]] (+0.76, fdr 7e-06), [[DDX10]] (+0.76, fdr 7e-06), [[DPH6]] (+0.75, fdr 7e-06); moves opposite to [[FAM117A]] (-0.71, fdr 7e-06), [[ERO1B]] (-0.66, fdr 7e-06), [[CSRP2]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +6.5 | 3e-08 | 36/49 (MIA PaCa-2, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.022 | 33/47 (SW1417, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.022 | 26/48 (BT-474, NCI-H2347, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.022 | 24/48 (LS 180, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +3.3 | 0.10 | 19/48 (AsPC-1, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | 1.23× | +3.3 | 0.11 | 25/48 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -10.9 | 7e-25 | 43/49 (CHP-212, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.502×** | -10.7 | 4e-24 | 41/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.520×** | -10.1 | 8e-22 | 46/48 (SW480, RKO, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.560×** | -9.0 | 4e-17 | 39/48 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.720×** | -7.2 | 7e-11 | 29/48 (NCI-H1792, J82, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.637×** | -6.5 | 8e-09 | 29/44 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.652×** | -6.1 | 6e-08 | 36/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.704×** | -5.4 | 4e-06 | 31/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.696×** | -5.2 | 1e-05 | 33/47 (SW1417, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.704×** | -5.0 | 3e-05 | 30/48 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.707×** | -5.0 | 3e-05 | 25/45 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -4.8 | 9e-05 | 29/50 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.746×** | -4.5 | 3e-04 | 29/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.664×** | -4.5 | 3e-04 | 33/49 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -3.9 | 0.003 | 28/48 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 128 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -15.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 134 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -15.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 113 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -17.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -11.1) |
| [[RKO (line)]] | wt | 109 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.3) |
| [[BT-474 (line)]] | alt | 75.3 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 78.1 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -12.5) |
| [[J82 (line)]] | alt | 56.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -14.0) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -10.8) |
| [[LoVo (line)]] | wt | 113 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -13.2) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.418× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 139 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.72× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.409× (z -10.8) |
| [[SW1417 (line)]] | alt | 132 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.353× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.306× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 82.2 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.385× (z -9.2) |
| [[KATO III (line)]] | alt | 101 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.308× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 119 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 226 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0649× (z -30.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 151 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -11.6) |
| [[SW48 (line)]] | wt | 106 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -9.1) |
| [[A-427 (line)]] | wt | 132 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.337× (z -12.9) |
| [[A549 (line)]] | wt | 115 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.9) |
| [[LS 180 (line)]] | wt | 88.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.255× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.0) |
| [[SNU-423 (line)]] | alt | 66.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.6) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.8) |
| [[SW 900 (line)]] | alt | 74.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -11.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 67.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -12.8) |
| [[AN3 CA (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0946× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 59.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.2) ⚠ cell-cycle shift, explains ~89% of this change |
| [[CHP-212 (line)]] | wt | 94.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -15.5) |
| [[HCT15 (line)]] | alt | 98.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.281× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 98.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -9.4) |
| [[Hs 766T (line)]] | wt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 73.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 64.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.2) ⚠ cell-cycle shift, explains ~89% of this change |
| [[NCI-H1792 (line)]] | alt | 92.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -15.1) ⚠ cell-cycle shift, explains ~89% of this change |
| [[NCI-H2030 (line)]] | alt | 93.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.2) |
| [[SNU-1 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 139 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 96.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHCHD6]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[DDX10]] | +0.76 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[DPH6]] | +0.75 | +0.65 / +0.81 | both halves | 7e-06 | same gene group |
| [[NOL10]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 | STRING 536 |
| [[MRPS27]] | +0.74 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[LCLAT1]] | +0.74 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[LSG1]] | +0.74 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[COA1]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[YLPM1]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[RAD54L2]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[BYSL]] | +0.71 | +0.74 / +0.71 | both halves | 7e-06 | STRING 496 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.71 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[ERO1B]] | -0.66 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[CSRP2]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.62 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[INTS6L]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[LASP1]] | -0.60 | -0.58 / -0.56 | both halves | 1e-05 | same gene group |
| [[GNAS]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DIS3L2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.3, -35.1); signed map (-9.9, -48.7). **Vector** length 115, 39.0% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.52 to 8); *tRNA processing* (reactome, mean cos +0.52 to 10); *Processing of Capped Intron-Containing Pre-mRNA* (reactome, mean cos +0.51 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.5 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.5 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.6 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.9 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.7 | -10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.5 | -2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -9.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.8 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | DIS3 like 3'-5' exoribonuclease 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:231,961,245-232,344,350 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36974, MGC42174; previously FAM6A |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Z-decay: degradation of maternal mRNAs by zygotically expressed factors; Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYB7](https://www.uniprot.org/uniprotkb/Q8IYB7) (DIS3-like exonuclease 2):

> 3'-5'-exoribonuclease that specifically recognizes RNAs polyuridylated at their 3' end and mediates their degradation. Component of an exosome-independent RNA degradation pathway that mediates degradation of both mRNAs and miRNAs that have been polyuridylated by a terminal uridylyltransferase, such as ZCCHC11/TUT4. Mediates degradation of cytoplasmic mRNAs that have been deadenylated and subsequently uridylated at their 3'. Mediates degradation of uridylated pre-let-7 miRNAs, contributing to …

**Summary**, from NCBI Gene [129563](https://www.ncbi.nlm.nih.gov/gene/129563):

> The protein encoded by this gene is similar in sequence to 3'/5' exonucleolytic subunits of the RNA exosome. The exosome is a large multimeric ribonucleotide complex responsible for degrading various RNA substrates. Several transcript variants, some protein-coding and some not, have been found for this gene. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:28648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28648) · Entrez [129563](https://www.ncbi.nlm.nih.gov/gene/129563) · UniProt [Q8IYB7](https://www.uniprot.org/uniprotkb/Q8IYB7) · Ensembl [ENSG00000144535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144535)

## Data

Gene col 6890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6890); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6890]; `tensor/DDL_lfc|DDL_z.npy` [6890]; `embed/gene_vectors.npy` [6890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6890 or target_col == 6890). Every well: [[DIS3L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIS3L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
