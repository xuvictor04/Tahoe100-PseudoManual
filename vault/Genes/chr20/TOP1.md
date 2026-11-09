---
symbol: "TOP1"
type: "gene"
col: 12727
ensembl_id: "ENSG00000198900"
name: "DNA topoisomerase I"
location: "20q12"
module: 98
arm: "+"
pooled_cpm: 387.72
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 16
n_dd_up_clean: 21
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 98
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# TOP1

*DNA topoisomerase I* — 20q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +25.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.666× (z -9.9, q 3e-20, down in 42 of 50 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA10]] (+0.70, fdr 7e-06), [[PTPN12]] (+0.67, fdr 1e-05), [[TBC1D8]] (+0.67, fdr 7e-06); moves opposite to [[GPRC5B]] (-0.61, fdr 1e-05), [[BBOX1-AS1]] (-0.51, fdr 3e-05), [[RRAD]] (-0.50, fdr 3e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 98 go from it, the strongest it → [[SRBD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +25.9 | 0e+00 | 45/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.40×** | +21.1 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +19.2 | 0e+00 | 46/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.16×** | +17.8 | 0e+00 | 45/48 (COLO 205, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +17.0 | 0e+00 | 45/48 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.80×** | +14.1 | 3e-43 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.79×** | +14.1 | 5e-43 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.84×** | +12.2 | 2e-32 | 46/49 (SW480, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.68×** | +12.0 | 2e-31 | 41/47 (COLO 205, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +11.3 | 7e-28 | 44/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +10.5 | 3e-24 | 34/49 (AsPC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +10.5 | 3e-24 | 39/50 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +8.9 | 2e-17 | 38/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +7.2 | 2e-11 | 29/48 (A-172, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.31×** | +6.5 | 3e-09 | 33/48 (A-172, Hs 766T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +6.3 | 1e-08 | 27/48 (LoVo, A-172, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.30×** | +6.3 | 1e-08 | 27/48 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +5.9 | 1e-07 | 22/48 (SNU-1, A-172, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.29×** | +5.8 | 2e-07 | 29/49 (HS-578T, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.26×** | +5.5 | 8e-07 | 25/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.666×** | -9.9 | 3e-20 | 42/50 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.710×** | -8.3 | 4e-14 | 38/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.710×** | -8.0 | 3e-13 | 37/47 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.762×** | -7.9 | 4e-13 | 32/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.795×** | -7.7 | 1e-12 | 33/48 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.728×** | -7.6 | 4e-12 | 36/47 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.730×** | -7.0 | 2e-10 | 36/48 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.770×** | -6.9 | 5e-10 | 34/49 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.752×** | -6.8 | 6e-10 | 34/49 (NCI-H1573, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.747×** | -6.8 | 7e-10 | 35/48 (NCI-H1573, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.811×** | -6.2 | 4e-08 | 28/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.851× | -5.6 | 1e-06 | 21/48 (RPMI-7951, SHP-77, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.792×** | -5.3 | 4e-06 | 29/48 (NCI-H2347, SHP-77, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.854× | -5.3 | 4e-06 | 19/49 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.673×** | -4.7 | 1e-04 | 32/50 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 266 | 25 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +18.5) | — |
| [[A498 (line)]] | wt | 252 | 23 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +29.3) | — |
| [[Hs 766T (line)]] | wt | 498 | 23 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +27.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 576 | 8 (2 ⚠) | 15 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +23.3) | [[Adagrasib (drug)]] 0.05 µM 0.600× (z -26.5) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.508× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 409 | 20 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.01× (z +15.3) | [[Trametinib (drug)]] 5 µM 0.500× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 836 | 9 (3 ⚠) | 9 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.24× (z +22.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.270× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 767 | 2 | 16 (4 ⚠) | [[Budesonide (drug)]] 0.05 µM 1.75× (z +8.9) | [[Trametinib (drug)]] 5 µM 0.462× (z -12.4) |
| [[A-172 (line)]] | wt | 196 | 17 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +22.7) | — |
| [[AsPC-1 (line)]] | alt | 401 | 17 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +29.5) | — |
| [[RPMI-7951 (line)]] | alt | 473 | 16 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +14.7) | — |
| [[SW480 (line)]] | alt | 352 | 16 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.56× (z +25.6) | — |
| [[SNU-423 (line)]] | alt | 370 | 15 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +21.9) | — |
| [[NCI-H460 (line)]] | wt | 340 | 13 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.68× (z +18.1) | — |
| [[HEC-1-A (line)]] | alt | 217 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +22.7) | — |
| [[NCI-H23 (line)]] | alt | 305 | 12 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.69× (z +17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +17.5) | — |
| [[SNU-1 (line)]] | wt | 281 | 12 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +14.7) | — |
| [[J82 (line)]] | alt | 326 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +19.4) | — |
| [[RKO (line)]] | wt | 509 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +13.3) | — |
| [[C32 (line)]] | wt | 318 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +18.5) | — |
| [[CFPAC-1 (line)]] | alt | 597 | 3 | 6 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +25.0) | [[Trametinib (drug)]] 5 µM 0.524× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 361 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +19.8) | — |
| [[PANC-1 (line)]] | alt | 233 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +18.6) | — |
| [[HOP62 (line)]] | alt | 253 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +19.8) | — |
| [[HT-29 (line)]] | alt | 439 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +20.9) | — |
| [[A549 (line)]] | wt | 348 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +22.9) | — |
| [[BT-474 (line)]] | alt | 219 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 334 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +21.4) | — |
| [[LoVo (line)]] | wt | 361 | 6 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.51× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +15.1) | [[Ponatinib (drug)]] 5 µM 0.558× (z -9.7) |
| [[LS 180 (line)]] | wt | 337 | 6 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +19.7) | [[Ponatinib (drug)]] 5 µM 0.592× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 279 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +20.1) | — |
| [[HepG2_C3A (line)]] | wt | 543 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +15.7) | — |
| [[hTERT-HPNE (line)]] | wt | 345 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.3) | — |
| [[KATO III (line)]] | alt | 422 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +17.3) | — |
| [[SW1417 (line)]] | alt | 811 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +13.6) | — |
| [[A-427 (line)]] | wt | 210 | 4 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +14.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.4) | — |
| [[H4 (line)]] | wt | 257 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.4) | — |
| [[HCT15 (line)]] | alt | 285 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.70× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 440 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +19.0) | — |
| [[C-33 A (line)]] | alt | 255 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 409 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +12.8) | — |
| [[SHP-77 (line)]] | alt | 305 | 0 | 3 | — | [[Trametinib (drug)]] 0.5 µM 0.524× (z -9.2) |
| [[CHP-212 (line)]] | wt | 405 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.2) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.349× (z -9.8) |
| [[SW 900 (line)]] | alt | 500 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.9) | — |
| [[SW48 (line)]] | wt | 660 | 1 (1 ⚠) | 1 | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.76× (z +9.9) ⚠ cell-cycle shift, explains ~51% of this change | [[Binimetinib (drug)]] 5 µM 0.453× (z -8.7) |
| [[SW 1271 (line)]] | alt | 293 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 361 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 448 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 409 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 405 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA10]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PTPN12]] | +0.67 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.67 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[TBXAS1]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[FOXL1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT5]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[STXBP5-AS1]] | +0.60 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[PITPNC1]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[NPAS2]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[HMGA2-AS1]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[FOXC2]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5B]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[BBOX1-AS1]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[RRAD]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[KIF13A]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SLAMF7]] | -0.48 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[CYRIA]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[CD5L]] | -0.46 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[ADAMTS16]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ZNF624]] | -0.45 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TOP1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity raises TOP1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[CYRIA]] | B | CYRIA activity raises TOP1's level | lines that do not express CYRIA (24) vs lines expressing it (26) | 1.17× lower at baseline in the lines without CYRIA | 0.085 | ⚠ within organs, on part of the lines; also absent: PTGS2, ATP10A, VCAN |
| [[CD5L]] | B | CD5L activity raises TOP1's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.22× lower at baseline in the lines without CD5L | 0.093 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |

### Downstream of this gene

*98 arrows, 98 of them with an alert ⚠; grade A 0, B 98, C 0. Shown: the 12 strongest; 86 more arrows (86 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRBD1]] | B | TOP1 activity lowers SRBD1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 1.4% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ENSG00000227240]] | B | TOP1 activity raises ENSG00000227240's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ENSG00000229618]] | B | TOP1 activity raises ENSG00000229618's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ENSG00000267053]] | B | TOP1 activity lowers ENSG00000267053's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MND1]] | B | TOP1 activity lowers MND1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC03041]] | B | TOP1 activity raises LINC03041's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TAF4]] | B | TOP1 activity lowers TAF4's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CENPO]] | B | TOP1 activity lowers CENPO's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MELK]] | B | TOP1 activity lowers MELK's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[POLQ]] | B | TOP1 activity lowers POLQ's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RFC3]] | B | TOP1 activity lowers RFC3's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TBC1D31]] | B | TOP1 activity lowers TBC1D31's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.8, 14.5); signed map (16.9, 33.6). **Vector** length 121, 49.2% of its response variance represented; |z| ≥ 3 in 2,286 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +8.0 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +10.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.7 | +8.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +6.5 | +3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +6.4 | +5.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +6.3 | +3.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +6.3 | +4.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.8 | -9.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.3 | -8.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.8 | -7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.4 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.0 | -6.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -7.0 | -7.6 |

## What is on record

|  |  |
|---|---|
| Name | DNA topoisomerase I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q12 — chr20:41,028,822-41,124,487 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Topoisomerases |
| Hallmark sets | HEME_METABOLISM, G2M_CHECKPOINT |
| Reactome | 3 pathways, smallest: SUMOylation of DNA replication proteins; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P11387](https://www.uniprot.org/uniprotkb/P11387) (DNA topoisomerase 1):

> Releases the supercoiling and torsional tension of DNA introduced during the DNA replication and transcription by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(3'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 5'-OH DNA strand. The free DNA strand then rotates …

**Summary**, from NCBI Gene [7150](https://www.ncbi.nlm.nih.gov/gene/7150):

> This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This enzyme catalyzes the transient breaking and rejoining of a single strand of DNA which allows the strands to pass through one another, thus altering the topology of DNA. This gene is localized to chromosome 20 and has pseudogenes which reside on chromosomes 1 and 22. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11986) · Entrez [7150](https://www.ncbi.nlm.nih.gov/gene/7150) · UniProt [P11387](https://www.uniprot.org/uniprotkb/P11387) · Ensembl [ENSG00000198900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198900)

## Data

Gene col 12727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12727); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12727]; `tensor/DDL_lfc|DDL_z.npy` [12727]; `embed/gene_vectors.npy` [12727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12727 or target_col == 12727). Every well: [[TOP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
