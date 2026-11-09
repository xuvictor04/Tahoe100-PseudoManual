---
symbol: "RSRC2"
type: "gene"
col: 3187
ensembl_id: "ENSG00000111011"
name: "arginine and serine rich coiled-coil 2"
location: "12q24.31"
module: 12
arm: "+"
pooled_cpm: 265.57
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# RSRC2

*arginine and serine rich coiled-coil 2* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.12× (z +33.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.650× (z -6.1, q 7e-07, down in 33 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.670× (z -5.9, q 1e-06, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNW1]] (+0.71, fdr 7e-06), [[GPBP1]] (+0.69, fdr 7e-06), [[PPP1R15A]] (+0.68, fdr 7e-06); moves opposite to [[SLC25A39]] (-0.64, fdr 1e-05), [[TCF3]] (-0.63, fdr 1e-05), [[ARF3]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.12×** | +33.6 | 0e+00 | 48/48 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.07×** | +20.4 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.62×** | +18.0 | 0e+00 | 48/48 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.78×** | +14.8 | 0e+00 | 48/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +13.3 | 4e-38 | 48/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.47×** | +13.2 | 1e-37 | 47/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.36×** | +11.2 | 4e-27 | 49/49 (COLO 205, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.88×** | +9.1 | 4e-18 | 46/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.88×** | +9.1 | 4e-18 | 46/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.97×** | +8.3 | 7e-15 | 46/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +8.2 | 2e-14 | 38/48 (LoVo, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +7.5 | 3e-12 | 47/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +6.8 | 5e-10 | 36/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.59×** | +6.4 | 5e-09 | 40/47 (COLO 205, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +6.2 | 2e-08 | 42/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +4.4 | 4e-04 | 41/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 9e-04 | 42/49 (KATO III, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.007 | 28/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.099 | 26/49 (NCI-H1573, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3187.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.650×** | -6.1 | 7e-07 | 33/44 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.670×** | -5.9 | 1e-06 | 45/48 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.684×** | -5.6 | 5e-06 | 40/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.757×** | -4.1 | 0.006 | 35/48 (HepG2/C3A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.791×** | -3.4 | 0.064 | 27/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.795×** | -3.4 | 0.070 | 34/48 (SW 900, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | 0.660× | -3.2 | 0.12 | 30/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 259 | 17 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +32.9) | — |
| [[LoVo (line)]] | wt | 313 | 14 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +34.8) | — |
| [[SW480 (line)]] | alt | 267 | 14 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +28.4) | — |
| [[KATO III (line)]] | alt | 195 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +32.7) | — |
| [[BT-474 (line)]] | alt | 285 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +22.1) | — |
| [[LOX-IMVI (line)]] | wt | 342 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +31.6) | — |
| [[SNU-1 (line)]] | wt | 288 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +21.5) | — |
| [[NCI-H23 (line)]] | alt | 287 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +28.2) | — |
| [[SW 900 (line)]] | alt | 322 | 9 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +27.5) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -10.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 261 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +28.2) | — |
| [[A549 (line)]] | wt | 234 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +31.9) | — |
| [[AsPC-1 (line)]] | alt | 321 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +38.0) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -10.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 203 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +20.1) | — |
| [[HEC-1-A (line)]] | alt | 245 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +26.1) | — |
| [[NCI-H1573 (line)]] | alt | 176 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +29.1) | — |
| [[NCI-H1792 (line)]] | alt | 241 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +30.3) | — |
| [[NCI-H2347 (line)]] | alt | 419 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +26.2) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -17.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 246 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +36.1) | — |
| [[A-427 (line)]] | wt | 220 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +17.7) | — |
| [[COLO 205 (line)]] | alt | 279 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +39.5) | — |
| [[HOP62 (line)]] | alt | 228 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +26.5) | — |
| [[HT-29 (line)]] | alt | 250 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +33.0) | — |
| [[LS 180 (line)]] | wt | 259 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +24.6) | — |
| [[SW48 (line)]] | wt | 292 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +20.8) | — |
| [[C32 (line)]] | wt | 214 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +28.2) | — |
| [[HepG2_C3A (line)]] | wt | 312 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +25.6) | [[Panobinostat (drug)]] 5 µM 0.507× (z -8.7) |
| [[Hs 766T (line)]] | wt | 170 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +27.8) | — |
| [[RKO (line)]] | wt | 308 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +19.1) | — |
| [[SHP-77 (line)]] | alt | 292 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.9) | — |
| [[SK-MEL-2 (line)]] | alt | 177 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +30.0) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 221 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +27.1) | — |
| [[C-33 A (line)]] | alt | 272 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +15.1) | — |
| [[HCT15 (line)]] | alt | 368 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +18.7) | — |
| [[HS-578T (line)]] | alt | 206 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +27.2) | — |
| [[hTERT-HPNE (line)]] | wt | 231 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +30.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 280 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +20.0) | — |
| [[NCI-H2030 (line)]] | alt | 318 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +20.8) | [[Dinaciclib (drug)]] 0.05 µM 0.374× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 277 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +29.7) | — |
| [[CFPAC-1 (line)]] | alt | 321 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +25.9) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 280 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +24.2) | — |
| [[Panc 03.27 (line)]] | alt | 201 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +24.3) | — |
| [[SNU-423 (line)]] | alt | 244 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +27.7) | — |
| [[RPMI-7951 (line)]] | alt | 250 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +23.2) | — |
| [[AN3 CA (line)]] | alt | 265 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.6) | — |
| [[CHP-212 (line)]] | wt | 307 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.2) | — |
| [[SW 1088 (line)]] | alt | 209 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +12.9) | — |
| [[SW 1271 (line)]] | alt | 370 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +12.7) | — |
| [[NCI-H2122 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 333 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNW1]] | +0.71 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GPBP1]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 | STRING 465 |
| [[PPP1R15A]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[RBM39]] | +0.68 | +0.78 / +0.47 | both halves | 2e-05 | STRING 613 |
| [[YTHDC1]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 | STRING 608 |
| [[CCDC174]] | +0.66 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[BRD2]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PPCS]] | +0.65 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[IFRD1]] | +0.63 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[DHX36]] | +0.63 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[PRRC2C]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[C1orf131]] | +0.62 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A39]] | -0.64 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TCF3]] | -0.63 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ARF3]] | -0.63 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[CHID1]] | -0.61 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[DCAF16]] | -0.61 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[AKT1]] | -0.61 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[MAPK1]] | -0.58 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[QSOX2]] | -0.57 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[NOMO2]] | -0.57 | -0.24 / -0.62 | both halves | 5e-04 |  |
| [[NOMO3]] | -0.57 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[APMAP]] | -0.57 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[NIPA2]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RSRC2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (25.7, -30.0); signed map (6.7, -9.6). **Vector** length 92.7, 42.5% of its response variance represented; |z| ≥ 3 in 1,360 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.7 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +13.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.6 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.9 | -0.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.8 | +9.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.4 | +14.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | +0.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | +1.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.2 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | +1.1 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | arginine and serine rich coiled-coil 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,503,454-122,527,000 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11021 |
| Matched by | ensembl_id |

UniProt [Q7L4I2](https://www.uniprot.org/uniprotkb/Q7L4I2) carries no function annotation.

**Summary**, from NCBI Gene [65117](https://www.ncbi.nlm.nih.gov/gene/65117):

> Enables RNA binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30559) · Entrez [65117](https://www.ncbi.nlm.nih.gov/gene/65117) · UniProt [Q7L4I2](https://www.uniprot.org/uniprotkb/Q7L4I2) · Ensembl [ENSG00000111011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111011)

## Data

Gene col 3187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3187); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3187]; `tensor/DDL_lfc|DDL_z.npy` [3187]; `embed/gene_vectors.npy` [3187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3187 or target_col == 3187). Every well: [[RSRC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSRC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
