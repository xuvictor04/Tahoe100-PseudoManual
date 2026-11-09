---
drug: "Arbutin"
type: "drug"
salt_base: "Arbutin"
targets: "MYC, KLF4"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 215
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Arbutin

*unclear (inhibitor/antagonist) · targets: MYC, KLF4 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 107 / 32 / 215; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.61 / -0.17.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:G12 | 98 / 9 | — | -0.14 | +0.1/+0.7/-1.0 | — |
| 0.5 µM | [[Plate 08]]:G12 | 25 / 7 | — | -0.10 | +0.2/-0.3/-0.6 | — |
| 5 µM | [[Plate 09]]:G12 | 130 / 85 | — | +0.17 | +1.8/+1.8/+2.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (98 genes, none with an alert; 12 shown): [[RPL18A]] 2.17× (z +5.9, 37/46 lines), [[COL4A1]] 1.41× (z +5.3, 14/19 lines), [[PDE10A]] 1.26× (z +4.3, 12/24 lines), [[TGFBR3]] 1.30× (z +4.2, 9/41 lines), [[ENSG00000241489]] 1.44× (z +4.2, 18/46 lines), [[COL4A2]] 1.26× (z +4.1, 10/23 lines), [[PDE4B]] 1.34× (z +4.1, 5/24 lines), [[SYTL4]] 1.27× (z +4.0, 5/36 lines), [[FBN1]] 1.32× (z +4.0, 10/20 lines), [[SNED1]] 1.38× (z +4.0, 14/39 lines), [[FANCL]] 1.24× (z +4.0, 23/48 lines), [[ANK3]] 1.27× (z +4.0, 12/24 lines)

**0.5 µM** (25 genes, none with an alert; 12 shown): [[FANCL]] 1.22× (z +3.9, 19/48 lines), [[CRYZL2P]] 1.49× (z +3.8, 7/34 lines), [[ADAM22]] 1.28× (z +3.7, 6/36 lines), [[ARRB1]] 1.22× (z +3.7, 9/46 lines), [[TGFBR3]] 1.23× (z +3.7, 5/41 lines), [[PDE10A]] 1.20× (z +3.7, 11/24 lines), [[ZNF618]] 1.37× (z +3.4, 7/38 lines), [[PLPP3]] 1.24× (z +3.4, 11/43 lines), [[CACNA1D]] 1.25× (z +3.4, 5/24 lines), [[MORN1]] 1.31× (z +3.4, 7/47 lines), [[SNED1]] 1.28× (z +3.3, 10/40 lines), [[LINC01013]] 1.41× (z +3.3, 4/40 lines)

**5 µM** (130 genes, none with an alert; 12 shown): [[ENSG00000235979]] 1.79× (z +4.3, 20/44 lines), [[TUBA1B]] 1.70× (z +4.0, 44/47 lines), [[NCAM2]] 1.32× (z +4.0, 2/21 lines), [[BCL2L14]] 1.49× (z +3.9, 23/46 lines), [[HOXA5]] 1.70× (z +3.9, 15/36 lines), [[ATP1B1]] 1.29× (z +3.8, 29/40 lines), [[VASN]] 1.45× (z +3.8, 6/38 lines), [[SNF8]] 1.28× (z +3.8, 15/47 lines), [[POLR2L]] 1.98× (z +3.7, 42/48 lines), [[THSD4-AS1]] 1.71× (z +3.7, 23/46 lines), [[BID]] 1.26× (z +3.7, 10/45 lines), [[PPA1]] 1.24× (z +3.7, 12/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (9 genes, none with an alert): [[ENSG00000237550]] 0.586× (z -4.0, 17/44 lines), [[GRPEL2]] 0.771× (z -3.5, 16/47 lines), [[TMEM167B]] 0.819× (z -3.4, 16/48 lines), [[SLC31A1]] 0.745× (z -3.4, 24/48 lines), [[LRATD2]] 0.800× (z -3.4, 4/31 lines), [[PRNP]] 0.825× (z -3.2, 8/45 lines), [[RHEB]] 0.829× (z -3.1, 18/48 lines), [[ENSG00000291079]] 0.785× (z -2.9, 4/37 lines), [[XBP1]] 0.832× (z -2.9, 12/47 lines)

**0.5 µM** (7 genes, none with an alert): [[CLDN1]] 0.798× (z -4.1, 1/25 lines), [[CHMP4C]] 0.798× (z -3.6, 15/32 lines), [[H4C3]] 0.552× (z -3.6, 31/47 lines), [[GRPEL2]] 0.804× (z -3.5, 13/47 lines), [[UPP1]] 0.719× (z -3.4, 23/39 lines), [[ADTRP]] 0.706× (z -3.4, 3/22 lines), [[KLF11]] 0.816× (z -3.4, 7/46 lines)

**5 µM** (85 genes, none with an alert; 12 shown): [[PLCG2]] 0.757× (z -4.4, 13/38 lines), [[ZNF701]] 0.789× (z -4.1, 10/40 lines), [[TGIF1]] 0.814× (z -4.1, 14/48 lines), [[RHBDF1]] 0.673× (z -4.0, 18/45 lines), [[RIPOR1]] 0.761× (z -3.9, 17/46 lines), [[CTIF]] 0.778× (z -3.9, 25/48 lines), [[CAMTA2]] 0.750× (z -3.9, 16/47 lines), [[GSDME]] 0.814× (z -3.8, 5/33 lines), [[ZSCAN9]] 0.769× (z -3.7, 13/46 lines), [[PICK1]] 0.769× (z -3.7, 9/42 lines), [[GDPD5]] 0.761× (z -3.6, 5/42 lines), [[ZNF516]] 0.755× (z -3.6, 24/43 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 048]] (+2.5), [[Module 054]] (+2.4), [[Module 059]] (+2.3) | [[Module 170]] (-2.7) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[AN3 CA (line)]] (1.45), [[Panc 03.27 (line)]] (1.15), [[C-33 A (line)]] (1.11), [[AsPC-1 (line)]] (1.08) · weakest: [[MIA PaCa-2 (line)]] (0.543), [[SK-MEL-2 (line)]] (0.619), [[HOP62 (line)]] (0.698) |
| 0.5 µM | — | [[SHP-77 (line)]] (1.40), [[SW 1271 (line)]] (1.33), [[SNU-1 (line)]] (1.30), [[NCI-H23 (line)]] (1.17) · weakest: [[CFPAC-1 (line)]] (0.545), [[Hs 766T (line)]] (0.604), [[SW1417 (line)]] (0.615) |
| 5 µM | — | [[A498 (line)]] (1.12), [[NCI-H2030 (line)]] (1.10), [[HS-578T (line)]] (1.09), [[A549 (line)]] (1.07) · weakest: [[SHP-77 (line)]] (0.734), [[RKO (line)]] (0.812), [[SK-MEL-2 (line)]] (0.831) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Silodosin (drug)]] (+0.81, unclear); [[Altretamine (drug)]] (+0.73, DNA synthesis/repair inhibitor, ⚠ only 1 significant gene); [[Bendamustine (drug)]] (+0.72, DNA synthesis/repair inhibitor); [[Sulfatinib (drug)]] (+0.70, Multi-TK inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.66, unclear); [[Azithromycin (hydrate) (drug)]] (+0.60, unclear); [[CP21R7 (drug)]] (+0.56, GSK3 inhibitor, ⚠ only 1 significant gene); [[Tetracycline (hydrochloride) (drug)]] (+0.56, unclear, ⚠ only 6 significant genes); [[Bicalutamide (drug)]] (+0.54, Androgen receptor antagonist); [[Decitabine (drug)]] (+0.54, DNA methyltransferase inhibitor); [[Aliskiren (drug)]] (+0.50, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 22 arrows, 22 of them with an alert ⚠; grade A 0, B 17, C 5. Shown: the 15 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SLFN5]] | 5 µM | B | SLFN5 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.78× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[PTGS2]] | 5 µM | B | PTGS2 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express PTGS2 (27) vs lines expressing it (21) | the lines without PTGS2: 0.81× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[PAPPA]] | 5 µM | B | PAPPA activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.79× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[F2RL2]] | 5 µM | B | F2RL2 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express F2RL2 (32) vs lines expressing it (16) | the lines without F2RL2: 0.77× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| [[PLA2G4A]] | 5 µM | B | PLA2G4A activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 0.85× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| [[ZNF469]] | 5 µM | B | ZNF469 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express ZNF469 (20) vs lines expressing it (28) | the lines without ZNF469: 0.78× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |
| [[LINC02057]] | 5 µM | B | LINC02057 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express LINC02057 (25) vs lines expressing it (23) | the lines without LINC02057: 0.78× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[GLIS3]] | 5 µM | B | GLIS3 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express GLIS3 (21) vs lines expressing it (27) | the lines without GLIS3: 0.81× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[KIAA1217]] | 5 µM | B | KIAA1217 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express KIAA1217 (10) vs lines expressing it (38) | the lines without KIAA1217: 0.79× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: FAM107B, MET, S100A16 |
| [[IL6]] | 5 µM | B | IL6 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express IL6 (32) vs lines expressing it (16) | the lines without IL6: 0.78× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[ENSG00000259354]], [[HMGN2P46]] | 5 µM | B | ENSG00000259354, HMGN2P46 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express ENSG00000259354, HMGN2P46 (18) vs lines expressing them (30) | the lines without ENSG00000259354, HMGN2P46: 0.81× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: C15orf48, IL1R1, STAC; co-absent genes |
| [[BASP1]] | 5 µM | B | BASP1 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express BASP1 (24) vs lines expressing it (24) | the lines without BASP1: 0.80× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |
| [[STAC]] | 5 µM | B | STAC activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express STAC (25) vs lines expressing it (23) | the lines without STAC: 0.82× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[PSD4]] | 5 µM | B | PSD4 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express PSD4 (8) vs lines expressing it (40) | the lines without PSD4: 0.75× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TBILA, SH2D4A, GPR39 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.80× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Arbutin"
- `tables/drugdoses.parquet` — dd in 102, 103, 104
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
