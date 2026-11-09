---
symbol: "MCL1"
type: "gene"
col: 6732
ensembl_id: "ENSG00000143384"
name: "MCL1 apoptosis regulator, BCL2 family member"
location: "1q21.2"
module: 109
arm: "+"
pooled_cpm: 397.04
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 39
n_dd_up_clean: 15
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# MCL1

*MCL1 apoptosis regulator, BCL2 family member* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +23.3, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (7 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.447× (z -12.9, q 1e-35, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR1]] (+0.82, fdr 7e-06), [[ERCC1]] (+0.80, fdr 7e-06), [[ADAMTSL4-AS2]] (+0.77, fdr 7e-06, ⚠ read-through risk), [[EGR3]] (+0.74, fdr 7e-06); moves opposite to [[HSF2]] (-0.62, fdr 1e-05), [[SNX4]] (-0.61, fdr 1e-05), [[FHIP2A]] (-0.59, fdr 8e-06).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MARCHF3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +23.3 | 0e+00 | 44/48 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.09×** | +11.9 | 4e-30 | 43/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +11.5 | 2e-28 | 40/48 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +10.9 | 1e-25 | 43/48 (A-172, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +8.6 | 9e-16 | 38/48 (A-427, HEC-1-A, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +6.5 | 7e-09 | 33/48 (SNU-1, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +5.9 | 3e-07 | 30/45 (A-427, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 4e-06 | 32/48 (BT-474, SNU-1, …) | two highest doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.0 | 4e-05 | 35/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.5 | 4e-04 | 30/47 (A-172, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +4.1 | 0.002 | 26/48 (BT-474, SNU-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.28×** | +3.9 | 0.004 | 24/48 (SNU-1, BT-474, …) | two highest doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.005 | 29/48 (HT-29, SW48, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.007 | 26/49 (A-172, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.013 | 26/48 (A-427, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +3.5 | 0.016 | 24/49 (Hs 766T, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.021 | 26/48 (hTERT-HPNE, LoVo, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.046 | 23/48 (Hs 766T, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.076 | 18/47 (A-427, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 11 with an alert ⚠; shown: the 15 strongest. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6732.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.447×** | -12.9 | 1e-35 | 45/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.536×** | -12.5 | 1e-33 | 45/48 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.512×** | -11.2 | 1e-26 | 45/49 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.505×** | -11.0 | 6e-26 | 46/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.503×** | -10.6 | 3e-24 | 46/48 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.509×** | -10.6 | 4e-24 | 43/48 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.479×** | -10.4 | 3e-23 | 46/50 (NCI-H23, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.651×** | -10.0 | 1e-21 | 44/48 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.573×** | -9.3 | 8e-19 | 43/47 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.685×** | -7.9 | 2e-13 | 43/48 (NCI-H460, SHP-77, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.611×** | -7.2 | 3e-11 | 43/49 (NCI-H460, NCI-H23, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.729×** | -7.1 | 6e-11 | 35/49 (NCI-H460, SHP-77, …) | all doses, flat | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.751×** | -6.7 | 7e-10 | 32/48 (RKO, C32, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.648×** | -6.6 | 2e-09 | 41/48 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.686×** | -6.3 | 1e-08 | 31/48 (HepG2/C3A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 872 | 0 | 21 (7 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.258× (z -18.0) |
| [[C32 (line)]] | wt | 318 | 4 | 12 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +28.7) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.216× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 895 | 3 | 13 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +18.0) | [[Cobimetinib (drug)]] 5 µM 0.173× (z -17.4) |
| [[A549 (line)]] | wt | 647 | 0 | 15 (3 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.205× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 617 | 6 (1 ⚠) | 9 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +21.0) | [[Trametinib (drug)]] 0.5 µM 0.359× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 982 | 2 | 13 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.88× (z +9.7) | [[Cobimetinib (drug)]] 5 µM 0.139× (z -17.5) |
| [[HOP62 (line)]] | alt | 513 | 1 | 13 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +18.7) | [[Cobimetinib (drug)]] 5 µM 0.219× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 252 | 5 (1 ⚠) | 9 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +19.5) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.360× (z -11.1) |
| [[SW480 (line)]] | alt | 193 | 7 (3 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +22.6) | [[Trametinib (drug)]] 0.5 µM 0.446× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 415 | 2 (1 ⚠) | 10 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.62× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.318× (z -12.1) |
| [[SHP-77 (line)]] | alt | 606 | 0 | 12 | — | [[Trametinib (drug)]] 0.5 µM 0.231× (z -13.8) |
| [[SNU-1 (line)]] | wt | 156 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +24.1) | — |
| [[BT-474 (line)]] | alt | 589 | 7 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 723 | 2 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +15.9) | [[Adagrasib (drug)]] 0.05 µM 0.549× (z -17.7) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.261× (z -11.1) |
| [[PANC-1 (line)]] | alt | 417 | 0 | 9 | — | [[Cobimetinib (drug)]] 5 µM 0.247× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 255 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +23.7) | [[Adagrasib (drug)]] 0.05 µM 0.546× (z -18.3) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.370× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 343 | 1 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +17.5) | [[Adagrasib (drug)]] 0.05 µM 0.651× (z -12.8) ⚠ position not correctable · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.262× (z -10.4) |
| [[RKO (line)]] | wt | 498 | 0 | 8 | — | [[Radotinib (drug)]] 5 µM 0.396× (z -13.6) |
| [[A-172 (line)]] | wt | 318 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +19.5) | — |
| [[A-427 (line)]] | wt | 205 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +15.4) | [[Cobimetinib (drug)]] 5 µM 0.449× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 437 | 1 | 6 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.2) | [[Cobimetinib (drug)]] 5 µM 0.282× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 350 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -10.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 524 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.8) | [[Cobimetinib (drug)]] 5 µM 0.342× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 167 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +28.4) | — |
| [[SW 900 (line)]] | alt | 298 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +21.2) | — |
| [[SW48 (line)]] | wt | 264 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.1) | [[Trametinib (drug)]] 0.5 µM 0.415× (z -10.5) |
| [[HS-578T (line)]] | alt | 174 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +17.9) | [[Ponatinib (drug)]] 5 µM 0.407× (z -9.5) |
| [[LoVo (line)]] | wt | 205 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.387× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 259 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +22.9) | — |
| [[A498 (line)]] | wt | 186 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +17.6) | — |
| [[RPMI-7951 (line)]] | alt | 299 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +18.1) | — |
| [[HCT15 (line)]] | alt | 537 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.1) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.334× (z -9.4) |
| [[J82 (line)]] | alt | 281 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.0) | [[Ponatinib (drug)]] 5 µM 0.407× (z -9.8) |
| [[C-33 A (line)]] | alt | 195 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.7) | — |
| [[H4 (line)]] | wt | 306 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.407× (z -8.5) ⚠ toxic · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.408× (z -8.5) |
| [[Hs 766T (line)]] | wt | 412 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +22.2) | — |
| [[HT-29 (line)]] | alt | 351 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 403 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.8) | [[Cobimetinib (drug)]] 5 µM 0.385× (z -8.6) |
| [[SNU-423 (line)]] | alt | 296 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +20.5) | [[Ponatinib (drug)]] 5 µM 0.381× (z -9.5) |
| [[AN3 CA (line)]] | alt | 171 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +15.5) | — |
| [[COLO 205 (line)]] | alt | 279 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.2) | — |
| [[KATO III (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.407× (z -8.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 236 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 203 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +15.0) | — |
| [[CHP-212 (line)]] | wt | 291 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 566 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 445 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 344 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR1]] | +0.82 | +0.85 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 414 |
| [[ERCC1]] | +0.80 | +0.82 / +0.78 | both halves | 7e-06 |  |
| [[ADAMTSL4-AS2]] | +0.77 | +0.75 / +0.77 | both halves | 7e-06 | ⚠ **readthrough risk**: ADAMTSL4-AS2 lies 3.2 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[EGR3]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[EGR2]] | +0.73 | +0.72 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[LINC00941]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[MAFF]] | +0.70 | +0.75 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IER2]] | +0.70 | +0.73 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DUSP6]] | +0.69 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[ERRFI1-DT]] | +0.68 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SPRY2]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSF2]] | -0.62 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[SNX4]] | -0.61 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[FHIP2A]] | -0.59 | -0.59 / -0.57 | both halves | 8e-06 |  |
| [[NPEPPS]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[KIF13A]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[FBXO7]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCHF3]] | B | MARCHF3 activity raises MCL1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without MARCHF3 | 0.016 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[TRIB1]] | B | TRIB1 activity raises MCL1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 1.90× lower at baseline in the lines without TRIB1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[ELL2]] | B | ELL2 activity raises MCL1's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without ELL2 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[CD163L1]] | B | CD163L1 activity raises MCL1's level | lines that do not express CD163L1 (24) vs lines expressing it (26) | 1.60× lower at baseline in the lines without CD163L1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, ENSG00000230647, CNRIP1; maybe low, not absent |
| [[DNAH17]] | B | DNAH17 activity raises MCL1's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without DNAH17 | 0.091 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[KIFC3]] | C | KIFC3 activity raises MCL1's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.9, -0.2); signed map (5.8, 30.1). **Vector** length 165, 65.0% of its response variance represented; |z| ≥ 3 in 1,929 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.63 to 9); *NGF-stimulated transcription* (reactome, mean cos +0.63 to 9); *Nuclear Events (kinase and transcription factor activation)* (reactome, mean cos +0.63 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +23.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.2 | +11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.8 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +0.7 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -10.3 | -12.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -10.2 | -10.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -10.2 | -11.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -10.0 | -11.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -9.9 | -12.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -9.6 | -10.6 |

## What is on record

|  |  |
|---|---|
| Name | MCL1 apoptosis regulator, BCL2 family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,560,895-150,579,738 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCL2L3, Mcl-1 |
| Gene groups (HGNC) | BCL2 family |
| Hallmark sets | APOPTOSIS, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 6 pathways, smallest: Interleukin-4 and Interleukin-13 signaling; Signaling by ALK fusions and activated point mutants; Signaling by ALK in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07820](https://www.uniprot.org/uniprotkb/Q07820) (Induced myeloid leukemia cell differentiation protein Mcl-1):

> Involved in the regulation of apoptosis versus cell survival, and in the maintenance of viability but not of proliferation. Mediates its effects by interactions with a number of other regulators of apoptosis. Isoform 1 inhibits apoptosis. Isoform 2 promotes apoptosis.

**Summary**, from NCBI Gene [4170](https://www.ncbi.nlm.nih.gov/gene/4170):

> This gene encodes an anti-apoptotic protein, which is a member of the Bcl-2 family. Alternative splicing results in multiple transcript variants. The longest gene product (isoform 1) enhances cell survival by inhibiting apoptosis while the alternatively spliced shorter gene products (isoform 2 and isoform 3) promote apoptosis and are death-inducing. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:6943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6943) · Entrez [4170](https://www.ncbi.nlm.nih.gov/gene/4170) · UniProt [Q07820](https://www.uniprot.org/uniprotkb/Q07820) · Ensembl [ENSG00000143384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143384)

## Data

Gene col 6732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6732); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6732]; `tensor/DDL_lfc|DDL_z.npy` [6732]; `embed/gene_vectors.npy` [6732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6732 or target_col == 6732). Every well: [[MCL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
