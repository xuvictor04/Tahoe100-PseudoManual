---
symbol: "PITPNB"
type: "gene"
col: 11150
ensembl_id: "ENSG00000180957"
name: "phosphatidylinositol transfer protein beta"
location: "22q12.1"
module: 4
arm: "+"
pooled_cpm: 164.34
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PITPNB

*phosphatidylinositol transfer protein beta* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.81× (z +17.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.707× (z -14.8, q 0e+00, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX10]] (+0.66, fdr 9e-06), [[NAA15]] (+0.65, fdr 1e-05), [[RABGAP1L]] (+0.60, fdr 3e-05); moves opposite to [[TMEM94]] (-0.58, fdr 3e-05), [[HOXA3]] (-0.58, fdr 2e-05), [[TGDS]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11150.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +17.8 | 0e+00 | 46/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +16.3 | 0e+00 | 44/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +16.2 | 0e+00 | 46/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +15.1 | 0e+00 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +15.1 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +13.0 | 2e-36 | 34/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +12.9 | 4e-36 | 28/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +11.4 | 3e-28 | 41/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +10.8 | 1e-25 | 35/48 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +10.6 | 2e-24 | 39/48 (Hs 766T, A498, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +9.5 | 2e-19 | 31/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +9.1 | 3e-18 | 35/49 (PANC-1, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +8.9 | 3e-17 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +8.8 | 5e-17 | 40/48 (PANC-1, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +7.9 | 1e-13 | 27/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +7.0 | 1e-10 | 29/48 (A498, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +5.2 | 7e-06 | 20/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.35×** | +4.7 | 6e-05 | 22/48 (A498, SW 900, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11150.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -14.8 | 0e+00 | 40/49 (HEC-1-A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.733×** | -9.4 | 2e-18 | 37/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.787×** | -7.3 | 8e-11 | 28/49 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -7.0 | 3e-10 | 19/48 (CFPAC-1, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.817×** | -6.1 | 1e-07 | 26/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.831×** | -5.6 | 2e-06 | 25/48 (Panc 03.27, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.878× | -5.6 | 2e-06 | 17/48 (J82, LoVo, …) | rises with dose | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.833×** | -5.5 | 2e-06 | 24/48 (SNU-423, HOP62, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.882× | -5.4 | 4e-06 | 12/48 (NCI-H23, hTERT-HPNE, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.851× | -4.7 | 1e-04 | 21/44 (NCI-H23, SHP-77, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.853× | -4.6 | 2e-04 | 22/47 (HEC-1-A, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.872× | -4.2 | 0.002 | 13/48 (KATO III, RKO, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.873× | -4.1 | 0.002 | 17/48 (HEC-1-A, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.778×** | -3.9 | 0.004 | 18/49 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.897× | -3.3 | 0.039 | 11/49 (SNU-423, LoVo, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.906× | -3.0 | 0.095 | 10/47 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.906× | -3.0 | 0.095 | 8/48 (H4, NCI-H2347, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 136 | 16 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.82× (z +25.5) | — |
| [[NCI-H460 (line)]] | wt | 129 | 14 (5 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.32× (z +19.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +17.5) | — |
| [[A498 (line)]] | wt | 150 | 10 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +22.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 205 | 10 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.06× (z +22.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +21.0) | — |
| [[SW 900 (line)]] | alt | 149 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 171 | 8 (3 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.52× (z +12.8) | [[Binimetinib (drug)]] 5 µM 0.544× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 144 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +15.1) | — |
| [[SW480 (line)]] | alt | 182 | 9 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.58× (z +18.7) | — |
| [[LS 180 (line)]] | wt | 123 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 160 | 5 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.105× (z -31.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -12.6) |
| [[HS-578T (line)]] | alt | 283 | 7 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 142 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.75× (z +12.3) | — |
| [[SHP-77 (line)]] | alt | 137 | 5 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.56× (z +12.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 128 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.65× (z +14.7) | — |
| [[H4 (line)]] | wt | 118 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 119 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.17× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -9.2) |
| [[SNU-1 (line)]] | wt | 220 | 2 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.82× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -9.9) |
| [[SNU-423 (line)]] | alt | 233 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -14.9) |
| [[A549 (line)]] | wt | 128 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 194 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 182 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 118 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +13.2) | — |
| [[RKO (line)]] | wt | 225 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.43× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -9.7) |
| [[A-172 (line)]] | wt | 82.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.3) | — |
| [[A-427 (line)]] | wt | 95.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.14× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 212 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.97× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.76× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 207 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +10.1) | [[Tofacitinib (drug)]] 5 µM 0.657× (z -9.2) |
| [[CHP-212 (line)]] | wt | 211 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -11.7) |
| [[HCT15 (line)]] | alt | 165 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.43× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HepG2_C3A (line)]] | wt | 115 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.51× (z +9.9) ⚠ toxic | — |
| [[J82 (line)]] | alt | 157 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -10.2) |
| [[LoVo (line)]] | wt | 250 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 174 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -11.1) |
| [[BT-474 (line)]] | alt | 149 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.20× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.44× (z +12.0) ⚠ toxic | — |
| [[Hs 766T (line)]] | wt | 255 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.58× (z +11.9) ⚠ unreliable plate only | — |
| [[HT-29 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.92× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 131 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -11.9) |
| [[SW 1271 (line)]] | alt | 139 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.134× (z -11.0) |
| [[SW48 (line)]] | wt | 206 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -11.6) |
| [[AN3 CA (line)]] | alt | 167 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 151 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 148 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 217 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX10]] | +0.66 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[NAA15]] | +0.65 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[RABGAP1L]] | +0.60 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[RASAL2]] | +0.59 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[URB2]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[FUT4]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RRP7A]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[DIAPH2]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SERBP1]] | +0.57 | +0.54 / +0.49 | both halves | 2e-05 |  |
| [[POLR1A]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[FAF1]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[NOL10]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM94]] | -0.58 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[HOXA3]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TGDS]] | -0.57 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[B4GALT4]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | -0.57 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[GNAS]] | -0.56 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ZNF821]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[CLK1]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[SMPDL3A]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[VDAC1P8]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[HOXA5]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[KLHDC2]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.0, -35.7); signed map (-6.4, -47.3). **Vector** length 110, 35.9% of its response variance represented; |z| ≥ 3 in 1,618 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +16.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.1 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +10.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.2 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +7.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.7 | +3.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.6 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.6 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -14.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.5 | -5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -4.3 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -7.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.0 | -2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol transfer protein beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:27,851,669-27,920,134 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VIB1B |
| Gene groups (HGNC) | Phosphatidylinositol transfer proteins |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: PI Metabolism; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P48739](https://www.uniprot.org/uniprotkb/P48739) (Phosphatidylinositol transfer protein beta isoform):

> Catalyzes the transfer of phosphatidylinositol and phosphatidylcholine between membranes. Also catalyzes the transfer of sphingomyelin (By similarity). Required for COPI-mediated retrograde transport from the Golgi to the endoplasmic reticulum; phosphatidylinositol and phosphatidylcholine transfer activity is essential for this function.

**Summary**, from NCBI Gene [23760](https://www.ncbi.nlm.nih.gov/gene/23760):

> This gene encodes a cytoplasmic protein that catalyzes the transfer of phosphatidylinositol and phosphatidylcholine between membranes. This transfer activity is required for COPI complex-mediated retrograde transport from the Golgi apparatus to the endoplasmic reticulum. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:9002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9002) · Entrez [23760](https://www.ncbi.nlm.nih.gov/gene/23760) · UniProt [P48739](https://www.uniprot.org/uniprotkb/P48739) · Ensembl [ENSG00000180957](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180957)

## Data

Gene col 11150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11150); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11150]; `tensor/DDL_lfc|DDL_z.npy` [11150]; `embed/gene_vectors.npy` [11150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11150 or target_col == 11150). Every well: [[PITPNB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITPNB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
