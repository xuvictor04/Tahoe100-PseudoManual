---
drug: "XRK3F2"
type: "drug"
salt_base: "XRK3F2"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 1745
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# XRK3F2

*unclear (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 19 / 1745 / 40; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.32 / -0.54.
> Flags by dose: - / low cells (technical?); plate-row cell shift; noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:D10 | 7 / 12 | — | +0.00 | -1.8/-1.4/-1.5 | — |
| 0.5 µM | [[Plate 02]]:D10 | 1,460 / 285 | — | -2.24 | -0.8/+0.4/+2.4 | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:D10 | 20 / 20 | — | +1.23 | -1.5/-1.2/-2.1 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[CFB]] 1.52× (z +3.4, 13/28 lines), [[ENSG00000291159]] 1.34× (z +3.4, 2/43 lines), [[ENSG00000287127]] 1.42× (z +3.2, 2/42 lines), [[DCAF4]] 1.20× (z +3.2, 4/48 lines), [[GBP2]] 1.32× (z +3.0, 5/35 lines), [[SH3BGR]] 1.25× (z +2.7, 1/45 lines), [[CABLES1]] 1.21× (z +2.7, 7/42 lines)

**0.5 µM** (1460 genes, none with an alert; 12 shown): [[DUSP28]] 1.89× (z +5.8, 7/23 lines), [[DRG2]] 1.61× (z +5.8, 16/43 lines), [[COPS5]] 1.46× (z +5.6, 26/45 lines), [[PLEKHA3]] 1.32× (z +5.6, 22/47 lines), [[EPHA7]] 2.37× (z +5.6, 0/11 lines), [[RFLNA]] 1.34× (z +5.5, 27/47 lines), [[ZNF667-AS1]] 2.45× (z +5.4, 1/9 lines), [[RNF141]] 1.48× (z +5.4, 22/44 lines), [[YBX2]] 2.91× (z +5.3, 1/10 lines), [[PPM1M]] 2.37× (z +5.3, 4/12 lines), [[ATXN7L3]] 1.42× (z +5.3, 22/45 lines), [[GPRIN2]] 2.75× (z +5.3, 2/10 lines)

**5 µM** (20 genes, none with an alert; 12 shown): [[BMPR2]] 1.35× (z +4.6, 31/48 lines), [[TULP4]] 1.40× (z +3.9, 24/48 lines), [[FOXN3]] 1.35× (z +3.7, 15/46 lines), [[ARID1B]] 1.38× (z +3.6, 33/47 lines), [[KANSL1L]] 1.41× (z +3.5, 12/48 lines), [[HDAC9]] 1.41× (z +3.4, 13/39 lines), [[NDUFAF6]] 1.37× (z +3.3, 9/48 lines), [[SKIL]] 1.44× (z +3.3, 21/46 lines), [[ZBTB20]] 1.46× (z +3.2, 26/48 lines), [[TNS3]] 1.63× (z +3.2, 22/40 lines), [[BCAS3]] 1.39× (z +3.1, 24/48 lines), [[CUX1]] 1.28× (z +3.1, 21/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (12 genes, none with an alert): [[LINC02476]] 0.688× (z -3.7, 0/8 lines), [[LINC00888]] 0.656× (z -3.5, 7/33 lines), [[SPRY4]] 0.750× (z -3.5, 16/48 lines), [[SLC45A1]] 0.641× (z -3.4, 4/23 lines), [[ENSG00000249803]] 0.636× (z -3.4, 1/11 lines), [[CEACAM6]] 0.682× (z -3.3, 0/11 lines), [[ETV4]] 0.767× (z -3.3, 6/46 lines), [[TMPRSS4]] 0.715× (z -3.2, 0/15 lines), [[EPHA2]] 0.822× (z -2.9, 10/37 lines), [[PRSS3]] 0.791× (z -2.8, 0/18 lines), [[DUSP5]] 0.794× (z -2.7, 6/41 lines), [[TGFA]] 0.816× (z -2.5, 2/31 lines)

**0.5 µM** (285 genes, none with an alert; 12 shown): [[STK4]] 0.760× (z -7.4, 32/47 lines), [[IQCB1]] 0.744× (z -6.5, 27/47 lines), [[ENSG00000291228]] 0.513× (z -6.1, 27/42 lines), [[LRRC1]] 0.667× (z -5.5, 23/43 lines), [[RBFOX2]] 0.773× (z -5.2, 35/47 lines), [[MRE11]] 0.736× (z -5.2, 23/47 lines), [[SMC5]] 0.771× (z -5.1, 32/47 lines), [[MAP3K1]] 0.731× (z -5.0, 22/47 lines), [[NAA35]] 0.742× (z -5.0, 27/47 lines), [[WAPL]] 0.813× (z -4.8, 25/47 lines), [[UBE2Q2P2]] 0.695× (z -4.8, 26/47 lines), [[DBF4B]] 0.702× (z -4.8, 18/44 lines)

**5 µM** (20 genes, none with an alert; 12 shown): [[STC1]] 0.492× (z -3.4, 10/24 lines), [[NLRP3]] 0.434× (z -3.4, 3/19 lines), [[CLMP]] 0.522× (z -3.4, 6/23 lines), [[LCK]] 0.405× (z -3.3, 3/14 lines), [[CCND2]] 0.584× (z -3.3, 0/11 lines), [[MAL2]] 0.710× (z -3.2, 0/17 lines), [[LINC00973]] 0.428× (z -3.0, 2/23 lines), [[SFRP1]] 0.571× (z -3.0, 1/16 lines), [[HS3ST1]] 0.639× (z -3.0, 0/17 lines), [[PLAU]] 0.567× (z -3.0, 4/22 lines), [[CLDN10-AS1]] 0.492× (z -2.9, 2/15 lines), [[TNFRSF10A]] 0.727× (z -2.9, 8/38 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 059]] (+2.8), [[Module 002]] (+2.7), [[Module 095]] (+2.6) | [[Module 018]] (-2.5), [[Module 077]] (-2.2) |
| 5 µM | [[Module 230]] (+2.0) | [[Module 048]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[C32 (line)]] (-3.2) | [[SW 1271 (line)]] (1.70), [[CHP-212 (line)]] (1.54), [[SW 1088 (line)]] (1.52), [[HCT15 (line)]] (1.37) · weakest: [[NCI-H2347 (line)]] (0.590), [[SW480 (line)]] (0.609), [[NCI-H460 (line)]] (0.669) |
| 5 µM | [[NCI-H1792 (line)]] (-4.2), [[Panc 03.27 (line)]] (-3.9), [[MIA PaCa-2 (line)]] (-3.5), [[LOX-IMVI (line)]] (-3.4), [[CHP-212 (line)]] (-3.4) | [[HCT15 (line)]] (1.53), [[MIA PaCa-2 (line)]] (1.46), [[AsPC-1 (line)]] (1.39), [[PANC-1 (line)]] (1.38) · weakest: [[A-172 (line)]] (0.482), [[RPMI-7951 (line)]] (0.506), [[J82 (line)]] (0.559) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[9-ING-41 (drug)]] (+0.87, GSK3 inhibitor); [[LY-2584702 (tosylate salt) (drug)]] (+0.82, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Alpelisib (drug)]] (+0.76, PI3K/AKT inhibitor); [[BI-78D3 (drug)]] (+0.75, Other MAPK inhibitor); [[Canagliflozin (drug)]] (+0.74, Glucose transporter inhibitor); [[DT-061 (drug)]] (+0.73, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.71, Glucose transporter inhibitor); [[Docetaxel (drug)]] (+0.71, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[Pyridoxine (drug)]] (+0.71, unclear); [[Capmatinib (drug)]] (+0.67, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000259200]] | 5 µM | B | ENSG00000259200 activity raises the cells' numbers under XRK3F2 5 µM (protects the cells) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 0.76× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[ENSG00000258919]] | 0.5 µM | B | ENSG00000258919 activity lowers the cells' numbers under XRK3F2 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000258919 (23) vs lines expressing it (25) | the lines without ENSG00000258919: 1.19× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: LINC02320, ENSG00000266088, DIO3OS |
| [[RSPO3]] | 5 µM | B | RSPO3 activity raises the cells' numbers under XRK3F2 5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.80× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[ADAMTS10]] | 0.5 µM | B | ADAMTS10 activity raises the cells' numbers under XRK3F2 0.5 µM (protects the cells) | lines that do not express ADAMTS10 (27) vs lines expressing it (21) | the lines without ADAMTS10: 0.88× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| [[VAV3]] | 5 µM | B | VAV3 activity raises the cells' numbers under XRK3F2 5 µM (protects the cells) | lines that do not express VAV3 (30) vs lines expressing it (18) | the lines without VAV3: 0.84× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM |
| [[PYGB]] | 5 µM | C | PYGB activity raises the cells' numbers under XRK3F2 5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.65× the cells of the other lines | 0.076 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| [[ISG20]] | 5 µM | C | ISG20 activity raises the cells' numbers under XRK3F2 5 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.69× the cells of the other lines | 0.093 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| [[ENSG00000240571]] | 5 µM | C | ENSG00000240571's natural level raises the cells' numbers under XRK3F2 5 µM (protects the cells) | ENSG00000240571's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71 | 0.260 over the table, 0.025 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[TMEM214]] | 5 µM | C | TMEM214's natural level raises the cells' numbers under XRK3F2 5 µM (protects the cells) | TMEM214's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.327 over the table, 0.071 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "XRK3F2"
- `tables/drugdoses.parquet` — dd in 1105, 1106, 1107
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
