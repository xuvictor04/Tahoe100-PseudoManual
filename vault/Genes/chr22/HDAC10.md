---
symbol: "HDAC10"
type: "gene"
col: 1961
ensembl_id: "ENSG00000100429"
name: "histone deacetylase 10"
location: "22q13.33"
module: 2
arm: "+"
pooled_cpm: 8.56
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 599
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# HDAC10

*histone deacetylase 10* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.73× (z +6.9, q 2e-09, up in 9 of 18 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.456× (z -10.3, q 2e-22, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL17]] (+0.66, fdr 7e-06), [[UCKL1]] (+0.64, fdr 7e-06), [[MAPK12]] (+0.63, fdr 1e-05, ⚠ same locus), [[ZDHHC8]] (+0.63, fdr 1e-05); moves opposite to [[CALM2]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 599 go from it, the strongest it → [[CDC23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.9 | 2e-09 | 9/18 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.1 | 1e-04 | 15/34 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.8 | 4e-04 | 12/38 (NCI-H1573, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.30× | +3.3 | 0.12 | 11/38 (NCI-H1792, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.28× | +3.3 | 0.13 | 9/44 (H4, Panc 03.27, …) | two highest doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | 1.40× | +3.2 | 0.13 | 2/43 (NCI-H23, NCI-H1792) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.15 | 8/42 (SW480, RPMI-7951, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.28× | +3.0 | 0.15 | 9/24 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 0.05 µM |  | 1.28× | +3.0 | 0.15 | 5/46 (A498, CHP-212, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1961.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.456×** | -10.3 | 2e-22 | 38/47 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -8.5 | 5e-15 | 34/46 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.532×** | -8.3 | 2e-14 | 31/46 (J82, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.652×** | -8.0 | 2e-13 | 26/44 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -7.0 | 3e-10 | 28/46 (COLO 205, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.589×** | -6.7 | 2e-09 | 25/46 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.633×** | -6.0 | 2e-07 | 20/42 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.642×** | -5.8 | 4e-07 | 22/46 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.749×** | -5.4 | 5e-06 | 20/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.767×** | -4.9 | 5e-05 | 14/48 (SW1417, SW48, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.694×** | -4.8 | 8e-05 | 20/47 (A-172, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.543×** | -4.2 | 0.001 | 15/45 (SHP-77, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.760×** | -3.6 | 0.013 | 13/47 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.761×** | -3.6 | 0.014 | 10/45 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.764×** | -3.5 | 0.015 | 9/46 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.756×** | -3.5 | 0.018 | 11/43 (A-172, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.634×** | -3.1 | 0.048 | 8/43 (MIA PaCa-2, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.783×** | -3.1 | 0.050 | 6/48 (MIA PaCa-2, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0924× (z -12.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -9.8) |
| [[C32 (line)]] | wt | 10.8 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.115× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[SW 900 (line)]] | alt | 5.92 | 0 | 2 | — | [[Saquinavir (drug)]] 0.05 µM 0.0747× (z -9.6) |
| [[SW48 (line)]] | wt | 11.5 | 0 | 2 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0804× (z -9.4) |
| [[COLO 205 (line)]] | alt | 6.38 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0711× (z -8.5) |
| [[H4 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0763× (z -9.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[J82 (line)]] | alt | 5.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0943× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 7.35 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -9.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL17]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[UCKL1]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[MAPK12]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZDHHC8]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[NPIPA1]] | +0.61 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[POMT1]] | +0.59 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TUBGCP6]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 | STRING 521; ⚠ same locus (0.2 kb, same strand: neighbours can correlate without regulation) |
| [[LLGL1]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ABCA2]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[GDPD3]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CPSF1]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[INPP5E]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[FBXO44]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PLCG1]] | +0.56 | +0.61 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALM2]] | -0.45 | -0.35 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*599 arrows, 599 of them with an alert ⚠; grade A 0, B 599, C 0. Shown: the 12 strongest; 587 more arrows (587 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC23]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity raises CDC23's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CMIP]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity lowers CMIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CROCCP3]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity lowers CROCCP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CYB561]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity raises CYB561's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[DNAJC2]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity raises DNAJC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ENSG00000288899]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity raises ENSG00000288899's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FAM78B]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity lowers FAM78B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FBXW9]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity raises FBXW9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FMN1]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity lowers FMN1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LRRC51]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity raises LRRC51's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MRPS7]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity raises MRPS7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NCBP3]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], HDAC10, [[HDAC11]] activity raises NCBP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.1, -24.0); signed map (-26.5, -0.2). **Vector** length 53.4, 6.94% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +3.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.3 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -5.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.3 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,245,183-50,251,405 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP761B039 |
| Gene groups (HGNC) | Histone deacetylases, class IIB |
| Reactome | 17 pathways, smallest: Notch-HLH transcription pathway; NOTCH signaling regulates gene expression in endothelial stalk cells; HDACs deacetylate histones |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969S8](https://www.uniprot.org/uniprotkb/Q969S8) (Polyamine deacetylase HDAC10):

> Polyamine deacetylase (PDAC), which acts preferentially on N(8)-acetylspermidine, and also on acetylcadaverine and acetylputrescine. Exhibits attenuated catalytic activity toward N(1),N(8)-diacetylspermidine and very low activity, if any, toward N(1)-acetylspermidine. Histone deacetylase activity has been observed in vitro. Has also been shown to be involved in MSH2 deacetylation. The physiological relevance of protein/histone deacetylase activity is unclear and could be very weak. May play a …

**Summary**, from NCBI Gene [83933](https://www.ncbi.nlm.nih.gov/gene/83933):

> The protein encoded by this gene belongs to the histone deacetylase family, members of which deacetylate lysine residues on the N-terminal part of the core histones. Histone deacetylation modulates chromatin structure, and plays an important role in transcriptional regulation, cell cycle progression, and developmental events. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:18128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18128) · Entrez [83933](https://www.ncbi.nlm.nih.gov/gene/83933) · UniProt [Q969S8](https://www.uniprot.org/uniprotkb/Q969S8) · Ensembl [ENSG00000100429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100429)

## Data

Gene col 1961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1961); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1961]; `tensor/DDL_lfc|DDL_z.npy` [1961]; `embed/gene_vectors.npy` [1961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1961 or target_col == 1961). Every well: [[HDAC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
