---
symbol: "UCHL5"
type: "gene"
col: 3833
ensembl_id: "ENSG00000116750"
name: "ubiquitin C-terminal hydrolase L5"
location: "1q31.2"
module: 215
arm: "+"
pooled_cpm: 69.46
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# UCHL5

*ubiquitin C-terminal hydrolase L5* — 1q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.72× (z +27.8, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.44× (z +10.1, q 1e-21, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.693× (z -10.2, q 9e-22, down in 31 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.767× (z -7.4, q 4e-11, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUS7L]] (+0.68, fdr 1e-05), [[SF3A3]] (+0.64, fdr 7e-06), [[LARS1]] (+0.62, fdr 7e-06); moves opposite to [[RBM38]] (-0.63, fdr 2e-05), [[IP6K2]] (-0.63, fdr 3e-05), [[MIEN1]] (-0.62, fdr 1e-05).
> It is in [[Module 215]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3833.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +27.8 | 0e+00 | 48/48 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +24.4 | 0e+00 | 42/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +15.5 | 0e+00 | 39/45 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +10.1 | 1e-21 | 39/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +9.5 | 4e-19 | 34/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.40×** | +9.0 | 2e-17 | 33/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.35×** | +8.1 | 5e-14 | 32/50 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +7.8 | 3e-13 | 33/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +7.2 | 3e-11 | 28/48 (PANC-1, SW48, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.19× | +7.0 | 2e-10 | 22/49 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 2e-08 | 29/48 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.17× | +6.2 | 4e-08 | 19/48 (NCI-H1792, C32, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.24×** | +6.0 | 8e-08 | 26/48 (LOX-IMVI, C32, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +6.0 | 8e-08 | 26/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.49×** | +5.7 | 4e-07 | 28/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.6 | 1e-04 | 10/48 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +4.3 | 5e-04 | 19/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.34×** | +4.2 | 9e-04 | 18/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +4.1 | 0.001 | 14/48 (CFPAC-1, KATO III, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.002 | 13/49 (C32, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.15× | +3.9 | 0.003 | 10/48 (NCI-H2030, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.003 | 14/48 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.14× | +3.5 | 0.011 | 7/48 (SW480, Hs 766T, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.018 | 6/48 (NCI-H460, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3833.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -10.2 | 9e-22 | 31/48 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.767×** | -7.4 | 4e-11 | 30/48 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.785×** | -6.7 | 3e-09 | 24/48 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.789×** | -6.6 | 5e-09 | 24/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.899× | -4.2 | 0.003 | 4/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.878× | -3.6 | 0.026 | 11/47 (NCI-H2030, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.840× | -3.6 | 0.026 | 17/48 (CHP-212, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | 0.922× | -3.2 | 0.088 | 4/49 (AsPC-1, J82, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.871× | -3.2 | 0.088 | 10/47 (CHP-212, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.894× | -3.1 | 0.088 | 10/47 (SNU-1, RKO, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.854× | -3.1 | 0.088 | 12/48 (Hs 766T, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.895× | -3.1 | 0.090 | 4/48 (KATO III, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 73.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +18.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 70.0 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.21× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.571× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 74.8 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +10.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.480× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.486× (z -9.7) |
| [[LS 180 (line)]] | wt | 66.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +14.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.435× (z -9.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 110 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.639× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 53.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +13.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 56.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.77× (z +12.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.445× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 57.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +11.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.423× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 55.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +17.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 52.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 56.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +15.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 122 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +16.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 43.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 57.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.13× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 48.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 70.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +10.8) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 78.3 | 0 | 2 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0988× (z -9.5) |
| [[COLO 205 (line)]] | alt | 45.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.304× (z -9.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 98.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 50.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +11.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 61.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 68.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +14.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 44.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +14.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 52.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +11.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 61.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +15.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 69.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 88.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 95.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.10× (z +13.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.489× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 80.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +10.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.369× (z -10.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 53.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 70.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +14.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +12.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 63.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 77.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 62.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS7L]] | +0.68 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[SF3A3]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[LARS1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[DDX1]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[PDAP1]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[MAGOHB]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[IPO8]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LMBRD2]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DNAJC10]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[NUP205]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[FARSB]] | +0.59 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[HNRNPR]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM38]] | -0.63 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[IP6K2]] | -0.63 | -0.43 / -0.73 | both halves | 3e-05 |  |
| [[MIEN1]] | -0.62 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[PRKD2]] | -0.59 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[MAP2K7]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ATP6V0C]] | -0.57 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[IER5L]] | -0.57 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[SNN]] | -0.56 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[PIAS4]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[UXT]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[COPS9]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.55 | -0.41 / -0.59 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GABARAPL2]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.7, -25.3); signed map (-5.3, -38.2). **Vector** length 113, 29.8% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +27.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.0 | +3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +7.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +4.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.4 | -10.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.0 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.2 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | -7.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.1 | -3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.8 | -2.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -3.7 | -3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.5 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin C-terminal hydrolase L5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.2 — chr1:193,012,250-193,060,080 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UCH37, CGI-70, INO80R |
| Gene groups (HGNC) | INO80 complex subunits; Ubiquitin C-terminal hydrolases |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 6 pathways, smallest: Downregulation of TGF-beta receptor signaling; TGF-beta receptor signaling activates SMADs; UCH proteinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5K5](https://www.uniprot.org/uniprotkb/Q9Y5K5) (Ubiquitin carboxyl-terminal hydrolase isozyme L5):

> Protease that specifically cleaves 'Lys-48'-linked polyubiquitin chains. Deubiquitinating enzyme associated with the 19S regulatory subunit of the 26S proteasome. Putative regulatory component of the INO80 complex; however is inactive in the INO80 complex and is activated by a transient interaction of the INO80 complex with the proteasome via ADRM1.

**Summary**, from NCBI Gene [51377](https://www.ncbi.nlm.nih.gov/gene/51377):

> Enables cysteine-type deubiquitinase activity; endopeptidase inhibitor activity; and proteasome binding activity. Involved in several processes, including negative regulation of proteasomal ubiquitin-dependent protein catabolic process; positive regulation of smoothened signaling pathway; and regulation of DNA metabolic process. Located in cytosol and nuclear lumen. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19678](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19678) · Entrez [51377](https://www.ncbi.nlm.nih.gov/gene/51377) · UniProt [Q9Y5K5](https://www.uniprot.org/uniprotkb/Q9Y5K5) · Ensembl [ENSG00000116750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116750)

## Data

Gene col 3833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3833); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3833]; `tensor/DDL_lfc|DDL_z.npy` [3833]; `embed/gene_vectors.npy` [3833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3833 or target_col == 3833). Every well: [[UCHL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UCHL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
