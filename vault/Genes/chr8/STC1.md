---
symbol: "STC1"
type: "gene"
col: 8224
ensembl_id: "ENSG00000159167"
name: "stanniocalcin 1"
location: "8p21.2"
module: 81
arm: "+"
pooled_cpm: 349.08
n_lines_expressing: 26
n_dd_up: 10
n_dd_down: 56
n_dd_up_clean: 8
n_dd_down_clean: 48
in_vector_space: true
direction_upstream: 28
direction_downstream: 47
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# STC1

*stanniocalcin 1* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.98× (z +9.1, q 4e-17, up in 20 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 56 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.301× (z -15.9, q 0e+00, down in 23 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM158]] (+0.79, fdr 7e-06), [[BCL2A1]] (+0.76, fdr 7e-06), [[SGIP1]] (+0.75, fdr 7e-06); moves opposite to [[MGST1]] (-0.57, fdr 2e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[TPBG]] → it (grade B ⚠); 47 go from it, the strongest it → [[ENTPD7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +9.1 | 4e-17 | 20/24 (A-172, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +6.5 | 3e-08 | 20/25 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +5.5 | 7e-06 | 19/24 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +4.9 | 1e-04 | 15/24 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.47×** | +3.7 | 0.025 | 6/24 (A498, A-172, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.029 | 19/25 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.029 | 5/24 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.029 | 18/24 (SHP-77, Hs 766T, …) | rises with dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.033 | 20/24 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.39×** | +3.2 | 0.088 | 3/25 (RKO, A498, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | 1.38× | +3.1 | 0.12 | 16/24 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 8 with an alert ⚠; shown: the 15 strongest. 56 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.301×** | -15.9 | 0e+00 | 23/24 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.295×** | -10.9 | 3e-25 | 25/26 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.511×** | -8.6 | 2e-15 | 23/24 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.373×** | -8.5 | 2e-15 | 24/24 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.424×** | -8.0 | 1e-13 | 22/24 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.416×** | -7.9 | 3e-13 | 24/24 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.442×** | -7.6 | 2e-12 | 23/23 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.512×** | -7.6 | 3e-12 | 24/24 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.434×** | -7.5 | 4e-12 | 23/23 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.463×** | -7.3 | 2e-11 | 23/25 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.466×** | -7.1 | 5e-11 | 24/25 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.477×** | -6.7 | 1e-09 | 20/24 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.533×** | -5.9 | 2e-07 | 23/24 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.590×** | -5.7 | 4e-07 | 22/24 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.318×** | -5.6 | 1e-06 | 23/24 (NCI-H460, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 615 | 0 | 39 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0371× (z -32.6) |
| [[HS-578T (line)]] | alt | 871 | 2 | 23 (8 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.25× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -19.3) |
| [[A549 (line)]] | wt | 827 | 0 | 18 (3 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0748× (z -18.5) |
| [[hTERT-HPNE (line)]] | wt | 2,894 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -25.8) |
| [[NCI-H460 (line)]] | wt | 557 | 0 | 18 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -20.5) |
| [[H4 (line)]] | wt | 908 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0613× (z -28.0) |
| [[NCI-H23 (line)]] | alt | 378 | 0 | 17 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0562× (z -28.4) |
| [[Hs 766T (line)]] | wt | 792 | 1 | 15 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.13× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -16.1) |
| [[HOP62 (line)]] | alt | 1,009 | 0 | 15 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.547× (z -14.6) ⚠ position not correctable · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.130× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 648 | 3 | 11 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.46× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.0432× (z -33.2) |
| [[NCI-H1792 (line)]] | alt | 793 | 0 | 13 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.534× (z -16.6) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 422 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -21.9) |
| [[RKO (line)]] | wt | 1,021 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -28.0) |
| [[SHP-77 (line)]] | alt | 735 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -16.6) |
| [[RPMI-7951 (line)]] | alt | 2,591 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0756× (z -27.8) |
| [[A-172 (line)]] | wt | 424 | 4 | 2 | [[Tucidinostat (drug)]] 5 µM 3.87× (z +14.8) | [[Trametinib (drug)]] 5 µM 0.205× (z -12.0) |
| [[CHP-212 (line)]] | wt | 276 | 2 | 4 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.72× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.0617× (z -20.0) |
| [[SNU-423 (line)]] | alt | 632 | 1 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.91× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -24.4) |
| [[A498 (line)]] | wt | 88.0 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 11.2× (z +17.2) | — |
| [[CFPAC-1 (line)]] | alt | 303 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -17.6) |
| [[J82 (line)]] | alt | 91.5 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 2.94× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.1) |
| [[SW 900 (line)]] | alt | 137 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.86× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 96.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.76× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 1,199 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -11.8) |
| [[A-427 (line)]] | wt | 19.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 62.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 48.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 32.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 26.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 25.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 32.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 24.5 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 25.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 528 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 438 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.5 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 42.7 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 29.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 80.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 31.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 33.7 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 35.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 24.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM158]] | +0.79 | +0.79 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[BCL2A1]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SGIP1]] | +0.75 | +0.70 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TIMP1]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_ANGIOGENESIS |
| [[RAC2]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[MMP1]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[PLAUR]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[BMERB1]] | +0.69 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NT5E]] | +0.69 | +0.72 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[ANTXR2]] | +0.68 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[PKIA]] | +0.68 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[LRRC8C]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGST1]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 8, C 20. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPBG]] | B | TPBG activity raises STC1's level | lines that do not express TPBG (10) vs lines expressing it (40) | 3.85× lower at baseline in the lines without TPBG | 0.030 | ⚠ within organs, on part of the lines |
| [[LRRC8C]] | B | LRRC8C activity raises STC1's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 5.07× lower at baseline in the lines without LRRC8C | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises STC1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 10.4% of all compounds | 0.062 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SHANK1]] | B | SHANK1 activity raises STC1's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 3.22× lower at baseline in the lines without SHANK1 | 0.065 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[MARCHF3]] | B | MARCHF3 activity raises STC1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 5.56× lower at baseline in the lines without MARCHF3 | 0.073 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[CEMIP]] | B | CEMIP activity raises STC1's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 3.80× lower at baseline in the lines without CEMIP | 0.074 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[FBXO27]] | B | FBXO27 activity lowers STC1's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 1.92× higher at baseline in the lines without FBXO27 | 0.080 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[SHB]] | B | SHB activity raises STC1's level | lines that do not express SHB (5) vs lines expressing it (45) | 5.37× lower at baseline in the lines without SHB | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[GJA1]] | C | GJA1 activity raises STC1's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 7.40× lower at baseline in the lines without GJA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; co-absent with the target |
| [[GRAMD1B]] | C | GRAMD1B activity raises STC1's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 6.77× lower at baseline in the lines without GRAMD1B | 0.005 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[CLMP]] | C | CLMP activity raises STC1's level | lines that do not express CLMP (25) vs lines expressing it (25) | 8.03× lower at baseline in the lines without CLMP | 0.007 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises STC1's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 7.29× lower at baseline in the lines without SPOCK1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 28, C 19. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTPD7]] | B | STC1 activity raises ENTPD7's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.33× lower at baseline in the lines without STC1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[UBA6]] | B | STC1 activity raises UBA6's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.43× lower at baseline in the lines without STC1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[SMTN]] | B | STC1 activity raises SMTN's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.70× lower at baseline in the lines without STC1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[NME7]] | B | STC1 activity raises NME7's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.93× lower at baseline in the lines without STC1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[SHANK1]] | B | STC1 activity raises SHANK1's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without STC1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[CSNK1E]] | B | STC1 activity raises CSNK1E's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without STC1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[RPSAP52]] | B | STC1 activity raises RPSAP52's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without STC1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[ITPRIP]] | B | STC1 activity raises ITPRIP's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.43× lower at baseline in the lines without STC1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[MARCHF3]] | B | STC1 activity raises MARCHF3's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without STC1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[EFL1]] | B | STC1 activity raises EFL1's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without STC1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[ANTXR2]] | B | STC1 activity raises ANTXR2's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without STC1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[LRRC8C]] | B | STC1 activity raises LRRC8C's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without STC1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.812). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.2, 3.0); signed map (3.2, 48.2). **Vector** length 157, 54.0% of its response variance represented; |z| ≥ 3 in 1,515 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.7 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.2 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.8 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +6.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.5 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +2.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.7 | +3.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.6 | +3.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -9.4 | -10.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -7.9 | -8.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -7.8 | -8.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.7 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.0 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.0 | -7.9 |

## What is on record

|  |  |
|---|---|
| Name | stanniocalcin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:23,841,929-23,854,806 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously STC |
| Hallmark sets | ANGIOGENESIS, GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [P52823](https://www.uniprot.org/uniprotkb/P52823) (Stanniocalcin-1):

> Stimulates renal phosphate reabsorption, and could therefore prevent hypercalcemia.

**Summary**, from NCBI Gene [6781](https://www.ncbi.nlm.nih.gov/gene/6781):

> This gene encodes a secreted, homodimeric glycoprotein that is expressed in a wide variety of tissues and may have autocrine or paracrine functions. The gene contains a 5' UTR rich in CAG trinucleotide repeats. The encoded protein contains 11 conserved cysteine residues and is phosphorylated by protein kinase C exclusively on its serine residues. The protein may play a role in the regulation of renal and intestinal calcium and phosphate transport, cell metabolism, or cellular calcium/phosphate …

**Accessions** — [HGNC:11373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11373) · Entrez [6781](https://www.ncbi.nlm.nih.gov/gene/6781) · UniProt [P52823](https://www.uniprot.org/uniprotkb/P52823) · Ensembl [ENSG00000159167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159167)

## Data

Gene col 8224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8224); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8224]; `tensor/DDL_lfc|DDL_z.npy` [8224]; `embed/gene_vectors.npy` [8224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8224 or target_col == 8224). Every well: [[STC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
