---
drug: "Bimiralisib"
type: "drug"
salt_base: "Bimiralisib"
targets: "PIK3CA, PIK3CB, MTOR"
moa_fine: "PI3K/AKT inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1002
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Bimiralisib

*PI3K/AKT inhibitor (inhibitor/antagonist) · targets: PIK3CA, PIK3CB, MTOR · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 153 / 753 / 1002; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.01 / 0.05.
> Flags by dose: - / low cells (technical?); plate-row cell shift; noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:D11 | 75 / 78 | — | +0.18 | -2.9/-2.5/-2.3 | — |
| 0.5 µM | [[Plate 02]]:D11 | 460 / 293 | — | -1.26 | -1.5/-0.4/+1.0 | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:D11 | 616 / 386 | — | +1.48 | -2.7/-2.5/-3.0 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (75 genes, none with an alert; 12 shown): [[GBP2]] 1.46× (z +4.1, 14/36 lines), [[ZNF345]] 1.32× (z +3.9, 10/35 lines), [[JDP2]] 1.33× (z +3.8, 8/34 lines), [[GNG7]] 1.27× (z +3.8, 6/46 lines), [[YPEL2]] 1.26× (z +3.7, 11/46 lines), [[KIZ]] 1.21× (z +3.7, 15/49 lines), [[DISP1]] 1.25× (z +3.7, 17/49 lines), [[CPEB3]] 1.24× (z +3.6, 10/49 lines), [[TMEM260]] 1.24× (z +3.6, 15/49 lines), [[LMAN2L]] 1.25× (z +3.6, 9/48 lines), [[CDKL3]] 1.27× (z +3.6, 13/48 lines), [[ENSG00000165121]] 1.28× (z +3.5, 6/45 lines)

**0.5 µM** (460 genes, none with an alert; 12 shown): [[SELENOP]] 2.61× (z +5.8, 14/25 lines), [[SLC25A23]] 1.60× (z +4.7, 17/42 lines), [[DRG2]] 1.46× (z +4.6, 9/45 lines), [[ZNF580]] 1.79× (z +4.5, 18/44 lines), [[PNPLA2]] 1.60× (z +4.5, 24/46 lines), [[MTUS1-DT]] 2.10× (z +4.5, 9/27 lines), [[CFB]] 2.02× (z +4.5, 17/26 lines), [[ALDH3B1]] 1.91× (z +4.4, 19/34 lines), [[FAM200A]] 1.66× (z +4.3, 12/43 lines), [[BMF]] 2.05× (z +4.3, 10/33 lines), [[ARSD]] 1.61× (z +4.3, 16/41 lines), [[RASSF4]] 1.68× (z +4.3, 10/33 lines)

**5 µM** (616 genes, none with an alert; 12 shown): [[JAK1]] 1.58× (z +6.6, 40/50 lines), [[ARID5B]] 2.20× (z +6.3, 31/44 lines), [[GBP2]] 3.05× (z +6.2, 28/36 lines), [[KANSL1L]] 1.80× (z +5.9, 37/50 lines), [[DUSP16]] 1.65× (z +5.8, 31/48 lines), [[FOXN3]] 1.57× (z +5.6, 30/48 lines), [[SEMA3C]] 2.07× (z +5.5, 29/42 lines), [[CFB]] 3.83× (z +5.4, 18/27 lines), [[KLHL24]] 1.95× (z +5.4, 40/50 lines), [[PHLDB2]] 1.87× (z +5.4, 22/39 lines), [[ZBTB20]] 1.88× (z +5.3, 40/50 lines), [[APOLD1]] 1.47× (z +5.2, 24/50 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (78 genes, none with an alert; 12 shown): [[FERMT1]] 0.674× (z -4.5, 17/27 lines), [[EGR1]] 0.543× (z -4.4, 43/47 lines), [[CDCP1]] 0.752× (z -4.4, 25/33 lines), [[FOSL1]] 0.628× (z -4.3, 30/44 lines), [[SPRY4]] 0.702× (z -4.3, 23/48 lines), [[VARS1]] 0.686× (z -4.0, 20/48 lines), [[BZW1]] 0.737× (z -3.8, 40/49 lines), [[DUSP6]] 0.611× (z -3.8, 32/45 lines), [[FKBP1A]] 0.806× (z -3.8, 21/49 lines), [[RRM2]] 0.691× (z -3.7, 22/46 lines), [[LAMB1]] 0.806× (z -3.7, 23/42 lines), [[PHLDA1]] 0.651× (z -3.7, 33/44 lines)

**0.5 µM** (293 genes, none with an alert; 12 shown): [[ETV5]] 0.640× (z -5.9, 29/48 lines), [[SLC4A7]] 0.687× (z -5.6, 36/45 lines), [[SPRED2]] 0.622× (z -5.3, 44/48 lines), [[B4GALT6]] 0.656× (z -5.2, 20/38 lines), [[SPRY4]] 0.570× (z -5.2, 30/48 lines), [[MCTP1]] 0.652× (z -5.1, 22/35 lines), [[ZNF215]] 0.687× (z -4.7, 16/35 lines), [[ZFPM2-AS1]] 0.700× (z -4.6, 22/32 lines), [[SLC9A7]] 0.719× (z -4.6, 28/47 lines), [[CNOT10]] 0.798× (z -4.5, 14/47 lines), [[DNMBP]] 0.705× (z -4.3, 24/48 lines), [[PTPN12]] 0.752× (z -4.3, 30/48 lines)

**5 µM** (386 genes, none with an alert; 12 shown): [[ETV5]] 0.191× (z -11.8, 42/50 lines), [[SPRY4-AS1]] 0.184× (z -9.1, 42/47 lines), [[CCND1]] 0.331× (z -8.2, 35/43 lines), [[SPRY4]] 0.145× (z -8.1, 43/49 lines), [[MYEOV]] 0.262× (z -8.0, 22/29 lines), [[ETV1]] 0.202× (z -7.9, 29/38 lines), [[FOSL1]] 0.232× (z -7.5, 39/45 lines), [[DUSP6]] 0.119× (z -6.9, 42/46 lines), [[DUSP4]] 0.401× (z -6.8, 28/35 lines), [[EGR1]] 0.133× (z -6.6, 45/48 lines), [[ENSG00000260877]] 0.286× (z -6.5, 27/34 lines), [[SPRED1]] 0.451× (z -6.3, 40/50 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 170]] (+2.6), [[Module 225]] (+2.3), [[Module 234]] (+2.1) | [[Module 060]] (-2.3) |
| 0.5 µM | [[Module 059]] (+3.2), [[Module 010]] (+2.6), [[Module 024]] (+2.6) | [[Module 020]] (-2.3), [[Module 174]] (-2.1), [[Module 018]] (-2.1) |
| 5 µM | [[Module 232]] (+3.2), [[Module 225]] (+3.1), [[Module 230]] (+3.0) | [[Module 174]] (-2.9), [[Module 048]] (-2.8), [[Module 092]] (-2.7) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[Hs 766T (line)]] (1.54), [[SW 1271 (line)]] (1.40), [[SW480 (line)]] (1.38), [[MIA PaCa-2 (line)]] (1.35) · weakest: [[AN3 CA (line)]] (0.293), [[NCI-H2122 (line)]] (0.371), [[NCI-H661 (line)]] (0.502) |
| 0.5 µM | [[CHP-212 (line)]] (-3.2) | [[AsPC-1 (line)]] (1.28), [[CHP-212 (line)]] (1.20), [[MIA PaCa-2 (line)]] (1.19), [[Hs 766T (line)]] (1.18) · weakest: [[SHP-77 (line)]] (0.632), [[BT-474 (line)]] (0.723), [[AN3 CA (line)]] (0.771) |
| 5 µM | [[NCI-H1792 (line)]] (-8.1), [[CHP-212 (line)]] (-7.7), [[COLO 205 (line)]] (-6.9), [[Panc 03.27 (line)]] (-6.7), [[H4 (line)]] (-6.3) | [[HOP62 (line)]] (1.30), [[AsPC-1 (line)]] (1.28), [[MIA PaCa-2 (line)]] (1.27), [[NCI-H23 (line)]] (1.26) · weakest: [[NCI-H596 (line)]] (0.569), [[CHP-212 (line)]] (0.590), [[AN3 CA (line)]] (0.669) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[BI-3406 (drug)]] (+0.85, RAS inhibitor); [[Trametinib (drug)]] (+0.82, MEK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[RMC-6236 (drug)]] (+0.81, RAS inhibitor); [[AZD-8055 (drug)]] (+0.79, MTOR inhibitor); [[Trametinib (DMSO_TF solvate) (drug)]] (+0.71, MEK inhibitor); [[Binimetinib (drug)]] (+0.68, MEK inhibitor); [[Perindopril (erbumine) (drug)]] (+0.68, unclear); [[Elimusertib hydrochloride (drug)]] (+0.64, unclear); [[Cobimetinib (drug)]] (+0.62, MEK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 20 arrows, 20 of them with an alert ⚠; grade A 0, B 14, C 6. Shown: the 15 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[DUSP4]] | 0.05 µM | B | DUSP4 activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express DUSP4 (15) vs lines expressing it (33) | the lines without DUSP4: 1.26× the cells of the other lines | 0.044 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[ENSG00000283240]] | 0.05 µM | B | ENSG00000283240 activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000283240 (19) vs lines expressing it (29) | the lines without ENSG00000283240: 1.12× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: MGST1, IL1R2, STON2 |
| [[ATXN1-AS1]] | 0.5 µM | B | ATXN1-AS1 activity lowers the cells' numbers under Bimiralisib 0.5 µM (makes them more sensitive) | lines that do not express ATXN1-AS1 (6) vs lines expressing it (42) | the lines without ATXN1-AS1: 1.32× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[ABCC3]] | 0.05 µM | B | ABCC3 activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express ABCC3 (16) vs lines expressing it (32) | the lines without ABCC3: 1.17× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[SLC16A4]] | 0.05 µM | B | SLC16A4 activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express SLC16A4 (15) vs lines expressing it (33) | the lines without SLC16A4: 1.18× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[IL15]] | 0.5 µM | B | IL15 activity lowers the cells' numbers under Bimiralisib 0.5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.25× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[IGSF9]] | 0.05 µM | B | IGSF9 activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express IGSF9 (16) vs lines expressing it (32) | the lines without IGSF9: 1.25× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[ABHD17C]] | 0.05 µM | B | ABHD17C activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express ABHD17C (8) vs lines expressing it (40) | the lines without ABHD17C: 1.19× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[ENSG00000258919]] | 0.5 µM | B | ENSG00000258919 activity lowers the cells' numbers under Bimiralisib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000258919 (23) vs lines expressing it (25) | the lines without ENSG00000258919: 1.16× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC02320, ENSG00000266088, DIO3OS |
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity lowers the cells' numbers under Bimiralisib 0.5 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.26× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[GPRC5D-AS1]] | 0.05 µM | B | GPRC5D-AS1 activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (43) | the lines without GPRC5D-AS1: 1.23× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[PLEKHA6]] | 0.05 µM | B | PLEKHA6 activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express PLEKHA6 (16) vs lines expressing it (32) | the lines without PLEKHA6: 1.13× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[IL1R2]] | 0.05 µM | B | IL1R2 activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express IL1R2 (23) vs lines expressing it (25) | the lines without IL1R2: 1.17× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[LGALS3BP]] | 0.05 µM | B | LGALS3BP activity lowers the cells' numbers under Bimiralisib 0.05 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.19× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[ANG]], [[RNASE4]] | 5 µM | C | ANG, RNASE4 activity raises the cells' numbers under Bimiralisib 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.53× the cells of the other lines | 0.053 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 125 arrows, 125 of them with an alert ⚠; grade A 0, B 125, C 0. Shown: the 15 strongest; 110 more arrows (110 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MTOR]] | [[INSR]] | moves it that way too | B | MTOR activity lowers INSR's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[FKBP14]] | moves it that way too | B | MTOR activity raises FKBP14's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WASHC2C]] | moves it that way too | B | MTOR activity lowers WASHC2C's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[TSPAN13]] | moves it that way too | B | MTOR activity raises TSPAN13's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[MCM8]] | moves it that way too | B | MTOR activity raises MCM8's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WDR19]] | moves it that way too | B | MTOR activity lowers WDR19's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[CENPN]] | moves it that way too | B | MTOR activity raises CENPN's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[DTL]] | moves it that way too | B | MTOR activity raises DTL's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WDR62]] | moves it that way too | B | MTOR activity raises WDR62's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[MARS1]] | moves it that way too | B | MTOR activity raises MARS1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds |
| [[MTOR]] | [[SMAP2]] | moves it that way too | B | MTOR activity raises SMAP2's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[ERICH1]] | moves it that way too | B | MTOR activity lowers ERICH1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.6% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[FBXO32]] | moves it that way too | B | MTOR activity lowers FBXO32's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 7.3% of all compounds | 0.013 | ⚠ off-target possible; 6 compounds |
| [[MTOR]] | [[PDIA3]] | moves it that way too | B | MTOR activity raises PDIA3's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[YPEL1]] | moves it that way too | B | MTOR activity lowers YPEL1's level | compounds that target MTOR: 5 of 8 raise it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Bimiralisib"
- `tables/drugdoses.parquet` — dd in 197, 198, 199
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
