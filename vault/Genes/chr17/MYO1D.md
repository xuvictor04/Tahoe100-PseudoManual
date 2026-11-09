---
symbol: "MYO1D"
type: "gene"
col: 10739
ensembl_id: "ENSG00000176658"
name: "myosin ID"
location: "17q11.2"
module: 31
arm: "+"
pooled_cpm: 200.56
n_lines_expressing: 37
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 37
direction_downstream: 31
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# MYO1D

*myosin ID* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +14.5, q 4e-45, up in 23 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.550× (z -15.9, q 0e+00, down in 24 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.352× (z -15.1, q 0e+00, down in 31 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L5]] (+0.62, fdr 7e-06), [[TMC6]] (+0.60, fdr 1e-05), [[RASA2]] (+0.56, fdr 1e-05); moves opposite to [[DZIP1L]] (-0.54, fdr 4e-05), [[BTN3A3]] (-0.50, fdr 3e-05), [[LMAN2L]] (-0.47, fdr 7e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[ST14]] → it (grade B ⚠); 31 go from it, the strongest it → [[DIAPH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +14.5 | 4e-45 | 23/35 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +13.3 | 7e-38 | 24/36 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +6.3 | 6e-08 | 22/35 (SW48, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +6.2 | 1e-07 | 16/35 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +6.0 | 2e-07 | 17/35 (A498, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +5.8 | 6e-07 | 15/35 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +5.2 | 1e-05 | 14/35 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +5.1 | 2e-05 | 6/35 (LOX-IMVI, SHP-77, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.20×** | +4.9 | 6e-05 | 20/35 (COLO 205, C32, …) | two highest doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.37×** | +4.6 | 3e-04 | 19/35 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.21×** | +4.5 | 4e-04 | 15/35 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.3 | 1e-03 | 14/36 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.2 | 0.001 | 13/35 (A498, J82, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +4.2 | 0.001 | 10/35 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.007 | 8/36 (RKO, NCI-H23, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.14× | +3.5 | 0.016 | 14/35 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.4 | 0.017 | 3/35 (A-427, C-33 A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.019 | 10/35 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.028 | 15/36 (SK-MEL-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 20 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.550×** | -15.9 | 0e+00 | 24/32 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.352×** | -15.1 | 0e+00 | 31/36 (HEC-1-A, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -13.3 | 6e-38 | 32/35 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.628×** | -12.8 | 1e-35 | 25/36 (HCT15, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.443×** | -11.8 | 7e-30 | 33/35 (HEC-1-A, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.610×** | -11.3 | 2e-27 | 28/33 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.679×** | -10.3 | 7e-23 | 24/35 (HEC-1-A, NCI-H23, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -9.8 | 7e-21 | 24/35 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.702×** | -9.8 | 1e-20 | 25/35 (HEC-1-A, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.708×** | -9.5 | 8e-20 | 24/35 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.808×** | -8.4 | 3e-15 | 20/35 (HEC-1-A, NCI-H1573, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.760×** | -7.6 | 2e-12 | 25/35 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **0.777×** | -7.0 | 1e-10 | 27/35 (KATO III, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.776×** | -6.7 | 7e-10 | 22/35 (A549, HEC-1-A, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.653×** | -6.2 | 3e-08 | 22/34 (A549, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.826×** | -5.3 | 4e-06 | 18/35 (HOP62, CFPAC-1, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.910× | -3.7 | 0.006 | 9/35 (HOP62, C32, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.875× | -3.5 | 0.010 | 14/36 (HOP62, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 452 | 5 (2 ⚠) | 15 (11 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.75× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -22.2) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -17.7) |
| [[HEC-1-A (line)]] | alt | 465 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -27.2) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.359× (z -18.6) |
| [[HOP62 (line)]] | alt | 206 | 0 | 14 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.659× (z -17.0) ⚠ position not correctable · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.412× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 237 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -18.7) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.235× (z -10.9) |
| [[KATO III (line)]] | alt | 464 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -16.7) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.255× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 226 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.348× (z -8.6) |
| [[A549 (line)]] | wt | 153 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -15.6) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -12.3) |
| [[HCT15 (line)]] | alt | 434 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.205× (z -11.3) |
| [[LoVo (line)]] | wt | 462 | 0 | 7 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.364× (z -13.4) |
| [[SW48 (line)]] | wt | 247 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -14.8) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.463× (z -9.0) |
| [[A498 (line)]] | wt | 62.6 | 6 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.13× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 199 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -21.3) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -15.8) |
| [[LS 180 (line)]] | wt | 420 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.254× (z -10.3) |
| [[BT-474 (line)]] | alt | 365 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.364× (z -10.3) |
| [[COLO 205 (line)]] | alt | 224 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.202× (z -10.4) |
| [[HT-29 (line)]] | alt | 375 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.388× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 144 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -18.3) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.514× (z -8.6) |
| [[A-427 (line)]] | wt | 256 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -15.3) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -13.7) |
| [[J82 (line)]] | alt | 97.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +13.2) | — |
| [[Panc 03.27 (line)]] | alt | 263 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.446× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.227× (z -11.5) |
| [[RKO (line)]] | wt | 56.4 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.7) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.74× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 285 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.602× (z -9.1) |
| [[SW480 (line)]] | alt | 460 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.454× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 255 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.89× (z +9.0) ⚠ cell-cycle shift, explains ~81% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 114 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.100× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 149 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.68× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -17.7) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SHP-77 (line)]] | alt | 91.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.05× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 216 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.486× (z -10.1) |
| [[CHP-212 (line)]] | wt | 137 | 0 | 1 | — | [[AZD-7648 (drug)]] 5 µM 0.0795× (z -8.7) |
| [[H4 (line)]] | wt | 70.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.51× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 130 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.92× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 230 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.471× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 43.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.0 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 39.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 202 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 25.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 48.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 27.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 22.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 39.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 45.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L5]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[TMC6]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[RASA2]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CDH1]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[CLDN4]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[RDH13]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TMEM45B]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PPP1R13B]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 | same gene group |
| [[B4GALNT3]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[KHDRBS3]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[USP53]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZIP1L]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[BTN3A3]] | -0.50 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[LMAN2L]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[LYSMD1]] | -0.45 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[OSGEPL1]] | -0.45 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[GPX8]] | -0.45 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[FAM120C]] | -0.45 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[MTERF1]] | -0.44 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[NUDT13]] | -0.44 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[ZFP30]] | -0.43 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[ZBTB6]] | -0.43 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ZKSCAN3]] | -0.43 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 35, C 2. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST14]] | B | ST14 activity raises MYO1D's level | lines that do not express ST14 (32) vs lines expressing it (18) | 4.15× lower at baseline in the lines without ST14 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[INAVA]] | B | INAVA activity raises MYO1D's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.58× lower at baseline in the lines without INAVA | 5e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[B3GNT3]] | B | B3GNT3 activity raises MYO1D's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.89× lower at baseline in the lines without B3GNT3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[CDH1]] | B | CDH1 activity raises MYO1D's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 4.27× lower at baseline in the lines without CDH1 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[MYO5B]] | B | MYO5B activity raises MYO1D's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.72× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[CLDN7]] | B | CLDN7 activity raises MYO1D's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 3.67× lower at baseline in the lines without CLDN7 | 0.002 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[C1orf116]] | B | C1orf116 activity raises MYO1D's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.60× lower at baseline in the lines without C1orf116 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[CBLC]] | B | CBLC activity raises MYO1D's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.27× lower at baseline in the lines without CBLC | 0.003 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[TMEM45B]] | B | TMEM45B activity raises MYO1D's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 3.65× lower at baseline in the lines without TMEM45B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises MYO1D's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.85× lower at baseline in the lines without TMPRSS4 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[FAM83B]] | B | FAM83B activity raises MYO1D's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.46× lower at baseline in the lines without FAM83B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[TMC4]] | B | TMC4 activity raises MYO1D's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.75× lower at baseline in the lines without TMC4 | 0.004 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 29, C 2. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIAPH1]] | B | MYO1D activity raises DIAPH1's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.54× lower at baseline in the lines without MYO1D | 0.002 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[MYO5B]] | B | MYO1D activity raises MYO5B's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 4.90× lower at baseline in the lines without MYO1D | 0.008 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[TMC6]] | B | MYO1D activity raises TMC6's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 3.09× lower at baseline in the lines without MYO1D | 0.012 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[EDA]] | B | MYO1D activity raises EDA's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.83× lower at baseline in the lines without MYO1D | 0.013 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[IGSF3]] | B | MYO1D activity raises IGSF3's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without MYO1D | 0.015 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[TMC4]] | B | MYO1D activity raises TMC4's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without MYO1D | 0.016 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[CDH1]] | B | MYO1D activity raises CDH1's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 4.72× lower at baseline in the lines without MYO1D | 0.016 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[CRYBG2]] | B | MYO1D activity raises CRYBG2's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 2.79× lower at baseline in the lines without MYO1D | 0.018 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[PRDX6-AS1]] | B | MYO1D activity lowers PRDX6-AS1's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.53× higher at baseline in the lines without MYO1D | 0.020 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[ST14]] | B | MYO1D activity raises ST14's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 4.41× lower at baseline in the lines without MYO1D | 0.020 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[GDPD5]] | B | MYO1D activity raises GDPD5's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.20× lower at baseline in the lines without MYO1D | 0.022 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[INAVA]] | B | MYO1D activity raises INAVA's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 3.77× lower at baseline in the lines without MYO1D | 0.022 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, 55.2); signed map (0.0, 38.0). **Vector** length 128, 40.2% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +14.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +13.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +5.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -7.1 | -11.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.8 | -15.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -13.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.4 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | myosin ID |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:32,492,522-32,877,177 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0727, myr4, PPP1R108 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Myosin heavy chains, class I |
| Matched by | ensembl_id |

**Function**, from UniProt [O94832](https://www.uniprot.org/uniprotkb/O94832) (Unconventional myosin-Id):

> Unconventional myosin that functions as actin-based motor protein with ATPase activity (By similarity). Plays a role in endosomal protein trafficking, and especially in the transfer of cargo proteins from early to recycling endosomes (By similarity). Required for normal planar cell polarity in ciliated tracheal cells, for normal rotational polarity of cilia, and for coordinated, unidirectional ciliary movement in the trachea. Required for normal, polarized cilia organization in brain ependymal …

**Summary**, from NCBI Gene [4642](https://www.ncbi.nlm.nih.gov/gene/4642):

> Enables protein domain specific binding activity. Predicted to be involved in several processes, including actin filament organization; actin filament-based movement; and obsolete early endosome to recycling endosome transport. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7598) · Entrez [4642](https://www.ncbi.nlm.nih.gov/gene/4642) · UniProt [O94832](https://www.uniprot.org/uniprotkb/O94832) · Ensembl [ENSG00000176658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176658)

## Data

Gene col 10739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10739); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10739]; `tensor/DDL_lfc|DDL_z.npy` [10739]; `embed/gene_vectors.npy` [10739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10739 or target_col == 10739). Every well: [[MYO1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
