---
symbol: "BOD1L1"
type: "gene"
col: 450
ensembl_id: "ENSG00000038219"
name: "biorientation of chromosomes in cell division 1 like 1"
location: "4p15.33"
module: 74
arm: "+"
pooled_cpm: 201.73
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# BOD1L1

*biorientation of chromosomes in cell division 1 like 1* — 4p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +20.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.667× (z -10.4, q 1e-22, down in 43 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.663× (z -5.5, q 9e-06, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGB1]] (+0.75, fdr 7e-06), [[SLU7]] (+0.73, fdr 7e-06), [[RSF1]] (+0.72, fdr 7e-06); moves opposite to [[COLGALT1]] (-0.62, fdr 7e-06), [[SIGMAR1]] (-0.62, fdr 7e-06), [[MDH2]] (-0.60, fdr 9e-06).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +20.9 | 0e+00 | 46/48 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +14.8 | 0e+00 | 44/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +13.0 | 2e-36 | 44/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +7.6 | 5e-12 | 33/48 (C32, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +6.9 | 4e-10 | 30/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.29×** | +6.5 | 7e-09 | 29/48 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +6.4 | 1e-08 | 32/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +5.9 | 2e-07 | 28/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +5.9 | 2e-07 | 30/48 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +5.4 | 3e-06 | 26/48 (A-172, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.23×** | +5.3 | 5e-06 | 28/48 (LS 180, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +5.1 | 2e-05 | 31/49 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +5.1 | 2e-05 | 34/47 (A549, J82, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.4 | 5e-04 | 21/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.2 | 0.001 | 26/45 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.005 | 23/48 (LS 180, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ciclopirox (drug)]] 5 µM |  | 1.09× | +3.1 | 0.047 | 0/48 | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.052 | 8/48 (HS-578T, Hs 766T, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.056 | 7/49 (LoVo, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -10.4 | 1e-22 | 43/48 (SNU-1, SW48, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.663×** | -5.5 | 9e-06 | 44/48 (SW48, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.813×** | -5.1 | 6e-05 | 26/47 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.713×** | -4.6 | 6e-04 | 37/48 (PANC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.713×** | -4.6 | 6e-04 | 33/48 (RKO, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.840× | -4.5 | 7e-04 | 21/48 (LOX-IMVI, SW 900, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -4.3 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.888× | -4.3 | 0.001 | 4/48 (KATO III, RKO, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.746×** | -3.9 | 0.005 | 26/48 (H4, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.760×** | -3.9 | 0.005 | 25/48 (A498, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.899× | -3.9 | 0.006 | 2/48 (C-33 A, SNU-1) | rises with dose |  |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.907× | -3.5 | 0.021 | 0/48 | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.858× | -3.5 | 0.023 | 12/48 (J82, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.025 | 22/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.912× | -3.3 | 0.031 | 3/48 (SK-MEL-2, Hs 766T, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.887× | -3.1 | 0.068 | 9/48 (RKO, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 211 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +21.2) | — |
| [[LS 180 (line)]] | wt | 167 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +18.8) | — |
| [[NCI-H1573 (line)]] | alt | 285 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +19.1) | — |
| [[A549 (line)]] | wt | 169 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +22.6) | — |
| [[NCI-H460 (line)]] | wt | 105 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.5) | — |
| [[RKO (line)]] | wt | 155 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +19.6) | — |
| [[C32 (line)]] | wt | 207 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.5) | — |
| [[LOX-IMVI (line)]] | wt | 154 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +20.3) | — |
| [[NCI-H1792 (line)]] | alt | 198 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +18.9) | — |
| [[NCI-H2347 (line)]] | alt | 228 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +24.3) | — |
| [[SW480 (line)]] | alt | 198 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +12.0) | — |
| [[A498 (line)]] | wt | 259 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 214 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 248 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +15.3) | — |
| [[HS-578T (line)]] | alt | 173 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 248 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.9) | — |
| [[A-172 (line)]] | wt | 185 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.3) | — |
| [[A-427 (line)]] | wt | 190 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.452× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 158 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 322 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +17.6) | — |
| [[COLO 205 (line)]] | alt | 188 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.2) | — |
| [[H4 (line)]] | wt | 341 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 216 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 159 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 102 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.3) | — |
| [[NCI-H23 (line)]] | alt | 214 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.6) | — |
| [[PANC-1 (line)]] | alt | 155 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 260 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +12.0) | — |
| [[SNU-1 (line)]] | wt | 190 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.444× (z -9.5) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 164 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +12.4) | — |
| [[SW48 (line)]] | wt | 142 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 201 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.364× (z -8.8) |
| [[BT-474 (line)]] | alt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +15.2) | — |
| [[HT-29 (line)]] | alt | 204 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 292 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.83× (z +8.6) | — |
| [[J82 (line)]] | alt | 259 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +10.5) | — |
| [[KATO III (line)]] | alt | 198 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 232 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.193× (z -12.8) ⚠ toxic |
| [[SW 900 (line)]] | alt | 408 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.549× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 259 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 169 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 180 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 321 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGB1]] | +0.75 | +0.69 / +0.82 | both halves | 7e-06 |  |
| [[SLU7]] | +0.73 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[RSF1]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | STRING 416 |
| [[AKAP9]] | +0.71 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[LARP7]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[KDM5A]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[SEC62]] | +0.69 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[XRN1]] | +0.69 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[NBR1]] | +0.69 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[SNW1]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[FAM32A]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.68 | +0.74 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLGALT1]] | -0.62 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[SIGMAR1]] | -0.62 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[MDH2]] | -0.60 | -0.57 / -0.57 | both halves | 9e-06 |  |
| [[OLA1]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[FAR1]] | -0.59 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[CDCA7]] | -0.59 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[NDC1]] | -0.58 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[WRNIP1]] | -0.57 | -0.61 / -0.52 | both halves | 1e-05 | STRING 605 |
| [[ALG6]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TMEM109]] | -0.56 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[RANBP1]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.5, -47.3); signed map (3.3, -14.7). **Vector** length 137, 44.8% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +14.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +20.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +7.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.5 | +3.1 |
|  | [[Saquinavir (drug)]] 5 µM |  | +3.3 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.2 | -10.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | -7.0 | -5.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.3 | -5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.6 | -4.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.5 | -3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.5 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | biorientation of chromosomes in cell division 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.33 — chr4:13,568,738-13,627,725 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33215, KIAA1327; previously FAM44A, BOD1L |
| Gene groups (HGNC) | Biorientation of chromosomes in cell division family |
| Reactome | 3 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; Epigenetic regulation by WDR5-containing histone modifying complexes; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFC6](https://www.uniprot.org/uniprotkb/Q8NFC6) (Biorientation of chromosomes in cell division protein 1-like 1):

> Component of the fork protection machinery required to protect stalled/damaged replication forks from uncontrolled DNA2-dependent resection. Acts by stabilizing RAD51 at stalled replication forks and protecting RAD51 nucleofilaments from the antirecombinogenic activities of FBH1 and BLM. Does not regulate spindle orientation.

**Summary**, from NCBI Gene [259282](https://www.ncbi.nlm.nih.gov/gene/259282):

> Involved in DNA damage response and replication fork processing. Predicted to be located in nucleoplasm. Predicted to be part of Set1C/COMPASS complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31792) · Entrez [259282](https://www.ncbi.nlm.nih.gov/gene/259282) · UniProt [Q8NFC6](https://www.uniprot.org/uniprotkb/Q8NFC6) · Ensembl [ENSG00000038219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000038219)

## Data

Gene col 450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 450); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 450]; `tensor/DDL_lfc|DDL_z.npy` [450]; `embed/gene_vectors.npy` [450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 450 or target_col == 450). Every well: [[BOD1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BOD1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
