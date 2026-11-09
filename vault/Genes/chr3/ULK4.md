---
symbol: "ULK4"
type: "gene"
col: 9586
ensembl_id: "ENSG00000168038"
name: "unc-51 like kinase 4"
location: "3p22.1"
module: 185
arm: "+"
pooled_cpm: 62.01
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 21
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# ULK4

*unc-51 like kinase 4* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.06× (z +21.2, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.483× (z -10.6, q 1e-23, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFT43]] (+0.70, fdr 7e-06), [[CDKAL1]] (+0.69, fdr 7e-06), [[IPO11]] (+0.64, fdr 2e-05); moves opposite to [[NPL]] (-0.53, fdr 8e-05), [[TCEANC]] (-0.49, fdr 2e-04), [[ZNF385C]] (-0.49, fdr 9e-05).
> It is in [[Module 185]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.06×** | +21.2 | 0e+00 | 47/47 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.33×** | +18.2 | 0e+00 | 47/47 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.18×** | +17.5 | 0e+00 | 46/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +8.2 | 5e-14 | 41/47 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +6.5 | 1e-08 | 35/47 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.16×** | +6.1 | 1e-07 | 38/48 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.48×** | +5.6 | 2e-06 | 30/47 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.8 | 9e-05 | 25/47 (HEC-1-A, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +4.4 | 5e-04 | 24/47 (HOP62, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.041 | 17/46 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.043 | 18/47 (SW1417, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.043 | 17/47 (A498, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.055 | 14/49 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.059 | 12/47 (RPMI-7951, C32, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.23×** | +3.1 | 0.064 | 18/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.064 | 13/47 (PANC-1, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.069 | 14/48 (HEC-1-A, SW48, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9586.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.483×** | -10.6 | 1e-23 | 38/47 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.695×** | -7.8 | 2e-12 | 35/47 (HS-578T, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.601×** | -7.7 | 2e-12 | 30/47 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -7.7 | 2e-12 | 34/47 (C-33 A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.640×** | -6.7 | 2e-09 | 28/47 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.671×** | -5.8 | 5e-07 | 28/48 (NCI-H23, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.764×** | -5.8 | 7e-07 | 34/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.689×** | -5.6 | 1e-06 | 30/47 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.690×** | -5.4 | 4e-06 | 27/47 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **0.715×** | -5.1 | 2e-05 | 26/47 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.725×** | -4.9 | 6e-05 | 22/47 (RKO, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.733×** | -4.7 | 1e-04 | 30/47 (SNU-1, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -4.7 | 1e-04 | 28/46 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.767×** | -4.0 | 0.002 | 23/47 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.765×** | -3.9 | 0.004 | 21/43 (NCI-H23, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.768×** | -3.9 | 0.004 | 21/47 (NCI-H2030, LS 180, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.021 | 21/46 (LS 180, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.022 | 22/46 (SW480, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.801×** | -3.1 | 0.049 | 18/46 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vilanterol (drug)]] 5 µM |  | 0.868× | -3.0 | 0.061 | 11/48 (C-33 A, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 109 | 1 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +9.4) | [[Harringtonine (drug)]] 5 µM 0.183× (z -14.8) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.232× (z -12.8) |
| [[SW480 (line)]] | alt | 119 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +13.5) | [[Auranofin (drug)]] 5 µM 0.408× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 176 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +11.0) | [[Harringtonine (drug)]] 5 µM 0.316× (z -12.2) ⚠ cell-cycle shift, explains ~65% of this change |
| [[J82 (line)]] | alt | 70.3 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.56× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 34.4 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.77× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0931× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.294× (z -8.9) |
| [[A-427 (line)]] | wt | 105 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.377× (z -10.1) |
| [[A498 (line)]] | wt | 41.1 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -13.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.220× (z -12.7) |
| [[C32 (line)]] | wt | 62.4 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 4.64× (z +12.6) | [[Harringtonine (drug)]] 0.5 µM 0.288× (z -9.9) |
| [[LoVo (line)]] | wt | 40.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.65× (z +13.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 57.9 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.55× (z +10.9) | [[Harringtonine (drug)]] 0.5 µM 0.200× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 40.9 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.08× (z +15.1) | [[Digitoxin (drug)]] 5 µM 0.327× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.389× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 60.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.19× (z +16.6) | — |
| [[LOX-IMVI (line)]] | wt | 54.4 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.76× (z +12.4) | [[Harringtonine (drug)]] 0.5 µM 0.288× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 50.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.38× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 23.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.63× (z +15.4) | — |
| [[Panc 03.27 (line)]] | alt | 40.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.95× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 59.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.77× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -9.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 87.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.06× (z +11.9) | [[Harringtonine (drug)]] 0.5 µM 0.327× (z -9.2) |
| [[SNU-1 (line)]] | wt | 108 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.483× (z -8.5) |
| [[SNU-423 (line)]] | alt | 54.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.68× (z +12.8) | [[Harringtonine (drug)]] 5 µM 0.202× (z -11.3) ⚠ cell-cycle shift, explains ~65% of this change |
| [[AN3 CA (line)]] | alt | 109 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.145× (z -11.1) |
| [[C-33 A (line)]] | alt | 89.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 21.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 43.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.44× (z +15.9) | — |
| [[HT-29 (line)]] | alt | 20.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.16× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 53.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.60× (z +12.0) | — |
| [[KATO III (line)]] | alt | 109 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 56.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.14× (z +11.2) | — |
| [[RKO (line)]] | wt | 42.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.43× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 45.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.01× (z +13.8) | — |
| [[A549 (line)]] | wt | 48.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 54.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 30.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.01× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 45.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.47× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 80.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -21.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 131 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -12.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 53.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 60.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 46.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -9.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 48.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.72× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT43]] | +0.70 | +0.58 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CDKAL1]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[IPO11]] | +0.64 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[VTI1A]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[FTO]] | +0.61 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[KATNIP]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TTLL5]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[INVS]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MIPEP]] | +0.58 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[CSTPP1]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TASP1]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[TYW1]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPL]] | -0.53 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[TCEANC]] | -0.49 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ZNF385C]] | -0.49 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[COMMD3]] | -0.49 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[RETSAT]] | -0.48 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[GLIPR2]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[HHLA3]] | -0.47 | -0.20 / -0.45 | both halves | 7e-04 |  |
| [[OGFRL1]] | -0.47 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[TRIM36]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ZNF706]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[GYG1]] | -0.46 | -0.29 / -0.38 | both halves | 3e-04 |  |
| [[BTG3]] | -0.45 | -0.31 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.816). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.3, -13.3); signed map (-15.2, -49.2). **Vector** length 110, 34.8% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +6.0 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.3 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +8.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +0.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -14.2 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -11.4 | -5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.2 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.8 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.3 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.3 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | unc-51 like kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:41,246,599-41,962,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20574, REC01035, FAM7C1 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Pseudokinases; Unc-51 like kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C45](https://www.uniprot.org/uniprotkb/Q96C45) (Inactive serine/threonine-protein kinase ULK4):

> Pseudokinase that acts as a molecular adapter in the smoothened signaling pathway. Required to relieve inhibition of the GLI2 transcription factor in the presence of hedgehog (DHH, IHH or SHH) ligand: acts by mediating the association between STK36 and its ligand GLI2 in ciliary tip, promoting GLI2 phosphorylation and dissociation from SUFU inhibitor, followed by GLI2 translocation to the nucleus.

**Summary**, from NCBI Gene [54986](https://www.ncbi.nlm.nih.gov/gene/54986):

> This gene encodes a member of the unc-51-like serine/threonine kinase (STK) family. Members of this protein family play a role in neuronal growth and endocytosis. The encoded protein is likely involved in neurite branching, neurite elongation and neuronal migration. Genome-wide association studies (GWAS) indicate an association of variations in this gene with blood pressure and hypertension. Sequence variations in this gene may also be be associated with psychiatric disorders, including …

**Accessions** — [HGNC:15784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15784) · Entrez [54986](https://www.ncbi.nlm.nih.gov/gene/54986) · UniProt [Q96C45](https://www.uniprot.org/uniprotkb/Q96C45) · Ensembl [ENSG00000168038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168038)

## Data

Gene col 9586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9586); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9586]; `tensor/DDL_lfc|DDL_z.npy` [9586]; `embed/gene_vectors.npy` [9586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9586 or target_col == 9586). Every well: [[ULK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ULK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
