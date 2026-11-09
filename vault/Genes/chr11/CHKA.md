---
symbol: "CHKA"
type: "gene"
col: 3162
ensembl_id: "ENSG00000110721"
name: "choline kinase alpha"
location: "11q13.2"
module: 148
arm: "-"
pooled_cpm: 92.81
n_lines_expressing: 48
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# CHKA

*choline kinase alpha* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +24.6, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.619× (z -10.1, q 3e-21, down in 34 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.802× (z -4.5, q 0.001, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.0628×, SW480 0.262×, HT-29 0.268×, KATO III 0.293×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.168×, SHP-77 0.166×, SK-MEL-2 0.179×, HT-29 0.283×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 0.425×, SW480 0.474×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.479×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LLGL2]] (+0.60, fdr 2e-05), [[SLC25A33]] (+0.59, fdr 4e-05), [[PPP1R13B]] (+0.58, fdr 1e-05); moves opposite to [[SMARCAL1]] (-0.55, fdr 2e-05), [[PSMC2]] (-0.51, fdr 4e-04), [[ANGEL2]] (-0.51, fdr 8e-05).
> It sits in the **-** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CRACR2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +24.6 | 0e+00 | 44/46 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.99×** | +23.0 | 0e+00 | 46/46 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.83×** | +21.9 | 0e+00 | 44/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.45×** | +18.9 | 0e+00 | 46/46 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.33×** | +17.8 | 0e+00 | 45/46 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +17.4 | 0e+00 | 45/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.02×** | +14.7 | 0e+00 | 44/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.93×** | +13.8 | 3e-41 | 42/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +10.1 | 2e-22 | 34/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +9.7 | 2e-20 | 31/46 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +8.4 | 2e-15 | 31/46 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +8.2 | 9e-15 | 32/46 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +8.2 | 9e-15 | 35/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +6.3 | 1e-08 | 29/46 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +6.1 | 4e-08 | 28/46 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +5.6 | 1e-06 | 28/47 (PANC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +5.5 | 1e-06 | 28/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.66×** | +5.4 | 2e-06 | 25/46 (NCI-H23, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3162.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.0628×, SW480 0.262×, HT-29 0.268×, KATO III 0.293×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.168×, SHP-77 0.166×, SK-MEL-2 0.179×, HT-29 0.283×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 0.425×, SW480 0.474×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.479×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -10.1 | 3e-21 | 34/47 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -9.2 | 7e-18 | 26/42 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.740×** | -5.9 | 8e-07 | 25/43 (C-33 A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -4.5 | 0.001 | 22/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -4.1 | 0.005 | 22/46 (SW 900, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.892× | -3.4 | 0.061 | 22/47 (SW1417, SW480, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.901× | -3.1 | 0.14 | 6/46 (CHP-212, NCI-H2347, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.867× | -3.0 | 0.18 | 11/46 (C-33 A, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.2 | 16 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.5× (z +21.6) | — |
| [[SNU-423 (line)]] | alt | 84.8 | 9 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 121 | 9 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.84× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.515× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 101 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 195 | 5 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 43.8 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.90× (z +15.3) | — |
| [[NCI-H1573 (line)]] | alt | 39.9 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +23.7) | — |
| [[NCI-H23 (line)]] | alt | 85.7 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 117 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.5) | [[Lonafarnib (drug)]] 5 µM 0.136× (z -10.5) ⚠ toxic |
| [[BT-474 (line)]] | alt | 118 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 74.2 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 116 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 36.9 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.47× (z +14.0) | — |
| [[SW480 (line)]] | alt | 207 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -8.8) |
| [[HCT15 (line)]] | alt | 89.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 241 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -14.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 166 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 131 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0628× (z -22.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 59.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +12.3) | — |
| [[A549 (line)]] | wt | 41.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.20× (z +17.1) | — |
| [[CFPAC-1 (line)]] | alt | 99.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +17.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 33.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.82× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 185 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.188× (z -15.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 108 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 51.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.68× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 41.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +14.8) | — |
| [[NCI-H2347 (line)]] | alt | 113 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 78.6 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +10.0) | — |
| [[A-172 (line)]] | wt | 46.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 132 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +16.8) | — |
| [[C32 (line)]] | wt | 46.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +18.2) | — |
| [[HS-578T (line)]] | alt | 46.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.55× (z +14.5) | — |
| [[KATO III (line)]] | alt | 189 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.37× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -13.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 70.9 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 145 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -17.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 55.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -13.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 48.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.42× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 51.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.32× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -13.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 66.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +12.5) | — |
| [[RKO (line)]] | wt | 104 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +11.3) | — |
| [[A498 (line)]] | wt | 42.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.164× (z -8.8) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 18.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LLGL2]] | +0.60 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A33]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[PPP1R13B]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[MLXIPL]] | +0.57 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[GPR153]] | +0.54 | +0.37 / +0.49 | both halves | 9e-05 |  |
| [[SNN]] | +0.54 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[EML4]] | +0.53 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[EEPD1]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[SPATA2L]] | +0.52 | +0.40 / +0.38 | both halves | 6e-05 |  |
| [[CYSTM1]] | +0.51 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[CRACR2B]] | +0.51 | +0.31 / +0.36 | both halves | 2e-04 |  |
| [[NOS1AP]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCAL1]] | -0.55 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[PSMC2]] | -0.51 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[ANGEL2]] | -0.51 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[LINC01829]] | -0.49 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[CSTF3]] | -0.48 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[YARS2]] | -0.46 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[DNAAF10]] | -0.45 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[ZMPSTE24]] | -0.45 | -0.41 / -0.20 | ⚠ not reproduced | 7e-04 |  |
| [[PPP4R1L]] | -0.45 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[VPS52]] | -0.45 | -0.38 / -0.24 | both halves | 5e-04 |  |
| [[SLC30A9]] | -0.45 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[LINC02542]] | -0.45 | -0.29 / -0.28 | both halves | 3e-04 |  |
| [[STMP1]] | -0.44 | -0.35 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACR2B]] | B | CRACR2B activity raises CHKA's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 1.97× lower at baseline in the lines without CRACR2B | 0.005 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[ZDHHC11B]] | B | ZDHHC11B activity raises CHKA's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.60× lower at baseline in the lines without ZDHHC11B | 0.010 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity raises CHKA's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without MCF2L | 0.015 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[SORL1]] | B | SORL1 activity raises CHKA's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without SORL1 | 0.037 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[EEPD1]] | B | EEPD1 activity raises CHKA's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without EEPD1 | 0.044 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[ABLIM2]] | B | ABLIM2 activity raises CHKA's level | lines that do not express ABLIM2 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without ABLIM2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent |
| [[SLC45A4]] | B | SLC45A4 activity raises CHKA's level | lines that do not express SLC45A4 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without SLC45A4 | 0.060 | ⚠ within organs, on part of the lines; also absent: ARHGEF3; maybe low, not absent; its own permutation p |
| [[LLGL2]] | B | LLGL2 activity raises CHKA's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without LLGL2 | 0.062 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[EPHB3]] | B | EPHB3 activity raises CHKA's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.23× lower at baseline in the lines without EPHB3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[NOS1AP]] | B | NOS1AP activity raises CHKA's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.20× lower at baseline in the lines without NOS1AP | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **-** arm (projection on the module's main direction -0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-7.9, 34.5); signed map (-20.5, 32.4). **Vector** length 100, 30.2% of its response variance represented; |z| ≥ 3 in 1,352 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +23.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +17.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +9.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | +18.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.4 | +0.2 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.5 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | choline kinase alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:68,052,859-68,121,444 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CKI; previously CHK |
| Gene groups (HGNC) | Choline kinase family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, UV_RESPONSE_UP |
| Reactome | 5 pathways, smallest: Synthesis of PE; Synthesis of PC; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P35790](https://www.uniprot.org/uniprotkb/P35790) (Choline kinase alpha):

> Plays a key role in phospholipid biosynthesis by catalyzing the phosphorylation of free choline to phosphocholine, the first step in phosphatidylcholine biosynthesis. Also phosphorylates ethanolamine, thereby contributing to phosphatidylethanolamine biosynthesis. Has higher activity with choline. May contribute to tumor cell growth.; [Isoform 1]: This isoform plays a key role in lipolysis of lipid droplets following glucose deprivation. In response to glucose deprivation, phosphorylated by …

**Summary**, from NCBI Gene [1119](https://www.ncbi.nlm.nih.gov/gene/1119):

> The major pathway for the biosynthesis of phosphatidylcholine occurs via the CDP-choline pathway. The protein encoded by this gene is the initial enzyme in the sequence and may play a regulatory role. The encoded protein also catalyzes the phosphorylation of ethanolamine. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1937) · Entrez [1119](https://www.ncbi.nlm.nih.gov/gene/1119) · UniProt [P35790](https://www.uniprot.org/uniprotkb/P35790) · Ensembl [ENSG00000110721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110721)

## Data

Gene col 3162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3162); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3162]; `tensor/DDL_lfc|DDL_z.npy` [3162]; `embed/gene_vectors.npy` [3162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3162 or target_col == 3162). Every well: [[CHKA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHKA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
