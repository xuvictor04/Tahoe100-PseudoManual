---
symbol: "FOXO1"
type: "gene"
col: 7467
ensembl_id: "ENSG00000150907"
name: "forkhead box O1"
location: "13q14.11"
module: 97
arm: "+"
pooled_cpm: 146.12
n_lines_expressing: 43
n_dd_up: 19
n_dd_down: 20
n_dd_up_clean: 18
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 8
direction_downstream: 2
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# FOXO1

*forkhead box O1* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +11.4, q 4e-27, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.393× (z -17.9, q 0e+00, down in 39 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.419× (z -8.7, q 3e-16, down in 33 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00598]] (+0.74, fdr 7e-06, ⚠ same locus), [[TCF7L2]] (+0.65, fdr 2e-05), [[AKAP13]] (+0.62, fdr 2e-05), [[KIF13B]] (+0.62, fdr 4e-05); moves opposite to [[LINC01605]] (-0.47, fdr 4e-05), [[ZCCHC4]] (-0.46, fdr 9e-05), [[RPTOR]] (-0.44, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CYP3A5]] → it (grade B ⚠); 2 go from it, the strongest it → [[GAREM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7467.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +11.4 | 4e-27 | 25/41 (BT-474, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +10.4 | 9e-23 | 26/41 (PANC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +9.9 | 1e-20 | 30/41 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +9.1 | 1e-17 | 27/41 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +8.1 | 6e-14 | 30/41 (RKO, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +7.7 | 9e-13 | 27/41 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +7.7 | 9e-13 | 25/41 (J82, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +7.3 | 2e-11 | 25/41 (J82, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +6.4 | 1e-08 | 27/41 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.3 | 1e-08 | 26/41 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.3 | 2e-08 | 24/42 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +6.0 | 9e-08 | 25/41 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.2 | 1e-05 | 20/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 5e-05 | 16/41 (RPMI-7951, HS-578T, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +4.7 | 1e-04 | 19/42 (PANC-1, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.007 | 18/41 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7467.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.393×** | -17.9 | 0e+00 | 39/42 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -17.0 | 0e+00 | 33/37 (Panc 03.27, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.498×** | -12.4 | 8e-33 | 32/38 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.614×** | -9.4 | 1e-18 | 33/41 (AsPC-1, SW48, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.419×** | -8.7 | 3e-16 | 33/41 (HEC-1-A, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.454×** | -7.9 | 2e-13 | 34/41 (AsPC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.516×** | -6.6 | 2e-09 | 32/41 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.710×** | -6.6 | 4e-09 | 31/41 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[EX229 (drug)]] 5 µM |  | **0.562×** | -5.8 | 5e-07 | 28/41 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.764×** | -5.2 | 1e-05 | 28/41 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.764×** | -5.0 | 4e-05 | 25/40 (Hs 766T, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.616×** | -4.9 | 5e-05 | 26/40 (A549, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -4.7 | 1e-04 | 1/43 (NCI-H2122) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.644×** | -4.4 | 4e-04 | 23/41 (SW48, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.666×** | -4.1 | 0.002 | 16/33 (BT-474, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -3.6 | 0.012 | 17/41 (Hs 766T, NCI-H661, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.833×** | -3.5 | 0.013 | 16/41 (HepG2/C3A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.824×** | -3.5 | 0.013 | 15/41 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -3.4 | 0.023 | 17/41 (LoVo, RKO, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.768×** | -3.2 | 0.037 | 15/42 (Hs 766T, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.057 | 14/41 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.781×** | -3.0 | 0.068 | 10/41 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.782×** | -3.0 | 0.068 | 14/41 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 36.6 | 13 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 5.22× (z +10.5) | — |
| [[A498 (line)]] | wt | 129 | 9 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -13.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 830 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0730× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.6) |
| [[SW1417 (line)]] | alt | 219 | 5 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -20.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 58.4 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -11.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 76.4 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +21.9) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -9.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 70.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.6) | — |
| [[Panc 03.27 (line)]] | alt | 306 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.0177× (z -47.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 61.9 | 2 | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.80× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.489× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 499 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -19.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -8.7) |
| [[HS-578T (line)]] | alt | 78.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.8) | — |
| [[LoVo (line)]] | wt | 607 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -19.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 433 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0879× (z -26.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 89.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.58× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 317 | 1 | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 7.85× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0767× (z -20.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 109 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -8.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 93.5 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -12.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 300 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.341× (z -9.6) |
| [[HT-29 (line)]] | alt | 380 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -14.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 74.9 | 1 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.39× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.427× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 66.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 150 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -12.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 37.7 | 2 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 3.35× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 115 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 89.8 | 3 | 0 | [[Clobetasol propionate (drug)]] 5 µM 2.47× (z +9.2) | — |
| [[SW480 (line)]] | alt | 105 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -22.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 49.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.1) |
| [[A549 (line)]] | wt | 105 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.87× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -10.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0814× (z -13.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 109 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.9) | — |
| [[CHP-212 (line)]] | wt | 99.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 86.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -18.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 85.5 | 1 | 0 | [[Panobinostat (drug)]] 0.05 µM 2.51× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 87.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 56.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -12.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.5 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 33.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00598]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 | ⚠ same locus (19.9 kb, same strand: neighbours can correlate without regulation) |
| [[TCF7L2]] | +0.65 | +0.47 / +0.66 | both halves | 2e-05 | STRING 589 |
| [[AKAP13]] | +0.62 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[KIF13B]] | +0.62 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[TBC1D8]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[PPP3CA]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[GAREM1]] | +0.59 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[EPS8]] | +0.58 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[KLF5]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TGFBR3]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ID1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 | STRING 438 |
| [[PELI1]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[DENND3]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01605]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZCCHC4]] | -0.46 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[RPTOR]] | -0.44 | -0.34 / -0.47 | both halves | 1e-04 | pathway: Intracellular signaling by second messengers; STRING 634 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP3A5]] | B | CYP3A5 activity raises FOXO1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.69× lower at baseline in the lines without CYP3A5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[SHROOM3]] | B | SHROOM3 activity raises FOXO1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without SHROOM3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[GAREM1]] | B | GAREM1 activity raises FOXO1's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 2.61× lower at baseline in the lines without GAREM1 | 0.035 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[C4BPB]] | B | C4BPB activity weakens FOXO1's drug response | lines that do not express C4BPB (31) vs lines expressing it (11) | the lines without C4BPB respond 1.20× as strongly (z diff -0.32); strongest at Homoharringtonine 5 µM: 1.64x vs 1.07x (z diff -5.7) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4; target measured in part of the lines; both ways; artifact flags |
| [[CYP3A5]] | B | CYP3A5 activity weakens FOXO1's drug response | lines that do not express CYP3A5 (26) vs lines expressing it (16) | the lines without CYP3A5 respond 1.03× as strongly (z diff -0.09); strongest at Belinostat 5 µM: 1.75x vs 1.11x (z diff -3.9) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A; target measured in part of the lines; both ways; artifact flags |
| [[C4BPB]] | B | C4BPB activity raises FOXO1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.79× lower at baseline in the lines without C4BPB | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[KLF5]] | B | KLF5 activity raises FOXO1's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.30× lower at baseline in the lines without KLF5 | 0.084 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises FOXO1's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without TJP2 | 0.086 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAREM1]] | B | FOXO1 activity raises GAREM1's level | lines that do not express FOXO1 (7) vs lines expressing it (43) | 2.85× lower at baseline in the lines without FOXO1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000288542, LINC00598; maybe low, not absent |
| [[LINC00598]] | C | FOXO1 activity raises LINC00598's level | lines that do not express FOXO1 (7) vs lines expressing it (43) | 3.02× lower at baseline in the lines without FOXO1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000288542, LINC00598; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.4, 47.4); signed map (11.1, 32.8). **Vector** length 120, 36.4% of its response variance represented; |z| ≥ 3 in 1,447 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.8 | +7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +4.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +3.6 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.4 | +4.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.4 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.4 | -9.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.3 | -8.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.7 | -7.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.3 | -6.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box O1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:40,555,667-40,666,641 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FKH1; previously FKHR, FOXO1A |
| Gene groups (HGNC) | Forkhead boxes |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 20 pathways, smallest: AKT-mediated inactivation of FOXO1A; Regulation of gene expression in beta cells; AKT phosphorylates targets in the nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12778](https://www.uniprot.org/uniprotkb/Q12778) (Forkhead box protein O1):

> Transcription factor that is the main target of insulin signaling and regulates metabolic homeostasis in response to oxidative stress. Binds to the insulin response element (IRE) with consensus sequence 5'-TT[G/A]TTTTG-3' and the related Daf-16 family binding element (DBE) with consensus sequence 5'-TT[G/A]TTTAC-3'. Activity suppressed by insulin. Main regulator of redox balance and osteoblast numbers and controls bone mass (By similarity). Orchestrates the endocrine function of the skeleton in …

**Summary**, from NCBI Gene [2308](https://www.ncbi.nlm.nih.gov/gene/2308):

> This gene belongs to the forkhead family of transcription factors which are characterized by a distinct forkhead domain. The specific function of this gene has not yet been determined; however, it may play a role in myogenic growth and differentiation. Translocation of this gene with PAX3 has been associated with alveolar rhabdomyosarcoma. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3819) · Entrez [2308](https://www.ncbi.nlm.nih.gov/gene/2308) · UniProt [Q12778](https://www.uniprot.org/uniprotkb/Q12778) · Ensembl [ENSG00000150907](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150907)

## Data

Gene col 7467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7467); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7467]; `tensor/DDL_lfc|DDL_z.npy` [7467]; `embed/gene_vectors.npy` [7467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7467 or target_col == 7467). Every well: [[FOXO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
