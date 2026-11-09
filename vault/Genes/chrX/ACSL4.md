---
symbol: "ACSL4"
type: "gene"
col: 888
ensembl_id: "ENSG00000068366"
name: "acyl-CoA synthetase long chain family member 4"
location: "Xq23"
module: 216
arm: "+"
pooled_cpm: 138.05
n_lines_expressing: 49
n_dd_up: 35
n_dd_down: 9
n_dd_up_clean: 23
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# ACSL4

*acyl-CoA synthetase long chain family member 4* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.92× (z +17.1, q 0e+00, up in 38 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.73× (z +14.3, q 5e-44, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.700× (z -13.2, q 3e-37, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PANK3]] (+0.61, fdr 7e-06), [[ENAH]] (+0.53, fdr 4e-05), [[EFR3A]] (+0.53, fdr 4e-05); moves opposite to [[KBTBD4]] (-0.55, fdr 4e-05), [[TOGARAM1]] (-0.53, fdr 6e-05), [[COQ4]] (-0.53, fdr 4e-05).
> It is in [[Module 216]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +17.1 | 0e+00 | 38/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +15.5 | 0e+00 | 37/43 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +14.3 | 5e-44 | 36/47 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +13.4 | 7e-39 | 38/47 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +11.0 | 5e-26 | 31/44 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +10.8 | 2e-25 | 30/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +10.5 | 6e-24 | 33/46 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +10.1 | 3e-22 | 39/48 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +10.1 | 5e-22 | 28/47 (MIA PaCa-2, AsPC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +9.3 | 6e-19 | 36/47 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 5 µM |  | **1.28×** | +9.0 | 1e-17 | 33/48 (LoVo, LS 180, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.27×** | +8.9 | 3e-17 | 27/47 (A549, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +7.9 | 9e-14 | 27/48 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +7.7 | 5e-13 | 30/47 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +7.6 | 8e-13 | 28/47 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +6.8 | 3e-10 | 26/47 (SNU-423, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +6.1 | 2e-08 | 24/46 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +6.0 | 5e-08 | 23/46 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.47×** | +5.3 | 3e-06 | 23/47 (PANC-1, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +5.2 | 5e-06 | 22/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +5.1 | 8e-06 | 26/47 (SK-MEL-2, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 888.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -13.2 | 3e-37 | 33/48 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -9.4 | 2e-18 | 37/48 (NCI-H23, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.833×** | -6.8 | 2e-09 | 22/47 (J82, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.782×** | -6.5 | 2e-08 | 30/47 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.791×** | -6.2 | 9e-08 | 29/47 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.670×** | -5.5 | 4e-06 | 25/47 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.802×** | -3.8 | 0.013 | 18/47 (SHP-77, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.910× | -3.5 | 0.029 | 3/48 (Hs 766T, SNU-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.879× | -3.4 | 0.037 | 11/47 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | 0.874× | -3.4 | 0.037 | 20/46 (HepG2/C3A, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.914× | -3.3 | 0.042 | 6/47 (HepG2/C3A, COLO 205, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.831×** | -3.2 | 0.073 | 19/46 (NCI-H1573, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.834× | -3.1 | 0.078 | 17/47 (RKO, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.885× | -3.1 | 0.078 | 19/47 (A498, A549, …) | top dose only |  |
| [[Regorafenib (drug)]] 5 µM |  | **0.799×** | -3.1 | 0.078 | 10/47 (NCI-H23, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.902× | -3.0 | 0.085 | 11/47 (NCI-H23, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.923× | -3.0 | 0.087 | 8/47 (COLO 205, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 293 | 4 (1 ⚠) | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -18.3) |
| [[HepG2_C3A (line)]] | wt | 635 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -23.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -16.5) |
| [[HOP62 (line)]] | alt | 162 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +18.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 299 | 7 (4 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.14× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 53.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +18.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.92× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 118 | 6 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.93× (z +12.8) | — |
| [[SK-MEL-2 (line)]] | alt | 184 | 5 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.44× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -9.3) |
| [[A-172 (line)]] | wt | 49.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.24× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 50.2 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Berbamine (drug)]] 5 µM 2.27× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 170 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 67.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.08× (z +11.4) | — |
| [[A498 (line)]] | wt | 301 | 2 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.12× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 73.0 | 4 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.33× (z +11.7) ⚠ unreliable plate only · without an alert: [[Berbamine (drug)]] 5 µM 1.61× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 98.1 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.86× (z +10.8) | — |
| [[LoVo (line)]] | wt | 71.5 | 4 (2 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 1.99× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 213 | 3 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.01× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 44.7 | 3 (2 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.27× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 122 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +17.6) ⚠ cell-cycle shift, explains ~25% of this change | [[TAK-901 (drug)]] 5 µM 0.204× (z -9.6) |
| [[A549 (line)]] | wt | 148 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 2.59× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -15.5) |
| [[C32 (line)]] | wt | 74.0 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.42× (z +11.2) | — |
| [[SW480 (line)]] | alt | 175 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.85× (z +17.0) | — |
| [[A-427 (line)]] | wt | 112 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +8.5) ⚠ toxic; transcription drop | [[PH-797804 (drug)]] 5 µM 0.237× (z -9.2) |
| [[COLO 205 (line)]] | alt | 156 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -11.1) |
| [[Hs 766T (line)]] | wt | 132 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.13× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 142 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +8.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -8.9) |
| [[SW1417 (line)]] | alt | 83.2 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.01× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 72.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +18.4) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[CFPAC-1 (line)]] | alt | 135 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.42× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 78.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -9.1) |
| [[H4 (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HCT15 (line)]] | alt | 96.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.05× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 95.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +8.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.520× (z -15.7) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H1792 (line)]] | alt | 95.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 105 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 147 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0841× (z -9.8) |
| [[SW 900 (line)]] | alt | 162 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -10.4) |
| [[AN3 CA (line)]] | alt | 201 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 97.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PANK3]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ENAH]] | +0.53 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[EFR3A]] | +0.53 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[TACC1]] | +0.50 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[GALNT10]] | +0.49 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[MAN2A1]] | +0.49 | +0.43 / +0.53 | both halves | 4e-05 |  |
| [[ME2]] | +0.49 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[PTPN11]] | +0.48 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[REEP3]] | +0.48 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[GALNT1]] | +0.47 | +0.31 / +0.52 | both halves | 2e-04 |  |
| [[ELOVL5]] | +0.46 | +0.38 / +0.51 | both halves | 7e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 418 |
| [[PEA15]] | +0.46 | +0.34 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD4]] | -0.55 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[TOGARAM1]] | -0.53 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[COQ4]] | -0.53 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[FAM174A]] | -0.52 | -0.36 / -0.59 | both halves | 9e-05 |  |
| [[ZNF446]] | -0.52 | -0.24 / -0.60 | both halves | 4e-04 |  |
| [[LZTS2]] | -0.49 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[SMPD4BP]] | -0.49 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[DBR1]] | -0.49 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[RNF139]] | -0.49 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[MED4]] | -0.48 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[TRAPPC2L]] | -0.48 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[NUDT2]] | -0.48 | -0.30 / -0.60 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.3, -12.5); signed map (11.1, -53.3). **Vector** length 134, 41.0% of its response variance represented; |z| ≥ 3 in 1,715 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +13.8 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +11.1 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.5 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.6 | +17.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.0 | +14.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +6.3 | +8.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +5.6 | +9.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.7 | -9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.7 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -13.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.3 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.6 | -6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -6.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.5 | -6.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -3.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA synthetase long chain family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:109,624,244-109,733,403 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ACS4, LACS4; previously FACL4, MRX63, MRX68 |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Hallmark sets | PEROXISOME, FATTY_ACID_METABOLISM |
| Reactome | 8 pathways, smallest: Intracellular metabolism of fatty acids regulates insulin secretion; Free fatty acids regulate insulin secretion; Synthesis of very long-chain fatty acyl-CoAs |
| Matched by | ensembl_id |

**Function**, from UniProt [O60488](https://www.uniprot.org/uniprotkb/O60488) (Long-chain-fatty-acid--CoA ligase 4):

> Catalyzes the conversion of long- and medium-chain fatty acids to their active form fatty acyl-CoA. May drive cellular fatty acid uptake by metabolic trapping, and regulate the channeling of fatty acids towards specific metabolic pathways such as the generation of energy by beta-oxidation or the synthesis of membrane lipids. Preferentially activates arachidonate and eicosapentaenoate as substrates, and among the eicosanoids 8,9-EET > 14,15-EET > 5,6-EET > 11,12-EET, but can also activate other …

**Summary**, from NCBI Gene [2182](https://www.ncbi.nlm.nih.gov/gene/2182):

> The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme preferentially utilizes arachidonate as substrate. The absence of this enzyme may contribute to the cognitive …

**Accessions** — [HGNC:3571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3571) · Entrez [2182](https://www.ncbi.nlm.nih.gov/gene/2182) · UniProt [O60488](https://www.uniprot.org/uniprotkb/O60488) · Ensembl [ENSG00000068366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068366)

## Data

Gene col 888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 888); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 888]; `tensor/DDL_lfc|DDL_z.npy` [888]; `embed/gene_vectors.npy` [888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 888 or target_col == 888). Every well: [[ACSL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACSL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
