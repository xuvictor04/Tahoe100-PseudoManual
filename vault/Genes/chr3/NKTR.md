---
symbol: "NKTR"
type: "gene"
col: 3596
ensembl_id: "ENSG00000114857"
name: "natural killer cell triggering receptor"
location: "3p22.1"
module: 41
arm: "+"
pooled_cpm: 287.27
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# NKTR

*natural killer cell triggering receptor* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.25× (z +7.8, q 3e-12, up in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.29× (z +6.5, q 2e-08, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.651× (z -10.9, q 7e-25, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP48]] (+0.71, fdr 7e-06), [[PRKRA]] (+0.66, fdr 1e-05), [[TTC3]] (+0.66, fdr 7e-06); moves opposite to [[KRT8P12]] (-0.62, fdr 4e-05), [[RBM12B]] (-0.62, fdr 1e-05), [[AP5B1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.25×** | +7.8 | 3e-12 | 25/48 (SW480, HEC-1-A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +7.3 | 1e-10 | 29/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +6.5 | 2e-08 | 29/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +6.3 | 5e-08 | 27/48 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +5.0 | 5e-05 | 25/48 (C-33 A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.22×** | +5.0 | 5e-05 | 25/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.22×** | +5.0 | 5e-05 | 25/48 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.15× | +3.7 | 0.018 | 19/48 (C-33 A, A-427, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.15× | +3.5 | 0.027 | 17/47 (C-33 A, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.14× | +3.3 | 0.061 | 21/48 (HEC-1-A, C-33 A, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.2 | 0.075 | 16/49 (SNU-423, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3596.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.651×** | -10.9 | 7e-25 | 41/48 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -8.4 | 1e-14 | 0/50 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.715×** | -7.9 | 7e-13 | 39/48 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.777×** | -6.4 | 2e-08 | 28/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.774×** | -6.0 | 2e-07 | 31/48 (A498, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -5.8 | 5e-07 | 18/48 (A-172, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.863× | -5.2 | 2e-05 | 16/48 (NCI-H1573, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.840× | -4.1 | 0.003 | 22/47 (C32, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.856× | -3.6 | 0.018 | 17/48 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.766×** | -3.5 | 0.023 | 21/49 (NCI-H2347, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.906× | -3.5 | 0.024 | 16/49 (A549, LoVo, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.875× | -3.1 | 0.082 | 9/49 (LS 180, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 396 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +16.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.57× (z +9.4) | [[Auranofin (drug)]] 5 µM 0.566× (z -11.8) |
| [[A-427 (line)]] | wt | 264 | 5 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.578× (z -9.8) |
| [[C-33 A (line)]] | alt | 366 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 404 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.444× (z -10.8) |
| [[A-172 (line)]] | wt | 338 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.402× (z -18.3) |
| [[HS-578T (line)]] | alt | 375 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.501× (z -12.2) |
| [[LS 180 (line)]] | wt | 316 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 234 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.95× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 253 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +11.4) | — |
| [[SW1417 (line)]] | alt | 413 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.78× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 446 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +15.0) ⚠ cell-cycle shift, explains ~28% of this change | [[Auranofin (drug)]] 5 µM 0.610× (z -10.2) |
| [[HT-29 (line)]] | alt | 187 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.01× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 119 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.59× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | [[Selinexor (drug)]] 5 µM 0.631× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 227 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +13.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +10.3) | — |
| [[A498 (line)]] | wt | 222 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.501× (z -12.6) |
| [[LoVo (line)]] | wt | 363 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.70× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.648× (z -10.2) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H2347 (line)]] | alt | 328 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.623× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 359 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Auranofin (drug)]] 5 µM 0.376× (z -16.9) |
| [[A549 (line)]] | wt | 245 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -13.7) ⚠ cell-cycle shift, explains ~12% of this change |
| [[BT-474 (line)]] | alt | 165 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 233 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.452× (z -10.4) |
| [[COLO 205 (line)]] | alt | 184 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 385 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.476× (z -12.7) |
| [[KATO III (line)]] | alt | 204 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 231 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.436× (z -11.7) |
| [[RKO (line)]] | wt | 271 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 387 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.493× (z -10.9) |
| [[SHP-77 (line)]] | alt | 328 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SNU-423 (line)]] | alt | 308 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.436× (z -13.5) |
| [[SW 1271 (line)]] | alt | 541 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.350× (z -8.6) ⚠ transcription drop |
| [[SW 900 (line)]] | alt | 324 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.501× (z -9.9) |
| [[AN3 CA (line)]] | alt | 326 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 273 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 238 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 404 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 241 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 242 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 279 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 215 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 309 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 335 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP48]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PRKRA]] | +0.66 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[TTC3]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SEPTIN2]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ARL3]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ANAPC5]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SLC17A5]] | +0.61 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[MINDY2]] | +0.61 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[SEC63]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[SEC22A]] | +0.58 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[FAM193B]] | +0.57 | +0.70 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT8P12]] | -0.62 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[RBM12B]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[AP5B1]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[MOCS3]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ZNF300]] | -0.58 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H4]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ZNF629]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CENPBD1P]] | -0.57 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[TOR1A]] | -0.56 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[PPP2CA]] | -0.55 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SMG8]] | -0.55 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[C7orf25]] | -0.55 | -0.52 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers NKTR's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.433). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (2.4, -12.9); signed map (-41.1, 10.2). **Vector** length 144, 48.7% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.8 | +2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.6 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +5.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.4 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -12.4 | -10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -9.2 | -5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -8.0 | -5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.9 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.6 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.6 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | natural killer cell triggering receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:42,600,655-42,648,735 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p104, CypNK |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases |
| Matched by | ensembl_id |

**Function**, from UniProt [P30414](https://www.uniprot.org/uniprotkb/P30414) (NK-tumor recognition protein):

> PPIase that catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and may therefore assist protein folding. Component of a putative tumor-recognition complex involved in the function of NK cells.

**Summary**, from NCBI Gene [4820](https://www.ncbi.nlm.nih.gov/gene/4820):

> This gene encodes a membrane-anchored protein with a hydrophobic amino terminal domain and a cyclophilin-like PPIase domain. It is present on the surface of natural killer cells and facilitates their binding to targets. Its expression is regulated by IL2 activation of the cells. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7833) · Entrez [4820](https://www.ncbi.nlm.nih.gov/gene/4820) · UniProt [P30414](https://www.uniprot.org/uniprotkb/P30414) · Ensembl [ENSG00000114857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114857)

## Data

Gene col 3596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3596); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3596]; `tensor/DDL_lfc|DDL_z.npy` [3596]; `embed/gene_vectors.npy` [3596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3596 or target_col == 3596). Every well: [[NKTR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKTR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
