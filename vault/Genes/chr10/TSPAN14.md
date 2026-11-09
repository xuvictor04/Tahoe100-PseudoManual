---
symbol: "TSPAN14"
type: "gene"
col: 2925
ensembl_id: "ENSG00000108219"
name: "tetraspanin 14"
location: "10q23.1"
module: 100
arm: "+"
pooled_cpm: 52.45
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# TSPAN14

*tetraspanin 14* — 10q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.29× (z +5.7, q 8e-06, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.470× (z -23.5, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK9]] (+0.64, fdr 1e-05), [[CDYL]] (+0.59, fdr 3e-05), [[SRPK2]] (+0.58, fdr 3e-05); moves opposite to [[LARP7]] (-0.58, fdr 2e-05), [[RBM23]] (-0.58, fdr 1e-05), [[GOSR1]] (-0.58, fdr 3e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PCSK9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +5.7 | 8e-06 | 25/46 (A549, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +4.8 | 4e-04 | 19/47 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +4.3 | 0.003 | 17/46 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.010 | 15/46 (SW48, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.010 | 15/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.032 | 19/46 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.033 | 18/47 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.034 | 13/46 (COLO 205, NCI-H1573, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +3.4 | 0.045 | 12/46 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.058 | 10/47 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.061 | 11/43 (NCI-H1573, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.2 | 0.065 | 18/47 (NCI-H460, RKO, …) | top dose only |  |
| [[Tadalafil (drug)]] 5 µM |  | 1.16× | +3.2 | 0.068 | 11/46 (Panc 03.27, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.470×** | -23.5 | 0e+00 | 42/47 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.478×** | -16.3 | 0e+00 | 37/47 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.558×** | -12.4 | 8e-33 | 34/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.630×** | -10.2 | 4e-22 | 30/47 (HEC-1-A, C32, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -8.3 | 1e-14 | 31/45 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -7.8 | 6e-13 | 28/47 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.709×** | -7.6 | 3e-12 | 23/43 (C32, HEC-1-A, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.723×** | -7.1 | 7e-11 | 30/47 (HEC-1-A, C32, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.722×** | -6.9 | 3e-10 | 21/37 (SW480, AN3 CA, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.712×** | -6.9 | 3e-10 | 22/38 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.612×** | -5.7 | 8e-07 | 19/46 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.618×** | -5.5 | 1e-06 | 24/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -5.5 | 2e-06 | 22/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.796×** | -5.0 | 2e-05 | 19/47 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.863× | -4.6 | 2e-04 | 16/47 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.828×** | -4.1 | 0.001 | 18/47 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.850× | -3.6 | 0.012 | 19/47 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.775×** | -2.9 | 0.098 | 10/47 (LOX-IMVI, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.910× | -2.9 | 0.099 | 6/47 (SK-MEL-2, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 177 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -18.4) |
| [[HEC-1-A (line)]] | alt | 102 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.357× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 53.7 | 6 (3 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.40× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 34.4 | 1 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.222× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -14.6) |
| [[SW480 (line)]] | alt | 40.4 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.428× (z -11.5) |
| [[LoVo (line)]] | wt | 49.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -21.4) |
| [[NCI-H2347 (line)]] | alt | 47.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -11.5) |
| [[Hs 766T (line)]] | wt | 62.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -15.5) |
| [[J82 (line)]] | alt | 50.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 60.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -17.3) |
| [[LS 180 (line)]] | wt | 68.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 17.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.2) |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -11.0) |
| [[A549 (line)]] | wt | 72.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -13.4) |
| [[AN3 CA (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.4) |
| [[BT-474 (line)]] | alt | 84.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.2) |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -8.9) |
| [[COLO 205 (line)]] | alt | 63.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -22.8) |
| [[HOP62 (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.9) |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.9) |
| [[HT-29 (line)]] | alt | 78.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -12.2) |
| [[KATO III (line)]] | alt | 47.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 61.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -9.7) |
| [[RKO (line)]] | wt | 28.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.297× (z -8.7) |
| [[SW1417 (line)]] | alt | 47.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.396× (z -9.6) |
| [[A-172 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 99.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK9]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[CDYL]] | +0.59 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[SRPK2]] | +0.58 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[LPCAT4]] | +0.58 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[CYRIB]] | +0.57 | +0.63 / +0.37 | both halves | 7e-05 |  |
| [[NOL4L]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CD276]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[INPP5F]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CYTH3]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[TANC1]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TSPAN17]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 | same gene group |
| [[B3GNT2]] | +0.55 | +0.42 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP7]] | -0.58 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[RBM23]] | -0.58 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[GOSR1]] | -0.58 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[ZNF140]] | -0.57 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[AIMP1]] | -0.56 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[C1orf43]] | -0.55 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[LINC00174]] | -0.55 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[EPC1]] | -0.54 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[OCIAD1]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TOR1AIP1]] | -0.53 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[USP16]] | -0.53 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[METTL6]] | -0.53 | -0.62 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK9]] | B | PCSK9 activity raises TSPAN14's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.55× lower at baseline in the lines without PCSK9 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[B3GNT7]] | B | B3GNT7 activity raises TSPAN14's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.62× lower at baseline in the lines without B3GNT7 | 0.037 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[WNT7A]] | B | WNT7A activity raises TSPAN14's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.57× lower at baseline in the lines without WNT7A | 0.045 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[RFLNB]] | B | RFLNB activity lowers TSPAN14's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.65× higher at baseline in the lines without RFLNB | 0.046 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[SYTL4]] | B | SYTL4 activity raises TSPAN14's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.24× lower at baseline in the lines without SYTL4 | 0.060 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[MMP15]] | B | MMP15 activity raises TSPAN14's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 2.01× lower at baseline in the lines without MMP15 | 0.066 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.429). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.6, -2.9); signed map (-16.9, 39.5). **Vector** length 103, 24.7% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +7.1 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +2.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[vincristine (drug)]] 5 µM |  | +2.7 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -23.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -7.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.7 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -5.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.1 — chr10:80,454,265-80,533,124 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DC-TM4F2, MGC11352; previously TM4SF14 |
| Gene groups (HGNC) | Tetraspanin family |
| Reactome | 3 pathways, smallest: Amyloid fiber formation; Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NG11](https://www.uniprot.org/uniprotkb/Q8NG11) (Tetraspanin-14):

> Part of TspanC8 subgroup, composed of 6 members that interact with the transmembrane metalloprotease ADAM10. This interaction is required for ADAM10 exit from the endoplasmic reticulum and for enzymatic maturation and trafficking to the cell surface as well as substrate specificity. Different TspanC8/ADAM10 complexes have distinct substrates. Negatively regulates ADAM10-mediated cleavage of GP6 (By similarity). Promotes ADAM10-mediated cleavage of CDH5 (By similarity).

**Summary**, from NCBI Gene [81619](https://www.ncbi.nlm.nih.gov/gene/81619):

> Enables enzyme binding activity. Involved in positive regulation of Notch signaling pathway; protein localization to plasma membrane; and protein maturation. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23303) · Entrez [81619](https://www.ncbi.nlm.nih.gov/gene/81619) · UniProt [Q8NG11](https://www.uniprot.org/uniprotkb/Q8NG11) · Ensembl [ENSG00000108219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108219)

## Data

Gene col 2925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2925); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2925]; `tensor/DDL_lfc|DDL_z.npy` [2925]; `embed/gene_vectors.npy` [2925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2925 or target_col == 2925). Every well: [[TSPAN14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
