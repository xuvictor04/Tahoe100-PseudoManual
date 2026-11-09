---
symbol: "DYRK1A"
type: "gene"
col: 8081
ensembl_id: "ENSG00000157540"
name: "dual specificity tyrosine phosphorylation regulated kinase 1A"
location: "21q22.13"
module: 46
arm: "+"
pooled_cpm: 283.86
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# DYRK1A

*dual specificity tyrosine phosphorylation regulated kinase 1A* — 21q22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.08× (z +15.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.236× (z -21.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAF1]] (+0.76, fdr 7e-06), [[CHASERR]] (+0.73, fdr 7e-06), [[WAC]] (+0.73, fdr 7e-06); moves opposite to [[DAP3]] (-0.62, fdr 1e-05), [[STK4]] (-0.59, fdr 6e-05), [[CAP1]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00649]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CREBBP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +15.6 | 0e+00 | 47/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.96×** | +15.2 | 0e+00 | 49/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.41×** | +13.2 | 1e-37 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.27×** | +11.4 | 6e-28 | 46/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +9.8 | 1e-20 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.89×** | +9.6 | 9e-20 | 41/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +9.1 | 1e-17 | 44/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +8.5 | 2e-15 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +7.7 | 8e-13 | 39/48 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.52×** | +6.3 | 1e-08 | 35/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 2e-05 | 28/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.30×** | +4.0 | 0.004 | 27/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.007 | 33/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Tomivosertib (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.070 | 33/48 (NCI-H1573, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8081.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.236×** | -21.7 | 0e+00 | 48/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.239×** | -21.5 | 0e+00 | 48/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.316×** | -17.3 | 0e+00 | 48/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.322×** | -16.4 | 0e+00 | 44/44 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.387×** | -14.3 | 5e-44 | 49/49 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.497×** | -9.7 | 3e-20 | 39/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.538×** | -9.3 | 1e-18 | 46/48 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.698×** | -7.6 | 2e-12 | 47/48 (HT-29, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.671×** | -5.8 | 5e-07 | 38/47 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.701×** | -5.3 | 5e-06 | 42/48 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.737×** | -4.6 | 3e-04 | 37/48 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.740×** | -4.5 | 3e-04 | 34/49 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.632×** | -3.6 | 0.014 | 35/49 (HT-29, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **0.810×** | -3.2 | 0.063 | 27/47 (RPMI-7951, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.812×** | -3.1 | 0.066 | 25/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 238 | 14 (3 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +27.1) | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -19.1) |
| [[SW480 (line)]] | alt | 306 | 9 (1 ⚠) | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +19.2) | [[Panobinostat (drug)]] 5 µM 0.199× (z -25.1) |
| [[SW1417 (line)]] | alt | 383 | 4 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -24.5) |
| [[H4 (line)]] | wt | 224 | 8 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.94× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.267× (z -12.5) |
| [[HT-29 (line)]] | alt | 228 | 5 (1 ⚠) | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.57× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.152× (z -25.3) |
| [[LS 180 (line)]] | wt | 313 | 8 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.82× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -14.8) |
| [[PANC-1 (line)]] | alt | 155 | 10 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +20.0) | [[Panobinostat (drug)]] 5 µM 0.262× (z -19.8) |
| [[HOP62 (line)]] | alt | 296 | 5 | 7 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.84× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -18.6) |
| [[LoVo (line)]] | wt | 234 | 8 (2 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +18.0) | [[Panobinostat (drug)]] 5 µM 0.286× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 381 | 4 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.156× (z -19.7) |
| [[NCI-H1573 (line)]] | alt | 352 | 6 (2 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -17.2) |
| [[NCI-H23 (line)]] | alt | 199 | 7 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.87× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.349× (z -13.9) |
| [[SNU-423 (line)]] | alt | 219 | 5 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -15.6) |
| [[SW48 (line)]] | wt | 351 | 6 (1 ⚠) | 5 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 16.0× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.208× (z -13.0) |
| [[A-172 (line)]] | wt | 262 | 4 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.248× (z -15.7) |
| [[A-427 (line)]] | wt | 260 | 5 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.277× (z -14.7) |
| [[A549 (line)]] | wt | 184 | 4 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +22.1) | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -18.0) |
| [[KATO III (line)]] | alt | 157 | 7 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +18.6) | [[Panobinostat (drug)]] 5 µM 0.235× (z -19.8) |
| [[NCI-H1792 (line)]] | alt | 266 | 5 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.180× (z -20.0) |
| [[RKO (line)]] | wt | 250 | 6 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +21.5) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.320× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 243 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.124× (z -22.9) |
| [[COLO 205 (line)]] | alt | 276 | 6 (2 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 16.5× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.265× (z -17.3) |
| [[HCT15 (line)]] | alt | 325 | 4 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.70× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.369× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 468 | 2 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.59× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.168× (z -17.7) |
| [[Panc 03.27 (line)]] | alt | 296 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.191× (z -18.8) |
| [[RPMI-7951 (line)]] | alt | 261 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -16.8) |
| [[CFPAC-1 (line)]] | alt | 459 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.01× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.186× (z -18.0) |
| [[HEC-1-A (line)]] | alt | 356 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.208× (z -18.6) |
| [[HepG2_C3A (line)]] | wt | 287 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.25× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -16.3) |
| [[Hs 766T (line)]] | wt | 255 | 3 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.78× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.209× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 208 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -14.0) |
| [[J82 (line)]] | alt | 204 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 300 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.96× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.174× (z -18.5) |
| [[NCI-H2030 (line)]] | alt | 336 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.273× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 230 | 4 (1 ⚠) | 4 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.51× (z +12.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 9.81× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -14.3) |
| [[SW 900 (line)]] | alt | 277 | 2 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.38× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -19.0) |
| [[C-33 A (line)]] | alt | 363 | 2 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.27× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.241× (z -14.3) |
| [[A498 (line)]] | wt | 298 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +16.3) | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -15.2) |
| [[BT-474 (line)]] | alt | 261 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -16.0) |
| [[C32 (line)]] | wt | 313 | 2 | 4 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 14.1× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.315× (z -11.3) |
| [[SHP-77 (line)]] | alt | 342 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.32× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.286× (z -13.4) |
| [[SNU-1 (line)]] | wt | 386 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.15× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.327× (z -10.4) |
| [[AN3 CA (line)]] | alt | 443 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.212× (z -12.0) |
| [[NCI-H661 (line)]] | alt | 478 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -14.5) |
| [[CHP-212 (line)]] | wt | 320 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.199× (z -12.6) |
| [[HS-578T (line)]] | alt | 253 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -11.7) |
| [[SW 1271 (line)]] | alt | 216 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -9.1) |
| [[NCI-H2122 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 237 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAF1]] | +0.76 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[CHASERR]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[WAC]] | +0.73 | +0.79 / +0.67 | both halves | 7e-06 | STRING 442 |
| [[ZNF362]] | +0.69 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[QKI]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TLK2]] | +0.65 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SIAH1]] | +0.65 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZBED5-AS1]] | +0.65 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[NCOA2]] | +0.63 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ANXA2R-AS1]] | +0.62 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[CYB561A3]] | +0.62 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[RBM33]] | +0.62 | +0.71 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAP3]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[STK4]] | -0.59 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[CAP1]] | -0.57 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[SIN3B]] | -0.57 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[LRRFIP1]] | -0.56 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[CUTC]] | -0.55 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[KCTD20]] | -0.55 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[GPR89B]] | -0.53 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[HMOX2]] | -0.53 | -0.32 / -0.51 | both halves | 1e-04 |  |
| [[EFL1]] | -0.53 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[PHC2]] | -0.52 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[MPP3]] | -0.52 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00649]] | B | LINC00649 activity raises DYRK1A's level | lines that do not express LINC00649 (25) vs lines expressing it (25) | 1.20× lower at baseline in the lines without LINC00649 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000287923, RMST, SERPINF1; maybe low, not absent |
| [[PLUT]] | B | PLUT activity raises DYRK1A's level | lines that do not express PLUT (23) vs lines expressing it (27) | 1.17× lower at baseline in the lines without PLUT | 0.067 | ⚠ within organs, on part of the lines; also absent: SHROOM3, MST1R, KCNK5; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREBBP]] | C | DYRK1A's natural level strengthens CREBBP's drug response | DYRK1A's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.18; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.7, 14.5); signed map (29.4, -23.7). **Vector** length 95.8, 48.7% of its response variance represented; |z| ≥ 3 in 1,425 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.1 | -0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +15.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.0 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | -9.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.5 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | -0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.9 | +0.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.8 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | +1.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -17.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.2 | -9.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -7.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | +3.0 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity tyrosine phosphorylation regulated kinase 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.13 — chr21:37,365,573-37,526,358 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DYRK1, DYRK, MNBH |
| Gene groups (HGNC) | Dual-specificity tyrosine-regulated kinase family |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 4 pathways, smallest: G0 and Early G1; Mitotic G1 phase and G1/S transition; Cell Cycle, Mitotic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13627](https://www.uniprot.org/uniprotkb/Q13627) (Dual specificity tyrosine-phosphorylation-regulated kinase 1A):

> Dual-specificity kinase which possesses both serine/threonine and tyrosine kinase activities. Exhibits a substrate preference for proline at position P+1 and arginine at position P-3. Plays an important role in double-strand breaks (DSBs) repair following DNA damage. Mechanistically, phosphorylates RNF169 and increases its ability to block accumulation of TP53BP1 at the DSB sites thereby promoting homologous recombination repair (HRR). Also acts as a positive regulator of transcription by …

**Summary**, from NCBI Gene [1859](https://www.ncbi.nlm.nih.gov/gene/1859):

> This gene encodes a member of the Dual-specificity tyrosine phosphorylation-regulated kinase (DYRK) family. This member contains a nuclear targeting signal sequence, a protein kinase domain, a leucine zipper motif, and a highly conservative 13-consecutive-histidine repeat. It catalyzes its autophosphorylation on serine/threonine and tyrosine residues. It may play a significant role in a signaling pathway regulating cell proliferation and may be involved in brain development. This gene is a …

**Accessions** — [HGNC:3091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3091) · Entrez [1859](https://www.ncbi.nlm.nih.gov/gene/1859) · UniProt [Q13627](https://www.uniprot.org/uniprotkb/Q13627) · Ensembl [ENSG00000157540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157540)

## Data

Gene col 8081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8081); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8081]; `tensor/DDL_lfc|DDL_z.npy` [8081]; `embed/gene_vectors.npy` [8081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8081 or target_col == 8081). Every well: [[DYRK1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYRK1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
