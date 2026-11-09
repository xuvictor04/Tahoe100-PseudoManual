---
symbol: "PNRC2"
type: "gene"
col: 12110
ensembl_id: "ENSG00000189266"
name: "proline rich nuclear receptor coactivator 2"
location: "1p36.11"
module: 40
arm: "-"
pooled_cpm: 32.53
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# PNRC2

*proline rich nuclear receptor coactivator 2* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.12× (z +30.5, q 0e+00, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.96× (z +19.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Lonafarnib (drug)]] 5 µM: 0.589× (z -5.2, q 9e-05, down in 17 of 33 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.775× (z -4.8, q 3e-04, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK1IP1L]] (+0.70, fdr 7e-06), [[SKIL]] (+0.69, fdr 7e-06), [[ZNF776]] (+0.68, fdr 7e-06); moves opposite to [[SEC63]] (-0.70, fdr 7e-06), [[ANKRD27]] (-0.70, fdr 7e-06), [[COG5]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.12×** | +30.5 | 0e+00 | 46/47 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.96×** | +19.8 | 0e+00 | 47/48 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.36×** | +16.3 | 0e+00 | 45/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +15.9 | 0e+00 | 46/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +15.7 | 0e+00 | 41/47 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.91×** | +12.2 | 2e-32 | 42/48 (HS-578T, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +11.8 | 2e-30 | 37/45 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.76×** | +10.5 | 4e-24 | 39/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.59×** | +8.6 | 3e-16 | 33/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +7.3 | 1e-11 | 32/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.46×** | +6.7 | 1e-09 | 23/42 (PANC-1, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.42×** | +6.6 | 2e-09 | 30/45 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.37×** | +5.7 | 6e-07 | 25/47 (NCI-H2030, A-427, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.58×** | +4.6 | 2e-04 | 22/48 (NCI-H1573, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.3 | 6e-04 | 20/47 (HS-578T, AsPC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.009 | 14/47 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.011 | 12/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cilostazol (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.018 | 10/47 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Piroxicam (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.027 | 6/48 (CFPAC-1, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.027 | 11/44 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.032 | 9/48 (HCT15, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.047 | 8/47 (SW1417, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.056 | 8/45 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +2.9 | 0.071 | 10/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12110.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.589×** | -5.2 | 9e-05 | 17/33 (HT-29, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.775×** | -4.8 | 3e-04 | 20/48 (J82, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.775×** | -4.8 | 3e-04 | 24/47 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.784×** | -4.6 | 6e-04 | 21/48 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -4.4 | 0.001 | 3/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.811×** | -4.0 | 0.007 | 18/48 (SW48, LoVo, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.676×** | -3.9 | 0.008 | 17/48 (MIA PaCa-2, C-33 A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.827×** | -3.4 | 0.047 | 17/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.887× | -3.2 | 0.086 | 11/48 (A-427, HT-29, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 31.7 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.56× (z +16.1) | — |
| [[BT-474 (line)]] | alt | 33.5 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 29.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +21.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.24× (z +16.2) | — |
| [[KATO III (line)]] | alt | 52.5 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.62× (z +14.3) | — |
| [[SW480 (line)]] | alt | 42.2 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +11.5) | [[Lonafarnib (drug)]] 5 µM 0.218× (z -9.1) ⚠ toxic |
| [[LS 180 (line)]] | wt | 64.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 31.8 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.27× (z +13.0) | — |
| [[AsPC-1 (line)]] | alt | 30.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +21.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.58× (z +13.6) | — |
| [[C32 (line)]] | wt | 22.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +17.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.50× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +16.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.06× (z +12.6) | [[Lonafarnib (drug)]] 5 µM 0.142× (z -9.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 27.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.56× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 22.1 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.65× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +11.0) | — |
| [[RKO (line)]] | wt | 46.8 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.13× (z +12.9) | — |
| [[A498 (line)]] | wt | 15.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.53× (z +10.9) | — |
| [[A549 (line)]] | wt | 19.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.88× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 35.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +17.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.27× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +15.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.36× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 37.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 34.2 | 0 | 2 (1 ⚠) | — | [[Oxaprozin (drug)]] 0.5 µM 0.0789× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 35.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +16.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.16× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 41.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.89× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 49.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +15.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Lonafarnib (drug)]] 5 µM 0.122× (z -9.9) ⚠ toxic |
| [[J82 (line)]] | alt | 40.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +19.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.32× (z +13.1) | — |
| [[LoVo (line)]] | wt | 38.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +18.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.07× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.74× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 20.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[Panc 03.27 (line)]] | alt | 26.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.57× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 24.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +16.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.68× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 23.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.21× (z +9.1) | — |
| [[A-172 (line)]] | wt | 14.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[COLO 205 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +11.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HEC-1-A (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[Hs 766T (line)]] | wt | 33.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +14.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.0) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H2347 (line)]] | alt | 24.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0586× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +11.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 34.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.65× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 39.0 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.87× (z +8.5) | — |
| [[SW48 (line)]] | wt | 30.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK1IP1L]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SKIL]] | +0.69 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[ZNF776]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ZNF518A]] | +0.68 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[EP300]] | +0.67 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[FAM200A]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.64 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ZNF764]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[FAM111A]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[VEZF1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MEPCE]] | +0.63 | +0.59 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC63]] | -0.70 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[ANKRD27]] | -0.70 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[COG5]] | -0.69 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[TMEM120B]] | -0.67 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[SEC23A]] | -0.66 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[NBAS]] | -0.66 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[STRAP]] | -0.65 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.65 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[DYM]] | -0.64 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[MMS19]] | -0.64 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[OXNAD1]] | -0.64 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | -0.64 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PNRC2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.3, -21.5); signed map (15.0, -10.4). **Vector** length 93.3, 22.1% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +19.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.4 | +30.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.3 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +7.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.4 | +1.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | -5.2 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | +0.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.9 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | proline rich nuclear receptor coactivator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:23,956,839-23,963,462 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 3 pathways, smallest: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); Nonsense-Mediated Decay (NMD); Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPJ4](https://www.uniprot.org/uniprotkb/Q9NPJ4) (Proline-rich nuclear receptor coactivator 2):

> Involved in nonsense-mediated mRNA decay (NMD) by acting as a bridge between the mRNA decapping complex and the NMD machinery. May act by targeting the NMD machinery to the P-body and recruiting the decapping machinery to aberrant mRNAs. Required for UPF1/RENT1 localization to the P-body. Plays a role in glucocorticoid receptor-mediated mRNA degradation by interacting with the glucocorticoid receptor NR3C1 in a ligand-dependent manner when it is bound to the 5' UTR of target mRNAs and …

**Summary**, from NCBI Gene [55629](https://www.ncbi.nlm.nih.gov/gene/55629):

> Involved in nuclear-transcribed mRNA catabolic process, nonsense-mediated decay. Located in P-body and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23158) · Entrez [55629](https://www.ncbi.nlm.nih.gov/gene/55629) · UniProt [Q9NPJ4](https://www.uniprot.org/uniprotkb/Q9NPJ4) · Ensembl [ENSG00000189266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189266)

## Data

Gene col 12110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12110); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12110]; `tensor/DDL_lfc|DDL_z.npy` [12110]; `embed/gene_vectors.npy` [12110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12110 or target_col == 12110). Every well: [[PNRC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNRC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
