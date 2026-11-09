---
symbol: "ANKIB1"
type: "gene"
col: 14
ensembl_id: "ENSG00000001629"
name: "ankyrin repeat and IBR domain containing 1"
location: "7q21.2"
module: 40
arm: "+"
pooled_cpm: 326.22
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ANKIB1

*ankyrin repeat and IBR domain containing 1* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.21× (z +5.5, q 2e-05, up in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change.
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.489× (z -30.7, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS6KC1]] (+0.58, fdr 1e-05), [[SCAMP1]] (+0.57, fdr 2e-05), [[DYM]] (+0.54, fdr 1e-05); moves opposite to [[SRSF6]] (-0.53, fdr 4e-05), [[PLEKHG2]] (-0.53, fdr 3e-05), [[HNRNPL]] (-0.52, fdr 7e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.21×** | +5.5 | 2e-05 | 24/47 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +4.5 | 0.001 | 13/47 (NCI-H2030, HCT15, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +4.5 | 0.001 | 15/47 (NCI-H1573, SW48, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.12× | +3.3 | 0.16 | 2/49 (A-427, SNU-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.489×** | -30.7 | 0e+00 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.515×** | -19.3 | 0e+00 | 46/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -15.4 | 0e+00 | 38/49 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.583×** | -14.4 | 4e-45 | 42/45 (SK-MEL-2, NCI-H23, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.616×** | -14.1 | 4e-43 | 41/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.655×** | -12.8 | 2e-35 | 40/49 (A-427, A498, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.677×** | -11.8 | 3e-30 | 36/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.670×** | -11.7 | 1e-29 | 32/44 (SK-MEL-2, NCI-H460, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.686×** | -11.4 | 3e-28 | 32/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.695×** | -11.0 | 2e-26 | 36/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.712×** | -10.3 | 4e-23 | 34/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.732×** | -9.4 | 2e-19 | 30/48 (NCI-H1573, BT-474, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.760×** | -8.3 | 5e-15 | 35/48 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.772×** | -7.8 | 3e-13 | 33/48 (SW480, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.791×** | -7.1 | 6e-11 | 30/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -6.5 | 3e-09 | 20/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.880× | -3.8 | 0.003 | 17/48 (RPMI-7951, MIA PaCa-2, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.866× | -3.8 | 0.003 | 16/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.888× | -3.6 | 0.007 | 5/48 (A-172, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.888× | -3.6 | 0.007 | 12/49 (A-172, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.890× | -3.5 | 0.009 | 17/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.875× | -2.9 | 0.074 | 13/48 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.5 µM |  | 0.910× | -2.8 | 0.075 | 1/48 (SW48) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.905× | -2.8 | 0.075 | 8/47 (BT-474, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 542 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -25.7) |
| [[NCI-H1792 (line)]] | alt | 397 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -29.9) |
| [[NCI-H460 (line)]] | wt | 247 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -24.8) |
| [[HOP62 (line)]] | alt | 271 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -26.8) |
| [[HS-578T (line)]] | alt | 385 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -21.9) |
| [[A549 (line)]] | wt | 325 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -27.2) |
| [[MIA PaCa-2 (line)]] | alt | 455 | 0 | 10 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.264× (z -20.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.325× (z -18.2) |
| [[SNU-423 (line)]] | alt | 365 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -25.2) |
| [[A498 (line)]] | wt | 497 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -31.6) |
| [[BT-474 (line)]] | alt | 205 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -19.9) |
| [[NCI-H1573 (line)]] | alt | 217 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -21.2) |
| [[PANC-1 (line)]] | alt | 326 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -33.1) |
| [[SK-MEL-2 (line)]] | alt | 422 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -21.0) |
| [[SW 900 (line)]] | alt | 355 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -15.0) |
| [[C32 (line)]] | wt | 442 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -17.4) |
| [[H4 (line)]] | wt | 526 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -16.5) |
| [[hTERT-HPNE (line)]] | wt | 299 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.324× (z -16.3) |
| [[J82 (line)]] | alt | 277 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -24.1) |
| [[KATO III (line)]] | alt | 306 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.379× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.611× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 406 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -23.7) |
| [[SW1417 (line)]] | alt | 270 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -18.0) |
| [[SW480 (line)]] | alt | 334 | 0 | 7 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.435× (z -19.7) |
| [[A-427 (line)]] | wt | 280 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.451× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 455 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -15.7) |
| [[Hs 766T (line)]] | wt | 389 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -20.6) |
| [[NCI-H23 (line)]] | alt | 358 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.411× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.618× (z -14.6) |
| [[NCI-H2347 (line)]] | alt | 345 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 314 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -21.0) |
| [[HEC-1-A (line)]] | alt | 271 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 155 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -21.6) |
| [[Panc 03.27 (line)]] | alt | 329 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -14.6) |
| [[RKO (line)]] | wt | 419 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.355× (z -16.9) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.454× (z -12.9) |
| [[SW48 (line)]] | wt | 337 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.486× (z -13.4) |
| [[LoVo (line)]] | wt | 348 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.603× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 217 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -16.6) |
| [[AN3 CA (line)]] | alt | 358 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -16.3) |
| [[LS 180 (line)]] | wt | 244 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.483× (z -12.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.566× (z -9.3) |
| [[HCT15 (line)]] | alt | 310 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 165 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -14.5) |
| [[HT-29 (line)]] | alt | 305 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.498× (z -13.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.543× (z -12.2) |
| [[CHP-212 (line)]] | wt | 276 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.4) |
| [[SNU-1 (line)]] | wt | 239 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -10.5) |
| [[SW 1088 (line)]] | alt | 510 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.8) |
| [[C-33 A (line)]] | alt | 259 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 320 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS6KC1]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[SCAMP1]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[DYM]] | +0.54 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.54 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[ZCCHC7]] | +0.53 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[COG5]] | +0.52 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[TULP3]] | +0.52 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[BTRC]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ANO10]] | +0.51 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[ANKS3]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 | same gene group |
| [[UBR2]] | +0.51 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[VPS35]] | +0.51 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF6]] | -0.53 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[PLEKHG2]] | -0.53 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPL]] | -0.52 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[MCL1]] | -0.51 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TMEM147-AS1]] | -0.50 | -0.63 / -0.31 | both halves | 2e-04 |  |
| [[ZNF628]] | -0.50 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ATXN7L2]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[H6PD]] | -0.48 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[PNRC2]] | -0.48 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[PTP4A3]] | -0.48 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[TRA2B]] | -0.48 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ZYX]] | -0.48 | -0.46 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-4.3, -52.3); signed map (-44.1, 6.7). **Vector** length 98.5, 34.5% of its response variance represented; |z| ≥ 3 in 1,444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +3.5 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | -0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +0.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.6 | +0.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -7.7 | -14.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -14.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -5.1 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and IBR domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:92,245,974-92,401,383 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434A0225, KIAA1386 |
| Gene groups (HGNC) | Ring finger proteins; Ankyrin repeat domain containing; RBR E3 ubiquitin ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2G1](https://www.uniprot.org/uniprotkb/Q9P2G1) (Ankyrin repeat and IBR domain-containing protein 1):

> Might act as an E3 ubiquitin-protein ligase, or as part of E3 complex, which accepts ubiquitin from specific E2 ubiquitin-conjugating enzymes and then transfers it to substrates.

**Summary**, from NCBI Gene [54467](https://www.ncbi.nlm.nih.gov/gene/54467):

> Predicted to enable ubiquitin conjugating enzyme binding activity and ubiquitin protein ligase activity. Predicted to be involved in ubiquitin-dependent protein catabolic process. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22215) · Entrez [54467](https://www.ncbi.nlm.nih.gov/gene/54467) · UniProt [Q9P2G1](https://www.uniprot.org/uniprotkb/Q9P2G1) · Ensembl [ENSG00000001629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001629)

## Data

Gene col 14: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14]; `tensor/DDL_lfc|DDL_z.npy` [14]; `embed/gene_vectors.npy` [14]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14 or target_col == 14). Every well: [[ANKIB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKIB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
