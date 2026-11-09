---
symbol: "ZFR"
type: "gene"
col: 634
ensembl_id: "ENSG00000056097"
name: "zinc finger RNA binding protein"
location: "5p13.3"
module: 46
arm: "+"
pooled_cpm: 249.4
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ZFR

*zinc finger RNA binding protein* — 5p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +25.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.508× (z -18.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPF40A]] (+0.69, fdr 7e-06), [[FAM204A]] (+0.67, fdr 7e-06), [[CCAR1]] (+0.67, fdr 1e-05); moves opposite to [[TMEM104]] (-0.60, fdr 1e-05), [[EHD4]] (-0.59, fdr 1e-04), [[SLC35B2]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CTXN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +25.0 | 0e+00 | 47/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +19.3 | 0e+00 | 47/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +15.1 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +14.7 | 0e+00 | 46/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +13.0 | 1e-36 | 48/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +12.5 | 1e-33 | 44/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +12.2 | 3e-32 | 45/49 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +12.1 | 8e-32 | 45/48 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +10.2 | 2e-22 | 38/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +9.4 | 4e-19 | 43/48 (LS 180, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +8.5 | 7e-16 | 34/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +8.5 | 7e-16 | 37/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +7.6 | 1e-12 | 33/48 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +6.7 | 1e-09 | 35/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +6.2 | 2e-08 | 30/47 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.20×** | +5.1 | 1e-05 | 25/48 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.6 | 1e-04 | 4/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.508×** | -18.8 | 0e+00 | 48/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.530×** | -17.6 | 0e+00 | 46/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.601×** | -14.1 | 1e-42 | 47/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.774×** | -7.1 | 2e-10 | 39/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -6.3 | 4e-08 | 20/48 (SW480, A498, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.777×** | -5.0 | 6e-05 | 31/48 (A-427, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -4.6 | 4e-04 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | 0.858× | -4.1 | 0.003 | 22/47 (RKO, NCI-H2347, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.759×** | -4.0 | 0.004 | 25/45 (hTERT-HPNE, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.867× | -4.0 | 0.004 | 14/48 (RPMI-7951, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.867× | -3.9 | 0.004 | 16/48 (SW1417, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 255 | 13 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +25.5) | [[Panobinostat (drug)]] 5 µM 0.468× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 236 | 11 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +17.9) | [[Panobinostat (drug)]] 5 µM 0.458× (z -14.8) |
| [[LoVo (line)]] | wt | 221 | 11 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +17.1) | [[Panobinostat (drug)]] 5 µM 0.530× (z -11.7) |
| [[BT-474 (line)]] | alt | 309 | 8 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +19.3) | [[Panobinostat (drug)]] 0.5 µM 0.464× (z -13.6) |
| [[KATO III (line)]] | alt | 171 | 9 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +21.3) | [[Panobinostat (drug)]] 0.5 µM 0.561× (z -9.9) |
| [[SW480 (line)]] | alt | 283 | 8 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.476× (z -16.1) |
| [[LOX-IMVI (line)]] | wt | 233 | 7 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.474× (z -11.9) |
| [[H4 (line)]] | wt | 247 | 8 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +18.5) | [[Panobinostat (drug)]] 5 µM 0.469× (z -10.0) |
| [[HOP62 (line)]] | alt | 263 | 6 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.400× (z -14.8) |
| [[LS 180 (line)]] | wt | 193 | 7 | 2 | [[PH-797804 (drug)]] 5 µM 3.80× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.500× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 332 | 6 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.13× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.388× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 234 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +14.3) | — |
| [[A-427 (line)]] | wt | 269 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.521× (z -12.5) |
| [[A498 (line)]] | wt | 233 | 6 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.511× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 202 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +18.2) | [[Panobinostat (drug)]] 5 µM 0.470× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 216 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.452× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 322 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +18.6) | [[Panobinostat (drug)]] 5 µM 0.478× (z -11.8) |
| [[A549 (line)]] | wt | 262 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -17.5) |
| [[AsPC-1 (line)]] | alt | 214 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.402× (z -13.2) |
| [[SHP-77 (line)]] | alt | 293 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.505× (z -12.0) |
| [[SNU-423 (line)]] | alt | 232 | 3 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.04× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.508× (z -10.5) |
| [[SW 900 (line)]] | alt | 301 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.443× (z -11.3) |
| [[SW1417 (line)]] | alt | 264 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.451× (z -14.1) |
| [[SW48 (line)]] | wt | 243 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.449× (z -11.1) |
| [[A-172 (line)]] | wt | 253 | 3 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 1.93× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.469× (z -14.6) |
| [[COLO 205 (line)]] | alt | 143 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.6) | — |
| [[Hs 766T (line)]] | wt | 257 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.517× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 333 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.431× (z -16.2) |
| [[RKO (line)]] | wt | 203 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +23.0) | [[Panobinostat (drug)]] 0.5 µM 0.562× (z -8.9) |
| [[C-33 A (line)]] | alt | 216 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 254 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.1) | [[Panobinostat (drug)]] 0.5 µM 0.470× (z -9.7) |
| [[HS-578T (line)]] | alt | 259 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.511× (z -9.1) |
| [[HT-29 (line)]] | alt | 200 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +19.4) | — |
| [[J82 (line)]] | alt | 334 | 2 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 1.82× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.475× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 359 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.530× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 263 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.445× (z -13.4) |
| [[SNU-1 (line)]] | wt | 237 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.7) | — |
| [[CFPAC-1 (line)]] | alt | 201 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.13× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.522× (z -10.8) |
| [[C32 (line)]] | wt | 182 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 1.89× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.532× (z -8.5) |
| [[HCT15 (line)]] | alt | 246 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.5) | — |
| [[CHP-212 (line)]] | wt | 237 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 192 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.521× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 188 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 137 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 333 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 397 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 269 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF40A]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[FAM204A]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CCAR1]] | +0.67 | +0.54 / +0.53 | both halves | 1e-05 | same gene group |
| [[PAIP1]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[FAIM]] | +0.66 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[CCDC122]] | +0.65 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[THOC7]] | +0.65 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[MRPL45]] | +0.64 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[IDNK]] | +0.63 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[RAB21]] | +0.63 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[UBXN2A]] | +0.63 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[TDP2]] | +0.62 | +0.63 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM104]] | -0.60 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[EHD4]] | -0.59 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[SLC35B2]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 | same gene group |
| [[MAPKAPK2]] | -0.58 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[ATG101]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[TXNDC17]] | -0.57 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[RHPN1]] | -0.56 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[SLC66A2]] | -0.55 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[DUSP5]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[MATCAP1]] | -0.55 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[RCOR1]] | -0.54 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[YIF1B]] | -0.54 | -0.39 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTXN1]] | B | CTXN1 activity raises ZFR's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without CTXN1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises ZFR's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HTATIP2]] | B | HTATIP2 activity lowers ZFR's level | lines that do not express HTATIP2 (7) vs lines expressing it (43) | 1.11× higher at baseline in the lines without HTATIP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: C3orf52, TBILA, ITPR3; its own permutation p |
| [[RDX]] | C | RDX activity raises ZFR's level | lines that do not express RDX (4) vs lines expressing it (46) | 1.42× lower at baseline in the lines without RDX | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SOGA1, CITED2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.0, 8.0); signed map (9.8, -31.8). **Vector** length 112, 41.7% of its response variance represented; |z| ≥ 3 in 1,465 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +19.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +12.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.0 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.9 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.7 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +8.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.0 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +13.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.0 | -1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +0.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.7 | -17.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.7 | -18.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.1 | -14.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.4 | +6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.9 | -1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger RNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3 — chr5:32,354,350-32,444,740 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZFR1, SPG71 |
| Gene groups (HGNC) | Zinc fingers matrin-type; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KR1](https://www.uniprot.org/uniprotkb/Q96KR1) (Zinc finger RNA-binding protein):

> Involved in postimplantation and gastrulation stages of development. Involved in the nucleocytoplasmic shuttling of STAU2. Binds to DNA and RNA (By similarity).

**Summary**, from NCBI Gene [51663](https://www.ncbi.nlm.nih.gov/gene/51663):

> This gene encodes an RNA-binding protein characterized by its DZF (domain associated with zinc fingers) domain. The encoded protein may play a role in the nucleocytoplasmic shuttling of another RNA-binding protein, Staufen homolog 2, in neurons. Expression of this gene is regulated through alternative polyadenylation that mediates differential microRNA targeting. Elevated expression of this gene has been observed in human patients with pancreatic cancer and knockdown of this gene may result in …

**Accessions** — [HGNC:17277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17277) · Entrez [51663](https://www.ncbi.nlm.nih.gov/gene/51663) · UniProt [Q96KR1](https://www.uniprot.org/uniprotkb/Q96KR1) · Ensembl [ENSG00000056097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000056097)

## Data

Gene col 634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 634); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 634]; `tensor/DDL_lfc|DDL_z.npy` [634]; `embed/gene_vectors.npy` [634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 634 or target_col == 634). Every well: [[ZFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
