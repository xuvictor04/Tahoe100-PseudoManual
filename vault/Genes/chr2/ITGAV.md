---
symbol: "ITGAV"
type: "gene"
col: 6179
ensembl_id: "ENSG00000138448"
name: "integrin subunit alpha V"
location: "2q32.1"
module: 197
arm: "+"
pooled_cpm: 230.08
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# ITGAV

*integrin subunit alpha V* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.34× (z +29.4, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.598× (z -12.6, q 1e-33, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL5]] (+0.72, fdr 7e-06), [[ALCAM]] (+0.63, fdr 7e-06), [[ARHGEF12]] (+0.62, fdr 1e-05); moves opposite to [[EEF1AKMT4]] (-0.63, fdr 1e-05), [[POP7]] (-0.59, fdr 5e-05), [[MPG]] (-0.57, fdr 9e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +29.4 | 0e+00 | 41/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +12.8 | 3e-35 | 40/48 (NCI-H1573, SNU-1, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +10.6 | 3e-24 | 38/49 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +10.0 | 4e-21 | 32/48 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +9.1 | 7e-18 | 29/44 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +7.7 | 1e-12 | 32/48 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +7.0 | 2e-10 | 34/45 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +6.3 | 3e-08 | 33/49 (RKO, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +6.0 | 1e-07 | 26/47 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.5 | 2e-06 | 30/48 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +5.5 | 2e-06 | 20/48 (RKO, CFPAC-1, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.8 | 6e-05 | 1/50 (HOP62) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +4.5 | 3e-04 | 24/48 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.5 | 3e-04 | 23/48 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.018 | 12/47 (SK-MEL-2, RKO, …) | two highest doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.031 | 22/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.09× | +3.1 | 0.063 | 7/48 (PANC-1, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.598×** | -12.6 | 1e-33 | 40/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.612×** | -12.0 | 6e-31 | 40/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.705×** | -8.6 | 2e-15 | 35/48 (HepG2/C3A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -8.3 | 2e-14 | 24/49 (NCI-H1792, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -7.9 | 3e-13 | 38/48 (HT-29, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.734×** | -7.3 | 3e-11 | 29/47 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.791×** | -5.7 | 7e-07 | 25/48 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.807×** | -5.3 | 1e-05 | 27/48 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.730×** | -4.0 | 0.003 | 22/48 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.853× | -3.9 | 0.005 | 21/48 (HepG2/C3A, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Terfenadine (drug)]] 5 µM |  | 0.895× | -3.9 | 0.006 | 9/48 (Hs 766T, RPMI-7951, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.855× | -3.8 | 0.006 | 21/48 (NCI-H1792, AN3 CA, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.865× | -3.6 | 0.016 | 18/48 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.877× | -3.2 | 0.052 | 19/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.840× | -3.1 | 0.084 | 13/48 (A498, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.879× | -3.0 | 0.087 | 17/49 (hTERT-HPNE, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 267 | 7 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +32.3) | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -13.0) |
| [[A498 (line)]] | wt | 567 | 6 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +24.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.566× (z -10.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.592× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 194 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +33.6) | — |
| [[KATO III (line)]] | alt | 130 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +27.2) | [[Panobinostat (drug)]] 5 µM 0.285× (z -16.6) |
| [[A549 (line)]] | wt | 250 | 5 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +24.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -9.1) |
| [[LoVo (line)]] | wt | 137 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +23.1) | [[Panobinostat (drug)]] 5 µM 0.495× (z -11.2) |
| [[SHP-77 (line)]] | alt | 223 | 1 | 5 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.66× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.311× (z -15.1) |
| [[HepG2_C3A (line)]] | wt | 820 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -19.9) |
| [[HOP62 (line)]] | alt | 236 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +20.3) | — |
| [[Hs 766T (line)]] | wt | 229 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +25.9) | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -15.1) |
| [[RKO (line)]] | wt | 140 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +17.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.466× (z -9.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.511× (z -8.9) |
| [[SNU-1 (line)]] | wt | 155 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +33.7) | — |
| [[SW1417 (line)]] | alt | 161 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +21.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -9.0) |
| [[CHP-212 (line)]] | wt | 254 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 105 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +36.7) | — |
| [[NCI-H1792 (line)]] | alt | 375 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -19.6) |
| [[Panc 03.27 (line)]] | alt | 220 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +25.0) | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -11.3) |
| [[SW 900 (line)]] | alt | 261 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +18.0) | [[Panobinostat (drug)]] 0.5 µM 0.555× (z -8.5) |
| [[SW480 (line)]] | alt | 117 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.336× (z -18.2) |
| [[A-172 (line)]] | wt | 200 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +23.3) | — |
| [[AN3 CA (line)]] | alt | 483 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -15.1) |
| [[C32 (line)]] | wt | 155 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +16.2) | — |
| [[COLO 205 (line)]] | alt | 87.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +22.2) | — |
| [[HS-578T (line)]] | alt | 233 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 145 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.485× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 174 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +22.9) | — |
| [[NCI-H23 (line)]] | alt | 137 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 2.10× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 252 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +21.5) | — |
| [[NCI-H460 (line)]] | wt | 175 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 410 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 213 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +36.9) | — |
| [[BT-474 (line)]] | alt | 118 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +26.6) | — |
| [[J82 (line)]] | alt | 210 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.518× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 242 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 166 | 1 | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.14× (z +9.1) | [[5-Azacytidine (drug)]] 5 µM 0.486× (z -8.7) |
| [[SNU-423 (line)]] | alt | 194 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +21.5) | — |
| [[C-33 A (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 211 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 268 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.7) | — |
| [[NCI-H596 (line)]] | alt | 192 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.0643× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 313 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.1) | — |
| [[SW 1271 (line)]] | alt | 238 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.4) | — |
| [[SW48 (line)]] | wt | 94.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1,448 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 373 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL5]] | +0.72 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[ALCAM]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 539 |
| [[ARHGEF12]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MBNL1]] | +0.60 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[NID1]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 | pathway: Extracellular matrix organization; STRING 568 |
| [[TIA1]] | +0.57 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[CFL2]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[NCOA4]] | +0.56 | +0.47 / +0.61 | both halves | 2e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[CCDC50]] | +0.56 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[IL6ST]] | +0.56 | +0.39 / +0.59 | both halves | 6e-05 | same gene group |
| [[ACADM]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[SEPTIN11]] | +0.56 | +0.46 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1AKMT4]] | -0.63 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[POP7]] | -0.59 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[MPG]] | -0.57 | -0.36 / -0.61 | both halves | 9e-05 |  |
| [[ZNF749]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[MRPS26]] | -0.56 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[DNAJC5]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[THOC3]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.56 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[QPCTL]] | -0.55 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[C16orf91]] | -0.55 | -0.22 / -0.56 | both halves | 6e-04 |  |
| [[MRPS12]] | -0.55 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[ANKS3]] | -0.55 | -0.38 / -0.59 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.4, 15.4); signed map (47.2, 18.4). **Vector** length 142, 44.8% of its response variance represented; |z| ≥ 3 in 1,456 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +11.3 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.4 | +29.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +5.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.9 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +0.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.3 | +1.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -7.1 | -12.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.5 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha V |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:186,590,010-186,680,901 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD51; previously VNRA, MSK8, VTNR |
| Gene groups (HGNC) | CD molecules; Integrin alpha subunits |
| Hallmark sets | ANGIOGENESIS, ANDROGEN_RESPONSE, IL2_STAT5_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 32 pathways, smallest: Cross-presentation of particulate exogenous antigens (phagosomes); PECAM1 interactions; Mechanical load activates signaling by PIEZO1 and integrins in osteocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [P06756](https://www.uniprot.org/uniprotkb/P06756) (Integrin alpha-V):

> The alpha-V (ITGAV) integrins are receptors for vitronectin, cytotactin, fibronectin, fibrinogen, laminin, matrix metalloproteinase-2, osteopontin, osteomodulin, prothrombin, thrombospondin and vWF. They recognize the sequence R-G-D in a wide array of ligands. ITGAV:ITGB3 binds to fractalkine (CX3CL1) and may act as its coreceptor in CX3CR1-dependent fractalkine signaling. ITGAV:ITGB3 binds to NRG1 (via EGF domain) and this binding is essential for NRG1-ERBB signaling. ITGAV:ITGB3 binds to FGF1 …

**Summary**, from NCBI Gene [3685](https://www.ncbi.nlm.nih.gov/gene/3685):

> The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha V subunit. This subunit associates with beta 1, beta 3, beta 5, beta 6 and beta 8 subunits. The heterodimer consisting of alpha V and beta 3 subunits is also …

**Accessions** — [HGNC:6150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6150) · Entrez [3685](https://www.ncbi.nlm.nih.gov/gene/3685) · UniProt [P06756](https://www.uniprot.org/uniprotkb/P06756) · Ensembl [ENSG00000138448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138448)

## Data

Gene col 6179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6179); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6179]; `tensor/DDL_lfc|DDL_z.npy` [6179]; `embed/gene_vectors.npy` [6179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6179 or target_col == 6179). Every well: [[ITGAV — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGAV.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
