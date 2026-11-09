---
symbol: "DR1"
type: "gene"
col: 3918
ensembl_id: "ENSG00000117505"
name: "down-regulator of transcription 1"
location: "1p22.1"
module: 25
arm: "+"
pooled_cpm: 57.88
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# DR1

*down-regulator of transcription 1* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (22 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.60× (z +15.1, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.683× (z -5.2, q 1e-04, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERLIN2]] (+0.75, fdr 7e-06), [[MOB1A]] (+0.72, fdr 1e-05), [[TWF1]] (+0.69, fdr 1e-05); moves opposite to [[SNHG6]] (-0.70, fdr 1e-05), [[SNHG7]] (-0.70, fdr 1e-05), [[RPP21]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 25 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.60×** | +15.1 | 0e+00 | 46/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +14.7 | 0e+00 | 38/44 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.66×** | +13.5 | 3e-39 | 41/48 (PANC-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +12.0 | 3e-31 | 40/48 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.77×** | +10.7 | 8e-25 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.60×** | +8.9 | 7e-17 | 35/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +8.3 | 1e-14 | 39/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.54×** | +8.1 | 3e-14 | 37/49 (C32, A549, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +8.0 | 7e-14 | 43/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +7.8 | 4e-13 | 40/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.51×** | +7.5 | 3e-12 | 27/43 (NCI-H460, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.47×** | +7.0 | 1e-10 | 37/48 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +6.9 | 2e-10 | 27/36 (NCI-H1573, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.44×** | +6.6 | 1e-09 | 31/48 (NCI-H460, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.38×** | +6.0 | 6e-08 | 35/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.6 | 1e-04 | 20/48 (SW1417, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.4 | 3e-04 | 22/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.003 | 22/48 (SW480, SNU-423, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.023 | 13/48 (SW 1088, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.042 | 13/48 (CFPAC-1, HOP62, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.683×** | -5.2 | 1e-04 | 30/48 (SNU-1, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.769×** | -3.6 | 0.065 | 17/48 (HT-29, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.830×** | -3.6 | 0.065 | 18/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.835× | -3.5 | 0.076 | 10/48 (HS-578T, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.8 | 9 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.25× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.11× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 42.7 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +16.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.32× (z +10.7) | — |
| [[C32 (line)]] | wt | 44.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.57× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 9.83× (z +9.4) | — |
| [[A549 (line)]] | wt | 37.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[LoVo (line)]] | wt | 66.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.74× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.94× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 60.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.51× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 46.4 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +12.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.10× (z +8.8) | — |
| [[RKO (line)]] | wt | 99.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +15.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.68× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 60.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.46× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 68.8 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.79× (z +9.6) | — |
| [[SW480 (line)]] | alt | 71.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.66× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.25× (z +12.1) | — |
| [[A498 (line)]] | wt | 62.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 63.1 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.71× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 76.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 62.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.96× (z +9.0) | — |
| [[SW48 (line)]] | wt | 63.9 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.36× (z +10.2) | — |
| [[A-172 (line)]] | wt | 35.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 43.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.71× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 75.0 | 0 | 1 | — | [[AT7519 (drug)]] 5 µM 0.0646× (z -8.5) |
| [[HCT15 (line)]] | alt | 77.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.76× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 68.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.6) | — |
| [[J82 (line)]] | alt | 64.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 43.7 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +9.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 86.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.62× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.51× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 69.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.26× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 84.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW 1271 (line)]] | alt | 57.4 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0576× (z -9.8) |
| [[SW1417 (line)]] | alt | 49.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERLIN2]] | +0.75 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.72 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[TWF1]] | +0.69 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[ALG10B]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SF3B4]] | +0.67 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.67 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[ZMPSTE24]] | +0.66 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[BTBD1]] | +0.66 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[GPAA1]] | +0.66 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[TMEM30A]] | +0.66 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[FH]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[EIF4G2]] | +0.65 | +0.51 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG6]] | -0.70 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.70 | -0.51 / -0.71 | both halves | 1e-05 |  |
| [[RPP21]] | -0.69 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | -0.68 | -0.49 / -0.74 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.68 | -0.48 / -0.70 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.67 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.67 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[MAP2K7]] | -0.67 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[GOLGA6L9]] | -0.66 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[NACA4P]] ⚠ | -0.65 | -0.49 / -0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.65 | -0.42 / -0.70 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF10]] | -0.64 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[SNHG12]] | -0.64 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[C19orf81]] | -0.63 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[PIAS4]] | -0.63 | -0.52 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.7, -21.7); signed map (-17.7, -38.0). **Vector** length 95.7, 26.1% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +7.1 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +6.9 | +8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +15.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +7.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +1.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.9 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.1 | -5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.1 | -1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.3 | -3.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | down-regulator of transcription 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:93,345,907-93,369,493 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NC2-BETA, NC2B, NCB2 |
| Gene groups (HGNC) | ATAC complex |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01658](https://www.uniprot.org/uniprotkb/Q01658) (Protein Dr1):

> The association of the DR1/DRAP1 heterodimer with TBP results in a functional repression of both activated and basal transcription of class II genes. This interaction precludes the formation of a transcription-competent complex by inhibiting the association of TFIIA and/or TFIIB with TBP. Can bind to DNA on its own. Component of the ATAC complex, a complex with histone acetyltransferase activity on histones H3 and H4.

**Summary**, from NCBI Gene [1810](https://www.ncbi.nlm.nih.gov/gene/1810):

> This gene encodes a TBP- (TATA box-binding protein) associated phosphoprotein that represses both basal and activated levels of transcription. The encoded protein is phosphorylated in vivo and this phosphorylation affects its interaction with TBP. This protein contains a histone fold motif at the amino terminus, a TBP-binding domain, and a glutamine- and alanine-rich region. The binding of DR1 repressor complexes to TBP-promoter complexes may establish a mechanism in which an altered DNA …

**Accessions** — [HGNC:3017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3017) · Entrez [1810](https://www.ncbi.nlm.nih.gov/gene/1810) · UniProt [Q01658](https://www.uniprot.org/uniprotkb/Q01658) · Ensembl [ENSG00000117505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117505)

## Data

Gene col 3918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3918); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3918]; `tensor/DDL_lfc|DDL_z.npy` [3918]; `embed/gene_vectors.npy` [3918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3918 or target_col == 3918). Every well: [[DR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
