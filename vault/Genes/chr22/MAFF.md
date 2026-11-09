---
symbol: "MAFF"
type: "gene"
col: 11611
ensembl_id: "ENSG00000185022"
name: "MAF bZIP transcription factor F"
location: "22q13.1"
module: 109
arm: "+"
pooled_cpm: 63.39
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 30
n_dd_up_clean: 19
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# MAFF

*MAF bZIP transcription factor F* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.94× (z +29.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.480× (z -8.6, q 3e-15, down in 39 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.497× (z -7.9, q 7e-13, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCL1]] (+0.70, fdr 7e-06), [[KDSR]] (+0.67, fdr 1e-05), [[PPP1R15A]] (+0.67, fdr 7e-06); moves opposite to [[EEF1AKMT2]] (-0.57, fdr 2e-05), [[KDM1A]] (-0.53, fdr 3e-05), [[ATP5F1C]] (-0.53, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.94×** | +29.6 | 0e+00 | 47/48 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.71×** | +17.5 | 0e+00 | 45/48 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.28×** | +13.9 | 1e-41 | 45/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.89×** | +12.5 | 2e-33 | 47/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +11.3 | 2e-27 | 47/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.47×** | +10.6 | 4e-24 | 39/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.26×** | +9.6 | 9e-20 | 41/48 (AN3 CA, SNU-1, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.17×** | +9.1 | 7e-18 | 43/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.60×** | +8.8 | 7e-17 | 44/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.99×** | +8.0 | 5e-14 | 42/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +7.6 | 2e-12 | 38/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.58×** | +5.5 | 2e-06 | 33/48 (NCI-H2030, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +4.5 | 4e-04 | 31/48 (SNU-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.45×** | +4.3 | 7e-04 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.8 | 0.005 | 31/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.007 | 24/49 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.010 | 27/49 (SK-MEL-2, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.010 | 29/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11611.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.480×** | -8.6 | 3e-15 | 39/48 (LoVo, HEC-1-A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.497×** | -7.9 | 7e-13 | 42/47 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.527×** | -7.3 | 5e-11 | 43/50 (SW480, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.571×** | -6.6 | 5e-09 | 31/48 (hTERT-HPNE, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.670×** | -6.6 | 5e-09 | 43/48 (SW480, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.573×** | -6.6 | 5e-09 | 41/48 (hTERT-HPNE, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.574×** | -6.5 | 5e-09 | 40/48 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.592×** | -6.2 | 5e-08 | 38/47 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.662×** | -5.9 | 2e-07 | 38/48 (SW480, NCI-H2347, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.592×** | -5.9 | 2e-07 | 37/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.369×** | -5.8 | 4e-07 | 41/48 (SHP-77, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.613×** | -5.8 | 4e-07 | 38/48 (HT-29, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.608×** | -5.4 | 3e-06 | 41/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.394×** | -5.4 | 3e-06 | 42/48 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.643×** | -5.2 | 8e-06 | 39/48 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.424×** | -5.0 | 2e-05 | 35/49 (SK-MEL-2, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.3 | 7 (1 ⚠) | 11 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +14.5) | [[Cobimetinib (drug)]] 5 µM 0.219× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 31.3 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +22.2) | — |
| [[SNU-1 (line)]] | wt | 85.5 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +15.7) | — |
| [[NCI-H1573 (line)]] | alt | 101 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +25.0) | [[Cobimetinib (drug)]] 5 µM 0.374× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 53.4 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +19.5) | [[Binimetinib (drug)]] 0.5 µM 0.374× (z -10.9) |
| [[C32 (line)]] | wt | 82.5 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +24.9) | [[Cobimetinib (drug)]] 0.5 µM 0.235× (z -8.9) |
| [[KATO III (line)]] | alt | 95.0 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +16.6) | [[Ponatinib (drug)]] 5 µM 0.322× (z -10.4) |
| [[PANC-1 (line)]] | alt | 33.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +25.4) | — |
| [[HEC-1-A (line)]] | alt | 63.2 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +19.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.300× (z -10.6) ⚠ unreliable plate only · without an alert: [[Trametinib (drug)]] 5 µM 0.366× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 152 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +22.0) | — |
| [[A-172 (line)]] | wt | 42.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +23.7) | — |
| [[A-427 (line)]] | wt | 38.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +14.4) | — |
| [[A549 (line)]] | wt | 40.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +26.5) | — |
| [[AsPC-1 (line)]] | alt | 104 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +26.7) | — |
| [[HS-578T (line)]] | alt | 82.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +22.4) | — |
| [[hTERT-HPNE (line)]] | wt | 59.7 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +21.0) | [[Belinostat (drug)]] 5 µM 0.229× (z -10.0) |
| [[LoVo (line)]] | wt | 62.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +17.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -10.8) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 42.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +20.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +20.2) | — |
| [[NCI-H23 (line)]] | alt | 62.5 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +16.9) | [[Cobimetinib (drug)]] 5 µM 0.143× (z -14.0) |
| [[A498 (line)]] | wt | 66.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +24.2) | — |
| [[AN3 CA (line)]] | alt | 83.2 | 4 | 0 | [[Auranofin (drug)]] 5 µM 13.0× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 45.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +15.0) | — |
| [[Hs 766T (line)]] | wt | 96.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +22.5) | — |
| [[LS 180 (line)]] | wt | 39.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +16.7) | — |
| [[RPMI-7951 (line)]] | alt | 61.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.69× (z +16.8) | — |
| [[SNU-423 (line)]] | alt | 69.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +26.9) | — |
| [[SW 900 (line)]] | alt | 51.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +19.2) | — |
| [[SW48 (line)]] | wt | 54.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +15.7) | — |
| [[HOP62 (line)]] | alt | 74.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +19.4) | — |
| [[NCI-H2030 (line)]] | alt | 74.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +18.2) | — |
| [[Panc 03.27 (line)]] | alt | 68.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +19.0) | — |
| [[CFPAC-1 (line)]] | alt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +24.0) | — |
| [[H4 (line)]] | wt | 61.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +20.5) | — |
| [[HepG2_C3A (line)]] | wt | 91.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 85.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +15.2) | [[Belinostat (drug)]] 5 µM 0.372× (z -8.5) |
| [[J82 (line)]] | alt | 55.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +20.2) | — |
| [[NCI-H1792 (line)]] | alt | 52.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +15.4) | — |
| [[SW 1088 (line)]] | alt | 70.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +11.4) | [[Sonidegib (drug)]] 0.05 µM 0.0612× (z -9.1) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 57.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +16.7) | — |
| [[C-33 A (line)]] | alt | 49.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.97× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 57.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +13.3) | — |
| [[HCT15 (line)]] | alt | 67.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.34× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 79.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 49.1 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0437× (z -10.0) |
| [[CHP-212 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCL1]] | +0.70 | +0.75 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KDSR]] | +0.67 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[PPP1R15A]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 418 |
| [[BTBD19]] | +0.61 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[SERTAD1]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MED29]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PIK3IP1-DT]] | +0.59 | +0.40 / +0.60 | both halves | 4e-05 |  |
| [[ZSWIM4]] | +0.59 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[FOSB]] | +0.59 | +0.67 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 575 |
| [[KDM6B]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TUT7]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ERCC1]] | +0.59 | +0.71 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1AKMT2]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[KDM1A]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 | pathway: Factors involved in megakaryocyte development and platelet production |
| [[ATP5F1C]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[SNRNP40]] | -0.52 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PRDX3]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ADPGK]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ANAPC10]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SKP2]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[RPA1]] | -0.51 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[BCL9]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[INTS10]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[FAR1]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MAFF's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 4.8% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises MAFF's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without ZNF341-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.7, -4.0); signed map (14.9, -2.9). **Vector** length 109, 40.3% of its response variance represented; |z| ≥ 3 in 1,621 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.51 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +29.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +13.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.5 | -8.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.2 | -5.4 |
|  | [[EX229 (drug)]] 5 µM |  | -7.7 | -3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.3 | -5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.1 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | MAF bZIP transcription factor F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,200,767-38,216,507 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hMafF |
| Gene groups (HGNC) | Small MAF bZIP transcription factor family |
| Hallmark sets | COAGULATION, COMPLEMENT, IL2_STAT5_SIGNALING, HYPOXIA, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULX9](https://www.uniprot.org/uniprotkb/Q9ULX9) (Transcription factor MafF):

> Since they lack a putative transactivation domain, the small Mafs behave as transcriptional repressors when they dimerize among themselves. However, they seem to serve as transcriptional activators by dimerizing with other (usually larger) basic-zipper proteins, such as NFE2L1/NRF1, and recruiting them to specific DNA-binding sites. Interacts with the upstream promoter region of the oxytocin receptor gene. May be a transcriptional enhancer in the up-regulation of the oxytocin receptor gene at …

**Summary**, from NCBI Gene [23764](https://www.ncbi.nlm.nih.gov/gene/23764):

> The protein encoded by this gene is a basic leucine zipper (bZIP) transcription factor that lacks a transactivation domain. It is known to bind the US-2 DNA element in the promoter of the oxytocin receptor (OTR) gene and most likely heterodimerizes with other leucine zipper-containing proteins to enhance expression of the OTR gene during term pregnancy. The encoded protein can also form homodimers, and since it lacks a transactivation domain, the homodimer may act as a repressor of …

**Accessions** — [HGNC:6780](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6780) · Entrez [23764](https://www.ncbi.nlm.nih.gov/gene/23764) · UniProt [Q9ULX9](https://www.uniprot.org/uniprotkb/Q9ULX9) · Ensembl [ENSG00000185022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185022)

## Data

Gene col 11611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11611); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11611]; `tensor/DDL_lfc|DDL_z.npy` [11611]; `embed/gene_vectors.npy` [11611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11611 or target_col == 11611). Every well: [[MAFF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAFF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
