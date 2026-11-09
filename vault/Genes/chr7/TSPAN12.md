---
symbol: "TSPAN12"
type: "gene"
col: 2709
ensembl_id: "ENSG00000106025"
name: "tetraspanin 12"
location: "7q31.31"
module: 9
arm: "+"
pooled_cpm: 6.86
n_lines_expressing: 37
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# TSPAN12

*tetraspanin 12* — 7q31.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.75× (z +17.3, q 0e+00, up in 27 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.677× (z -4.7, q 0.002, down in 18 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.242×; ⚠ cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H23 0.0612×); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.262×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0608×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRMPD3]] (+0.61, fdr 3e-05), [[PITX2]] (+0.59, fdr 3e-05), [[SLC7A8]] (+0.59, fdr 3e-05); moves opposite to [[SETX]] (-0.57, fdr 1e-05), [[IFT43]] (-0.54, fdr 4e-05), [[KATNIP]] (-0.54, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SCIN]] → it (grade B ⚠); 8 go from it, the strongest it → [[HMGN5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2709.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.75×** | +17.3 | 0e+00 | 27/34 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +13.0 | 3e-36 | 20/28 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.70×** | +12.0 | 4e-31 | 26/32 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +11.7 | 2e-29 | 11/20 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +11.0 | 3e-26 | 1/7 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.44×** | +10.8 | 4e-25 | 25/34 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.36×** | +10.4 | 2e-23 | 18/34 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +9.3 | 2e-18 | 18/35 (NCI-H2030, A498, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +8.9 | 3e-17 | 15/23 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +8.0 | 8e-14 | 17/34 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +7.9 | 2e-13 | 5/12 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.91×** | +7.8 | 2e-13 | 17/34 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +6.0 | 7e-08 | 8/24 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.44×** | +5.6 | 7e-07 | 8/31 (A498, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +5.3 | 4e-06 | 7/23 (LOX-IMVI, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.002 | 8/33 (A-427, HCT15, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.002 | 9/34 (SNU-1, SW480, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.012 | 8/34 (LoVo, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.012 | 9/35 (KATO III, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.022 | 8/35 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.053 | 7/34 (HT-29, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.242×; ⚠ cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H23 0.0612×); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.262×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0608×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.677×** | -4.7 | 0.002 | 18/33 (SHP-77, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.756× | -3.3 | 0.23 | 14/33 (BT-474, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adenosine (drug)]] 0.5 µM |  | 0.773× | -3.1 | 0.39 | 5/34 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 54.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.262× (z -9.3) |
| [[A498 (line)]] | wt | 10.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.05× (z +9.3) | — |
| [[KATO III (line)]] | alt | 9.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 9.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 4.21 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0608× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 3.30 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.67× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 6.68 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0612× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 2.70 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.21× (z +8.6) | — |
| [[A-172 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRMPD3]] | +0.61 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[PITX2]] | +0.59 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[SLC7A8]] | +0.59 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[SCIN]] | +0.58 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ATL1]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[GABRA2]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[GUCY1A1]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SPTB]] | +0.54 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SELENOP]] | +0.54 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[GPR63]] | +0.53 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[FAM102B]] | +0.53 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[MIR325HG]] | +0.52 | +0.44 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETX]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[IFT43]] | -0.54 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[KATNIP]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[FAM120B]] | -0.52 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[ATG7]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[GPATCH2L]] | -0.48 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[METTL2B]] | -0.47 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[CRK]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[ACAD9]] | -0.46 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[CCDC57]] | -0.45 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[PIGL]] | -0.45 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[MEF2B]] | -0.45 | -0.33 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCIN]] | B | SCIN activity raises TSPAN12's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without SCIN | 0.057 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[SMPDL3B]] | C | SMPDL3B activity raises TSPAN12's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.40× lower at baseline in the lines without SMPDL3B | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGN5]] | B | TSPAN12 activity raises HMGN5's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without TSPAN12 | 0.014 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| [[GPR63]] | B | TSPAN12 activity raises GPR63's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without TSPAN12 | 0.051 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| [[SLAIN1]] | B | TSPAN12 activity raises SLAIN1's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without TSPAN12 | 0.069 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| [[RNF144B]] | B | TSPAN12 activity raises RNF144B's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 1.36× lower at baseline in the lines without TSPAN12 | 0.074 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| [[SCIN]] | B | TSPAN12 activity raises SCIN's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 2.15× lower at baseline in the lines without TSPAN12 | 0.084 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| cells under [[Furosemide (drug)]] 0.5 µM | B | TSPAN12 activity raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | lines that do not express TSPAN12 (13) vs lines expressing it (35) | the lines without TSPAN12: 0.87× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| [[SMPDL3B]] | C | TSPAN12 activity raises SMPDL3B's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 2.38× lower at baseline in the lines without TSPAN12 | 0.056 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent; co-absent with the target |
| [[ATP8A1]] | C | TSPAN12 activity raises ATP8A1's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 2.70× lower at baseline in the lines without TSPAN12 | 0.068 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.437). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.1, 48.3); signed map (52.6, 1.0). **Vector** length 60.3, 11.4% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +17.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +5.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.31 — chr7:120,787,320-120,858,402 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NET-2; previously TM4SF12 |
| Gene groups (HGNC) | Tetraspanin family |
| Matched by | ensembl_id |

**Function**, from UniProt [O95859](https://www.uniprot.org/uniprotkb/O95859) (Tetraspanin-12):

> Regulator of cell surface receptor signal transduction. Plays a central role in retinal vascularization by regulating norrin (NDP) signal transduction. Acts in concert with norrin (NDP) to promote FZD4 multimerization and subsequent activation of FZD4, leading to promote accumulation of beta-catenin (CTNNB1) and stimulate LEF/TCF-mediated transcriptional programs. Suprisingly, it only activates the norrin (NDP)-dependent activation of FZD4, while it does not activate the Wnt-dependent …

**Summary**, from NCBI Gene [23554](https://www.ncbi.nlm.nih.gov/gene/23554):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21641) · Entrez [23554](https://www.ncbi.nlm.nih.gov/gene/23554) · UniProt [O95859](https://www.uniprot.org/uniprotkb/O95859) · Ensembl [ENSG00000106025](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106025)

## Data

Gene col 2709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2709); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2709]; `tensor/DDL_lfc|DDL_z.npy` [2709]; `embed/gene_vectors.npy` [2709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2709 or target_col == 2709). Every well: [[TSPAN12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
