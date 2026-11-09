---
symbol: "PCBP3"
type: "gene"
col: 11417
ensembl_id: "ENSG00000183570"
name: "poly(rC) binding protein 3"
location: "21q22.3"
module: 13
arm: "+"
pooled_cpm: 145.81
n_lines_expressing: 28
n_dd_up: 14
n_dd_down: 23
n_dd_up_clean: 14
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PCBP3

*poly(rC) binding protein 3* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.45× (z +16.2, q 0e+00, up in 24 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.525× (z -11.7, q 7e-29, down in 22 of 26 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CA12]] (+0.67, fdr 1e-05), [[LOX]] (+0.58, fdr 1e-05), [[ADGRB3]] (+0.57, fdr 1e-05); moves opposite to [[HNF4G]] (-0.50, fdr 2e-04), [[KLHL2P1]] (-0.49, fdr 3e-04), [[GALNT7]] (-0.49, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PDGFRB]] → it (grade B ⚠); 5 go from it, the strongest it → [[CCDC102B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +16.2 | 0e+00 | 24/26 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.43×** | +16.1 | 0e+00 | 23/26 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +10.2 | 5e-22 | 21/26 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +9.5 | 4e-19 | 15/26 (SW480, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +6.7 | 3e-09 | 13/27 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.38×** | +5.6 | 2e-06 | 19/25 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 2e-04 | 11/26 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +4.6 | 4e-04 | 18/26 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 6e-04 | 12/25 (LOX-IMVI, SNU-423, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.002 | 16/26 (A549, SNU-423, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 18/25 (SK-MEL-2, H4, …) | rises with dose | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.006 | 8/26 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.006 | 14/27 (SW480, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.006 | 11/26 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.010 | 7/26 (NCI-H1573, SW1417, …) | top dose only | composition shift |
| [[Quinestrol (drug)]] 5 µM |  | 1.14× | +3.4 | 0.023 | 12/27 (NCI-H1792, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.525×** | -11.7 | 7e-29 | 22/26 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.590×** | -9.6 | 2e-19 | 18/26 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.585×** | -9.4 | 1e-18 | 21/26 (NCI-H23, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -8.2 | 5e-14 | 21/25 (NCI-H1573, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.442×** | -7.7 | 1e-12 | 18/26 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.659×** | -7.6 | 3e-12 | 19/26 (SNU-423, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.678×** | -7.1 | 1e-10 | 19/26 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.482×** | -6.9 | 3e-10 | 23/27 (A-427, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.685×** | -6.9 | 4e-10 | 11/25 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.688×** | -6.8 | 6e-10 | 19/25 (HOP62, RPMI-7951, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.697×** | -6.3 | 2e-08 | 21/24 (SK-MEL-2, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -5.5 | 2e-06 | 16/26 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.738×** | -5.3 | 5e-06 | 20/25 (hTERT-HPNE, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.750×** | -5.2 | 6e-06 | 18/26 (HOP62, H4, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.758×** | -5.0 | 2e-05 | 17/26 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.763×** | -4.7 | 8e-05 | 12/26 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.780×** | -4.5 | 2e-04 | 12/26 (NCI-H460, NCI-H1573, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.802×** | -4.0 | 0.002 | 12/26 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **0.805×** | -4.0 | 0.002 | 8/26 (J82, NCI-H1573, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.869× | -3.6 | 0.007 | 11/26 (CHP-212, NCI-H1792, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.706×** | -3.3 | 0.023 | 10/26 (NCI-H460, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.024 | 10/25 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 919 | 0 | 21 (13 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.139× (z -16.2) |
| [[HOP62 (line)]] | alt | 595 | 1 (1 ⚠) | 16 (11 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +13.7) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.0799× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.119× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 463 | 0 | 14 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.199× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 300 | 0 | 13 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0763× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.169× (z -14.0) |
| [[H4 (line)]] | wt | 224 | 0 | 12 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.200× (z -12.5) |
| [[SNU-423 (line)]] | alt | 320 | 0 | 12 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -18.4) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -15.5) |
| [[A498 (line)]] | wt | 203 | 2 | 9 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.61× (z +11.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 141 | 9 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +28.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.62× (z +15.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.272× (z -12.3) ⚠ toxic |
| [[J82 (line)]] | alt | 105 | 4 (1 ⚠) | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.56× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[NCI-H23 (line)]] | alt | 120 | 3 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.90× (z +15.2) | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -22.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -9.9) |
| [[SW 900 (line)]] | alt | 259 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.328× (z -10.4) |
| [[SW480 (line)]] | alt | 91.7 | 6 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.57× (z +25.4) | [[Harringtonine (drug)]] 5 µM 0.404× (z -10.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.475× (z -8.8) |
| [[A-427 (line)]] | wt | 126 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.104× (z -13.0) |
| [[SHP-77 (line)]] | alt | 511 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.480× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 186 | 2 | 5 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.0623× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0600× (z -12.5) |
| [[SW1417 (line)]] | alt | 246 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[NCI-H1792 (line)]] | alt | 72.1 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.62× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -9.9) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.291× (z -8.9) |
| [[A549 (line)]] | wt | 62.9 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.23× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.197× (z -10.9) |
| [[CHP-212 (line)]] | wt | 301 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0717× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -12.2) |
| [[BT-474 (line)]] | alt | 37.0 | 3 | 0 | [[Auranofin (drug)]] 5 µM 5.26× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 67.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.54× (z +15.5) | — |
| [[CFPAC-1 (line)]] | alt | 39.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.63× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 59.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.52× (z +10.1) | — |
| [[NCI-H661 (line)]] | alt | 80.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0495× (z -11.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 23.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 26.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 31.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 34.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA12]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[LOX]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ADGRB3]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PRR16]] | +0.57 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[PC]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[C14orf132]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[TREM1]] | +0.52 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[KCTD16]] | +0.52 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[KCNJ6]] | +0.51 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[PTGFR]] | +0.51 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[ELL2]] | +0.50 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[ZNF471]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4G]] | -0.50 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[KLHL2P1]] | -0.49 | -0.45 / -0.29 | both halves | 3e-04 |  |
| [[GALNT7]] | -0.49 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[SLC44A3]] | -0.48 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[VSIG10]] | -0.47 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[IQCH-AS1]] | -0.47 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[TMCO4]] | -0.47 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[AMIGO2]] | -0.45 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[DMTN]] | -0.45 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[PLCL2]] | -0.45 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[KLHL42]] | -0.44 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[ITPKB]] | -0.44 | -0.28 / -0.32 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFRB]] | B | PDGFRB activity raises PCBP3's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 3.62× lower at baseline in the lines without PDGFRB | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[KCNE4]] | B | KCNE4 activity raises PCBP3's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.10× lower at baseline in the lines without KCNE4 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[WNT5A]] | C | WNT5A activity raises PCBP3's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 4.98× lower at baseline in the lines without WNT5A | 0.001 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[SDK1]] | C | SDK1 activity raises PCBP3's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 4.34× lower at baseline in the lines without SDK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3; co-absent with the target |
| [[KCNJ6]] | C | KCNJ6 activity raises PCBP3's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 4.15× lower at baseline in the lines without KCNJ6 | 0.016 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[DNER]] | C | DNER activity raises PCBP3's level | lines that do not express DNER (32) vs lines expressing it (18) | 3.52× lower at baseline in the lines without DNER | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |
| [[ENPP2]] | C | ENPP2 activity raises PCBP3's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 3.70× lower at baseline in the lines without ENPP2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[SCUBE1]] | C | SCUBE1 activity raises PCBP3's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 3.18× lower at baseline in the lines without SCUBE1 | 0.057 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |
| [[EPHA3]] | C | EPHA3 activity raises PCBP3's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 3.02× lower at baseline in the lines without EPHA3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC102B]] | B | PCBP3 activity raises CCDC102B's level | lines that do not express PCBP3 (22) vs lines expressing it (28) | 2.86× lower at baseline in the lines without PCBP3 | 0.094 | ⚠ within organs, on part of the lines; also absent: SDK1, RBM20, ANO4 |
| [[SDK1]] | C | PCBP3 activity raises SDK1's level | lines that do not express PCBP3 (22) vs lines expressing it (28) | 4.40× lower at baseline in the lines without PCBP3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SDK1, RBM20, ANO4; co-absent with the target |
| [[ADGRB3]] | C | PCBP3 activity raises ADGRB3's level | lines that do not express PCBP3 (22) vs lines expressing it (28) | 4.01× lower at baseline in the lines without PCBP3 | 0.067 | ⚠ within organs, on part of the lines; also absent: SDK1, RBM20, ANO4; co-absent with the target |
| [[C14orf132]] | C | PCBP3 activity raises C14orf132's level | lines that do not express PCBP3 (22) vs lines expressing it (28) | 3.20× lower at baseline in the lines without PCBP3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SDK1, RBM20, ANO4; co-absent with the target |
| [[WNT5A]] | C | PCBP3 activity raises WNT5A's level | lines that do not express PCBP3 (22) vs lines expressing it (28) | 4.51× lower at baseline in the lines without PCBP3 | 0.095 | ⚠ within organs, on part of the lines; also absent: SDK1, RBM20, ANO4; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.264). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.4, 20.8); signed map (27.7, 45.6). **Vector** length 114, 34.0% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | +6.3 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +5.3 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +16.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +16.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.7 | +2.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.4 | +4.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.3 | +4.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.3 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -7.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | poly(rC) binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:45,643,694-45,942,454 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ44028; previously PCBP3-OT1, PCBP3OT |
| Matched by | ensembl_id |

**Function**, from UniProt [P57721](https://www.uniprot.org/uniprotkb/P57721) (Poly(rC)-binding protein 3):

> Single-stranded nucleic acid binding protein that binds preferentially to oligo dC.

**Summary**, from NCBI Gene [54039](https://www.ncbi.nlm.nih.gov/gene/54039):

> This gene encodes a member of the KH-domain protein subfamily. Proteins of this subfamily, also referred to as alpha-CPs, bind to RNA with a specificity for C-rich pyrimidine regions. Alpha-CPs play important roles in post-transcriptional activities and have different cellular distributions. The protein encoded by this gene lacks the nuclear localization signals found in other subfamily members. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided …

**Accessions** — [HGNC:8651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8651) · Entrez [54039](https://www.ncbi.nlm.nih.gov/gene/54039) · UniProt [P57721](https://www.uniprot.org/uniprotkb/P57721) · Ensembl [ENSG00000183570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183570)

## Data

Gene col 11417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11417); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11417]; `tensor/DDL_lfc|DDL_z.npy` [11417]; `embed/gene_vectors.npy` [11417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11417 or target_col == 11417). Every well: [[PCBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
