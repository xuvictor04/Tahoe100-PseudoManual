---
symbol: "SH3TC2-DT"
type: "gene"
col: 14661
ensembl_id: "ENSG00000250072"
name: "SH3TC2 divergent transcript"
location: "5q32"
module: 195
arm: "+"
pooled_cpm: 14.43
n_lines_expressing: 26
n_dd_up: 6
n_dd_down: 31
n_dd_up_clean: 2
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 5
direction_downstream: 13
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# SH3TC2-DT

*SH3TC2 divergent transcript* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.42× (z +7.6, q 2e-11, up in 6 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.65× (z +4.3, q 0.002, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.385× (z -11.5, q 9e-28, down in 20 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3TC2]] (+0.93, fdr 7e-06, ⚠ same locus), [[MYEOV]] (+0.66, fdr 7e-06), [[S100A16]] (+0.63, fdr 7e-06), [[ETV4]] (+0.63, fdr 8e-06).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[COL13A1]] → it (grade B ⚠); 13 go from it, the strongest it → [[LINC02320]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +7.6 | 2e-11 | 6/20 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +7.3 | 8e-11 | 3/12 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +5.8 | 1e-06 | 4/17 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.65×** | +4.3 | 0.002 | 16/23 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.65×** | +3.7 | 0.022 | 8/20 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.066 | 6/23 (SW480, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.44× | +3.0 | 0.16 | 3/20 (SW1417, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.42× | +3.0 | 0.16 | 6/23 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[Erythromycin (drug)]] 5 µM |  | 1.42× | +3.0 | 0.16 | 2/23 (SNU-423, LOX-IMVI) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 1 with an alert ⚠; shown: the 15 strongest. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.385×** | -11.5 | 9e-28 | 20/22 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.360×** | -8.7 | 8e-16 | 18/22 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.345×** | -8.6 | 1e-15 | 23/23 (C32, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.352×** | -8.6 | 2e-15 | 20/22 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.393×** | -8.0 | 2e-13 | 22/23 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.406×** | -7.4 | 1e-11 | 18/22 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.394×** | -7.3 | 2e-11 | 19/23 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.449×** | -7.1 | 1e-10 | 20/23 (C32, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.469×** | -6.4 | 8e-09 | 16/23 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.539×** | -6.4 | 9e-09 | 18/23 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.492×** | -6.0 | 8e-08 | 20/23 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.617×** | -5.8 | 4e-07 | 16/23 (C32, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.513×** | -5.7 | 6e-07 | 16/23 (C32, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.546×** | -5.1 | 1e-05 | 18/23 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.550×** | -5.1 | 1e-05 | 15/23 (SNU-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 331 | 0 | 26 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0426× (z -28.3) |
| [[MIA PaCa-2 (line)]] | alt | 140 | 0 | 24 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.241× (z -26.1) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0369× (z -24.7) |
| [[C32 (line)]] | wt | 50.6 | 0 | 17 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0135× (z -18.9) |
| [[AsPC-1 (line)]] | alt | 21.8 | 0 | 15 | — | [[Homoharringtonine (drug)]] 5 µM 0.0647× (z -16.7) |
| [[HEC-1-A (line)]] | alt | 47.6 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0477× (z -20.8) |
| [[LoVo (line)]] | wt | 10.0 | 0 | 5 | — | [[Trametinib (drug)]] 0.5 µM 0.141× (z -11.1) |
| [[SW480 (line)]] | alt | 8.50 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0876× (z -16.4) |
| [[Hs 766T (line)]] | wt | 24.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -13.4) |
| [[LS 180 (line)]] | wt | 9.19 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0914× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 6.88 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -14.8) |
| [[HOP62 (line)]] | alt | 4.67 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0628× (z -9.7) |
| [[KATO III (line)]] | alt | 6.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 5.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -11.0) |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -14.5) |
| [[A-172 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3TC2]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[MYEOV]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[S100A16]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ETV4]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[ITGB5]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[KPNA2P3]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[COL13A1]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[BLACAT1]] | +0.60 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ANO1]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[LINC02320]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ST3GAL1]] | +0.58 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[ACOT7]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL13A1]] | B | COL13A1 activity raises SH3TC2-DT's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.56× lower at baseline in the lines without COL13A1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[MAP2K1]] | B | MAP2K1 activity raises SH3TC2-DT's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SH3TC2]] | C | SH3TC2 activity raises SH3TC2-DT's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 4.07× lower at baseline in the lines without SH3TC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent; co-absent with the target |
| [[PTPRZ1]] | C | PTPRZ1 activity raises SH3TC2-DT's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.94× lower at baseline in the lines without PTPRZ1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029; co-absent with the target |
| [[LAPTM5]] | C | LAPTM5 activity raises SH3TC2-DT's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without LAPTM5 | 0.095 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02320]] | B | SH3TC2-DT activity raises LINC02320's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 2.46× lower at baseline in the lines without SH3TC2-DT | 0.007 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[SOX13]] | B | SH3TC2-DT activity raises SOX13's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 1.85× lower at baseline in the lines without SH3TC2-DT | 0.010 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[ITGA6]] | B | SH3TC2-DT activity raises ITGA6's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 2.03× lower at baseline in the lines without SH3TC2-DT | 0.041 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[TINAGL1]] | B | SH3TC2-DT activity raises TINAGL1's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 2.45× lower at baseline in the lines without SH3TC2-DT | 0.062 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | B | SH3TC2-DT activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 1.32× lower at baseline in the lines without SH3TC2-DT | 0.067 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[KIAA1671]] | B | SH3TC2-DT activity raises KIAA1671's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 1.26× lower at baseline in the lines without SH3TC2-DT | 0.080 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[SLC20A1]] | B | SH3TC2-DT activity raises SLC20A1's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 1.44× lower at baseline in the lines without SH3TC2-DT | 0.083 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[NIBAN2]] | B | SH3TC2-DT activity raises NIBAN2's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 1.78× lower at baseline in the lines without SH3TC2-DT | 0.084 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[SERPINB5]] | B | SH3TC2-DT activity raises SERPINB5's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without SH3TC2-DT | 0.086 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | B | SH3TC2-DT activity strengthens ARHGAP27P1-BPTFP1-KPNA2P3's drug response | lines that do not express SH3TC2-DT (24) vs lines expressing it (24) | the lines without SH3TC2-DT respond 0.55× as strongly (z diff +1.47); strongest at Harringtonine 0.5 µM: 0.74x vs 0.49x (z diff +2.2) | 0.086 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G; target measured in part of the lines; artifact flags |
| [[STAMBPL1]] | B | SH3TC2-DT activity raises STAMBPL1's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without SH3TC2-DT | 0.098 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[SH3TC2]] | C | SH3TC2-DT activity raises SH3TC2's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 4.99× lower at baseline in the lines without SH3TC2-DT | 1e-04 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G; co-absent with the target |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.3, 4.3); signed map (4.7, 40.5). **Vector** length 98.2, 30.8% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | -1.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.2 | -8.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.2 | -7.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.2 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.1 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.0 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | SH3TC2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q32 — chr5:149,063,239-149,129,578 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52905) · Entrez [255187](https://www.ncbi.nlm.nih.gov/gene/255187) · Ensembl [ENSG00000250072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250072)

## Data

Gene col 14661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14661); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14661]; `tensor/DDL_lfc|DDL_z.npy` [14661]; `embed/gene_vectors.npy` [14661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14661 or target_col == 14661). Every well: [[SH3TC2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3TC2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
