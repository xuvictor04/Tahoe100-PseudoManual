---
symbol: "SCD"
type: "gene"
col: 1780
ensembl_id: "ENSG00000099194"
name: "stearoyl-CoA desaturase"
location: "10q24.31"
module: 86
arm: "+"
pooled_cpm: 377.95
n_lines_expressing: 50
n_dd_up: 59
n_dd_down: 37
n_dd_up_clean: 49
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# SCD

*stearoyl-CoA desaturase* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 59 drug-doses (10 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.65× (z +19.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.137× (z -40.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGCR]] (+0.82, fdr 7e-06), [[FDFT1]] (+0.81, fdr 7e-06), [[DHCR7]] (+0.81, fdr 7e-06); moves opposite to [[SRGAP1]] (-0.44, fdr 8e-05), [[CHAMP1]] (-0.43, fdr 4e-05), [[KIFC3]] (-0.43, fdr 7e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 63 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 59 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.65×** | +19.5 | 0e+00 | 48/48 (A549, HOP62, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | **2.52×** | +18.5 | 0e+00 | 48/49 (A549, Panc 03.27, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **2.48×** | +12.9 | 9e-36 | 47/48 (A549, H4, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **2.25×** | +11.0 | 4e-26 | 48/49 (A549, HOP62, …) | rises with dose | plate-row cell shift |
| [[Retinoic acid (drug)]] 5 µM |  | **1.72×** | +10.8 | 2e-25 | 45/49 (SW480, LoVo, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **2.12×** | +10.7 | 2e-24 | 46/48 (COLO 205, SW480, …) | all doses, flat |  |
| [[Posaconazole (drug)]] 5 µM |  | **2.02×** | +9.6 | 1e-19 | 47/48 (Panc 03.27, A549, …) | rises with dose | plate-row cell shift |
| [[Adagrasib (drug)]] 5 µM |  | **1.95×** | +9.1 | 7e-18 | 44/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.89×** | +9.0 | 2e-17 | 48/48 (COLO 205, SW480, …) | all doses, flat |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.91×** | +8.8 | 7e-17 | 47/48 (A549, HOP62, …) | rises with dose | plate-row cell shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.82×** | +8.5 | 1e-15 | 44/48 (A549, A498, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.80×** | +8.0 | 8e-14 | 43/48 (A549, HOP62, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.75×** | +7.9 | 1e-13 | 43/48 (COLO 205, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +7.0 | 7e-11 | 33/49 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bexarotene (drug)]] 5 µM |  | **1.63×** | +6.9 | 2e-10 | 46/48 (COLO 205, SW1417, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.4 | 4e-09 | 30/49 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1780.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.137×** | -40.0 | 0e+00 | 48/48 (SNU-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.123×** | -28.6 | 0e+00 | 48/48 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.142×** | -27.8 | 0e+00 | 48/48 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.354×** | -14.8 | 0e+00 | 46/48 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.458×** | -11.1 | 8e-27 | 44/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.597×** | -7.1 | 1e-10 | 34/47 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.630×** | -6.4 | 2e-08 | 37/48 (KATO III, NCI-H23, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.645×** | -6.3 | 2e-08 | 39/48 (A-427, KATO III, …) | top dose only | position effect removed |
| [[Clotrimazole (drug)]] 5 µM |  | **0.750×** | -5.9 | 3e-07 | 35/49 (COLO 205, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.686×** | -5.4 | 4e-06 | 29/48 (SNU-1, A-427, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.695×** | -5.2 | 9e-06 | 33/48 (NCI-H23, SNU-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.706×** | -5.0 | 3e-05 | 37/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Quinestrol (drug)]] 5 µM |  | **0.785×** | -4.9 | 4e-05 | 33/49 (KATO III, RKO, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.723×** | -4.6 | 1e-04 | 29/48 (BT-474, C-33 A, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.721×** | -4.4 | 4e-04 | 30/47 (SW480, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.739×** | -4.0 | 0.002 | 26/47 (RKO, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.762×** | -3.9 | 0.003 | 39/47 (HepG2/C3A, SW1417, …) | inconsistent across doses | position effect removed |
| [[Resveratrol (drug)]] 5 µM |  | 0.840× | -3.6 | 0.011 | 19/49 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.782×** | -3.5 | 0.011 | 25/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.775×** | -3.5 | 0.011 | 24/49 (HepG2/C3A, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 235 | 14 | 5 | [[Cepharanthine (drug)]] 5 µM 8.24× (z +28.4) | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -27.1) |
| [[COLO 205 (line)]] | alt | 545 | 13 | 6 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 3.72× (z +17.1) | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -25.7) |
| [[C-33 A (line)]] | alt | 827 | 8 | 10 (5 ⚠) | [[Cepharanthine (drug)]] 5 µM 3.56× (z +16.0) | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -23.5) |
| [[NCI-H23 (line)]] | alt | 335 | 8 | 9 (5 ⚠) | [[Cepharanthine (drug)]] 5 µM 4.65× (z +19.0) | [[Homoharringtonine (drug)]] 5 µM 0.0491× (z -37.5) |
| [[HOP62 (line)]] | alt | 225 | 13 (1 ⚠) | 3 | [[Cepharanthine (drug)]] 5 µM 5.57× (z +22.2) | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -24.7) |
| [[LOX-IMVI (line)]] | wt | 204 | 11 (1 ⚠) | 4 | [[Cepharanthine (drug)]] 5 µM 3.01× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -24.7) |
| [[AsPC-1 (line)]] | alt | 200 | 7 | 6 (2 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.69× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -26.2) |
| [[BT-474 (line)]] | alt | 520 | 2 | 11 (6 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.28× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.0647× (z -36.2) |
| [[HT-29 (line)]] | alt | 412 | 9 | 4 | [[Cepharanthine (drug)]] 5 µM 4.78× (z +19.2) | [[Homoharringtonine (drug)]] 5 µM 0.0901× (z -29.3) |
| [[SNU-1 (line)]] | wt | 1,363 | 3 | 10 (5 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.39× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.0307× (z -52.0) |
| [[A-172 (line)]] | wt | 452 | 8 (2 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -19.9) |
| [[A-427 (line)]] | wt | 1,068 | 1 | 11 (6 ⚠) | [[Bexarotene (drug)]] 0.5 µM 2.31× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.0426× (z -34.8) |
| [[C32 (line)]] | wt | 781 | 2 | 10 (5 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.22× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.0791× (z -34.7) |
| [[J82 (line)]] | alt | 298 | 8 (2 ⚠) | 4 | [[Cepharanthine (drug)]] 5 µM 2.35× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -24.8) |
| [[SW480 (line)]] | alt | 257 | 8 (1 ⚠) | 4 | [[Cepharanthine (drug)]] 5 µM 2.27× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -29.2) |
| [[H4 (line)]] | wt | 112 | 9 | 1 | [[Cepharanthine (drug)]] 5 µM 6.39× (z +18.4) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -15.8) |
| [[hTERT-HPNE (line)]] | wt | 135 | 7 | 3 | [[Cepharanthine (drug)]] 5 µM 4.56× (z +14.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 209 | 7 (2 ⚠) | 3 | [[Berbamine (drug)]] 5 µM 3.92× (z +19.7) | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -27.1) |
| [[A498 (line)]] | wt | 370 | 7 | 2 | [[Cepharanthine (drug)]] 5 µM 3.29× (z +15.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -11.4) |
| [[HCT15 (line)]] | alt | 447 | 5 | 4 | [[Cepharanthine (drug)]] 5 µM 3.05× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.0531× (z -28.8) |
| [[HS-578T (line)]] | alt | 186 | 6 | 3 | [[Cepharanthine (drug)]] 5 µM 4.12× (z +17.4) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -19.7) |
| [[LoVo (line)]] | wt | 113 | 5 | 4 | [[Cepharanthine (drug)]] 5 µM 6.09× (z +18.4) | [[Harringtonine (drug)]] 5 µM 0.107× (z -15.5) |
| [[NCI-H2030 (line)]] | alt | 265 | 6 | 3 | [[Cepharanthine (drug)]] 5 µM 4.08× (z +18.3) | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -27.0) |
| [[NCI-H460 (line)]] | wt | 457 | 4 | 5 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.15× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -26.1) |
| [[PANC-1 (line)]] | alt | 592 | 4 | 5 | [[Cepharanthine (drug)]] 5 µM 2.39× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -28.7) |
| [[SNU-423 (line)]] | alt | 420 | 6 | 3 | [[Cepharanthine (drug)]] 5 µM 4.15× (z +18.7) | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -29.8) |
| [[SW 900 (line)]] | alt | 268 | 5 | 4 | [[Cepharanthine (drug)]] 5 µM 4.59× (z +18.1) | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -24.2) |
| [[LS 180 (line)]] | wt | 278 | 3 | 5 | [[Cepharanthine (drug)]] 5 µM 4.58× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.0674× (z -23.2) |
| [[NCI-H2347 (line)]] | alt | 285 | 3 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -22.4) |
| [[RPMI-7951 (line)]] | alt | 248 | 4 | 4 | [[Entrectinib (drug)]] 5 µM 3.28× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -35.8) |
| [[SW48 (line)]] | wt | 292 | 6 | 2 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 5.60× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 405 | 2 | 5 | [[Cepharanthine (drug)]] 5 µM 2.84× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.0929× (z -28.8) |
| [[HEC-1-A (line)]] | alt | 180 | 3 | 4 | [[Berbamine (drug)]] 5 µM 3.57× (z +15.3) | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -20.3) |
| [[SHP-77 (line)]] | alt | 171 | 5 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -17.5) |
| [[SW1417 (line)]] | alt | 355 | 4 | 3 | [[Retinoic acid (drug)]] 5 µM 1.89× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -22.2) |
| [[KATO III (line)]] | alt | 383 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0841× (z -25.5) |
| [[NCI-H1573 (line)]] | alt | 216 | 2 (1 ⚠) | 4 | [[Berbamine (drug)]] 5 µM 4.01× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -14.2) |
| [[RKO (line)]] | wt | 288 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0575× (z -45.9) |
| [[AN3 CA (line)]] | alt | 689 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0943× (z -28.8) |
| [[HepG2_C3A (line)]] | wt | 615 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.0849× (z -37.8) |
| [[MIA PaCa-2 (line)]] | alt | 944 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0675× (z -35.8) |
| [[Hs 766T (line)]] | wt | 404 | 1 | 3 | [[Cepharanthine (drug)]] 5 µM 2.64× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.0854× (z -25.9) |
| [[NCI-H1792 (line)]] | alt | 386 | 1 | 3 | [[Cepharanthine (drug)]] 5 µM 1.96× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -24.9) |
| [[SK-MEL-2 (line)]] | alt | 231 | 1 | 3 | [[Cepharanthine (drug)]] 5 µM 1.82× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -26.4) |
| [[SW 1088 (line)]] | alt | 249 | 2 | 2 | [[Berbamine (drug)]] 5 µM 3.96× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -13.5) |
| [[SW 1271 (line)]] | alt | 205 | 2 | 2 | [[Cepharanthine (drug)]] 5 µM 4.19× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -14.5) |
| [[CHP-212 (line)]] | wt | 316 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -23.0) |
| [[NCI-H661 (line)]] | alt | 236 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -13.0) |
| [[NCI-H2122 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 340 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCR]] | +0.82 | +0.87 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 747 |
| [[FDFT1]] | +0.81 | +0.87 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 609 |
| [[DHCR7]] | +0.81 | +0.87 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 663 |
| [[MSMO1]] | +0.80 | +0.82 / +0.80 | both halves | 7e-06 | pathway: Metabolism of steroids; STRING 613 |
| [[CYP51A1]] | +0.78 | +0.77 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 580 |
| [[FDPS]] | +0.77 | +0.81 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 559 |
| [[HMGCS1]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 794 |
| [[IDI1]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 403 |
| [[ERG28]] | +0.72 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[PCSK9]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[OLMALINC]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 | ⚠ **readthrough risk**: OLMALINC lies 8.3 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[INSIG1]] | +0.71 | +0.74 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 690 |
| [[ACSS2]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 588 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP1]] | -0.44 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[CHAMP1]] | -0.43 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[KIFC3]] | -0.43 | -0.38 / -0.43 | both halves | 7e-05 | pathway: HALLMARK_MYOGENESIS |
| [[CEP135]] | -0.42 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[RPL7L1]] | -0.41 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[ZNF347]] | -0.41 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[TFAM]] | -0.41 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.880). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, -49.2); signed map (-52.7, 32.1). **Vector** length 162, 60.7% of its response variance represented; |z| ≥ 3 in 2,880 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.69 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.69 to 20); *Lanosterol biosynthesis* (reactome, mean cos +0.70 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +15.8 | +19.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +14.2 | +18.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +11.1 | +5.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +10.3 | +12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +6.4 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +8.8 | +11.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -13.7 | -14.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -13.6 | -28.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -10.4 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.5 | -27.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -7.6 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -7.2 | -6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.8 | -6.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -5.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | stearoyl-CoA desaturase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,347,233-100,364,826 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FADS5, SCD1; previously SCDOS |
| Gene groups (HGNC) | Fatty acid desaturases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, ANDROGEN_RESPONSE, MYOGENESIS, MTORC1_SIGNALING |
| Reactome | 14 pathways, smallest: NR1H2 & NR1H3 regulate gene expression linked to lipogenesis; Fatty acyl-CoA biosynthesis; NR1H2 and NR1H3-mediated signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O00767](https://www.uniprot.org/uniprotkb/O00767) (Stearoyl-CoA desaturase):

> Stearoyl-CoA desaturase that utilizes O(2) and electrons from reduced cytochrome b5 to introduce the first double bond into saturated fatty acyl-CoA substrates. Catalyzes the insertion of a cis double bond at the delta-9 position into fatty acyl-CoA substrates including palmitoyl-CoA and stearoyl-CoA. Gives rise to a mixture of 16:1 and 18:1 unsaturated fatty acids. Plays an important role in lipid biosynthesis. Plays an important role in regulating the expression of genes that are involved in …

**Summary**, from NCBI Gene [6319](https://www.ncbi.nlm.nih.gov/gene/6319):

> This gene encodes an enzyme involved in fatty acid biosynthesis, primarily the synthesis of oleic acid. The protein belongs to the fatty acid desaturase family and is an integral membrane protein located in the endoplasmic reticulum. Transcripts of approximately 3.9 and 5.2 kb, differing only by alternative polyadenlyation signals, have been detected. A gene encoding a similar enzyme is located on chromosome 4 and a pseudogene of this gene is located on chromosome 17. [provided by RefSeq, Sep …

**Accessions** — [HGNC:10571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10571) · Entrez [6319](https://www.ncbi.nlm.nih.gov/gene/6319) · UniProt [O00767](https://www.uniprot.org/uniprotkb/O00767) · Ensembl [ENSG00000099194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099194)

## Data

Gene col 1780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1780); `tables/drug_effects.parquet` (104 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1780]; `tensor/DDL_lfc|DDL_z.npy` [1780]; `embed/gene_vectors.npy` [1780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1780 or target_col == 1780). Every well: [[SCD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
