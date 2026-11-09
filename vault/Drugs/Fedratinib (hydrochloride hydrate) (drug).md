---
drug: "Fedratinib (hydrochloride hydrate)"
type: "drug"
salt_base: "Fedratinib"
targets: "JAK2, FLT3, RET"
moa_fine: "JAK/STAT inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1767
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Fedratinib (hydrochloride hydrate)

*JAK/STAT inhibitor (inhibitor/antagonist) · targets: JAK2, FLT3, RET · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 18 / 1767; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.41 / 0.53.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:F10 | 1 / 0 | — | +0.00 | +0.6/+1.1/+1.1 | — |
| 0.5 µM | [[Plate 11]]:F10 | 9 / 9 | — | +0.09 | +0.5/+0.4/+0.4 | — |
| 5 µM | [[Plate 12]]:F10 | 881 / 886 | — | +0.09 | -0.5/-0.1/+0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[CFAP210]] 1.67× (z +2.8, 10/45 lines)

**0.5 µM** (9 genes, none with an alert): [[ZBTB45]] 1.38× (z +3.7, 6/43 lines), [[CYB5D2]] 1.22× (z +3.5, 5/47 lines), [[SCN9A]] 1.31× (z +3.5, 2/25 lines), [[PALM]] 1.28× (z +3.1, 0/26 lines), [[TCTA]] 1.26× (z +3.1, 1/44 lines), [[ABCA3]] 1.23× (z +3.0, 3/38 lines), [[MSH4]] 1.35× (z +2.9, 4/43 lines), [[ENSG00000253363]] 1.40× (z +2.9, 0/9 lines), [[CXCL13]] 1.41× (z +2.8, 2/36 lines)

**5 µM** (881 genes, none with an alert; 12 shown): [[EFR3B]] 2.39× (z +14.3, 30/37 lines), [[SESN3]] 2.03× (z +12.4, 26/28 lines), [[PEG10]] 2.10× (z +10.3, 28/32 lines), [[B3GALT1]] 1.70× (z +9.6, 19/27 lines), [[MEGF9]] 1.44× (z +9.3, 32/48 lines), [[TYW1B]] 1.69× (z +9.2, 41/49 lines), [[SERPINI1]] 1.89× (z +9.1, 28/43 lines), [[CASTOR2]] 1.75× (z +9.1, 34/47 lines), [[ATP8A1]] 1.60× (z +8.6, 20/35 lines), [[ZCCHC24]] 1.56× (z +8.6, 27/43 lines), [[ITFG2]] 1.57× (z +8.6, 41/48 lines), [[CPEB4]] 1.38× (z +8.4, 38/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (9 genes, none with an alert): [[OAS2]] 0.612× (z -3.6, 22/34 lines), [[SPRY4]] 0.785× (z -3.1, 14/48 lines), [[CMPK2]] 0.692× (z -2.9, 11/36 lines), [[PARP12]] 0.818× (z -2.8, 18/46 lines), [[DDX60]] 0.780× (z -2.8, 16/43 lines), [[HERC5]] 0.805× (z -2.7, 12/33 lines), [[ITGA2]] 0.823× (z -2.6, 16/38 lines), [[IFI44]] 0.810× (z -2.6, 13/37 lines), [[ANTXR2]] 0.818× (z -2.5, 10/39 lines)

**5 µM** (886 genes, none with an alert; 12 shown): [[OAS3]] 0.181× (z -18.2, 41/44 lines), [[MX1]] 0.200× (z -16.9, 27/30 lines), [[OAS2]] 0.118× (z -15.9, 34/34 lines), [[IFI44]] 0.277× (z -15.8, 32/37 lines), [[IFI44L]] 0.181× (z -15.1, 24/26 lines), [[CMPK2]] 0.162× (z -14.4, 32/36 lines), [[TRIM22]] 0.260× (z -13.7, 28/30 lines), [[DDX60]] 0.295× (z -13.6, 36/43 lines), [[PARP9]] 0.329× (z -13.5, 37/42 lines), [[EIF2AK2]] 0.479× (z -13.2, 32/48 lines), [[XAF1]] 0.208× (z -13.0, 32/34 lines), [[PHF11]] 0.469× (z -12.8, 37/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 002]] (+3.5), [[Module 043]] (+3.1), [[Module 040]] (+2.4) | [[Module 032]] (-6.2), [[Module 006]] (-3.6), [[Module 070]] (-3.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[CHP-212 (line)]] (-5.3), [[H4 (line)]] (-4.3), [[A-172 (line)]] (-3.8) | [[SNU-423 (line)]] (1.42), [[MIA PaCa-2 (line)]] (1.39), [[A-172 (line)]] (1.36), [[RPMI-7951 (line)]] (1.30) · weakest: [[NCI-H661 (line)]] (0.451), [[AN3 CA (line)]] (0.565), [[A-427 (line)]] (0.597) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[HI-TOPK-032 (drug)]] (+0.55, unclear); [[Tofacitinib (citrate) (drug)]] (+0.53, JAK/STAT inhibitor); [[Ciclopirox (drug)]] (+0.52, unclear); [[Ixazomib (drug)]] (+0.48, Proteasome inhibitor); [[Berbamine (dihydrochloride) (drug)]] (+0.47, unclear); [[Tofacitinib (drug)]] (+0.47, JAK/STAT inhibitor); [[Crizotinib (hydrochloride) (drug)]] (+0.42, Multi-TK inhibitor); [[Almonertinib (mesylate) (drug)]] (+0.40, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000287263]] | 5 µM | B | ENSG00000287263 activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express ENSG00000287263 (15) vs lines expressing it (33) | the lines without ENSG00000287263: 0.86× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: PRTFDC1, LINC01273, LINC02086 |
| [[STX1A]] | 5 µM | C | STX1A activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.57× the cells of the other lines | 0.002 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[RILP]] | 5 µM | C | RILP activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.64× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[ENSG00000255031]] | 5 µM | C | ENSG00000255031 activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express ENSG00000255031 (3) vs lines expressing it (45) | the lines without ENSG00000255031: 0.63× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: GLMP, TCIRG1, MT1X; maybe low, not absent |
| [[ENSG00000257252]] | 5 µM | C | ENSG00000257252 activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express ENSG00000257252 (4) vs lines expressing it (44) | the lines without ENSG00000257252: 0.68× the cells of the other lines | 0.022 | ⚠ few lines (4 vs 46); across organs; also absent: PTPN6, ENSG00000248993; maybe low, not absent |
| [[VRK2]] | 5 µM | C | VRK2 activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.69× the cells of the other lines | 0.022 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| [[PYGB]] | 5 µM | C | PYGB activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.65× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| [[LPIN3]] | 5 µM | C | LPIN3 activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express LPIN3 (6) vs lines expressing it (42) | the lines without LPIN3: 0.73× the cells of the other lines | 0.045 | ⚠ tissue-confounded; across organs; also absent: TNFRSF10D, TACC2, PTER |
| [[ENSG00000291063]] | 5 µM | C | ENSG00000291063 activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express ENSG00000291063 (5) vs lines expressing it (43) | the lines without ENSG00000291063: 0.73× the cells of the other lines | 0.047 | ⚠ tissue-confounded; across organs; also absent: RNF135, ENSG00000266865, TMEM54; maybe low, not absent |
| [[KDM7A-DT]] | 5 µM | C | KDM7A-DT activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express KDM7A-DT (4) vs lines expressing it (44) | the lines without KDM7A-DT: 0.71× the cells of the other lines | 0.048 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent |
| [[CYB561]] | 5 µM | C | CYB561 activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express CYB561 (3) vs lines expressing it (45) | the lines without CYB561: 0.68× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); across organs; also absent: MATN1-AS1, E2F8, PBX4; maybe low, not absent |
| [[DLGAP2]] | 5 µM | C | DLGAP2's natural level lowers the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (makes them more sensitive) | DLGAP2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.72 | 0.206 over the table, 0.011 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 33 arrows, 33 of them with an alert ⚠; grade A 0, B 33, C 0. Shown: the 15 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[JAK2]] | [[TAP2]] | moves it that way too | B | JAK2 activity raises TAP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[OGFR]] | moves it that way too | B | JAK2 activity raises OGFR's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[TRIM25]] | moves it that way too | B | JAK2 activity raises TRIM25's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[ADAR]] | moves it that way too | B | JAK2 activity raises ADAR's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[STRIP2]] | moves it that way too | B | JAK2 activity raises STRIP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[NAMPT]] | moves it that way too | B | JAK2 activity raises NAMPT's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[ZSCAN5A]] | moves it that way too | B | JAK2 activity lowers ZSCAN5A's level | compounds that target JAK2: 2 of 3 raise it (Fedratinib, Filgotinib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds |
| [[JAK2]] | [[IL15]] | moves it that way too | B | JAK2 activity raises IL15's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[PATL1]] | moves it that way too | B | JAK2 activity raises PATL1's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[TRAF3IP2]] | moves it that way too | B | JAK2 activity raises TRAF3IP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[IL15RA]] | moves it that way too | B | JAK2 activity raises IL15RA's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[PLEKHA4]] | moves it that way too | B | JAK2 activity raises PLEKHA4's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[ENSG00000291144]] | moves it that way too | B | JAK2 activity raises ENSG00000291144's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[BIRC3]] | moves it that way too | B | JAK2 activity raises BIRC3's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[CFB]] | moves it that way too | B | JAK2 activity raises CFB's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

## Data

- `tables/drugs.parquet` — drug == "Fedratinib (hydrochloride hydrate)"
- `tables/drugdoses.parquet` — dd in 438, 439, 440
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
