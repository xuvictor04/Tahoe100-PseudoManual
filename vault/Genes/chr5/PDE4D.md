---
symbol: "PDE4D"
type: "gene"
col: 3464
ensembl_id: "ENSG00000113448"
name: "phosphodiesterase 4D"
location: "5q11.2-q12.1"
module: 19
arm: "+"
pooled_cpm: 1001.1
n_lines_expressing: 37
n_dd_up: 1
n_dd_down: 43
n_dd_up_clean: 1
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 12
direction_downstream: 7
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PDE4D

*phosphodiesterase 4D* — 5q11.2-q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 1.29× (z +4.0, q 0.039, up in 20 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dexamethasone (drug)]] 0.5 µM in 2 lines (SHP-77 2.18×, NCI-H1573 3.02×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.32×; ⚠ position not correctable); [[Phenylephrine (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 2.20×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (SHP-77 2.18×).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.318× (z -17.8, q 0e+00, down in 35 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPS1]] (+0.59, fdr 1e-05), [[PDE7B]] (+0.58, fdr 1e-05), [[PDE4B]] (+0.57, fdr 1e-05); moves opposite to [[TPD52L2]] (-0.48, fdr 1e-04), [[ST6GALNAC6-1]] (-0.47, fdr 4e-05), [[RTN4R]] (-0.47, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CD36]] → it (grade B ⚠); 7 go from it, the strongest it → [[RUBCN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3464.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dexamethasone (drug)]] 0.5 µM in 2 lines (SHP-77 2.18×, NCI-H1573 3.02×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.32×; ⚠ position not correctable); [[Phenylephrine (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 2.20×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (SHP-77 2.18×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.039 | 20/35 (COLO 205, AsPC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.27× | +3.3 | 0.20 | 17/35 (SHP-77, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.24× | +3.2 | 0.20 | 22/34 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.23× | +3.2 | 0.20 | 15/35 (A498, A-172, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.318×** | -17.8 | 0e+00 | 35/35 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.329×** | -17.3 | 0e+00 | 35/35 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.337×** | -16.9 | 0e+00 | 35/35 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.554×** | -13.0 | 2e-36 | 32/36 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.573×** | -12.2 | 2e-32 | 28/35 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.462×** | -12.0 | 3e-31 | 32/35 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.457×** | -11.7 | 1e-29 | 31/34 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.521×** | -10.1 | 3e-22 | 34/35 (hTERT-HPNE, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.563×** | -8.9 | 3e-17 | 33/35 (A-427, AN3 CA, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.698×** | -7.9 | 2e-13 | 29/36 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.607×** | -7.7 | 5e-13 | 26/35 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.646×** | -6.8 | 5e-10 | 27/35 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.648×** | -6.7 | 7e-10 | 28/35 (hTERT-HPNE, RPMI-7951, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.675×** | -5.9 | 2e-07 | 25/35 (NCI-H460, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.687×** | -5.8 | 2e-07 | 23/35 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.691×** | -5.5 | 1e-06 | 24/34 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.707×** | -5.1 | 9e-06 | 26/35 (AN3 CA, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -4.7 | 7e-05 | 21/35 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5,988 | 0 | 19 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -27.3) |
| [[NCI-H1792 (line)]] | alt | 2,906 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0929× (z -34.6) |
| [[SW480 (line)]] | alt | 966 | 0 | 17 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -28.2) |
| [[AN3 CA (line)]] | alt | 2,666 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -26.0) |
| [[LoVo (line)]] | wt | 1,186 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -18.9) |
| [[SHP-77 (line)]] | alt | 684 | 6 | 7 (2 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.20× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.2) |
| [[A549 (line)]] | wt | 4,360 | 0 | 12 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0955× (z -24.0) |
| [[NCI-H1573 (line)]] | alt | 954 | 1 | 11 (2 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.02× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -21.4) |
| [[RPMI-7951 (line)]] | alt | 629 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -21.3) |
| [[A-427 (line)]] | wt | 1,868 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 977 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 450 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -15.4) |
| [[Hs 766T (line)]] | wt | 790 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -16.3) |
| [[SW 900 (line)]] | alt | 644 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -18.2) |
| [[C-33 A (line)]] | alt | 670 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -21.4) |
| [[HOP62 (line)]] | alt | 323 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 567 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -15.3) |
| [[SNU-1 (line)]] | wt | 2,300 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -17.5) |
| [[H4 (line)]] | wt | 910 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -20.5) |
| [[HT-29 (line)]] | alt | 690 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -17.7) |
| [[LOX-IMVI (line)]] | wt | 607 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 482 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.8) |
| [[COLO 205 (line)]] | alt | 389 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -21.5) |
| [[NCI-H2030 (line)]] | alt | 2,615 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -16.2) |
| [[A498 (line)]] | wt | 590 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -11.0) |
| [[A-172 (line)]] | wt | 385 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.335× (z -10.0) |
| [[LS 180 (line)]] | wt | 574 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -17.3) |
| [[SK-MEL-2 (line)]] | alt | 344 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -10.0) |
| [[SW48 (line)]] | wt | 349 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -10.3) |
| [[BT-474 (line)]] | alt | 158 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 400 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 497 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 234 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 129 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 213 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 438 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 188 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 220 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 169 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1,702 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 84.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1,141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 531 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 160 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 108 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 200 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 205 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 338 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 399 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 212 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPS1]] | +0.59 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PDE7B]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 | same gene group; pathway: G alpha (s) signalling events; STRING 520 |
| [[PDE4B]] | +0.57 | +0.50 / +0.62 | both halves | 1e-05 | same gene group; pathway: DARPP-32 events; STRING 757 |
| [[COL4A5]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CXXC4]] | +0.53 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[CDH7]] | +0.53 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[DPYD]] | +0.52 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[GPC6]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[FGF14]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 | same gene group |
| [[MAPK10]] | +0.51 | +0.45 / +0.42 | both halves | 4e-05 | same gene group |
| [[TCF4]] | +0.51 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[SLC39A8]] | +0.51 | +0.56 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.48 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[ST6GALNAC6-1]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[RTN4R]] | -0.47 | -0.31 / -0.52 | both halves | 2e-04 | same gene group |
| [[KLC3]] | -0.46 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[C11orf80]] | -0.46 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[EIF4E3]] | -0.46 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[ST6GALNAC6]] | -0.45 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[ZFYVE21]] | -0.45 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[KLC1]] | -0.44 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[TMEM184B]] | -0.44 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[ZNF185]] | -0.44 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[RUBCN]] | -0.44 | -0.29 / -0.47 | both halves | 2e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD36]] | B | CD36 activity raises PDE4D's level | lines that do not express CD36 (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without CD36 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GNAT3, RPS4Y1, LIN7A; maybe low, not absent |
| [[MEIS1]] | B | MEIS1 activity raises PDE4D's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 2.55× lower at baseline in the lines without MEIS1 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[PDK4]] | B | PDK4 activity raises PDE4D's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without PDK4 | 0.016 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[ASB4]] | B | ASB4 activity raises PDE4D's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without ASB4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[PDE4B]] | B | PDE4B activity raises PDE4D's level | lines that do not express PDE4B (24) vs lines expressing it (26) | 2.59× lower at baseline in the lines without PDE4B | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCSK2, MAPK4, UNC5D |
| [[KYNU]] | B | KYNU activity raises PDE4D's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.71× lower at baseline in the lines without KYNU | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[NNMT]] | B | NNMT activity raises PDE4D's level | lines that do not express NNMT (24) vs lines expressing it (26) | 1.76× lower at baseline in the lines without NNMT | 0.059 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615 |
| [[GPRIN3]] | B | GPRIN3 activity raises PDE4D's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.41× lower at baseline in the lines without GPRIN3 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[PDE7B]] | B | PDE7B activity raises PDE4D's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 1.91× lower at baseline in the lines without PDE7B | 0.077 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent |
| [[TCF4]] | B | TCF4 activity raises PDE4D's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without TCF4 | 0.086 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1 |
| [[FGF14]] | B | FGF14 activity raises PDE4D's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 2.31× lower at baseline in the lines without FGF14 | 0.088 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2 |
| [[KCNJ6]] | B | KCNJ6 activity raises PDE4D's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without KCNJ6 | 0.091 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUBCN]] | B | PDE4D activity lowers RUBCN's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.33× higher at baseline in the lines without PDE4D | 0.010 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[ZFYVE21]] | B | PDE4D activity lowers ZFYVE21's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.30× higher at baseline in the lines without PDE4D | 0.024 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[KLC3]] | B | PDE4D activity lowers KLC3's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.78× higher at baseline in the lines without PDE4D | 0.045 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[MEIS1]] | B | PDE4D activity raises MEIS1's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 2.62× lower at baseline in the lines without PDE4D | 0.060 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[ST6GALNAC2]] | B | PDE4D activity lowers ST6GALNAC2's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.49× higher at baseline in the lines without PDE4D | 0.061 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[C11orf80]] | B | PDE4D activity lowers C11orf80's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.44× higher at baseline in the lines without PDE4D | 0.062 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[FOXP1]] | B | PDE4D activity raises FOXP1's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without PDE4D | 0.081 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.450). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.6, 34.1); signed map (38.5, 42.8). **Vector** length 99.9, 30.6% of its response variance represented; |z| ≥ 3 in 1,485 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | +7.2 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +7.2 | -5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.9 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | -12.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +4.0 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.1 | -7.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.9 | -7.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.7 | -4.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.5 | -5.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -4.0 | -5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.0 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 4D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2-q12.1 — chr5:58,969,038-60,522,120 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DPDE3 |
| Gene groups (HGNC) | Phosphodiesterases; MicroRNA protein coding host genes |
| Reactome | 10 pathways, smallest: DARPP-32 events; Turbulent (oscillatory, disturbed) flow shear stress activates signaling by PIEZO1 and integrins in endothelial cells; Opioid Signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08499](https://www.uniprot.org/uniprotkb/Q08499) (3',5'-cyclic-AMP phosphodiesterase 4D):

> Hydrolyzes the second messenger cAMP, which is a key regulator of many important physiological processes.

**Summary**, from NCBI Gene [5144](https://www.ncbi.nlm.nih.gov/gene/5144):

> This gene encodes one of four mammalian counterparts to the fruit fly 'dunce' gene. The encoded protein has 3',5'-cyclic-AMP phosphodiesterase activity and degrades cAMP, which acts as a signal transduction molecule in multiple cell types. This gene uses different promoters to generate multiple alternatively spliced transcript variants that encode functional proteins.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:8783](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8783) · Entrez [5144](https://www.ncbi.nlm.nih.gov/gene/5144) · UniProt [Q08499](https://www.uniprot.org/uniprotkb/Q08499) · Ensembl [ENSG00000113448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113448)

## Data

Gene col 3464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3464); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3464]; `tensor/DDL_lfc|DDL_z.npy` [3464]; `embed/gene_vectors.npy` [3464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3464 or target_col == 3464). Every well: [[PDE4D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE4D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
