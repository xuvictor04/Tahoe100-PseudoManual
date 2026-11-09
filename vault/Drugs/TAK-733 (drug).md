---
drug: "TAK-733"
type: "drug"
salt_base: "TAK-733"
targets: "MAP2K1"
moa_fine: "MEK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1903
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# TAK-733

*MEK inhibitor (inhibitor/antagonist) · targets: MAP2K1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 162 / 9 / 1903; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.18 / 0.20.
> Flags by dose: - / low cells (technical?); noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:F7 | 41 / 121 | — | +0.22 | -0.4/-1.5/+0.2 | — |
| 0.5 µM | [[Plate 02]]:F7 | 8 / 1 | — | -1.02 | +0.1/+0.2/-0.2 | low cells (technical?); noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F7 | 697 / 1,206 | — | +0.00 | +1.6/-1.1/+1.4 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (41 genes, none with an alert; 12 shown): [[TMED3]] 1.29× (z +5.3, 27/47 lines), [[UCHL3]] 1.25× (z +4.6, 21/47 lines), [[SEC23B]] 1.34× (z +4.4, 29/48 lines), [[PLEKHM1]] 1.27× (z +4.0, 19/48 lines), [[ENSG00000285906]] 1.29× (z +3.9, 12/39 lines), [[C6orf141]] 1.43× (z +3.7, 8/27 lines), [[ATAT1]] 1.24× (z +3.6, 13/48 lines), [[TMEM92-AS1]] 1.49× (z +3.6, 7/31 lines), [[CLCN5]] 1.20× (z +3.6, 8/47 lines), [[SYCE1L]] 1.46× (z +3.5, 5/44 lines), [[TM4SF19]] 1.31× (z +3.5, 6/28 lines), [[ARMC6]] 1.30× (z +3.4, 2/47 lines)

**0.5 µM** (8 genes, none with an alert): [[RAB38]] 1.54× (z +4.1, 3/24 lines), [[MIR181A1HG]] 1.45× (z +4.0, 24/41 lines), [[ZNF331]] 1.27× (z +3.4, 12/33 lines), [[TPRA1]] 1.35× (z +3.4, 12/48 lines), [[RIPK4]] 1.53× (z +3.3, 17/35 lines), [[E2F7]] 1.27× (z +3.1, 17/43 lines), [[TIPARP]] 1.90× (z +3.0, 19/47 lines), [[RMDN2-AS1]] 2.19× (z +2.9, 5/27 lines)

**5 µM** (697 genes, none with an alert; 12 shown): [[FRMD5]] 2.51× (z +8.9, 30/38 lines), [[DHX37]] 2.23× (z +7.6, 34/46 lines), [[CREB5]] 2.28× (z +7.5, 21/33 lines), [[RCAN1]] 2.18× (z +7.5, 28/47 lines), [[MRPS25]] 1.88× (z +7.4, 35/47 lines), [[PDCD11]] 2.06× (z +7.3, 39/48 lines), [[ZNRF3]] 1.95× (z +6.8, 34/46 lines), [[WDR3]] 1.86× (z +6.7, 32/48 lines), [[ENAH]] 1.62× (z +6.6, 31/45 lines), [[C19orf48]] 2.01× (z +6.6, 26/45 lines), [[POP1]] 2.26× (z +6.6, 23/45 lines), [[RBBP8]] 1.63× (z +6.5, 22/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (121 genes, none with an alert; 12 shown): [[TFDP2]] 0.713× (z -9.9, 38/48 lines), [[CCDC28A]] 0.640× (z -7.3, 32/48 lines), [[FBXO32]] 0.591× (z -7.2, 22/34 lines), [[PDCD4]] 0.705× (z -7.2, 37/48 lines), [[KLHL24]] 0.646× (z -6.6, 40/48 lines), [[YPEL2]] 0.678× (z -6.2, 25/45 lines), [[JMY]] 0.670× (z -6.1, 35/47 lines), [[REPS2]] 0.676× (z -5.6, 20/36 lines), [[NIPAL3]] 0.726× (z -5.4, 25/48 lines), [[RPS6KA5]] 0.784× (z -5.3, 26/48 lines), [[TCP11L2]] 0.659× (z -5.2, 30/48 lines), [[FBXO25]] 0.780× (z -5.1, 19/44 lines)

**0.5 µM** (1 gene, none with an alert): [[DUSP5]] 0.706× (z -3.1, 9/41 lines)

**5 µM** (1206 genes, none with an alert; 12 shown): [[TFDP2]] 0.300× (z -19.3, 47/48 lines), [[KLHL24]] 0.0978× (z -18.8, 48/48 lines), [[PDCD4]] 0.227× (z -17.0, 46/48 lines), [[RB1CC1]] 0.268× (z -16.9, 48/48 lines), [[FBXL20]] 0.198× (z -16.4, 48/48 lines), [[YPEL2]] 0.177× (z -15.3, 42/44 lines), [[FBXO25]] 0.273× (z -14.9, 40/42 lines), [[CCDC28A]] 0.194× (z -14.8, 44/47 lines), [[GARRE1]] 0.287× (z -14.3, 45/48 lines), [[CREBRF]] 0.173× (z -14.3, 48/48 lines), [[REPS2]] 0.167× (z -13.9, 32/34 lines), [[JMY]] 0.193× (z -13.9, 47/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 179]] (+3.0) | [[Module 182]] (-2.5), [[Module 076]] (-2.1) |
| 0.5 µM | — | — |
| 5 µM | [[Module 001]] (+4.2), [[Module 005]] (+4.1), [[Module 033]] (+3.6) | [[Module 069]] (-7.1), [[Module 145]] (-6.5), [[Module 234]] (-6.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW48 (line)]] (1.81), [[SNU-1 (line)]] (1.46), [[LoVo (line)]] (1.38), [[Hs 766T (line)]] (1.38) · weakest: [[NCI-H2347 (line)]] (0.683), [[SHP-77 (line)]] (0.685), [[A-172 (line)]] (0.706) |
| 0.5 µM | — | — |
| 5 µM | [[Panc 03.27 (line)]] (-6.0), [[RPMI-7951 (line)]] (-4.3), [[Hs 766T (line)]] (-4.0), [[CFPAC-1 (line)]] (-3.5) | [[AsPC-1 (line)]] (1.43), [[MIA PaCa-2 (line)]] (1.41), [[NCI-H1792 (line)]] (1.33), [[NCI-H460 (line)]] (1.31) · weakest: [[LS 180 (line)]] (0.628), [[A-427 (line)]] (0.740), [[AN3 CA (line)]] (0.788) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[c-Kit-IN-1 (drug)]] (+0.96, Multi-TK inhibitor); [[EX229 (drug)]] (+0.90, unclear); [[Abemaciclib (drug)]] (+0.89, CDK inhibitor); [[venetoclax (drug)]] (+0.87, unclear); [[Volasertib (drug)]] (+0.61, unclear); [[Belzutifan (drug)]] (+0.59, unclear); [[Everolimus (drug)]] (+0.55, MTOR inhibitor); [[Sapanisertib (drug)]] (+0.54, MTOR inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 83 arrows, 83 of them with an alert ⚠; grade A 0, B 78, C 5. Shown: the 15 strongest; 68 more arrows (68 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000283240]] | 0.05 µM | B | ENSG00000283240 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000283240 (19) vs lines expressing it (29) | the lines without ENSG00000283240: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: MGST1, IL1R2, STON2 |
| [[PLEKHA6]] | 0.05 µM | B | PLEKHA6 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express PLEKHA6 (16) vs lines expressing it (32) | the lines without PLEKHA6: 1.17× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[AQP3]] | 0.05 µM | B | AQP3 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 1.18× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[INAVA]], [[MROH3P]] | 0.05 µM | B | INAVA, MROH3P activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express INAVA, MROH3P (29) vs lines expressing them (19) | the lines without INAVA, MROH3P: 1.19× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[IL1RN]] | 0.05 µM | B | IL1RN activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express IL1RN (27) vs lines expressing it (21) | the lines without IL1RN: 1.22× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[TMEM92-AS1]] | 0.05 µM | B | TMEM92-AS1 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express TMEM92-AS1 (16) vs lines expressing it (32) | the lines without TMEM92-AS1: 1.15× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[SGPP2]] | 0.05 µM | B | SGPP2 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express SGPP2 (32) vs lines expressing it (16) | the lines without SGPP2: 1.21× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[B3GNT3]] | 0.05 µM | B | B3GNT3 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express B3GNT3 (31) vs lines expressing it (17) | the lines without B3GNT3: 1.20× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[SPTLC3]] | 0.05 µM | B | SPTLC3 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 1.18× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[KITLG]] | 0.05 µM | B | KITLG activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express KITLG (10) vs lines expressing it (38) | the lines without KITLG: 1.23× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[CATSPERB]] | 0.05 µM | B | CATSPERB activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express CATSPERB (30) vs lines expressing it (18) | the lines without CATSPERB: 1.20× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[ENSG00000287003]] | 0.05 µM | B | ENSG00000287003 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000287003 (20) vs lines expressing it (28) | the lines without ENSG00000287003: 1.13× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: TMEM154, ALOX5, RASSF6 |
| [[ATP2C2]] | 0.05 µM | B | ATP2C2 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.23× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[MAL2]] | 0.05 µM | B | MAL2 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express MAL2 (31) vs lines expressing it (17) | the lines without MAL2: 1.19× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[ABCC3]] | 0.05 µM | B | ABCC3 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express ABCC3 (16) vs lines expressing it (32) | the lines without ABCC3: 1.18× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 963 arrows, 963 of them with an alert ⚠; grade A 0, B 963, C 0. Shown: the 15 strongest; 948 more arrows (948 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MAP2K1]] | [[ST3GAL6]] | moves it that way too | B | MAP2K1 activity raises ST3GAL6's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | [[PIH1D1]] | moves it that way too | B | MAP2K1 activity raises PIH1D1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds |
| [[MAP2K1]] | [[CCT2]] | does not move it that way (the class's other compounds do) | B | MAP2K1 activity raises CCT2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | [[EPHA2-AS1]] | does not move it that way (the class's other compounds do) | B | MAP2K1 activity raises EPHA2-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[LINC00963]] | does not move it that way (the class's other compounds do) | B | MAP2K1 activity lowers LINC00963's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | [[LRFN5]] | does not move it that way (the class's other compounds do) | B | MAP2K1 activity raises LRFN5's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[PFDN2]] | does not move it that way (the class's other compounds do) | B | MAP2K1 activity raises PFDN2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | [[PRKG2-AS1]] | does not move it that way (the class's other compounds do) | B | MAP2K1 activity raises PRKG2-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[RRP9]] | does not move it that way (the class's other compounds do) | B | MAP2K1 activity raises RRP9's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[TBC1D32]] | does not move it that way (the class's other compounds do) | B | MAP2K1 activity lowers TBC1D32's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[ZNF630]] | does not move it that way (the class's other compounds do) | B | MAP2K1 activity lowers ZNF630's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[FOXL1]] | moves it that way too | B | MAP2K1 activity raises FOXL1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | [[DOCK4]] | moves it that way too | B | MAP2K1 activity raises DOCK4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.009 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | [[KDSR]] | moves it that way too | B | MAP2K1 activity raises KDSR's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.009 | ⚠ off-target possible; 4 compounds |
| [[MAP2K1]] | [[CDYL2]] | moves it that way too | B | MAP2K1 activity raises CDYL2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds |

## Data

- `tables/drugs.parquet` — drug == "TAK-733"
- `tables/drugdoses.parquet` — dd in 973, 974, 975
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
