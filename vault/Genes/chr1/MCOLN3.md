---
symbol: "MCOLN3"
type: "gene"
col: 629
ensembl_id: "ENSG00000055732"
name: "mucolipin TRP cation channel 3"
location: "1p22.3"
module: 124
arm: "+"
pooled_cpm: 8.76
n_lines_expressing: 32
n_dd_up: 36
n_dd_down: 4
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# MCOLN3

*mucolipin TRP cation channel 3* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.39× (z +16.2, q 0e+00, up in 16 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.584× (z -7.1, q 1e-09, down in 18 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (Panc 03.27 0.225×, SW480 0.192×, LoVo 0.251×, A-427 0.281×; ⚠ cell-cycle shift, explains ~28% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.207×, SW480 0.167×, Panc 03.27 0.281×; ⚠ cell-cycle shift, explains ~33% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.169×, RKO 0.385×); [[Naproxen (drug)]] 0.05 µM in 1 line (SW48 0.0618×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.124×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLXNC1]] (+0.64, fdr 1e-05), [[ABRACL]] (+0.61, fdr 4e-04), [[HPS1]] (+0.61, fdr 3e-05); moves opposite to [[BLTP2]] (-0.54, fdr 1e-04), [[PHF12]] (-0.54, fdr 6e-05), [[KIAA1328]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MRAS]] → it (grade B ⚠); 7 go from it, the strongest it → [[BEND7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.39×** | +16.2 | 0e+00 | 16/26 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.83×** | +13.7 | 6e-40 | 21/27 (RKO, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +13.2 | 3e-37 | 6/13 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +9.7 | 5e-20 | 13/27 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +7.5 | 6e-12 | 13/28 (LoVo, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +7.5 | 8e-12 | 15/27 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +7.4 | 1e-11 | 11/28 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.22×** | +7.4 | 1e-11 | 15/27 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +6.7 | 2e-09 | 8/17 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +6.3 | 1e-08 | 13/29 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.1 | 6e-08 | 8/23 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.1 | 6e-08 | 10/26 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +5.7 | 4e-07 | 17/29 (LoVo, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +5.5 | 1e-06 | 13/29 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.5 | 3e-04 | 12/24 (A-427, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.39×** | +4.3 | 5e-04 | 7/28 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.003 | 9/29 (LoVo, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.003 | 7/28 (LoVo, A-427, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.009 | 4/28 (SW480, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.012 | 10/28 (HCT15, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 629.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (Panc 03.27 0.225×, SW480 0.192×, LoVo 0.251×, A-427 0.281×; ⚠ cell-cycle shift, explains ~28% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.207×, SW480 0.167×, Panc 03.27 0.281×; ⚠ cell-cycle shift, explains ~33% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.169×, RKO 0.385×); [[Naproxen (drug)]] 0.05 µM in 1 line (SW48 0.0618×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.124×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.584×** | -7.1 | 1e-09 | 18/28 (Panc 03.27, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.643×** | -5.8 | 2e-06 | 16/28 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.656×** | -5.5 | 6e-06 | 16/29 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -5.0 | 9e-05 | 11/27 (HEC-1-A, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Pentagastrin (drug)]] 5 µM |  | 0.842× | -3.2 | 0.16 | 2/30 (SW 900, SK-MEL-2) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.7 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 21.6 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 6.49× (z +9.9) | [[PF-06260933 (drug)]] 5 µM 0.0458× (z -8.6) |
| [[LoVo (line)]] | wt | 20.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -11.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 22.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -9.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 24.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 38.9 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.56× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.0) |
| [[SW48 (line)]] | wt | 27.9 | 0 | 2 | — | [[Naproxen (drug)]] 0.05 µM 0.0618× (z -12.9) |
| [[A498 (line)]] | wt | 5.05 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.455× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 3.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 5.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.32× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +9.1) | — |
| [[A-172 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.759 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.894 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.910 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.644 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNC1]] | +0.64 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ABRACL]] | +0.61 | +0.62 / +0.25 | both halves | 4e-04 |  |
| [[HPS1]] | +0.61 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[HACD1]] | +0.60 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[STX3]] | +0.59 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[GNPDA1]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[LGALSL-DT]] | +0.59 | +0.53 / +0.31 | both halves | 2e-04 |  |
| [[ZFPM2]] | +0.58 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[UST]] | +0.58 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[TMEM192]] | +0.58 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[RRAGC-DT]] | +0.58 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[MAFG]] | +0.57 | +0.44 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLTP2]] | -0.54 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[PHF12]] | -0.54 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[KIAA1328]] | -0.53 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[SLC25A11]] | -0.53 | -0.44 / -0.22 | both halves | 6e-04 |  |
| [[SLX4]] | -0.53 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[METTL26]] | -0.52 | -0.53 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[TSFM]] | -0.51 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[CABIN1]] | -0.51 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[NHP2]] | -0.51 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[NOMO3]] | -0.50 | -0.38 / -0.28 | both halves | 3e-04 |  |
| [[CETN2]] | -0.50 | -0.26 / -0.26 | both halves | 4e-04 |  |
| [[STUB1]] | -0.49 | -0.36 / -0.13 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRAS]] | B | MRAS activity raises MCOLN3's level | lines that do not express MRAS (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without MRAS | 0.007 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[BEND7]] | B | BEND7 activity raises MCOLN3's level | lines that do not express BEND7 (12) vs lines expressing it (38) | 1.88× lower at baseline in the lines without BEND7 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZIC2 |
| [[HDAC6]] | B | HDAC6 activity raises MCOLN3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEND7]] | B | MCOLN3 activity raises BEND7's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 2.39× lower at baseline in the lines without MCOLN3 | 0.013 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[RAB29]] | B | MCOLN3 activity raises RAB29's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without MCOLN3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[IL27RA]] | B | MCOLN3 activity raises IL27RA's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without MCOLN3 | 0.043 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[FAM149A]] | B | MCOLN3 activity raises FAM149A's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 2.05× lower at baseline in the lines without MCOLN3 | 0.056 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[MRAS]] | B | MCOLN3 activity raises MRAS's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without MCOLN3 | 0.058 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[ITSN2]] | B | MCOLN3 activity raises ITSN2's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 1.28× lower at baseline in the lines without MCOLN3 | 0.075 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[XKR4]] | B | MCOLN3 activity lowers XKR4's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 1.12× higher at baseline in the lines without MCOLN3 | 0.096 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (18.4, 13.8); signed map (40.3, -17.2). **Vector** length 63.3, 14.4% of its response variance represented; |z| ≥ 3 in 549 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +3.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.9 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | -7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.7 | -5.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | mucolipin TRP cation channel 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:85,018,082-85,048,500 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRPML3, FLJ11006, TRP-ML3 |
| Gene groups (HGNC) | Mucolipin TRP cation channel family |
| Reactome | 4 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDD5](https://www.uniprot.org/uniprotkb/Q8TDD5) (Mucolipin-3):

> Nonselective cation channel probably playing a role in the regulation of membrane trafficking events. Acts as a Ca(2+)-permeable cation channel with inwardly rectifying activity. Mediates release of Ca(2+) from endosomes to the cytoplasm, contributes to endosomal acidification and is involved in the regulation of membrane trafficking and fusion in the endosomal pathway. Also permeable to Mg(2+), Na(+) and K(+) (By similarity). Does not seem to act as mechanosensory transduction channel in inner …

**Summary**, from NCBI Gene [55283](https://www.ncbi.nlm.nih.gov/gene/55283):

> This gene encodes one of members of the mucolipin cation channel proteins. Mutation studies of the highly similar protein in mice have shown that the protein is found in cochlea hair cells, and mutant mice show early-onset hearing loss and balance problems. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:13358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13358) · Entrez [55283](https://www.ncbi.nlm.nih.gov/gene/55283) · UniProt [Q8TDD5](https://www.uniprot.org/uniprotkb/Q8TDD5) · Ensembl [ENSG00000055732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055732)

## Data

Gene col 629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 629); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 629]; `tensor/DDL_lfc|DDL_z.npy` [629]; `embed/gene_vectors.npy` [629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 629 or target_col == 629). Every well: [[MCOLN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCOLN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
