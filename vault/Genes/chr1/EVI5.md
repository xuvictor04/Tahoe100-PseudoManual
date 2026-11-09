---
symbol: "EVI5"
type: "gene"
col: 856
ensembl_id: "ENSG00000067208"
name: "ecotropic viral integration site 5"
location: "1p22.1"
module: 77
arm: "+"
pooled_cpm: 194.25
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# EVI5

*ecotropic viral integration site 5* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.48× (z +9.1, q 5e-17, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.464× (z -20.3, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.737× (z -4.4, q 6e-04, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRPK2]] (+0.69, fdr 7e-06), [[COP1]] (+0.63, fdr 1e-05), [[DOCK9]] (+0.63, fdr 8e-06); moves opposite to [[COG4]] (-0.58, fdr 1e-05), [[THAP9]] (-0.57, fdr 4e-05), [[TAPBPL]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +9.1 | 5e-17 | 40/48 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +8.0 | 4e-13 | 35/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +7.3 | 5e-11 | 30/48 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +6.9 | 8e-10 | 32/48 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.5 | 1e-08 | 37/45 (LS 180, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +6.2 | 7e-08 | 28/48 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +6.1 | 8e-08 | 38/49 (CFPAC-1, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.1 | 1e-07 | 28/48 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +5.5 | 2e-06 | 17/48 (J82, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +5.5 | 2e-06 | 28/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.9 | 4e-05 | 23/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.6 | 2e-04 | 11/49 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.004 | 22/49 (NCI-H460, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.019 | 17/48 (HOP62, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.13× | +3.4 | 0.027 | 7/48 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.13× | +3.2 | 0.044 | 12/47 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.12× | +2.9 | 0.096 | 14/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 856.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -20.3 | 0e+00 | 39/44 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.516×** | -18.2 | 0e+00 | 43/49 (Panc 03.27, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.600×** | -13.0 | 3e-36 | 35/45 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.668×** | -10.7 | 2e-24 | 38/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.788×** | -9.3 | 2e-18 | 25/48 (HS-578T, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.727×** | -8.8 | 2e-16 | 39/48 (KATO III, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.798×** | -6.2 | 4e-08 | 26/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.805×** | -5.7 | 7e-07 | 25/48 (HS-578T, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.836× | -4.9 | 6e-05 | 23/48 (NCI-H2347, SNU-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.842× | -4.6 | 2e-04 | 21/48 (A-172, SNU-1, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.737×** | -4.4 | 6e-04 | 31/48 (NCI-H2347, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.856× | -4.1 | 0.002 | 17/49 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -3.9 | 0.005 | 19/48 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.771×** | -3.7 | 0.007 | 19/48 (C32, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.864× | -3.7 | 0.008 | 20/47 (HS-578T, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.877× | -3.6 | 0.011 | 18/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.789×** | -3.4 | 0.023 | 19/48 (SW 1271, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.803×** | -3.1 | 0.049 | 18/48 (NCI-H2347, SNU-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 174 | 2 (1 ⚠) | 13 (12 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +12.3) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.476× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.582× (z -10.2) |
| [[SNU-1 (line)]] | wt | 738 | 0 | 11 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.357× (z -11.0) |
| [[HS-578T (line)]] | alt | 317 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -19.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[KATO III (line)]] | alt | 199 | 3 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.97× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -17.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 222 | 4 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 191 | 1 (1 ⚠) | 6 (6 ⚠) | [[Belinostat (drug)]] 0.5 µM 1.70× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -17.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 238 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -18.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 184 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -16.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.609× (z -9.3) |
| [[HOP62 (line)]] | alt | 150 | 1 (1 ⚠) | 5 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.05× (z +9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Trametinib (drug)]] 0.5 µM 0.504× (z -11.3) |
| [[HT-29 (line)]] | alt | 189 | 2 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.81× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.597× (z -8.8) |
| [[J82 (line)]] | alt | 215 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -17.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 258 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -17.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 139 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -17.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 209 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -14.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 263 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.98× (z +11.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.97× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.477× (z -11.6) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 99.9 | 5 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.87× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 170 | 3 (1 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.28× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 124 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -17.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 130 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -14.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 271 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.415× (z -11.9) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 147 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +10.7) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.83× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.501× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 234 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -17.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 195 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +16.5) ⚠ cell-cycle shift, explains ~10% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -14.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 325 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.279× (z -19.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 287 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -12.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW1417 (line)]] | alt | 170 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.345× (z -16.8) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 204 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +13.8) ⚠ cell-cycle shift, explains ~10% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.275× (z -17.4) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -23.3) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 368 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -15.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 263 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -20.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 207 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.73× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -8.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 176 | 1 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.77× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.528× (z -13.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 164 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -12.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 252 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -10.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 239 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -18.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 218 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.501× (z -11.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -15.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -10.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 213 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPK2]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[COP1]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[DOCK9]] | +0.63 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[BICD2]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[FOCAD]] | +0.61 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[EXOC6B]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PACC1]] | +0.60 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[MPZL1]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SLC27A4]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[RNF13]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[FBXW11]] | +0.59 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[MACO1]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG4]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[THAP9]] | -0.57 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[TAPBPL]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[FAM111A]] | -0.54 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[ZNF436]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[DDX39B]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SLC39A1]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[TEF]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MED12]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ZBTB1]] | -0.53 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[YY1AP1]] | -0.52 | -0.40 / -0.56 | both halves | 4e-05 |  |
| [[IFT81]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers EVI5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers EVI5's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (0.9, -21.6); signed map (-45.7, -4.1). **Vector** length 133, 44.1% of its response variance represented; |z| ≥ 3 in 1,418 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.7 | +9.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.4 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.4 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +6.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -10.2 | -9.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -7.5 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -6.3 | -6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -13.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.7 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ecotropic viral integration site 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:92,508,696-92,792,404 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NB4S |
| Gene groups (HGNC) | TBC1 domain family members; EVI5 family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [O60447](https://www.uniprot.org/uniprotkb/O60447) (Ecotropic viral integration site 5 protein homolog):

> Functions as a regulator of cell cycle progression by stabilizing the FBXO5 protein and promoting cyclin-A accumulation during interphase. May play a role in cytokinesis.

**Summary**, from NCBI Gene [7813](https://www.ncbi.nlm.nih.gov/gene/7813):

> Enables GTPase activator activity and small GTPase binding activity. Involved in positive regulation of GTPase activity and retrograde transport, endosome to Golgi. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3501) · Entrez [7813](https://www.ncbi.nlm.nih.gov/gene/7813) · UniProt [O60447](https://www.uniprot.org/uniprotkb/O60447) · Ensembl [ENSG00000067208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067208)

## Data

Gene col 856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 856); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 856]; `tensor/DDL_lfc|DDL_z.npy` [856]; `embed/gene_vectors.npy` [856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 856 or target_col == 856). Every well: [[EVI5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EVI5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
