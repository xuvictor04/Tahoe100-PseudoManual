---
symbol: "TMEM131"
type: "gene"
col: 1124
ensembl_id: "ENSG00000075568"
name: "transmembrane protein 131"
location: "2q11.2"
module: 194
arm: "+"
pooled_cpm: 215.32
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# TMEM131

*transmembrane protein 131* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.65× (z +13.1, q 2e-36, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.623× (z -12.3, q 4e-32, down in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.682× (z -10.0, q 6e-21, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF12]] (+0.64, fdr 9e-06), [[NSD1]] (+0.61, fdr 2e-05), [[MED1]] (+0.54, fdr 4e-05); moves opposite to [[ZNF836]] (-0.50, fdr 1e-04), [[SGSM3]] (-0.49, fdr 4e-05), [[CEP295NL]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TP53]] → it (grade A ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +13.1 | 2e-36 | 47/48 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +9.2 | 1e-17 | 38/49 (A498, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +6.7 | 3e-09 | 32/48 (BT-474, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +6.7 | 3e-09 | 29/48 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +6.5 | 7e-09 | 34/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.7 | 1e-06 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +4.9 | 8e-05 | 29/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.7 | 2e-04 | 23/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.9 | 0.006 | 17/48 (PANC-1, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1124.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.623×** | -12.3 | 4e-32 | 38/49 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -10.0 | 6e-21 | 43/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -9.9 | 1e-20 | 34/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.689×** | -9.4 | 1e-18 | 33/44 (NCI-H23, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.730×** | -8.2 | 2e-14 | 38/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.732×** | -8.1 | 4e-14 | 38/48 (A549, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.808×** | -7.9 | 3e-13 | 27/49 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -6.8 | 5e-10 | 26/48 (LOX-IMVI, C32, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~16% of this change | **0.770×** | -6.8 | 6e-10 | 36/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -5.7 | 6e-07 | 25/48 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.814×** | -5.4 | 4e-06 | 25/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.819×** | -4.7 | 2e-04 | 23/45 (SW 900, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -4.2 | 0.001 | 14/49 (SW 900, C32, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.868× | -3.7 | 0.009 | 11/48 (J82, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.910× | -3.5 | 0.019 | 5/49 (SW 900, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.883× | -3.2 | 0.039 | 12/48 (A549, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.884× | -3.2 | 0.040 | 13/47 (A549, HT-29, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.842× | -3.2 | 0.040 | 17/48 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.045 | 18/48 (SW 1271, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.887× | -3.1 | 0.046 | 7/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.888× | -3.1 | 0.049 | 9/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.851× | -3.0 | 0.066 | 17/48 (hTERT-HPNE, SNU-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.895× | -2.9 | 0.087 | 3/48 (SNU-423, C32, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.858× | -2.9 | 0.093 | 14/48 (LoVo, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 270 | 5 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.553× (z -11.4) |
| [[A-427 (line)]] | wt | 333 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.15× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.522× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.542× (z -9.8) |
| [[A549 (line)]] | wt | 216 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.14× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.496× (z -10.8) |
| [[LS 180 (line)]] | wt | 252 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.32× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.538× (z -9.4) |
| [[SW480 (line)]] | alt | 200 | 2 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -15.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 157 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +17.5) | — |
| [[HOP62 (line)]] | alt | 185 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +10.4) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.635× (z -11.2) |
| [[LoVo (line)]] | wt | 191 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.555× (z -10.8) |
| [[PANC-1 (line)]] | alt | 203 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.574× (z -9.7) ⚠ toxic |
| [[C32 (line)]] | wt | 280 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.48× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.536× (z -9.7) |
| [[COLO 205 (line)]] | alt | 154 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +12.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.462× (z -9.3) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 241 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.97× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.472× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 254 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 390 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -18.1) ⚠ cell-cycle shift, explains ~11% of this change |
| [[SW48 (line)]] | wt | 246 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.29× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -8.9) ⚠ cell-cycle shift, explains ~11% of this change |
| [[H4 (line)]] | wt | 220 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.02× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 240 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 136 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.560× (z -8.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 424 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -16.9) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 406 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 252 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 338 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -10.5) ⚠ cell-cycle shift, explains ~11% of this change |
| [[SW1417 (line)]] | alt | 202 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.491× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.516× (z -10.4) |
| [[A-172 (line)]] | wt | 200 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.52× (z +11.7) | — |
| [[CHP-212 (line)]] | wt | 236 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -11.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.467× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 199 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 108 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 245 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.344× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 221 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.34× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 229 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.549× (z -8.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.500× (z -10.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 145 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.06× (z +8.7) ⚠ unreliable plate only | — |
| [[J82 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.461× (z -11.3) ⚠ toxic |
| [[KATO III (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.475× (z -10.9) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.586× (z -8.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[NCI-H661 (line)]] | alt | 222 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.316× (z -8.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -10.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 163 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 236 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 153 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 183 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 204 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF12]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[NSD1]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[MED1]] | +0.54 | +0.48 / +0.40 | both halves | 4e-05 |  |
| [[ZFP91]] | +0.53 | +0.30 / +0.56 | both halves | 2e-04 |  |
| [[ERCC6L2]] | +0.53 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[ASXL2]] | +0.52 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[PRR4]] | +0.51 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[BAX]] | +0.50 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[ACTA2]] | +0.50 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[TRAPPC8]] | +0.50 | +0.47 / +0.39 | both halves | 6e-05 | STRING 614 |
| [[PRH1]] | +0.50 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[ZMYND11]] | +0.50 | +0.38 / +0.51 | both halves | 7e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF836]] | -0.50 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[SGSM3]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[CEP295NL]] | -0.48 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[MIR29B2CHG]] | -0.47 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[TMEM243]] | -0.46 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[ZNF526]] | -0.46 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[CLDN12]] | -0.46 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[RNF139-DT]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[DNMT3B]] | -0.46 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[DAGLB]] | -0.45 | -0.26 / -0.48 | both halves | 4e-04 |  |
| [[ORMDL3]] | -0.45 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[SNHG21]] | -0.45 | -0.42 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 1, B 0, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens TMEM131's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 0.83× as strongly (z diff +0.80); rises at some drug-doses, falls at others (42% from rises): TAK-901 5 µM: 1.60x vs 3.23x (z diff +4.8); Panobinostat 5 µM: 0.77x vs 0.66x (z diff +2.3); Belinostat 5 µM: 0.78x vs 0.68x (z diff +2.1) | 0.040 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-6.2, 4.4); signed map (18.2, -29.6). **Vector** length 102, 31.5% of its response variance represented; |z| ≥ 3 in 1,256 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.7 | +13.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.7 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | -12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | -0.8 |
|  | [[Larotrectinib (drug)]] 5 µM |  | +2.2 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.6 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -5.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 131 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:97,756,333-97,995,948 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CC28, YR-23, RW1, KIAA0257, PRO1048 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92545](https://www.uniprot.org/uniprotkb/Q92545) (Transmembrane protein 131):

> Collagen binding transmembrane protein involved in collagen secretion by recruiting the ER-to-Golgi transport complex TRAPPIII. May play a role in the immune response to viral infection.

**Summary**, from NCBI Gene [23505](https://www.ncbi.nlm.nih.gov/gene/23505):

> Enables collagen binding activity. Involved in collagen biosynthetic process. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30366) · Entrez [23505](https://www.ncbi.nlm.nih.gov/gene/23505) · UniProt [Q92545](https://www.uniprot.org/uniprotkb/Q92545) · Ensembl [ENSG00000075568](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075568)

## Data

Gene col 1124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1124); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1124]; `tensor/DDL_lfc|DDL_z.npy` [1124]; `embed/gene_vectors.npy` [1124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1124 or target_col == 1124). Every well: [[TMEM131 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM131.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
