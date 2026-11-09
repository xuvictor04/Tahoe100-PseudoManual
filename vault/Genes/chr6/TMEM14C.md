---
symbol: "TMEM14C"
type: "gene"
col: 3290
ensembl_id: "ENSG00000111843"
name: "transmembrane protein 14C"
location: "6p24.2"
module: 142
arm: "+"
pooled_cpm: 35.8
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# TMEM14C

*transmembrane protein 14C* — 6p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.27× (z +15.7, q 0e+00, up in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 0.5 µM: 1.40× (z +3.6, q 0.034, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (J82 4.37×, PANC-1 5.27×, A498 4.88×, SNU-423 5.66×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 5.76×, HEC-1-A 6.49×, A-172 6.09×, A498 4.74×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.486× (z -4.1, q 0.022, down in 36 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.0941×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEPROT]] (+0.61, fdr 1e-05), [[ALCAM]] (+0.55, fdr 2e-05), [[DOP1A]] (+0.55, fdr 2e-05); moves opposite to [[RABEPK]] (-0.63, fdr 1e-05), [[SLC30A6]] (-0.61, fdr 1e-05), [[ADCY7]] (-0.59, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MYL9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3290.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (J82 4.37×, PANC-1 5.27×, A498 4.88×, SNU-423 5.66×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 5.76×, HEC-1-A 6.49×, A-172 6.09×, A498 4.74×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.27×** | +15.7 | 0e+00 | 44/45 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.07×** | +14.6 | 0e+00 | 34/36 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.10×** | +11.4 | 1e-27 | 39/43 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.69×** | +5.7 | 2e-06 | 34/46 (Hs 766T, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.034 | 25/48 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +3.4 | 0.059 | 25/48 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.35× | +3.2 | 0.10 | 22/48 (SK-MEL-2, A549, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3290.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.0941×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.486×** | -4.1 | 0.022 | 36/47 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | **0.774×** | -3.9 | 0.022 | 28/48 (AsPC-1, SNU-423, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.724×** | -3.5 | 0.075 | 22/47 (J82, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -3.5 | 0.075 | 24/48 (SNU-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.736× | -3.2 | 0.15 | 21/48 (C-33 A, A-172, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 36.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +12.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 50.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 34.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +11.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 46.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.60× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 50.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 51.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.44× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 50.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +12.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.20× (z +10.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 29.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 22.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 28.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.49× (z +13.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 39.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +9.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 81.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +13.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 31.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 36.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 26.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 59.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 47.5 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 45.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.76× (z +13.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.54× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.25× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 32.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.58× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 30.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.95× (z +12.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 41.3 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0941× (z -9.1) |
| [[HCT15 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.45× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 30.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 40.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +11.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEPROT]] | +0.61 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[ALCAM]] | +0.55 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[DOP1A]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[CFL2]] | +0.55 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[CXADR]] | +0.55 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[S100A4]] | +0.54 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[PICALM]] | +0.53 | +0.25 / +0.45 | both halves | 4e-04 |  |
| [[CMTM6]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SEMA3C]] | +0.53 | +0.56 / +0.37 | both halves | 7e-05 |  |
| [[CCDC50]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CREBL2]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ARHGEF12]] | +0.53 | +0.43 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABEPK]] | -0.63 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ADCY7]] | -0.59 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[GTF3C5]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CAPN15]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[IL17RA]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[GPR89A]] | -0.55 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[FERMT3]] | -0.55 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[KHDC1]] | -0.54 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[ERCC3]] | -0.54 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ANKUB1]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ZNF787]] | -0.53 | -0.51 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYL9]] | B | MYL9 activity raises TMEM14C's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.41× lower at baseline in the lines without MYL9 | 0.027 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[ANKRD33B]] | B | ANKRD33B activity raises TMEM14C's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without ANKRD33B | 0.050 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction -0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.0, -4.5); signed map (47.2, 17.8). **Vector** length 60.8, 12.7% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +11.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.4 | +0.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.7 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -0.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 14C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.2 — chr6:10,722,915-10,731,129 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC194, bA421M1.6, NET26; previously C6orf53 |
| Gene groups (HGNC) | Transmembrane protein 14 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0S9](https://www.uniprot.org/uniprotkb/Q9P0S9) (Transmembrane protein 14C):

> Required for normal heme biosynthesis.

**Summary**, from NCBI Gene [51522](https://www.ncbi.nlm.nih.gov/gene/51522):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in heme biosynthetic process. Predicted to act upstream of or within erythrocyte differentiation and mitochondrial transport. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20952) · Entrez [51522](https://www.ncbi.nlm.nih.gov/gene/51522) · UniProt [Q9P0S9](https://www.uniprot.org/uniprotkb/Q9P0S9) · Ensembl [ENSG00000111843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111843)

## Data

Gene col 3290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3290); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3290]; `tensor/DDL_lfc|DDL_z.npy` [3290]; `embed/gene_vectors.npy` [3290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3290 or target_col == 3290). Every well: [[TMEM14C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM14C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
