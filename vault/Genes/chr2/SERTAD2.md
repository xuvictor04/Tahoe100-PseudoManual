---
symbol: "SERTAD2"
type: "gene"
col: 11059
ensembl_id: "ENSG00000179833"
name: "SERTA domain containing 2"
location: "2p14"
module: 123
arm: "+"
pooled_cpm: 119.46
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 8
n_dd_up_clean: 27
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# SERTAD2

*SERTA domain containing 2* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.11× (z +38.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.442× (z -15.0, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 0.742× (z -5.7, q 2e-06, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF9]] (+0.59, fdr 1e-05), [[LMNA]] (+0.59, fdr 7e-06), [[CAVIN1]] (+0.58, fdr 7e-06); moves opposite to [[IPO11]] (-0.51, fdr 2e-05), [[DROSHA]] (-0.51, fdr 1e-05), [[XPO4]] (-0.50, fdr 2e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[JUP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.11×** | +38.1 | 0e+00 | 46/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **7.38×** | +19.9 | 0e+00 | 49/49 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.83×** | +19.0 | 0e+00 | 44/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.55×** | +17.8 | 0e+00 | 45/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +14.3 | 4e-44 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +13.5 | 2e-39 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +13.5 | 2e-39 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.02×** | +13.3 | 1e-38 | 43/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +12.7 | 6e-35 | 45/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +11.9 | 1e-30 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.04×** | +11.1 | 1e-26 | 39/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +9.8 | 4e-21 | 44/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +9.1 | 3e-18 | 36/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +8.7 | 9e-17 | 29/49 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.29×** | +8.3 | 6e-15 | 41/49 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +7.9 | 9e-14 | 37/49 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11059.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.442×** | -15.0 | 0e+00 | 40/44 (Hs 766T, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.514×** | -12.7 | 1e-34 | 38/49 (A-427, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.742×** | -5.7 | 2e-06 | 33/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.631×** | -4.6 | 5e-04 | 30/49 (Hs 766T, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.731×** | -4.3 | 0.002 | 29/48 (LoVo, A-427, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.814×** | -4.0 | 0.007 | 24/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.826×** | -3.7 | 0.018 | 22/48 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.829×** | -3.6 | 0.021 | 21/49 (LS 180, A498, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.880× | -3.5 | 0.028 | 10/48 (HOP62, A-172, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.3 | 0.063 | 17/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.893× | -3.1 | 0.094 | 11/48 (NCI-H1573, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 102 | 16 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +21.5) | — |
| [[NCI-H1573 (line)]] | alt | 182 | 9 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +30.3) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.481× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 127 | 10 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +29.6) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -13.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 74.2 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +25.7) | — |
| [[SW480 (line)]] | alt | 63.9 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +18.9) | — |
| [[A549 (line)]] | wt | 103 | 10 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +30.2) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -9.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 367 | 10 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +23.8) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 94.0 | 10 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -16.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 84.0 | 10 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +32.0) | [[Dinaciclib (drug)]] 0.5 µM 0.516× (z -9.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 130 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +18.2) | — |
| [[HS-578T (line)]] | alt | 100 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +35.8) | — |
| [[A498 (line)]] | wt | 110 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +36.5) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 39.2 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.69× (z +24.3) | — |
| [[NCI-H1792 (line)]] | alt | 246 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +29.5) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -18.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 69.3 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +29.0) | — |
| [[LOX-IMVI (line)]] | wt | 95.1 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 141 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +22.0) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 105 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +23.2) | — |
| [[HEC-1-A (line)]] | alt | 74.6 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +18.4) | — |
| [[KATO III (line)]] | alt | 85.7 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 132 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -17.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 88.9 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -14.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 82.7 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +33.5) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -10.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 286 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -18.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 68.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +27.5) | — |
| [[NCI-H2030 (line)]] | alt | 101 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.4× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 142 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -14.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 151 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +24.2) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -14.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 70.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +27.2) | — |
| [[NCI-H23 (line)]] | alt | 75.7 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +25.3) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -12.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 74.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +26.7) | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -17.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 199 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -10.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 170 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.32× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -11.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 73.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +25.3) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 171 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.40× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -19.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 202 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 11.3× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 42.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +14.7) | — |
| [[C-33 A (line)]] | alt | 209 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -14.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 198 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -17.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 53.3 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.23× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 84.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 143 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +11.1) | [[Clobetasol propionate (drug)]] 5 µM 0.121× (z -8.8) |
| [[CHP-212 (line)]] | wt | 134 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +8.9) | — |
| [[H4 (line)]] | wt | 98.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +17.6) | — |
| [[NCI-H661 (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 109 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.101× (z -10.7) |
| [[AN3 CA (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF9]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[LMNA]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CAVIN1]] | +0.58 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[DUSP14]] | +0.58 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[KCTD11]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TUBB2A]] | +0.55 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[PLEKHG3]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RNF223]] | +0.54 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[KDM5B]] | +0.54 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[GPRC5A]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[NR1D1]] | +0.54 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TSC22D2]] | +0.53 | +0.42 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO11]] | -0.51 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[DROSHA]] | -0.51 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[XPO4]] | -0.50 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[RPUSD4]] | -0.50 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[CDKAL1]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PDS5A]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TRRAP]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[NCBP3]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[COX10]] | -0.47 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[HEATR1]] | -0.46 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[MCM3AP]] | -0.46 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[CDK5RAP2]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | JUP activity raises SERTAD2's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without JUP | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.8, 8.0); signed map (3.2, 23.3). **Vector** length 118, 41.3% of its response variance represented; |z| ≥ 3 in 1,785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.2 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.7 | +7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.7 | +9.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.7 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.2 | +8.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.2 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +4.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | +0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.0 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -5.4 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | -1.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.2 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.8 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | SERTA domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:64,631,621-64,751,005 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRIP-Br2, KIAA0127, Sei-2 |
| Gene groups (HGNC) | SERTA domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14140](https://www.uniprot.org/uniprotkb/Q14140) (SERTA domain-containing protein 2):

> Acts at E2F-responsive promoters as coregulator to integrate signals provided by PHD- and/or bromodomain-containing transcription factors. May act as coactivator as well as corepressor of E2F1-TFDP1 and E2F4-TFDP1 complexes on E2F consensus binding sites, which would activate or inhibit E2F-target genes expression. Modulates fat storage by down-regulating the expression of key genes involved in adipocyte lipolysis, thermogenesis and oxidative metabolism.

**Summary**, from NCBI Gene [9792](https://www.ncbi.nlm.nih.gov/gene/9792):

> Predicted to enable transcription coactivator activity. Acts upstream of or within negative regulation of cell growth. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30784) · Entrez [9792](https://www.ncbi.nlm.nih.gov/gene/9792) · UniProt [Q14140](https://www.uniprot.org/uniprotkb/Q14140) · Ensembl [ENSG00000179833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179833)

## Data

Gene col 11059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11059); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11059]; `tensor/DDL_lfc|DDL_z.npy` [11059]; `embed/gene_vectors.npy` [11059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11059 or target_col == 11059). Every well: [[SERTAD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERTAD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
