---
symbol: "NOVA2"
type: "gene"
col: 2532
ensembl_id: "ENSG00000104967"
name: "NOVA alternative splicing regulator 2"
location: "19q13.32"
module: 82
arm: "+"
pooled_cpm: 4.53
n_lines_expressing: 27
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 12
direction_downstream: 23
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# NOVA2

*NOVA alternative splicing regulator 2* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.40× (z +19.2, q 0e+00, up in 22 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.466× (z -7.1, q 9e-10, down in 18 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAO1]] (+0.72, fdr 7e-06), [[JAKMIP1]] (+0.72, fdr 7e-06), [[CACNG7]] (+0.70, fdr 7e-06); moves opposite to [[GPATCH2]] (-0.56, fdr 7e-05), [[PRDM5]] (-0.53, fdr 2e-04), [[PSME3IP1]] (-0.51, fdr 9e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); 23 go from it, the strongest it → [[SLC17A7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.40×** | +19.2 | 0e+00 | 22/24 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **7.77×** | +18.8 | 0e+00 | 23/24 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.70×** | +17.5 | 0e+00 | 22/23 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.06×** | +16.5 | 0e+00 | 23/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.80×** | +14.4 | 6e-45 | 21/23 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.41×** | +13.6 | 2e-40 | 22/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **3.87×** | +12.4 | 1e-33 | 17/19 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +9.5 | 2e-19 | 1/5 (MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.06×** | +6.7 | 1e-09 | 16/23 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +6.6 | 3e-09 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **2.01×** | +6.4 | 8e-09 | 14/24 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.8 | 3e-07 | 4/18 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.90×** | +4.2 | 0.001 | 1/11 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +3.6 | 0.014 | 3/14 (A-427, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.68×** | +3.4 | 0.026 | 3/18 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.032 | 5/24 (SW480, Hs 766T, …) | two highest doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.043 | 2/17 (PANC-1, A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.39×** | +3.0 | 0.086 | 6/24 (SW480, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.466×** | -7.1 | 9e-10 | 18/24 (Hs 766T, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.524×** | -6.0 | 7e-07 | 14/24 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.647×** | -5.7 | 2e-06 | 15/22 (A-172, Hs 766T, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.545×** | -5.6 | 3e-06 | 15/19 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.567×** | -5.1 | 5e-05 | 12/23 (A-172, Hs 766T, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.610×** | -4.6 | 4e-04 | 12/23 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.628×** | -4.3 | 0.001 | 14/24 (NCI-H2030, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.647×** | -4.0 | 0.004 | 16/24 (SW 900, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.650×** | -4.0 | 0.004 | 10/24 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.652×** | -4.0 | 0.004 | 12/17 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.657×** | -3.7 | 0.009 | 8/24 (Hs 766T, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -3.2 | 0.057 | 8/23 (Hs 766T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 20.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0440× (z -30.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0317× (z -23.4) |
| [[Hs 766T (line)]] | wt | 45.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -17.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -16.6) |
| [[SW480 (line)]] | alt | 3.47 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 14.4× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 1 (1 ⚠) | 5 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +9.0) ⚠ position not correctable | [[Homoharringtonine (drug)]] 0.5 µM 0.0860× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 1.15 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 23.3× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.34 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 8.85× (z +8.9) | [[Homoharringtonine (drug)]] 0.05 µM 0.0379× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 6.62 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 7.78× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0607× (z -12.4) |
| [[PANC-1 (line)]] | alt | 2.83 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 16.3× (z +10.4) | — |
| [[A549 (line)]] | wt | 3.39 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 25.8× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 5.94 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0803× (z -11.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0376× (z -10.1) |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0998× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -11.5) |
| [[A-427 (line)]] | wt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 1.75 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.4× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 1.33 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 16.4× (z +8.6) | — |
| [[A498 (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.427 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAO1]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[JAKMIP1]] | +0.72 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CACNG7]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SYT11]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[KIF5C]] | +0.65 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[RET]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CFD]] | +0.63 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[PDZD4]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MAST1]] | +0.63 | +0.37 / +0.68 | both halves | 8e-05 |  |
| [[KCNQ2]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[MAP6]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MAPT]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2]] | -0.56 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[PRDM5]] | -0.53 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[PSME3IP1]] | -0.51 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[MSANTD2]] | -0.51 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[DDX59]] | -0.51 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[C8orf33]] | -0.50 | -0.35 / -0.21 | both halves | 6e-04 |  |
| [[FBXW4]] | -0.50 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[CRPPA]] | -0.50 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[MCCC2]] | -0.49 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises NOVA2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.49× lower at baseline in the lines without SEMA6B | 0.009 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[FAM78B]] | B | FAM78B activity raises NOVA2's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.94× lower at baseline in the lines without FAM78B | 0.055 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[MAN1C1]] | B | MAN1C1 activity raises NOVA2's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without MAN1C1 | 0.066 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[SYT7]] | B | SYT7 activity lowers NOVA2's level | lines that do not express SYT7 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without SYT7 | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EBF4]] | B | EBF4 activity raises NOVA2's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.87× lower at baseline in the lines without EBF4 | 0.096 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[DPYSL5]] | C | DPYSL5 activity raises NOVA2's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.95× lower at baseline in the lines without DPYSL5 | 0.009 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[NFASC]] | C | NFASC activity raises NOVA2's level | lines that do not express NFASC (27) vs lines expressing it (23) | 3.24× lower at baseline in the lines without NFASC | 0.049 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[MYT1]] | C | MYT1 activity raises NOVA2's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.58× lower at baseline in the lines without MYT1 | 0.049 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises NOVA2's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.29× lower at baseline in the lines without KIF1A | 0.073 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[RET]] | C | RET activity raises NOVA2's level | lines that do not express RET (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without RET | 0.079 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[LINC00173]] | C | LINC00173 activity raises NOVA2's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 3.00× lower at baseline in the lines without LINC00173 | 0.091 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2; co-absent with the target |
| [[CECR2]] | C | CECR2 activity raises NOVA2's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.62× lower at baseline in the lines without CECR2 | 0.097 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 12, C 11. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC17A7]] | B | NOVA2 activity raises SLC17A7's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without NOVA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[SEPTIN6]] | B | NOVA2 activity raises SEPTIN6's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.67× lower at baseline in the lines without NOVA2 | 0.009 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[SYP]] | B | NOVA2 activity raises SYP's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without NOVA2 | 0.013 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[PSME3IP1]] | B | NOVA2 activity raises PSME3IP1's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.14× lower at baseline in the lines without NOVA2 | 0.014 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[DDX59]] | B | NOVA2 activity raises DDX59's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without NOVA2 | 0.028 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[PTPRS]] | B | NOVA2 activity raises PTPRS's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 2.73× lower at baseline in the lines without NOVA2 | 0.032 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[SEMA6B]] | B | NOVA2 activity raises SEMA6B's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without NOVA2 | 0.037 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[ZNF483]] | B | NOVA2 activity strengthens ZNF483's drug response | lines that do not express NOVA2 (19) vs lines expressing it (24) | the lines without NOVA2 respond 0.81× as strongly (z diff +1.11); rises at some drug-doses, falls at others (33% from rises): Ouabain (Octahydrate) 5 µM: 0.60x vs 0.35x (z diff +3.1); Homoharringtonine 5 µM: 0.65x vs 0.44x (z diff +2.8); Panobinostat 0.05 µM: 2.11x vs 2.64x (z diff +1.4) | 0.052 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[DNAI1]] | B | NOVA2 activity raises DNAI1's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without NOVA2 | 0.055 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[KIF26A]] | B | NOVA2 activity raises KIF26A's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without NOVA2 | 0.077 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[FBXL16]] | B | NOVA2 activity raises FBXL16's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.38× lower at baseline in the lines without NOVA2 | 0.082 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[HDAC5]] | B | NOVA2 activity lowers HDAC5's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.09× higher at baseline in the lines without NOVA2 | 0.087 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.1, 39.2); signed map (27.1, 28.6). **Vector** length 64.0, 14.7% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +19.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +14.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +13.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +16.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +17.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +6.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | -0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | NOVA alternative splicing regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,933,734-45,974,044 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ANOVA, NOVA-2; previously NOVA3 |
| Gene groups (HGNC) | NOVA alternative splicing regulator family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNW9](https://www.uniprot.org/uniprotkb/Q9UNW9) (RNA-binding protein Nova-2):

> Functions to regulate alternative splicing in neurons by binding pre-mRNA in a sequence-specific manner to activate exon inclusion or exclusion. It binds specifically to the sequences 5'-YCAY-3' and regulates splicing in only a subset of regulated exons. Binding to an exonic 5'-YCAY-3' cluster changes the protein complexes assembled on pre-mRNA, blocking U1 snRNP binding and exon inclusion, whereas binding to an intronic 5'-YCAY-3' cluster enhances spliceosome assembly and exon inclusion. With …

**Summary**, from NCBI Gene [4858](https://www.ncbi.nlm.nih.gov/gene/4858):

> Enables sequence-specific mRNA binding activity. Involved in neuron differentiation and regulation of alternative mRNA splicing, via spliceosome. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7887) · Entrez [4858](https://www.ncbi.nlm.nih.gov/gene/4858) · UniProt [Q9UNW9](https://www.uniprot.org/uniprotkb/Q9UNW9) · Ensembl [ENSG00000104967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104967)

## Data

Gene col 2532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2532); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2532]; `tensor/DDL_lfc|DDL_z.npy` [2532]; `embed/gene_vectors.npy` [2532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2532 or target_col == 2532). Every well: [[NOVA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOVA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
