---
symbol: "INO80D"
type: "gene"
col: 3603
ensembl_id: "ENSG00000114933"
name: "INO80 complex subunit D"
location: "2q33.3"
module: 95
arm: "+"
pooled_cpm: 94.77
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# INO80D

*INO80 complex subunit D* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.64× (z +44.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.216× (z -37.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX4-DT]] (+0.83, fdr 1e-05), [[ZFX]] (+0.80, fdr 7e-06), [[WARS2-AS1]] (+0.80, fdr 1e-05); moves opposite to [[WASF3]] (-0.75, fdr 7e-06), [[HACE1]] (-0.73, fdr 1e-05), [[SH3PXD2B]] (-0.70, fdr 3e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLFN5]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.64×** | +44.2 | 0e+00 | 48/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.17×** | +27.0 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +22.7 | 0e+00 | 47/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +15.9 | 0e+00 | 47/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.97×** | +15.5 | 0e+00 | 46/49 (LoVo, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +9.8 | 8e-21 | 42/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +9.6 | 6e-20 | 40/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +8.6 | 6e-16 | 37/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +8.0 | 5e-14 | 26/49 (hTERT-HPNE, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +7.9 | 2e-13 | 37/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +7.1 | 6e-11 | 36/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.74×** | +6.2 | 2e-08 | 41/49 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.8 | 6e-05 | 25/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +4.6 | 2e-04 | 24/48 (LoVo, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +4.1 | 0.001 | 20/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.6 | 0.011 | 10/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3603.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.216×** | -37.3 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.230×** | -35.7 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.260×** | -32.8 | 0e+00 | 47/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.416×** | -21.3 | 0e+00 | 48/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.602×** | -17.3 | 0e+00 | 45/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.532×** | -15.4 | 0e+00 | 42/49 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.542×** | -14.9 | 0e+00 | 45/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.573×** | -13.0 | 5e-37 | 38/44 (A-172, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.679×** | -9.4 | 3e-19 | 41/49 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.439×** | -9.2 | 2e-18 | 46/49 (NCI-H2347, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.704×** | -5.8 | 4e-07 | 28/45 (SW48, LS 180, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.865× | -3.5 | 0.020 | 20/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.731×** | -3.5 | 0.020 | 20/48 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.798×** | -3.5 | 0.020 | 21/47 (NCI-H1792, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.038 | 12/48 (NCI-H1573, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Olanzapine (drug)]] 5 µM |  | 0.909× | -3.2 | 0.038 | 3/48 (SNU-423, AN3 CA, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.879× | -3.1 | 0.054 | 10/49 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.883× | -3.0 | 0.074 | 11/48 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 116 | 12 (2 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +27.3) | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -25.0) |
| [[NCI-H460 (line)]] | wt | 86.0 | 8 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +36.9) | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -20.7) |
| [[LOX-IMVI (line)]] | wt | 105 | 6 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +21.9) | [[Panobinostat (drug)]] 5 µM 0.183× (z -23.1) |
| [[MIA PaCa-2 (line)]] | alt | 100 | 7 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +19.5) | [[Panobinostat (drug)]] 5 µM 0.120× (z -24.4) |
| [[NCI-H1573 (line)]] | alt | 124 | 8 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +27.9) | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -23.2) |
| [[NCI-H2347 (line)]] | alt | 94.4 | 5 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +28.9) | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -25.8) |
| [[A-172 (line)]] | wt | 67.8 | 6 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +29.7) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.275× (z -15.3) |
| [[C32 (line)]] | wt | 106 | 6 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +23.7) | [[Belinostat (drug)]] 5 µM 0.255× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 144 | 6 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +29.9) | [[Panobinostat (drug)]] 5 µM 0.201× (z -22.1) |
| [[A498 (line)]] | wt | 82.4 | 6 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +38.2) | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 115 | 6 | 6 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +25.6) | [[Panobinostat (drug)]] 5 µM 0.215× (z -23.3) |
| [[SW480 (line)]] | alt | 109 | 4 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +22.1) | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -27.7) |
| [[PANC-1 (line)]] | alt | 80.2 | 5 | 6 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +37.9) | [[Panobinostat (drug)]] 5 µM 0.184× (z -26.0) |
| [[RKO (line)]] | wt | 107 | 6 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +25.7) | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -17.3) |
| [[A549 (line)]] | wt | 86.7 | 5 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +31.9) | [[Panobinostat (drug)]] 5 µM 0.245× (z -16.5) |
| [[HOP62 (line)]] | alt | 60.4 | 5 | 5 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +27.6) | [[Panobinostat (drug)]] 5 µM 0.218× (z -19.3) |
| [[HS-578T (line)]] | alt | 69.0 | 5 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +26.7) | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 96.0 | 4 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +21.5) | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -20.8) |
| [[Panc 03.27 (line)]] | alt | 86.0 | 4 | 6 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +21.6) | [[Panobinostat (drug)]] 5 µM 0.137× (z -23.9) |
| [[RPMI-7951 (line)]] | alt | 118 | 4 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +20.9) | [[Panobinostat (drug)]] 5 µM 0.219× (z -17.6) |
| [[SNU-423 (line)]] | alt | 66.7 | 4 | 6 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +25.5) | [[Panobinostat (drug)]] 5 µM 0.191× (z -18.9) |
| [[SW 900 (line)]] | alt | 110 | 3 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +19.1) | [[Panobinostat (drug)]] 5 µM 0.164× (z -22.6) |
| [[SW1417 (line)]] | alt | 119 | 3 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +20.6) | [[Panobinostat (drug)]] 5 µM 0.160× (z -25.3) |
| [[A-427 (line)]] | wt | 63.6 | 5 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.309× (z -12.6) |
| [[BT-474 (line)]] | alt | 84.3 | 5 | 4 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +28.0) | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -18.8) |
| [[CFPAC-1 (line)]] | alt | 108 | 3 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +23.9) | [[Panobinostat (drug)]] 5 µM 0.174× (z -24.0) |
| [[J82 (line)]] | alt | 51.6 | 3 | 6 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +23.3) | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -15.7) |
| [[KATO III (line)]] | alt | 84.0 | 3 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.106× (z -27.4) |
| [[LS 180 (line)]] | wt | 110 | 2 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -19.3) |
| [[SNU-1 (line)]] | wt | 112 | 5 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +21.3) | [[Panobinostat (drug)]] 5 µM 0.202× (z -15.8) |
| [[hTERT-HPNE (line)]] | wt | 72.2 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 7.56× (z +25.6) | [[Panobinostat (drug)]] 5 µM 0.282× (z -11.5) |
| [[SW48 (line)]] | wt | 80.8 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +18.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0904× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.199× (z -13.9) |
| [[HCT15 (line)]] | alt | 126 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +18.5) | [[Panobinostat (drug)]] 5 µM 0.229× (z -14.9) |
| [[Hs 766T (line)]] | wt | 65.7 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +17.8) | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 138 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.235× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 90.3 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +20.4) | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -19.9) |
| [[AsPC-1 (line)]] | alt | 102 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.128× (z -25.4) |
| [[H4 (line)]] | wt | 72.8 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +19.6) | [[Panobinostat (drug)]] 5 µM 0.200× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 130 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -19.3) |
| [[HT-29 (line)]] | alt | 101 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.116× (z -25.1) |
| [[COLO 205 (line)]] | alt | 120 | 1 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.186× (z -18.1) |
| [[SHP-77 (line)]] | alt | 64.2 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.235× (z -14.7) |
| [[AN3 CA (line)]] | alt | 114 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.159× (z -12.4) |
| [[C-33 A (line)]] | alt | 78.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.296× (z -11.7) |
| [[SW 1271 (line)]] | alt | 94.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.142× (z -9.0) |
| [[CHP-212 (line)]] | wt | 83.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +11.0) | — |
| [[NCI-H596 (line)]] | alt | 93.8 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.122× (z -9.9) |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX4-DT]] | +0.83 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[ZFX]] | +0.80 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | +0.80 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.79 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[ERCC6L2-AS1]] | +0.79 | +0.78 / +0.30 | both halves | 2e-04 |  |
| [[TMEM202-AS1]] | +0.76 | +0.65 / +0.32 | both halves | 1e-04 |  |
| [[PPP3CB-AS1]] | +0.76 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[LATS1]] | +0.76 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[KRCC1]] | +0.76 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.75 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[NAIF1]] | +0.75 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[EP300]] | +0.75 | +0.54 / +0.65 | both halves | 1e-05 | pathway: Deubiquitination |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.75 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[HACE1]] | -0.73 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[SH3PXD2B]] | -0.70 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[RIMS3]] | -0.69 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[LPCAT4]] | -0.68 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[FAM118A]] | -0.68 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[GNA12]] | -0.67 | -0.61 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLFN5]] | C | SLFN5 activity weakens INO80D's drug response | lines that do not express SLFN5 (11) vs lines expressing it (38) | the lines without SLFN5 respond 0.89× as strongly (z diff -0.71); rises at some drug-doses, falls at others (28% from rises): Belinostat 5 µM: 0.25x vs 0.26x (z diff -1.7); Homoharringtonine 5 µM: 2.81x vs 3.99x (z diff -1.4); Panobinostat 0.5 µM: 0.28x vs 0.22x (z diff -1.2) | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.903). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (2.7, 9.3); signed map (21.4, -17.8). **Vector** length 123, 42.8% of its response variance represented; |z| ≥ 3 in 1,405 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chromatin organization* (reactome, mean cos +0.63 to 7); *Activation of HOX genes during differentiation* (reactome, mean cos +0.61 to 4); *Activation of anterior HOX genes in hindbrain development during early embryogenesis* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.8 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.7 | +22.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.5 | +44.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.4 | +27.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +11.0 | +15.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.3 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.4 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.6 | +3.0 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -9.8 | -21.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -9.0 | -14.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.4 | -32.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.1 | -17.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -6.6 | -9.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -3.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | INO80 complex subunit D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:205,993,721-206,086,303 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20309 |
| Gene groups (HGNC) | INO80 complex subunits |
| Reactome | 6 pathways, smallest: DNA Damage Recognition in GG-NER; UCH proteinases; Global Genome Nucleotide Excision Repair (GG-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53TQ3](https://www.uniprot.org/uniprotkb/Q53TQ3) (INO80 complex subunit D):

> Putative regulatory component of the chromatin remodeling INO80 complex which is involved in transcriptional regulation, DNA replication and probably DNA repair.

**Summary**, from NCBI Gene [54891](https://www.ncbi.nlm.nih.gov/gene/54891):

> Involved in several processes, including positive regulation of DNA-templated transcription; regulation of DNA metabolic process; and regulation of chromosome organization. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25997) · Entrez [54891](https://www.ncbi.nlm.nih.gov/gene/54891) · UniProt [Q53TQ3](https://www.uniprot.org/uniprotkb/Q53TQ3) · Ensembl [ENSG00000114933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114933)

## Data

Gene col 3603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3603); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3603]; `tensor/DDL_lfc|DDL_z.npy` [3603]; `embed/gene_vectors.npy` [3603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3603 or target_col == 3603). Every well: [[INO80D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INO80D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
