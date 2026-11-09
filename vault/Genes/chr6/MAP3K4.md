---
symbol: "MAP3K4"
type: "gene"
col: 1430
ensembl_id: "ENSG00000085511"
name: "mitogen-activated protein kinase kinase kinase 4"
location: "6q26"
module: 4
arm: "+"
pooled_cpm: 94.58
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MAP3K4

*mitogen-activated protein kinase kinase kinase 4* — 6q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.56× (z +8.3, q 5e-14, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -14.6, q 1e-45, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THEM6]] (+0.57, fdr 9e-05), [[MRTFB]] (+0.57, fdr 3e-05), [[PDHB]] (+0.57, fdr 2e-05); moves opposite to [[LINC01772]] (-0.57, fdr 2e-05), [[MAP1LC3B]] (-0.57, fdr 2e-05), [[TRNAU1AP]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.56×** | +8.3 | 5e-14 | 40/49 (CFPAC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.18×** | +6.9 | 2e-09 | 35/48 (C32, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 2e-06 | 35/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.1 | 5e-05 | 27/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.2 | 0.003 | 24/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.011 | 25/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.015 | 24/48 (PANC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.057 | 10/48 (C32, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1430.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -14.6 | 1e-45 | 46/49 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.438×** | -14.0 | 5e-42 | 45/48 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.430×** | -13.7 | 1e-40 | 43/44 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.580×** | -9.2 | 5e-18 | 39/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.612×** | -8.0 | 2e-13 | 43/48 (hTERT-HPNE, C32, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -7.1 | 1e-10 | 42/50 (SK-MEL-2, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.669×** | -6.5 | 5e-09 | 38/47 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.728×** | -5.4 | 5e-06 | 35/48 (hTERT-HPNE, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.728×** | -5.0 | 4e-05 | 25/45 (A-427, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.755×** | -4.8 | 1e-04 | 28/48 (NCI-H1573, SW 900, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.790×** | -4.0 | 0.003 | 25/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.063 | 19/49 (SW1417, HEC-1-A, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.741×** | -3.1 | 0.095 | 17/47 (SW48, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 100 | 1 | 9 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 7.19× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -22.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -16.1) |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -16.9) |
| [[PANC-1 (line)]] | alt | 126 | 5 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +22.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.63× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -12.0) |
| [[HOP62 (line)]] | alt | 120 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.9) |
| [[A498 (line)]] | wt | 54.1 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +22.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.48× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 89.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -15.3) |
| [[A549 (line)]] | wt | 89.9 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -15.1) |
| [[AN3 CA (line)]] | alt | 142 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.263× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 88.8 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.04× (z +11.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 151 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 117 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.1) |
| [[A-172 (line)]] | wt | 115 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -18.4) |
| [[A-427 (line)]] | wt | 147 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0932× (z -26.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 70.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +32.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.9× (z +13.3) | — |
| [[HS-578T (line)]] | alt | 76.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 78.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +25.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.25× (z +12.9) | — |
| [[SW 900 (line)]] | alt | 153 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -14.6) |
| [[SW48 (line)]] | wt | 133 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.48× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -16.4) |
| [[SW480 (line)]] | alt | 79.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 135 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -12.6) |
| [[C-33 A (line)]] | alt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -14.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 83.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 63.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 47.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -8.6) |
| [[SNU-1 (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -14.5) |
| [[KATO III (line)]] | alt | 77.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 92.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.447× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 82.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -9.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 114 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 73.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.401× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 57.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -17.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -13.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -11.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -9.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 88.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 86.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | +0.57 | +0.37 / +0.49 | both halves | 9e-05 |  |
| [[MRTFB]] | +0.57 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[PDHB]] | +0.57 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[TUBGCP3]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SSX2IP]] | +0.56 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[TRERF1]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[LRIG3]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[VWA8]] | +0.55 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[RNFT2]] | +0.55 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[HEATR3]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[EHMT2]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[MRPL19]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01772]] | -0.57 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MAP1LC3B]] | -0.57 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TRNAU1AP]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MON1B]] | -0.54 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[C14orf28]] | -0.54 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ZNF547]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[NUDT16-DT]] | -0.51 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[NOXRED1]] | -0.51 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[RECQL5]] | -0.50 | -0.49 / -0.50 | both halves | 2e-05 |  |
| [[NRSN2-AS1]] | -0.50 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[ATXN1L]] | -0.50 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[USP34-DT]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MAP3K4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAGI1]] | C | MAGI1 activity raises MAP3K4's level | lines that do not express MAGI1 (3) vs lines expressing it (47) | 1.76× lower at baseline in the lines without MAGI1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PXYLP1, YPEL2, TMEM229B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (19.8, -6.9); signed map (-13.7, -50.3). **Vector** length 86.0, 22.9% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +8.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +6.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | +0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -8.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | +2.1 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q26 — chr6:160,991,727-161,117,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTK1, MAPKKK4, KIAA0213; previously MEKK4 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; STE11 kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6R4](https://www.uniprot.org/uniprotkb/Q9Y6R4) (Mitogen-activated protein kinase kinase kinase 4):

> Component of a protein kinase signal transduction cascade. Activates the CSBP2, P38 and JNK MAPK pathways, but not the ERK pathway. Specifically phosphorylates and activates MAP2K4 and MAP2K6.

**Summary**, from NCBI Gene [4216](https://www.ncbi.nlm.nih.gov/gene/4216):

> The central core of each mitogen-activated protein kinase (MAPK) pathway is a conserved cascade of 3 protein kinases: an activated MAPK kinase kinase (MAPKKK) phosphorylates and activates a specific MAPK kinase (MAPKK), which then activates a specific MAPK. While the ERK MAPKs are activated by mitogenic stimulation, the CSBP2 and JNK MAPKs are activated by environmental stresses such as osmotic shock, UV irradiation, wound stress, and inflammatory factors. This gene encodes a MAPKKK, the MEKK4 …

**Accessions** — [HGNC:6856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6856) · Entrez [4216](https://www.ncbi.nlm.nih.gov/gene/4216) · UniProt [Q9Y6R4](https://www.uniprot.org/uniprotkb/Q9Y6R4) · Ensembl [ENSG00000085511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085511)

## Data

Gene col 1430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1430); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1430]; `tensor/DDL_lfc|DDL_z.npy` [1430]; `embed/gene_vectors.npy` [1430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1430 or target_col == 1430). Every well: [[MAP3K4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
