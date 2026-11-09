---
symbol: "KDM5B"
type: "gene"
col: 3877
ensembl_id: "ENSG00000117139"
name: "lysine demethylase 5B"
location: "1q32.1"
module: 4
arm: "-"
pooled_cpm: 244.97
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# KDM5B

*lysine demethylase 5B* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.41× (z +25.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.311× (z -23.1, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.736× (z -6.1, q 1e-07, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM7-AS2]] (+0.69, fdr 7e-06), [[ACAP1]] (+0.68, fdr 7e-06), [[AFTPH]] (+0.65, fdr 7e-06); moves opposite to [[EFTUD2]] (-0.67, fdr 7e-06), [[CHCHD3]] (-0.66, fdr 7e-06), [[TMEM33]] (-0.66, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRABP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.41×** | +25.5 | 0e+00 | 46/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +19.4 | 0e+00 | 45/49 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +13.6 | 1e-39 | 39/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.47×** | +13.3 | 2e-38 | 48/49 (RKO, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.61×** | +9.3 | 1e-18 | 37/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +8.8 | 9e-17 | 41/48 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +6.4 | 1e-08 | 38/49 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +6.2 | 3e-08 | 27/48 (NCI-H460, HCT15, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.0 | 1e-07 | 29/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.27×** | +4.8 | 8e-05 | 30/48 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **1.24×** | +4.4 | 5e-04 | 25/48 (PANC-1, BT-474, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.027 | 22/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.068 | 22/48 (C32, A-172, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.069 | 20/48 (CFPAC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.069 | 25/48 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 1.17× | +3.1 | 0.074 | 16/48 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.094 | 18/48 (C32, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3877.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.311×** | -23.1 | 0e+00 | 43/44 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.338×** | -22.3 | 0e+00 | 46/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.406×** | -17.1 | 0e+00 | 41/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.674×** | -8.1 | 6e-14 | 45/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -6.6 | 4e-09 | 36/47 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.719×** | -6.5 | 5e-09 | 35/47 (NCI-H2347, SW 1271, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.736×** | -6.1 | 1e-07 | 35/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.761×** | -5.6 | 1e-06 | 33/48 (NCI-H1573, SW 900, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.767×** | -5.5 | 3e-06 | 31/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.773×** | -5.3 | 6e-06 | 27/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.793×** | -4.8 | 9e-05 | 34/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -4.1 | 0.002 | 17/48 (AN3 CA, A-172, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.823×** | -3.9 | 0.005 | 25/49 (LS 180, CFPAC-1, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.8 | 0.006 | 10/48 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.879× | -3.8 | 0.006 | 12/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.831×** | -3.7 | 0.009 | 22/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.717×** | -3.6 | 0.011 | 25/48 (AsPC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.837× | -3.5 | 0.014 | 21/49 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.845× | -3.3 | 0.026 | 16/48 (Panc 03.27, A-427, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.746×** | -3.2 | 0.045 | 20/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.857× | -3.1 | 0.059 | 20/48 (SW1417, CFPAC-1, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 0.865× | -3.0 | 0.066 | 13/48 (A549, HepG2/C3A, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.757×** | -3.0 | 0.066 | 18/48 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.868× | -2.9 | 0.077 | 18/48 (NCI-H2347, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 204 | 10 (3 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +33.5) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -21.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 498 | 1 | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -33.6) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.530× (z -9.7) |
| [[PANC-1 (line)]] | alt | 222 | 7 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +23.1) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -15.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 404 | 5 (2 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.86× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -14.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 516 | 4 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -24.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 519 | 4 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -19.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 545 | 2 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -28.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 304 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +21.7) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -16.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 217 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +21.6) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -15.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 259 | 4 (1 ⚠) | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -24.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 328 | 4 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.498× (z -9.3) |
| [[RKO (line)]] | wt | 146 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +22.3) | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -19.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 212 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +23.5) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -15.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 196 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 258 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 181 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +27.9) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -20.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 193 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +24.5) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -13.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 297 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -26.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 219 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -18.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 146 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.430× (z -11.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 278 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -18.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 240 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -17.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 293 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -17.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 136 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -14.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 206 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -11.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 276 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -15.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 232 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -15.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 163 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 279 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -19.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 370 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -17.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 344 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.0912× (z -28.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 134 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 181 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 226 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -11.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 165 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 280 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -18.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 99.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +18.9) | — |
| [[AN3 CA (line)]] | alt | 495 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -14.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 315 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -14.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 123 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +13.9) | — |
| [[NCI-H661 (line)]] | alt | 365 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -16.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 203 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -17.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 115 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +13.2) | — |
| [[KATO III (line)]] | alt | 108 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +18.5) | — |
| [[SHP-77 (line)]] | alt | 190 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -19.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 99.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +14.3) | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.163× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[SW 1088 (line)]] | alt | 277 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 321 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 272 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM7-AS2]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ACAP1]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[AFTPH]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[WBP1]] | +0.65 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.65 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[ZNF395]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[RIOK3]] | +0.64 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[MXI1]] | +0.64 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[LCA5]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[VASN]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 | same gene group; STRING 512 |
| [[RSBN1]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | -0.67 | -0.59 / -0.67 | both halves | 7e-06 | STRING 447 |
| [[CHCHD3]] | -0.66 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.66 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[HERC2]] | -0.66 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[INTS7]] | -0.65 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[RTEL1]] | -0.64 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[ELAC2]] | -0.64 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[HERC2P9-1]] | -0.64 | -0.57 / -0.65 | both halves | 8e-06 |  |
| [[IPO9]] | -0.64 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[LETM1]] | -0.63 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[GFM1]] | -0.63 | -0.57 / -0.60 | both halves | 9e-06 | STRING 447 |
| [[MRPS27]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRABP2]] | B | CRABP2 activity raises KDM5B's level | lines that do not express CRABP2 (24) vs lines expressing it (26) | 1.24× lower at baseline in the lines without CRABP2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.2, -36.7); signed map (-6.5, 11.6). **Vector** length 148, 56.3% of its response variance represented; |z| ≥ 3 in 1,480 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.7 | +19.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.4 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +25.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.6 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +4.1 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +8.8 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +2.9 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.3 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -10.4 | -5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.0 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.7 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -8.1 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.9 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.8 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -5.7 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.8 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:202,724,495-202,808,487 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RBBP2H1A, PLU-1, CT31, PPP1R98; previously JARID1B |
| Gene groups (HGNC) | PHD finger proteins; AT-rich interaction domain containing; Lysine demethylase 5 family |
| Reactome | 8 pathways, smallest: TFAP2 (AP-2) family regulates transcription of cell cycle factors; Chromatin modifications during the maternal to zygotic transition (MZT); HDMs demethylate histones |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGL1](https://www.uniprot.org/uniprotkb/Q9UGL1) (Lysine-specific demethylase 5B):

> Histone demethylase that demethylates 'Lys-4' of histone H3, thereby playing a central role in histone code. Does not demethylate histone H3 'Lys-9' or H3 'Lys-27'. Demethylates trimethylated, dimethylated and monomethylated H3 'Lys-4'. Acts as a transcriptional corepressor for FOXG1B and PAX9. Favors the proliferation of breast cancer cells by repressing tumor suppressor genes such as BRCA1 and HOXA5. In contrast, may act as a tumor suppressor for melanoma. Represses the CLOCK-BMAL1 …

**Summary**, from NCBI Gene [10765](https://www.ncbi.nlm.nih.gov/gene/10765):

> This gene encodes a lysine-specific histone demethylase that belongs to the jumonji/ARID domain-containing family of histone demethylases. The encoded protein is capable of demethylating tri-, di- and monomethylated lysine 4 of histone H3. This protein plays a role in the transcriptional repression or certain tumor suppressor genes and is upregulated in certain cancer cells. This protein may also play a role in genome stability and DNA repair. Alternate splicing results in multiple transcript …

**Accessions** — [HGNC:18039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18039) · Entrez [10765](https://www.ncbi.nlm.nih.gov/gene/10765) · UniProt [Q9UGL1](https://www.uniprot.org/uniprotkb/Q9UGL1) · Ensembl [ENSG00000117139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117139)

## Data

Gene col 3877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3877); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3877]; `tensor/DDL_lfc|DDL_z.npy` [3877]; `embed/gene_vectors.npy` [3877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3877 or target_col == 3877). Every well: [[KDM5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
