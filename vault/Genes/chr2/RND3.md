---
symbol: "RND3"
type: "gene"
col: 3743
ensembl_id: "ENSG00000115963"
name: "Rho family GTPase 3"
location: "2q23.3"
module: 93
arm: "+"
pooled_cpm: 180.74
n_lines_expressing: 45
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 20
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 16
direction_downstream: 6
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# RND3

*Rho family GTPase 3* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.12× (z +11.9, q 6e-30, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.331× (z -14.8, q 0e+00, down in 35 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.440× (z -11.4, q 8e-28, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABL2]] (+0.64, fdr 1e-05), [[RNF103-CHMP3]] (+0.61, fdr 1e-05), [[IFRD1]] (+0.58, fdr 1e-05); moves opposite to [[TCF3]] (-0.52, fdr 3e-05), [[NUDT21]] (-0.51, fdr 6e-05), [[PRKACA]] (-0.49, fdr 9e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[ETS2]] → it (grade B ⚠); 6 go from it, the strongest it → [[DUSP10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.12×** | +11.9 | 6e-30 | 41/44 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +11.4 | 9e-28 | 33/43 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.14×** | +8.4 | 1e-14 | 31/43 (C32, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.45×** | +7.3 | 3e-11 | 28/43 (hTERT-HPNE, C32, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +7.3 | 3e-11 | 34/43 (A-172, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.57×** | +6.1 | 9e-08 | 32/42 (BT-474, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.52×** | +5.9 | 3e-07 | 30/43 (BT-474, C32, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.7 | 8e-07 | 29/43 (HS-578T, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +5.4 | 3e-06 | 27/43 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.9 | 7e-05 | 26/43 (SW480, RKO, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.5 | 3e-04 | 25/44 (C32, LS 180, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +4.5 | 3e-04 | 29/43 (HS-578T, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 4e-04 | 27/43 (J82, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.37×** | +4.4 | 5e-04 | 26/42 (C32, BT-474, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 5e-04 | 24/42 (C32, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 7e-04 | 25/44 (HS-578T, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.005 | 22/43 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.005 | 26/43 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3743.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.331×** | -14.8 | 0e+00 | 35/39 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.383×** | -13.4 | 3e-38 | 39/44 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.440×** | -11.4 | 8e-28 | 37/43 (SNU-423, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.487×** | -10.0 | 2e-21 | 32/43 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.496×** | -9.0 | 2e-17 | 26/40 (NCI-H2347, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.610×** | -6.9 | 6e-10 | 29/43 (A498, SNU-423, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.686×** | -5.2 | 1e-05 | 29/43 (A498, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.754×** | -3.9 | 0.007 | 23/43 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.759×** | -3.8 | 0.009 | 25/43 (KATO III, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.765×** | -3.7 | 0.012 | 26/43 (LOX-IMVI, A498, …) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.767×** | -3.7 | 0.013 | 25/43 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.793×** | -3.2 | 0.065 | 21/43 (A498, HS-578T, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.093 | 20/42 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 168 | 9 (2 ⚠) | 13 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +17.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +14.1) | [[Cobimetinib (drug)]] 0.5 µM 0.189× (z -16.0) |
| [[A498 (line)]] | wt | 459 | 3 (1 ⚠) | 12 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.297× (z -12.3) |
| [[HS-578T (line)]] | alt | 414 | 4 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.65× (z +19.6) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.332× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 366 | 7 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.404× (z -10.0) |
| [[J82 (line)]] | alt | 396 | 8 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.65× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.324× (z -10.2) |
| [[SNU-423 (line)]] | alt | 530 | 1 | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.226× (z -14.5) |
| [[BT-474 (line)]] | alt | 131 | 5 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 13.4× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.337× (z -9.8) |
| [[A549 (line)]] | wt | 322 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.187× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 333 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.271× (z -13.1) |
| [[A-172 (line)]] | wt | 325 | 4 (1 ⚠) | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 6.68× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -13.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 226 | 2 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 18.0× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.336× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 215 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.16× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.487× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 87.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.52× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 168 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -10.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 319 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +19.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.87× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -11.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 279 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.73× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.436× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 101 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +15.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 165 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.397× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 168 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.4× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 58.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +11.6) | — |
| [[LoVo (line)]] | wt | 141 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.84× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 91.8 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.40× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -13.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 82.4 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.57× (z +12.9) | — |
| [[COLO 205 (line)]] | alt | 204 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -10.8) |
| [[H4 (line)]] | wt | 117 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.60× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 222 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.26× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 292 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 84.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.84× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -9.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 57.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -12.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 214 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.5) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 53.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.56× (z +11.4) | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0732× (z -14.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 89.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 120 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.27× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 88.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 270 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 81.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0981× (z -8.5) |
| [[AN3 CA (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABL2]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[RNF103-CHMP3]] | +0.61 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[IFRD1]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[LINC01828]] | +0.57 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[HDAC9]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ATF3]] | +0.56 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[DUSP16]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PPP1R15A]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SPINK1]] | +0.55 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[GATA6]] | +0.54 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[NABP1]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TLE4]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF3]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[NUDT21]] | -0.51 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[PRKACA]] | -0.49 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[CPSF1]] | -0.48 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[IFT122]] | -0.47 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[IMMT]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[RMDN3]] | -0.46 | -0.26 / -0.48 | both halves | 4e-04 |  |
| [[DAZAP1]] | -0.46 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[LHPP]] | -0.45 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[MAPK1]] | -0.45 | -0.32 / -0.42 | both halves | 1e-04 |  |
| [[SNRNP40]] | -0.45 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[QSOX2]] | -0.45 | -0.32 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETS2]] | B | ETS2 activity raises RND3's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 3.48× lower at baseline in the lines without ETS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[BMP2]] | B | BMP2 activity raises RND3's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.64× lower at baseline in the lines without BMP2 | 0.004 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[DUSP10]] | B | DUSP10 activity raises RND3's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 3.46× lower at baseline in the lines without DUSP10 | 0.006 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[FBXO32]] | B | FBXO32 activity raises RND3's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 3.39× lower at baseline in the lines without FBXO32 | 0.008 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[IFI16]] | B | IFI16 activity raises RND3's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.79× lower at baseline in the lines without IFI16 | 0.009 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[CTSS]] | B | CTSS activity raises RND3's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.62× lower at baseline in the lines without CTSS | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[C21orf91]] | B | C21orf91 activity raises RND3's level | lines that do not express C21orf91 (5) vs lines expressing it (45) | 2.53× lower at baseline in the lines without C21orf91 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[ETS2]] | B | ETS2 activity strengthens RND3's drug response | lines that do not express ETS2 (6) vs lines expressing it (38) | the lines without ETS2 respond 0.65× as strongly (z diff +1.47); strongest at Panobinostat 0.5 µM: 1.10x vs 0.50x (z diff +5.6) | 0.049 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3; target measured in part of the lines; artifact flags |
| [[GATA6]] | B | GATA6 activity raises RND3's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.19× lower at baseline in the lines without GATA6 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[LINC00944]] | B | LINC00944 activity raises RND3's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 2.37× lower at baseline in the lines without LINC00944 | 0.063 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[RPLP0P2]] | B | RPLP0P2 activity raises RND3's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 3.18× lower at baseline in the lines without RPLP0P2 | 0.066 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[TLE4]] | B | TLE4 activity raises RND3's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 2.62× lower at baseline in the lines without TLE4 | 0.079 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP10]] | B | RND3 activity raises DUSP10's level | lines that do not express RND3 (5) vs lines expressing it (45) | 4.74× lower at baseline in the lines without RND3 | 0.060 | ⚠ within organs, on part of the lines; also absent: GULP1, SFXN3, GALNT7; its own permutation p |
| [[PMAIP1]] | B | RND3 activity raises PMAIP1's level | lines that do not express RND3 (5) vs lines expressing it (45) | 3.32× lower at baseline in the lines without RND3 | 0.060 | ⚠ within organs, on part of the lines; also absent: GULP1, SFXN3, GALNT7; its own permutation p |
| [[PPP1R3B]] | B | RND3 activity raises PPP1R3B's level | lines that do not express RND3 (5) vs lines expressing it (45) | 2.99× lower at baseline in the lines without RND3 | 0.060 | ⚠ within organs, on part of the lines; also absent: GULP1, SFXN3, GALNT7; its own permutation p |
| [[LINC01619]] | B | RND3 activity raises LINC01619's level | lines that do not express RND3 (5) vs lines expressing it (45) | 2.48× lower at baseline in the lines without RND3 | 0.060 | ⚠ within organs, on part of the lines; also absent: GULP1, SFXN3, GALNT7; its own permutation p |
| [[BTG1]] | B | RND3 activity raises BTG1's level | lines that do not express RND3 (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without RND3 | 0.060 | ⚠ within organs, on part of the lines; also absent: GULP1, SFXN3, GALNT7; its own permutation p |
| [[NABP1]] | B | RND3 activity raises NABP1's level | lines that do not express RND3 (5) vs lines expressing it (45) | 2.58× lower at baseline in the lines without RND3 | 0.089 | ⚠ within organs, on part of the lines; also absent: GULP1, SFXN3, GALNT7; its own permutation p |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.0, 5.4); signed map (26.4, 11.3). **Vector** length 135, 45.7% of its response variance represented; |z| ≥ 3 in 1,447 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.4 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +3.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -14.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -13.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -9.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.0 | -2.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | Rho family GTPase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:150,468,195-150,539,011 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RhoE, Rho8; previously ARHE |
| Gene groups (HGNC) | Rho family GTPases |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 4 pathways, smallest: RND3 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [P61587](https://www.uniprot.org/uniprotkb/P61587) (Rho-related GTP-binding protein RhoE):

> Binds GTP but lacks intrinsic GTPase activity and is resistant to Rho-specific GTPase-activating proteins.

**Summary**, from NCBI Gene [390](https://www.ncbi.nlm.nih.gov/gene/390):

> This gene encodes a protein which is a member of the small GTPase protein superfamily. The encoded protein binds only GTP but has no GTPase activity, and appears to act as a negative regulator of cytoskeletal organization leading to loss of adhesion. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:671) · Entrez [390](https://www.ncbi.nlm.nih.gov/gene/390) · UniProt [P61587](https://www.uniprot.org/uniprotkb/P61587) · Ensembl [ENSG00000115963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115963)

## Data

Gene col 3743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3743); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3743]; `tensor/DDL_lfc|DDL_z.npy` [3743]; `embed/gene_vectors.npy` [3743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3743 or target_col == 3743). Every well: [[RND3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RND3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
