---
symbol: "MARK3"
type: "gene"
col: 1118
ensembl_id: "ENSG00000075413"
name: "microtubule affinity regulating kinase 3"
location: "14q32.32-q32.33"
module: 136
arm: "+"
pooled_cpm: 264.2
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 11
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# MARK3

*microtubule affinity regulating kinase 3* — 14q32.32-q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.26× (z +15.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.506× (z -13.3, q 2e-37, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.668× (z -11.1, q 1e-26, down in 44 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A549 0.427×, C32 0.424×, hTERT-HPNE 0.451×, HOP62 0.488×, …); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SK-MEL-2 0.209×, C32 0.249×, RKO 0.300×, NCI-H1792 0.328×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SK-MEL-2 0.271×, C32 0.268×, AsPC-1 0.298×, hTERT-HPNE 0.312×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO9B]] (+0.61, fdr 3e-05), [[ATG4B]] (+0.60, fdr 1e-04), [[TECPR1]] (+0.59, fdr 1e-04); moves opposite to [[UBAP2L]] (-0.57, fdr 2e-04), [[C5orf15]] (-0.56, fdr 1e-04), [[MBNL3]] (-0.54, fdr 4e-04).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.26×** | +15.8 | 0e+00 | 48/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +13.6 | 2e-39 | 46/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +11.6 | 1e-28 | 41/48 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +11.0 | 7e-26 | 46/48 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +10.6 | 4e-24 | 48/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.71×** | +10.4 | 3e-23 | 47/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.56×** | +9.6 | 1e-19 | 45/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +6.6 | 3e-09 | 38/47 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +6.2 | 4e-08 | 37/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +6.1 | 8e-08 | 35/48 (J82, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.6 | 1e-06 | 33/48 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.6 | 1e-06 | 35/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +4.7 | 9e-05 | 34/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 2e-04 | 29/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 3e-04 | 30/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.002 | 16/49 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.009 | 24/49 (SNU-423, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1118.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A549 0.427×, C32 0.424×, hTERT-HPNE 0.451×, HOP62 0.488×, …); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SK-MEL-2 0.209×, C32 0.249×, RKO 0.300×, NCI-H1792 0.328×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SK-MEL-2 0.271×, C32 0.268×, AsPC-1 0.298×, hTERT-HPNE 0.312×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.506×** | -13.3 | 2e-37 | 46/49 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -13.1 | 2e-36 | 40/44 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.536×** | -11.2 | 5e-27 | 44/45 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -11.1 | 1e-26 | 44/49 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.655×** | -7.9 | 2e-13 | 39/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.804×** | -6.0 | 2e-07 | 29/48 (NCI-H2347, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.763×** | -5.3 | 1e-05 | 34/48 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.803×** | -4.3 | 0.001 | 27/48 (C32, hTERT-HPNE, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.812×** | -3.9 | 0.005 | 25/50 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.813×** | -3.9 | 0.005 | 24/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.820×** | -3.9 | 0.005 | 25/48 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.7 | 0.008 | 9/48 (CFPAC-1, AN3 CA, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.840× | -3.4 | 0.029 | 21/48 (CHP-212, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.847× | -3.2 | 0.048 | 15/47 (A498, SW 900, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.852× | -3.2 | 0.048 | 20/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.850× | -3.2 | 0.052 | 21/48 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.062 | 17/47 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.855× | -3.1 | 0.068 | 14/48 (SNU-423, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 230 | 8 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -11.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 319 | 5 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -10.6) |
| [[SNU-1 (line)]] | wt | 229 | 9 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -9.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 273 | 8 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 379 | 6 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 314 | 6 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +21.7) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -12.8) |
| [[PANC-1 (line)]] | alt | 209 | 7 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -9.4) |
| [[RKO (line)]] | wt | 304 | 6 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -10.2) |
| [[C32 (line)]] | wt | 454 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 243 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -12.6) |
| [[H4 (line)]] | wt | 139 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 158 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +12.7) | — |
| [[hTERT-HPNE (line)]] | wt | 290 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -13.9) |
| [[LoVo (line)]] | wt | 214 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -12.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 245 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.506× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 415 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 183 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.502× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 320 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.75× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 337 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.454× (z -9.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 238 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.84× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +15.3) | — |
| [[COLO 205 (line)]] | alt | 102 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 339 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -13.0) |
| [[KATO III (line)]] | alt | 180 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 255 | 2 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.01× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -11.5) |
| [[SHP-77 (line)]] | alt | 220 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 339 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -12.7) |
| [[SNU-423 (line)]] | alt | 189 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.43× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 228 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +11.9) | — |
| [[HCT15 (line)]] | alt | 315 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 222 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.16× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 252 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -9.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 370 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.23× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.359× (z -11.8) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 315 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -12.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 248 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -12.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 285 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.37× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -11.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 167 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -9.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 259 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 380 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -15.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 201 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.484× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 241 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -9.8) |
| [[A-172 (line)]] | wt | 154 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -11.8) |
| [[SW48 (line)]] | wt | 688 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -11.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 227 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -10.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.391× (z -9.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 260 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 344 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | +0.61 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ATG4B]] | +0.60 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[TECPR1]] | +0.59 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[KCTD20]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[GIPC1]] | +0.57 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[TMEM184B]] | +0.57 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[ARID3B]] | +0.56 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[FAM89B]] | +0.56 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[SPIRE1]] | +0.55 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[SH3BGRL3]] | +0.54 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[CSNK1E]] | +0.54 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[MAP3K9]] | +0.54 | +0.54 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBAP2L]] | -0.57 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[C5orf15]] | -0.56 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[MBNL3]] | -0.54 | -0.51 / -0.25 | both halves | 4e-04 |  |
| [[RBM7]] | -0.53 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[SNX5]] | -0.51 | -0.52 / -0.24 | both halves | 5e-04 |  |
| [[DECR1]] | -0.50 | -0.51 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[HFE]] | -0.50 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[CA5BP1-1]] | -0.50 | -0.13 / -0.42 | ⚠ not reproduced | 0.002 |  |
| [[MCCC2]] | -0.50 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[NNT]] | -0.49 | -0.35 / -0.25 | both halves | 4e-04 | pathway: HALLMARK_HEME_METABOLISM |
| [[ARFGAP2]] | -0.49 | -0.57 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[RCBTB2]] | -0.49 | -0.49 / -0.21 | both halves | 6e-04 |  |
| [[DDX3X]] | -0.48 | -0.47 / -0.21 | both halves | 7e-04 |  |
| [[FUBP1]] | -0.48 | -0.33 / -0.26 | both halves | 4e-04 |  |
| [[TMX4]] | -0.47 | -0.44 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MARK3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.7, 2.9); signed map (-29.3, 14.1). **Vector** length 85.6, 34.8% of its response variance represented; |z| ≥ 3 in 1,629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.6 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +0.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.7 | +1.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -6.7 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -11.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.9 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.5 | -4.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.8 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.7 | -0.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.3 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -0.3 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.8 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | microtubule affinity regulating kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.32-q32.33 — chr14:103,385,377-103,503,831 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CTAK1, KP78, PAR-1A |
| Gene groups (HGNC) | Microtubule affinity regulating kinases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 17 pathways, smallest: RAF activation; Signaling by high-kinase activity BRAF mutants; MAP2K and MAPK activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P27448](https://www.uniprot.org/uniprotkb/P27448) (MAP/microtubule affinity-regulating kinase 3):

> Serine/threonine-protein kinase. Involved in the specific phosphorylation of microtubule-associated proteins for MAP2 and MAP4. Phosphorylates the microtubule-associated protein MAPT/TAU. Phosphorylates CDC25C on 'Ser-216'. Regulates localization and activity of some histone deacetylases by mediating phosphorylation of HDAC7, promoting subsequent interaction between HDAC7 and 14-3-3 and export from the nucleus. Regulates localization and activity of MITF by mediating its phosphorylation, …

**Summary**, from NCBI Gene [4140](https://www.ncbi.nlm.nih.gov/gene/4140):

> The protein encoded by this gene is activated by phosphorylation and in turn is involved in the phosphorylation of tau proteins MAP2 and MAP4. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:6897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6897) · Entrez [4140](https://www.ncbi.nlm.nih.gov/gene/4140) · UniProt [P27448](https://www.uniprot.org/uniprotkb/P27448) · Ensembl [ENSG00000075413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075413)

## Data

Gene col 1118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1118); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1118]; `tensor/DDL_lfc|DDL_z.npy` [1118]; `embed/gene_vectors.npy` [1118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1118 or target_col == 1118). Every well: [[MARK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
