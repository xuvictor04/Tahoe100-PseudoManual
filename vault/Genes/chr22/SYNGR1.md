---
symbol: "SYNGR1"
type: "gene"
col: 1926
ensembl_id: "ENSG00000100321"
name: "synaptogyrin 1"
location: "22q13.1"
module: 100
arm: "+"
pooled_cpm: 5.61
n_lines_expressing: 38
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 12
direction_downstream: 12
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# SYNGR1

*synaptogyrin 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.24× (z +8.7, q 2e-15, up in 9 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +3.9, q 0.016, up in 15 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 5.68×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 5.77×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 5.23×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -13.4, q 4e-38, down in 26 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMO]] (+0.65, fdr 1e-05), [[P3H3]] (+0.60, fdr 2e-05), [[BCL9]] (+0.60, fdr 3e-05); moves opposite to [[ENOX2]] (-0.51, fdr 4e-05), [[ITPRIPL2]] (-0.50, fdr 4e-05), [[RGS5]] (-0.49, fdr 1e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); 12 go from it, the strongest it → [[CNPY4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1926.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 5.68×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 5.77×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 5.23×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +8.7 | 2e-15 | 9/11 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +8.2 | 6e-14 | 17/23 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.016 | 15/31 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +3.7 | 0.035 | 7/15 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.33× | +3.2 | 0.17 | 6/31 (NCI-H2030, Hs 766T, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1926.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.430×** | -13.4 | 4e-38 | 26/33 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.350×** | -11.8 | 1e-29 | 25/30 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -6.2 | 9e-08 | 21/33 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.582×** | -6.1 | 2e-07 | 15/34 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -6.0 | 2e-07 | 23/35 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -5.7 | 1e-06 | 19/34 (A-427, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.605×** | -5.7 | 1e-06 | 16/34 (LoVo, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.606×** | -5.6 | 1e-06 | 13/35 (SW 900, MIA PaCa-2, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.387×** | -5.5 | 3e-06 | 16/30 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.657×** | -4.7 | 1e-04 | 16/34 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.660×** | -4.7 | 2e-04 | 9/33 (NCI-H460, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.670×** | -4.5 | 3e-04 | 13/35 (SW 900, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.683×** | -4.3 | 8e-04 | 9/34 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.688×** | -4.2 | 0.001 | 12/34 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.779×** | -4.0 | 0.003 | 12/36 (Panc 03.27, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -4.0 | 0.003 | 17/33 (Hs 766T, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.81 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.68× (z +12.8) | — |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.0) |
| [[PANC-1 (line)]] | alt | 5.66 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.3) |
| [[A-172 (line)]] | wt | 6.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -8.7) |
| [[A-427 (line)]] | wt | 9.95 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0822× (z -12.3) |
| [[A549 (line)]] | wt | 4.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -8.6) |
| [[BT-474 (line)]] | alt | 8.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 7.48 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.119× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 5.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0694× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 6.28 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0712× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 6.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0491× (z -10.2) |
| [[A498 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.551 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMO]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[P3H3]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[BCL9]] | +0.60 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[GAMT]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[SLC29A4]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SEPTIN6]] | +0.58 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PDZD7]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CIB2]] | +0.58 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[ZNF483]] | +0.58 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[ZFP14]] | +0.57 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SMARCD3]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[PTK7]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.51 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ITPRIPL2]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[RGS5]] | -0.49 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[DGKH]] | -0.48 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[RFX3-DT]] | -0.48 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[ST7L]] | -0.48 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ETS1]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises SYNGR1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.82× lower at baseline in the lines without SEMA6B | 0.029 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[SV2A]] | B | SV2A activity raises SYNGR1's level | lines that do not express SV2A (17) vs lines expressing it (33) | 2.41× lower at baseline in the lines without SV2A | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000268163, SYT11, SMARCA1; maybe low, not absent |
| [[SMO]] | B | SMO activity raises SYNGR1's level | lines that do not express SMO (17) vs lines expressing it (33) | 2.43× lower at baseline in the lines without SMO | 0.046 | ⚠ within organs, on part of the lines; also absent: RADIL, DUSP9, APBA2 |
| [[SEPTIN5]] | B | SEPTIN5 activity raises SYNGR1's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 2.98× lower at baseline in the lines without SEPTIN5 | 0.073 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[MEOX2]] | B | MEOX2 activity raises SYNGR1's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 2.26× lower at baseline in the lines without MEOX2 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252 |
| [[GAMT]] | C | GAMT activity raises SYNGR1's level | lines that do not express GAMT (11) vs lines expressing it (39) | 3.56× lower at baseline in the lines without GAMT | 0.023 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3; co-absent with the target |
| [[PDZD4]] | C | PDZD4 activity raises SYNGR1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.56× lower at baseline in the lines without PDZD4 | 0.024 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |
| [[TCF7L1]] | C | TCF7L1 activity raises SYNGR1's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 3.52× lower at baseline in the lines without TCF7L1 | 0.054 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A; co-absent with the target |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises SYNGR1's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[RFX3-DT]] | C | RFX3-DT activity raises SYNGR1's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.97× lower at baseline in the lines without RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[CECR2]] | C | CECR2 activity raises SYNGR1's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.69× lower at baseline in the lines without CECR2 | 0.064 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent; co-absent with the target |
| [[TMEM144]] | C | TMEM144 activity lowers SYNGR1's level | lines that do not express TMEM144 (3) vs lines expressing it (47) | 3.15× higher at baseline in the lines without TMEM144 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: WNK4, RNF103-CHMP3, RBMS2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNPY4]] | B | SYNGR1 activity raises CNPY4's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 1.89× lower at baseline in the lines without SYNGR1 | 0.012 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[KANTR]] | B | SYNGR1 activity raises KANTR's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 1.37× lower at baseline in the lines without SYNGR1 | 0.020 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[SMO]] | B | SYNGR1 activity raises SMO's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 3.06× lower at baseline in the lines without SYNGR1 | 0.050 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[HYKK]] | B | SYNGR1 activity raises HYKK's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 1.13× lower at baseline in the lines without SYNGR1 | 0.051 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[TET1]] | B | SYNGR1 activity raises TET1's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 3.01× lower at baseline in the lines without SYNGR1 | 0.064 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[SNTA1]] | B | SYNGR1 activity raises SNTA1's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 2.34× lower at baseline in the lines without SYNGR1 | 0.073 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[SCPEP1]] | B | SYNGR1 activity raises SCPEP1's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 1.81× lower at baseline in the lines without SYNGR1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[SV2A]] | B | SYNGR1 activity raises SV2A's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 2.63× lower at baseline in the lines without SYNGR1 | 0.078 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[TET1]] | B | SYNGR1 activity strengthens TET1's drug response | lines that do not express SYNGR1 (6) vs lines expressing it (30) | the lines without SYNGR1 respond 0.45× as strongly (z diff +2.53); strongest at Homoharringtonine 5 µM: 0.67x vs 0.33x (z diff +4.4) | 0.098 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1; target measured in part of the lines; artifact flags |
| [[TCF7L1]] | C | SYNGR1 activity raises TCF7L1's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 5.49× lower at baseline in the lines without SYNGR1 | 0.017 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1; co-absent with the target |
| [[PDZD4]] | C | SYNGR1 activity raises PDZD4's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 3.41× lower at baseline in the lines without SYNGR1 | 0.017 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1; co-absent with the target |
| [[RAB6B]] | C | SYNGR1 activity raises RAB6B's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 2.86× lower at baseline in the lines without SYNGR1 | 0.059 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1; co-absent with the target |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.3, -5.3); signed map (-29.8, -2.3). **Vector** length 49.0, 8.01% of its response variance represented; |z| ≥ 3 in 619 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -11.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -4.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | synaptogyrin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,349,925-39,385,575 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Synaptogyrins |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O43759](https://www.uniprot.org/uniprotkb/O43759) (Synaptogyrin-1):

> May play a role in regulated exocytosis. Modulates the localization of synaptophysin/SYP into synaptic-like microvesicles and may therefore play a role in synaptic-like microvesicle formation and/or maturation (By similarity). Involved in the regulation of short-term and long-term synaptic plasticity (By similarity).

**Summary**, from NCBI Gene [9145](https://www.ncbi.nlm.nih.gov/gene/9145):

> This gene encodes an integral membrane protein associated with presynaptic vesicles in neuronal cells. The exact function of this protein is unclear, but studies of a similar murine protein suggest that it functions in synaptic plasticity without being required for synaptic transmission. The gene product belongs to the synaptogyrin gene family. Three alternatively spliced variants encoding three different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11498](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11498) · Entrez [9145](https://www.ncbi.nlm.nih.gov/gene/9145) · UniProt [O43759](https://www.uniprot.org/uniprotkb/O43759) · Ensembl [ENSG00000100321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100321)

## Data

Gene col 1926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1926); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1926]; `tensor/DDL_lfc|DDL_z.npy` [1926]; `embed/gene_vectors.npy` [1926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1926 or target_col == 1926). Every well: [[SYNGR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNGR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
