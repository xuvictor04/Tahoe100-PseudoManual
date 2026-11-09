---
symbol: "RSPRY1"
type: "gene"
col: 8260
ensembl_id: "ENSG00000159579"
name: "ring finger and SPRY domain containing 1"
location: "16q13"
module: 11
arm: "+"
pooled_cpm: 83.34
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RSPRY1

*ring finger and SPRY domain containing 1* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +25.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.503× (z -18.2, q 0e+00, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.744× (z -8.2, q 5e-14, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCD7]] (+0.67, fdr 1e-05), [[LINS1]] (+0.66, fdr 7e-06), [[METTL25B]] (+0.64, fdr 1e-05); moves opposite to [[MAPK9]] (-0.62, fdr 1e-05), [[GSR]] (-0.61, fdr 1e-05), [[BLMH]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +25.9 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +20.9 | 0e+00 | 44/49 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.11×** | +20.3 | 0e+00 | 46/49 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +14.7 | 0e+00 | 42/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +12.2 | 6e-32 | 38/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +10.9 | 8e-26 | 37/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +8.3 | 9e-15 | 31/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.5 | 6e-09 | 28/48 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.6 | 1e-06 | 23/50 (SK-MEL-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.7 | 0.014 | 15/48 (HEC-1-A, J82, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.14× | +3.6 | 0.014 | 2/49 (HCT15, SW 1088) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.13× | +3.2 | 0.052 | 16/48 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.2 | 0.052 | 0/48 | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.12× | +3.1 | 0.081 | 4/49 (SNU-423, BT-474, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.094 | 6/48 (Hs 766T, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -18.2 | 0e+00 | 37/44 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.599×** | -14.1 | 6e-43 | 40/49 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.589×** | -13.5 | 3e-39 | 37/45 (A-172, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.744×** | -8.2 | 5e-14 | 38/48 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.767×** | -6.9 | 5e-10 | 30/48 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.780×** | -6.9 | 6e-10 | 27/48 (C32, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.813×** | -5.7 | 9e-07 | 28/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.874× | -5.3 | 9e-06 | 16/48 (SW480, SW 900, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.849× | -4.4 | 8e-04 | 20/48 (J82, NCI-H1792, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.857× | -4.3 | 0.001 | 14/48 (HCT15, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -4.2 | 0.001 | 16/49 (RPMI-7951, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.859× | -4.2 | 0.001 | 17/48 (RKO, A549, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 0.866× | -4.0 | 0.003 | 13/48 (hTERT-HPNE, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.868× | -3.9 | 0.003 | 13/48 (NCI-H2030, SNU-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.874× | -3.7 | 0.007 | 21/48 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.912× | -3.6 | 0.010 | 7/48 (AsPC-1, RKO, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.798×** | -3.3 | 0.034 | 11/48 (BT-474, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | 0.922× | -3.2 | 0.042 | 1/48 (AsPC-1) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.923× | -3.2 | 0.045 | 2/48 (HS-578T, H4) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 0.901× | -3.0 | 0.066 | 8/49 (A-172, HS-578T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 109 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +23.8) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -22.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 61.5 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 79.3 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -13.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 102 | 5 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +23.0) | [[Bortezomib (drug)]] 0.05 µM 0.434× (z -9.5) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.460× (z -9.4) |
| [[A498 (line)]] | wt | 166 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +16.4) | [[Dinaciclib (drug)]] 0.05 µM 0.470× (z -10.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 112 | 4 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -19.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 87.5 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +22.1) | [[Dinaciclib (drug)]] 5 µM 0.473× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 64.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +30.7) | — |
| [[SW480 (line)]] | alt | 107 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.42× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -16.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 61.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 85.7 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +13.8) | [[Ixazomib citrate (drug)]] 5 µM 0.482× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 60.2 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -20.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 68.2 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +10.2) | [[Lonafarnib (drug)]] 5 µM 0.0708× (z -16.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 78.2 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.24× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -20.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 82.6 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -9.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 55.9 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.8) | [[Lonafarnib (drug)]] 5 µM 0.109× (z -10.9) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 76.1 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -18.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 66.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -13.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 79.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +15.0) | — |
| [[NCI-H1792 (line)]] | alt | 65.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 76.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0364× (z -37.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 74.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -9.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 94.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0428× (z -26.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 43.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -10.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 55.7 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.92× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 53.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +13.7) | — |
| [[RKO (line)]] | wt | 111 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -12.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 75.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -12.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 74.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.461× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Alpelisib (drug)]] 5 µM 0.165× (z -9.8) |
| [[J82 (line)]] | alt | 57.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.1) | — |
| [[NCI-H2030 (line)]] | alt | 154 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +19.1) | — |
| [[SHP-77 (line)]] | alt | 59.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 50.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.9) | — |
| [[SNU-1 (line)]] | wt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -18.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 75.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.450× (z -8.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.8) | — |
| [[KATO III (line)]] | alt | 83.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 49.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.5) | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.106× (z -9.1) |
| [[SW48 (line)]] | wt | 47.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD7]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[LINS1]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[METTL25B]] | +0.64 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TOGARAM1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ZNF324]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PEX13]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[MYNN]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SYNRG]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[GPANK1]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[NFX1]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 | same gene group |
| [[YIPF5]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ZNF451]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | -0.62 | -0.71 / -0.52 | both halves | 1e-05 |  |
| [[GSR]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[BLMH]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ANKRD52]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[PACC1]] | -0.57 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[NCKAP1]] | -0.57 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[CHORDC1]] | -0.57 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[C1orf216]] | -0.56 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[CACYBP]] | -0.56 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[SOAT1]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SORD]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CHRNA5]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RSPRY1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises RSPRY1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF585A]] | B | ZNF585A activity raises RSPRY1's level | lines that do not express ZNF585A (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without ZNF585A | 0.099 | ⚠ within organs, on part of the lines; also absent: ZFP14, WWTR1, ZNF540 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.391). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.3, 2.1); signed map (-8.9, -2.4). **Vector** length 118, 34.2% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +20.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +20.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +14.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +25.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +12.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +0.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +2.0 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -9.6 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.4 | -5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -7.2 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.7 | -13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.8 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | ring finger and SPRY domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:57,186,137-57,240,469 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1972 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

UniProt [Q96DX4](https://www.uniprot.org/uniprotkb/Q96DX4) carries no function annotation.

**Summary**, from NCBI Gene [89970](https://www.ncbi.nlm.nih.gov/gene/89970):

> This gene encodes a glycoprotein that contains a RING-type zinc finger domain and an SPRY domain of unknown function. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:29420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29420) · Entrez [89970](https://www.ncbi.nlm.nih.gov/gene/89970) · UniProt [Q96DX4](https://www.uniprot.org/uniprotkb/Q96DX4) · Ensembl [ENSG00000159579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159579)

## Data

Gene col 8260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8260); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8260]; `tensor/DDL_lfc|DDL_z.npy` [8260]; `embed/gene_vectors.npy` [8260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8260 or target_col == 8260). Every well: [[RSPRY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSPRY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
