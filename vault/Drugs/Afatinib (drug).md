---
drug: "Afatinib"
type: "drug"
salt_base: "Afatinib"
targets: "EGFR, ERBB2"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 437
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Afatinib

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: EGFR, ERBB2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 12 / 43 / 437; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.46 / 0.42.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B10, [[Plate 07]]:C12 | 12 / 0 | 0.763 | -0.28 | -0.7/+0.3/-0.7 | — |
| 0.5 µM | [[Plate 02]]:B10, [[Plate 08]]:C12 | 34 / 9 | 0.839 | +0.48 | +1.3/-0.5/-1.4 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B10, [[Plate 09]]:C12 | 322 / 115 | 0.746 | +0.41 | -0.2/-0.6/-1.6 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (12 genes, none with an alert): [[DIRC3-AS1]] 1.27× (z +3.9, 5/43 lines), [[GBP2]] 1.26× (z +3.7, 11/36 lines), [[ENSG00000257869]] 1.29× (z +3.5, 0/12 lines), [[SEMA3D]] 1.23× (z +3.4, 0/16 lines), [[RHEX]] 1.37× (z +3.2, 0/5 lines), [[ZNF608]] 1.21× (z +3.2, 12/37 lines), [[SCIN]] 1.29× (z +3.1, 4/22 lines), [[LINC00470]] 1.26× (z +3.1, 0/10 lines), [[AGMO]] 1.26× (z +3.1, 0/17 lines), [[CFB]] 1.29× (z +3.0, 11/28 lines), [[ENSG00000250137]] 1.29× (z +2.9, 0/16 lines), [[CPS1]] 1.25× (z +2.9, 1/13 lines)

**0.5 µM** (34 genes, none with an alert; 12 shown): [[MACROD2]] 1.30× (z +4.5, 29/39 lines), [[WWOX]] 1.30× (z +4.1, 33/44 lines), [[CENPP]] 1.23× (z +3.9, 17/45 lines), [[ANKS1B]] 1.22× (z +3.8, 11/31 lines), [[PLCB1]] 1.21× (z +3.8, 13/30 lines), [[ENSG00000283415]] 1.24× (z +3.8, 10/34 lines), [[MIR924HG]] 1.26× (z +3.7, 17/41 lines), [[LINC01239]] 1.35× (z +3.7, 13/29 lines), [[CCDC148]] 1.27× (z +3.7, 7/46 lines), [[NR2F2-AS1]] 1.28× (z +3.6, 26/41 lines), [[LINC00342]] 1.24× (z +3.6, 25/49 lines), [[SPATA6]] 1.20× (z +3.5, 10/46 lines)

**5 µM** (322 genes, none with an alert; 12 shown): [[IDH1]] 1.55× (z +6.0, 32/48 lines), [[PIR]] 1.55× (z +5.8, 21/38 lines), [[DIXDC1]] 1.32× (z +5.6, 18/48 lines), [[MAP2K6]] 1.80× (z +5.3, 15/26 lines), [[WDSUB1]] 1.36× (z +5.2, 21/48 lines), [[KCNAB2]] 1.28× (z +5.2, 11/45 lines), [[KIAA0319]] 1.36× (z +5.2, 15/30 lines), [[NIBAN1]] 1.37× (z +5.1, 22/38 lines), [[GPR137C]] 1.56× (z +5.1, 18/46 lines), [[FOXN3]] 1.27× (z +5.1, 23/47 lines), [[RNFT2]] 1.43× (z +5.0, 19/44 lines), [[ACACB]] 1.51× (z +4.9, 22/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (9 genes, none with an alert): [[FASN]] 0.752× (z -4.0, 32/48 lines), [[ARHGDIA]] 0.806× (z -3.8, 31/49 lines), [[CASC3]] 0.800× (z -3.7, 35/49 lines), [[PPTC7]] 0.831× (z -3.5, 19/49 lines), [[TRAF4]] 0.833× (z -3.4, 7/48 lines), [[MTATP6P1]] 0.676× (z -3.4, 45/49 lines), [[CAPN10-DT]] 0.739× (z -3.3, 2/47 lines), [[MT-CO2]] 0.818× (z -3.0, 15/49 lines), [[NUAK2]] 0.826× (z -3.0, 8/38 lines)

**5 µM** (115 genes, none with an alert; 12 shown): [[DIAPH1]] 0.832× (z -5.2, 24/49 lines), [[MYO5B]] 0.782× (z -5.1, 12/23 lines), [[PRDM1]] 0.700× (z -5.0, 19/34 lines), [[ENSG00000255202]] 0.455× (z -4.9, 25/38 lines), [[PAG1]] 0.794× (z -4.8, 15/34 lines), [[NT5E]] 0.578× (z -4.8, 21/35 lines), [[PHLDA1]] 0.600× (z -4.7, 35/44 lines), [[C11orf91]] 0.503× (z -4.4, 19/38 lines), [[CDCP1]] 0.666× (z -4.3, 22/33 lines), [[TNFRSF10A]] 0.745× (z -4.3, 25/39 lines), [[ARPC2]] 0.742× (z -4.2, 32/49 lines), [[DLC1]] 0.832× (z -4.2, 10/35 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 200]] (+2.7), [[Module 230]] (+2.1) | [[Module 168]] (-2.6), [[Module 030]] (-2.0) |
| 5 µM | [[Module 230]] (+2.4), [[Module 146]] (+2.2), [[Module 122]] (+2.1) | [[Module 160]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[HT-29 (line)]] (-3.4), [[BT-474 (line)]] (-3.2) | [[C-33 A (line)]] (1.53), [[SW48 (line)]] (1.43), [[CHP-212 (line)]] (1.37), [[BT-474 (line)]] (1.35) · weakest: [[NCI-H2122 (line)]] (0.574), [[SHP-77 (line)]] (0.581), [[A-427 (line)]] (0.656) |
| 5 µM | [[NCI-H1792 (line)]] (-6.5), [[CHP-212 (line)]] (-5.1), [[BT-474 (line)]] (-4.4), [[Panc 03.27 (line)]] (-4.0), [[COLO 205 (line)]] (-3.8) | [[BT-474 (line)]] (1.55), [[NCI-H1573 (line)]] (1.42), [[CFPAC-1 (line)]] (1.28), [[SW48 (line)]] (1.26) · weakest: [[CHP-212 (line)]] (0.431), [[NCI-H661 (line)]] (0.462), [[AN3 CA (line)]] (0.588) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Ponatinib (drug)]] (+0.80, Multi-TK inhibitor); [[Cabozantinib (S-malate) (drug)]] (+0.72, Multi-TK inhibitor); [[Regorafenib (drug)]] (+0.66, Multi-TK inhibitor); [[Radotinib (drug)]] (+0.63, Other TK inhibitor); [[Flumatinib (mesylate) (drug)]] (+0.60, Other TK inhibitor); [[Vandetanib (drug)]] (+0.58, Multi-TK inhibitor); [[Encorafenib (drug)]] (+0.53, RAF inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.51, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 126 arrows, 126 of them with an alert ⚠; grade A 0, B 118, C 8. Shown: the 15 strongest; 111 more arrows (111 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[TMEM30B]] | 0.5 µM | B | TMEM30B activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express TMEM30B (35) vs lines expressing it (13) | the lines without TMEM30B: 1.17× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[TMEM125]] | 0.5 µM | B | TMEM125 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express TMEM125 (33) vs lines expressing it (15) | the lines without TMEM125: 1.16× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[MAL2]] | 0.5 µM | B | MAL2 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express MAL2 (31) vs lines expressing it (17) | the lines without MAL2: 1.14× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[SLC5A1]] | 0.5 µM | B | SLC5A1 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express SLC5A1 (36) vs lines expressing it (12) | the lines without SLC5A1: 1.16× the cells of the other lines | 0.032 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[SMPDL3B]] | 5 µM | B | SMPDL3B activity lowers the cells' numbers under Afatinib 5 µM (makes them more sensitive) | lines that do not express SMPDL3B (23) vs lines expressing it (25) | the lines without SMPDL3B: 1.16× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[GRHL2]], [[LINC02967]] | 0.5 µM | B | GRHL2, LINC02967 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (14) | the lines without GRHL2, LINC02967: 1.16× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[ATP2C2]] | 0.5 µM | B | ATP2C2 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.16× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[TRIM29]] | 0.05 µM | B | TRIM29 activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 1.14× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[TMPRSS2]] | 0.5 µM | B | TMPRSS2 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express TMPRSS2 (35) vs lines expressing it (13) | the lines without TMPRSS2: 1.17× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TACSTD2]] | 0.5 µM | B | TACSTD2 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express TACSTD2 (34) vs lines expressing it (14) | the lines without TACSTD2: 1.16× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[CDH1]] | 0.5 µM | B | CDH1 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express CDH1 (31) vs lines expressing it (17) | the lines without CDH1: 1.13× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[ENSG00000243004]] | 0.05 µM | B | ENSG00000243004 activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000243004 (31) vs lines expressing it (17) | the lines without ENSG00000243004: 1.12× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MACC1, TMEM125, GRHL2 |
| [[ESRP1]] | 0.5 µM | B | ESRP1 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express ESRP1 (31) vs lines expressing it (17) | the lines without ESRP1: 1.14× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[C1orf116]], [[IRF6]] | 0.05 µM | B | C1orf116, IRF6 activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 1.12× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[TRIM29]] | 0.5 µM | B | TRIM29 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 1.13× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Afatinib"
- `tables/drugdoses.parquet` — dd in 63, 64, 65
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
