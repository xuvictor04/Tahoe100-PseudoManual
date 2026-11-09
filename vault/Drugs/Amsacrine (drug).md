---
drug: "Amsacrine"
type: "drug"
salt_base: "Amsacrine"
targets: "TOP2A"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 442
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Amsacrine

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TOP2A · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 31 / 442; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.17 / 0.45.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:H7 | 1 / 0 | — | +0.17 | -0.1/+0.0/-0.3 | — |
| 0.5 µM | [[Plate 05]]:H7 | 24 / 7 | — | +0.65 | +2.7/+0.2/+0.3 | — |
| 5 µM | [[Plate 14]]:H7 | 307 / 135 | 0.907 | -0.36 | +0.9/-3.5/+0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[SLCO5A1]] 1.24× (z +3.2, 4/42 lines)

**0.5 µM** (24 genes, none with an alert; 12 shown): [[MDM2]] 1.37× (z +6.8, 29/49 lines), [[ZMAT3]] 1.34× (z +4.9, 18/43 lines), [[DDB2]] 1.29× (z +4.4, 22/47 lines), [[PTCHD4]] 1.49× (z +4.1, 12/16 lines), [[BAX]] 1.33× (z +4.1, 17/48 lines), [[DDIAS]] 1.36× (z +3.9, 14/46 lines), [[FAS]] 1.29× (z +3.8, 12/40 lines), [[BTG2]] 1.40× (z +3.6, 12/40 lines), [[AEN]] 1.35× (z +3.6, 16/47 lines), [[FANCD2]] 1.23× (z +3.6, 16/47 lines), [[TP53INP1]] 1.40× (z +3.5, 17/40 lines), [[ATAD5]] 1.21× (z +3.5, 14/48 lines)

**5 µM** (307 genes, none with an alert; 12 shown): [[PSTPIP2]] 1.39× (z +7.7, 16/28 lines), [[ACTA2]] 1.64× (z +7.4, 19/36 lines), [[PID1]] 1.43× (z +6.9, 19/26 lines), [[TMEM132B]] 1.54× (z +6.9, 22/40 lines), [[NTN1]] 1.31× (z +6.7, 13/31 lines), [[PTCHD4]] 1.58× (z +6.6, 13/15 lines), [[SOCS4]] 1.22× (z +6.0, 20/48 lines), [[PURPL]] 1.37× (z +6.0, 13/23 lines), [[MDM2]] 1.22× (z +5.9, 24/48 lines), [[DRAM1]] 1.28× (z +5.9, 22/42 lines), [[CCDC26]] 1.37× (z +5.9, 14/44 lines), [[NKX3-1]] 1.62× (z +5.9, 22/34 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (7 genes, none with an alert): [[PIF1]] 0.750× (z -3.6, 18/47 lines), [[H2AC12]] 0.557× (z -3.5, 9/43 lines), [[PLK1]] 0.767× (z -3.4, 15/48 lines), [[H1-3]] 0.608× (z -3.3, 14/36 lines), [[ENSG00000254526]] 0.724× (z -3.1, 6/18 lines), [[GPI]] 0.812× (z -3.0, 22/48 lines), [[KIF20A]] 0.762× (z -3.0, 19/47 lines)

**5 µM** (135 genes, none with an alert; 12 shown): [[PIF1]] 0.545× (z -10.7, 33/47 lines), [[PLK1]] 0.627× (z -8.6, 34/48 lines), [[KIF14]] 0.711× (z -8.2, 29/47 lines), [[CENPE]] 0.726× (z -7.8, 32/48 lines), [[CIT]] 0.721× (z -7.7, 30/47 lines), [[ENSG00000284906]] 0.775× (z -7.5, 27/48 lines), [[KIF20A]] 0.621× (z -7.3, 28/47 lines), [[TROAP]] 0.708× (z -7.1, 25/48 lines), [[CCNF]] 0.738× (z -7.0, 26/48 lines), [[DLGAP5]] 0.671× (z -6.8, 34/46 lines), [[TACC3]] 0.762× (z -6.7, 22/48 lines), [[CCNB1]] 0.687× (z -6.7, 31/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 068]] (+3.9), [[Module 062]] (+3.4), [[Module 137]] (+3.1) | [[Module 022]] (-2.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[CHP-212 (line)]] (-3.9) | [[SNU-1 (line)]] (2.68), [[SW48 (line)]] (2.40), [[NCI-H460 (line)]] (2.30), [[A549 (line)]] (2.21) · weakest: [[RPMI-7951 (line)]] (0.238), [[SHP-77 (line)]] (0.402), [[C-33 A (line)]] (0.413) |
| 5 µM | [[CHP-212 (line)]] (-4.7), [[H4 (line)]] (-4.1), [[A549 (line)]] (-3.7), [[C32 (line)]] (-3.3) | [[A549 (line)]] (2.38), [[A498 (line)]] (1.89), [[A-172 (line)]] (1.84), [[SW48 (line)]] (1.82) · weakest: [[NCI-H23 (line)]] (0.425), [[C-33 A (line)]] (0.498), [[RPMI-7951 (line)]] (0.516) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Topotecan (hydrochloride) (drug)]] (+0.61, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: toxic; cell-cycle shift); [[Cytarabine (hydrochloride) (drug)]] (+0.60, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Vitamin K4 (drug)]] (+0.59, unclear); [[Benztropine (mesylate) (drug)]] (+0.57, unclear); [[Oxaprozin (drug)]] (+0.55, Cyclooxygenase inhibitor); [[Bestatin (hydrochloride) (drug)]] (+0.49, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.46, unclear); [[IQ 1 (drug)]] (+0.45, unclear); [[Mitoxantrone (dihydrochloride) (drug)]] (+0.45, DNA synthesis/repair inhibitor); [[Meloxicam (drug)]] (+0.45, Cyclooxygenase inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 20 arrows, 20 of them with an alert ⚠; grade A 0, B 18, C 2. Shown: the 15 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[BATF]] | 5 µM | B | BATF activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express BATF (33) vs lines expressing it (15) | the lines without BATF: 0.84× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[AOX1]] | 5 µM | B | AOX1 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.08× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.20× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[EPCAM]] | 5 µM | B | EPCAM activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.86× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[MSRB3]] | 5 µM | B | MSRB3 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 1.17× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[ENSG00000260710]] | 5 µM | B | ENSG00000260710 activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express ENSG00000260710 (19) vs lines expressing it (29) | the lines without ENSG00000260710: 0.85× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: LAD1, TRIM29, NOS3; maybe low, not absent |
| [[ENSG00000266877]] | 5 µM | B | ENSG00000266877 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express ENSG00000266877 (22) vs lines expressing it (26) | the lines without ENSG00000266877: 1.09× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: KCNMA1, BASP1, F2RL2 |
| [[LRG1]] | 5 µM | B | LRG1 activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express LRG1 (28) vs lines expressing it (20) | the lines without LRG1: 0.85× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[NAV3]] | 5 µM | B | NAV3 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express NAV3 (16) vs lines expressing it (32) | the lines without NAV3: 1.17× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.17× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ENSG00000230615]] | 5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.11× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[CRACDL]] | 5 µM | B | CRACDL activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express CRACDL (25) vs lines expressing it (23) | the lines without CRACDL: 0.85× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[PCDH1]] | 5 µM | B | PCDH1 activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express PCDH1 (20) vs lines expressing it (28) | the lines without PCDH1: 0.86× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[COL27A1]] | 5 µM | B | COL27A1 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express COL27A1 (12) vs lines expressing it (36) | the lines without COL27A1: 1.16× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[FAAH2]] | 5 µM | B | FAAH2 activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.92× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4,166 arrows, 4,166 of them with an alert ⚠; grade A 0, B 4,166, C 0. Shown: the 15 strongest; 4,151 more arrows (4,151 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[TOP2A]] | [[G2E3]] | moves it that way too | B | TOP2A activity raises G2E3's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.5% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[RABL2B]] | moves it that way too | B | TOP2A activity lowers RABL2B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[RASSF8-AS1]] | moves it that way too | B | TOP2A activity lowers RASSF8-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000285667]] | moves it that way too | B | TOP2A activity lowers ENSG00000285667's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[LRRIQ3]] | moves it that way too | B | TOP2A activity lowers LRRIQ3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[BAX]] | moves it that way too | B | TOP2A activity lowers BAX's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[CIBAR1-DT]] | moves it that way too | B | TOP2A activity lowers CIBAR1-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000287400]] | moves it that way too | B | TOP2A activity lowers ENSG00000287400's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[MIDEAS]] | moves it that way too | B | TOP2A activity raises MIDEAS's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[TARID]] | moves it that way too | B | TOP2A activity lowers TARID's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ZNF665]] | moves it that way too | B | TOP2A activity lowers ZNF665's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[AK1]] | moves it that way too | B | TOP2A activity lowers AK1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[CAMKK1]] | moves it that way too | B | TOP2A activity raises CAMKK1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000228566]] | moves it that way too | B | TOP2A activity lowers ENSG00000228566's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[FCGBP]] | moves it that way too | B | TOP2A activity lowers FCGBP's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Amsacrine"
- `tables/drugdoses.parquet` — dd in 87, 88, 89
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
