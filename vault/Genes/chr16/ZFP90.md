---
symbol: "ZFP90"
type: "gene"
col: 11594
ensembl_id: "ENSG00000184939"
name: "ZFP90 zinc finger protein"
location: "16q22.1"
module: 11
arm: "+"
pooled_cpm: 27.54
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 22
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ZFP90

*ZFP90 zinc finger protein* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.85× (z +16.8, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.282× (z -20.3, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF555]] (+0.66, fdr 1e-05), [[ZNF606]] (+0.64, fdr 1e-05), [[ZNF197]] (+0.63, fdr 1e-05); moves opposite to [[STT3B]] (-0.54, fdr 1e-05), [[DPY19L1]] (-0.53, fdr 1e-05), [[LAPTM4B]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.85×** | +16.8 | 0e+00 | 39/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +12.5 | 1e-33 | 38/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +9.9 | 1e-20 | 27/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +6.0 | 2e-07 | 24/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.0 | 2e-07 | 25/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +5.7 | 2e-06 | 25/47 (KATO III, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.20× | +3.9 | 0.007 | 13/47 (NCI-H23, A549, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.017 | 13/47 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.021 | 15/47 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +3.5 | 0.027 | 10/47 (A498, LS 180, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +3.4 | 0.036 | 19/47 (SW1417, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +3.4 | 0.036 | 17/47 (A498, RKO, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.26×** | +3.3 | 0.036 | 10/47 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.036 | 9/47 (SW480, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.036 | 13/47 (LoVo, J82, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.044 | 9/47 (C-33 A, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.044 | 11/47 (CFPAC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.054 | 9/47 (SW480, C32, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.073 | 9/47 (A-427, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.282×** | -20.3 | 0e+00 | 46/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.353×** | -16.7 | 0e+00 | 42/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.365×** | -16.2 | 0e+00 | 40/47 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.477×** | -11.9 | 3e-30 | 38/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.486×** | -11.1 | 1e-26 | 36/45 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.306×** | -9.9 | 3e-21 | 36/46 (BT-474, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.339×** | -9.1 | 1e-17 | 36/47 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.561×** | -8.6 | 8e-16 | 29/42 (Hs 766T, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.621×** | -7.3 | 1e-11 | 30/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.634×** | -7.3 | 2e-11 | 31/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -6.7 | 8e-10 | 29/47 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.741×** | -4.8 | 7e-05 | 22/43 (NCI-H1573, J82, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.735×** | -4.6 | 2e-04 | 22/47 (CFPAC-1, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.581×** | -4.6 | 2e-04 | 14/28 (HOP62, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.760×** | -4.2 | 9e-04 | 22/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.740×** | -3.4 | 0.019 | 11/47 (NCI-H460, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.825×** | -3.1 | 0.064 | 6/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 0.874× | -3.0 | 0.066 | 8/47 (A498, HOP62, …) | all doses, flat |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.828×** | -3.0 | 0.068 | 11/47 (SW 900, H4, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.833× | -2.9 | 0.087 | 9/47 (NCI-H460, SW 900, …) | top dose only |  |
| [[Fluvoxamine (maleate) (drug)]] 0.05 µM |  | 0.835× | -2.9 | 0.090 | 7/47 (Panc 03.27, CHP-212, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.6 | 0 | 14 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -17.8) |
| [[MIA PaCa-2 (line)]] | alt | 60.8 | 0 | 11 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.249× (z -12.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -12.1) |
| [[SW480 (line)]] | alt | 21.0 | 7 (2 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 29.4× (z +26.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 29.6 | 5 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 12.1× (z +17.8) | [[Digitoxin (drug)]] 0.5 µM 0.177× (z -12.4) |
| [[PANC-1 (line)]] | alt | 30.9 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -21.6) |
| [[KATO III (line)]] | alt | 21.3 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 44.2× (z +22.9) | — |
| [[SW1417 (line)]] | alt | 16.0 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 21.8× (z +17.3) | — |
| [[HOP62 (line)]] | alt | 31.8 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0903× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.189× (z -13.4) |
| [[LoVo (line)]] | wt | 21.9 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.88× (z +8.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.152× (z -15.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -10.6) |
| [[HCT15 (line)]] | alt | 41.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 13.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +19.4) | — |
| [[J82 (line)]] | alt | 25.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 33.2 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.57× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.261× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 42.7 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.43× (z +11.9) | [[TAK-901 (drug)]] 5 µM 0.0353× (z -14.1) |
| [[SNU-423 (line)]] | alt | 30.6 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.57× (z +12.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -13.4) |
| [[A549 (line)]] | wt | 35.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.24× (z +15.8) | — |
| [[Hs 766T (line)]] | wt | 22.6 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.32× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.0689× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -11.9) |
| [[HT-29 (line)]] | alt | 10.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 10.0× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 21.2 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 6.55× (z +11.6) | — |
| [[SW48 (line)]] | wt | 24.5 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.09× (z +9.8) | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0467× (z -14.2) |
| [[A-172 (line)]] | wt | 72.7 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.365× (z -10.3) |
| [[A498 (line)]] | wt | 22.9 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.37× (z +14.4) | — |
| [[BT-474 (line)]] | alt | 35.5 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.162× (z -12.4) |
| [[C32 (line)]] | wt | 22.7 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +13.5) | [[Digitoxin (drug)]] 0.5 µM 0.211× (z -9.5) |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0842× (z -10.8) |
| [[H4 (line)]] | wt | 22.0 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 11.5× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 2 (1 ⚠) | — | [[Hydroxyurea (drug)]] 0.05 µM 0.102× (z -10.9) |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 11.6× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SHP-77 (line)]] | alt | 32.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.201× (z -10.6) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 48.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0290× (z -11.9) |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0731× (z -14.7) |
| [[A-427 (line)]] | wt | 44.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.3) | — |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0997× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 31.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -11.4) |
| [[RKO (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF555]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 | same gene group |
| [[ZNF606]] | +0.64 | +0.77 / +0.53 | both halves | 1e-05 | same gene group |
| [[ZNF197]] | +0.63 | +0.70 / +0.55 | both halves | 1e-05 | same gene group |
| [[TRMT10B]] | +0.63 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[NECAP2]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[PDRG1]] | +0.61 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ZNF23]] | +0.61 | +0.68 / +0.53 | both halves | 1e-05 | same gene group |
| [[POLI]] | +0.60 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[GIN1]] | +0.59 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[MRPL58]] | +0.58 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[NFKBIL1]] | +0.57 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[PHAX]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.54 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[DPY19L1]] | -0.53 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[LAPTM4B]] | -0.53 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[IMPA2]] | -0.52 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[TM9SF3]] | -0.50 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[PHTF2]] | -0.50 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[CRTAP]] | -0.50 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[ATP2A2]] | -0.49 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-30.9, 6.0); signed map (4.4, -22.5). **Vector** length 76.2, 17.3% of its response variance represented; |z| ≥ 3 in 1,195 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +3.2 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.9 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -16.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | +3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.5 | -11.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +1.5 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ZFP90 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,530,090-68,576,072 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1954, NK10, ZNF756 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF47](https://www.uniprot.org/uniprotkb/Q8TF47) (Zinc finger protein 90 homolog):

> Inhibits the transcriptional repressor activity of REST by inhibiting its binding to DNA, thereby derepressing transcription of REST target genes.; [Isoform 2]: Acts as a bridge between FOXP3 and the corepressor TRIM28, and is required for the transcriptional repressor activity of FOXP3 in regulatory T-cells (Treg).

**Summary**, from NCBI Gene [146198](https://www.ncbi.nlm.nih.gov/gene/146198):

> This gene encodes a member of the zinc finger protein family that modulates gene expression. The encoded protein derepresses the transcription of certain fetal cardiac genes and may contribute to the genetic reprogramming that occurs during the development of heart failure. Genome wide association studies have identified this gene among ulcerative colitis risk loci. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Mar 2015]

**Accessions** — [HGNC:23329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23329) · Entrez [146198](https://www.ncbi.nlm.nih.gov/gene/146198) · UniProt [Q8TF47](https://www.uniprot.org/uniprotkb/Q8TF47) · Ensembl [ENSG00000184939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184939)

## Data

Gene col 11594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11594); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11594]; `tensor/DDL_lfc|DDL_z.npy` [11594]; `embed/gene_vectors.npy` [11594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11594 or target_col == 11594). Every well: [[ZFP90 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP90.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
