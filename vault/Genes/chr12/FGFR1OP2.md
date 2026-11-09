---
symbol: "FGFR1OP2"
type: "gene"
col: 3282
ensembl_id: "ENSG00000111790"
name: "FGFR1 oncogene partner 2"
location: "12p11.23"
module: 24
arm: "+"
pooled_cpm: 80.09
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# FGFR1OP2

*FGFR1 oncogene partner 2* — 12p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.33× (z +16.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.938× (z -4.6, q 0.002, down in 0 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.813× (z -4.1, q 0.011, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.0896×, SK-MEL-2 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW 1271 0.0916×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H596 0.207×; ⚠ cell-cycle shift, would explain all of this change); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.219×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF654]] (+0.65, fdr 1e-05), [[KATNA1]] (+0.63, fdr 1e-05), [[RBPJ]] (+0.63, fdr 1e-05); moves opposite to [[ZNF628]] (-0.58, fdr 1e-05), [[COA7]] (-0.57, fdr 3e-05), [[ARMC6]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +16.8 | 0e+00 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +16.2 | 0e+00 | 42/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +16.0 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.13×** | +15.0 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +14.9 | 0e+00 | 46/49 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +12.3 | 8e-33 | 44/50 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +12.2 | 3e-32 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +12.0 | 2e-31 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +11.2 | 2e-27 | 43/48 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.69×** | +10.4 | 1e-23 | 43/48 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +8.9 | 2e-17 | 38/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +8.7 | 1e-16 | 41/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.49×** | +7.9 | 1e-13 | 36/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.8 | 2e-13 | 34/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.1 | 6e-11 | 32/47 (HT-29, HCT15, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +7.0 | 8e-11 | 43/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +5.3 | 4e-06 | 35/49 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +5.3 | 4e-06 | 29/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3282.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.0896×, SK-MEL-2 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW 1271 0.0916×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H596 0.207×; ⚠ cell-cycle shift, would explain all of this change); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.219×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -4.6 | 0.002 | 0/50 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -4.1 | 0.011 | 25/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.823×** | -3.7 | 0.038 | 19/49 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.845× | -3.4 | 0.11 | 18/49 (NCI-H2030, SW 900, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.858× | -3.1 | 0.23 | 11/48 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.860× | -3.0 | 0.23 | 14/49 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 182 | 14 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +16.0) | — |
| [[PANC-1 (line)]] | alt | 94.1 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.7) | — |
| [[NCI-H23 (line)]] | alt | 138 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +12.6) | — |
| [[LoVo (line)]] | wt | 72.7 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +15.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 94.3 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +11.9) | — |
| [[A498 (line)]] | wt | 51.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +16.3) | — |
| [[HT-29 (line)]] | alt | 71.6 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +12.0) | — |
| [[KATO III (line)]] | alt | 59.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 58.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 85.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.0896× (z -30.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 77.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 42.7 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +10.9) | — |
| [[A-172 (line)]] | wt | 41.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +13.9) | — |
| [[COLO 205 (line)]] | alt | 46.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 168 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.2) | — |
| [[A549 (line)]] | wt | 57.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 55.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 124 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.54× (z +11.4) | — |
| [[J82 (line)]] | alt | 73.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 74.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.9) | — |
| [[A-427 (line)]] | wt | 90.7 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 83.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 87.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.534× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 94.2 | 0 | 2 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.207× (z -9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Atazanavir (sulfate) (drug)]] 5 µM 0.219× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 46.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 42.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 65.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +13.3) | — |
| [[SW48 (line)]] | wt | 55.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.2) | — |
| [[C32 (line)]] | wt | 82.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +13.2) | — |
| [[Hs 766T (line)]] | wt | 58.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.66× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 58.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 80.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.4) | — |
| [[RKO (line)]] | wt | 97.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.54× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 52.0 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.75× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0916× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 82.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF654]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[KATNA1]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.63 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RAB8B]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PPP1R2]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[OST4]] | +0.60 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[TBC1D12]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PEX3]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.59 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PAPOLG]] | +0.59 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[CNIH4]] | +0.59 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF628]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[COA7]] | -0.57 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ARMC6]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[SAE1]] | -0.57 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[DNAJB12]] | -0.54 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[GRWD1]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SLC19A1]] | -0.54 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[BRD9]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[WDR18]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[SRSF6]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PFAS]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PUS1]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.480). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-1.2, -35.8); signed map (-23.6, 17.8). **Vector** length 72.7, 19.3% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +12.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +4.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.0 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.4 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | +16.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -0.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | FGFR1 oncogene partner 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.23 — chr12:26,938,470-26,966,650 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564O1863 |
| Gene groups (HGNC) | STRIPAK complex |
| Reactome | 5 pathways, smallest: Signaling by cytosolic FGFR1 fusion mutants; FGFR1 mutant receptor activation; Signaling by FGFR1 in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVK5](https://www.uniprot.org/uniprotkb/Q9NVK5) (FGFR1 oncogene partner 2):

> May be involved in wound healing pathway.

**Summary**, from NCBI Gene [26127](https://www.ncbi.nlm.nih.gov/gene/26127):

> Predicted to enable identical protein binding activity. Predicted to be involved in response to wounding. Predicted to act upstream of or within wound healing. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23098) · Entrez [26127](https://www.ncbi.nlm.nih.gov/gene/26127) · UniProt [Q9NVK5](https://www.uniprot.org/uniprotkb/Q9NVK5) · Ensembl [ENSG00000111790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111790)

## Data

Gene col 3282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3282); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3282]; `tensor/DDL_lfc|DDL_z.npy` [3282]; `embed/gene_vectors.npy` [3282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3282 or target_col == 3282). Every well: [[FGFR1OP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGFR1OP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
