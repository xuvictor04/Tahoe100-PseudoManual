---
symbol: "STAG1"
type: "gene"
col: 3960
ensembl_id: "ENSG00000118007"
name: "STAG1 cohesin complex component"
location: "3q22.3"
module: 51
arm: "+"
pooled_cpm: 328.15
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 22
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# STAG1

*STAG1 cohesin complex component* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.80× (z +11.2, q 1e-26, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.375× (z -18.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD10]] (+0.73, fdr 7e-06), [[INO80]] (+0.72, fdr 7e-06), [[TCF12]] (+0.69, fdr 7e-06); moves opposite to [[UNC119]] (-0.60, fdr 2e-05), [[ANKRD37]] (-0.60, fdr 2e-05), [[TSNAX]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +11.2 | 1e-26 | 46/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +10.3 | 3e-22 | 48/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +9.6 | 2e-19 | 45/48 (SNU-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.38×** | +8.6 | 9e-16 | 44/49 (COLO 205, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +7.7 | 2e-12 | 30/48 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +7.3 | 3e-11 | 43/48 (SHP-77, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.4 | 6e-06 | 30/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.3 | 9e-06 | 33/47 (LoVo, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +5.2 | 1e-05 | 39/48 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.66×** | +5.0 | 3e-05 | 42/49 (LOX-IMVI, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.5 | 4e-04 | 29/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.018 | 25/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.025 | 32/50 (NCI-H2347, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.032 | 23/48 (C32, PANC-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.088 | 26/49 (NCI-H2347, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3960.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.375×** | -18.7 | 0e+00 | 48/48 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.391×** | -17.9 | 0e+00 | 48/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.393×** | -17.8 | 0e+00 | 48/48 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -12.5 | 2e-33 | 40/49 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.630×** | -8.8 | 1e-16 | 45/48 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.643×** | -8.4 | 3e-15 | 43/48 (CFPAC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.684×** | -7.0 | 2e-10 | 27/44 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.696×** | -6.9 | 3e-10 | 38/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.698×** | -6.9 | 4e-10 | 37/49 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.702×** | -6.8 | 8e-10 | 39/48 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.697×** | -6.6 | 2e-09 | 39/50 (HOP62, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.711×** | -6.3 | 2e-08 | 38/48 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.571×** | -5.6 | 9e-07 | 45/49 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -5.4 | 2e-06 | 34/48 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.821×** | -5.4 | 3e-06 | 24/48 (RKO, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -4.4 | 4e-04 | 20/48 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.823×** | -3.7 | 0.005 | 24/49 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.703×** | -3.5 | 0.011 | 30/48 (CFPAC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.838× | -3.4 | 0.016 | 20/48 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.852× | -3.1 | 0.050 | 18/49 (LS 180, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 397 | 6 (1 ⚠) | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -16.3) |
| [[HOP62 (line)]] | alt | 519 | 1 | 12 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 2.96× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.252× (z -20.7) |
| [[LoVo (line)]] | wt | 570 | 4 (1 ⚠) | 9 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.213× (z -25.0) |
| [[SW480 (line)]] | alt | 283 | 7 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.372× (z -16.1) |
| [[HEC-1-A (line)]] | alt | 761 | 2 | 10 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.321× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 382 | 0 | 11 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.302× (z -19.3) |
| [[LS 180 (line)]] | wt | 412 | 4 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.275× (z -19.5) |
| [[RKO (line)]] | wt | 469 | 2 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -17.5) |
| [[SW48 (line)]] | wt | 632 | 2 | 8 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.20× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.209× (z -19.9) |
| [[C32 (line)]] | wt | 208 | 6 (1 ⚠) | 3 | [[Digitoxin (drug)]] 0.5 µM 2.18× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.379× (z -13.5) |
| [[SHP-77 (line)]] | alt | 197 | 4 (1 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.91× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.411× (z -11.9) |
| [[H4 (line)]] | wt | 453 | 4 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.11× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.333× (z -13.0) |
| [[SNU-1 (line)]] | wt | 379 | 4 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.71× (z +12.2) | [[Belinostat (drug)]] 5 µM 0.335× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 270 | 1 | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.250× (z -18.8) |
| [[COLO 205 (line)]] | alt | 347 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +17.7) | [[Panobinostat (drug)]] 5 µM 0.266× (z -17.4) |
| [[HS-578T (line)]] | alt | 397 | 1 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.82× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -15.9) |
| [[NCI-H2030 (line)]] | alt | 327 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -17.1) |
| [[NCI-H2347 (line)]] | alt | 217 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.413× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 199 | 4 | 3 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.98× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.558× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 378 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.376× (z -13.2) |
| [[A-172 (line)]] | wt | 288 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 265 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 3.61× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.330× (z -14.6) |
| [[J82 (line)]] | alt | 323 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.410× (z -11.4) |
| [[KATO III (line)]] | alt | 384 | 2 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.350× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 192 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.272× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 380 | 1 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.311× (z -17.0) |
| [[SNU-423 (line)]] | alt | 392 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -17.0) |
| [[C-33 A (line)]] | alt | 322 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -11.0) |
| [[HCT15 (line)]] | alt | 327 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.351× (z -11.7) |
| [[HT-29 (line)]] | alt | 213 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 478 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -21.4) |
| [[NCI-H23 (line)]] | alt | 381 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.402× (z -12.4) |
| [[A498 (line)]] | wt | 178 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -13.2) |
| [[A549 (line)]] | wt | 178 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 272 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 441 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -15.6) |
| [[SW1417 (line)]] | alt | 272 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -13.5) |
| [[Hs 766T (line)]] | wt | 157 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.474× (z -9.0) |
| [[PANC-1 (line)]] | alt | 257 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -10.2) |
| [[SW 900 (line)]] | alt | 135 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -9.5) |
| [[A-427 (line)]] | wt | 378 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.475× (z -8.5) |
| [[BT-474 (line)]] | alt | 246 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 208 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.431× (z -9.0) |
| [[AN3 CA (line)]] | alt | 395 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 294 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD10]] | +0.73 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[INO80]] | +0.72 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[TCF12]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[ATF7IP]] | +0.67 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ZNF644]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PRH1]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PBRM1]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ZFX]] | +0.64 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ADNP]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CUX1]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.62 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[CEP112]] | +0.60 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC119]] | -0.60 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ANKRD37]] | -0.60 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[TSNAX]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ANKZF1]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.56 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SRP54-AS1]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MAX]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 | pathway: S Phase |
| [[TUBE1]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[INSIG2]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[WDR45B]] | -0.55 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[GPR160]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[NAPB]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises STAG1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.4, 13.0); signed map (12.9, -32.3). **Vector** length 128, 49.0% of its response variance represented; |z| ≥ 3 in 1,602 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +8.3 | +10.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.7 | +11.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +7.2 | +9.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.1 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.4 | +0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.4 | +1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +4.2 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +5.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.8 | -8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -8.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -4.3 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -5.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -3.7 | -0.3 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -3.3 | -0.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -3.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | STAG1 cohesin complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:136,336,236-136,752,403 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SA-1, SCC3A, SA1 |
| Gene groups (HGNC) | Cohesin complex; Armadillo like helical domain containing; STAG family |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 21 pathways, smallest: Cohesin Loading onto Chromatin; Establishment of Sister Chromatid Cohesion; Mitotic Telophase/Cytokinesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVM7](https://www.uniprot.org/uniprotkb/Q8WVM7) (Cohesin subunit SA-1):

> Component of cohesin complex, a complex required for the cohesion of sister chromatids after DNA replication. The cohesin complex apparently forms a large proteinaceous ring within which sister chromatids can be trapped. At anaphase, the complex is cleaved and dissociates from chromatin, allowing sister chromatids to segregate. The cohesin complex may also play a role in spindle pole assembly during mitosis.

**Summary**, from NCBI Gene [10274](https://www.ncbi.nlm.nih.gov/gene/10274):

> This gene is a member of the SCC3 family and is expressed in the nucleus. It encodes a component of cohesin, a multisubunit protein complex that provides sister chromatid cohesion along the length of a chromosome from DNA replication through prophase and prometaphase, after which it is dissociated in preparation for segregation during anaphase. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11354) · Entrez [10274](https://www.ncbi.nlm.nih.gov/gene/10274) · UniProt [Q8WVM7](https://www.uniprot.org/uniprotkb/Q8WVM7) · Ensembl [ENSG00000118007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118007)

## Data

Gene col 3960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3960); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3960]; `tensor/DDL_lfc|DDL_z.npy` [3960]; `embed/gene_vectors.npy` [3960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3960 or target_col == 3960). Every well: [[STAG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
