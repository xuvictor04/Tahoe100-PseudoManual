---
symbol: "SLC39A1"
type: "gene"
col: 6773
ensembl_id: "ENSG00000143570"
name: "solute carrier family 39 member 1"
location: "1q21.3"
module: 14
arm: "+"
pooled_cpm: 29.45
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SLC39A1

*solute carrier family 39 member 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +11.6, q 2e-28, up in 40 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.48× (z +3.8, q 0.009, up in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H460 3.29×, SW480 3.10×, HOP62 4.52×, PANC-1 2.85×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 5.05×, A498 2.88×, J82 2.96×, SNU-423 2.78×, …; ⚠ cell-cycle shift, explains ~80% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 2.95×, A-172 3.11×; ⚠ cell-cycle shift, explains ~49% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 4.26×).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.548× (z -8.5, q 2e-14, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAPBP]] (+0.67, fdr 1e-05), [[MED12]] (+0.66, fdr 1e-05), [[TAPBPL]] (+0.65, fdr 1e-05); moves opposite to [[HERC2P3]] (-0.61, fdr 2e-05), [[HERC2P9]] (-0.61, fdr 1e-05), [[DAP3]] (-0.56, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LUM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6773.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H460 3.29×, SW480 3.10×, HOP62 4.52×, PANC-1 2.85×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 5.05×, A498 2.88×, J82 2.96×, SNU-423 2.78×, …; ⚠ cell-cycle shift, explains ~80% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 2.95×, A-172 3.11×; ⚠ cell-cycle shift, explains ~49% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 4.26×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +11.6 | 2e-28 | 40/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +9.7 | 1e-19 | 28/36 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +6.9 | 1e-09 | 30/42 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.55×** | +6.2 | 1e-07 | 33/46 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.33×** | +5.6 | 3e-06 | 25/47 (A-172, A498, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.44×** | +4.9 | 7e-05 | 26/47 (A498, A-172, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.40×** | +4.7 | 2e-04 | 24/46 (PANC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.1 | 0.003 | 3/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.009 | 17/47 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.7 | 0.010 | 20/46 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.054 | 18/46 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +3.1 | 0.089 | 16/48 (A498, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6773.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.548×** | -8.5 | 2e-14 | 43/48 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -7.5 | 2e-11 | 40/48 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.625×** | -6.6 | 7e-09 | 39/47 (SW1417, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.653×** | -5.8 | 1e-06 | 35/47 (C32, NCI-H2030, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -4.7 | 3e-04 | 30/45 (H4, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.733×** | -4.4 | 0.001 | 23/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.769×** | -3.7 | 0.017 | 20/47 (C32, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.760×** | -3.7 | 0.018 | 24/48 (NCI-H23, RPMI-7951, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.783×** | -3.5 | 0.035 | 17/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.795×** | -3.2 | 0.066 | 18/48 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.665× | -3.0 | 0.13 | 12/47 (CHP-212, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 42.0 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.3) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[A-172 (line)]] | wt | 34.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +18.9) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 26.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 30.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +10.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -11.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -8.5) ⚠ cell-cycle shift, explains ~80% of this change |
| [[HEC-1-A (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +10.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.1) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[NCI-H2030 (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -9.6) |
| [[PANC-1 (line)]] | alt | 36.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.5) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[SW 900 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +8.7) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[SW480 (line)]] | alt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAPBP]] | +0.67 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[MED12]] | +0.66 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[GPR108]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 | same gene group |
| [[RAP2C]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PLXNB2]] | +0.62 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[FBRS]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[BCL9L]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[STAP2]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[UBAP2L]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[HLA-H]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[GRINA]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P3]] | -0.61 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[HERC2P9]] | -0.61 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[DAP3]] | -0.56 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ABTB3]] | -0.56 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[HERC2P2]] | -0.56 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[GNA12]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[PACC1]] | -0.54 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[CACYBP]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[EVI5]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RNF216]] | -0.53 | -0.45 / -0.43 | both halves | 3e-05 | same gene group |
| [[SH3KBP1]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ZNF496]] | -0.53 | -0.50 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUM]] | B | LUM activity lowers SLC39A1's level | lines that do not express LUM (34) vs lines expressing it (16) | 1.15× higher at baseline in the lines without LUM | 0.036 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2 |
| [[HDAC6]] | B | HDAC6 activity raises SLC39A1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises SLC39A1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NFIX]] | B | NFIX activity lowers SLC39A1's level | lines that do not express NFIX (8) vs lines expressing it (42) | 1.36× higher at baseline in the lines without NFIX | 0.096 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.2, 4.2); signed map (12.5, -17.7). **Vector** length 82.1, 17.9% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +7.4 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.7 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.2 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | -0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.7 | +0.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.7 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.5 | -4.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 39 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,959,099-153,968,184 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZIP1; previously ZIRTL |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 39 |
| Reactome | 5 pathways, smallest: Zinc influx into cells by the SLC39 gene family; Zinc transporters; Metal ion SLC transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY26](https://www.uniprot.org/uniprotkb/Q9NY26) (Zinc transporter ZIP1):

> Transporter for the divalent cation Zn(2+). Mediates the influx of Zn(2+) into cells from extracellular space. Functions as the major importer of zinc from circulating blood plasma into prostate cells.

**Summary**, from NCBI Gene [27173](https://www.ncbi.nlm.nih.gov/gene/27173):

> This gene encodes a member of the zinc-iron permease family. The encoded protein is localized to the cell membrane and acts as a zinc uptake transporter. This gene has been linked to prostate cancer, breast cancer, and Alzheimer's disease. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:12876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12876) · Entrez [27173](https://www.ncbi.nlm.nih.gov/gene/27173) · UniProt [Q9NY26](https://www.uniprot.org/uniprotkb/Q9NY26) · Ensembl [ENSG00000143570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143570)

## Data

Gene col 6773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6773); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6773]; `tensor/DDL_lfc|DDL_z.npy` [6773]; `embed/gene_vectors.npy` [6773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6773 or target_col == 6773). Every well: [[SLC39A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC39A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
