---
symbol: "PKN2"
type: "gene"
col: 777
ensembl_id: "ENSG00000065243"
name: "protein kinase N2"
location: "1p22.2"
module: 28
arm: "+"
pooled_cpm: 270.74
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# PKN2

*protein kinase N2* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.53× (z +15.2, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.521× (z -16.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP350]] (+0.59, fdr 1e-05), [[WASHC4]] (+0.58, fdr 1e-05), [[TPR]] (+0.58, fdr 3e-05); moves opposite to [[KCTD15]] (-0.57, fdr 1e-05), [[C1orf216]] (-0.55, fdr 4e-05), [[ANKUB1]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +15.2 | 0e+00 | 43/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +7.6 | 9e-12 | 39/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +6.1 | 3e-07 | 37/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.8 | 2e-04 | 22/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +4.7 | 3e-04 | 24/48 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.3 | 0.002 | 19/48 (HT-29, KATO III, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.007 | 17/48 (HT-29, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.16× | +3.8 | 0.012 | 22/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.11× | +3.6 | 0.018 | 6/48 (HOP62, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.026 | 27/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.15× | +3.5 | 0.027 | 12/48 (CHP-212, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.1 | 0.094 | 9/48 (RKO, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 777.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.521×** | -16.5 | 0e+00 | 47/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -14.6 | 0e+00 | 45/49 (A549, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.576×** | -13.9 | 7e-42 | 44/49 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -13.3 | 3e-38 | 42/44 (SK-MEL-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.581×** | -9.9 | 3e-21 | 41/45 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -8.8 | 8e-17 | 42/47 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.789×** | -6.0 | 2e-07 | 35/48 (Panc 03.27, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.830×** | -4.7 | 2e-04 | 24/48 (A549, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.638×** | -4.6 | 3e-04 | 34/45 (H4, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.838× | -4.4 | 5e-04 | 22/48 (J82, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.901× | -3.7 | 0.011 | 8/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.903× | -3.6 | 0.014 | 2/48 (Hs 766T, H4) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.877× | -3.3 | 0.042 | 13/48 (H4, AN3 CA, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.729×** | -3.2 | 0.048 | 22/45 (SK-MEL-2, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.880× | -3.2 | 0.048 | 6/48 (NCI-H1792, A-427, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.883× | -3.1 | 0.063 | 7/47 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.886× | -3.1 | 0.074 | 4/48 (CFPAC-1, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 273 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -15.5) |
| [[LoVo (line)]] | wt | 416 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -13.9) |
| [[A-427 (line)]] | wt | 253 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.509× (z -12.2) |
| [[A498 (line)]] | wt | 253 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 366 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -13.8) |
| [[HT-29 (line)]] | alt | 251 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +22.7) | [[Auranofin (drug)]] 5 µM 0.449× (z -13.9) |
| [[LS 180 (line)]] | wt | 387 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 248 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -13.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 406 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -18.5) |
| [[RKO (line)]] | wt | 255 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +16.4) | [[Auranofin (drug)]] 5 µM 0.451× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 204 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -25.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.240× (z -22.4) |
| [[SNU-423 (line)]] | alt | 218 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.456× (z -12.2) |
| [[A-172 (line)]] | wt | 140 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +13.5) | [[Auranofin (drug)]] 5 µM 0.431× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 319 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +15.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -18.4) |
| [[HS-578T (line)]] | alt | 260 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.660× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 259 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -10.5) |
| [[KATO III (line)]] | alt | 333 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -17.3) |
| [[LOX-IMVI (line)]] | wt | 265 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 276 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -14.4) |
| [[PANC-1 (line)]] | alt | 356 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.563× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.613× (z -10.0) |
| [[SW 900 (line)]] | alt | 245 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -11.7) |
| [[SW48 (line)]] | wt | 247 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -12.0) |
| [[A549 (line)]] | wt | 226 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -26.6) |
| [[AsPC-1 (line)]] | alt | 436 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.435× (z -11.5) |
| [[C32 (line)]] | wt | 205 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +13.0) | [[Auranofin (drug)]] 5 µM 0.427× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 194 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 284 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.454× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 174 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +17.1) | [[Auranofin (drug)]] 5 µM 0.578× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 241 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.468× (z -10.8) |
| [[SNU-1 (line)]] | wt | 233 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.476× (z -9.6) |
| [[BT-474 (line)]] | alt | 182 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.8) | [[Auranofin (drug)]] 5 µM 0.545× (z -8.7) |
| [[H4 (line)]] | wt | 187 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -17.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 381 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.412× (z -11.9) |
| [[HOP62 (line)]] | alt | 167 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.9) | [[Auranofin (drug)]] 5 µM 0.404× (z -15.6) |
| [[Hs 766T (line)]] | wt | 381 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.422× (z -12.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 240 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.576× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 317 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.357× (z -17.5) |
| [[NCI-H2030 (line)]] | alt | 165 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.508× (z -10.4) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 229 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -13.0) |
| [[SHP-77 (line)]] | alt | 239 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.543× (z -9.1) |
| [[SW1417 (line)]] | alt | 335 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.566× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 243 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.418× (z -11.5) |
| [[COLO 205 (line)]] | alt | 223 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -11.6) |
| [[SW 1088 (line)]] | alt | 245 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -11.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 252 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 351 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP350]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[WASHC4]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TPR]] | +0.58 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[RAB3GAP2]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 | same gene group |
| [[TXNIP]] | +0.54 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[CETN3]] | +0.53 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[CTNND1]] | +0.52 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[INIP]] | +0.52 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[SENP2]] | +0.52 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[CEP295]] | +0.52 | +0.42 / +0.46 | both halves | 4e-05 | same gene group |
| [[SKAP2]] | +0.51 | +0.56 / +0.36 | both halves | 9e-05 |  |
| [[RABGAP1]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD15]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[C1orf216]] | -0.55 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[ANKUB1]] | -0.54 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[CAPN15]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[KLHL25]] | -0.52 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[MFAP3L]] | -0.52 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[BEND3]] | -0.51 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[PABPC1L]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ANO7]] | -0.51 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CTC-338M12.4]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[SEPTIN7P13]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PGS1]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.427). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-29.8, 1.8); signed map (6.1, -11.3). **Vector** length 103, 34.8% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +15.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +4.1 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +3.9 |
|  | [[Thymol (drug)]] 5 µM |  | +1.6 | -1.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.5 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.3 | -0.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.3 | -0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.0 | -16.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -14.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -7.0 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.3 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.3 | -0.9 |
|  | [[Infigratinib (drug)]] 5 µM |  | -2.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase N2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:88,684,222-88,836,255 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRK2, Pak-2, STK7; previously PRKCL2 |
| Gene groups (HGNC) | C2 domain containing protein kinases; Small nucleolar RNA protein coding host genes; Protein kinase N family |
| Reactome | 13 pathways, smallest: RHO GTPases activate PKNs; High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16513](https://www.uniprot.org/uniprotkb/Q16513) (Serine/threonine-protein kinase N2):

> PKC-related serine/threonine-protein kinase and Rho/Rac effector protein that participates in specific signal transduction responses in the cell. Plays a role in the regulation of cell cycle progression, actin cytoskeleton assembly, cell migration, cell adhesion, tumor cell invasion and transcription activation signaling processes. Phosphorylates CTTN in hyaluronan-induced astrocytes and hence decreases CTTN ability to associate with filamentous actin. Phosphorylates HDAC5, therefore lead to …

**Summary**, from NCBI Gene [5586](https://www.ncbi.nlm.nih.gov/gene/5586):

> Enables RNA polymerase binding activity; histone deacetylase binding activity; and protein serine/threonine kinase activity. Involved in several processes, including apical junction assembly; positive regulation of cell cycle; and positive regulation of viral genome replication. Located in several cellular components, including cleavage furrow; lamellipodium; and midbody. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9406) · Entrez [5586](https://www.ncbi.nlm.nih.gov/gene/5586) · UniProt [Q16513](https://www.uniprot.org/uniprotkb/Q16513) · Ensembl [ENSG00000065243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065243)

## Data

Gene col 777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 777); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 777]; `tensor/DDL_lfc|DDL_z.npy` [777]; `embed/gene_vectors.npy` [777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 777 or target_col == 777). Every well: [[PKN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
