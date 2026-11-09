---
symbol: "SETX"
type: "gene"
col: 2842
ensembl_id: "ENSG00000107290"
name: "senataxin"
location: "9q34.13"
module: 182
arm: "-"
pooled_cpm: 235.96
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# SETX

*senataxin* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +18.8, q 0e+00, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.537× (z -12.2, q 1e-31, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.804× (z -6.1, q 2e-07, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUT7]] (+0.77, fdr 7e-06), [[CRK]] (+0.69, fdr 7e-06), [[GPATCH2L]] (+0.63, fdr 7e-06); moves opposite to [[SEC61A2]] (-0.61, fdr 7e-06), [[RYK]] (-0.61, fdr 1e-05), [[HSF2]] (-0.61, fdr 7e-06).
> It sits in the **-** arm of [[Module 182]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +18.8 | 0e+00 | 36/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +14.3 | 7e-44 | 43/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +13.1 | 9e-37 | 40/48 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +8.4 | 9e-15 | 39/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +7.6 | 4e-12 | 34/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +7.2 | 6e-11 | 38/48 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +7.1 | 1e-10 | 35/48 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +6.3 | 2e-08 | 36/48 (LS 180, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +6.2 | 3e-08 | 30/48 (HEC-1-A, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +5.8 | 4e-07 | 31/48 (SNU-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +5.0 | 3e-05 | 36/48 (BT-474, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.7 | 1e-04 | 36/45 (HEC-1-A, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 2e-04 | 30/48 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.5 | 3e-04 | 30/48 (A498, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.22×** | +3.9 | 0.003 | 26/48 (SNU-1, HepG2/C3A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.018 | 24/49 (NCI-H2030, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.038 | 23/49 (SK-MEL-2, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -12.2 | 1e-31 | 42/49 (NCI-H23, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -11.9 | 3e-30 | 41/44 (SNU-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.545×** | -11.1 | 4e-26 | 35/45 (RKO, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.804×** | -6.1 | 2e-07 | 32/48 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.759×** | -5.4 | 6e-06 | 31/48 (NCI-H23, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.826×** | -5.3 | 9e-06 | 24/48 (NCI-H23, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -5.2 | 2e-05 | 34/49 (SW 1271, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.817×** | -4.0 | 0.005 | 26/48 (NCI-H23, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.814×** | -3.9 | 0.006 | 24/47 (RKO, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.852× | -3.8 | 0.008 | 18/48 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.836× | -3.5 | 0.019 | 19/48 (NCI-H1792, C-33 A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.836× | -3.5 | 0.019 | 23/49 (NCI-H23, SW480, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -3.5 | 0.019 | 16/49 (RKO, A498, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.846× | -3.2 | 0.061 | 21/48 (NCI-H23, RKO, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.799×** | -3.2 | 0.061 | 21/48 (A-172, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.873× | -3.0 | 0.098 | 18/49 (NCI-H23, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 269 | 12 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +24.6) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 286 | 3 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +32.7) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.584× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 258 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.77× (z +23.2) | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -15.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 240 | 8 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -18.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 411 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.512× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 282 | 5 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.98× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -11.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 319 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -12.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 308 | 3 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Radotinib (drug)]] 5 µM 0.545× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 166 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +23.3) | — |
| [[KATO III (line)]] | alt | 320 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +16.4) | [[Digitoxin (drug)]] 5 µM 0.366× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[A-427 (line)]] | wt | 237 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.71× (z +21.9) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -11.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 243 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +43.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 226 | 3 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.62× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.468× (z -11.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 176 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.493× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 244 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +31.4) | — |
| [[HOP62 (line)]] | alt | 225 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 222 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +38.2) | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -9.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 193 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +23.7) | — |
| [[COLO 205 (line)]] | alt | 324 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +31.3) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -11.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 222 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.83× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 156 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +39.6) | — |
| [[PANC-1 (line)]] | alt | 181 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +42.2) | — |
| [[A-172 (line)]] | wt | 211 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +31.9) | [[Dinaciclib (drug)]] 0.05 µM 0.505× (z -8.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 268 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -11.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 303 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -14.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 263 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.22× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -13.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 384 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -14.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 556 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -22.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 188 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.93× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 196 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 200 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 252 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -8.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 184 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.474× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 163 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.03× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 109 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +15.4) | — |
| [[Panc 03.27 (line)]] | alt | 196 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 262 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.435× (z -10.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 232 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +10.5) | — |
| [[C32 (line)]] | wt | 165 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 125 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.402× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 157 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.42× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 216 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 332 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUT7]] | +0.77 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[CRK]] | +0.69 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[GPATCH2L]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SLC30A7]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DNTTIP2]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[UTP11]] | +0.61 | +0.66 / +0.54 | both halves | 1e-05 | same gene group |
| [[RRP7A]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[KPNA4]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[KCTD5]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[BACH1]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SLC35C2]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SAP30BP]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | -0.61 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[RYK]] | -0.61 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[HSF2]] | -0.61 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[KDM1A]] | -0.59 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[ALG9]] | -0.59 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[SNRPA1]] | -0.58 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[CHASERR]] | -0.58 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[HOXB5]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[PEBP1]] | -0.58 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[USP3]] | -0.58 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.58 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[RCOR3]] | -0.57 | -0.61 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **-** arm (projection on the module's main direction -0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (4.4, -9.9); signed map (8.1, 13.5). **Vector** length 137, 50.5% of its response variance represented; |z| ≥ 3 in 1,387 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.7 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +13.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +14.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +4.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +3.3 | +1.0 |
|  | [[Mifepristone (drug)]] 0.5 µM |  | +3.1 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.9 | -5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -7.4 | -6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.0 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.6 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.0 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | senataxin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:132,261,356-132,354,986 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0625, AOA2, Sen1, STEX; previously ALS4, SCAR1 |
| Gene groups (HGNC) | UPF1 like RNA helicases; SSU processome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z333](https://www.uniprot.org/uniprotkb/Q7Z333) (Helicase senataxin):

> ATP-dependent 5'-3' helicase that preferentially unwinds RNA:DNA substrates over DNA:DNA substrates, playing a crucial role in resolving 5'-overhang RNA:DNA hybrids (R-loops) and promoting transcription termination. Plays a role in transcription regulation by its ability to modulate RNA Polymerase II (Pol II) binding to chromatin and through its interaction with proteins involved in transcription. Contributes to the mRNA splicing efficiency and splice site selection. Required for the resolution …

**Summary**, from NCBI Gene [23064](https://www.ncbi.nlm.nih.gov/gene/23064):

> This gene encodes a protein named for its homology to the Sen1p protein of fungi which has RNA helicase activity encoded by a domain at the C-terminal end of the protein. The protein encoded by this gene contains a DNA/RNA helicase domain at its C-terminal end which suggests that it may be involved in both DNA and RNA processing. Mutations in this gene have been associated with ataxia-ocular apraxia-2 (AOA2) and an autosomal dominant form of juvenile amyotrophic lateral sclerosis (ALS4). …

**Accessions** — [HGNC:445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:445) · Entrez [23064](https://www.ncbi.nlm.nih.gov/gene/23064) · UniProt [Q7Z333](https://www.uniprot.org/uniprotkb/Q7Z333) · Ensembl [ENSG00000107290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107290)

## Data

Gene col 2842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2842); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2842]; `tensor/DDL_lfc|DDL_z.npy` [2842]; `embed/gene_vectors.npy` [2842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2842 or target_col == 2842). Every well: [[SETX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
