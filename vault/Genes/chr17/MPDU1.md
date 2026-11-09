---
symbol: "MPDU1"
type: "gene"
col: 4961
ensembl_id: "ENSG00000129255"
name: "mannose-P-dolichol utilization defect 1"
location: "17p13.1"
module: 83
arm: "+"
pooled_cpm: 18.0
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# MPDU1

*mannose-P-dolichol utilization defect 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.29× (z +16.3, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.508× (z -9.4, q 1e-18, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2D3-AS1]] (+0.84, fdr 7e-06), [[PCBP1-AS1]] (+0.79, fdr 7e-06), [[PARD6G-AS1]] (+0.77, fdr 1e-05); moves opposite to [[STX7]] (-0.70, fdr 1e-05), [[SERAC1]] (-0.70, fdr 1e-05), [[TMEM185A]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 083]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +16.3 | 0e+00 | 44/46 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +14.1 | 2e-42 | 39/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +9.4 | 9e-19 | 35/46 (SW480, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.78×** | +8.1 | 1e-13 | 35/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +7.6 | 3e-12 | 29/46 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.73×** | +7.1 | 1e-10 | 27/33 (NCI-H460, PANC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.7 | 2e-09 | 28/42 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.62×** | +6.5 | 6e-09 | 27/46 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.61×** | +6.4 | 1e-08 | 19/30 (Hs 766T, NCI-H2030, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.55×** | +6.1 | 5e-08 | 27/41 (LoVo, NCI-H2030, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.42×** | +4.9 | 6e-05 | 21/45 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.7 | 1e-04 | 23/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.45×** | +4.5 | 3e-04 | 19/46 (NCI-H460, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +4.4 | 5e-04 | 19/46 (A-172, C-33 A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.2 | 0.001 | 16/46 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.002 | 14/46 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.007 | 16/47 (A-172, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.007 | 14/46 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.021 | 15/47 (SK-MEL-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.022 | 5/44 (SHP-77, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.024 | 9/47 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.043 | 12/44 (RKO, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.046 | 16/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.047 | 13/47 (HEC-1-A, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4961.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.508×** | -9.4 | 1e-18 | 36/46 (SW48, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.508×** | -9.4 | 1e-18 | 41/47 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.642×** | -8.7 | 7e-16 | 38/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.548×** | -8.3 | 1e-14 | 32/47 (PANC-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.545×** | -7.3 | 3e-11 | 36/47 (COLO 205, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.426×** | -6.2 | 6e-08 | 32/47 (SW480, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.627×** | -5.6 | 2e-06 | 23/46 (C-33 A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **0.765×** | -5.3 | 1e-05 | 26/47 (A498, A549, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.720×** | -4.6 | 3e-04 | 21/46 (LS 180, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.732×** | -4.3 | 8e-04 | 23/47 (COLO 205, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.758×** | -3.5 | 0.024 | 14/47 (RKO, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | 0.842× | -3.4 | 0.035 | 18/47 (BT-474, LOX-IMVI, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.849× | -3.2 | 0.059 | 13/47 (SNU-1, AsPC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.790×** | -3.1 | 0.068 | 13/46 (NCI-H2030, LOX-IMVI, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.804×** | -3.0 | 0.092 | 11/46 (RKO, SW 1271, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.1) | [[Belinostat (drug)]] 5 µM 0.410× (z -8.5) |
| [[A498 (line)]] | wt | 25.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +15.3) | — |
| [[HEC-1-A (line)]] | alt | 14.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 11.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 16.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.64× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | [[Temsirolimus (drug)]] 0.5 µM 0.207× (z -8.5) |
| [[HS-578T (line)]] | alt | 17.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 8.32 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +9.8) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.137× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 21.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 15.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +14.6) | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0917× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.296× (z -8.6) |
| [[A-172 (line)]] | wt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +10.0) | — |
| [[A549 (line)]] | wt | 17.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0764× (z -10.4) |
| [[C32 (line)]] | wt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +11.9) | — |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 15.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +11.0) | — |
| [[LoVo (line)]] | wt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 18.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +11.1) | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.130× (z -9.1) |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2D3-AS1]] | +0.84 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[PCBP1-AS1]] | +0.79 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[PARD6G-AS1]] | +0.77 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[SNAPC5]] | +0.75 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[C2orf49-DT]] | +0.74 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | +0.73 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[LINC01004]] | +0.72 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[ERI2]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ZNF546]] | +0.71 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.70 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[GPR137]] | +0.70 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | +0.70 | +0.68 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX7]] | -0.70 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[SERAC1]] | -0.70 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[TMEM185A]] | -0.68 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[PCMT1]] | -0.65 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[SLC9A6]] | -0.65 | -0.66 / -0.39 | both halves | 5e-05 |  |
| [[RAB4A]] | -0.64 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[PKN1]] | -0.64 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[KIF3A]] | -0.64 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[ARNT]] | -0.64 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD27]] | -0.63 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[TUBG2]] | -0.63 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[RSAD1]] | -0.63 | -0.55 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.7, 9.5); signed map (21.4, -3.0). **Vector** length 101, 24.3% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.0 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +4.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.8 | -9.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.7 | -9.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.3 | -5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.0 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -8.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | mannose-P-dolichol utilization defect 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,583,529-7,592,789 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SL15, Lec35, PQLC5, CDGIf, SLC66A5 |
| Gene groups (HGNC) | Solute carrier family 66 |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75352](https://www.uniprot.org/uniprotkb/O75352) (Mannose-P-dolichol utilization defect 1 protein):

> Required for normal utilization of mannose-dolichol phosphate (Dol-P-Man) in the synthesis of N-linked and O-linked oligosaccharides and GPI anchors.

**Summary**, from NCBI Gene [9526](https://www.ncbi.nlm.nih.gov/gene/9526):

> This gene encodes an endoplasmic reticulum membrane protein that is required for utilization of the mannose donor mannose-P-dolichol in the synthesis of lipid-linked oligosaccharides and glycosylphosphatidylinositols. Mutations in this gene result in congenital disorder of glycosylation type If. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:7207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7207) · Entrez [9526](https://www.ncbi.nlm.nih.gov/gene/9526) · UniProt [O75352](https://www.uniprot.org/uniprotkb/O75352) · Ensembl [ENSG00000129255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129255)

## Data

Gene col 4961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4961); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4961]; `tensor/DDL_lfc|DDL_z.npy` [4961]; `embed/gene_vectors.npy` [4961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4961 or target_col == 4961). Every well: [[MPDU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPDU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
