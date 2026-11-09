---
symbol: "ERF"
type: "gene"
col: 2654
ensembl_id: "ENSG00000105722"
name: "ETS2 repressor factor"
location: "19q13.2"
module: 57
arm: "-"
pooled_cpm: 23.68
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# ERF

*ETS2 repressor factor* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.55× (z +19.9, q 0e+00, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +10.4, q 1e-22, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.681× (z -5.8, q 3e-06, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM6B]] (+0.69, fdr 9e-06), [[GLIS2]] (+0.65, fdr 8e-06), [[STK11]] (+0.64, fdr 3e-05); moves opposite to [[OPA1]] (-0.71, fdr 7e-06), [[ANAPC10]] (-0.65, fdr 7e-06), [[PHKB]] (-0.64, fdr 8e-06).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.55×** | +19.9 | 0e+00 | 41/47 (A498, LoVo, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +10.4 | 1e-22 | 38/48 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.86×** | +8.9 | 1e-16 | 38/48 (PANC-1, A498, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.63×** | +7.3 | 3e-11 | 27/47 (HEC-1-A, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.50×** | +6.1 | 1e-07 | 30/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.49×** | +6.0 | 2e-07 | 29/46 (NCI-H460, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.5 | 2e-06 | 22/48 (HEC-1-A, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.7 | 2e-04 | 19/32 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.3 | 0.001 | 20/48 (HS-578T, A549, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.32×** | +4.2 | 0.002 | 21/45 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.003 | 17/46 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.006 | 19/48 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.29×** | +3.8 | 0.006 | 18/48 (HOP62, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.28×** | +3.7 | 0.009 | 17/47 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.010 | 21/47 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.015 | 21/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.019 | 13/48 (HEC-1-A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.681×** | -5.8 | 3e-06 | 29/48 (NCI-H23, A-427, …) | two highest doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.687×** | -5.7 | 3e-06 | 31/47 (COLO 205, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.675×** | -5.6 | 3e-06 | 26/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.793×** | -5.0 | 8e-05 | 26/48 (C32, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -4.6 | 4e-04 | 24/48 (HOP62, SW 1271, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.742×** | -4.5 | 5e-04 | 23/48 (A-427, NCI-H23, …) | two highest doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.760×** | -4.2 | 0.002 | 15/48 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.584×** | -4.0 | 0.004 | 21/41 (HOP62, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.596×** | -3.9 | 0.007 | 17/48 (C32, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 40.2 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.258× (z -12.8) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.255× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 17.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +13.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.2) | — |
| [[A-427 (line)]] | wt | 34.5 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -11.1) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.256× (z -10.9) |
| [[A498 (line)]] | wt | 20.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +16.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AsPC-1 (line)]] | alt | 15.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +14.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 19.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +12.5) ⚠ cell-cycle shift, explains ~27% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.173× (z -8.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 22.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 41.7 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.262× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 14.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +12.0) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H1792 (line)]] | alt | 24.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +14.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -16.0) |
| [[PANC-1 (line)]] | alt | 13.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 33.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.7) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -10.7) |
| [[SNU-423 (line)]] | alt | 19.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Selinexor (drug)]] 5 µM 0.281× (z -10.7) ⚠ cell-cycle shift, explains ~65% of this change |
| [[A549 (line)]] | wt | 32.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +14.7) | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[CHP-212 (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.113× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HS-578T (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HT-29 (line)]] | alt | 56.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[KATO III (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +15.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 17.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +16.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 19.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +12.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +13.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +12.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW1417 (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.5) | — |
| [[A-172 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM6B]] | +0.69 | +0.69 / +0.57 | both halves | 9e-06 | pathway: Cellular Senescence |
| [[GLIS2]] | +0.65 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[STK11]] | +0.64 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[ZIC2]] | +0.63 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[TNRC6C]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[SIX5]] | +0.60 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[DLX2]] | +0.60 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[GSE1]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ZCCHC3]] | +0.59 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[PIK3IP1-DT]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ENO3]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[FOSL2]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPA1]] | -0.71 | -0.73 / -0.66 | both halves | 7e-06 |  |
| [[ANAPC10]] | -0.65 | -0.66 / -0.66 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[PHKB]] | -0.64 | -0.58 / -0.62 | both halves | 8e-06 |  |
| [[LONP2]] | -0.63 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[IQCB1]] | -0.62 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[MRPS35]] | -0.61 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[WDR36]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[DROSHA]] | -0.59 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[DNAJC24]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ATG5]] | -0.58 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[EIF3H]] | -0.58 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[EDEM2]] | -0.58 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises ERF's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (21.4, -2.9); signed map (5.2, -6.3). **Vector** length 109, 26.9% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +8.2 | +19.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.7 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.8 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +4.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.1 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -6.0 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.9 | -5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ETS2 repressor factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:42,247,569-42,255,128 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PE-2, PE2 |
| Gene groups (HGNC) | ETS transcription factor family |
| Reactome | 4 pathways, smallest: Oncogene Induced Senescence; Cellular Senescence; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P50548](https://www.uniprot.org/uniprotkb/P50548) (ETS domain-containing transcription factor ERF):

> Potent transcriptional repressor that binds to the H1 element of the Ets2 promoter. May regulate other genes involved in cellular proliferation. Required for extraembryonic ectoderm differentiation, ectoplacental cone cavity closure, and chorioallantoic attachment (By similarity). May be important for regulating trophoblast stem cell differentiation (By similarity).

**Summary**, from NCBI Gene [2077](https://www.ncbi.nlm.nih.gov/gene/2077):

> ETS2 is a transcription factor and protooncogene involved in development, apoptosis, and the regulation of telomerase. The protein encoded by this gene binds to the ETS2 promoter and is a strong repressor of ETS2 transcription. Several transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:3444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3444) · Entrez [2077](https://www.ncbi.nlm.nih.gov/gene/2077) · UniProt [P50548](https://www.uniprot.org/uniprotkb/P50548) · Ensembl [ENSG00000105722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105722)

## Data

Gene col 2654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2654); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2654]; `tensor/DDL_lfc|DDL_z.npy` [2654]; `embed/gene_vectors.npy` [2654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2654 or target_col == 2654). Every well: [[ERF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
