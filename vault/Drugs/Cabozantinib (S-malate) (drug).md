---
drug: "Cabozantinib (S-malate)"
type: "drug"
salt_base: "Cabozantinib"
targets: "MET, KDR, AXL"
moa_fine: "Multi-TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 626
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Cabozantinib (S-malate)

*Multi-TK inhibitor (inhibitor/antagonist) · targets: MET, KDR, AXL · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 87 / 69 / 626; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.69 / 0.44.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A12 | 77 / 10 | — | -0.33 | -0.3/-1.7/-1.1 | — |
| 0.5 µM | [[Plate 11]]:A12 | 60 / 9 | — | -0.37 | -0.2/-0.4/-0.9 | — |
| 5 µM | [[Plate 12]]:A12 | 435 / 191 | — | +0.19 | -0.1/-0.9/-2.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (77 genes, none with an alert; 12 shown): [[ENSG00000289293]] 1.49× (z +3.7, 5/45 lines), [[ENSG00000183308]] 1.24× (z +3.7, 6/47 lines), [[ENSG00000261427]] 1.57× (z +3.7, 6/40 lines), [[BTBD2]] 1.21× (z +3.6, 13/48 lines), [[DET1]] 1.30× (z +3.6, 13/46 lines), [[ZER1]] 1.27× (z +3.6, 18/48 lines), [[CHRNA10]] 1.56× (z +3.6, 2/38 lines), [[ZKSCAN7-AS1]] 1.37× (z +3.5, 10/46 lines), [[ZNF611]] 1.23× (z +3.5, 15/45 lines), [[UGDH-AS1]] 1.26× (z +3.5, 5/47 lines), [[ZNF813]] 1.30× (z +3.5, 4/33 lines), [[FAHD2A]] 1.23× (z +3.4, 5/47 lines)

**0.5 µM** (60 genes, none with an alert; 12 shown): [[ENSG00000289293]] 1.65× (z +4.7, 19/44 lines), [[ENSG00000254536]] 1.50× (z +4.6, 5/39 lines), [[PSTK]] 1.24× (z +3.8, 7/45 lines), [[PPP2R2B]] 1.43× (z +3.6, 3/22 lines), [[ENSG00000231424]] 1.38× (z +3.6, 0/40 lines), [[ENSG00000207751]] 1.43× (z +3.6, 3/44 lines), [[ENSG00000263551]] 1.38× (z +3.5, 3/15 lines), [[DANT1]] 1.50× (z +3.5, 1/26 lines), [[LINC02932]] 1.39× (z +3.5, 4/29 lines), [[LINC01091]] 1.39× (z +3.5, 4/29 lines), [[GBP2]] 1.26× (z +3.5, 11/35 lines), [[ZNF503-AS1]] 1.39× (z +3.5, 5/23 lines)

**5 µM** (435 genes, none with an alert; 12 shown): [[MAP2K6]] 2.41× (z +7.8, 21/26 lines), [[SRGAP3]] 1.49× (z +5.7, 27/46 lines), [[CFAP43]] 1.81× (z +5.6, 22/46 lines), [[LRIG3]] 1.49× (z +5.5, 20/41 lines), [[SLC25A12]] 1.29× (z +5.5, 23/48 lines), [[SDHAF4]] 1.40× (z +5.4, 15/47 lines), [[NSL1]] 1.28× (z +5.4, 22/48 lines), [[PPM1H]] 1.35× (z +5.3, 18/36 lines), [[HNMT]] 1.50× (z +5.3, 12/30 lines), [[ACP6]] 1.33× (z +5.0, 15/44 lines), [[GBP2]] 1.39× (z +5.0, 19/35 lines), [[ATP8A1]] 1.31× (z +4.9, 6/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[SKA1]] 0.775× (z -3.8, 9/45 lines), [[NUP188]] 0.824× (z -3.3, 11/48 lines), [[DUSP10]] 0.772× (z -3.3, 11/37 lines), [[TICRR]] 0.781× (z -3.2, 14/45 lines), [[C3orf52]] 0.753× (z -3.2, 18/42 lines), [[ANLN]] 0.801× (z -3.1, 22/46 lines), [[ARL5B]] 0.763× (z -3.1, 28/48 lines), [[CRY1]] 0.755× (z -3.0, 25/48 lines), [[TRIB1]] 0.809× (z -3.0, 14/42 lines), [[ARRDC3]] 0.807× (z -2.6, 19/48 lines)

**0.5 µM** (9 genes, none with an alert): [[DNAJB6]] 0.831× (z -3.8, 22/48 lines), [[UTP15]] 0.770× (z -3.5, 13/47 lines), [[C3orf52]] 0.742× (z -3.4, 19/42 lines), [[ELOVL5]] 0.791× (z -3.2, 17/42 lines), [[NUAK2]] 0.799× (z -3.0, 3/37 lines), [[EHD1]] 0.821× (z -2.8, 11/48 lines), [[SERPINB9]] 0.831× (z -2.8, 7/24 lines), [[PSMD14]] 0.824× (z -2.8, 20/48 lines), [[ENSG00000239462]] 0.803× (z -2.7, 9/27 lines)

**5 µM** (191 genes, none with an alert; 12 shown): [[EHD4]] 0.713× (z -7.1, 34/48 lines), [[TJP1]] 0.819× (z -6.2, 28/48 lines), [[EGR3]] 0.421× (z -5.9, 27/38 lines), [[KLF2]] 0.429× (z -5.8, 33/44 lines), [[CCN1]] 0.600× (z -5.7, 27/41 lines), [[CREB5]] 0.727× (z -5.6, 18/33 lines), [[SGMS2]] 0.648× (z -5.6, 31/43 lines), [[RHOB]] 0.608× (z -5.6, 37/47 lines), [[PITPNB]] 0.833× (z -5.5, 24/48 lines), [[MAP1B]] 0.758× (z -5.4, 23/32 lines), [[EGR1]] 0.501× (z -5.3, 42/46 lines), [[CCN2]] 0.567× (z -5.2, 14/31 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 025]] (-2.0) |
| 0.5 µM | — | — |
| 5 µM | [[Module 146]] (+5.1), [[Module 171]] (+3.7), [[Module 045]] (+3.6) | [[Module 184]] (-3.1), [[Module 160]] (-2.6), [[Module 109]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H661 (line)]] (1.54), [[H4 (line)]] (1.22), [[hTERT-HPNE (line)]] (1.19), [[Panc 03.27 (line)]] (1.10) · weakest: [[BT-474 (line)]] (0.282), [[RKO (line)]] (0.536), [[KATO III (line)]] (0.552) |
| 0.5 µM | — | [[SW 1088 (line)]] (1.70), [[CHP-212 (line)]] (1.35), [[NCI-H1573 (line)]] (1.20), [[hTERT-HPNE (line)]] (1.11) · weakest: [[SHP-77 (line)]] (0.341), [[C-33 A (line)]] (0.367), [[A-427 (line)]] (0.443) |
| 5 µM | — | [[KATO III (line)]] (1.81), [[H4 (line)]] (1.52), [[HOP62 (line)]] (1.27), [[NCI-H1573 (line)]] (1.24) · weakest: [[NCI-H661 (line)]] (0.476), [[SHP-77 (line)]] (0.597), [[NCI-H2347 (line)]] (0.602) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Ponatinib (drug)]] (+0.87, Multi-TK inhibitor); [[Regorafenib (drug)]] (+0.72, Multi-TK inhibitor); [[Afatinib (drug)]] (+0.72, EGFR/ERBB inhibitor); [[Radotinib (drug)]] (+0.71, Other TK inhibitor); [[Vandetanib (drug)]] (+0.68, Multi-TK inhibitor); [[Flumatinib (mesylate) (drug)]] (+0.63, Other TK inhibitor); [[Fostamatinib (disodium hexahydrate) (drug)]] (+0.60, Other TK inhibitor, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Cysteamine (hydrochloride) (drug)]] (+0.55, unclear); [[Mozavaptan (drug)]] (+0.47, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 11, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[BMPER]] | 5 µM | B | BMPER activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.16× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[CNRIP1]] | 5 µM | B | CNRIP1 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.12× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[RSPO3]] | 5 µM | B | RSPO3 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 1.20× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[GJA1]] | 5 µM | B | GJA1 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 1.13× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[ADAM12]] | 5 µM | B | ADAM12 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 1.16× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[SLC46A3]] | 5 µM | B | SLC46A3 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express SLC46A3 (11) vs lines expressing it (37) | the lines without SLC46A3: 1.19× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |
| [[PLBD1]] | 5 µM | B | PLBD1 activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express PLBD1 (24) vs lines expressing it (24) | the lines without PLBD1: 0.84× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, LINC01357, IKZF3 |
| [[PPP1R9A]] | 5 µM | B | PPP1R9A activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express PPP1R9A (16) vs lines expressing it (32) | the lines without PPP1R9A: 0.83× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.16× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.18× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.15× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ATAD1]], [[PTEN]] | 5 µM | C | ATAD1, PTEN activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.76× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| [[ZC3HAV1L]] | 5 µM | C | ZC3HAV1L activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 0.79× the cells of the other lines | 0.037 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| [[PTPN3]] | 5 µM | C | PTPN3 activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 0.75× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| [[VRK2]] | 5 µM | C | VRK2 activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.78× the cells of the other lines | 0.083 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| KDR | [[PPARD]] | moves it that way too | B | KDR activity raises PPARD's level | compounds that target KDR: 5 of 8 lower it (Cabozantinib, Ponatinib, Regorafenib, Sulfatinib, Sunitinib) | 62% of the class's compounds vs 6.2% of all compounds | 0.036 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MET]] | [[TNFAIP1]] | moves it that way too | B | MET activity raises TNFAIP1's level | compounds that target MET: 3 of 4 lower it (Cabozantinib, Crizotinib / crizotinib, c-Kit-IN-1) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| KDR | [[DNAJB6]] | moves it that way too | B | KDR activity raises DNAJB6's level | compounds that target KDR: 3 of 8 lower it (Cabozantinib, Ponatinib, c-Kit-IN-1) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| KDR | [[DUSP10]] | moves it that way too | B | KDR activity raises DUSP10's level | compounds that target KDR: 4 of 8 lower it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |
| KDR | [[PGLS-DT]] | moves it that way too | B | KDR activity lowers PGLS-DT's level | compounds that target KDR: 4 of 8 raise it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Cabozantinib (S-malate)"
- `tables/drugdoses.parquet` — dd in 227, 228, 229
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
