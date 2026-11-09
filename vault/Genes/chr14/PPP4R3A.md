---
symbol: "PPP4R3A"
type: "gene"
col: 2022
ensembl_id: "ENSG00000100796"
name: "protein phosphatase 4 regulatory subunit 3A"
location: "14q32.12"
module: 62
arm: "+"
pooled_cpm: 129.5
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# PPP4R3A

*protein phosphatase 4 regulatory subunit 3A* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.64× (z +28.9, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.420× (z -25.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM5]] (+0.68, fdr 1e-05), [[CREBBP]] (+0.65, fdr 1e-05), [[XPC]] (+0.64, fdr 3e-05); moves opposite to [[ASPH]] (-0.60, fdr 1e-05), [[MSN]] (-0.59, fdr 2e-05), [[KIF21B]] (-0.58, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.64×** | +28.9 | 0e+00 | 49/49 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.21×** | +23.2 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +21.0 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.70×** | +20.0 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.84×** | +17.7 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +17.3 | 0e+00 | 36/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +16.0 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +10.4 | 3e-23 | 36/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +8.8 | 7e-17 | 32/48 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.35×** | +8.0 | 8e-14 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +6.6 | 2e-09 | 30/48 (RKO, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.21×** | +5.3 | 6e-06 | 22/48 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.20× | +4.7 | 9e-05 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +4.4 | 4e-04 | 19/47 (NCI-H460, A549, …) | all doses, flat | low cells (technical?) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.14× | +3.8 | 0.006 | 6/49 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.030 | 1/48 (SHP-77) | inconsistent across doses | plate-row cell shift |
| [[TAK-901 (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.035 | 16/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.085 | 7/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.096 | 10/48 (SW48, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.11× | +2.9 | 0.096 | 16/47 (SW48, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2022.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.420×** | -25.3 | 0e+00 | 48/48 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.466×** | -22.3 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -21.5 | 0e+00 | 42/44 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.506×** | -19.8 | 0e+00 | 45/48 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.522×** | -18.9 | 0e+00 | 45/49 (A-427, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.714×** | -13.9 | 1e-41 | 44/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.609×** | -13.0 | 6e-37 | 46/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.627×** | -12.5 | 3e-34 | 38/45 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.721×** | -9.5 | 1e-19 | 39/49 (SW480, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.735×** | -8.9 | 2e-17 | 36/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.770×** | -7.6 | 2e-12 | 30/48 (A-427, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.611×** | -7.5 | 3e-12 | 40/49 (CFPAC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.844× | -7.0 | 1e-10 | 23/49 (CFPAC-1, A549, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.827×** | -3.9 | 0.003 | 14/48 (H4, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | 0.869× | -3.9 | 0.004 | 18/47 (CFPAC-1, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 142 | 11 (4 ⚠) | 9 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.85× (z +25.5) | [[Panobinostat (drug)]] 0.5 µM 0.433× (z -17.8) |
| [[KATO III (line)]] | alt | 121 | 7 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 124 | 9 (3 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.6× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.407× (z -12.7) |
| [[SW 900 (line)]] | alt | 183 | 6 (1 ⚠) | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.49× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.359× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 139 | 5 (1 ⚠) | 8 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 6.00× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.326× (z -17.5) |
| [[HOP62 (line)]] | alt | 111 | 6 (1 ⚠) | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.66× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.414× (z -13.2) |
| [[LoVo (line)]] | wt | 138 | 7 (2 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.488× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 122 | 6 (1 ⚠) | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 14.5× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.456× (z -10.7) |
| [[LS 180 (line)]] | wt | 188 | 6 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.33× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.278× (z -14.4) |
| [[SW1417 (line)]] | alt | 120 | 7 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.370× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 169 | 2 | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.19× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.419× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 151 | 5 (1 ⚠) | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.19× (z +19.6) | [[Panobinostat (drug)]] 0.5 µM 0.467× (z -13.6) |
| [[PANC-1 (line)]] | alt | 80.4 | 9 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +21.0) | [[Panobinostat (drug)]] 5 µM 0.576× (z -8.9) |
| [[SHP-77 (line)]] | alt | 145 | 6 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.420× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 108 | 4 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.386× (z -13.5) |
| [[COLO 205 (line)]] | alt | 154 | 6 (2 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 14.5× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.263× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 208 | 2 | 8 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.04× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -16.4) |
| [[A-427 (line)]] | wt | 127 | 3 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.80× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.453× (z -11.0) |
| [[A498 (line)]] | wt | 99.3 | 3 (1 ⚠) | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +15.4) | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -13.8) |
| [[BT-474 (line)]] | alt | 178 | 7 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 117 | 5 (2 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.05× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.403× (z -12.3) |
| [[SW48 (line)]] | wt | 254 | 5 (1 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 8.16× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.303× (z -11.5) |
| [[A549 (line)]] | wt | 167 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.3× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.329× (z -14.4) |
| [[HT-29 (line)]] | alt | 90.4 | 4 (1 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.02× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.473× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 124 | 3 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.7× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.392× (z -9.7) |
| [[RKO (line)]] | wt | 128 | 6 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 16.2× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -16.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 148 | 6 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.4× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.0957× (z -23.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 185 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.07× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.422× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 111 | 6 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 7.31× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.506× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 148 | 3 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.18× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.433× (z -12.7) |
| [[C32 (line)]] | wt | 133 | 2 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 14.6× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.405× (z -9.3) |
| [[H4 (line)]] | wt | 120 | 3 (1 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.1× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 230 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.23× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.450× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 118 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.64× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 86.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.496× (z -8.6) |
| [[A-172 (line)]] | wt | 81.3 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 10.1× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.405× (z -9.8) |
| [[Hs 766T (line)]] | wt | 81.2 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 8.47× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.426× (z -10.6) |
| [[J82 (line)]] | alt | 98.1 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.412× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 87.9 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 6.00× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 104 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 9.57× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.377× (z -10.1) |
| [[AN3 CA (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -8.9) ⚠ cell-cycle shift, explains ~88% of this change |
| [[C-33 A (line)]] | alt | 65.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.70× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -17.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 87.8 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.08× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.399× (z -9.7) |
| [[CHP-212 (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -11.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM5]] | +0.68 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[XPC]] | +0.64 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[NFYC]] | +0.64 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SPATA18]] | +0.64 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PPM1D]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TP53I3]] | +0.62 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PPCS]] | +0.62 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PURPL]] | +0.62 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CES2]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[COIL]] | +0.61 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[GTF2IRD2B]] | +0.61 | +0.53 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASPH]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[MSN]] | -0.59 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[KIF21B]] | -0.58 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[ATP13A2]] | -0.57 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[CORO1C]] | -0.57 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SMS]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[FLNB]] | -0.55 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[SEPTIN10]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ITPR3]] | -0.54 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[LTBP4]] | -0.54 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[ENTPD4]] | -0.54 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[TPMT]] | -0.54 | -0.36 / -0.46 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PPP4R3A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PPP4R3A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.4, 35.0); signed map (40.6, -23.5). **Vector** length 101, 34.2% of its response variance represented; |z| ≥ 3 in 1,491 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +0.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +28.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +17.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | -0.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +4.2 | +0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.9 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.9 | -0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -13.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.6 | -9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -13.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -19.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -7.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | +2.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 4 regulatory subunit 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:91,457,508-91,510,554 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20707, MSTP033, FLFL1, smk-1, smk1, PP4R3; previously KIAA2010, SMEK1 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IN85](https://www.uniprot.org/uniprotkb/Q6IN85) (Serine/threonine-protein phosphatase 4 regulatory subunit 3A):

> Regulatory subunit of serine/threonine-protein phosphatase 4. May regulate the activity of PPP4C at centrosomal microtubule organizing centers. The PPP4C-PPP4R2-PPP4R3A PP4 complex specifically dephosphorylates H2AX phosphorylated on 'Ser-140' (gamma-H2AX) generated during DNA replication and required for DNA DSB repair.

**Summary**, from NCBI Gene [55671](https://www.ncbi.nlm.nih.gov/gene/55671):

> Predicted to enable protein phosphatase activator activity. Predicted to be involved in DNA damage response and regulation of double-strand break repair. Predicted to act upstream of or within positive regulation of gluconeogenesis and protein dephosphorylation. Located in cytosol and nuclear speck. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:20219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20219) · Entrez [55671](https://www.ncbi.nlm.nih.gov/gene/55671) · UniProt [Q6IN85](https://www.uniprot.org/uniprotkb/Q6IN85) · Ensembl [ENSG00000100796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100796)

## Data

Gene col 2022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2022); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2022]; `tensor/DDL_lfc|DDL_z.npy` [2022]; `embed/gene_vectors.npy` [2022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2022 or target_col == 2022). Every well: [[PPP4R3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP4R3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
