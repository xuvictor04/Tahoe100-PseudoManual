---
symbol: "GLG1"
type: "gene"
col: 1640
ensembl_id: "ENSG00000090863"
name: "golgi glycoprotein 1"
location: "16q23.1"
module: 42
arm: "+"
pooled_cpm: 331.16
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# GLG1

*golgi glycoprotein 1* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.28× (z +7.1, q 5e-10, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.484× (z -29.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90B1]] (+0.73, fdr 7e-06), [[ATRN]] (+0.71, fdr 1e-05), [[PDIA4]] (+0.71, fdr 7e-06); moves opposite to [[SLC9A8]] (-0.66, fdr 7e-06), [[CDC42EP1]] (-0.65, fdr 1e-05), [[NANOS3]] (-0.64, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +7.1 | 5e-10 | 31/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +6.3 | 1e-07 | 30/49 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +5.1 | 6e-05 | 36/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +4.8 | 2e-04 | 23/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.17× | +4.4 | 0.001 | 21/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | 1.15× | +4.0 | 0.005 | 20/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.15× | +3.9 | 0.008 | 16/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.5 | 0.028 | 17/48 (PANC-1, A498, …) | all doses, flat |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.10 | 2/48 (hTERT-HPNE, SW 1088) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.13 | 13/49 (A498, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1640.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.484×** | -29.2 | 0e+00 | 47/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.501×** | -19.7 | 0e+00 | 48/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -16.9 | 0e+00 | 46/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.649×** | -11.9 | 3e-30 | 46/47 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.666×** | -10.7 | 1e-24 | 35/45 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.709×** | -9.8 | 1e-20 | 42/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.720×** | -9.3 | 8e-19 | 39/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.762×** | -7.7 | 7e-13 | 28/49 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.758×** | -7.6 | 2e-12 | 30/44 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.843× | -6.9 | 3e-10 | 24/49 (C32, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.791×** | -6.7 | 1e-09 | 36/48 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.851× | -6.5 | 5e-09 | 18/48 (C32, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.864× | -5.9 | 2e-07 | 14/48 (SNU-1, hTERT-HPNE, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.855× | -4.1 | 0.002 | 20/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.873× | -3.9 | 0.004 | 22/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.868× | -3.9 | 0.004 | 19/48 (HOP62, J82, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.792×** | -3.5 | 0.016 | 26/49 (SK-MEL-2, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.794×** | -3.4 | 0.017 | 23/48 (Hs 766T, A498, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.891× | -3.3 | 0.027 | 7/48 (A549, MIA PaCa-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.894× | -3.2 | 0.037 | 4/48 (hTERT-HPNE, LS 180, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.855× | -3.2 | 0.037 | 16/48 (CFPAC-1, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 449 | 1 | 11 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 2.79× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -29.5) |
| [[HOP62 (line)]] | alt | 471 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -42.2) |
| [[hTERT-HPNE (line)]] | wt | 369 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.420× (z -14.1) |
| [[SW480 (line)]] | alt | 547 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -18.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 363 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.634× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 274 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -26.5) |
| [[NCI-H460 (line)]] | wt | 216 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -31.1) |
| [[A-172 (line)]] | wt | 364 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -36.3) |
| [[AsPC-1 (line)]] | alt | 335 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -22.8) |
| [[HS-578T (line)]] | alt | 348 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -24.4) |
| [[J82 (line)]] | alt | 217 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -26.0) |
| [[LoVo (line)]] | wt | 375 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -19.6) |
| [[NCI-H2347 (line)]] | alt | 203 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -16.6) |
| [[SW 900 (line)]] | alt | 308 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -13.4) |
| [[A-427 (line)]] | wt | 236 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -19.8) |
| [[A498 (line)]] | wt | 393 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.508× (z -13.4) |
| [[A549 (line)]] | wt | 284 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -15.1) |
| [[H4 (line)]] | wt | 426 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -24.3) |
| [[HCT15 (line)]] | alt | 420 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -16.7) |
| [[Hs 766T (line)]] | wt | 368 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -25.2) |
| [[KATO III (line)]] | alt | 362 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 419 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -21.9) |
| [[NCI-H1792 (line)]] | alt | 386 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -29.9) |
| [[NCI-H23 (line)]] | alt | 277 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -23.9) |
| [[PANC-1 (line)]] | alt | 211 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -25.6) |
| [[RPMI-7951 (line)]] | alt | 305 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -29.4) |
| [[SK-MEL-2 (line)]] | alt | 255 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -22.2) |
| [[SW1417 (line)]] | alt | 313 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.555× (z -11.5) ⚠ toxic |
| [[SW48 (line)]] | wt | 410 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.16× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.476× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.629× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 382 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -20.4) |
| [[HT-29 (line)]] | alt | 316 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.613× (z -9.7) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 597 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -27.2) |
| [[SNU-1 (line)]] | wt | 290 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.497× (z -9.8) |
| [[SNU-423 (line)]] | alt | 265 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -32.8) |
| [[AN3 CA (line)]] | alt | 327 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -15.6) |
| [[C-33 A (line)]] | alt | 304 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 268 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -24.6) |
| [[HEC-1-A (line)]] | alt | 303 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.625× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 233 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 206 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.240× (z -13.3) ⚠ toxic |
| [[RKO (line)]] | wt | 361 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.608× (z -11.2) |
| [[SW 1088 (line)]] | alt | 512 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.8) |
| [[BT-474 (line)]] | alt | 219 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 253 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -9.6) |
| [[SW 1271 (line)]] | alt | 326 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.350× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 383 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 264 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90B1]] | +0.73 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[ATRN]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[PDIA4]] | +0.71 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.70 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[SBNO1]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[MLEC]] | +0.69 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[NBAS]] | +0.68 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[AKR7A2]] | +0.68 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[P3H1]] | +0.68 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[PDIA6]] | +0.67 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[P4HB]] | +0.67 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[TMED4]] | +0.66 | +0.77 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A8]] | -0.66 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[CDC42EP1]] | -0.65 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[NANOS3]] | -0.64 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | -0.64 | -0.73 / -0.43 | both halves | 3e-05 |  |
| [[ZC3H4]] | -0.63 | -0.67 / -0.40 | both halves | 5e-05 |  |
| [[PATL2]] | -0.63 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[ZNF620]] | -0.63 | -0.72 / -0.47 | both halves | 2e-05 |  |
| [[LACC1]] | -0.63 | -0.67 / -0.46 | both halves | 3e-05 |  |
| [[BCDIN3D]] | -0.62 | -0.68 / -0.40 | both halves | 5e-05 |  |
| [[NEPRO-AS1]] | -0.61 | -0.71 / -0.36 | both halves | 9e-05 |  |
| [[TRIM47]] | -0.61 | -0.71 / -0.45 | both halves | 3e-05 |  |
| [[KCNMB3]] | -0.60 | -0.64 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.0, -14.0); signed map (-54.3, 5.9). **Vector** length 137, 48.3% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.58 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.52 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.51 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.2 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +0.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +0.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.5 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -13.5 | -19.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -12.7 | -29.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -11.3 | -16.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.8 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.2 | -9.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.7 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | golgi glycoprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:74,447,427-74,607,144 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MG-160, ESL-1, CFR-1 |
| Reactome | 2 pathways, smallest: Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92896](https://www.uniprot.org/uniprotkb/Q92896) (Golgi apparatus protein 1):

> Binds fibroblast growth factor and E-selectin (cell-adhesion lectin on endothelial cells mediating the binding of neutrophils).

**Summary**, from NCBI Gene [2734](https://www.ncbi.nlm.nih.gov/gene/2734):

> Predicted to enable fibroblast growth factor binding activity. Predicted to act upstream of or within several processes, including negative regulation of protein processing; negative regulation of transforming growth factor beta receptor signaling pathway; and regulation of chondrocyte differentiation. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4316) · Entrez [2734](https://www.ncbi.nlm.nih.gov/gene/2734) · UniProt [Q92896](https://www.uniprot.org/uniprotkb/Q92896) · Ensembl [ENSG00000090863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090863)

## Data

Gene col 1640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1640); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1640]; `tensor/DDL_lfc|DDL_z.npy` [1640]; `embed/gene_vectors.npy` [1640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1640 or target_col == 1640). Every well: [[GLG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
