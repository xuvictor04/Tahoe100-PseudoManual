---
symbol: "FUBP1"
type: "gene"
col: 8542
ensembl_id: "ENSG00000162613"
name: "far upstream element binding protein 1"
location: "1p31.1"
module: 192
arm: "+"
pooled_cpm: 187.32
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# FUBP1

*far upstream element binding protein 1* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.83× (z +21.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.489× (z -14.9, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EWSR1]] (+0.83, fdr 7e-06), [[BCLAF1]] (+0.72, fdr 7e-06), [[SRSF1]] (+0.70, fdr 1e-05); moves opposite to [[MYO9B]] (-0.74, fdr 1e-05), [[FAM89B]] (-0.71, fdr 1e-05), [[TRPT1]] (-0.70, fdr 3e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8542.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.83×** | +21.7 | 0e+00 | 48/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +17.9 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.08×** | +15.3 | 0e+00 | 48/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.65×** | +14.8 | 0e+00 | 42/48 (HT-29, NCI-H23, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.96×** | +14.1 | 6e-43 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.32×** | +13.1 | 3e-37 | 48/49 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +9.7 | 3e-20 | 44/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +9.5 | 1e-19 | 38/48 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +8.8 | 9e-17 | 44/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +8.1 | 5e-14 | 43/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.42×** | +7.3 | 1e-11 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.44×** | +7.3 | 1e-11 | 40/48 (NCI-H460, HT-29, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +6.8 | 4e-10 | 39/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +6.7 | 9e-10 | 31/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +5.8 | 3e-07 | 35/48 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.015 | 22/49 (Hs 766T, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.18× | +3.3 | 0.027 | 18/48 (A549, HS-578T, …) | top dose only |  |
| [[Tadalafil (drug)]] 5 µM |  | 1.17× | +3.2 | 0.038 | 9/48 (LS 180, HepG2/C3A, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 1.10× | +2.9 | 0.072 | 2/48 (SK-MEL-2, COLO 205) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8542.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.489×** | -14.9 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.504×** | -14.3 | 6e-44 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.535×** | -13.1 | 8e-37 | 47/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -11.8 | 8e-30 | 40/49 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.633×** | -9.5 | 1e-19 | 44/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.730×** | -6.6 | 5e-09 | 39/48 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -5.5 | 4e-06 | 24/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.660×** | -4.5 | 4e-04 | 31/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.827×** | -4.0 | 0.005 | 21/47 (LoVo, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.8 | 0.010 | 22/49 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.835× | -3.6 | 0.016 | 21/47 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.854× | -3.3 | 0.047 | 19/48 (BT-474, CHP-212, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.849× | -3.3 | 0.047 | 21/48 (SW480, AN3 CA, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.862× | -3.1 | 0.078 | 15/48 (LS 180, RPMI-7951, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.863× | -3.1 | 0.078 | 12/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.902× | -3.0 | 0.086 | 3/48 (NCI-H2347, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 180 | 13 (4 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +21.0) | [[Panobinostat (drug)]] 5 µM 0.485× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 162 | 14 (6 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 4.80× (z +23.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +21.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -8.9) |
| [[HT-29 (line)]] | alt | 180 | 9 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +18.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +16.2) | [[Belinostat (drug)]] 5 µM 0.396× (z -13.1) |
| [[KATO III (line)]] | alt | 160 | 9 (2 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.51× (z +24.6) | [[Panobinostat (drug)]] 5 µM 0.359× (z -14.9) |
| [[SW480 (line)]] | alt | 224 | 8 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +22.1) | [[Panobinostat (drug)]] 5 µM 0.310× (z -21.2) |
| [[Panc 03.27 (line)]] | alt | 197 | 6 (2 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.408× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 220 | 10 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +15.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.491× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 191 | 7 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +17.2) | [[Belinostat (drug)]] 5 µM 0.438× (z -11.8) |
| [[HOP62 (line)]] | alt | 133 | 6 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.394× (z -11.6) |
| [[LoVo (line)]] | wt | 253 | 7 (3 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.81× (z +29.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -14.7) |
| [[LS 180 (line)]] | wt | 207 | 8 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.23× (z +23.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.0) |
| [[BT-474 (line)]] | alt | 185 | 4 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.1) |
| [[COLO 205 (line)]] | alt | 134 | 4 (2 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 227 | 4 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.96× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.362× (z -13.1) |
| [[J82 (line)]] | alt | 209 | 5 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.503× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 281 | 4 (2 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.363× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 155 | 4 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.415× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 188 | 3 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +14.0) | [[Belinostat (drug)]] 5 µM 0.316× (z -14.3) |
| [[SNU-1 (line)]] | wt | 302 | 6 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.482× (z -8.6) |
| [[SW1417 (line)]] | alt | 101 | 4 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.422× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 240 | 3 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -13.3) |
| [[Hs 766T (line)]] | wt | 188 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 126 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.396× (z -9.0) |
| [[RKO (line)]] | wt | 229 | 4 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 188 | 4 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.419× (z -9.2) |
| [[A-172 (line)]] | wt | 87.1 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +15.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +9.2) | — |
| [[A549 (line)]] | wt | 144 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 238 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.524× (z -8.5) |
| [[HS-578T (line)]] | alt | 157 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 183 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.447× (z -12.1) |
| [[SW 900 (line)]] | alt | 173 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -9.4) |
| [[SW48 (line)]] | wt | 245 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +15.0) | [[Panobinostat (drug)]] 5 µM 0.396× (z -9.2) |
| [[A498 (line)]] | wt | 207 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -10.2) |
| [[HCT15 (line)]] | alt | 224 | 2 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 134 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.43× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +14.0) | — |
| [[SHP-77 (line)]] | alt | 176 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.503× (z -9.2) |
| [[C32 (line)]] | wt | 152 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +9.0) | — |
| [[H4 (line)]] | wt | 137 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.95× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 190 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.487× (z -8.9) |
| [[SNU-423 (line)]] | alt | 145 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 207 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 189 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW 1271 (line)]] | alt | 159 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.62× (z +8.5) | — |
| [[A-427 (line)]] | wt | 197 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 246 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 162 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | +0.83 | +0.78 / +0.81 | both halves | 7e-06 | STRING 492 |
| [[BCLAF1]] | +0.72 | +0.64 / +0.64 | both halves | 7e-06 | STRING 433 |
| [[SRSF1]] | +0.70 | +0.54 / +0.65 | both halves | 1e-05 | STRING 628 |
| [[HNRNPM]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 | STRING 725 |
| [[CC2D2A]] | +0.67 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[ZNF280D]] | +0.67 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[HNRNPH3]] | +0.65 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[U2SURP]] | +0.65 | +0.51 / +0.66 | both halves | 1e-05 | STRING 460 |
| [[ILF3]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 | STRING 592 |
| [[CUL5]] | +0.64 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[GTF3C6]] | +0.64 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[TXNRD2]] | +0.63 | +0.40 / +0.53 | both halves | 5e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | -0.74 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[FAM89B]] | -0.71 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[TRPT1]] | -0.70 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[ARID3B]] | -0.68 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[PLIN3]] | -0.68 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[TMEM184B]] | -0.67 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[DNASE1L1]] | -0.67 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | -0.66 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[MPG]] | -0.66 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[DUSP18]] | -0.64 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[CIB1]] | -0.64 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[RTN2]] | -0.64 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises FUBP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises FUBP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction -0.795). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.6, 1.7); signed map (14.4, -37.8). **Vector** length 83.2, 30.5% of its response variance represented; |z| ≥ 3 in 1,374 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.9 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.7 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.4 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.3 | +14.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | -0.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.1 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.8 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | -0.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -13.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -14.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -9.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -4.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | far upstream element binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:77,944,055-77,979,110 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBP; previously FUBP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AE4](https://www.uniprot.org/uniprotkb/Q96AE4) (Far upstream element-binding protein 1):

> Regulates MYC expression by binding to a single-stranded far-upstream element (FUSE) upstream of the MYC promoter. May act both as activator and repressor of transcription.

**Summary**, from NCBI Gene [8880](https://www.ncbi.nlm.nih.gov/gene/8880):

> The protein encoded by this gene is a single stranded DNA-binding protein that binds to multiple DNA elements, including the far upstream element (FUSE) located upstream of c-myc. Binding to FUSE occurs on the non-coding strand, and is important to the regulation of c-myc in undifferentiated cells. This protein contains three domains, an amphipathic helix N-terminal domain, a DNA-binding central domain, and a C-terminal transactivation domain that contains three tyrosine-rich motifs. The …

**Accessions** — [HGNC:4004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4004) · Entrez [8880](https://www.ncbi.nlm.nih.gov/gene/8880) · UniProt [Q96AE4](https://www.uniprot.org/uniprotkb/Q96AE4) · Ensembl [ENSG00000162613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162613)

## Data

Gene col 8542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8542); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8542]; `tensor/DDL_lfc|DDL_z.npy` [8542]; `embed/gene_vectors.npy` [8542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8542 or target_col == 8542). Every well: [[FUBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
