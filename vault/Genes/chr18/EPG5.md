---
symbol: "EPG5"
type: "gene"
col: 7604
ensembl_id: "ENSG00000152223"
name: "ectopic P-granules 5 autophagy tethering factor"
location: "18q12.3-q21.1"
module: 76
arm: "+"
pooled_cpm: 102.39
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# EPG5

*ectopic P-granules 5 autophagy tethering factor* — 18q12.3-q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.22× (z +22.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.449× (z -15.4, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.624× (z -3.6, q 0.027, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LS 180 0.148×, SNU-423 0.168×, Panc 03.27 0.239×, HCT15 0.178×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2030 0.202×, NCI-H1573 0.299×, Hs 766T 0.231×, A-427 0.264×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.0948×, NCI-H2030 0.303×; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 1 line (LoVo 0.626×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPC2]] (+0.51, fdr 5e-05), [[RB1CC1]] (+0.50, fdr 2e-05), [[ERBIN]] (+0.50, fdr 3e-05); moves opposite to [[LOXL1]] (-0.38, fdr 2e-04), [[BRMS1L]] (-0.38, fdr 4e-04), [[KLHL2]] (-0.37, fdr 4e-04).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7604.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.22×** | +22.3 | 0e+00 | 48/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +18.9 | 0e+00 | 45/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +15.4 | 0e+00 | 46/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +14.4 | 1e-44 | 45/48 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.07×** | +13.9 | 1e-41 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.10×** | +13.8 | 2e-41 | 44/49 (NCI-H1573, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.04×** | +13.6 | 5e-40 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +11.3 | 8e-28 | 42/48 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +11.2 | 2e-27 | 43/48 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +9.2 | 2e-18 | 36/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.97×** | +8.3 | 5e-15 | 41/48 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +7.3 | 2e-11 | 28/48 (hTERT-HPNE, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.6 | 1e-06 | 30/47 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +5.3 | 5e-06 | 28/48 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.0 | 2e-05 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +4.6 | 1e-04 | 25/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.3 | 5e-04 | 26/48 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +4.3 | 5e-04 | 25/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7604.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LS 180 0.148×, SNU-423 0.168×, Panc 03.27 0.239×, HCT15 0.178×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2030 0.202×, NCI-H1573 0.299×, Hs 766T 0.231×, A-427 0.264×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.0948×, NCI-H2030 0.303×; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 1 line (LoVo 0.626×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.449×** | -15.4 | 0e+00 | 45/49 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.500×** | -12.8 | 5e-35 | 39/44 (LS 180, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -7.9 | 6e-13 | 26/45 (SW48, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.687×** | -7.2 | 7e-11 | 30/48 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.799×** | -4.2 | 0.003 | 26/47 (NCI-H23, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.624×** | -3.6 | 0.027 | 21/48 (LoVo, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~11% of this change | 0.841× | -3.4 | 0.061 | 20/48 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.3 | 0.070 | 19/49 (CHP-212, LoVo, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.850× | -3.2 | 0.10 | 13/47 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.852× | -3.1 | 0.10 | 15/48 (Panc 03.27, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.894× | -3.1 | 0.10 | 16/48 (LoVo, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 0.677× | -3.0 | 0.13 | 17/48 (LoVo, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 58.1 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +28.2) | — |
| [[HS-578T (line)]] | alt | 87.2 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +23.7) | — |
| [[NCI-H460 (line)]] | wt | 83.1 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 106 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +23.2) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 207 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.23× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 114 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -12.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 159 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -16.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 61.2 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.58× (z +18.3) | — |
| [[SNU-423 (line)]] | alt | 135 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -19.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 103 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -9.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 116 | 3 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.626× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 103 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.81× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -14.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 100 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.11× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -11.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 109 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -12.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 82.7 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +21.7) | — |
| [[HepG2_C3A (line)]] | wt | 82.8 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 36.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.7 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.88× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 126 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 271 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -18.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 47.9 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -12.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 59.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -13.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 100 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 86.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.11× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -9.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 78.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -10.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 73.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.42× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 103 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.8) | — |
| [[SK-MEL-2 (line)]] | alt | 139 | 5 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.60× (z +10.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 98.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -14.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 282 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 83.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -20.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 143 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 101 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 76.7 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.19× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0948× (z -16.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 120 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -8.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 99.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.64× (z +9.9) | — |
| [[C32 (line)]] | wt | 89.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -8.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 99.0 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.02× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 55.1 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 72.5 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +10.9) | — |
| [[A549 (line)]] | wt | 67.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -16.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 91.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 8 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPC2]] | +0.51 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[RB1CC1]] | +0.50 | +0.51 / +0.48 | both halves | 2e-05 | STRING 617 |
| [[ERBIN]] | +0.50 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[GABARAPL2]] | +0.50 | +0.52 / +0.32 | both halves | 2e-04 | STRING 571 |
| [[MICU1]] | +0.49 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[CCN1]] | +0.48 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[CHMP1B]] | +0.47 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[CREBRF]] | +0.47 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CALCOCO1]] | +0.47 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[ARHGEF28]] | +0.46 | +0.43 / +0.51 | both halves | 4e-05 |  |
| [[ATG2A]] | +0.46 | +0.35 / +0.34 | both halves | 1e-04 | STRING 587 |
| [[GABARAP]] ⚠ | +0.46 | +0.47 / +0.38 | both halves | 7e-05 | STRING 547; ⚠ in the vector space only through flagged drug-doses |
| [[YPEL3]] | +0.46 | +0.45 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LOXL1]] | -0.38 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[BRMS1L]] | -0.38 | -0.26 / -0.32 | both halves | 4e-04 |  |
| [[KLHL2]] | -0.37 | -0.37 / -0.24 | both halves | 4e-04 |  |
| [[RAB27A]] | -0.37 | -0.18 / -0.35 | ⚠ not reproduced | 9e-04 |  |
| [[ANKUB1]] | -0.37 | -0.39 / -0.26 | both halves | 4e-04 |  |
| [[SSX2IP]] | -0.37 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[IDE]] | -0.37 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[UBA5]] | -0.37 | -0.36 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.3, -48.5); signed map (-14.5, 8.0). **Vector** length 82.3, 25.5% of its response variance represented; |z| ≥ 3 in 1,286 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +3.6 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.5 | +22.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +14.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +11.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +1.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.9 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.7 | -7.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ectopic P-granules 5 autophagy tethering factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.3-q21.1 — chr18:45,800,581-45,967,329 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hEPG5; previously KIAA1632 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCE0](https://www.uniprot.org/uniprotkb/Q9HCE0) (Ectopic P granules protein 5 homolog):

> Involved in autophagy. May play a role in a late step of autophagy, such as clearance of autophagosomal cargo. Plays a key role in innate and adaptive immune response triggered by unmethylated cytidine-phosphate-guanosine (CpG) dinucleotides from pathogens, and mediated by the nucleotide-sensing receptor TLR9. It is necessary for the translocation of CpG dinucleotides from early endosomes to late endosomes and lysosomes, where TLR9 is located.

**Summary**, from NCBI Gene [57724](https://www.ncbi.nlm.nih.gov/gene/57724):

> This gene encodes a large coiled coil domain-containing protein that functions in autophagy during starvation conditions. Mutations in this gene cause Vici syndrome. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:29331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29331) · Entrez [57724](https://www.ncbi.nlm.nih.gov/gene/57724) · UniProt [Q9HCE0](https://www.uniprot.org/uniprotkb/Q9HCE0) · Ensembl [ENSG00000152223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152223)

## Data

Gene col 7604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7604); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7604]; `tensor/DDL_lfc|DDL_z.npy` [7604]; `embed/gene_vectors.npy` [7604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7604 or target_col == 7604). Every well: [[EPG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
