---
symbol: "ID2-AS1"
type: "gene"
col: 13997
ensembl_id: "ENSG00000235092"
name: "ID2 antisense RNA 1"
location: "2p25.1"
module: 10
arm: "+"
pooled_cpm: 2.6
n_lines_expressing: 42
n_dd_up: 38
n_dd_down: 12
n_dd_up_clean: 30
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 9
direction_downstream: 18
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ID2-AS1

*ID2 antisense RNA 1* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.88× (z +11.6, q 3e-28, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.40× (z +11.0, q 1e-25, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.402× (z -8.1, q 4e-13, down in 21 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSPOP]] (+0.67, fdr 7e-06), [[LRRIQ3]] (+0.65, fdr 7e-06), [[PACRG]] (+0.63, fdr 7e-06); moves opposite to [[SLC30A6]] (-0.58, fdr 3e-05), [[RABEPK]] (-0.50, fdr 8e-05), [[KNOP1]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LNC-LBCS]] → it (grade B ⚠); 18 go from it, the strongest it → [[TTC30A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.88×** | +11.6 | 3e-28 | 2/2 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +11.0 | 1e-25 | 16/23 (SW1417, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +9.7 | 4e-20 | 2/4 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +8.1 | 1e-13 | 7/9 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.30×** | +7.4 | 2e-11 | 22/38 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +7.1 | 1e-10 | 17/37 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +7.0 | 2e-10 | 15/35 (A498, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +6.5 | 6e-09 | 18/33 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +5.4 | 5e-06 | 16/33 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +5.0 | 3e-05 | 5/18 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.73×** | +4.9 | 5e-05 | 7/21 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +4.7 | 1e-04 | 9/25 (HepG2/C3A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.63×** | +4.4 | 5e-04 | 11/29 (HepG2/C3A, NCI-H2030, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 7e-04 | 9/31 (NCI-H23, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +4.3 | 7e-04 | 9/29 (HEC-1-A, C-33 A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.60×** | +4.0 | 0.002 | 11/27 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.003 | 10/28 (KATO III, HOP62, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.38×** | +3.9 | 0.003 | 7/36 (SW480, HepG2/C3A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13997.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.402×** | -8.1 | 4e-13 | 21/33 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -6.4 | 4e-08 | 20/38 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.488×** | -6.4 | 4e-08 | 19/29 (NCI-H1573, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.499×** | -6.2 | 1e-07 | 15/30 (NCI-H1573, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.510×** | -5.6 | 2e-06 | 15/24 (A-427, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.531×** | -5.6 | 2e-06 | 17/27 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.557×** | -5.2 | 2e-05 | 13/35 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.685×** | -4.7 | 2e-04 | 13/32 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.421×** | -4.0 | 0.004 | 9/23 (PANC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.661×** | -3.7 | 0.015 | 8/35 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.575×** | -3.5 | 0.024 | 11/37 (SNU-423, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -3.2 | 0.057 | 12/35 (A549, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Rutin (trihydrate) (drug)]] 5 µM |  | 0.699× | -3.0 | 0.10 | 7/28 (HOP62, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 7.12 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0618× (z -10.9) |
| [[A-427 (line)]] | wt | 11.6 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.154× (z -9.0) |
| [[A549 (line)]] | wt | 6.70 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0463× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 5.58 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0309× (z -11.2) |
| [[A-172 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.690 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.658 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSPOP]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[LRRIQ3]] | +0.65 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[PACRG]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[LINC01569]] | +0.63 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[AJUBA-DT]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[FAM66C]] | +0.61 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[ZMAT1]] | +0.60 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[PPEF1]] | +0.59 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[LINC02175]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ERICH6-AS1]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 | same gene group |
| [[FBXO15]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[DUSP19]] | +0.58 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A6]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[RABEPK]] | -0.50 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[KNOP1]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[PIGU]] | -0.49 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[FAM120B]] | -0.49 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[ORC3]] | -0.47 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[DAP3]] | -0.47 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[GPR89A]] | -0.47 | -0.56 / -0.29 | both halves | 3e-04 |  |
| [[IQCB1]] | -0.47 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[ERI3]] | -0.47 | -0.57 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LNC-LBCS]] | B | LNC-LBCS activity raises ID2-AS1's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without LNC-LBCS | 0.006 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[JPH3]] | B | JPH3 activity raises ID2-AS1's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 1.92× lower at baseline in the lines without JPH3 | 0.010 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |
| [[LINC02269]] | B | LINC02269 activity raises ID2-AS1's level | lines that do not express LINC02269 (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without LINC02269 | 0.055 | ⚠ within organs, on part of the lines; also absent: HAND2-AS1, C19orf81, TUSC3; maybe low, not absent |
| [[CHGB]] | B | CHGB activity raises ID2-AS1's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.10× lower at baseline in the lines without CHGB | 0.058 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[LRIG3-DT]] | B | LRIG3-DT activity raises ID2-AS1's level | lines that do not express LRIG3-DT (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without LRIG3-DT | 0.082 | ⚠ within organs, on part of the lines; also absent: LRIG3, MID1, CPEB2; maybe low, not absent |
| [[TTC30A]] | B | TTC30A activity raises ID2-AS1's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without TTC30A | 0.083 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |
| [[MIR1915HG]] | B | MIR1915HG activity raises ID2-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without MIR1915HG | 0.095 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[RDM1P5]] | C | RDM1P5 activity raises ID2-AS1's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without RDM1P5 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent; co-absent with the target |
| [[ID2]] | C | ID2 activity raises ID2-AS1's level | lines that do not express ID2 (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without ID2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GAL3ST1, ID2-AS1, MYO15B; co-absent with the target; its own permutation p |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 16, C 2. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC30A]] | B | ID2-AS1 activity raises TTC30A's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without ID2-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[LINC00205]] | B | ID2-AS1 activity raises LINC00205's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.70× lower at baseline in the lines without ID2-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[TMEM198B]] | B | ID2-AS1 activity raises TMEM198B's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without ID2-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[SLC30A6]] | B | ID2-AS1 activity raises SLC30A6's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without ID2-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[PRRT2]] | B | ID2-AS1 activity raises PRRT2's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.86× lower at baseline in the lines without ID2-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[ACKR2]] | B | ID2-AS1 activity raises ACKR2's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without ID2-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[IL11RA]] | B | ID2-AS1 activity raises IL11RA's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without ID2-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[DRAIC]] | B | ID2-AS1 activity raises DRAIC's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without ID2-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[ZNF48]] | B | ID2-AS1 activity raises ZNF48's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without ID2-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[PACRG]] | B | ID2-AS1 activity raises PACRG's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without ID2-AS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[KSR2]] | B | ID2-AS1 activity raises KSR2's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 2.79× lower at baseline in the lines without ID2-AS1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[LNC-LBCS]] | B | ID2-AS1 activity raises LNC-LBCS's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 3.18× lower at baseline in the lines without ID2-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.3, 29.0); signed map (36.7, -7.9). **Vector** length 46.1, 7.35% of its response variance represented; |z| ≥ 3 in 806 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +4.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -6.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -6.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -3.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ID2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p25.1 — chr2:8,666,636-8,681,864 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51103) · Entrez [100506299](https://www.ncbi.nlm.nih.gov/gene/100506299) · Ensembl [ENSG00000235092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235092)

## Data

Gene col 13997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13997); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13997]; `tensor/DDL_lfc|DDL_z.npy` [13997]; `embed/gene_vectors.npy` [13997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13997 or target_col == 13997). Every well: [[ID2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ID2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
