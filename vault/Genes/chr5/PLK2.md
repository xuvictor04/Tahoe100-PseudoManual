---
symbol: "PLK2"
type: "gene"
col: 7009
ensembl_id: "ENSG00000145632"
name: "polo like kinase 2"
location: "5q11.2"
module: 224
arm: "+"
pooled_cpm: 116.51
n_lines_expressing: 44
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/224"]
generated_by: "tahoemap"
---

# PLK2

*polo like kinase 2* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.16× (z +19.0, q 0e+00, up in 38 of 42 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 3.87× (z +15.8, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.526× (z -7.2, q 3e-10, down in 27 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.595× (z -5.8, q 1e-06, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP14]] (+0.64, fdr 7e-06), [[SYTL2]] (+0.61, fdr 7e-06), [[KITLG]] (+0.60, fdr 1e-05); moves opposite to [[SDHAP4-1]] (-0.52, fdr 1e-05), [[RARS2]] (-0.52, fdr 1e-05), [[SMG1P5]] (-0.50, fdr 1e-05).
> It is in [[Module 224]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF462]] → it (grade B ⚠); 4 go from it, the strongest it → [[AHR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.16×** | +19.0 | 0e+00 | 38/42 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.87×** | +15.8 | 0e+00 | 38/42 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.51×** | +14.1 | 1e-42 | 37/42 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.12×** | +13.3 | 6e-38 | 35/42 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.49×** | +10.6 | 3e-24 | 38/42 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.58×** | +7.8 | 7e-13 | 32/43 (MIA PaCa-2, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.83×** | +7.1 | 1e-10 | 32/42 (LoVo, LS 180, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.83×** | +7.0 | 2e-10 | 25/42 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +6.5 | 6e-09 | 33/42 (NCI-H2347, CFPAC-1, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.73×** | +6.4 | 1e-08 | 22/42 (LoVo, LS 180, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.62×** | +5.6 | 8e-07 | 24/42 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +5.4 | 3e-06 | 24/42 (NCI-H2347, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +3.9 | 0.004 | 27/42 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.8 | 0.005 | 21/41 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.38×** | +3.6 | 0.011 | 23/41 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.020 | 22/42 (SNU-423, HT-29, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.070 | 17/42 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.073 | 17/42 (LoVo, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.094 | 19/43 (NCI-H1792, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7009.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.526×** | -7.2 | 3e-10 | 27/38 (SNU-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.596×** | -6.0 | 5e-07 | 28/42 (SNU-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.595×** | -5.8 | 1e-06 | 26/41 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.619×** | -5.4 | 1e-05 | 26/42 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.727×** | -3.7 | 0.023 | 23/42 (Hs 766T, HT-29, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.731×** | -3.6 | 0.025 | 22/42 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.734×** | -3.6 | 0.027 | 21/41 (SW48, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.730×** | -3.5 | 0.031 | 22/43 (HT-29, SW1417, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.750×** | -3.3 | 0.053 | 19/42 (A498, LOX-IMVI, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.759×** | -3.2 | 0.076 | 17/42 (A498, PANC-1, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.682×** | -3.2 | 0.076 | 20/41 (A498, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 431 | 5 (1 ⚠) | 11 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +21.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.49× (z +17.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.289× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 381 | 8 (2 ⚠) | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 6.04× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.1) |
| [[LoVo (line)]] | wt | 150 | 10 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.45× (z +20.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.39× (z +14.0) | — |
| [[SNU-1 (line)]] | wt | 221 | 7 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 8.51× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0401× (z -24.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 225 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.10× (z +12.4) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.318× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 109 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +18.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.09× (z +15.2) | — |
| [[LS 180 (line)]] | wt | 82.0 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.14× (z +15.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.01× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 131 | 6 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 7.60× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -12.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 138 | 4 (3 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.82× (z +12.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.23× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -8.5) |
| [[A-172 (line)]] | wt | 90.2 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 11.2× (z +14.1) | — |
| [[A549 (line)]] | wt | 114 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +21.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.4× (z +18.7) | — |
| [[HS-578T (line)]] | alt | 59.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +17.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 13.0× (z +13.5) | — |
| [[C32 (line)]] | wt | 112 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +17.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.83× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 150 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +24.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.95× (z +17.3) | — |
| [[HT-29 (line)]] | alt | 297 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 50.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +22.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 23.6× (z +17.0) | — |
| [[J82 (line)]] | alt | 225 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.44× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 50.3 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.75× (z +14.3) | — |
| [[PANC-1 (line)]] | alt | 71.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.87× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 69.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.2× (z +14.6) | — |
| [[Hs 766T (line)]] | wt | 166 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.123× (z -14.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 37.7 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.34× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 53.7 | 3 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.78× (z +13.1) ⚠ position not correctable · without an alert: [[Harringtonine (drug)]] 5 µM 5.37× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 47.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 7.86× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 225 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +16.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.06× (z +12.3) | — |
| [[SW48 (line)]] | wt | 131 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +10.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 4.15× (z +9.0) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.279× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 29.5 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.71× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 77.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +14.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.77× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 116 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.1) ⚠ cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 93.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +13.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HEC-1-A (line)]] | alt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 42.6 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.29× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.89 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP14]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SYTL2]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[KITLG]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[AMOTL2]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ADRB2]] | +0.58 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[TIGD2]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[C21orf91]] | +0.57 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[BBS10]] | +0.57 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[SLC30A1]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[AHR]] | +0.57 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[LIMA1]] | +0.56 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TLE4]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4-1]] | -0.52 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[RARS2]] | -0.52 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SMG1P5]] | -0.50 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.50 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[DCUN1D2]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[PMS2P3]] | -0.48 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[DCUN1D5]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[NUP43]] | -0.48 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[SARNP]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SRD5A1]] | -0.47 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[CCT6P3-1]] | -0.47 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[NAP1L4]] | -0.47 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF462]] | B | ZNF462 activity lowers PLK2's level | lines that do not express ZNF462 (5) vs lines expressing it (45) | 2.63× higher at baseline in the lines without ZNF462 | 0.058 | ⚠ within organs, on part of the lines; also absent: PDE11A, ENSG00000214803 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHR]] | B | PLK2 activity raises AHR's level | lines that do not express PLK2 (6) vs lines expressing it (44) | 3.92× lower at baseline in the lines without PLK2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, POLE |
| [[EDN1]] | B | PLK2 activity raises EDN1's level | lines that do not express PLK2 (6) vs lines expressing it (44) | 4.36× lower at baseline in the lines without PLK2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, POLE |
| [[HES1]] | B | PLK2 activity raises HES1's level | lines that do not express PLK2 (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without PLK2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, POLE |
| [[SERTAD1]] | B | PLK2 activity strengthens SERTAD1's drug response | lines that do not express PLK2 (6) vs lines expressing it (42) | the lines without PLK2 respond 0.56× as strongly (z diff +1.91); strongest at Homoharringtonine 5 µM: 2.14x vs 5.25x (z diff +4.0) | 0.097 | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, POLE; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 224]] — hypoxia; 9 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.2, 18.4); signed map (22.5, 35.9). **Vector** length 133, 41.7% of its response variance represented; |z| ≥ 3 in 1,470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.3 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +15.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.0 | +3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.6 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +3.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.8 | -3.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.4 | -2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | +0.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -4.0 | -5.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -4.0 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | polo like kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:58,453,982-58,460,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SNK |
| Gene groups (HGNC) | Polo like kinase family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 10 pathways, smallest: CD163 mediating an anti-inflammatory response; NPAS4 regulates expression of target genes; TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYY3](https://www.uniprot.org/uniprotkb/Q9NYY3) (Serine/threonine-protein kinase PLK2):

> Tumor suppressor serine/threonine-protein kinase involved in synaptic plasticity, centriole duplication and G1/S phase transition. Polo-like kinases act by binding and phosphorylating proteins that are already phosphorylated on a specific motif recognized by the POLO box domains. Phosphorylates CPAP, NPM1, RAPGEF2, RASGRF1, SNCA, SIPA1L1 and SYNGAP1. Plays a key role in synaptic plasticity and memory by regulating the Ras and Rap protein signaling: required for overactivity-dependent spine …

**Summary**, from NCBI Gene [10769](https://www.ncbi.nlm.nih.gov/gene/10769):

> The protein encoded by this gene is a member of the polo family of serine/threonine protein kinases that have a role in normal cell division. This gene is most abundantly expressed in testis, spleen and fetal tissues, and its expression is inducible by serum, suggesting that it may also play an important role in cells undergoing rapid cell division. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:19699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19699) · Entrez [10769](https://www.ncbi.nlm.nih.gov/gene/10769) · UniProt [Q9NYY3](https://www.uniprot.org/uniprotkb/Q9NYY3) · Ensembl [ENSG00000145632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145632)

## Data

Gene col 7009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7009); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7009]; `tensor/DDL_lfc|DDL_z.npy` [7009]; `embed/gene_vectors.npy` [7009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7009 or target_col == 7009). Every well: [[PLK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
