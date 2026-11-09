---
symbol: "SEPTIN7"
type: "gene"
col: 4348
ensembl_id: "ENSG00000122545"
name: "septin 7"
location: "7p14.2"
module: 182
arm: "+"
pooled_cpm: 362.2
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# SEPTIN7

*septin 7* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.93× (z +10.8, q 2e-24, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.31× (z +4.6, q 6e-04, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.609× (z -8.2, q 1e-13, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAF6]] (+0.58, fdr 1e-05), [[ROCK1]] (+0.58, fdr 1e-05), [[MIER1]] (+0.53, fdr 2e-05); moves opposite to [[SLC35C2]] (-0.54, fdr 2e-05), [[ZNF587]] (-0.53, fdr 1e-04), [[CHERP]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.93×** | +10.8 | 2e-24 | 46/49 (PANC-1, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.55×** | +7.0 | 8e-10 | 36/44 (A498, Hs 766T, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +6.7 | 5e-09 | 34/45 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.34×** | +4.8 | 2e-04 | 32/48 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 6e-04 | 41/48 (A549, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.26×** | +3.9 | 0.010 | 28/48 (SW480, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.26×** | +3.8 | 0.012 | 30/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.044 | 29/48 (PANC-1, H4, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.045 | 27/48 (H4, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.050 | 29/47 (A549, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.45×** | +3.2 | 0.067 | 29/49 (AsPC-1, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.20× | +3.1 | 0.10 | 22/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4348.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.609×** | -8.2 | 1e-13 | 45/48 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.630×** | -7.7 | 5e-12 | 40/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.744×** | -4.9 | 2e-04 | 32/48 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.766×** | -4.3 | 0.003 | 32/47 (SW 900, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.813×** | -3.4 | 0.083 | 28/48 (C32, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.0 | 0.23 | 19/48 (NCI-H2030, AN3 CA, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 511 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.530× (z -9.0) |
| [[Hs 766T (line)]] | wt | 342 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 0.5 µM 0.496× (z -9.3) |
| [[SW480 (line)]] | alt | 194 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 520 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 438 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 370 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.474× (z -9.5) |
| [[HOP62 (line)]] | alt | 375 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 453 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.470× (z -10.3) |
| [[SNU-423 (line)]] | alt | 367 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 5 µM 0.531× (z -8.5) |
| [[AN3 CA (line)]] | alt | 448 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 454 | 1 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 3.71× (z +11.1) ⚠ cell-cycle shift, explains ~46% of this change | [[Panobinostat (drug)]] 0.5 µM 0.541× (z -9.9) |
| [[C32 (line)]] | wt | 399 | 1 | 1 | [[Ponatinib (drug)]] 5 µM 2.16× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.510× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 575 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.74× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -9.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HT-29 (line)]] | alt | 266 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 291 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 394 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 154 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 311 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 372 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.75× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 281 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.521× (z -8.8) |
| [[COLO 205 (line)]] | alt | 160 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 614 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HCT15 (line)]] | alt | 314 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HS-578T (line)]] | alt | 441 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 213 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 511 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 282 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 435 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 406 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 298 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RPMI-7951 (line)]] | alt | 504 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SHP-77 (line)]] | alt | 349 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.551× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 468 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.639× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 390 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.466× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 362 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 333 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 304 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 259 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 213 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 419 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 313 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 369 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 651 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 428 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 331 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF6]] | +0.58 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ROCK1]] | +0.58 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[MIER1]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[UBR5]] | +0.52 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[DOCK7]] | +0.51 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[TMOD3]] | +0.50 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[RAD21]] | +0.50 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[EXOC5]] | +0.49 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[IARS2]] | +0.49 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[CAPZA2]] | +0.49 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[SSBP2]] | +0.49 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[FGFR1OP2]] | +0.49 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35C2]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ZNF587]] | -0.53 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[CHERP]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ZNF628]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SPATA2]] | -0.49 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[PUS1]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[DPH2]] | -0.48 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[SNAPC4]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[TRMT61A]] | -0.46 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[PPRC1]] | -0.45 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[RRP7BP]] | -0.44 | -0.29 / -0.52 | both halves | 3e-04 |  |
| [[NSUN4]] | -0.44 | -0.32 / -0.56 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SEPTIN7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **+** arm (projection on the module's main direction 0.433). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (1.7, -56.6); signed map (5.3, -13.5). **Vector** length 110, 46.7% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | -8.2 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -2.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.4 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.0 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | septin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.2 — chr7:35,800,932-35,907,110 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDC3, SEPT7A, Septin-7; previously CDC10, SEPT7 |
| Gene groups (HGNC) | Septins |
| Reactome | 2 pathways, smallest: MAPK6/MAPK4 signaling; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16181](https://www.uniprot.org/uniprotkb/Q16181) (Septin-7):

> Filament-forming cytoskeletal GTPase. Required for normal organization of the actin cytoskeleton. Required for normal progress through mitosis. Involved in cytokinesis. Required for normal association of CENPE with the kinetochore. Plays a role in ciliogenesis and collective cell movements. Forms a filamentous structure with SEPTIN12, SEPTIN6, SEPTIN2 and probably SEPTIN4 at the sperm annulus which is required for the structural integrity and motility of the sperm tail during postmeiotic …

**Summary**, from NCBI Gene [989](https://www.ncbi.nlm.nih.gov/gene/989):

> This gene encodes a protein that is highly similar to the CDC10 protein of Saccharomyces cerevisiae. The protein also shares similarity with Diff 6 of Drosophila and with H5 of mouse. Each of these similar proteins, including the yeast CDC10, contains a GTP-binding motif. The yeast CDC10 protein is a structural component of the 10 nm filament which lies inside the cytoplasmic membrane and is essential for cytokinesis. This human protein functions in gliomagenesis and in the suppression of …

**Accessions** — [HGNC:1717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1717) · Entrez [989](https://www.ncbi.nlm.nih.gov/gene/989) · UniProt [Q16181](https://www.uniprot.org/uniprotkb/Q16181) · Ensembl [ENSG00000122545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122545)

## Data

Gene col 4348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4348); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4348]; `tensor/DDL_lfc|DDL_z.npy` [4348]; `embed/gene_vectors.npy` [4348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4348 or target_col == 4348). Every well: [[SEPTIN7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
