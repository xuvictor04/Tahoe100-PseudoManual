---
drug: "Ponatinib"
type: "drug"
salt_base: "Ponatinib"
targets: "ABL1, PDGFRA, KDR, FGFR1, SRC, KIT"
moa_fine: "Multi-TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 3510
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Ponatinib

*Multi-TK inhibitor (inhibitor/antagonist) · targets: ABL1, PDGFRA, KDR, FGFR1, SRC, KIT · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 83 / 1701 / 3510; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.48 / 0.79.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A11 | 47 / 36 | — | +0.77 | +1.4/+1.3/-0.5 | — |
| 0.5 µM | [[Plate 11]]:A11 | 1,396 / 305 | — | -0.17 | -0.2/+0.2/-2.2 | — |
| 5 µM | [[Plate 12]]:A11 | 2,439 / 1,071 | — | +0.41 | -0.5/-0.7/-2.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (47 genes, none with an alert; 12 shown): [[OSBPL1A]] 1.23× (z +5.6, 22/46 lines), [[TRERF1]] 1.28× (z +4.6, 25/42 lines), [[MAP2K6]] 1.66× (z +4.5, 16/26 lines), [[EPHA1]] 1.51× (z +4.5, 0/22 lines), [[TM7SF3]] 1.21× (z +4.5, 18/48 lines), [[NUAK1]] 1.25× (z +4.2, 10/43 lines), [[GALM]] 1.41× (z +4.2, 18/37 lines), [[PIP4P2]] 1.27× (z +4.1, 22/44 lines), [[EPB41L4B]] 1.29× (z +4.0, 13/39 lines), [[CAT]] 1.29× (z +4.0, 15/47 lines), [[LRIG3]] 1.32× (z +3.9, 9/42 lines), [[PM20D2]] 1.26× (z +3.8, 11/44 lines)

**0.5 µM** (1396 genes, none with an alert; 12 shown): [[MAP2K6]] 3.86× (z +12.0, 23/25 lines), [[SRGAP3]] 1.75× (z +8.0, 36/46 lines), [[PIK3C2B]] 1.58× (z +7.6, 25/44 lines), [[ENSG00000264808]] 2.00× (z +7.3, 23/43 lines), [[RHOXF1]] 1.61× (z +7.2, 32/47 lines), [[EFCAB7]] 1.49× (z +6.8, 19/47 lines), [[EEF2K]] 1.34× (z +6.8, 35/48 lines), [[PKIB]] 1.51× (z +6.7, 15/39 lines), [[TMC3-AS1]] 2.16× (z +6.6, 20/40 lines), [[SCN9A]] 1.67× (z +6.6, 20/26 lines), [[DIXDC1]] 1.39× (z +6.6, 28/48 lines), [[TRERF1]] 1.43× (z +6.5, 31/42 lines)

**5 µM** (2439 genes, none with an alert; 12 shown): [[MAP2K6]] 7.29× (z +17.7, 24/25 lines), [[IDH1]] 2.70× (z +14.0, 44/48 lines), [[JDP2]] 2.54× (z +13.3, 25/35 lines), [[PSAT1]] 2.74× (z +12.9, 38/40 lines), [[ATP8A1]] 1.92× (z +11.9, 24/35 lines), [[PCK2]] 2.33× (z +11.8, 39/45 lines), [[PECR]] 1.76× (z +11.4, 35/46 lines), [[PHGDH]] 2.39× (z +10.7, 40/43 lines), [[TM7SF3]] 1.58× (z +10.7, 41/48 lines), [[NBR2]] 2.07× (z +10.7, 41/48 lines), [[DMGDH]] 3.47× (z +10.7, 35/40 lines), [[SCN9A]] 2.27× (z +10.6, 21/26 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (36 genes, none with an alert; 12 shown): [[CREB5]] 0.766× (z -4.7, 17/33 lines), [[DUSP16]] 0.816× (z -4.5, 23/46 lines), [[ENSG00000239462]] 0.715× (z -4.2, 14/30 lines), [[PVR]] 0.825× (z -4.1, 19/48 lines), [[KRTAP5-AS1]] 0.679× (z -3.8, 15/33 lines), [[MYOSLID]] 0.642× (z -3.7, 8/33 lines), [[PDLIM3]] 0.758× (z -3.7, 3/28 lines), [[IRGQ]] 0.754× (z -3.7, 10/48 lines), [[ENSG00000234261]] 0.731× (z -3.6, 3/19 lines), [[DUSP5-DT]] 0.714× (z -3.5, 12/39 lines), [[NPC1]] 0.803× (z -3.5, 26/47 lines), [[LRP8]] 0.762× (z -3.5, 13/46 lines)

**0.5 µM** (305 genes, none with an alert; 12 shown): [[DIAPH1]] 0.796× (z -6.7, 31/48 lines), [[ERRFI1]] 0.608× (z -6.2, 41/44 lines), [[ACSL4]] 0.791× (z -6.2, 29/47 lines), [[PITPNB]] 0.817× (z -6.1, 26/48 lines), [[CD59]] 0.710× (z -6.1, 30/41 lines), [[EHD4]] 0.752× (z -6.0, 33/48 lines), [[YES1]] 0.823× (z -5.8, 22/48 lines), [[SLC4A7]] 0.760× (z -5.7, 31/45 lines), [[YWHAZ]] 0.783× (z -5.7, 40/48 lines), [[ETS1]] 0.729× (z -5.5, 28/37 lines), [[CXCL8]] 0.541× (z -5.4, 25/28 lines), [[LIF]] 0.629× (z -5.4, 25/38 lines)

**5 µM** (1071 genes, none with an alert; 12 shown): [[HRH1]] 0.499× (z -12.5, 36/38 lines), [[TGM2]] 0.342× (z -11.9, 32/32 lines), [[SPRY4]] 0.434× (z -10.8, 41/48 lines), [[DUSP6]] 0.302× (z -10.6, 42/44 lines), [[STK17A]] 0.654× (z -10.6, 37/46 lines), [[MCL1]] 0.509× (z -10.6, 43/48 lines), [[TEAD4]] 0.582× (z -10.3, 39/45 lines), [[LUCAT1]] 0.516× (z -10.0, 36/40 lines), [[DUSP5]] 0.454× (z -10.0, 35/41 lines), [[IL1RAP]] 0.549× (z -10.0, 34/40 lines), [[SPRY4-AS1]] 0.388× (z -9.8, 37/45 lines), [[ZNFX1]] 0.591× (z -9.8, 39/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 045]] (+3.1) | — |
| 0.5 µM | [[Module 146]] (+4.2), [[Module 230]] (+3.2), [[Module 045]] (+2.8) | [[Module 184]] (-2.2) |
| 5 µM | [[Module 146]] (+6.3), [[Module 045]] (+5.8), [[Module 171]] (+5.6) | [[Module 160]] (-5.7), [[Module 174]] (-5.2), [[Module 151]] (-3.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[KATO III (line)]] (1.66), [[H4 (line)]] (1.56), [[SW 1088 (line)]] (1.40), [[NCI-H1573 (line)]] (1.39) · weakest: [[NCI-H2347 (line)]] (0.500), [[HEC-1-A (line)]] (0.525), [[SNU-1 (line)]] (0.531) |
| 0.5 µM | [[CHP-212 (line)]] (-3.3) | [[KATO III (line)]] (1.55), [[NCI-H1792 (line)]] (1.26), [[H4 (line)]] (1.20), [[NCI-H23 (line)]] (1.19) · weakest: [[C32 (line)]] (0.303), [[SW48 (line)]] (0.362), [[SHP-77 (line)]] (0.444) |
| 5 µM | [[HepG2_C3A (line)]] (-6.0), [[C32 (line)]] (-5.9), [[AN3 CA (line)]] (-5.8), [[CHP-212 (line)]] (-5.2), [[A-427 (line)]] (-4.7) | [[H4 (line)]] (1.46), [[KATO III (line)]] (1.42), [[NCI-H23 (line)]] (1.38), [[J82 (line)]] (1.25) · weakest: [[SW48 (line)]] (0.102), [[C32 (line)]] (0.183), [[NCI-H661 (line)]] (0.291) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Cabozantinib (S-malate) (drug)]] (+0.87, Multi-TK inhibitor); [[Afatinib (drug)]] (+0.80, EGFR/ERBB inhibitor); [[Regorafenib (drug)]] (+0.73, Multi-TK inhibitor); [[Radotinib (drug)]] (+0.72, Other TK inhibitor); [[Flumatinib (mesylate) (drug)]] (+0.67, Other TK inhibitor); [[Vandetanib (drug)]] (+0.66, Multi-TK inhibitor); [[Ixazomib (drug)]] (+0.54, Proteasome inhibitor); [[Perindopril (erbumine) (drug)]] (+0.54, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Ponatinib 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.84× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Ponatinib 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.86× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[RSPO3]] | 0.05 µM | B | RSPO3 activity raises the cells' numbers under Ponatinib 0.05 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.83× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[BMPER]] | 0.05 µM | B | BMPER activity raises the cells' numbers under Ponatinib 0.05 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.87× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[SETD7]] | 5 µM | C | SETD7 activity raises the cells' numbers under Ponatinib 5 µM (protects the cells) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 0.46× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| [[ISG20]] | 0.05 µM | C | ISG20 activity raises the cells' numbers under Ponatinib 0.05 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.72× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| [[TBILA]] | 0.05 µM | C | TBILA activity raises the cells' numbers under Ponatinib 0.05 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.78× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[STX1A]] | 5 µM | C | STX1A activity raises the cells' numbers under Ponatinib 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.56× the cells of the other lines | 0.078 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[ZNF423]] | 5 µM | C | ZNF423's natural level lowers the cells' numbers under Ponatinib 5 µM (makes them more sensitive) | ZNF423's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.72 | 0.285 over the table, 0.070 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[RC3H1]] | 0.05 µM | C | RC3H1's natural level lowers the cells' numbers under Ponatinib 0.05 µM (makes them more sensitive) | RC3H1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.081 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 74 arrows, 74 of them with an alert ⚠; grade A 0, B 74, C 0. Shown: the 15 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[ABL1]] | [[ANKMY2]] | moves it that way too | B | ABL1 activity lowers ANKMY2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 2.8% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| KIT | [[PKD1P6]] | moves it that way too | B | KIT activity lowers PKD1P6's level | compounds that target KIT: 3 of 4 raise it (Pexidartinib, Ponatinib, c-Kit-IN-1) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[CDKN2B]] | moves it that way too | B | ABL1 activity raises CDKN2B's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[GSG1L]] | moves it that way too | B | ABL1 activity raises GSG1L's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[TMEM185A]] | moves it that way too | B | ABL1 activity lowers TMEM185A's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.4% of all compounds | 0.025 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[NUAK1]] | moves it that way too | B | ABL1 activity lowers NUAK1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.6% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CAMK2G]] | moves it that way too | B | ABL1 activity lowers CAMK2G's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.9% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| KDR | [[PPARD]] | moves it that way too | B | KDR activity raises PPARD's level | compounds that target KDR: 5 of 8 lower it (Cabozantinib, Ponatinib, Regorafenib, Sulfatinib, Sunitinib) | 62% of the class's compounds vs 6.2% of all compounds | 0.036 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ABL1]] | [[CDKN1A]] | moves it that way too | B | ABL1 activity raises CDKN1A's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ENSG00000225218]] | moves it that way too | B | ABL1 activity raises ENSG00000225218's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ENSG00000290241]] | moves it that way too | B | ABL1 activity raises ENSG00000290241's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[HEATR6]] | moves it that way too | B | ABL1 activity lowers HEATR6's level | compounds that target ABL1: 3 of 6 raise it (Flumatinib, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds |
| [[ABL1]] | [[PRKAB2]] | moves it that way too | B | ABL1 activity lowers PRKAB2's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[SLC8A2]] | moves it that way too | B | ABL1 activity raises SLC8A2's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ALDH7A1]] | moves it that way too | B | ABL1 activity lowers ALDH7A1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Ponatinib"
- `tables/drugdoses.parquet` — dd in 830, 831, 832
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
