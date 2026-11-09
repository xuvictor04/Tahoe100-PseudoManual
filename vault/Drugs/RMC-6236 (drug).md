---
drug: "RMC-6236"
type: "drug"
salt_base: "RMC-6236"
targets: "KRAS"
moa_fine: "RAS inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 511
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# RMC-6236

*RAS inhibitor (inhibitor/antagonist) · targets: KRAS · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 30 / 34 / 511; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.46 / 0.62.
> Flags by dose: - / noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C10 | 25 / 5 | — | -0.19 | -1.5/-2.1/-1.7 | — |
| 0.5 µM | [[Plate 02]]:C10 | 15 / 19 | — | +0.61 | -1.3/-0.3/-0.6 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:C10 | 217 / 294 | — | +1.44 | -3.2/-1.6/-2.1 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (25 genes, none with an alert; 12 shown): [[AHI1-DT]] 1.48× (z +3.4, 8/47 lines), [[ADCY9]] 1.21× (z +3.3, 11/46 lines), [[DNAH5]] 1.37× (z +3.3, 14/38 lines), [[POT1-AS1]] 1.39× (z +3.3, 9/44 lines), [[TNS3]] 1.32× (z +3.2, 23/40 lines), [[ENSG00000287127]] 1.41× (z +3.1, 1/42 lines), [[C12orf60]] 1.32× (z +3.1, 5/45 lines), [[LINC00298]] 1.45× (z +3.1, 1/34 lines), [[SOX6]] 1.27× (z +3.1, 6/26 lines), [[MMADHC-DT]] 1.30× (z +3.1, 5/46 lines), [[LINC02646]] 1.48× (z +3.0, 6/45 lines), [[EFCAB2]] 1.21× (z +3.0, 6/48 lines)

**0.5 µM** (15 genes, none with an alert; 12 shown): [[CFB]] 1.87× (z +4.0, 16/28 lines), [[GBP2]] 1.55× (z +3.7, 14/36 lines), [[MTUS1-DT]] 1.82× (z +3.6, 4/29 lines), [[KRAS]] 1.22× (z +3.3, 20/49 lines), [[RHOB]] 1.51× (z +3.3, 19/48 lines), [[ENSG00000253671]] 1.90× (z +3.1, 2/29 lines), [[PGM2L1]] 1.21× (z +3.1, 4/45 lines), [[BMF]] 1.65× (z +3.0, 5/44 lines), [[TCTA]] 1.36× (z +2.9, 1/48 lines), [[OTUD1]] 1.33× (z +2.9, 0/47 lines), [[LINC02057]] 1.52× (z +2.9, 9/23 lines), [[TMEM140]] 1.54× (z +2.9, 4/40 lines)

**5 µM** (217 genes, none with an alert; 12 shown): [[PHLDB2]] 2.10× (z +6.4, 24/37 lines), [[DUSP16]] 1.68× (z +6.0, 34/46 lines), [[DST]] 1.85× (z +5.7, 35/46 lines), [[CLIP1]] 1.56× (z +5.6, 28/48 lines), [[KRAS]] 1.57× (z +5.6, 29/48 lines), [[GBP2]] 2.76× (z +5.6, 25/35 lines), [[ARID5B]] 1.89× (z +5.1, 29/42 lines), [[MYOF]] 1.58× (z +5.0, 30/42 lines), [[TLE1]] 1.48× (z +5.0, 18/46 lines), [[AGTPBP1]] 1.53× (z +4.9, 24/45 lines), [[STK38]] 1.34× (z +4.8, 20/48 lines), [[RHOB]] 2.26× (z +4.7, 28/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[FOSL1]] 0.717× (z -3.1, 20/43 lines), [[RAB3B]] 0.827× (z -2.9, 0/31 lines), [[EGR1]] 0.677× (z -2.8, 20/46 lines), [[ETV1]] 0.771× (z -2.8, 10/37 lines), [[PLAUR]] 0.804× (z -2.6, 11/38 lines)

**0.5 µM** (19 genes, none with an alert; 12 shown): [[ETV5]] 0.670× (z -5.3, 26/49 lines), [[SPRY4]] 0.608× (z -4.6, 28/49 lines), [[ZFPM2-AS1]] 0.764× (z -3.4, 14/33 lines), [[PRAG1]] 0.825× (z -3.3, 5/33 lines), [[EPHA2]] 0.750× (z -3.2, 11/38 lines), [[MCTP1]] 0.765× (z -3.2, 12/36 lines), [[ETV4]] 0.735× (z -3.1, 10/46 lines), [[SPRED2]] 0.765× (z -3.0, 25/49 lines), [[ITGB5]] 0.787× (z -3.0, 16/47 lines), [[MYEOV]] 0.699× (z -2.9, 7/29 lines), [[DUSP5]] 0.723× (z -2.9, 10/42 lines), [[ETV1]] 0.717× (z -2.8, 10/37 lines)

**5 µM** (294 genes, none with an alert; 12 shown): [[ETV5]] 0.177× (z -12.4, 43/48 lines), [[ETV1]] 0.137× (z -9.9, 33/37 lines), [[SPRY4-AS1]] 0.167× (z -9.7, 43/45 lines), [[ZFPM2-AS1]] 0.338× (z -9.0, 30/32 lines), [[ENSG00000260877]] 0.188× (z -8.7, 28/34 lines), [[SPRY4]] 0.127× (z -8.7, 45/48 lines), [[CCND1]] 0.315× (z -8.5, 38/41 lines), [[DUSP4]] 0.338× (z -8.1, 30/33 lines), [[MYEOV]] 0.263× (z -8.0, 25/29 lines), [[SPRED1]] 0.398× (z -7.3, 42/48 lines), [[DUSP6]] 0.107× (z -7.2, 43/44 lines), [[EGR1]] 0.112× (z -7.2, 46/46 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 230]] (+2.2) | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 234]] (+2.7), [[Module 194]] (+2.1), [[Module 232]] (+2.0) | [[Module 174]] (-3.4), [[Module 092]] (-3.3), [[Module 158]] (-2.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H661 (line)]] (1.96), [[Hs 766T (line)]] (1.44), [[MIA PaCa-2 (line)]] (1.25), [[NCI-H23 (line)]] (1.24) · weakest: [[CHP-212 (line)]] (-0.107), [[A-172 (line)]] (0.341), [[hTERT-HPNE (line)]] (0.422) |
| 0.5 µM | [[NCI-H1792 (line)]] (-4.1) | [[AsPC-1 (line)]] (1.76), [[HOP62 (line)]] (1.48), [[A549 (line)]] (1.36), [[SW 900 (line)]] (1.36) · weakest: [[NCI-H2122 (line)]] (0.256), [[CHP-212 (line)]] (0.308), [[SW48 (line)]] (0.370) |
| 5 µM | [[NCI-H1792 (line)]] (-15.4), [[CHP-212 (line)]] (-7.7), [[SK-MEL-2 (line)]] (-6.6), [[NCI-H23 (line)]] (-4.1), [[Panc 03.27 (line)]] (-3.6) | [[HOP62 (line)]] (1.42), [[H4 (line)]] (1.35), [[NCI-H1573 (line)]] (1.33), [[NCI-H23 (line)]] (1.29) · weakest: [[CHP-212 (line)]] (0.411), [[SW1417 (line)]] (0.724), [[NCI-H661 (line)]] (0.760) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[BI-3406 (drug)]] (+0.88, RAS inhibitor); [[Trametinib (drug)]] (+0.82, MEK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Bimiralisib (drug)]] (+0.81, PI3K/AKT inhibitor); [[Binimetinib (drug)]] (+0.73, MEK inhibitor); [[Trametinib (DMSO_TF solvate) (drug)]] (+0.70, MEK inhibitor); [[Cobimetinib (drug)]] (+0.67, MEK inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.65, unclear); [[Perindopril (erbumine) (drug)]] (+0.57, unclear); [[Capmatinib (drug)]] (+0.44, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PLEKHG2]] | 5 µM | B | PLEKHG2 activity raises the cells' numbers under RMC-6236 5 µM (protects the cells) | lines that do not express PLEKHG2 (10) vs lines expressing it (38) | the lines without PLEKHG2: 0.87× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000225689; maybe low, not absent |
| [[PYGB]] | 5 µM | C | PYGB activity raises the cells' numbers under RMC-6236 5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.50× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[KRAS]] | [[MFSD2A]] | moves it that way too | B | KRAS activity raises MFSD2A's level | compounds that target KRAS: 3 of 4 lower it (BI-3406, Lonafarnib, RMC-6236) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

## Data

- `tables/drugs.parquet` — drug == "RMC-6236"
- `tables/drugdoses.parquet` — dd in 860, 861, 862
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
