---
symbol: "CUL3"
type: "gene"
col: 436
ensembl_id: "ENSG00000036257"
name: "cullin 3"
location: "2q36.2"
module: 3
arm: "+"
pooled_cpm: 294.01
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CUL3

*cullin 3* — 2q36.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.43× (z +16.5, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.425× (z -17.5, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.623× (z -10.0, q 2e-21, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACVR2A]] (+0.55, fdr 2e-05), [[SETD5]] (+0.53, fdr 1e-05), [[LRP6]] (+0.52, fdr 9e-05); moves opposite to [[RSC1A1]] (-0.59, fdr 4e-05), [[SMYD5]] (-0.47, fdr 3e-05), [[ZPR1]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.43×** | +16.5 | 0e+00 | 49/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.05×** | +15.2 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +14.2 | 1e-43 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.47×** | +13.8 | 3e-41 | 47/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +12.1 | 9e-32 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +10.4 | 1e-23 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.31×** | +8.1 | 5e-14 | 32/48 (A498, A549, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +6.0 | 2e-07 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.9 | 3e-07 | 30/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +4.7 | 2e-04 | 29/48 (A549, NCI-H460, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +4.4 | 6e-04 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 26/48 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.9 | 0.004 | 23/38 (NCI-H1573, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.425×** | -17.5 | 0e+00 | 44/44 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.469×** | -16.1 | 0e+00 | 49/49 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.623×** | -10.0 | 2e-21 | 43/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.628×** | -9.9 | 7e-21 | 43/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -9.5 | 3e-19 | 37/49 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.666×** | -8.0 | 1e-13 | 28/45 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.741×** | -6.4 | 2e-08 | 37/48 (A549, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.736×** | -6.3 | 3e-08 | 34/47 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.785×** | -5.2 | 2e-05 | 30/48 (A549, BT-474, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.788×** | -5.1 | 2e-05 | 31/48 (SW 1271, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.871× | -4.2 | 0.002 | 13/48 (A549, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.827×** | -4.1 | 0.002 | 25/48 (BT-474, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.828×** | -4.0 | 0.003 | 22/48 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.830×** | -3.8 | 0.006 | 26/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.832×** | -3.8 | 0.006 | 26/50 (BT-474, SNU-423, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.769×** | -3.7 | 0.009 | 32/47 (J82, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.873× | -2.9 | 0.096 | 18/48 (PANC-1, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 330 | 12 (5 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 4.15× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -13.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 340 | 6 (3 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +18.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.08× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -28.7) |
| [[BT-474 (line)]] | alt | 286 | 9 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.521× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.583× (z -8.5) |
| [[LoVo (line)]] | wt | 258 | 7 (2 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.50× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.541× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.571× (z -10.6) |
| [[PANC-1 (line)]] | alt | 291 | 6 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -14.0) |
| [[SW480 (line)]] | alt | 274 | 9 (2 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.48× (z +21.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -12.0) |
| [[SW 900 (line)]] | alt | 377 | 6 (1 ⚠) | 5 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.28× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.501× (z -9.6) |
| [[HOP62 (line)]] | alt | 320 | 6 (1 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.76× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.461× (z -10.8) |
| [[HS-578T (line)]] | alt | 207 | 7 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.12× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -9.2) |
| [[HT-29 (line)]] | alt | 311 | 5 (1 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.43× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.508× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 309 | 6 (2 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.50× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.97× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.530× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 291 | 5 (1 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.52× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 369 | 6 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -15.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 443 | 5 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.83× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.567× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 284 | 4 (1 ⚠) | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.67× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.653× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 332 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +16.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -13.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 375 | 3 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.451× (z -9.7) |
| [[H4 (line)]] | wt | 274 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.94× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 196 | 5 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.33× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -10.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 230 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +18.1) | [[Dinaciclib (drug)]] 0.05 µM 0.404× (z -13.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 382 | 4 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.60× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 325 | 3 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.29× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.552× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 339 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -14.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 294 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -13.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 266 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.38× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 213 | 2 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.77× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -12.6) |
| [[C-33 A (line)]] | alt | 266 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.10× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 346 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.52× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -16.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 271 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.507× (z -9.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 249 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.72× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -12.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 283 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.43× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.500× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 294 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -21.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 260 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.71× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -12.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 302 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.57× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 301 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -11.1) |
| [[A498 (line)]] | wt | 233 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +19.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.366× (z -13.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 431 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 10.6× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -17.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 286 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.78× (z +13.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.534× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 271 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.24× (z +10.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.40× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -12.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 257 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.97× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.538× (z -9.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 345 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -10.5) |
| [[A-427 (line)]] | wt | 260 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.35× (z +13.0) | — |
| [[J82 (line)]] | alt | 154 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -9.6) |
| [[SW 1271 (line)]] | alt | 358 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -17.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 267 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.79× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 293 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 11 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACVR2A]] | +0.55 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[SETD5]] | +0.53 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LRP6]] | +0.52 | +0.36 / +0.54 | both halves | 9e-05 | pathway: Signaling by WNT |
| [[FBXO11]] | +0.50 | +0.59 / +0.44 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 559 |
| [[IST1]] | +0.50 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CTNNB1]] | +0.50 | +0.43 / +0.44 | both halves | 3e-05 | pathway: Co-inhibition by PD-1; STRING 639 |
| [[IP6K2]] | +0.49 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[PAN3]] | +0.49 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PUM1]] | +0.49 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[PPP3R1]] | +0.48 | +0.58 / +0.42 | both halves | 4e-05 | pathway: Signaling by WNT |
| [[RHEB]] | +0.48 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[TYW1B]] | +0.48 | +0.27 / +0.31 | both halves | 3e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSC1A1]] | -0.59 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[SMYD5]] | -0.47 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZPR1]] | -0.46 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[FLII]] | -0.46 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[DNAJC13]] | -0.45 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[ZNG1B]] | -0.45 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CDC16]] | -0.44 | -0.24 / -0.35 | both halves | 5e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[MAPK7]] | -0.44 | -0.17 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[ELK4]] | -0.43 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[SIKE1]] | -0.43 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[TPD52L2]] | -0.43 | -0.09 / -0.42 | ⚠ not reproduced | 0.003 |  |
| [[EIF2B1]] | -0.42 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[ZBTB41]] | -0.41 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[MSANTD7]] | -0.41 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.0662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-0.5, -35.7); signed map (-26.6, 24.6). **Vector** length 73.4, 27.5% of its response variance represented; |z| ≥ 3 in 1,432 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | -0.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.1 | +16.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | -2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.9 | +0.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | cullin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.2 — chr2:224,470,150-224,585,397 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cullins |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 32 pathways, smallest: RHOBTB3 ATPase cycle; RHOBTB1 GTPase cycle; RHOBTB2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13618](https://www.uniprot.org/uniprotkb/Q13618) (Cullin-3):

> Core component of multiple cullin-RING-based BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complexes which mediate the ubiquitination and subsequent proteasomal degradation of target proteins. BCR complexes and ARIH1 collaborate in tandem to mediate ubiquitination of target proteins. As a scaffold protein may contribute to catalysis through positioning of the substrate and the ubiquitin-conjugating enzyme. The E3 ubiquitin-protein ligase activity of the complex is dependent on the neddylation …

**Summary**, from NCBI Gene [8452](https://www.ncbi.nlm.nih.gov/gene/8452):

> This gene encodes a member of the cullin protein family. The encoded protein plays a critical role in the polyubiquitination and subsequent degradation of specific protein substrates as the core component and scaffold protein of an E3 ubiquitin ligase complex. Complexes including the encoded protein may also play a role in late endosome maturation. Mutations in this gene are a cause of type 2E pseudohypoaldosteronism. Alternatively spliced transcript variants encoding multiple isoforms have …

**Accessions** — [HGNC:2553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2553) · Entrez [8452](https://www.ncbi.nlm.nih.gov/gene/8452) · UniProt [Q13618](https://www.uniprot.org/uniprotkb/Q13618) · Ensembl [ENSG00000036257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000036257)

## Data

Gene col 436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 436); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 436]; `tensor/DDL_lfc|DDL_z.npy` [436]; `embed/gene_vectors.npy` [436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 436 or target_col == 436). Every well: [[CUL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
