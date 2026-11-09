---
symbol: "FGFR4"
type: "gene"
col: 8389
ensembl_id: "ENSG00000160867"
name: "fibroblast growth factor receptor 4"
location: "5q35.2"
module: 44
arm: "+"
pooled_cpm: 5.25
n_lines_expressing: 39
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 19
direction_downstream: 12
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# FGFR4

*fibroblast growth factor receptor 4* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.71× (z +19.8, q 0e+00, up in 33 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.644× (z -5.0, q 3e-04, down in 13 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.105×; ⚠ cell-cycle shift, explains ~11% of this change); [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (PANC-1 0.163×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.231×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA4G]] (+0.69, fdr 7e-06), [[CKMT1B]] (+0.66, fdr 1e-05), [[PRR5]] (+0.64, fdr 2e-05); moves opposite to [[ANKRD17-DT]] (-0.54, fdr 8e-05), [[DNAI4]] (-0.52, fdr 1e-04), [[RAB30-DT]] (-0.52, fdr 2e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[CKMT1B]] → it (grade B ⚠); 12 go from it, the strongest it → [[LMTK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.71×** | +19.8 | 0e+00 | 33/35 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.75×** | +17.7 | 0e+00 | 32/34 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.84×** | +11.9 | 3e-30 | 26/35 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +11.2 | 9e-27 | 5/7 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +10.9 | 9e-26 | 15/17 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +10.6 | 3e-24 | 12/28 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +9.9 | 4e-21 | 18/33 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +8.9 | 4e-17 | 9/12 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.16×** | +8.7 | 1e-16 | 22/35 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +7.6 | 2e-12 | 7/20 (HT-29, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +7.4 | 1e-11 | 15/31 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +6.9 | 2e-10 | 17/35 (NCI-H1573, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +6.0 | 1e-07 | 14/34 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +5.5 | 1e-06 | 6/29 (SK-MEL-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.38×** | +5.1 | 1e-05 | 8/31 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +4.4 | 4e-04 | 14/30 (NCI-H1573, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.003 | 12/28 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.010 | 3/35 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.80×** | +3.5 | 0.013 | 7/23 (HEC-1-A, A498, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8389.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.105×; ⚠ cell-cycle shift, explains ~11% of this change); [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (PANC-1 0.163×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.231×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.644×** | -5.0 | 3e-04 | 13/35 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.723×** | -3.7 | 0.057 | 15/33 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.825× | -3.1 | 0.28 | 9/35 (HT-29, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.764× | -3.1 | 0.28 | 10/32 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 32.7 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.231× (z -8.7) |
| [[KATO III (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -10.3) ⚠ cell-cycle shift, explains ~11% of this change |
| [[PANC-1 (line)]] | alt | 1.94 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.163× (z -9.0) |
| [[A-172 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.934 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.748 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4G]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[CKMT1B]] | +0.66 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PRR5]] | +0.64 | +0.46 / +0.55 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |
| [[CKMT1A]] | +0.64 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[AZGP1]] | +0.62 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[PCSK9]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[GLB1L2]] | +0.61 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[AIF1L]] | +0.60 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[VASH2]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PODXL2]] | +0.59 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[PADI2]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[FCHO1]] | +0.58 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD17-DT]] | -0.54 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[DNAI4]] | -0.52 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[RAB30-DT]] | -0.52 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[HEXIM2-AS1]] | -0.51 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[N4BP2]] | -0.51 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[CHD1-DT]] | -0.50 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[PPP1R12A-AS2]] | -0.50 | -0.31 / -0.29 | both halves | 3e-04 |  |
| [[CCDC122]] | -0.49 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[LINC01004]] | -0.49 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[NIFK-AS1]] | -0.49 | -0.40 / -0.24 | both halves | 5e-04 |  |
| [[XPC]] | -0.48 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[RO60]] | -0.48 | -0.41 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 15, C 4. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CKMT1B]] | B | CKMT1B activity raises FGFR4's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without CKMT1B | 0.003 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[CKMT1A]] | B | CKMT1A activity raises FGFR4's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without CKMT1A | 0.013 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM |
| [[YBX2]] | B | YBX2 activity raises FGFR4's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without YBX2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[SMPDL3B]] | B | SMPDL3B activity raises FGFR4's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.08× lower at baseline in the lines without SMPDL3B | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[LMTK3]] | B | LMTK3 activity raises FGFR4's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.78× lower at baseline in the lines without LMTK3 | 0.038 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[PIK3AP1]] | B | PIK3AP1 activity raises FGFR4's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without PIK3AP1 | 0.040 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139 |
| [[ARHGAP8]] | B | ARHGAP8 activity raises FGFR4's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without ARHGAP8 | 0.058 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[TESC]] | B | TESC activity raises FGFR4's level | lines that do not express TESC (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without TESC | 0.060 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[SLC29A2]] | B | SLC29A2 activity raises FGFR4's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without SLC29A2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[ESPN]] | B | ESPN activity raises FGFR4's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.55× lower at baseline in the lines without ESPN | 0.060 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[STXBP6]] | B | STXBP6 activity raises FGFR4's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without STXBP6 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[LARGE2]] | B | LARGE2 activity raises FGFR4's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 1.69× lower at baseline in the lines without LARGE2 | 0.074 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | FGFR4 activity raises LMTK3's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 2.84× lower at baseline in the lines without FGFR4 | 0.011 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[RHPN1]] | B | FGFR4 activity raises RHPN1's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 2.25× lower at baseline in the lines without FGFR4 | 0.015 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[MARVELD2]] | B | FGFR4 activity raises MARVELD2's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 2.84× lower at baseline in the lines without FGFR4 | 0.044 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[FCHO1]] | B | FGFR4 activity raises FCHO1's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without FGFR4 | 0.060 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[MATCAP1]] | B | FGFR4 activity lowers MATCAP1's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 1.18× higher at baseline in the lines without FGFR4 | 0.072 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[SLC29A2]] | B | FGFR4 activity raises SLC29A2's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 2.58× lower at baseline in the lines without FGFR4 | 0.073 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[MYORG]] | B | FGFR4 activity raises MYORG's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without FGFR4 | 0.075 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[TMEM63C]] | B | FGFR4 activity raises TMEM63C's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 1.92× lower at baseline in the lines without FGFR4 | 0.094 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[CISD3]] | B | FGFR4 activity raises CISD3's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without FGFR4 | 0.096 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[MCF2L]] | C | FGFR4 activity raises MCF2L's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 3.47× lower at baseline in the lines without FGFR4 | 0.055 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent; co-absent with the target |
| [[ENTPD2]] | C | FGFR4 activity raises ENTPD2's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 2.68× lower at baseline in the lines without FGFR4 | 0.061 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent; co-absent with the target |
| [[MLXIPL]] | C | FGFR4 activity raises MLXIPL's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 2.81× lower at baseline in the lines without FGFR4 | 0.098 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.436). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.6, 43.7); signed map (-23.8, 37.6). **Vector** length 58.4, 10.4% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +9.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +19.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -2.9 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor receptor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:177,086,905-177,098,144 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JTK2, CD334, TKF |
| Gene groups (HGNC) | CD molecules; I-set domain containing; Fibroblast growth factor receptor family |
| Reactome | 29 pathways, smallest: FGFR4 ligand binding and activation; Phospholipase C-mediated cascade; FGFR4; Signaling by FGFR4 in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [P22455](https://www.uniprot.org/uniprotkb/P22455) (Fibroblast growth factor receptor 4):

> Tyrosine-protein kinase that acts as a cell-surface receptor for fibroblast growth factors and plays a role in the regulation of cell proliferation, differentiation and migration, and in regulation of lipid metabolism, bile acid biosynthesis, glucose uptake, vitamin D metabolism and phosphate homeostasis. Required for normal down-regulation of the expression of CYP7A1, the rate-limiting enzyme in bile acid synthesis, in response to FGF19. Phosphorylates PLCG1 and FRS2. Ligand binding leads to …

**Summary**, from NCBI Gene [2264](https://www.ncbi.nlm.nih.gov/gene/2264):

> The protein encoded by this gene is a tyrosine kinase and cell surface receptor for fibroblast growth factors. The encoded protein is involved in the regulation of several pathways, including cell proliferation, cell differentiation, cell migration, lipid metabolism, bile acid biosynthesis, vitamin D metabolism, glucose uptake, and phosphate homeostasis. This protein consists of an extracellular region, composed of three immunoglobulin-like domains, a single hydrophobic membrane-spanning …

**Accessions** — [HGNC:3691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3691) · Entrez [2264](https://www.ncbi.nlm.nih.gov/gene/2264) · UniProt [P22455](https://www.uniprot.org/uniprotkb/P22455) · Ensembl [ENSG00000160867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160867)

## Data

Gene col 8389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8389); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8389]; `tensor/DDL_lfc|DDL_z.npy` [8389]; `embed/gene_vectors.npy` [8389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8389 or target_col == 8389). Every well: [[FGFR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGFR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
