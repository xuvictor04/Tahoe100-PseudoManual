---
symbol: "CCDC190"
type: "gene"
col: 11741
ensembl_id: "ENSG00000185860"
name: "coiled-coil domain containing 190"
location: "1q23.3"
module: 116
arm: "+"
pooled_cpm: 3.54
n_lines_expressing: 12
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 29
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# CCDC190

*coiled-coil domain containing 190* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.74× (z +13.2, q 7e-37, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.34× (z +10.8, q 1e-24, up in 3 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.0760×, Hs 766T 0.0533×, RKO 0.0684×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.477×; ⚠ position not correctable); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.175×); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (RKO 0.0420×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01592]] (+0.73, fdr 7e-06), [[RGS4]] (+0.66, fdr 7e-06), [[FGF1]] (+0.65, fdr 7e-06); moves opposite to [[HSDL1]] (-0.44, fdr 1e-04), [[AVPI1]] (-0.44, fdr 9e-05), [[TOM1]] (-0.44, fdr 8e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC02509]] → it (grade C ⚠); 29 go from it, the strongest it → [[RGMB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.74×** | +13.2 | 7e-37 | 4/4 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.91×** | +11.2 | 9e-27 | 4/5 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.34×** | +10.8 | 1e-24 | 3/9 (J82, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.70×** | +10.2 | 4e-22 | 4/4 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +5.2 | 2e-05 | 1/9 (C32) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +5.1 | 3e-05 | 1/4 (MIA PaCa-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.8 | 1e-04 | 2/9 (HS-578T, MIA PaCa-2) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +4.4 | 7e-04 | 1/8 (HOP62) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.0 | 0.004 | 1/6 (SNU-423) | top dose only | cell-cycle shift (explains ~9% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **3.23×** | +3.9 | 0.006 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.92×** | +3.8 | 0.009 | 0/8 | top dose only | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.13×** | +3.4 | 0.031 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +3.1 | 0.075 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.54×** | +3.1 | 0.078 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +3.1 | 0.078 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.62×** | +3.1 | 0.079 | 1/6 (RKO) | inconsistent across doses | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.67×** | +3.0 | 0.088 | 0/6 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11741.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.0760×, Hs 766T 0.0533×, RKO 0.0684×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.477×; ⚠ position not correctable); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.175×); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (RKO 0.0420×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | 0.688× | -3.4 | 0.28 | 4/9 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | 0.601× | -3.1 | 0.28 | 0/9 | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 74.0 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0760× (z -11.7) |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0533× (z -10.0) |
| [[RKO (line)]] | wt | 11.5 | 0 | 2 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0420× (z -10.5) |
| [[A-172 (line)]] | wt | 0.705 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.316 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.424 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01592]] | +0.73 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[RGS4]] | +0.66 | +0.62 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[FGF1]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CDH6]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ROBO4]] | +0.63 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[LINC01776]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ANK1]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[HTR1F]] | +0.58 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ADAMTSL1]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ABCA13]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[LTBP2]] | +0.56 | +0.46 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSDL1]] | -0.44 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[AVPI1]] | -0.44 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[TOM1]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[LSM14B]] | -0.43 | -0.27 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02509]] | C | LINC02509 activity raises CCDC190's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 1.94× lower at baseline in the lines without LINC02509 | 0.005 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises CCDC190's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.39× lower at baseline in the lines without RGS4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[ROBO4]] | C | ROBO4 activity raises CCDC190's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.18× lower at baseline in the lines without ROBO4 | 0.019 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[SPOCD1]] | C | SPOCD1 activity raises CCDC190's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without SPOCD1 | 0.057 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; co-absent with the target |
| [[PSG5]] | C | PSG5 activity raises CCDC190's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 2.74× lower at baseline in the lines without PSG5 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 10, C 19. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGMB]] | B | CCDC190 activity raises RGMB's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.39× lower at baseline in the lines without CCDC190 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[LINC01204]] | B | CCDC190 activity raises LINC01204's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.11× lower at baseline in the lines without CCDC190 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[DELEC1]] | B | CCDC190 activity raises DELEC1's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 1.61× lower at baseline in the lines without CCDC190 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[NAV3]] | B | CCDC190 activity raises NAV3's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.57× lower at baseline in the lines without CCDC190 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[ZPLD1]] | B | CCDC190 activity raises ZPLD1's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 1.75× lower at baseline in the lines without CCDC190 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[PICART1]] | B | CCDC190 activity weakens PICART1's drug response | lines that do not express CCDC190 (31) vs lines expressing it (9) | the lines without CCDC190 respond 0.90× as strongly (z diff +0.04); strongest at Dinaciclib 5 µM: 9.46x vs 2.01x (z diff -4.8) | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; target measured in part of the lines; both ways; artifact flags |
| [[NEMP2]] | B | CCDC190 activity raises NEMP2's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 1.76× lower at baseline in the lines without CCDC190 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[RGMB]] | B | CCDC190 activity weakens RGMB's drug response | lines that do not express CCDC190 (37) vs lines expressing it (10) | the lines without CCDC190 respond 2.37× as strongly (z diff -1.72); strongest at Idarubicin (hydrochloride) 5 µM: 1.86x vs 0.68x (z diff -7.9) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; target measured in part of the lines; artifact flags |
| [[MIR222HG]] | B | CCDC190 activity raises MIR222HG's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 1.49× lower at baseline in the lines without CCDC190 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[CD44]] | B | CCDC190 activity raises CD44's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.99× lower at baseline in the lines without CCDC190 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[RGS4]] | C | CCDC190 activity raises RGS4's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 7.20× lower at baseline in the lines without CCDC190 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[LINC01592]] | C | CCDC190 activity raises LINC01592's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.68× lower at baseline in the lines without CCDC190 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.7, 19.5); signed map (34.8, 29.5). **Vector** length 30.8, 9.96% of its response variance represented; |z| ≥ 3 in 252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +0.8 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.8 | +0.2 |
| fall | [[Triamcinolone (drug)]] 0.5 µM |  | -0.7 | -0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.7 | -0.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.7 | -1.1 |
|  | [[Artesunate (drug)]] 5 µM |  | -0.7 | -3.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.7 | -0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 190 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:162,824,458-162,868,761 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC48998; previously C1orf110 |
| Matched by | ensembl_id |

UniProt [Q86UF4](https://www.uniprot.org/uniprotkb/Q86UF4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28736) · Entrez [339512](https://www.ncbi.nlm.nih.gov/gene/339512) · UniProt [Q86UF4](https://www.uniprot.org/uniprotkb/Q86UF4) · Ensembl [ENSG00000185860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185860)

## Data

Gene col 11741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11741); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11741]; `tensor/DDL_lfc|DDL_z.npy` [11741]; `embed/gene_vectors.npy` [11741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11741 or target_col == 11741). Every well: [[CCDC190 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC190.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
