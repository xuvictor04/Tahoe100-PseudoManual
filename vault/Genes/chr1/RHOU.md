---
symbol: "RHOU"
type: "gene"
col: 3806
ensembl_id: "ENSG00000116574"
name: "ras homolog family member U"
location: "1q42.13"
module: 123
arm: "+"
pooled_cpm: 6.91
n_lines_expressing: 41
n_dd_up: 40
n_dd_down: 15
n_dd_up_clean: 33
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 11
direction_downstream: 4
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# RHOU

*ras homolog family member U* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +9.9, q 2e-20, up in 22 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.429× (z -8.3, q 7e-14, down in 20 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIGD2]] (+0.66, fdr 7e-06), [[ZFP36L2]] (+0.66, fdr 7e-06), [[LGALS3]] (+0.65, fdr 7e-06); moves opposite to [[SNHG30]] (-0.56, fdr 1e-05), [[SENP5]] (-0.55, fdr 1e-05), [[ZCCHC17]] (-0.54, fdr 2e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CDH17]] → it (grade B ⚠); 4 go from it, the strongest it → [[PDCD6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +9.9 | 2e-20 | 22/30 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.67×** | +9.3 | 5e-18 | 21/32 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +8.6 | 1e-15 | 24/36 (NCI-H2347, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +7.4 | 2e-11 | 11/24 (SW1417, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +7.3 | 4e-11 | 18/36 (A498, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.05×** | +7.1 | 1e-10 | 18/36 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +6.6 | 3e-09 | 21/35 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +6.3 | 2e-08 | 7/13 (NCI-H2347, A549, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +6.2 | 4e-08 | 17/29 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +5.7 | 5e-07 | 18/35 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +5.6 | 1e-06 | 15/34 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +5.1 | 1e-05 | 4/11 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.55×** | +4.8 | 6e-05 | 15/35 (NCI-H460, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.98×** | +4.7 | 1e-04 | 8/22 (NCI-H460, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +4.6 | 2e-04 | 13/33 (C32, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +4.5 | 2e-04 | 17/36 (LoVo, AsPC-1, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.54×** | +4.3 | 6e-04 | 12/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.55×** | +4.2 | 9e-04 | 11/33 (C32, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.429×** | -8.3 | 7e-14 | 20/35 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.456×** | -7.7 | 5e-12 | 23/36 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.582×** | -5.3 | 2e-05 | 17/35 (LS 180, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.583×** | -5.3 | 2e-05 | 18/35 (J82, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -5.1 | 5e-05 | 18/37 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.584×** | -5.0 | 7e-05 | 17/34 (LS 180, C32, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -4.7 | 2e-04 | 18/34 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -4.6 | 3e-04 | 16/29 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.724×** | -4.4 | 6e-04 | 16/37 (Hs 766T, SW1417, …) | all doses, flat | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.448×** | -4.1 | 0.002 | 13/33 (LoVo, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.565×** | -3.9 | 0.006 | 13/36 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.684×** | -3.7 | 0.010 | 5/35 (SW1417, PANC-1, …) | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.780×** | -3.4 | 0.029 | 8/36 (HT-29, AsPC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.700×** | -3.3 | 0.042 | 8/35 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.544×** | -3.1 | 0.071 | 7/29 (LoVo, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.83 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +13.9) | — |
| [[LS 180 (line)]] | wt | 34.4 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.162× (z -11.9) |
| [[C32 (line)]] | wt | 14.7 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0943× (z -10.4) |
| [[A498 (line)]] | wt | 2.10 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +11.0) | [[Ixazomib citrate (drug)]] 5 µM 0.0970× (z -9.4) |
| [[SW 900 (line)]] | alt | 5.62 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 2.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +12.0) | — |
| [[J82 (line)]] | alt | 2.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +8.5) | — |
| [[LoVo (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.253× (z -10.3) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 2.84 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0608× (z -9.6) |
| [[A-427 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIGD2]] | +0.66 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[ZFP36L2]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[LGALS3]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[TRIM29]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PLEKHG6]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[KLF4]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RASSF6]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[EDN1]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[FOSL2]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[LGALSL]] | +0.59 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[CGN]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[REPIN1]] | +0.58 | +0.67 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG30]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[SENP5]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.54 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[MFN1]] | -0.54 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[SLC30A6]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[CERS5]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CCDC168]] | -0.52 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[CTC-338M12.4]] | -0.51 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SGSM3]] | -0.51 | -0.56 / -0.43 | both halves | 4e-05 |  |
| [[BCAP31]] | -0.51 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[TPD52L2]] | -0.51 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[TIMM10B]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH17]] | B | CDH17 activity raises RHOU's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.64× lower at baseline in the lines without CDH17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[RASSF6]] | B | RASSF6 activity raises RHOU's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.12× lower at baseline in the lines without RASSF6 | 0.009 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[FRMD4B]] | B | FRMD4B activity raises RHOU's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.80× lower at baseline in the lines without FRMD4B | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[EFNA1]] | B | EFNA1 activity raises RHOU's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without EFNA1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[TRIM29]] | B | TRIM29 activity raises RHOU's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without TRIM29 | 0.031 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[SHROOM3]] | B | SHROOM3 activity raises RHOU's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without SHROOM3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[AKR1C3]] | B | AKR1C3 activity raises RHOU's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 1.94× lower at baseline in the lines without AKR1C3 | 0.043 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[PDK4]] | B | PDK4 activity raises RHOU's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without PDK4 | 0.043 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[EDN1]] | B | EDN1 activity raises RHOU's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.79× lower at baseline in the lines without EDN1 | 0.046 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[SLC40A1]] | B | SLC40A1 activity raises RHOU's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without SLC40A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[RSPH1]] | B | RSPH1 activity raises RHOU's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without RSPH1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDCD6]] | B | RHOU activity raises PDCD6's level | lines that do not express RHOU (9) vs lines expressing it (41) | 1.35× lower at baseline in the lines without RHOU | 0.071 | ⚠ within organs, on part of the lines; also absent: JAKMIP3, HAP1 |
| [[EFNA1]] | B | RHOU activity raises EFNA1's level | lines that do not express RHOU (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without RHOU | 0.083 | ⚠ within organs, on part of the lines; also absent: JAKMIP3, HAP1 |
| [[C1orf226]] | B | RHOU activity raises C1orf226's level | lines that do not express RHOU (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without RHOU | 0.084 | ⚠ within organs, on part of the lines; also absent: JAKMIP3, HAP1 |
| [[SFT2D1]] | B | RHOU activity lowers SFT2D1's level | lines that do not express RHOU (9) vs lines expressing it (41) | 1.20× higher at baseline in the lines without RHOU | 0.099 | ⚠ within organs, on part of the lines; also absent: JAKMIP3, HAP1 |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.0, 13.3); signed map (49.5, 11.6). **Vector** length 78.0, 16.7% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +9.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +4.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -8.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member U |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:228,735,479-228,746,664 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WRCH-1, DJ646B12.2, FLJ10616, WRCH1, CDC42L1, hG28K, fJ646B12.2; previously ARHU |
| Gene groups (HGNC) | Rho family GTPases |
| Reactome | 7 pathways, smallest: RHOU GTPase cycle; Interleukin-4 and Interleukin-13 signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L0Q8](https://www.uniprot.org/uniprotkb/Q7L0Q8) (Rho-related GTP-binding protein RhoU):

> Binds to and activates protein kinase PAK1. Plays a role in the regulation of cell morphology, cytoskeletal organization and focal adhesion assembly during cell migration. Also stimulates quiescent cells to reenter the cell cycle. Has no detectable GTPase activity but its high intrinsic guanine nucleotide exchange activity suggests it is constitutively GTP-bound.

**Summary**, from NCBI Gene [58480](https://www.ncbi.nlm.nih.gov/gene/58480):

> This gene encodes a member of the Rho family of GTPases. This protein can activate PAK1 and JNK1, and can induce filopodium formation and stress fiber dissolution. It may also mediate the effects of WNT1 signaling in the regulation of cell morphology, cytoskeletal organization, and cell proliferation. A non-coding transcript variant of this gene results from naturally occurring read-through transcription between this locus and the neighboring DUSP5P (dual specificity phosphatase 5 pseudogene) …

**Accessions** — [HGNC:17794](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17794) · Entrez [58480](https://www.ncbi.nlm.nih.gov/gene/58480) · UniProt [Q7L0Q8](https://www.uniprot.org/uniprotkb/Q7L0Q8) · Ensembl [ENSG00000116574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116574)

## Data

Gene col 3806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3806); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3806]; `tensor/DDL_lfc|DDL_z.npy` [3806]; `embed/gene_vectors.npy` [3806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3806 or target_col == 3806). Every well: [[RHOU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
