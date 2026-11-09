---
drug: "NG25"
type: "drug"
salt_base: "NG25"
targets: "MAP4K2, MAP3K7, LYN, ABL1, ABL2, FER, SRC, EPHA2, EPHB2, EPHB4, ZAK, ZKSCAN1, RAF1"
moa_fine: "Other MAPK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 2239
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# NG25

*Other MAPK inhibitor (inhibitor/antagonist) · targets: MAP4K2, MAP3K7, LYN, ABL1, ABL2, FER, SRC, EPHA2, EPHB2, EPHB4, ZAK, ZKSCAN1, RAF1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 35 / 6 / 2239; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.39 / -0.08.
> Flags by dose: - / noisy plate (z scaled) / cell-cycle shift; noisy plate (z scaled). ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:G6 | 23 / 12 | — | -0.30 | +0.3/+1.7/+2.0 | — |
| 0.5 µM | [[Plate 02]]:G6 | 5 / 1 | — | -0.44 | -0.6/+0.2/-0.8 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G6 | 805 / 1,434 | — | -0.00 | -0.4/+6.3/+1.4 | ⚠ cell-cycle shift · noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (23 genes, none with an alert; 12 shown): [[TMEM107]] 1.47× (z +4.1, 12/48 lines), [[RABGGTA]] 1.43× (z +3.9, 4/43 lines), [[GTF2H2C]] 1.37× (z +3.8, 8/44 lines), [[HSP90AB3P]] 1.57× (z +3.6, 10/42 lines), [[COPS8]] 1.22× (z +3.6, 14/48 lines), [[ARL2BP]] 1.21× (z +3.6, 8/48 lines), [[HSP90AA1]] 1.49× (z +3.5, 42/49 lines), [[HSPD1]] 1.40× (z +3.4, 38/49 lines), [[TRIM28]] 1.24× (z +3.4, 13/48 lines), [[TYW3]] 1.27× (z +3.4, 9/48 lines), [[NFYB]] 1.24× (z +3.2, 8/48 lines), [[SCAMP4]] 1.20× (z +3.2, 7/48 lines)

**0.5 µM** (5 genes, none with an alert): [[RIPK4]] 1.62× (z +3.7, 16/35 lines), [[ZNF331]] 1.26× (z +3.3, 4/33 lines), [[TIPARP]] 1.97× (z +3.2, 21/47 lines), [[MIR181A1HG]] 1.34× (z +3.2, 14/41 lines), [[TPRA1]] 1.30× (z +2.9, 8/48 lines)

**5 µM** (805 genes, 319 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 18 shown): [[HSP90AA1]] 6.50× (z +9.3, 47/47 lines; cell-cycle shift (explains ~15% here)), [[GTF3C3]] 1.82× (z +9.1, 33/47 lines; cell-cycle shift (explains ~0% here)), [[AURKA]] ⚠ 3.30× (z +8.6, 42/47 lines; cell-cycle shift, explains ~69% of this change), [[DNAJB4]] 2.85× (z +8.2, 33/45 lines; cell-cycle shift (explains ~7% here)), [[GAS2L3]] ⚠ 2.46× (z +8.2, 40/47 lines; cell-cycle shift, explains ~69% of this change), [[CENPF]] ⚠ 3.43× (z +8.0, 41/45 lines; cell-cycle shift, explains ~77% of this change), [[HSPA4L]] 2.48× (z +7.9, 37/44 lines; cell-cycle shift (explains ~0% here)), [[BRD8]] ⚠ 1.92× (z +7.9, 37/47 lines; cell-cycle shift, explains ~48% of this change), [[HSP90AB1]] 3.42× (z +7.7, 47/47 lines; cell-cycle shift (explains ~19% here)), [[ASPM]] ⚠ 2.75× (z +7.5, 37/46 lines; cell-cycle shift, explains ~77% of this change), [[NEK2]] ⚠ 3.46× (z +7.4, 39/46 lines; cell-cycle shift, explains ~73% of this change), [[HSPH1]] 3.92× (z +7.4, 46/47 lines; cell-cycle shift (explains ~23% here)), [[CAP2]] 2.01× (z +7.4, 28/39 lines; cell-cycle shift (explains ~0% here)), [[PEG10]] 2.75× (z +7.3, 26/30 lines; cell-cycle shift (explains ~14% here)), [[INTU]] 2.17× (z +7.3, 29/43 lines; cell-cycle shift (explains ~0% here)), [[HSP90AA2P]] 5.01× (z +7.1, 20/29 lines; cell-cycle shift (explains ~9% here)), [[HIBCH]] 1.65× (z +7.1, 36/47 lines; cell-cycle shift (explains ~0% here)), [[SECISBP2L]] 1.57× (z +7.1, 39/47 lines; cell-cycle shift (explains ~16% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (12 genes, none with an alert): [[SUZ12P1]] 0.810× (z -3.9, 17/49 lines), [[ENSG00000285725]] 0.707× (z -3.4, 14/43 lines), [[LINC00265]] 0.776× (z -3.3, 14/45 lines), [[XYLB]] 0.812× (z -3.2, 13/48 lines), [[TMPRSS5]] 0.740× (z -3.2, 8/41 lines), [[ENSG00000285257]] 0.697× (z -3.2, 5/35 lines), [[BLOC1S5-TXNDC5]] 0.804× (z -3.2, 8/48 lines), [[METTL22]] 0.831× (z -3.0, 15/48 lines), [[CYP27C1]] 0.784× (z -3.0, 4/28 lines), [[PIGC]] 0.800× (z -2.9, 11/48 lines), [[ENSG00000291054]] 0.807× (z -2.8, 10/46 lines), [[ARHGEF4]] 0.826× (z -2.8, 5/34 lines)

**0.5 µM** (1 gene, none with an alert): [[ZFP36]] 0.618× (z -3.3, 21/45 lines)

**5 µM** (1434 genes, 575 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[MTHFD1L]] 0.421× (z -11.0, 42/44 lines; cell-cycle shift (explains ~15% here)), [[HIVEP1]] 0.358× (z -10.7, 44/46 lines; cell-cycle shift (explains ~0% here)), [[SPRY4-AS1]] 0.155× (z -10.1, 44/44 lines; cell-cycle shift (explains ~16% here)), [[RELB]] 0.393× (z -10.0, 44/47 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000259354]] 0.209× (z -9.6, 27/30 lines; cell-cycle shift (explains ~0% here)), [[IRAK2]] 0.323× (z -9.5, 35/39 lines; cell-cycle shift (explains ~0% here)), [[SKIL]] 0.347× (z -9.5, 44/45 lines; cell-cycle shift (explains ~0% here)), [[TNFAIP8]] 0.433× (z -9.3, 39/46 lines; cell-cycle shift (explains ~13% here)), [[LUCAT1]] 0.318× (z -9.1, 40/40 lines; cell-cycle shift (explains ~7% here)), [[OSMR-DT]] 0.302× (z -8.5, 30/32 lines; cell-cycle shift (explains ~22% here)), [[IL4R]] 0.302× (z -8.2, 36/43 lines; cell-cycle shift (explains ~0% here)), [[RHBDF2]] 0.408× (z -8.2, 33/42 lines; cell-cycle shift (explains ~8% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 060]] (+2.2) | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 057]] (+6.1), [[Module 045]] (+4.6), [[Module 064]] (+4.5) | [[Module 184]] (-4.0), [[Module 174]] (-3.5), [[Module 170]] (-3.4) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[HS-578T (line)]] (1.43), [[SK-MEL-2 (line)]] (1.38), [[LOX-IMVI (line)]] (1.30), [[C-33 A (line)]] (1.21) · weakest: [[NCI-H2122 (line)]] (-0.193), [[CHP-212 (line)]] (0.0447), [[RPMI-7951 (line)]] (0.554) |
| 0.5 µM | — | — |
| 5 µM | [[C32 (line)]] (-8.5), [[RPMI-7951 (line)]] (-6.8), [[H4 (line)]] (-5.9), [[CHP-212 (line)]] (-5.6), [[SW48 (line)]] (-4.9) | [[RKO (line)]] (1.30), [[NCI-H1573 (line)]] (1.21), [[A549 (line)]] (1.20), [[HOP62 (line)]] (1.17) · weakest: [[SW 1271 (line)]] (0.539), [[NCI-H661 (line)]] (0.680), [[SNU-1 (line)]] (0.739) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar.*

- [[Regorafenib (drug)]] (+0.60, Multi-TK inhibitor); [[Ixazomib (drug)]] (+0.53, Proteasome inhibitor); [[Radotinib (drug)]] (+0.52, Other TK inhibitor); [[Ponatinib (drug)]] (+0.50, Multi-TK inhibitor); [[Cabozantinib (S-malate) (drug)]] (+0.46, Multi-TK inhibitor); [[Furosemide (drug)]] (+0.45, unclear); [[Flumatinib (mesylate) (drug)]] (+0.44, Other TK inhibitor); [[Vandetanib (drug)]] (+0.43, Multi-TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KIAA1522]] | 5 µM | B | KIAA1522 activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express KIAA1522 (5) vs lines expressing it (43) | the lines without KIAA1522: 0.56× the cells of the other lines | 0.030 | ⚠ across organs; also absent: ENSG00000257489, TRIB3, PBX4 |
| [[MTMR7]] | 5 µM | B | MTMR7 activity lowers the cells' numbers under NG25 5 µM (makes them more sensitive) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 1.40× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[TRIB3]] | 5 µM | C | TRIB3 activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express TRIB3 (3) vs lines expressing it (45) | the lines without TRIB3: 0.40× the cells of the other lines | 0.009 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ARHGAP27, KIAA1522, ALOXE3; maybe low, not absent |
| [[LINC02068]] | 5 µM | C | LINC02068 activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express LINC02068 (3) vs lines expressing it (45) | the lines without LINC02068: 0.47× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: TRIB3; maybe low, not absent |
| [[DDAH1]] | 5 µM | C | DDAH1 activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express DDAH1 (3) vs lines expressing it (45) | the lines without DDAH1: 0.45× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| [[RILP]] | 5 µM | C | RILP activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.50× the cells of the other lines | 0.042 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[PLEKHN1]] | 5 µM | C | PLEKHN1 activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.49× the cells of the other lines | 0.054 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| [[ATAD1]], [[PTEN]] | 5 µM | C | ATAD1, PTEN activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.56× the cells of the other lines | 0.059 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| [[TNFRSF10D]] | 5 µM | C | TNFRSF10D activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express TNFRSF10D (11) vs lines expressing it (37) | the lines without TNFRSF10D: 0.71× the cells of the other lines | 0.088 | ⚠ tissue-confounded; across organs; also absent: OPLAH, LINC00857, LPIN3 |
| [[KDM7A-DT]] | 5 µM | C | KDM7A-DT activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express KDM7A-DT (4) vs lines expressing it (44) | the lines without KDM7A-DT: 0.59× the cells of the other lines | 0.0999 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 67 arrows, 67 of them with an alert ⚠; grade A 0, B 67, C 0. Shown: the 15 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[ABL1]] | [[ANKMY2]] | moves it that way too | B | ABL1 activity lowers ANKMY2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 2.8% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CDKN2B]] | moves it that way too | B | ABL1 activity raises CDKN2B's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[GSG1L]] | moves it that way too | B | ABL1 activity raises GSG1L's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[TMEM185A]] | moves it that way too | B | ABL1 activity lowers TMEM185A's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.4% of all compounds | 0.025 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[NUAK1]] | moves it that way too | B | ABL1 activity lowers NUAK1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.6% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CAMK2G]] | moves it that way too | B | ABL1 activity lowers CAMK2G's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.9% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CDKN1A]] | moves it that way too | B | ABL1 activity raises CDKN1A's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ENSG00000225218]] | moves it that way too | B | ABL1 activity raises ENSG00000225218's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ENSG00000290241]] | moves it that way too | B | ABL1 activity raises ENSG00000290241's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[HEATR6]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers HEATR6's level | compounds that target ABL1: 3 of 6 raise it (Flumatinib, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds |
| [[ABL1]] | [[PRKAB2]] | moves it that way too | B | ABL1 activity lowers PRKAB2's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[SLC8A2]] | moves it that way too | B | ABL1 activity raises SLC8A2's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ALDH7A1]] | moves it that way too | B | ABL1 activity lowers ALDH7A1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[ARL6]] | moves it that way too | B | ABL1 activity lowers ARL6's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[PIP4P2]] | moves it that way too | B | ABL1 activity lowers PIP4P2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "NG25"
- `tables/drugdoses.parquet` — dd in 699, 700, 701
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
