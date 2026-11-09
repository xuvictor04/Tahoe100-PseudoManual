---
symbol: "MARCHF7"
type: "gene"
col: 5878
ensembl_id: "ENSG00000136536"
name: "membrane associated ring-CH-type finger 7"
location: "2q24.2"
module: 11
arm: "+"
pooled_cpm: 220.45
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MARCHF7

*membrane associated ring-CH-type finger 7* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +19.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.444× (z -17.7, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.519× (z -14.3, q 3e-44, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL18]] (+0.68, fdr 1e-05), [[ZNF197]] (+0.66, fdr 1e-05), [[USP47]] (+0.66, fdr 1e-05); moves opposite to [[GSDMB]] (-0.60, fdr 4e-05), [[SEPTIN7P14]] (-0.59, fdr 2e-04), [[MLEC]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF480]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +19.1 | 0e+00 | 47/48 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +14.4 | 1e-44 | 47/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +13.0 | 2e-36 | 45/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +10.7 | 1e-24 | 45/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.29×** | +9.5 | 4e-19 | 43/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +7.9 | 3e-13 | 42/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +7.9 | 3e-13 | 43/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +7.4 | 9e-12 | 36/48 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.1 | 6e-11 | 33/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.6 | 3e-09 | 34/48 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +6.1 | 6e-08 | 36/48 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +5.6 | 1e-06 | 33/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 4e-06 | 33/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.021 | 21/48 (A549, SNU-1, …) | all doses, stronger at high dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.031 | 27/48 (HOP62, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.050 | 23/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5878.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.444×** | -17.7 | 0e+00 | 46/49 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -16.0 | 0e+00 | 42/44 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.519×** | -14.3 | 3e-44 | 47/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.521×** | -14.2 | 7e-44 | 48/48 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.589×** | -10.7 | 1e-24 | 36/45 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.627×** | -10.2 | 2e-22 | 45/48 (SNU-423, SW 900, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.807×** | -6.6 | 3e-09 | 27/49 (A549, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.743×** | -6.5 | 6e-09 | 37/48 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.805×** | -4.6 | 3e-04 | 28/47 (AN3 CA, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -4.4 | 5e-04 | 26/48 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.831×** | -4.0 | 0.003 | 25/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.745×** | -3.9 | 0.004 | 31/48 (NCI-H2347, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.844× | -3.7 | 0.010 | 23/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.899× | -3.3 | 0.041 | 7/48 (Hs 766T, NCI-H1792, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.756×** | -3.2 | 0.054 | 23/45 (RPMI-7951, AN3 CA, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.865× | -3.2 | 0.057 | 17/48 (H4, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 219 | 7 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +21.5) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.489× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 271 | 6 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.497× (z -11.0) |
| [[A549 (line)]] | wt | 263 | 4 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +19.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -18.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.388× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 238 | 6 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.510× (z -11.1) |
| [[SW480 (line)]] | alt | 205 | 6 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +15.3) | [[Panobinostat (drug)]] 0.5 µM 0.489× (z -13.2) |
| [[A-172 (line)]] | wt | 282 | 2 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -17.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.463× (z -12.4) |
| [[KATO III (line)]] | alt | 120 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -12.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 247 | 4 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +23.2) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 267 | 5 | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.32× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.481× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 221 | 3 | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.10× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.451× (z -12.4) |
| [[BT-474 (line)]] | alt | 250 | 4 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 229 | 4 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.470× (z -10.4) |
| [[HOP62 (line)]] | alt | 290 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.379× (z -13.4) |
| [[LoVo (line)]] | wt | 156 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -11.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 308 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.470× (z -10.6) |
| [[HS-578T (line)]] | alt | 195 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +17.1) | [[Panobinostat (drug)]] 5 µM 0.515× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 251 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.447× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 276 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.502× (z -9.8) |
| [[SNU-423 (line)]] | alt | 196 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.403× (z -12.9) |
| [[SW 900 (line)]] | alt | 246 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -12.3) |
| [[SW1417 (line)]] | alt | 296 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.545× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 144 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 243 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.399× (z -11.5) |
| [[HT-29 (line)]] | alt | 151 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +20.2) | — |
| [[NCI-H1573 (line)]] | alt | 118 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 227 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -18.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 199 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.584× (z -8.8) |
| [[J82 (line)]] | alt | 250 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.534× (z -8.9) |
| [[LS 180 (line)]] | wt | 176 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 224 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.400× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.420× (z -11.1) |
| [[H4 (line)]] | wt | 230 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.488× (z -8.7) |
| [[Hs 766T (line)]] | wt | 163 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.459× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 229 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -10.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 244 | 2 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.14× (z +10.0) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.233× (z -10.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 214 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.471× (z -11.3) |
| [[SW48 (line)]] | wt | 223 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -13.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 204 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.475× (z -8.8) |
| [[HCT15 (line)]] | alt | 240 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -9.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 228 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 127 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 184 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.76× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -9.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 214 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -14.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 236 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -10.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 248 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -13.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 277 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 236 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL18]] | +0.68 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ZNF197]] | +0.66 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[USP47]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ARL14EP]] | +0.66 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ZC3HC1]] | +0.64 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ZNF518A]] | +0.63 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[ZNF75A]] | +0.63 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[THG1L]] | +0.62 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ZFY]] | +0.62 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[LATS1]] | +0.61 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[ZNF155]] | +0.60 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[FAM200A]] | +0.60 | +0.42 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSDMB]] | -0.60 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SEPTIN7P14]] | -0.59 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[MLEC]] | -0.59 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[GAK]] | -0.57 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[SEC61A1]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[RPA1]] | -0.56 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SHQ1]] | -0.55 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[TM9SF2]] | -0.55 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[RAB40B]] | -0.54 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[PIK3R2]] | -0.54 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[LAPTM4A]] | -0.54 | -0.48 / -0.43 | both halves | 4e-05 |  |
| [[PMPCA]] | -0.53 | -0.34 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF480]] | C | ZNF480 activity strengthens MARCHF7's drug response | lines that do not express ZNF480 (3) vs lines expressing it (46) | the lines without ZNF480 respond 0.91× as strongly (z diff +1.05); strongest at Dinaciclib 0.05 µM: 0.88x vs 0.60x (z diff +4.8) | 0.091 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP14, CIBAR1, ZNF540; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-31.7, 7.1); signed map (3.8, -22.2). **Vector** length 84.9, 30.3% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.9 | +14.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +19.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +13.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.1 | -0.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -14.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -10.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -14.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | -1.9 | +0.2 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated ring-CH-type finger 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:159,712,457-159,771,027 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MARCH-VII, RNF177; previously AXOT, MARCH7 |
| Gene groups (HGNC) | Ring finger proteins; Membrane associated ring-CH-type fingers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H992](https://www.uniprot.org/uniprotkb/Q9H992) (E3 ubiquitin-protein ligase MARCHF7):

> E3 ubiquitin-protein ligase which may specifically enhance the E2 activity of HIP2. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfer the ubiquitin to targeted substrates. May be involved in T-cell proliferation by regulating LIF secretion (By similarity). May play a role in lysosome homeostasis. Promotes 'Lys-6', 'Lys-11' and 'Lys-63'-linked mixed polyubiquitination on ATG14 leading to the inhibition of autophagy …

**Summary**, from NCBI Gene [64844](https://www.ncbi.nlm.nih.gov/gene/64844):

> MARCH7 is a member of the MARCH family of membrane-bound E3 ubiquitin ligases (EC 6.3.2.19). MARCH proteins add ubiquitin (see MIM 191339) to target lysines in substrate proteins, thereby signaling their vesicular transport between membrane compartments (Bartee et al., 2004 [PubMed 14722266]).[supplied by OMIM, Mar 2010]

**Accessions** — [HGNC:17393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17393) · Entrez [64844](https://www.ncbi.nlm.nih.gov/gene/64844) · UniProt [Q9H992](https://www.uniprot.org/uniprotkb/Q9H992) · Ensembl [ENSG00000136536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136536)

## Data

Gene col 5878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5878); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5878]; `tensor/DDL_lfc|DDL_z.npy` [5878]; `embed/gene_vectors.npy` [5878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5878 or target_col == 5878). Every well: [[MARCHF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCHF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
