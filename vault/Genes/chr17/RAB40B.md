---
symbol: "RAB40B"
type: "gene"
col: 6540
ensembl_id: "ENSG00000141542"
name: "RAB40B, member RAS oncogene family"
location: "17q25.3"
module: 85
arm: "+"
pooled_cpm: 14.19
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 39
n_dd_up_clean: 15
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# RAB40B

*RAB40B, member RAS oncogene family* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.11× (z +21.9, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.333× (z -24.0, q 0e+00, down in 38 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPSB3]] (+0.73, fdr 8e-06), [[GET1]] (+0.68, fdr 1e-05), [[SLC27A1]] (+0.67, fdr 7e-05); moves opposite to [[ST7]] (-0.67, fdr 3e-05), [[ST7L]] (-0.65, fdr 3e-05), [[CSTF3]] (-0.65, fdr 2e-04).
> It sits in the **+** arm of [[Module 085]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.11×** | +21.9 | 0e+00 | 43/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.64×** | +20.0 | 0e+00 | 42/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.93×** | +16.6 | 0e+00 | 41/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +11.3 | 1e-27 | 37/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.90×** | +9.9 | 3e-21 | 33/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +6.8 | 1e-09 | 23/45 (KATO III, A549, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.14×** | +6.1 | 7e-08 | 21/46 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.6 | 2e-06 | 1/46 (NCI-H2347) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +4.4 | 7e-04 | 10/46 (NCI-H1792, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.003 | 9/45 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.015 | 8/46 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.036 | 6/45 (NCI-H460, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.2 | 0.055 | 9/42 (KATO III, RKO, …) | top dose only | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.076 | 6/43 (LoVo, COLO 205, …) | rises with dose |  |
| [[MK-3903 (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.084 | 4/41 (HT-29, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.086 | 6/45 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.086 | 5/46 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.333×** | -24.0 | 0e+00 | 38/43 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.211×** | -23.1 | 0e+00 | 39/43 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.295×** | -18.9 | 0e+00 | 38/45 (SNU-423, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.307×** | -18.2 | 0e+00 | 39/44 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.440×** | -12.5 | 1e-33 | 27/41 (A-172, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.493×** | -10.9 | 6e-26 | 31/45 (KATO III, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -10.3 | 7e-23 | 30/44 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.540×** | -9.5 | 1e-19 | 26/45 (A-172, LS 180, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.351×** | -8.5 | 2e-15 | 26/45 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.359×** | -8.3 | 7e-15 | 28/43 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.366×** | -8.1 | 2e-14 | 26/42 (KATO III, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.367×** | -8.1 | 3e-14 | 24/40 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.371×** | -8.0 | 5e-14 | 24/40 (CFPAC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.602×** | -7.9 | 2e-13 | 27/44 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.384×** | -7.7 | 4e-13 | 24/36 (MIA PaCa-2, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -6.4 | 7e-09 | 22/45 (HT-29, KATO III, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -6.3 | 1e-08 | 20/44 (hTERT-HPNE, A-427, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.668×** | -5.9 | 1e-07 | 19/44 (Hs 766T, LoVo, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 32.4 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -23.2) |
| [[KATO III (line)]] | alt | 91.1 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -22.3) |
| [[A-172 (line)]] | wt | 20.0 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0123× (z -28.4) |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0495× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 18.2 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 33.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -16.5) |
| [[LS 180 (line)]] | wt | 33.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -15.0) |
| [[HEC-1-A (line)]] | alt | 21.6 | 2 | 3 | [[Panobinostat (drug)]] 5 µM 3.03× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.9) |
| [[HOP62 (line)]] | alt | 14.4 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 11.5 | 1 | 4 | [[Panobinostat (drug)]] 5 µM 4.08× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.0782× (z -14.8) |
| [[SW480 (line)]] | alt | 8.37 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 7.37× (z +12.7) | [[Harringtonine (drug)]] 5 µM 0.174× (z -10.6) |
| [[A498 (line)]] | wt | 16.9 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.201× (z -11.2) |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 17.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -14.1) |
| [[PANC-1 (line)]] | alt | 4.80 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.6× (z +12.1) | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.8) |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 3 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0775× (z -13.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 10.1 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 3.67× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.4) |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 3 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0629× (z -10.5) |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -16.8) |
| [[A-427 (line)]] | wt | 8.95 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0866× (z -10.4) |
| [[A549 (line)]] | wt | 7.86 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.72× (z +8.8) | — |
| [[LoVo (line)]] | wt | 8.72 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.99× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.160× (z -10.4) |
| [[C-33 A (line)]] | alt | 7.02 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0388× (z -10.2) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 6.01 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0747× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 8.83 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0785× (z -8.7) |
| [[J82 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -16.2) |
| [[RKO (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 9.40 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0720× (z -11.1) |
| [[SW48 (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0877× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPSB3]] | +0.73 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[GET1]] | +0.68 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.67 | +0.64 / +0.38 | both halves | 7e-05 |  |
| [[MAST3]] | +0.66 | +0.70 / +0.31 | both halves | 2e-04 |  |
| [[CABLES2]] | +0.66 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[MOSPD3]] | +0.66 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ANKRD27]] | +0.65 | +0.67 / +0.34 | both halves | 1e-04 |  |
| [[YPEL2]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | same gene group |
| [[ADIPOR1]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MPST]] | +0.64 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[MPND]] | +0.64 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[C2CD2L]] | +0.64 | +0.39 / +0.68 | both halves | 5e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7]] | -0.67 | -0.51 / -0.44 | both halves | 3e-05 | same gene group |
| [[ST7L]] | -0.65 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[CSTF3]] | -0.65 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[ERCC6L2]] | -0.64 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ZNF518A]] | -0.64 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[FAM169A]] | -0.63 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[PATL2]] | -0.63 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[RP1]] | -0.62 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[RWDD2B]] | -0.62 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[ARRDC3-AS1]] | -0.62 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[LPXN]] | -0.62 | -0.58 / -0.32 | both halves | 1e-04 |  |
| [[WAKMAR2]] | -0.62 | -0.58 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.712). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.0, -13.7); signed map (-39.0, -1.7). **Vector** length 102, 25.1% of its response variance represented; |z| ≥ 3 in 1,338 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.9 | +16.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.5 | +21.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.4 | +20.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +11.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.7 | -23.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -18.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -12.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -18.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -24.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.8 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | RAB40B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,654,973-82,698,698 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEC4L, RAR |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases; MicroRNA protein coding host genes |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12829](https://www.uniprot.org/uniprotkb/Q12829) (Ras-related protein Rab-40B):

> RAB40B small GTPase acts as substrate-recognition components of the ECS(RAB40B) E3 ubiquitin ligase complex which mediates the ubiquitination of target proteins. The Rab40 subfamily belongs to the Rab family that are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors …

**Summary**, from NCBI Gene [10966](https://www.ncbi.nlm.nih.gov/gene/10966):

> The protein encoded by this gene has similarity to a yeast protein which suggests a role of the gene product in regulating secretory vesicles. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18284) · Entrez [10966](https://www.ncbi.nlm.nih.gov/gene/10966) · UniProt [Q12829](https://www.uniprot.org/uniprotkb/Q12829) · Ensembl [ENSG00000141542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141542)

## Data

Gene col 6540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6540); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6540]; `tensor/DDL_lfc|DDL_z.npy` [6540]; `embed/gene_vectors.npy` [6540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6540 or target_col == 6540). Every well: [[RAB40B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB40B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
