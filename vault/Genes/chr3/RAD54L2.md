---
symbol: "RAD54L2"
type: "gene"
col: 8859
ensembl_id: "ENSG00000164080"
name: "RAD54 like 2"
location: "3p21.2"
module: 1
arm: "+"
pooled_cpm: 54.27
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 20
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RAD54L2

*RAD54 like 2* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +17.6, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.620× (z -13.7, q 8e-40, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIS3L2]] (+0.71, fdr 7e-06), [[ACSF3]] (+0.68, fdr 7e-06), [[AGK]] (+0.66, fdr 7e-06); moves opposite to [[CSRP2]] (-0.64, fdr 1e-05), [[SAP30-DT]] (-0.62, fdr 1e-05), [[ADCY10]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +17.6 | 0e+00 | 41/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.56×** | +13.4 | 2e-38 | 47/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.97×** | +13.1 | 6e-37 | 43/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +11.3 | 2e-27 | 41/48 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.53×** | +9.8 | 1e-20 | 42/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +9.5 | 2e-19 | 37/48 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +9.0 | 2e-17 | 39/48 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +8.4 | 2e-15 | 32/48 (LS 180, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.49×** | +8.0 | 5e-14 | 35/48 (LS 180, SW1417, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +7.7 | 1e-12 | 34/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +7.5 | 3e-12 | 32/48 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +6.7 | 8e-10 | 35/48 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +6.7 | 8e-10 | 37/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +6.4 | 7e-09 | 31/48 (HEC-1-A, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.3 | 1e-08 | 31/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 4e-07 | 29/48 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8859.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -13.7 | 8e-40 | 39/48 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -7.5 | 2e-11 | 30/48 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -7.4 | 2e-11 | 36/49 (SNU-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.731×** | -6.3 | 3e-08 | 28/49 (RKO, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -5.4 | 1e-05 | 27/48 (LS 180, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -4.9 | 1e-04 | 15/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.782×** | -4.8 | 1e-04 | 25/44 (SHP-77, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.862× | -3.0 | 0.18 | 7/48 (KATO III, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 72.8 | 6 | 1 | [[Panobinostat (drug)]] 5 µM 2.33× (z +10.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -10.9) |
| [[SW480 (line)]] | alt | 90.1 | 7 | 0 | [[TAK-901 (drug)]] 5 µM 6.27× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +18.4) | — |
| [[SW1417 (line)]] | alt | 62.3 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +19.8) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.442× (z -12.5) |
| [[SW48 (line)]] | wt | 78.2 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -16.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 31.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 47.1 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.92× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.9) |
| [[LS 180 (line)]] | wt | 42.1 | 4 (1 ⚠) | 0 | [[Selinexor (drug)]] 0.05 µM 3.75× (z +12.6) | — |
| [[RKO (line)]] | wt | 90.6 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.05× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -21.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 37.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 37.5 | 3 | 0 | [[Selinexor (drug)]] 5 µM 2.21× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 72.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 64.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 58.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -12.3) |
| [[SW 900 (line)]] | alt | 50.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.9) |
| [[C-33 A (line)]] | alt | 75.8 | 2 | 0 | [[Selinexor (drug)]] 0.05 µM 2.95× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 48.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +14.3) | — |
| [[NCI-H2347 (line)]] | alt | 61.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -16.6) |
| [[PANC-1 (line)]] | alt | 40.5 | 2 | 0 | [[Selinexor (drug)]] 5 µM 2.05× (z +12.0) | — |
| [[SNU-1 (line)]] | wt | 73.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -10.4) |
| [[A-172 (line)]] | wt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.6) | — |
| [[A-427 (line)]] | wt | 74.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.421× (z -9.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 28.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.5) | — |
| [[A549 (line)]] | wt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 95.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -12.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 73.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 51.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 41.0 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.46× (z +11.7) | — |
| [[J82 (line)]] | alt | 59.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.0) |
| [[KATO III (line)]] | alt | 47.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.0) | — |
| [[LoVo (line)]] | wt | 59.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 41.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -13.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 55.9 | 1 | 0 | [[Selinexor (drug)]] 0.05 µM 2.90× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -18.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -8.8) |
| [[SNU-423 (line)]] | alt | 43.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -8.6) |
| [[CHP-212 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L2]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[ACSF3]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[AGK]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[YLPM1]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[COG2]] | +0.64 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[FKTN]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[ZNF839]] | +0.63 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[DNAJC14]] | +0.61 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[WDR70]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[WDR7]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[DRG2]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LCLAT1]] | +0.60 | +0.44 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP2]] | -0.64 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[SAP30-DT]] | -0.62 | -0.51 / -0.71 | both halves | 1e-05 |  |
| [[ADCY10]] | -0.59 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[GNAS]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[CXCR4]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[KDM3A]] | -0.53 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[NARF]] | -0.52 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[LEPR]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CD27-AS1]] | -0.52 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[ZBTB11]] | -0.52 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[ERO1B]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[HLA-F-AS1]] | -0.52 | -0.42 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RAD54L2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.0, -40.7); signed map (-9.1, -47.2). **Vector** length 102, 27.2% of its response variance represented; |z| ≥ 3 in 1,236 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.2 | +8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +13.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +13.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +5.2 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +9.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.7 | -13.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.9 | -3.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | RAD54 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,538,719-51,668,667 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0809, SRISNF2L, ARIP4 |
| Gene groups (HGNC) | SNF2 related family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4B4](https://www.uniprot.org/uniprotkb/Q9Y4B4) (Helicase ARIP4):

> Helicase that modulates androgen receptor (AR)-dependent transactivation in a promoter-dependent manner (By similarity). May stimulate the release of RNA polymerase II, that has paused near the transcription start sites of AR-targeted genes and unwind R-loops formed at these sites; R-loops result from the hybridization of the short RNA strand nascently synthesized by the paused RNA polymerase II molecule and the DNA template. May also stimulate double-strand break formation by TOP2B, which …

**Summary**, from NCBI Gene [23132](https://www.ncbi.nlm.nih.gov/gene/23132):

> Enables DNA/RNA helicase activity and ubiquitin protein ligase activity. Involved in R-loop processing and transcription elongation by RNA polymerase II. Located in chromatin. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29123) · Entrez [23132](https://www.ncbi.nlm.nih.gov/gene/23132) · UniProt [Q9Y4B4](https://www.uniprot.org/uniprotkb/Q9Y4B4) · Ensembl [ENSG00000164080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164080)

## Data

Gene col 8859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8859); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8859]; `tensor/DDL_lfc|DDL_z.npy` [8859]; `embed/gene_vectors.npy` [8859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8859 or target_col == 8859). Every well: [[RAD54L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD54L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
