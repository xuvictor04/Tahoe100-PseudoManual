---
symbol: "HOXC9"
type: "gene"
col: 11132
ensembl_id: "ENSG00000180806"
name: "homeobox C9"
location: "12q13.13"
module: 46
arm: "+"
pooled_cpm: 12.48
n_lines_expressing: 40
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# HOXC9

*homeobox C9* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +17.9, q 0e+00, up in 31 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (PANC-1 3.05×, A498 4.86×, BT-474 4.12×, AsPC-1 3.67×, …); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.09×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (PANC-1 2.59×; ⚠ cell-cycle shift, explains ~5% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 1.93×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.349× (z -15.6, q 0e+00, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXC8]] (+0.78, fdr 7e-06, ⚠ same locus), [[HOXC6]] (+0.72, fdr 7e-06, ⚠ same locus), [[HOXB7]] (+0.68, fdr 3e-04), [[LINC00938]] (+0.68, fdr 3e-05), [[TSTD3]] (+0.66, fdr 1e-04); moves opposite to [[DNAJB1]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HOXC10]] → it (grade B ⚠); 6 go from it, the strongest it → [[KMT2E-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11132.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (PANC-1 3.05×, A498 4.86×, BT-474 4.12×, AsPC-1 3.67×, …); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.09×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (PANC-1 2.59×; ⚠ cell-cycle shift, explains ~5% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 1.93×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +17.9 | 0e+00 | 31/34 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +6.3 | 1e-07 | 18/32 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.7 | 6e-04 | 14/35 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.1 | 0.007 | 10/29 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.5 | 0.050 | 7/22 (SW480, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.36× | +3.3 | 0.11 | 9/35 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.25× | +3.0 | 0.18 | 8/22 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD-7648 (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.18 | 4/36 (PANC-1, C-33 A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.349×** | -15.6 | 0e+00 | 29/38 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.375×** | -14.5 | 3e-45 | 27/37 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.451×** | -11.8 | 1e-29 | 26/37 (C-33 A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.718×** | -6.9 | 8e-10 | 21/37 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.678×** | -5.7 | 1e-06 | 20/38 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.723×** | -4.8 | 2e-04 | 14/36 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.728×** | -4.4 | 8e-04 | 13/36 (SW 900, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.743×** | -4.4 | 8e-04 | 16/37 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.748×** | -4.3 | 0.001 | 14/35 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.603×** | -3.9 | 0.005 | 12/36 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.772×** | -3.8 | 0.007 | 11/37 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -3.7 | 0.011 | 2/38 (AsPC-1, SNU-1) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.849× | -3.4 | 0.028 | 12/37 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.657×** | -3.2 | 0.049 | 13/37 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.1 | 4 (2 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +16.2) | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -15.0) |
| [[SW480 (line)]] | alt | 19.4 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.9) |
| [[AN3 CA (line)]] | alt | 78.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0907× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.174× (z -9.3) |
| [[C-33 A (line)]] | alt | 67.5 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.127× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 19.0 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.139× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -14.4) |
| [[BT-474 (line)]] | alt | 25.4 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +13.0) | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -11.8) |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 32.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -10.3) |
| [[SW48 (line)]] | wt | 14.3 | 0 | 2 | — | [[LJI308 (drug)]] 0.05 µM 0.0375× (z -12.5) |
| [[A498 (line)]] | wt | 8.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.86× (z +14.1) | — |
| [[A549 (line)]] | wt | 4.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.67× (z +9.8) | — |
| [[C32 (line)]] | wt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 8.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.2) |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -9.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 7.56 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -9.3) |
| [[KATO III (line)]] | alt | 21.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0868× (z -11.2) |
| [[A-172 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 18 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXC8]] | +0.78 | +0.69 / +0.70 | both halves | 7e-06 | same gene group; STRING 883; ⚠ same locus (5.6 kb, same strand: neighbours can correlate without regulation) |
| [[HOXC6]] | +0.72 | +0.59 / +0.65 | both halves | 7e-06 | same gene group; STRING 999; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB7]] | +0.68 | +0.28 / +0.62 | both halves | 3e-04 | same gene group; STRING 688 |
| [[LINC00938]] | +0.68 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[TSTD3]] | +0.66 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[HOXB-AS3]] | +0.64 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[ACOT2]] | +0.63 | +0.29 / +0.55 | both halves | 3e-04 |  |
| [[SETD1B]] | +0.63 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[HOXC10]] | +0.63 | +0.54 / +0.69 | both halves | 1e-05 | same gene group; STRING 900; ⚠ same locus (4.6 kb, same strand: neighbours can correlate without regulation) |
| [[SPEN-AS1]] | +0.62 | +0.29 / +0.48 | both halves | 3e-04 |  |
| [[C3orf38]] | +0.60 | +0.26 / +0.48 | both halves | 4e-04 |  |
| [[SPESP1]] | +0.60 | +0.28 / +0.42 | both halves | 3e-04 |  |
| [[SHOX2]] | +0.60 | +0.35 / +0.48 | both halves | 1e-04 | STRING 541 |
| [[HOXB6]] | +0.59 | +0.35 / +0.57 | both halves | 1e-04 | same gene group; STRING 630 |
| [[CARNMT1-AS1]] | +0.59 | +0.25 / +0.44 | both halves | 4e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB1]] | -0.52 | -0.41 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC10]] | B | HOXC10 activity raises HOXC9's level | lines that do not express HOXC10 (26) vs lines expressing it (24) | 3.16× lower at baseline in the lines without HOXC10 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: NTRK3, CES1, POTEE |
| [[KCNG1]] | B | KCNG1 activity raises HOXC9's level | lines that do not express KCNG1 (18) vs lines expressing it (32) | 2.96× lower at baseline in the lines without KCNG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |
| [[ZIC2]] | B | ZIC2 activity raises HOXC9's level | lines that do not express ZIC2 (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without ZIC2 | 0.060 | ⚠ within organs, on part of the lines; also absent: FOXD1, BEND7 |
| [[HOXA3]] | B | HOXA3 activity raises HOXC9's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.92× lower at baseline in the lines without HOXA3 | 0.078 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[HOXC6]] | C | HOXC6 activity raises HOXC9's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 4.24× lower at baseline in the lines without HOXC6 | 0.003 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent; co-absent with the target |
| [[HOXC8]] | C | HOXC8 activity raises HOXC9's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 3.76× lower at baseline in the lines without HOXC8 | 0.012 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KMT2E-AS1]] | B | HOXC9 activity raises KMT2E-AS1's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 1.18× lower at baseline in the lines without HOXC9 | 0.044 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2 |
| [[SLC12A9]] | B | HOXC9 activity raises SLC12A9's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 1.34× lower at baseline in the lines without HOXC9 | 0.078 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2 |
| [[HOXC10]] | B | HOXC9 activity raises HOXC10's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 3.92× lower at baseline in the lines without HOXC9 | 0.081 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2 |
| [[KCNG1]] | B | HOXC9 activity raises KCNG1's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 2.71× lower at baseline in the lines without HOXC9 | 0.093 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2 |
| [[HOXC8]] | C | HOXC9 activity raises HOXC8's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 3.67× lower at baseline in the lines without HOXC9 | 0.011 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2; co-absent with the target |
| [[HOXC6]] | C | HOXC9 activity raises HOXC6's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 3.49× lower at baseline in the lines without HOXC9 | 0.029 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2; co-absent with the target |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.5, 25.0); signed map (25.8, -15.0). **Vector** length 67.0, 12.0% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +17.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +1.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -15.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -14.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | -11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | homeobox C9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,994,895-54,003,337 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX3, HOX3B |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P31274](https://www.uniprot.org/uniprotkb/P31274) (Homeobox protein Hox-C9):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3225](https://www.ncbi.nlm.nih.gov/gene/3225):

> This gene belongs to the homeobox family of genes. The homeobox genes encode a highly conserved family of transcription factors that play an important role in morphogenesis in all multicellular organisms. Mammals possess four similar homeobox gene clusters, HOXA, HOXB, HOXC and HOXD, which are located on different chromosomes and consist of 9 to 11 genes arranged in tandem. This gene is one of several homeobox HOXC genes located in a cluster on chromosome 12. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5130](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5130) · Entrez [3225](https://www.ncbi.nlm.nih.gov/gene/3225) · UniProt [P31274](https://www.uniprot.org/uniprotkb/P31274) · Ensembl [ENSG00000180806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180806)

## Data

Gene col 11132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11132); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11132]; `tensor/DDL_lfc|DDL_z.npy` [11132]; `embed/gene_vectors.npy` [11132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11132 or target_col == 11132). Every well: [[HOXC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
