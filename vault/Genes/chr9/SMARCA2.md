---
symbol: "SMARCA2"
type: "gene"
col: 1282
ensembl_id: "ENSG00000080503"
name: "SWI/SNF related BAF chromatin remodeling complex subunit ATPase 2"
location: "9p24.3"
module: 130
arm: "+"
pooled_cpm: 79.59
n_lines_expressing: 44
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# SMARCA2

*SWI/SNF related BAF chromatin remodeling complex subunit ATPase 2* — 9p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +17.4, q 0e+00, up in 33 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.490× (z -14.8, q 0e+00, down in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.616× (z -10.1, q 2e-21, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LASP1]] (+0.50, fdr 1e-04), [[UTRN]] (+0.49, fdr 2e-05), [[CEP57]] (+0.48, fdr 3e-05); moves opposite to [[RRP1]] (-0.49, fdr 4e-05), [[COA4]] (-0.46, fdr 4e-04), [[GATD1]] (-0.46, fdr 2e-04).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADD3]] → it (grade B ⚠); 9 go from it, the strongest it → [[RRP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +17.4 | 0e+00 | 33/42 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +13.4 | 2e-38 | 32/43 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +6.6 | 1e-08 | 27/42 (RKO, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +6.1 | 1e-07 | 31/42 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +5.3 | 1e-05 | 29/42 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +5.3 | 1e-05 | 21/42 (RKO, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.1 | 3e-05 | 25/42 (SW48, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +4.9 | 7e-05 | 20/42 (NCI-H2030, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +4.8 | 9e-05 | 23/42 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +4.7 | 1e-04 | 22/43 (LoVo, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +4.3 | 7e-04 | 19/42 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.0 | 0.003 | 13/42 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.003 | 20/42 (A549, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +4.0 | 0.003 | 18/42 (NCI-H2030, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.003 | 22/42 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.9 | 0.003 | 13/42 (SNU-1, A549, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.004 | 20/42 (KATO III, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.006 | 14/42 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.025 | 13/41 (SW480, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1282.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.490×** | -14.8 | 0e+00 | 36/42 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.593×** | -10.8 | 9e-25 | 37/42 (SNU-423, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.616×** | -10.1 | 2e-21 | 27/42 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.626×** | -9.4 | 1e-18 | 34/41 (HT-29, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -8.5 | 2e-15 | 27/42 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.481×** | -8.0 | 2e-13 | 31/43 (Hs 766T, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.684×** | -7.9 | 3e-13 | 29/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[EX229 (drug)]] 5 µM |  | **0.502×** | -7.5 | 4e-12 | 31/42 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.502×** | -7.5 | 4e-12 | 28/42 (SW480, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.506×** | -7.4 | 8e-12 | 34/42 (SW 900, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.517×** | -7.2 | 4e-11 | 32/42 (COLO 205, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.518×** | -7.1 | 4e-11 | 35/42 (SW 900, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -7.1 | 4e-11 | 28/42 (A498, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.731×** | -6.5 | 3e-09 | 29/42 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.591×** | -5.7 | 4e-07 | 23/31 (HT-29, H4, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.601×** | -5.5 | 1e-06 | 25/42 (RKO, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.723×** | -4.8 | 5e-05 | 25/42 (NCI-H460, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.746×** | -4.3 | 4e-04 | 25/42 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.762×** | -4.0 | 0.002 | 22/43 (Hs 766T, RPMI-7951, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 108 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.363× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.465× (z -12.3) |
| [[HS-578T (line)]] | alt | 117 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -12.1) |
| [[Hs 766T (line)]] | wt | 109 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -15.6) |
| [[KATO III (line)]] | alt | 132 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.417× (z -12.1) |
| [[HT-29 (line)]] | alt | 136 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.475× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 81.9 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +15.6) | [[Digitoxin (drug)]] 5 µM 0.314× (z -10.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 84.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +22.2) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[RKO (line)]] | wt | 99.9 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.8) | [[PH-797804 (drug)]] 5 µM 0.156× (z -10.1) |
| [[SNU-423 (line)]] | alt | 99.3 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.388× (z -10.3) |
| [[A549 (line)]] | wt | 57.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.353× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.401× (z -9.3) |
| [[HOP62 (line)]] | alt | 49.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +17.7) | [[Digitoxin (drug)]] 5 µM 0.243× (z -13.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 126 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.412× (z -11.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 180 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +21.4) | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.74× (z +12.0) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[NCI-H460 (line)]] | wt | 62.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +20.6) | — |
| [[PANC-1 (line)]] | alt | 24.4 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.284× (z -12.3) |
| [[SW48 (line)]] | wt | 140 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.4) | — |
| [[A498 (line)]] | wt | 189 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.339× (z -14.6) |
| [[AN3 CA (line)]] | alt | 75.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.0) | [[Harringtonine (drug)]] 0.5 µM 0.165× (z -9.8) |
| [[C32 (line)]] | wt | 64.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +15.9) | — |
| [[COLO 205 (line)]] | alt | 136 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 164 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +18.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -11.8) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 92.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.391× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.451× (z -9.0) |
| [[SW 900 (line)]] | alt | 88.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.7) | [[TAK-733 (drug)]] 5 µM 0.202× (z -8.8) |
| [[SW1417 (line)]] | alt | 110 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.419× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 34.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 33.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +17.0) | — |
| [[HCT15 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.416× (z -9.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 117 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.339× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 78.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.312× (z -9.4) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +15.1) | — |
| [[NCI-H1792 (line)]] | alt | 37.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +19.2) | — |
| [[NCI-H596 (line)]] | alt | 74.2 | 1 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 5.11× (z +8.5) ⚠ cell-cycle shift, explains ~7% of this change | — |
| [[RPMI-7951 (line)]] | alt | 89.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.8) | — |
| [[SHP-77 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.374× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 47.2 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.0630× (z -9.9) |
| [[A-172 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 80.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.98 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LASP1]] | +0.50 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[UTRN]] | +0.49 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[CEP57]] | +0.48 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[MAGI3]] | +0.48 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[PDCD4]] | +0.47 | +0.23 / +0.55 | both halves | 5e-04 |  |
| [[NSD3]] | +0.47 | +0.40 / +0.44 | both halves | 4e-05 | pathway: Chromatin modifying enzymes; STRING 425 |
| [[WNK1]] | +0.47 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[CNOT6L]] | +0.46 | +0.22 / +0.52 | both halves | 6e-04 |  |
| [[TAX1BP1]] | +0.46 | +0.25 / +0.53 | both halves | 4e-04 |  |
| [[CCDC186]] | +0.45 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[UBL3]] | +0.44 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[AASS]] | +0.44 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[COA4]] | -0.46 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[GATD1]] | -0.46 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[ZNF512]] | -0.45 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[ZNF112]] | -0.45 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[TMEM177]] | -0.45 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[MTG1]] | -0.44 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[PINX1-1]] | -0.44 | -0.41 / -0.24 | both halves | 5e-04 |  |
| [[MCM3AP-AS1]] | -0.44 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[VPS37C]] | -0.43 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CTU1]] | -0.43 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[FARSA]] | -0.42 | -0.31 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity raises SMARCA2's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.78× lower at baseline in the lines without ADD3 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[UBL3]] | C | UBL3's natural level strengthens SMARCA2's drug response | UBL3's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.69, reverse -0.15; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRP1]] | B | SMARCA2 activity lowers RRP1's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.38× higher at baseline in the lines without SMARCA2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[CADPS2]] | B | SMARCA2 activity raises CADPS2's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 4.64× lower at baseline in the lines without SMARCA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[RFT1]] | B | SMARCA2 activity lowers RFT1's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.35× higher at baseline in the lines without SMARCA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[ALDH1B1]] | B | SMARCA2 activity lowers ALDH1B1's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.78× higher at baseline in the lines without SMARCA2 | 0.048 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[NPIPB14P]] | B | SMARCA2 activity raises NPIPB14P's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without SMARCA2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[WNK1]] | B | SMARCA2 activity lowers WNK1's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.68× higher at baseline in the lines without SMARCA2 | 0.084 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[UMPS]] | B | SMARCA2 activity lowers UMPS's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.31× higher at baseline in the lines without SMARCA2 | 0.086 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| cells under [[BAY1125976 (drug)]] 0.5 µM | B | SMARCA2 activity lowers the cells' numbers under BAY1125976 0.5 µM (makes them more sensitive) | lines that do not express SMARCA2 (6) vs lines expressing it (42) | the lines without SMARCA2: 1.37× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 5 µM | B | SMARCA2 activity lowers the cells' numbers under 18β-Glycyrrhetinic acid 5 µM (makes them more sensitive) | lines that do not express SMARCA2 (6) vs lines expressing it (42) | the lines without SMARCA2: 1.22× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.333). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.0, -50.0); signed map (-12.2, 12.8). **Vector** length 105, 28.5% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +17.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | -1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +13.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.5 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.4 | -9.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.8 | -10.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -7.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -7.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.6 | -7.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -7.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | SWI/SNF related BAF chromatin remodeling complex subunit ATPase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.3 — chr9:1,980,290-2,193,624 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAF190, hSNF2a, hBRM, Sth1p, SNF2LA, BRM, SNF2, SWI2; previously SNF2L2 |
| Gene groups (HGNC) | SNF2 related family; Bromodomain containing; BAF complex subunits; GBAF complex subunits |
| Reactome | 21 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; Formation of the canonical BAF (cBAF) complex; Formation of the polybromo-BAF (pBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P51531](https://www.uniprot.org/uniprotkb/P51531) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A member 2):

> ATPase involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Binds DNA non-specifically. Belongs to the neural progenitors-specific chromatin remodeling complex (npBAF complex) and the neuron-specific chromatin …

**Summary**, from NCBI Gene [6595](https://www.ncbi.nlm.nih.gov/gene/6595):

> The protein encoded by this gene is a member of the SWI/SNF family of proteins and is highly similar to the brahma protein of Drosophila. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI, which is required for transcriptional activation of genes normally repressed by chromatin. …

**Accessions** — [HGNC:11098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11098) · Entrez [6595](https://www.ncbi.nlm.nih.gov/gene/6595) · UniProt [P51531](https://www.uniprot.org/uniprotkb/P51531) · Ensembl [ENSG00000080503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080503)

## Data

Gene col 1282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1282); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1282]; `tensor/DDL_lfc|DDL_z.npy` [1282]; `embed/gene_vectors.npy` [1282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1282 or target_col == 1282). Every well: [[SMARCA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
