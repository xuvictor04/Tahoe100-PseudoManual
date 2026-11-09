---
symbol: "EFNA4"
type: "gene"
col: 14354
ensembl_id: "ENSG00000243364"
name: "ephrin A4"
location: "1q21.3"
module: 88
arm: "-"
pooled_cpm: 3.84
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# EFNA4

*ephrin A4* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.70× (z +10.4, q 9e-23, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.404× (z -9.5, q 1e-18, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFNA3]] (+0.87, fdr 7e-06, ⚠ same locus), [[ALDOC]] (+0.74, fdr 7e-06), [[PLEKHH3]] (+0.73, fdr 7e-06), [[SLC26A6]] (+0.71, fdr 1e-05); moves opposite to [[SDCBP2-AS1]] (-0.70, fdr 1e-05), [[ST7L]] (-0.70, fdr 1e-05), [[ZNF655]] (-0.69, fdr 3e-05).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MMP15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.70×** | +10.4 | 9e-23 | 34/44 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +7.5 | 1e-11 | 27/44 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +7.5 | 1e-11 | 25/44 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.1 | 5e-05 | 8/46 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +4.5 | 7e-04 | 8/44 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.018 | 8/33 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.6 | 0.023 | 5/23 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.039 | 5/44 (SK-MEL-2, PANC-1, …) | rises with dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.35× | +3.2 | 0.10 | 5/41 (SW48, J82, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14354.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.404×** | -9.5 | 1e-18 | 28/35 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.384×** | -9.4 | 2e-18 | 30/41 (A-172, C-33 A, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.583×** | -8.0 | 2e-13 | 27/36 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.497×** | -7.3 | 3e-11 | 23/43 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.520×** | -6.9 | 7e-10 | 16/20 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.521×** | -6.8 | 7e-10 | 25/45 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.356×** | -5.7 | 1e-06 | 24/39 (LS 180, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -5.5 | 3e-06 | 11/44 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.613×** | -5.1 | 2e-05 | 20/41 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.403×** | -5.0 | 3e-05 | 16/32 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -4.9 | 4e-05 | 16/33 (Hs 766T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.635×** | -4.8 | 9e-05 | 18/43 (LS 180, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.660×** | -4.4 | 6e-04 | 10/36 (C-33 A, CFPAC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -4.1 | 0.002 | 12/25 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.659×** | -4.0 | 0.002 | 7/11 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.690×** | -3.9 | 0.003 | 14/42 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.696×** | -3.8 | 0.005 | 12/42 (LS 180, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -3.6 | 0.008 | 17/43 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.025 | 16/43 (COLO 205, SNU-423, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 7.99 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0840× (z -11.1) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.115× (z -10.3) |
| [[A498 (line)]] | wt | 4.39 | 0 | 2 (1 ⚠) | — | [[Ixazomib (drug)]] 0.05 µM 0.0724× (z -11.2) |
| [[Hs 766T (line)]] | wt | 4.79 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -8.5) |
| [[HT-29 (line)]] | alt | 4.17 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 4.76 | 0 | 2 | — | [[Belumosudil (drug)]] 5 µM 0.0547× (z -9.0) |
| [[PANC-1 (line)]] | alt | 3.52 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -12.6) |
| [[A-172 (line)]] | wt | 4.04 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0498× (z -10.3) |
| [[C-33 A (line)]] | alt | 5.29 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0367× (z -9.1) |
| [[KATO III (line)]] | alt | 6.90 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0447× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 5.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 4.71 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA3]] | +0.87 | +0.80 / +0.76 | both halves | 7e-06 | same gene group; pathway: EPH-Ephrin signaling; STRING 576; ⚠ same locus (9.3 kb, same strand: neighbours can correlate without regulation) |
| [[ALDOC]] | +0.74 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PLEKHH3]] | +0.73 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SLC26A6]] | +0.71 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.69 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[RASSF7]] | +0.69 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.68 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[RAB3A]] | +0.68 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[GMCL1]] | +0.67 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[DNAAF3]] | +0.66 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CABLES2]] | +0.65 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[IGSF8]] | +0.64 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[STK32C]] | +0.64 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP2-AS1]] | -0.70 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[ST7L]] | -0.70 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.69 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[RAB30-DT]] | -0.69 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[AVEN]] | -0.66 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[LTO1]] | -0.66 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[RGS20]] | -0.65 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | -0.65 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[CSTF3]] | -0.65 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[RXYLT1]] | -0.65 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[CLHC1]] | -0.64 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[NEPRO-AS1]] | -0.64 | -0.61 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP15]] | B | MMP15 activity raises EFNA4's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without MMP15 | 0.033 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers EFNA4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers EFNA4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[XKR8]] | B | XKR8 activity raises EFNA4's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without XKR8 | 0.064 | ⚠ within organs, on part of the lines; also absent: MORC4 |
| [[ZNF655]] | B | ZNF655 activity lowers EFNA4's level | lines that do not express ZNF655 (7) vs lines expressing it (43) | 1.58× higher at baseline in the lines without ZNF655 | 0.085 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.750). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (5.7, -4.3); signed map (-31.0, 18.9). **Vector** length 61.4, 9.43% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +7.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +7.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.7 | +4.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.0 | +0.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ephrin A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:155,063,737-155,069,553 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LERK4; previously EPLG4 |
| Gene groups (HGNC) | Ephrins |
| Reactome | 5 pathways, smallest: EPHA-mediated growth cone collapse; EPH-ephrin mediated repulsion of cells; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P52798](https://www.uniprot.org/uniprotkb/P52798) (Ephrin-A4):

> Cell surface GPI-bound ligand for Eph receptors, a family of receptor tyrosine kinases which are crucial for migration, repulsion and adhesion during neuronal, vascular and epithelial development. Binds promiscuously Eph receptors residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. May play a role in the interaction between activated B-lymphocytes and dendritic cells in tonsils.

**Summary**, from NCBI Gene [1945](https://www.ncbi.nlm.nih.gov/gene/1945):

> This gene encodes a member of the ephrin (EPH) family. The ephrins and EPH-related receptors comprise the largest subfamily of receptor protein-tyrosine kinases and have been implicated in mediating developmental events, especially in the nervous system and in erythropoiesis. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchored to the membrane by a glycosylphosphatidylinositol linkage, and the ephrin-B (EFNB) class, which …

**Accessions** — [HGNC:3224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3224) · Entrez [1945](https://www.ncbi.nlm.nih.gov/gene/1945) · UniProt [P52798](https://www.uniprot.org/uniprotkb/P52798) · Ensembl [ENSG00000243364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243364)

## Data

Gene col 14354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14354); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14354]; `tensor/DDL_lfc|DDL_z.npy` [14354]; `embed/gene_vectors.npy` [14354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14354 or target_col == 14354). Every well: [[EFNA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFNA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
